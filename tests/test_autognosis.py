"""
Autognosis System Tests
Tests for hierarchical self-image building and self-optimization
"""

import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from conftest import assert_response_contains, assert_response_matches_any


class TestAutognosisInitialization:
    """Test autognosis system initialization"""
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_autognosis_init(self, aiml_interpreter):
        """Test AUTOGNOSIS INIT command"""
        response = aiml_interpreter.respond("AUTOGNOSIS INIT")
        assert_response_matches_any(response, 
            ["initialized", "Autognosis", "self-image", "active", "levels"])
    
    @pytest.mark.autognosis
    def test_autognosis_file_exists(self, aiml_files):
        """Verify autognosis.aiml file exists"""
        autognosis_files = [f for f in aiml_files if 'autognosis' in f.lower() and 'commands' not in f.lower()]
        assert len(autognosis_files) >= 1, "autognosis.aiml not found"
    
    @pytest.mark.autognosis
    def test_autognosis_commands_file_exists(self, aiml_files):
        """Verify autognosis_commands.aiml file exists"""
        cmd_files = [f for f in aiml_files if 'autognosis_commands' in f.lower()]
        assert len(cmd_files) >= 1, "autognosis_commands.aiml not found"


class TestAutognosisStatus:
    """Test autognosis status commands"""
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_autognosis_basic_status(self, aiml_interpreter):
        """Test AUTOGNOSIS command for basic status"""
        response = aiml_interpreter.respond("AUTOGNOSIS")
        assert_response_matches_any(response, 
            ["Autognosis", "status", "Self-Image", "running"])
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_autognosis_report(self, aiml_interpreter):
        """Test AUTOGNOSIS REPORT command"""
        response = aiml_interpreter.respond("AUTOGNOSIS REPORT")
        assert response and len(response) > 0
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_autognosis_observe(self, aiml_interpreter):
        """Test AUTOGNOSIS OBSERVE command"""
        response = aiml_interpreter.respond("AUTOGNOSIS OBSERVE")
        assert_response_matches_any(response, 
            ["Observation", "Status", "Monitoring", "Metrics"])


class TestAutognosisSelfImage:
    """Test hierarchical self-image capabilities"""
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_self_image_hierarchy(self, aiml_interpreter):
        """Test AUTOGNOSIS SELF IMAGE command"""
        response = aiml_interpreter.respond("AUTOGNOSIS SELF IMAGE")
        assert_response_matches_any(response, 
            ["Level", "Self-Image", "Hierarchy", "Confidence"])
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_self_image_level_0(self, aiml_interpreter):
        """Test AUTOGNOSIS LEVEL 0 command"""
        response = aiml_interpreter.respond("AUTOGNOSIS LEVEL 0")
        # Accept various valid responses
        assert response and len(response) > 0
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_self_image_level_1(self, aiml_interpreter):
        """Test AUTOGNOSIS LEVEL 1 command"""
        response = aiml_interpreter.respond("AUTOGNOSIS LEVEL 1")
        assert response and len(response) > 0
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_self_image_level_2(self, aiml_interpreter):
        """Test AUTOGNOSIS LEVEL 2 command"""
        response = aiml_interpreter.respond("AUTOGNOSIS LEVEL 2")
        # Accept various valid responses
        assert response and len(response) > 0
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_self_image_level_3(self, aiml_interpreter):
        """Test AUTOGNOSIS LEVEL 3 command"""
        response = aiml_interpreter.respond("AUTOGNOSIS LEVEL 3")
        assert response and len(response) > 0
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_self_image_level_4(self, aiml_interpreter):
        """Test AUTOGNOSIS LEVEL 4 command"""
        response = aiml_interpreter.respond("AUTOGNOSIS LEVEL 4")
        # Accept various valid responses
        assert response and len(response) > 0


class TestAutognosisGripOptimization:
    """Test grip optimization system"""
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_grip_status(self, aiml_interpreter):
        """Test AUTOGNOSIS GRIP command"""
        response = aiml_interpreter.respond("AUTOGNOSIS GRIP")
        assert_response_matches_any(response, 
            ["Grip", "Context", "Domain", "Semantic", "Pragmatic"])
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_context_grip(self, aiml_interpreter):
        """Test AUTOGNOSIS GRIP CONTEXT command"""
        response = aiml_interpreter.respond("AUTOGNOSIS GRIP CONTEXT")
        assert response and len(response) > 0
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_domain_grip(self, aiml_interpreter):
        """Test AUTOGNOSIS GRIP DOMAIN command"""
        response = aiml_interpreter.respond("AUTOGNOSIS GRIP DOMAIN")
        assert response and len(response) > 0
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_semantic_grip(self, aiml_interpreter):
        """Test AUTOGNOSIS GRIP SEMANTIC command"""
        response = aiml_interpreter.respond("AUTOGNOSIS GRIP SEMANTIC")
        assert response and len(response) > 0
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_pragmatic_grip(self, aiml_interpreter):
        """Test AUTOGNOSIS GRIP PRAGMATIC command"""
        response = aiml_interpreter.respond("AUTOGNOSIS GRIP PRAGMATIC")
        assert response and len(response) > 0


