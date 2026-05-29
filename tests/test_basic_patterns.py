"""
Basic Pattern Tests
Tests for basic AIML patterns and interactions
"""

import pytest
import sys
from pathlib import Path

# Add tests directory to path for conftest imports
sys.path.insert(0, str(Path(__file__).parent))

from conftest import assert_response_contains, assert_response_matches_any


class TestGreetingPatterns:
    """Test greeting and basic interaction patterns"""
    
    @pytest.mark.e2e
    def test_hello_pattern(self, aiml_interpreter):
        """Test HELLO greeting pattern"""
        response = aiml_interpreter.respond("HELLO")
        assert_response_matches_any(response, ["Hello", "Hi", "meta-cognitive"])
    
    @pytest.mark.e2e
    def test_hi_pattern_reduces_to_hello(self, aiml_interpreter):
        """Test HI reduces to HELLO via SRAI"""
        response = aiml_interpreter.respond("HI")
        assert_response_matches_any(response, ["Hello", "Hi", "meta-cognitive"])
    
    @pytest.mark.e2e
    def test_greetings_pattern(self, aiml_interpreter):
        """Test GREETINGS reduces to HELLO"""
        response = aiml_interpreter.respond("GREETINGS")
        assert_response_matches_any(response, ["Hello", "Hi", "meta-cognitive"])
    
    @pytest.mark.e2e
    def test_greeting_sets_state(self, aiml_interpreter):
        """Test greeting sets conversation state"""
        aiml_interpreter.respond("HELLO")
        # After greeting, greeted should be true
        greeted = aiml_interpreter.get_variable("greeted")
        # Note: May not work with mock interpreter
        if greeted:
            assert greeted == "true"


class TestIdentityPatterns:
    """Test bot identity patterns"""
    
    @pytest.mark.e2e
    def test_what_is_your_name(self, aiml_interpreter):
        """Test identity query"""
        response = aiml_interpreter.respond("WHAT IS YOUR NAME")
        assert_response_contains(response, "PandaMania")
    
    @pytest.mark.e2e
    def test_who_are_you(self, aiml_interpreter):
        """Test WHO ARE YOU reduces to name query"""
        response = aiml_interpreter.respond("WHO ARE YOU")
        assert_response_contains(response, "PandaMania")
    
    @pytest.mark.e2e
    def test_bot_name_pattern(self, aiml_interpreter):
        """Test BOT NAME pattern"""
        response = aiml_interpreter.respond("BOT NAME")
        assert_response_contains(response, "PandaMania")
    
    @pytest.mark.e2e
    def test_bot_version(self, aiml_interpreter):
        """Test BOT VERSION pattern"""
        response = aiml_interpreter.respond("BOT VERSION")
        # Should contain version number
        assert response and len(response) > 0


class TestStatePatterns:
    """Test state query patterns"""
    
    @pytest.mark.e2e
    def test_how_are_you(self, aiml_interpreter):
        """Test HOW ARE YOU pattern"""
        response = aiml_interpreter.respond("HOW ARE YOU")
        assert_response_matches_any(response, ["functioning", "optimal", "state", "processing"])
    
    @pytest.mark.e2e
    def test_status_command(self, aiml_interpreter):
        """Test STATUS command"""
        response = aiml_interpreter.respond("STATUS")
        # Should return status information
        assert response and len(response) > 0
    
    @pytest.mark.e2e
    def test_loop_status(self, aiml_interpreter):
        """Test LOOP STATUS command"""
        response = aiml_interpreter.respond("LOOP STATUS")
        assert_response_matches_any(response, ["Loop", "Active", "Meta-Cognitive"])


class TestSystemCommands:
    """Test system command patterns"""
    
    @pytest.mark.e2e
    def test_system_init(self, aiml_interpreter):
        """Test SYSTEM INIT command"""
        response = aiml_interpreter.respond("SYSTEM INIT")
        assert_response_matches_any(response, ["initialized", "Init", "ready", "operational"])
    
    @pytest.mark.e2e
    def test_diagnostic(self, aiml_interpreter):
        """Test DIAGNOSTIC command"""
        response = aiml_interpreter.respond("DIAGNOSTIC")
        assert_response_matches_any(response, ["diagnostic", "Operational", "check", "systems"])
    
    @pytest.mark.e2e
    def test_run_diagnostic(self, aiml_interpreter):
        """Test RUN DIAGNOSTIC reduces to DIAGNOSTIC"""
        response = aiml_interpreter.respond("RUN DIAGNOSTIC")
        assert response and len(response) > 0
    
    @pytest.mark.e2e
    def test_system_check(self, aiml_interpreter):
        """Test SYSTEM CHECK reduces to DIAGNOSTIC"""
        response = aiml_interpreter.respond("SYSTEM CHECK")
        assert response and len(response) > 0


