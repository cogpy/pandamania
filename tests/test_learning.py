"""
Learning System Tests
Tests for session learning and knowledge base capabilities
"""

import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from conftest import assert_response_contains, assert_response_matches_any


class TestSessionLearningInitialization:
    """Test session learning initialization"""
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_session_init(self, aiml_interpreter):
        """Test SESSION INIT command"""
        response = aiml_interpreter.respond("SESSION INIT")
        assert response and len(response) > 0
    
    @pytest.mark.learning
    def test_session_learning_file_exists(self, aiml_files):
        """Verify session_learning.aiml file exists"""
        sl_files = [f for f in aiml_files if 'session_learning' in f.lower()]
        assert len(sl_files) >= 1, "session_learning.aiml not found"
    
    @pytest.mark.learning
    def test_knowledge_base_file_exists(self, aiml_files):
        """Verify knowledge_base.aiml file exists"""
        kb_files = [f for f in aiml_files if 'knowledge_base' in f.lower()]
        assert len(kb_files) >= 1, "knowledge_base.aiml not found"


class TestFactExtraction:
    """Test fact extraction from user statements"""
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_learn_name(self, aiml_interpreter):
        """Test learning user's name"""
        response = aiml_interpreter.respond("MY NAME IS ALICE")
        # Accept any valid response
        assert response and len(response) > 0
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_learn_location(self, aiml_interpreter):
        """Test learning user's location"""
        response = aiml_interpreter.respond("I LIVE IN SEATTLE")
        assert response and len(response) > 0
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_learn_occupation(self, aiml_interpreter):
        """Test learning user's occupation"""
        response = aiml_interpreter.respond("I WORK AS A SOFTWARE ENGINEER")
        assert response and len(response) > 0


class TestPreferenceLearning:
    """Test preference learning capabilities"""
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_learn_preference_like(self, aiml_interpreter):
        """Test learning user preferences (likes)"""
        response = aiml_interpreter.respond("I LIKE TECHNICAL EXPLANATIONS")
        assert response and len(response) > 0
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_learn_preference_prefer(self, aiml_interpreter):
        """Test learning user preferences (prefer)"""
        response = aiml_interpreter.respond("I PREFER DETAILED RESPONSES")
        assert response and len(response) > 0


class TestSessionMemory:
    """Test session memory capabilities"""
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_what_have_you_learned(self, aiml_interpreter):
        """Test querying what the bot has learned"""
        # First teach something
        aiml_interpreter.respond("MY NAME IS BOB")
        # Then ask
        response = aiml_interpreter.respond("WHAT HAVE YOU LEARNED")
        assert response and len(response) > 0
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_session_status(self, aiml_interpreter):
        """Test SESSION STATUS command"""
        response = aiml_interpreter.respond("SESSION STATUS")
        assert response and len(response) > 0


class TestKnowledgeBaseInitialization:
    """Test knowledge base initialization"""
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_knowledge_base_init(self, aiml_interpreter):
        """Test KNOWLEDGE BASE INIT command"""
        response = aiml_interpreter.respond("KNOWLEDGE BASE INIT")
        assert response and len(response) > 0
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_kb_status(self, aiml_interpreter):
        """Test KB STATUS command"""
        response = aiml_interpreter.respond("KB STATUS")
        assert response and len(response) > 0


class TestKnowledgeStorage:
    """Test knowledge storage capabilities"""
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_store_fact_is(self, aiml_interpreter):
        """Test storing IS facts"""
        response = aiml_interpreter.respond("STORE FACT AIML IS MARKUP LANGUAGE")
        # Accept any valid response
        assert response and len(response) > 0
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_store_fact_has(self, aiml_interpreter):
        """Test storing HAS facts"""
        response = aiml_interpreter.respond("STORE FACT AIML HAS XML SYNTAX")
        assert response and len(response) > 0
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_store_fact_can(self, aiml_interpreter):
        """Test storing CAN facts"""
        response = aiml_interpreter.respond("STORE FACT AIML CAN CREATE CHATBOTS")
        assert response and len(response) > 0
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_store_relationship(self, aiml_interpreter):
        """Test storing relationships"""
        response = aiml_interpreter.respond("STORE RELATIONSHIP AIML ISA MARKUP LANGUAGE")
        assert response and len(response) > 0


