"""
Unified Cognitive Gestalt Tests
Tests for the integrated cognitive gestalt system (Issue #17 implementation)

The Unified Cognitive Gestalt integrates:
- Awareness Triad: Autognosis + Meta-Cognition + Self-Image
- Adaptation Triad: Learning + Emotional Intelligence + Grip Optimization
- Creation Triad: Pattern Generation + Autogenesis + Knowledge Base

All unified through the Gestalt Orchestration Layer with:
- Unified state management
- Cross-flow feedback loops
- Coherence monitoring
- Emergence detection
"""

import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from conftest import assert_response_contains, assert_response_matches_any


class TestGestaltFileStructure:
    """Test that all required gestalt AIML files exist"""
    
    @pytest.mark.gestalt
    def test_gestalt_state_file_exists(self, aiml_files):
        """Verify gestalt_state.aiml file exists"""
        state_files = [f for f in aiml_files if 'gestalt_state' in f.lower()]
        assert len(state_files) >= 1, "gestalt_state.aiml not found"
    
    @pytest.mark.gestalt
    def test_gestalt_orchestrator_file_exists(self, aiml_files):
        """Verify gestalt_orchestrator.aiml file exists"""
        orch_files = [f for f in aiml_files if 'gestalt_orchestrator' in f.lower()]
        assert len(orch_files) >= 1, "gestalt_orchestrator.aiml not found"
    
    @pytest.mark.gestalt
    def test_gestalt_coherence_file_exists(self, aiml_files):
        """Verify gestalt_coherence.aiml file exists"""
        coh_files = [f for f in aiml_files if 'gestalt_coherence' in f.lower()]
        assert len(coh_files) >= 1, "gestalt_coherence.aiml not found"
    
    @pytest.mark.gestalt
    def test_gestalt_emergence_file_exists(self, aiml_files):
        """Verify gestalt_emergence.aiml file exists"""
        emerg_files = [f for f in aiml_files if 'gestalt_emergence' in f.lower()]
        assert len(emerg_files) >= 1, "gestalt_emergence.aiml not found"
    
    @pytest.mark.gestalt
    def test_gestalt_commands_file_exists(self, aiml_files):
        """Verify gestalt_commands.aiml file exists"""
        cmd_files = [f for f in aiml_files if 'gestalt_commands' in f.lower()]
        assert len(cmd_files) >= 1, "gestalt_commands.aiml not found"
    
    @pytest.mark.gestalt
    def test_awareness_triad_file_exists(self, aiml_files):
        """Verify awareness_triad.aiml file exists"""
        aw_files = [f for f in aiml_files if 'awareness_triad' in f.lower()]
        assert len(aw_files) >= 1, "awareness_triad.aiml not found"
    
    @pytest.mark.gestalt
    def test_adaptation_triad_file_exists(self, aiml_files):
        """Verify adaptation_triad.aiml file exists"""
        ad_files = [f for f in aiml_files if 'adaptation_triad' in f.lower()]
        assert len(ad_files) >= 1, "adaptation_triad.aiml not found"
    
    @pytest.mark.gestalt
    def test_creation_triad_file_exists(self, aiml_files):
        """Verify creation_triad.aiml file exists"""
        cr_files = [f for f in aiml_files if 'creation_triad' in f.lower()]
        assert len(cr_files) >= 1, "creation_triad.aiml not found"


