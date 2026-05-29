"""
PandaMania Test Configuration
pytest fixtures and test helpers for AIML testing
"""

import os
import sys
import glob
import pytest
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


@dataclass
class AIMLPattern:
    """Represents an AIML pattern"""
    pattern: str
    template: str
    topic: str = ""
    that: str = ""
    file: str = ""
    
    @property
    def normalized_pattern(self) -> str:
        """Return normalized pattern text (uppercase, stripped)"""
        return self.pattern.upper().strip()


@dataclass
class AIMLResponse:
    """Represents a response from the AIML interpreter"""
    input: str
    response: str
    variables: Dict[str, str]
    topic: str = ""


class MockAIMLInterpreter:
    """
    Mock AIML interpreter for testing when python-aiml is not available.
    Provides basic pattern matching without full AIML semantics.
    """
    
    def __init__(self):
        self.patterns: Dict[str, AIMLPattern] = {}
        self.variables: Dict[str, str] = {}
        self.topic: str = ""
        self._loaded_files: List[str] = []
        self._srai_cache: Dict[str, str] = {}
        
    def load_file(self, filepath: str) -> int:
        """Load patterns from an AIML file"""
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            count = 0
            
            for category in root.findall('.//category'):
                pattern_elem = category.find('pattern')
                template_elem = category.find('template')
                that_elem = category.find('that')
                
                if pattern_elem is not None and template_elem is not None:
                    pattern_text = self._get_element_text(pattern_elem).upper().strip()
                    template_text = self._serialize_template(template_elem)
                    that_text = self._get_element_text(that_elem).strip() if that_elem is not None else ""
                    
                    # Get topic from parent
                    topic = ""
                    parent = category
                    # Note: ElementTree doesn't have getparent, so we track it during iteration
                    
                    self.patterns[pattern_text] = AIMLPattern(
                        pattern=pattern_text,
                        template=template_text,
                        topic=topic,
                        that=that_text,
                        file=filepath
                    )
                    count += 1
            
            self._loaded_files.append(filepath)
            return count
        except Exception as e:
            raise RuntimeError(f"Failed to load {filepath}: {e}")
    
    def _get_element_text(self, elem) -> str:
        """Get all text content from an element"""
        return ''.join(elem.itertext())
    
    def _serialize_template(self, template_elem) -> str:
        """Serialize template element to string"""
        return ET.tostring(template_elem, encoding='unicode', method='xml')
    
    def respond(self, input_text: str) -> str:
        """Generate a response for the input"""
        normalized = input_text.upper().strip()
        
        # Direct pattern match
        if normalized in self.patterns:
            return self._process_template(self.patterns[normalized].template)
        
        # Wildcard matching (simplified)
        for pattern, aiml_pattern in self.patterns.items():
            if self._matches_pattern(normalized, pattern):
                return self._process_template(aiml_pattern.template)
        
        return "I don't understand."
    
    def _matches_pattern(self, input_text: str, pattern: str) -> bool:
        """Simple pattern matching with wildcards"""
        if pattern == input_text:
            return True
        
        # Handle * wildcard
        if '*' in pattern:
            parts = pattern.split('*')
            if len(parts) == 2:
                prefix, suffix = parts
                prefix = prefix.strip()
                suffix = suffix.strip()
                if prefix and suffix:
                    return input_text.startswith(prefix) and input_text.endswith(suffix)
                elif prefix:
                    return input_text.startswith(prefix)
                elif suffix:
                    return input_text.endswith(suffix)
                else:
                    return True  # Pattern is just "*"
        
        return False
    
    def _process_template(self, template: str) -> str:
        """Process template to generate response (simplified)"""
        # Strip XML tags for basic response
        import re
        # Remove <think>...</think> blocks
        template = re.sub(r'<think>.*?</think>', '', template, flags=re.DOTALL)
        # Remove <set>...</set> but extract for variables
        set_matches = re.findall(r'<set name="(\w+)">([^<]*)</set>', template)
        for name, value in set_matches:
            self.variables[name] = value
        template = re.sub(r'<set[^>]*>.*?</set>', '', template, flags=re.DOTALL)
        # Handle <get name="..."/>
        def replace_get(match):
            name = match.group(1)
            return self.variables.get(name, '')
        template = re.sub(r'<get name="(\w+)"\s*/>', replace_get, template)
        # Handle <srai>...</srai>
        srai_match = re.search(r'<srai>([^<]+)</srai>', template)
        if srai_match:
            srai_target = srai_match.group(1).strip()
            if srai_target not in self._srai_cache:
                self._srai_cache[srai_target] = self.respond(srai_target)
            srai_response = self._srai_cache[srai_target]
            template = re.sub(r'<srai>[^<]+</srai>', srai_response, template, count=1)
        # Remove remaining XML tags
        template = re.sub(r'<[^>]+>', '', template)
        # Clean up whitespace
        template = ' '.join(template.split())
        return template.strip()
    
    def set_variable(self, name: str, value: str):
        """Set a session variable"""
        self.variables[name] = value
    
    def get_variable(self, name: str) -> Optional[str]:
        """Get a session variable"""
        return self.variables.get(name)
    
    def set_topic(self, topic: str):
        """Set the current topic"""
        self.topic = topic
    
    def reset(self):
        """Reset interpreter state"""
        self.variables.clear()
        self.topic = ""
        self._srai_cache.clear()