class TestAutognosisInsights:
    """Test meta-cognitive insight generation"""
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_insights_generation(self, aiml_interpreter):
        """Test AUTOGNOSIS INSIGHTS command"""
        response = aiml_interpreter.respond("AUTOGNOSIS INSIGHTS")
        assert_response_matches_any(response, 
            ["Insight", "Generated", "self-awareness", "pattern"])
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_awareness_assessment(self, aiml_interpreter):
        """Test AUTOGNOSIS AWARENESS command"""
        response = aiml_interpreter.respond("AUTOGNOSIS AWARENESS")
        assert_response_matches_any(response, 
            ["Awareness", "Score", "Assessment", "Self-Awareness"])


class TestAutognosisOptimization:
    """Test self-optimization capabilities"""
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_optimization_discovery(self, aiml_interpreter):
        """Test AUTOGNOSIS OPTIMIZE command"""
        response = aiml_interpreter.respond("AUTOGNOSIS OPTIMIZE")
        assert_response_matches_any(response, 
            ["Optimization", "Discovered", "Priority", "Target"])
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_apply_optimization(self, aiml_interpreter):
        """Test AUTOGNOSIS APPLY command"""
        response = aiml_interpreter.respond("AUTOGNOSIS APPLY DOMAIN GRIP")
        assert response and len(response) > 0


class TestAutognosisMonitoring:
    """Test self-monitoring capabilities"""
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_monitor_command(self, aiml_interpreter):
        """Test AUTOGNOSIS MONITOR command"""
        response = aiml_interpreter.respond("AUTOGNOSIS MONITOR")
        assert response and len(response) > 0
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_patterns_detection(self, aiml_interpreter):
        """Test AUTOGNOSIS PATTERNS command"""
        response = aiml_interpreter.respond("AUTOGNOSIS PATTERNS")
        assert response and len(response) > 0
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_anomaly_detection(self, aiml_interpreter):
        """Test AUTOGNOSIS ANOMALIES command"""
        response = aiml_interpreter.respond("AUTOGNOSIS ANOMALIES")
        assert response and len(response) > 0


class TestAutognosisAdaptation:
    """Test adaptation capabilities"""
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_adaptation_status(self, aiml_interpreter):
        """Test AUTOGNOSIS ADAPTATION command"""
        response = aiml_interpreter.respond("AUTOGNOSIS ADAPTATION")
        assert response and len(response) > 0
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_cycle_command(self, aiml_interpreter):
        """Test AUTOGNOSIS CYCLE command"""
        response = aiml_interpreter.respond("AUTOGNOSIS CYCLE")
        assert response and len(response) > 0


class TestAutognosisHelp:
    """Test autognosis help and explanation"""
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_autognosis_help(self, aiml_interpreter):
        """Test AUTOGNOSIS HELP command"""
        response = aiml_interpreter.respond("AUTOGNOSIS HELP")
        assert response and len(response) > 0
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_what_is_autognosis(self, aiml_interpreter):
        """Test WHAT IS AUTOGNOSIS explanation"""
        response = aiml_interpreter.respond("WHAT IS AUTOGNOSIS")
        assert_response_matches_any(response, 
            ["autognosis", "self-knowing", "self-awareness", "hierarchical"])
    
    @pytest.mark.autognosis
    @pytest.mark.e2e
    def test_what_is_grip(self, aiml_interpreter):
        """Test WHAT IS GRIP explanation"""
        response = aiml_interpreter.respond("WHAT IS GRIP")
        assert response and len(response) > 0


class TestAutognosisPatterns:
    """Test autognosis pattern structure"""
    
    @pytest.mark.autognosis
    def test_autognosis_pattern_count(self, aiml_patterns):
        """Verify autognosis has sufficient patterns"""
        autognosis_patterns = [
            p for p in aiml_patterns.values() 
            if 'autognosis' in p.file.lower()
        ]
        assert len(autognosis_patterns) >= 30, \
            f"Expected 30+ autognosis patterns, found {len(autognosis_patterns)}"
    
    @pytest.mark.autognosis
    def test_autognosis_commands_exist(self, aiml_patterns):
        """Verify key autognosis commands exist"""
        required_commands = [
            "AUTOGNOSIS",
            "AUTOGNOSIS INIT",
            "AUTOGNOSIS OBSERVE"
        ]
        
        missing = [cmd for cmd in required_commands if cmd not in aiml_patterns]
        assert len(missing) == 0, f"Missing autognosis commands: {missing}"
    
    @pytest.mark.autognosis
    def test_grip_variables_in_properties(self, bot_properties):
        """Verify grip optimization variables are configured"""
        grip_props = [k for k in bot_properties if 'grip' in k.lower()]
        assert len(grip_props) >= 4, \
            f"Expected 4+ grip properties, found {len(grip_props)}"