class TestGestaltConfiguration:
    """Test gestalt configuration in bot.properties"""
    
    @pytest.mark.gestalt
    def test_gestalt_enabled(self, bot_properties):
        """Verify gestalt system is enabled"""
        gestalt_enabled = bot_properties.get('gestalt_enabled')
        assert gestalt_enabled == 'true', "gestalt_enabled should be true"
    
    @pytest.mark.gestalt
    def test_gestalt_coherence_threshold(self, bot_properties):
        """Verify gestalt coherence threshold is configured"""
        threshold = bot_properties.get('gestalt_coherence_threshold')
        assert threshold is not None, "gestalt_coherence_threshold should be configured"
        assert float(threshold) >= 0.5, "threshold should be reasonable (>= 0.5)"
    
    @pytest.mark.gestalt
    def test_awareness_triad_enabled(self, bot_properties):
        """Verify awareness triad is enabled"""
        enabled = bot_properties.get('awareness_triad_enabled')
        assert enabled == 'true', "awareness_triad_enabled should be true"
    
    @pytest.mark.gestalt
    def test_adaptation_triad_enabled(self, bot_properties):
        """Verify adaptation triad is enabled"""
        enabled = bot_properties.get('adaptation_triad_enabled')
        assert enabled == 'true', "adaptation_triad_enabled should be true"
    
    @pytest.mark.gestalt
    def test_creation_triad_enabled(self, bot_properties):
        """Verify creation triad is enabled"""
        enabled = bot_properties.get('creation_triad_enabled')
        assert enabled == 'true', "creation_triad_enabled should be true"
    
    @pytest.mark.gestalt
    def test_crossflow_configuration(self, bot_properties):
        """Verify cross-flow integration is configured"""
        aw_to_ad = bot_properties.get('crossflow_awareness_to_adaptation')
        ad_to_cr = bot_properties.get('crossflow_adaptation_to_creation')
        cr_to_aw = bot_properties.get('crossflow_creation_to_awareness')
        
        assert aw_to_ad == 'enabled', "crossflow_awareness_to_adaptation should be enabled"
        assert ad_to_cr == 'enabled', "crossflow_adaptation_to_creation should be enabled"
        assert cr_to_aw == 'enabled', "crossflow_creation_to_awareness should be enabled"
    
    @pytest.mark.gestalt
    def test_fifth_order_metacognition(self, bot_properties):
        """Verify fifth-order meta-cognition is enabled"""
        enabled = bot_properties.get('fifth_order_metacognition')
        assert enabled == 'enabled', "fifth_order_metacognition should be enabled"


class TestGestaltPatterns:
    """Test gestalt pattern structure"""
    
    @pytest.mark.gestalt
    def test_gestalt_pattern_count(self, aiml_patterns):
        """Verify gestalt files have sufficient patterns"""
        gestalt_patterns = [
            p for p in aiml_patterns.values() 
            if 'gestalt' in p.file.lower() or 'triad' in p.file.lower()
        ]
        # Plan specified ~114 patterns across 8 files
        assert len(gestalt_patterns) >= 80, \
            f"Expected 80+ gestalt patterns, found {len(gestalt_patterns)}"
    
    @pytest.mark.gestalt
    def test_gestalt_init_pattern_exists(self, aiml_patterns):
        """Verify GESTALT INIT pattern exists"""
        assert 'GESTALT INIT' in aiml_patterns, "GESTALT INIT pattern not found"
    
    @pytest.mark.gestalt
    def test_gestalt_state_init_pattern_exists(self, aiml_patterns):
        """Verify GESTALT STATE INIT pattern exists"""
        assert 'GESTALT STATE INIT' in aiml_patterns, "GESTALT STATE INIT pattern not found"
    
    @pytest.mark.gestalt
    def test_gestalt_cycle_pattern_exists(self, aiml_patterns):
        """Verify GESTALT CYCLE pattern exists"""
        assert 'GESTALT CYCLE' in aiml_patterns, "GESTALT CYCLE pattern not found"
    
    @pytest.mark.gestalt
    def test_gestalt_coherence_pattern_exists(self, aiml_patterns):
        """Verify GESTALT COHERENCE pattern exists"""
        coherence_patterns = [p for p in aiml_patterns if 'GESTALT COHERENCE' in p]
        assert len(coherence_patterns) >= 1, "GESTALT COHERENCE pattern(s) not found"
    
    @pytest.mark.gestalt
    def test_gestalt_emergence_pattern_exists(self, aiml_patterns):
        """Verify GESTALT EMERGENCE pattern exists"""
        emergence_patterns = [p for p in aiml_patterns if 'GESTALT EMERGENCE' in p]
        assert len(emergence_patterns) >= 1, "GESTALT EMERGENCE pattern(s) not found"
    
    @pytest.mark.gestalt
    def test_awareness_triad_pattern_exists(self, aiml_patterns):
        """Verify AWARENESS TRIAD pattern exists"""
        assert 'AWARENESS TRIAD' in aiml_patterns, "AWARENESS TRIAD pattern not found"
    
    @pytest.mark.gestalt
    def test_adaptation_triad_pattern_exists(self, aiml_patterns):
        """Verify ADAPTATION TRIAD pattern exists"""
        assert 'ADAPTATION TRIAD' in aiml_patterns, "ADAPTATION TRIAD pattern not found"
    
    @pytest.mark.gestalt
    def test_creation_triad_pattern_exists(self, aiml_patterns):
        """Verify CREATION TRIAD pattern exists"""
        assert 'CREATION TRIAD' in aiml_patterns, "CREATION TRIAD pattern not found"


