"""
Domain Knowledge Tests
Tests for domain-specific AIML patterns (math, programming, psychology, ethics)
"""

import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from conftest import assert_response_contains, assert_response_matches_any


class TestMathLogicDomain:
    """Test mathematics and logic domain patterns"""
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_what_is_prime_number(self, aiml_interpreter):
        """Test prime number definition"""
        response = aiml_interpreter.respond("WHAT IS A PRIME NUMBER")
        assert_response_matches_any(response, 
            ["prime", "number", "divisible", "divisor", "natural"])
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_what_is_logic(self, aiml_interpreter):
        """Test logic definition"""
        response = aiml_interpreter.respond("WHAT IS LOGIC")
        assert_response_matches_any(response, 
            ["logic", "reasoning", "valid", "argument"])
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_godels_theorem(self, aiml_interpreter):
        """Test Gödel's incompleteness theorem"""
        response = aiml_interpreter.respond("WHAT IS GODELS INCOMPLETENESS THEOREM")
        assert response and len(response) > 0
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_russells_paradox(self, aiml_interpreter):
        """Test Russell's paradox"""
        response = aiml_interpreter.respond("WHAT IS RUSSELLS PARADOX")
        assert response and len(response) > 0
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_math_problem_solving(self, aiml_interpreter):
        """Test math problem solving approach"""
        response = aiml_interpreter.respond("HOW DO YOU SOLVE MATH PROBLEMS")
        assert response and len(response) > 0
    
    @pytest.mark.domain
    def test_math_file_exists(self, aiml_files):
        """Verify math_logic.aiml file exists"""
        math_files = [f for f in aiml_files if 'math' in f.lower()]
        assert len(math_files) >= 1, "math_logic.aiml not found"
    
    @pytest.mark.domain
    def test_math_patterns_count(self, aiml_patterns):
        """Verify math domain has sufficient patterns"""
        math_patterns = [p for p in aiml_patterns.values() if 'math' in p.file.lower()]
        assert len(math_patterns) >= 20, \
            f"Expected 20+ math patterns, found {len(math_patterns)}"


class TestProgrammingTechDomain:
    """Test programming and technology domain patterns"""
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_what_is_recursion(self, aiml_interpreter):
        """Test recursion definition"""
        response = aiml_interpreter.respond("WHAT IS RECURSION")
        assert_response_matches_any(response, 
            ["recursion", "recursive", "function", "itself", "calls"])
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_what_is_aiml(self, aiml_interpreter):
        """Test AIML definition"""
        response = aiml_interpreter.respond("WHAT IS AIML")
        assert_response_matches_any(response, 
            ["AIML", "markup", "language", "pattern", "artificial intelligence"])
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_what_is_artificial_intelligence(self, aiml_interpreter):
        """Test AI definition"""
        response = aiml_interpreter.respond("WHAT IS ARTIFICIAL INTELLIGENCE")
        assert_response_matches_any(response, 
            ["artificial", "intelligence", "AI", "machine", "computer"])
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_what_is_oop(self, aiml_interpreter):
        """Test OOP definition"""
        response = aiml_interpreter.respond("WHAT IS OBJECT ORIENTED PROGRAMMING")
        assert response and len(response) > 0
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_what_is_functional_programming(self, aiml_interpreter):
        """Test functional programming definition"""
        response = aiml_interpreter.respond("WHAT IS FUNCTIONAL PROGRAMMING")
        assert response and len(response) > 0
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_what_is_algorithm(self, aiml_interpreter):
        """Test algorithm definition"""
        response = aiml_interpreter.respond("WHAT IS AN ALGORITHM")
        assert response and len(response) > 0
    
    @pytest.mark.domain
    def test_programming_file_exists(self, aiml_files):
        """Verify programming_tech.aiml file exists"""
        prog_files = [f for f in aiml_files if 'programming' in f.lower()]
        assert len(prog_files) >= 1, "programming_tech.aiml not found"
    
    @pytest.mark.domain
    def test_programming_patterns_count(self, aiml_patterns):
        """Verify programming domain has sufficient patterns"""
        prog_patterns = [p for p in aiml_patterns.values() if 'programming' in p.file.lower()]
        assert len(prog_patterns) >= 30, \
            f"Expected 30+ programming patterns, found {len(prog_patterns)}"


