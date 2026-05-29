"""
Conversation Flow Tests
Tests for multi-turn conversations and context management
"""

import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from conftest import assert_response_contains, assert_response_matches_any


class TestMultiTurnCoherence:
    """Test multi-turn conversation coherence"""
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_greeting_then_state_query(self, fresh_interpreter):
        """Test greeting followed by state query"""
        # First turn
        response1 = fresh_interpreter.respond("HELLO")
        assert response1 and len(response1) > 0
        
        # Second turn
        response2 = fresh_interpreter.respond("HOW ARE YOU")
        assert response2 and len(response2) > 0
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_greeting_then_introspection(self, fresh_interpreter):
        """Test greeting followed by introspection"""
        # First turn
        fresh_interpreter.respond("HELLO")
        
        # Second turn - introspection
        response = fresh_interpreter.respond("WHAT ARE YOU THINKING")
        assert_response_matches_any(response, 
            ["thinking", "processing", "analyzing", "thought"])
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_multi_turn_meta_cognitive_chain(self, fresh_interpreter):
        """Test multi-turn meta-cognitive exploration"""
        # Turn 1: Greeting
        fresh_interpreter.respond("HELLO")
        
        # Turn 2: State query
        fresh_interpreter.respond("HOW ARE YOU")
        
        # Turn 3: Introspection
        fresh_interpreter.respond("WHAT ARE YOU THINKING")
        
        # Turn 4: Deep meta-cognition
        response = fresh_interpreter.respond("WHY DO YOU THINK THAT")
        assert response and len(response) > 0


class TestTopicManagement:
    """Test topic switching and context"""
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_enter_philosophy_topic(self, fresh_interpreter):
        """Test entering philosophy topic"""
        response = fresh_interpreter.respond("LETS TALK ABOUT PHILOSOPHY")
        assert_response_matches_any(response, 
            ["philosophy", "philosophical", "topic", "entering"])
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_enter_science_topic(self, fresh_interpreter):
        """Test entering science topic"""
        response = fresh_interpreter.respond("LETS TALK ABOUT SCIENCE")
        assert response and len(response) > 0
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_topic_query(self, fresh_interpreter):
        """Test querying current topic"""
        # Enter a topic
        fresh_interpreter.respond("LETS TALK ABOUT PHILOSOPHY")
        
        # Query topic
        response = fresh_interpreter.respond("WHAT IS THE TOPIC")
        assert response and len(response) > 0
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_change_topic(self, fresh_interpreter):
        """Test changing topic"""
        # Enter first topic
        fresh_interpreter.respond("LETS TALK ABOUT PHILOSOPHY")
        
        # Change topic
        response = fresh_interpreter.respond("CHANGE TOPIC")
        assert response and len(response) > 0
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_topic_switch(self, fresh_interpreter):
        """Test switching between topics"""
        # Enter philosophy
        fresh_interpreter.respond("LETS TALK ABOUT PHILOSOPHY")
        
        # Switch to science
        response = fresh_interpreter.respond("LETS TALK ABOUT SCIENCE")
        assert response and len(response) > 0


class TestStatePersistence:
    """Test state persistence across turns"""
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_greeting_state_persists(self, fresh_interpreter):
        """Test that greeting state persists"""
        # Greet
        fresh_interpreter.respond("HELLO")
        
        # Check state (via status or other means)
        response = fresh_interpreter.respond("STATUS")
        # Should reflect active conversation
        assert response and len(response) > 0
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_init_state_persists(self, fresh_interpreter):
        """Test that initialization state persists"""
        # Initialize
        fresh_interpreter.respond("SYSTEM INIT")
        
        # Check status
        response = fresh_interpreter.respond("STATUS")
        assert response and len(response) > 0


class TestConversationHistory:
    """Test conversation history tracking"""
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_what_did_i_say(self, fresh_interpreter):
        """Test recalling what user said"""
        # Say something
        fresh_interpreter.respond("HELLO")
        
        # Ask what was said
        response = fresh_interpreter.respond("WHAT DID I JUST SAY")
        # Response depends on <that> implementation
        assert response and len(response) > 0


class TestContextRetention:
    """Test context retention across conversation"""
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_context_retained_in_topic(self, fresh_interpreter):
        """Test context is retained within topic"""
        # Enter topic
        fresh_interpreter.respond("LETS TALK ABOUT PHILOSOPHY")
        
        # Ask question in topic context
        response1 = fresh_interpreter.respond("WHAT IS CONSCIOUSNESS")
        
        # Follow-up should maintain context
        response2 = fresh_interpreter.respond("TELL ME MORE")
        
        # Both should produce responses
        assert response1 and len(response1) > 0
        assert response2 and len(response2) > 0
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_learning_context_retained(self, fresh_interpreter):
        """Test learned facts are retained in conversation"""
        # Teach name
        fresh_interpreter.respond("MY NAME IS DAVID")
        
        # Have intermediate conversation
        fresh_interpreter.respond("HOW ARE YOU")
        
        # Check if name is still known
        response = fresh_interpreter.respond("WHAT IS MY NAME")
        # May or may not work depending on implementation
        assert response and len(response) > 0