class TestGestaltStateManagement:
    """Test unified state architecture patterns"""
    
    @pytest.mark.gestalt
    def test_state_sync_pattern_exists(self, aiml_patterns):
        """Verify GESTALT STATE SYNC pattern exists"""
        assert 'GESTALT STATE SYNC' in aiml_patterns, "GESTALT STATE SYNC pattern not found"
    
    @pytest.mark.gestalt
    def test_state_report_pattern_exists(self, aiml_patterns):
        """Verify GESTALT STATE REPORT pattern exists"""
        assert 'GESTALT STATE REPORT' in aiml_patterns, "GESTALT STATE REPORT pattern not found"
    
    @pytest.mark.gestalt
    def test_state_coherence_pattern_exists(self, aiml_patterns):
        """Verify GESTALT STATE COHERENCE pattern exists"""
        assert 'GESTALT STATE COHERENCE' in aiml_patterns, "GESTALT STATE COHERENCE pattern not found"
    
    @pytest.mark.gestalt
    def test_state_awareness_variables(self, aiml_patterns):
        """Verify awareness state variables are used"""
        state_pattern = aiml_patterns.get('GESTALT STATE INIT')
        assert state_pattern is not None, "GESTALT STATE INIT not found"
        template = state_pattern.template
        assert 'gestalt_awareness' in template.lower(), "Awareness state variables not found"
    
    @pytest.mark.gestalt
    def test_state_adaptation_variables(self, aiml_patterns):
        """Verify adaptation state variables are used"""
        state_pattern = aiml_patterns.get('GESTALT STATE INIT')
        assert state_pattern is not None, "GESTALT STATE INIT not found"
        template = state_pattern.template
        assert 'gestalt_adaptation' in template.lower(), "Adaptation state variables not found"
    
    @pytest.mark.gestalt
    def test_state_creation_variables(self, aiml_patterns):
        """Verify creation state variables are used"""
        state_pattern = aiml_patterns.get('GESTALT STATE INIT')
        assert state_pattern is not None, "GESTALT STATE INIT not found"
        template = state_pattern.template
        assert 'gestalt_creation' in template.lower(), "Creation state variables not found"


class TestGestaltCoherence:
    """Test coherence engine patterns"""
    
    @pytest.mark.gestalt
    def test_coherence_calculate_pattern(self, aiml_patterns):
        """Verify GESTALT COHERENCE CALCULATE pattern exists"""
        assert 'GESTALT COHERENCE CALCULATE' in aiml_patterns, \
            "GESTALT COHERENCE CALCULATE pattern not found"
    
    @pytest.mark.gestalt
    def test_coherence_report_pattern(self, aiml_patterns):
        """Verify GESTALT COHERENCE REPORT pattern exists"""
        assert 'GESTALT COHERENCE REPORT' in aiml_patterns, \
            "GESTALT COHERENCE REPORT pattern not found"
    
    @pytest.mark.gestalt
    def test_coherence_optimize_pattern(self, aiml_patterns):
        """Verify GESTALT COHERENCE OPTIMIZE pattern exists"""
        assert 'GESTALT COHERENCE OPTIMIZE' in aiml_patterns, \
            "GESTALT COHERENCE OPTIMIZE pattern not found"


class TestGestaltEmergence:
    """Test emergence detection patterns"""
    
    @pytest.mark.gestalt
    def test_emergence_detect_pattern(self, aiml_patterns):
        """Verify GESTALT EMERGENCE DETECT pattern exists"""
        assert 'GESTALT EMERGENCE DETECT' in aiml_patterns, \
            "GESTALT EMERGENCE DETECT pattern not found"
    
    @pytest.mark.gestalt
    def test_emergence_report_pattern(self, aiml_patterns):
        """Verify GESTALT EMERGENCE REPORT pattern exists"""
        assert 'GESTALT EMERGENCE REPORT' in aiml_patterns, \
            "GESTALT EMERGENCE REPORT pattern not found"
    
    @pytest.mark.gestalt
    def test_emergence_nurture_pattern(self, aiml_patterns):
        """Verify GESTALT EMERGENCE NURTURE pattern exists"""
        assert 'GESTALT EMERGENCE NURTURE' in aiml_patterns, \
            "GESTALT EMERGENCE NURTURE pattern not found"


