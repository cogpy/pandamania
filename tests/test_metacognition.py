"""
Meta-Cognitive Layer Tests
Tests for all 5 meta-cognitive layers (0-4)
"""

import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from conftest import assert_response_contains, assert_response_matches_any


class TestLayer0BaseProcessing:
    """Test Layer 0: Base pattern matching"""
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_direct_pattern_match(self, aiml_interpreter):
        """Test direct pattern matching at Layer 0"""
        response = aiml_interpreter.respond("HELLO")
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_srai_reduction(self, aiml_interpreter):
        """Test SRAI pattern reduction at Layer 0"""
        response = aiml_interpreter.respond("HI")
        # HI should reduce to HELLO via SRAI
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    def test_base_patterns_exist(self, aiml_patterns):
        """Verify base layer patterns exist"""
        base_patterns = ["HELLO", "HI", "GREETINGS", "HOW ARE YOU"]
        found = sum(1 for p in base_patterns if p in aiml_patterns)
        assert found >= 3, f"Expected at least 3 base patterns, found {found}"


class TestLayer1FirstOrderMetaCognition:
    """Test Layer 1: First-order meta-cognition (self-awareness)"""
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_what_are_you_thinking(self, aiml_interpreter):
        """Test first-order introspection"""
        response = aiml_interpreter.respond("WHAT ARE YOU THINKING")
        assert_response_matches_any(response, 
            ["thinking", "processing", "thought", "analyzing", "examining"])
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_self_assessment(self, aiml_interpreter):
        """Test meta-cognitive self-assessment"""
        response = aiml_interpreter.respond("METACOGNITIVE SELF ASSESS")
        assert_response_matches_any(response, 
            ["state", "processing", "awareness", "current"])
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_introspect_thought(self, aiml_interpreter):
        """Test thought introspection"""
        response = aiml_interpreter.respond("INTROSPECT CURRENT THOUGHT")
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    def test_layer1_patterns_exist(self, aiml_patterns):
        """Verify Layer 1 patterns exist"""
        layer1_patterns = [
            "WHAT ARE YOU THINKING",
            "METACOGNITIVE SELF ASSESS",
            "INTROSPECT CURRENT THOUGHT"
        ]
        found = sum(1 for p in layer1_patterns if p in aiml_patterns)
        assert found >= 2, f"Expected at least 2 Layer 1 patterns, found {found}"


class TestLayer2SecondOrderMetaCognition:
    """Test Layer 2: Second-order meta-cognition (thinking about thinking)"""
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_how_do_you_think(self, aiml_interpreter):
        """Test second-order reflection query"""
        response = aiml_interpreter.respond("HOW DO YOU THINK")
        assert_response_matches_any(response, 
            ["layer", "process", "reflect", "thinking", "pattern"])
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_second_order_reflection(self, aiml_interpreter):
        """Test explicit second-order reflection"""
        response = aiml_interpreter.respond("SECOND ORDER REFLECTION")
        assert_response_matches_any(response, 
            ["monitoring", "reflection", "analyzing", "self-assessment"])
    
    @pytest.mark.metacognition
    def test_layer2_patterns_exist(self, aiml_patterns):
        """Verify Layer 2 patterns exist"""
        layer2_patterns = [
            "SECOND ORDER REFLECTION",
            "HOW DO YOU THINK"
        ]
        found = sum(1 for p in layer2_patterns if p in aiml_patterns)
        assert found >= 1, f"Expected at least 1 Layer 2 pattern, found {found}"


class TestLayer3ThirdOrderMetaCognition:
    """Test Layer 3: Third-order meta-cognition (reasoning about reasoning)"""
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_why_do_you_think_that(self, aiml_interpreter):
        """Test third-order reasoning query"""
        response = aiml_interpreter.respond("WHY DO YOU THINK THAT")
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_third_order_reasoning(self, aiml_interpreter):
        """Test explicit third-order reasoning"""
        response = aiml_interpreter.respond("THIRD ORDER REASONING")
        assert_response_matches_any(response, 
            ["reasoning", "meta", "evaluating", "process"])
    
    @pytest.mark.metacognition
    def test_layer3_patterns_exist(self, aiml_patterns):
        """Verify Layer 3 patterns exist"""
        # Check for third-order patterns
        layer3_patterns = [p for p in aiml_patterns if 'THIRD ORDER' in p]
        assert len(layer3_patterns) >= 1, "Expected at least 1 third-order pattern"