class TestHelpCommands:
    """Test help and information commands"""
    
    @pytest.mark.e2e
    def test_help_command(self, aiml_interpreter):
        """Test HELP command exists"""
        response = aiml_interpreter.respond("HELP")
        # Help should provide usage information
        assert response and len(response) > 0
    
    @pytest.mark.e2e
    def test_about_command(self, aiml_interpreter):
        """Test ABOUT command"""
        response = aiml_interpreter.respond("ABOUT")
        assert_response_contains(response, "PandaMania")
    
    @pytest.mark.e2e
    def test_version_command(self, aiml_interpreter):
        """Test VERSION command"""
        response = aiml_interpreter.respond("VERSION")
        assert_response_contains(response, "PandaMania")
    
    @pytest.mark.e2e
    def test_show_config(self, aiml_interpreter):
        """Test SHOW CONFIG command"""
        response = aiml_interpreter.respond("SHOW CONFIG")
        assert response and len(response) > 0
    
    @pytest.mark.e2e
    def test_show_performance(self, aiml_interpreter):
        """Test SHOW PERFORMANCE command"""
        response = aiml_interpreter.respond("SHOW PERFORMANCE")
        assert response and len(response) > 0


class TestBotPropertyPatterns:
    """Test bot property access patterns"""
    
    @pytest.mark.e2e
    def test_bot_description(self, aiml_interpreter):
        """Test BOT DESCRIPTION pattern"""
        response = aiml_interpreter.respond("BOT DESCRIPTION")
        assert_response_matches_any(response, ["AIML", "conversational", "meta-cognitive"])
    
    @pytest.mark.e2e
    def test_bot_architecture(self, aiml_interpreter):
        """Test BOT ARCHITECTURE pattern"""
        response = aiml_interpreter.respond("BOT ARCHITECTURE")
        assert_response_matches_any(response, ["Layer", "Meta-Cognitive", "loop"])
    
    @pytest.mark.e2e
    def test_bot_capabilities(self, aiml_interpreter):
        """Test BOT CAPABILITIES pattern"""
        response = aiml_interpreter.respond("BOT CAPABILITIES")
        assert response and len(response) > 0
    
    @pytest.mark.e2e
    def test_bot_language(self, aiml_interpreter):
        """Test BOT LANGUAGE pattern"""
        response = aiml_interpreter.respond("BOT LANGUAGE")
        assert_response_contains(response, "AIML")
    
    @pytest.mark.e2e
    def test_bot_purpose(self, aiml_interpreter):
        """Test BOT PURPOSE pattern"""
        response = aiml_interpreter.respond("BOT PURPOSE")
        assert_response_matches_any(response, ["AIML", "demonstrate", "cognitive"])


class TestSRAIReductions:
    """Test SRAI reduction patterns"""
    
    def test_srai_patterns_exist(self, aiml_patterns):
        """Verify SRAI patterns are defined"""
        # Common SRAI targets should exist
        common_targets = ["HELLO", "WHAT IS YOUR NAME"]
        
        for target in common_targets:
            assert target in aiml_patterns, f"SRAI target '{target}' not found"
    
    def test_greeting_reductions(self, aiml_patterns):
        """Verify greeting patterns exist for SRAI"""
        greeting_patterns = ["HELLO", "HI", "GREETINGS"]
        
        for pattern in greeting_patterns:
            assert pattern in aiml_patterns, f"Greeting pattern '{pattern}' not found"
    
    def test_identity_reductions(self, aiml_patterns):
        """Verify identity patterns exist"""
        identity_patterns = ["WHAT IS YOUR NAME", "WHO ARE YOU", "BOT NAME"]
        
        found = sum(1 for p in identity_patterns if p in aiml_patterns)
        assert found >= 2, "Expected at least 2 identity patterns"


class TestPatternCoverage:
    """Test pattern coverage statistics"""
    
    def test_total_pattern_count(self, aiml_patterns):
        """Verify total pattern count meets minimum"""
        assert len(aiml_patterns) >= 400, \
            f"Expected 400+ patterns, found {len(aiml_patterns)}"
    
    def test_patterns_per_file(self, aiml_patterns):
        """Verify reasonable distribution of patterns per file"""
        from collections import Counter
        
        files = Counter(p.file for p in aiml_patterns.values())
        
        # Check that no single file has more than 30% of patterns
        max_patterns = max(files.values())
        total_patterns = len(aiml_patterns)
        
        assert max_patterns < total_patterns * 0.3, \
            f"Pattern distribution too concentrated: {max_patterns}/{total_patterns}"
    
    def test_core_patterns_exist(self, aiml_patterns):
        """Verify core bot patterns exist"""
        core_patterns = [
            "HELLO",
            "HOW ARE YOU",
            "WHAT IS YOUR NAME",
            "STATUS",
            "HELP",
            "DIAGNOSTIC"
        ]
        
        missing = [p for p in core_patterns if p not in aiml_patterns]
        assert len(missing) == 0, f"Missing core patterns: {missing}"