class TestPsychologyCognitionDomain:
    """Test psychology and cognition domain patterns"""
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_what_is_metacognition(self, aiml_interpreter):
        """Test meta-cognition definition"""
        response = aiml_interpreter.respond("WHAT IS METACOGNITION")
        assert_response_matches_any(response, 
            ["metacognition", "thinking", "cognition", "awareness"])
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_what_is_theory_of_mind(self, aiml_interpreter):
        """Test theory of mind definition"""
        response = aiml_interpreter.respond("WHAT IS THEORY OF MIND")
        assert_response_matches_any(response, 
            ["theory of mind", "mental", "states", "others", "beliefs"])
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_what_is_consciousness_psychology(self, aiml_interpreter):
        """Test consciousness from psychology perspective"""
        response = aiml_interpreter.respond("WHAT IS CONSCIOUSNESS PSYCHOLOGY")
        assert response and len(response) > 0
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_what_is_cognitive_bias(self, aiml_interpreter):
        """Test cognitive bias definition"""
        response = aiml_interpreter.respond("WHAT IS COGNITIVE BIAS")
        assert response and len(response) > 0
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_what_is_intelligence(self, aiml_interpreter):
        """Test intelligence definition"""
        response = aiml_interpreter.respond("WHAT IS INTELLIGENCE")
        assert response and len(response) > 0
    
    @pytest.mark.domain
    def test_psychology_file_exists(self, aiml_files):
        """Verify psychology_cognition.aiml file exists"""
        psych_files = [f for f in aiml_files if 'psychology' in f.lower()]
        assert len(psych_files) >= 1, "psychology_cognition.aiml not found"
    
    @pytest.mark.domain
    def test_psychology_patterns_count(self, aiml_patterns):
        """Verify psychology domain has sufficient patterns"""
        psych_patterns = [p for p in aiml_patterns.values() if 'psychology' in p.file.lower()]
        assert len(psych_patterns) >= 20, \
            f"Expected 20+ psychology patterns, found {len(psych_patterns)}"


class TestEthicsPhilosophyDomain:
    """Test ethics and philosophy domain patterns"""
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_hard_problem_of_consciousness(self, aiml_interpreter):
        """Test hard problem of consciousness"""
        response = aiml_interpreter.respond("WHAT IS THE HARD PROBLEM OF CONSCIOUSNESS")
        assert_response_matches_any(response, 
            ["hard problem", "consciousness", "qualia", "subjective", "experience"])
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_chinese_room(self, aiml_interpreter):
        """Test Chinese Room argument"""
        response = aiml_interpreter.respond("WHAT IS THE CHINESE ROOM")
        assert_response_matches_any(response, 
            ["Chinese room", "Searle", "understanding", "symbol", "manipulation"])
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_ai_ethics(self, aiml_interpreter):
        """Test AI ethics"""
        response = aiml_interpreter.respond("WHAT IS AI ETHICS")
        assert_response_matches_any(response, 
            ["ethics", "AI", "moral", "responsible", "artificial intelligence"])
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_functionalism(self, aiml_interpreter):
        """Test functionalism definition"""
        response = aiml_interpreter.respond("WHAT IS FUNCTIONALISM")
        assert response and len(response) > 0
    
    @pytest.mark.domain
    @pytest.mark.e2e
    def test_free_will(self, aiml_interpreter):
        """Test free will definition"""
        response = aiml_interpreter.respond("WHAT IS FREE WILL")
        assert response and len(response) > 0
    
    @pytest.mark.domain
    def test_ethics_file_exists(self, aiml_files):
        """Verify ethics_philosophy.aiml file exists"""
        ethics_files = [f for f in aiml_files if 'ethics' in f.lower()]
        assert len(ethics_files) >= 1, "ethics_philosophy.aiml not found"
    
    @pytest.mark.domain
    def test_ethics_patterns_count(self, aiml_patterns):
        """Verify ethics domain has sufficient patterns"""
        ethics_patterns = [p for p in aiml_patterns.values() if 'ethics' in p.file.lower()]
        assert len(ethics_patterns) >= 20, \
            f"Expected 20+ ethics patterns, found {len(ethics_patterns)}"