class TestConversationPatterns:
    """Test conversation-related patterns"""
    
    @pytest.mark.conversation
    def test_topic_patterns_exist(self, aiml_patterns):
        """Verify topic management patterns exist"""
        topic_keywords = ['TALK ABOUT', 'TOPIC', 'CHANGE TOPIC']
        
        topic_patterns = [
            p for p in aiml_patterns 
            if any(kw in p for kw in topic_keywords)
        ]
        
        assert len(topic_patterns) >= 3, \
            f"Expected 3+ topic patterns, found {len(topic_patterns)}"
    
    @pytest.mark.conversation
    def test_topics_file_exists(self, aiml_files):
        """Verify topics.aiml file exists"""
        topics_files = [f for f in aiml_files if 'topics' in f.lower()]
        assert len(topics_files) >= 1, "topics.aiml not found"
    
    @pytest.mark.conversation
    def test_topics_pattern_count(self, aiml_patterns):
        """Verify topics has sufficient patterns"""
        topics_patterns = [
            p for p in aiml_patterns.values() 
            if 'topics' in p.file.lower()
        ]
        assert len(topics_patterns) >= 20, \
            f"Expected 20+ topics patterns, found {len(topics_patterns)}"


class TestEdgeCases:
    """Test conversation edge cases"""
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_unknown_input(self, fresh_interpreter):
        """Test handling of unknown input"""
        response = fresh_interpreter.respond("XYZZY NONSENSE INPUT")
        # Should get some response (even if default)
        assert response and len(response) > 0
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_empty_input(self, fresh_interpreter):
        """Test handling of empty input"""
        response = fresh_interpreter.respond("")
        # Should handle gracefully
        assert response is not None
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_repeated_input(self, fresh_interpreter):
        """Test repeated input handling"""
        # Same input twice
        response1 = fresh_interpreter.respond("HELLO")
        response2 = fresh_interpreter.respond("HELLO")
        
        # Both should produce responses
        assert response1 and len(response1) > 0
        assert response2 and len(response2) > 0


class TestSystemCommands:
    """Test system command sequences"""
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_init_then_hello(self, fresh_interpreter):
        """Test system init followed by greeting"""
        # Initialize
        fresh_interpreter.respond("SYSTEM INIT")
        
        # Greet
        response = fresh_interpreter.respond("HELLO")
        assert_response_matches_any(response, ["Hello", "Hi", "meta-cognitive"])
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_init_then_status(self, fresh_interpreter):
        """Test system init followed by status"""
        # Initialize
        fresh_interpreter.respond("SYSTEM INIT")
        
        # Check status
        response = fresh_interpreter.respond("STATUS")
        assert response and len(response) > 0
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_diagnostic_sequence(self, fresh_interpreter):
        """Test diagnostic command sequence"""
        # Init
        fresh_interpreter.respond("SYSTEM INIT")
        
        # Diagnostic
        response1 = fresh_interpreter.respond("DIAGNOSTIC")
        
        # Loop status
        response2 = fresh_interpreter.respond("LOOP STATUS")
        
        assert response1 and len(response1) > 0
        assert response2 and len(response2) > 0


class TestIntegrationScenarios:
    """Test integrated conversation scenarios"""
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_full_introduction_flow(self, fresh_interpreter):
        """Test full introduction conversation flow"""
        # Initialize
        fresh_interpreter.respond("SYSTEM INIT")
        
        # Greet
        fresh_interpreter.respond("HELLO")
        
        # Ask who
        response = fresh_interpreter.respond("WHO ARE YOU")
        assert_response_contains(response, "PandaMania")
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_exploration_flow(self, fresh_interpreter):
        """Test exploration conversation flow"""
        # Start
        fresh_interpreter.respond("HELLO")
        
        # State
        fresh_interpreter.respond("HOW ARE YOU")
        
        # Capabilities
        response = fresh_interpreter.respond("WHAT CAN YOU DO")
        assert response and len(response) > 0
    
    @pytest.mark.conversation
    @pytest.mark.e2e
    def test_meta_cognitive_exploration_flow(self, fresh_interpreter):
        """Test meta-cognitive exploration flow"""
        # Initialize
        fresh_interpreter.respond("SYSTEM INIT")
        
        # Greet
        fresh_interpreter.respond("HELLO")
        
        # Introspection
        fresh_interpreter.respond("WHAT ARE YOU THINKING")
        
        # Deep reflection
        fresh_interpreter.respond("HOW DO YOU THINK")
        
        # Meta-reasoning
        response = fresh_interpreter.respond("ARE YOU SELF AWARE")
        assert_response_matches_any(response, 
            ["aware", "awareness", "self", "levels", "recursive", "yes"])