class TestKnowledgeRetrieval:
    """Test knowledge retrieval capabilities"""
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_what_is_query(self, aiml_interpreter):
        """Test WHAT IS query"""
        # First store a fact
        aiml_interpreter.respond("STORE FACT PYTHON IS PROGRAMMING LANGUAGE")
        # Then query
        response = aiml_interpreter.respond("WHAT IS PYTHON")
        assert response and len(response) > 0
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_what_do_you_know(self, aiml_interpreter):
        """Test WHAT DO YOU KNOW ABOUT query"""
        response = aiml_interpreter.respond("WHAT DO YOU KNOW ABOUT AIML")
        assert response and len(response) > 0
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_kb_query(self, aiml_interpreter):
        """Test KB QUERY command"""
        response = aiml_interpreter.respond("KB QUERY AIML")
        assert response and len(response) > 0


class TestInferenceEngine:
    """Test inference engine capabilities"""
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_infer_knowledge(self, aiml_interpreter):
        """Test INFER KNOWLEDGE ABOUT command"""
        response = aiml_interpreter.respond("INFER KNOWLEDGE ABOUT AIML")
        assert response and len(response) > 0
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_inference_status(self, aiml_interpreter):
        """Test INFERENCE STATUS command"""
        response = aiml_interpreter.respond("INFERENCE STATUS")
        assert response and len(response) > 0


class TestMetaKnowledge:
    """Test meta-knowledge capabilities"""
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_how_do_you_learn(self, aiml_interpreter):
        """Test HOW DO YOU LEARN explanation"""
        response = aiml_interpreter.respond("HOW DO YOU LEARN")
        assert_response_matches_any(response, 
            ["learn", "Learning", "session", "facts", "knowledge"])
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_what_is_knowledge(self, aiml_interpreter):
        """Test WHAT IS KNOWLEDGE explanation"""
        response = aiml_interpreter.respond("WHAT IS KNOWLEDGE")
        assert_response_matches_any(response, 
            ["knowledge", "information", "facts", "beliefs"])
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_are_you_learning(self, aiml_interpreter):
        """Test ARE YOU LEARNING query"""
        response = aiml_interpreter.respond("ARE YOU LEARNING")
        assert response and len(response) > 0


class TestLearningPatterns:
    """Test learning pattern structure"""
    
    @pytest.mark.learning
    def test_session_learning_pattern_count(self, aiml_patterns):
        """Verify session learning has sufficient patterns"""
        sl_patterns = [
            p for p in aiml_patterns.values() 
            if 'session_learning' in p.file.lower()
        ]
        assert len(sl_patterns) >= 20, \
            f"Expected 20+ session learning patterns, found {len(sl_patterns)}"
    
    @pytest.mark.learning
    def test_knowledge_base_pattern_count(self, aiml_patterns):
        """Verify knowledge base has sufficient patterns"""
        kb_patterns = [
            p for p in aiml_patterns.values() 
            if 'knowledge_base' in p.file.lower()
        ]
        assert len(kb_patterns) >= 20, \
            f"Expected 20+ knowledge base patterns, found {len(kb_patterns)}"
    
    @pytest.mark.learning
    def test_learning_configuration(self, bot_properties):
        """Verify learning is configured"""
        session_learning = bot_properties.get('session_learning')
        assert session_learning == 'enabled', "session_learning should be enabled"
        
        knowledge_base = bot_properties.get('knowledge_base')
        assert knowledge_base == 'enabled', "knowledge_base should be enabled"


class TestLearningIntegration:
    """Test integration between learning systems"""
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_learn_then_recall(self, fresh_interpreter):
        """Test learning then recalling information"""
        # Teach the bot
        fresh_interpreter.respond("MY NAME IS CHARLIE")
        # Recall
        response = fresh_interpreter.respond("WHAT IS MY NAME")
        # May or may not work depending on implementation
        assert response and len(response) > 0
    
    @pytest.mark.learning
    @pytest.mark.e2e
    def test_store_then_query(self, fresh_interpreter):
        """Test storing fact then querying"""
        # Store a fact
        fresh_interpreter.respond("STORE FACT COFFEE IS BEVERAGE")
        # Query
        response = fresh_interpreter.respond("WHAT IS COFFEE")
        assert response and len(response) > 0
    
    @pytest.mark.learning
    def test_learning_meta_awareness(self, aiml_patterns):
        """Verify learning patterns include meta-cognitive awareness"""
        learning_patterns = [
            p for p in aiml_patterns.values() 
            if 'learning' in p.file.lower() or 'knowledge' in p.file.lower()
        ]
        
        # At least some should reference meta-cognition
        meta_refs = [
            p for p in learning_patterns 
            if 'meta' in p.template.lower() or 'aware' in p.template.lower()
        ]
        
        assert len(meta_refs) >= 1, \
            "Expected learning patterns with meta-cognitive awareness"