class TestDomainCrossReferences:
    """Test cross-domain integration"""
    
    @pytest.mark.domain
    def test_all_domain_files_exist(self, aiml_files):
        """Verify all domain files exist"""
        required_domains = ['math', 'programming', 'psychology', 'ethics']
        
        for domain in required_domains:
            matching = [f for f in aiml_files if domain in f.lower()]
            assert len(matching) >= 1, f"Domain file for '{domain}' not found"
    
    @pytest.mark.domain
    def test_domain_patterns_total(self, aiml_patterns):
        """Verify total domain patterns count"""
        domain_files = ['math_logic', 'programming_tech', 'psychology_cognition', 'ethics_philosophy']
        
        domain_patterns = [
            p for p in aiml_patterns.values() 
            if any(df in p.file.lower() for df in domain_files)
        ]
        
        assert len(domain_patterns) >= 100, \
            f"Expected 100+ domain patterns total, found {len(domain_patterns)}"
    
    @pytest.mark.domain
    def test_meta_cognitive_framing_in_domains(self, aiml_patterns):
        """Verify domain responses include meta-cognitive framing"""
        # Domain patterns should reference meta-cognition
        domain_files = ['math_logic', 'programming_tech', 'psychology_cognition', 'ethics_philosophy']
        
        domain_patterns = [
            p for p in aiml_patterns.values() 
            if any(df in p.file.lower() for df in domain_files)
        ]
        
        # At least some should reference meta-cognition
        meta_refs = [
            p for p in domain_patterns 
            if 'meta' in p.template.lower() or 'layer' in p.template.lower()
        ]
        
        # Should have some meta-cognitive framing
        assert len(meta_refs) >= 5, \
            f"Expected 5+ domain patterns with meta-cognitive framing, found {len(meta_refs)}"


class TestNaturalLanguagePatterns:
    """Test natural language processing patterns"""
    
    @pytest.mark.domain
    def test_natural_language_file_exists(self, aiml_files):
        """Verify natural_language.aiml file exists"""
        nl_files = [f for f in aiml_files if 'natural_language' in f.lower()]
        assert len(nl_files) >= 1, "natural_language.aiml not found"
    
    @pytest.mark.domain
    def test_natural_language_patterns_count(self, aiml_patterns):
        """Verify natural language patterns count"""
        nl_patterns = [p for p in aiml_patterns.values() if 'natural' in p.file.lower()]
        assert len(nl_patterns) >= 50, \
            f"Expected 50+ NL patterns, found {len(nl_patterns)}"


class TestEmotionalIntelligencePatterns:
    """Test emotional intelligence patterns"""
    
    @pytest.mark.domain
    def test_emotional_intelligence_file_exists(self, aiml_files):
        """Verify emotional_intelligence.aiml file exists"""
        ei_files = [f for f in aiml_files if 'emotional' in f.lower()]
        assert len(ei_files) >= 1, "emotional_intelligence.aiml not found"
    
    @pytest.mark.domain
    def test_emotional_patterns_count(self, aiml_patterns):
        """Verify emotional intelligence patterns count"""
        ei_patterns = [p for p in aiml_patterns.values() if 'emotional' in p.file.lower()]
        assert len(ei_patterns) >= 15, \
            f"Expected 15+ emotional patterns, found {len(ei_patterns)}"
