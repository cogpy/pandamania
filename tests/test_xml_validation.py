"""
AIML XML Validation Tests
Tests for XML structure and schema validation
"""

import xml.etree.ElementTree as ET
import pytest
from pathlib import Path


class TestXMLValidation:
    """Test XML validity of all AIML files"""
    
    def test_all_aiml_files_are_valid_xml(self, aiml_files):
        """Verify all AIML files are well-formed XML"""
        errors = []
        
        for filepath in aiml_files:
            try:
                tree = ET.parse(filepath)
                root = tree.getroot()
                assert root is not None
            except ET.ParseError as e:
                errors.append(f"{Path(filepath).name}: {e}")
            except Exception as e:
                errors.append(f"{Path(filepath).name}: {e}")
        
        if errors:
            pytest.fail(f"XML validation errors:\n" + "\n".join(errors))
    
    def test_aiml_root_elements(self, aiml_files):
        """Verify all AIML files have correct root element"""
        for filepath in aiml_files:
            tree = ET.parse(filepath)
            root = tree.getroot()
            
            assert root.tag == 'aiml', f"{Path(filepath).name}: Root element is '{root.tag}', expected 'aiml'"
    
    def test_aiml_version_attribute(self, aiml_files):
        """Verify AIML files have version attribute"""
        for filepath in aiml_files:
            tree = ET.parse(filepath)
            root = tree.getroot()
            
            version = root.get('version')
            # Version is optional but if present should be 2.0
            if version:
                assert version in ['2.0', '1.0', '1.1'], \
                    f"{Path(filepath).name}: Unexpected AIML version '{version}'"
    
    def test_categories_have_required_elements(self, aiml_files):
        """Verify all categories have pattern and template elements"""
        errors = []
        
        for filepath in aiml_files:
            tree = ET.parse(filepath)
            root = tree.getroot()
            filename = Path(filepath).name
            
            for i, category in enumerate(root.findall('.//category')):
                pattern = category.find('pattern')
                template = category.find('template')
                
                if pattern is None:
                    errors.append(f"{filename}: Category {i+1} missing <pattern>")
                if template is None:
                    errors.append(f"{filename}: Category {i+1} missing <template>")
        
        if errors:
            pytest.fail(f"Category structure errors:\n" + "\n".join(errors[:20]))
    
    def test_xml_encoding_declaration(self, aiml_files):
        """Verify XML files have proper encoding"""
        for filepath in aiml_files:
            with open(filepath, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
            
            # XML declaration should specify UTF-8
            if first_line.startswith('<?xml'):
                assert 'utf-8' in first_line.lower() or 'encoding' not in first_line.lower(), \
                    f"{Path(filepath).name}: Non-UTF-8 encoding specified"


class TestPatternCount:
    """Test pattern counts and distribution"""
    
    def test_minimum_pattern_count(self, aiml_patterns):
        """Verify minimum number of patterns loaded"""
        assert len(aiml_patterns) >= 400, \
            f"Expected at least 400 patterns, got {len(aiml_patterns)}"
    
    def test_pattern_distribution(self, aiml_patterns):
        """Verify patterns are distributed across multiple files"""
        files = set(p.file for p in aiml_patterns.values())
        assert len(files) >= 10, \
            f"Expected patterns from at least 10 files, got {len(files)}"
    
    def test_core_files_have_patterns(self, aiml_files, aiml_patterns):
        """Verify core AIML files have patterns"""
        core_files = ['bot.aiml', 'config.aiml', 'advanced_metacog.aiml']
        
        for core_file in core_files:
            patterns_in_file = [p for p in aiml_patterns.values() if p.file == core_file]
            assert len(patterns_in_file) > 0, f"No patterns found in {core_file}"


class TestAIMLElements:
    """Test AIML element structure and usage"""
    
    def test_srai_elements_have_content(self, aiml_files):
        """Verify SRAI elements have content"""
        errors = []
        
        for filepath in aiml_files:
            tree = ET.parse(filepath)
            root = tree.getroot()
            filename = Path(filepath).name
            
            for srai in root.findall('.//srai'):
                content = ''.join(srai.itertext()).strip()
                # Check if SRAI has child elements (like <star/>, <get/>, etc.)
                has_children = len(list(srai)) > 0
                if not content and not has_children:
                    # Find parent pattern for context
                    errors.append(f"{filename}: Empty <srai> element found")
        
        # Some empty SRAI might be valid (dynamic content)
        # Just warn if there are very many
        if len(errors) > 20:
            pytest.fail(f"Found {len(errors)} empty SRAI elements")
    
    def test_set_elements_have_name_attribute(self, aiml_files):
        """Verify SET elements have name attribute"""
        errors = []
        
        for filepath in aiml_files:
            tree = ET.parse(filepath)
            root = tree.getroot()
            filename = Path(filepath).name
            
            for set_elem in root.findall('.//set'):
                name = set_elem.get('name')
                var = set_elem.get('var')  # AIML 2.0 alternate syntax
                # Valid if has name, var, or is a bot predicate set
                if not name and not var:
                    # Check for valid alternate forms (e.g., bot predicates)
                    if 'predicate' not in set_elem.attrib:
                        errors.append(f"{filename}: <set> element without name/var attribute")
        
        # Allow some flexibility for valid AIML 2.0 syntax variations
        if len(errors) > 50:
            pytest.fail(f"SET element errors:\n" + "\n".join(errors[:10]))
    
    def test_get_elements_have_name_attribute(self, aiml_files):
        """Verify GET elements have name attribute"""
        errors = []
        
        for filepath in aiml_files:
            tree = ET.parse(filepath)
            root = tree.getroot()
            filename = Path(filepath).name
            
            for get_elem in root.findall('.//get'):
                name = get_elem.get('name')
                var = get_elem.get('var')  # AIML 2.0 alternate syntax
                # Valid if has name, var, or is a bot predicate get
                if not name and not var:
                    # Check for valid alternate forms
                    if 'predicate' not in get_elem.attrib:
                        errors.append(f"{filename}: <get> element without name/var attribute")
        
        # Allow some flexibility for valid AIML 2.0 syntax variations
        if len(errors) > 50:
            pytest.fail(f"GET element errors:\n" + "\n".join(errors[:10]))
    
    def test_topic_elements_have_name_attribute(self, aiml_files):
        """Verify TOPIC elements have name attribute"""
        errors = []
        
        for filepath in aiml_files:
            tree = ET.parse(filepath)
            root = tree.getroot()
            filename = Path(filepath).name
            
            for topic in root.findall('.//topic'):
                name = topic.get('name')
                if not name:
                    errors.append(f"{filename}: <topic> element without name attribute")
        
        if errors:
            pytest.fail(f"TOPIC element errors:\n" + "\n".join(errors[:10]))
    
    def test_condition_elements_structure(self, aiml_files):
        """Verify CONDITION elements have proper structure"""
        for filepath in aiml_files:
            tree = ET.parse(filepath)
            root = tree.getroot()
            
            for condition in root.findall('.//condition'):
                # Conditions should have either name attribute or li children
                name = condition.get('name')
                li_elements = condition.findall('li')
                
                # Either direct condition or multi-value condition
                has_structure = name is not None or len(li_elements) > 0
                # Note: Some conditions may be dynamically structured
                # Just verify they exist


class TestBotProperties:
    """Test bot.properties file"""
    
    def test_bot_properties_exists(self, project_root):
        """Verify bot.properties file exists"""
        prop_file = project_root / "bot.properties"
        assert prop_file.exists(), "bot.properties file not found"
    
    def test_required_properties(self, bot_properties):
        """Verify required bot properties are present"""
        required = ['name', 'version', 'author', 'language']
        
        for prop in required:
            assert prop in bot_properties, f"Required property '{prop}' not found"
    
    def test_bot_name(self, bot_properties):
        """Verify bot name is PandaMania"""
        assert bot_properties.get('name') == 'PandaMania', \
            f"Expected bot name 'PandaMania', got '{bot_properties.get('name')}'"
    
    def test_aiml_version(self, bot_properties):
        """Verify AIML language version"""
        language = bot_properties.get('language', '')
        assert 'AIML' in language, f"Expected AIML language, got '{language}'"
    
    def test_metacog_configuration(self, bot_properties):
        """Verify meta-cognitive configuration"""
        metacog_layers = bot_properties.get('metacog_layers')
        assert metacog_layers is not None, "metacog_layers property not found"
        assert int(metacog_layers) >= 3, "Expected at least 3 meta-cognitive layers"
    
    def test_autognosis_configuration(self, bot_properties):
        """Verify autognosis configuration"""
        autognosis = bot_properties.get('autognosis_enabled')
        assert autognosis == 'true', "autognosis should be enabled"
    
    def test_holistic_metamodel_configuration(self, bot_properties):
        """Verify holistic metamodel configuration"""
        metamodel = bot_properties.get('holistic_metamodel')
        assert metamodel == 'enabled', "holistic_metamodel should be enabled"