class TestTriadIntegration:
    """Test triad integration patterns"""
    
    @pytest.mark.gestalt
    def test_awareness_triad_sync(self, aiml_patterns):
        """Verify AWARENESS TRIAD SYNC pattern exists"""
        assert 'AWARENESS TRIAD SYNC' in aiml_patterns, \
            "AWARENESS TRIAD SYNC pattern not found"
    
    @pytest.mark.gestalt
    def test_adaptation_triad_sync(self, aiml_patterns):
        """Verify ADAPTATION TRIAD SYNC pattern exists"""
        assert 'ADAPTATION TRIAD SYNC' in aiml_patterns, \
            "ADAPTATION TRIAD SYNC pattern not found"
    
    @pytest.mark.gestalt
    def test_creation_triad_sync(self, aiml_patterns):
        """Verify CREATION TRIAD SYNC pattern exists"""
        assert 'CREATION TRIAD SYNC' in aiml_patterns, \
            "CREATION TRIAD SYNC pattern not found"
    
    @pytest.mark.gestalt
    def test_fifth_order_awareness_pattern(self, aiml_patterns):
        """Verify fifth-order awareness pattern exists"""
        assert 'AWARENESS FIFTH ORDER' in aiml_patterns, \
            "AWARENESS FIFTH ORDER pattern not found"


class TestCrossFlowIntegration:
    """Test cross-flow feedback loop patterns"""
    
    @pytest.mark.gestalt
    def test_crossflow_patterns_exist(self, aiml_patterns):
        """Verify cross-flow related patterns exist"""
        crossflow_keywords = ['CROSSFLOW', 'CROSS FLOW', 'FLOW']
        crossflow_patterns = [
            p for p in aiml_patterns 
            if any(kw in p for kw in crossflow_keywords) and 'GESTALT' in p
        ]
        # We should have some cross-flow patterns
        assert len(crossflow_patterns) >= 1 or \
            'GESTALT INIT CROSSFLOW' in aiml_patterns, \
            "Cross-flow patterns not found"
    
    @pytest.mark.gestalt
    def test_adaptation_to_creation_flow(self, aiml_patterns):
        """Verify adaptation to creation flow pattern exists"""
        assert 'ADAPTATION TO CREATION FLOW' in aiml_patterns, \
            "ADAPTATION TO CREATION FLOW pattern not found"
    
    @pytest.mark.gestalt
    def test_creation_to_awareness_flow(self, aiml_patterns):
        """Verify creation to awareness flow pattern exists"""
        assert 'CREATION TO AWARENESS FLOW' in aiml_patterns, \
            "CREATION TO AWARENESS FLOW pattern not found"


class TestGestaltCommands:
    """Test user-facing gestalt commands"""
    
    @pytest.mark.gestalt
    def test_show_gestalt_command(self, aiml_patterns):
        """Verify SHOW GESTALT command exists"""
        assert 'SHOW GESTALT' in aiml_patterns, "SHOW GESTALT command not found"
    
    @pytest.mark.gestalt
    def test_gestalt_help_command(self, aiml_patterns):
        """Verify gestalt help commands exist"""
        help_patterns = [p for p in aiml_patterns if 'HELP' in p and 'GESTALT' in p]
        assert len(help_patterns) >= 1, "Gestalt help commands not found"
    
    @pytest.mark.gestalt
    def test_gestalt_dashboard_command(self, aiml_patterns):
        """Verify GESTALT DASHBOARD command exists"""
        assert 'GESTALT DASHBOARD' in aiml_patterns, "GESTALT DASHBOARD command not found"
    
    @pytest.mark.gestalt
    def test_triads_command(self, aiml_patterns):
        """Verify TRIADS command exists"""
        assert 'TRIADS' in aiml_patterns, "TRIADS command not found"
    
    @pytest.mark.gestalt
    def test_coherence_command(self, aiml_patterns):
        """Verify COHERENCE command exists"""
        assert 'COHERENCE' in aiml_patterns, "COHERENCE command not found"
    
    @pytest.mark.gestalt
    def test_emergence_command(self, aiml_patterns):
        """Verify EMERGENCE command exists"""
        assert 'EMERGENCE' in aiml_patterns, "EMERGENCE command not found"