class TestLayer4FourthOrderMetaCognition:
    """Test Layer 4: Fourth-order meta-cognition (architectural reasoning)"""
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_fourth_order_reasoning(self, aiml_interpreter):
        """Test fourth-order architectural reasoning"""
        response = aiml_interpreter.respond("FOURTH ORDER REASONING")
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_fourth_order_status(self, aiml_interpreter):
        """Test fourth-order status query"""
        response = aiml_interpreter.respond("FOURTH ORDER STATUS")
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_evaluate_cognitive_architecture(self, aiml_interpreter):
        """Test cognitive architecture evaluation"""
        response = aiml_interpreter.respond("EVALUATE COGNITIVE ARCHITECTURE")
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_check_cognitive_efficiency(self, aiml_interpreter):
        """Test cognitive efficiency check"""
        response = aiml_interpreter.respond("CHECK COGNITIVE EFFICIENCY")
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    def test_layer4_patterns_exist(self, aiml_patterns):
        """Verify Layer 4 patterns exist"""
        # Check layer4_metacog.aiml patterns
        layer4_patterns = [p for p in aiml_patterns if 'FOURTH ORDER' in p]
        assert len(layer4_patterns) >= 1, "Expected Layer 4 patterns"
    
    @pytest.mark.metacognition
    def test_layer4_file_exists(self, aiml_files):
        """Verify layer4_metacog.aiml file exists"""
        layer4_files = [f for f in aiml_files if 'layer4' in f.lower()]
        assert len(layer4_files) >= 1, "layer4_metacog.aiml not found"


class TestRecursiveSelfAwareness:
    """Test recursive self-awareness capabilities"""
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_are_you_self_aware(self, aiml_interpreter):
        """Test self-awareness query"""
        response = aiml_interpreter.respond("ARE YOU SELF AWARE")
        assert_response_matches_any(response, 
            ["aware", "awareness", "self", "levels", "recursive"])
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_can_you_think_about_thinking(self, aiml_interpreter):
        """Test recursive thinking capability"""
        response = aiml_interpreter.respond("CAN YOU THINK ABOUT YOUR THINKING")
        assert_response_matches_any(response, 
            ["yes", "meta-cognition", "recursive", "thinking", "capability"])
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_optimize_yourself(self, aiml_interpreter):
        """Test self-optimization capability"""
        response = aiml_interpreter.respond("OPTIMIZE YOURSELF")
        assert response and len(response) > 0


class TestEpistemicReasoning:
    """Test epistemic reasoning capabilities"""
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_how_do_you_know(self, aiml_interpreter):
        """Test knowledge-about-knowledge reasoning"""
        response = aiml_interpreter.respond("HOW DO YOU KNOW")
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_epistemic_reflection(self, aiml_interpreter):
        """Test epistemic reflection"""
        response = aiml_interpreter.respond("EPISTEMIC REFLECTION")
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    def test_epistemic_patterns_exist(self, aiml_patterns):
        """Verify epistemic reasoning patterns exist"""
        epistemic_keywords = ['EPISTEMIC', 'KNOW', 'CERTAIN']
        epistemic_patterns = [
            p for p in aiml_patterns 
            if any(kw in p for kw in epistemic_keywords)
        ]
        assert len(epistemic_patterns) >= 1, "Expected epistemic reasoning patterns"


class TestCounterfactualReasoning:
    """Test counterfactual reasoning capabilities"""
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_what_if_pattern(self, aiml_interpreter):
        """Test counterfactual reasoning"""
        response = aiml_interpreter.respond("WHAT IF")
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    def test_counterfactual_patterns_exist(self, aiml_patterns):
        """Verify counterfactual patterns exist"""
        counterfactual_patterns = [
            p for p in aiml_patterns 
            if 'WHAT IF' in p or 'COUNTERFACTUAL' in p
        ]
        assert len(counterfactual_patterns) >= 1, "Expected counterfactual patterns"


class TestTheoryOfMind:
    """Test theory of mind capabilities"""
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_what_am_i_thinking(self, aiml_interpreter):
        """Test user cognitive state modeling"""
        response = aiml_interpreter.respond("WHAT AM I THINKING")
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    def test_theory_of_mind_patterns_exist(self, aiml_patterns):
        """Verify theory of mind patterns exist"""
        tom_patterns = [
            p for p in aiml_patterns 
            if 'WHAT AM I' in p or 'THEORY OF MIND' in p or 'MODEL USER' in p
        ]
        assert len(tom_patterns) >= 1, "Expected theory of mind patterns"


class TestMetaCognitiveChains:
    """Test meta-cognitive chain execution"""
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_multi_layer_chain(self, aiml_interpreter):
        """Test multi-layer meta-cognitive chain"""
        # HOW ARE YOU should trigger chain through multiple layers
        response = aiml_interpreter.respond("HOW ARE YOU")
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    @pytest.mark.e2e
    def test_reflection_chain(self, aiml_interpreter):
        """Test reflection chain execution"""
        # First greeting
        aiml_interpreter.respond("HELLO")
        # Then reflection
        response = aiml_interpreter.respond("WHAT ARE YOU THINKING")
        assert response and len(response) > 0
    
    @pytest.mark.metacognition
    def test_srai_chain_depth(self, aiml_patterns):
        """Verify SRAI chains are defined properly"""
        import xml.etree.ElementTree as ET
        
        # Check for patterns that trigger SRAI chains
        chain_patterns = []
        for pattern_text, pattern in aiml_patterns.items():
            if '<srai>' in pattern.template.lower():
                chain_patterns.append(pattern_text)
        
        # Should have many patterns with SRAI chains
        assert len(chain_patterns) >= 20, \
            f"Expected 20+ patterns with SRAI chains, found {len(chain_patterns)}"