# Try to import real AIML interpreter
try:
    import aiml
    AIML_AVAILABLE = True
except ImportError:
    AIML_AVAILABLE = False


def create_aiml_interpreter():
    """Create an AIML interpreter (real or mock)"""
    if AIML_AVAILABLE:
        kernel = aiml.Kernel()
        kernel.verbose(False)
        return kernel
    else:
        return MockAIMLInterpreter()


# ============================================
# PYTEST FIXTURES
# ============================================

@pytest.fixture(scope="session")
def project_root() -> Path:
    """Return the project root directory"""
    return PROJECT_ROOT


@pytest.fixture(scope="session")
def aiml_files(project_root) -> List[str]:
    """Return list of all AIML files in the project"""
    return sorted(glob.glob(str(project_root / "*.aiml")))


@pytest.fixture(scope="session")
def aiml_patterns(aiml_files) -> Dict[str, AIMLPattern]:
    """Parse and return all patterns from AIML files"""
    patterns = {}
    
    for filepath in aiml_files:
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            
            for category in root.findall('.//category'):
                pattern_elem = category.find('pattern')
                template_elem = category.find('template')
                that_elem = category.find('that')
                
                if pattern_elem is not None and template_elem is not None:
                    pattern_text = ''.join(pattern_elem.itertext()).upper().strip()
                    template_text = ET.tostring(template_elem, encoding='unicode')
                    that_text = ''.join(that_elem.itertext()).strip() if that_elem is not None else ""
                    
                    patterns[pattern_text] = AIMLPattern(
                        pattern=pattern_text,
                        template=template_text,
                        topic="",
                        that=that_text,
                        file=os.path.basename(filepath)
                    )
        except Exception as e:
            pytest.fail(f"Failed to parse {filepath}: {e}")
    
    return patterns


@pytest.fixture(scope="session")
def bot_properties(project_root) -> Dict[str, str]:
    """Load bot.properties file"""
    properties = {}
    prop_file = project_root / "bot.properties"
    
    if prop_file.exists():
        with open(prop_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and ':' in line:
                    key, value = line.split(':', 1)
                    properties[key.strip()] = value.strip()
    
    return properties


@pytest.fixture(scope="function")
def aiml_interpreter(aiml_files) -> MockAIMLInterpreter:
    """
    Create and load AIML interpreter for testing.
    Uses mock interpreter that doesn't require python-aiml.
    """
    interpreter = MockAIMLInterpreter()
    
    # Load all AIML files
    for filepath in aiml_files:
        interpreter.load_file(filepath)
    
    return interpreter


@pytest.fixture(scope="function")
def fresh_interpreter(aiml_files) -> MockAIMLInterpreter:
    """Create a fresh interpreter for each test"""
    interpreter = MockAIMLInterpreter()
    for filepath in aiml_files:
        interpreter.load_file(filepath)
    return interpreter


# ============================================
# TEST HELPERS
# ============================================

def assert_response_contains(response: str, expected: str, case_sensitive: bool = False):
    """Assert that response contains expected text"""
    if case_sensitive:
        assert expected in response, f"Expected '{expected}' in response: {response}"
    else:
        assert expected.lower() in response.lower(), f"Expected '{expected}' (case-insensitive) in response: {response}"


def assert_response_matches_any(response: str, expected_list: List[str], case_sensitive: bool = False):
    """Assert that response contains at least one of the expected texts"""
    response_check = response if case_sensitive else response.lower()
    for expected in expected_list:
        expected_check = expected if case_sensitive else expected.lower()
        if expected_check in response_check:
            return
    pytest.fail(f"Expected one of {expected_list} in response: {response}")


def get_pattern_categories(patterns: Dict[str, AIMLPattern]) -> Dict[str, List[str]]:
    """Group patterns by source file"""
    categories = {}
    for pattern_text, pattern in patterns.items():
        file = pattern.file
        if file not in categories:
            categories[file] = []
        categories[file].append(pattern_text)
    return categories


# ============================================
# PYTEST MARKERS
# ============================================

def pytest_configure(config):
    """Register custom markers"""
    config.addinivalue_line("markers", "e2e: mark test as end-to-end test")
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line("markers", "metacognition: mark test as meta-cognition test")
    config.addinivalue_line("markers", "autognosis: mark test as autognosis test")
    config.addinivalue_line("markers", "holistic: mark test as holistic metamodel test")
    config.addinivalue_line("markers", "learning: mark test as learning system test")
    config.addinivalue_line("markers", "domain: mark test as domain knowledge test")
    config.addinivalue_line("markers", "conversation: mark test as conversation flow test")
    config.addinivalue_line("markers", "performance: mark test as performance benchmark")