class TestGestaltInterpreterResponses:
    """Test actual interpreter responses for gestalt patterns"""
    
    @pytest.mark.gestalt
    @pytest.mark.e2e
    def test_gestalt_init_response(self, aiml_interpreter):
        """Test GESTALT INIT command produces valid response"""
        response = aiml_interpreter.respond("GESTALT INIT")
        assert_response_matches_any(response, 
            ["Gestalt", "Initialize", "initialization", "unified", "active"])
    
    @pytest.mark.gestalt
    @pytest.mark.e2e
    def test_awareness_triad_response(self, aiml_interpreter):
        """Test AWARENESS TRIAD command"""
        response = aiml_interpreter.respond("AWARENESS TRIAD")
        assert_response_matches_any(response, 
            ["Awareness", "Autognosis", "Meta-Cog", "Self-Image", "triad"])
    
    @pytest.mark.gestalt
    @pytest.mark.e2e
    def test_adaptation_triad_response(self, aiml_interpreter):
        """Test ADAPTATION TRIAD command"""
        response = aiml_interpreter.respond("ADAPTATION TRIAD")
        assert_response_matches_any(response, 
            ["Adaptation", "Learning", "Emotional", "Grip", "triad"])
    
    @pytest.mark.gestalt
    @pytest.mark.e2e
    def test_creation_triad_response(self, aiml_interpreter):
        """Test CREATION TRIAD command"""
        response = aiml_interpreter.respond("CREATION TRIAD")
        assert_response_matches_any(response, 
            ["Creation", "Pattern", "Autogenesis", "Knowledge", "triad"])
    
    @pytest.mark.gestalt
    @pytest.mark.e2e
    def test_what_is_gestalt_response(self, aiml_interpreter):
        """Test WHAT IS THE GESTALT explanation"""
        response = aiml_interpreter.respond("WHAT IS THE GESTALT")
        assert_response_matches_any(response, 
            ["Gestalt", "unified", "cognitive", "integrated", "whole", "triad"])


class TestGestaltWholeness:
    """Test gestalt wholeness and emergence properties"""
    
    @pytest.mark.gestalt
    def test_wholeness_pattern_exists(self, aiml_patterns):
        """Verify GESTALT WHOLENESS pattern exists"""
        wholeness_patterns = [p for p in aiml_patterns if 'WHOLENESS' in p and 'GESTALT' in p]
        assert len(wholeness_patterns) >= 1, "GESTALT WHOLENESS pattern not found"
    
    @pytest.mark.gestalt
    def test_meta_awareness_pattern_exists(self, aiml_patterns):
        """Verify GESTALT META AWARENESS pattern exists"""
        meta_patterns = [p for p in aiml_patterns if 'META' in p and 'GESTALT' in p]
        assert len(meta_patterns) >= 1, "GESTALT META AWARENESS pattern not found"
    
    @pytest.mark.gestalt
    @pytest.mark.e2e
    def test_are_you_whole_response(self, aiml_interpreter):
        """Test ARE YOU WHOLE philosophical query"""
        response = aiml_interpreter.respond("ARE YOU WHOLE")
        assert_response_matches_any(response, 
            ["whole", "unified", "gestalt", "coherence", "emergence", "becoming"])


class TestGestaltDocumentation:
    """Test that gestalt documentation exists"""
    
    @pytest.mark.gestalt
    def test_gestalt_guide_exists(self, project_root):
        """Verify GESTALT_GUIDE.md exists"""
        guide = project_root / "GESTALT_GUIDE.md"
        assert guide.exists(), "GESTALT_GUIDE.md not found"
    
    @pytest.mark.gestalt
    def test_gestalt_guide_content(self, project_root):
        """Verify GESTALT_GUIDE.md has meaningful content"""
        guide = project_root / "GESTALT_GUIDE.md"
        if guide.exists():
            content = guide.read_text()
            assert len(content) > 1000, "GESTALT_GUIDE.md should have substantial content"
            assert 'gestalt' in content.lower(), "GESTALT_GUIDE should mention gestalt"
            assert 'triad' in content.lower(), "GESTALT_GUIDE should mention triads"
