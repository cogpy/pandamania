"""
Holistic Metamodel Tests
Tests for Eric Schwarz's organizational systems theory implementation
"""

import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from conftest import assert_response_contains, assert_response_matches_any


class TestHolisticMetamodelInitialization:
    """Test holistic metamodel initialization"""
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_metamodel_init(self, aiml_interpreter):
        """Test METAMODEL INIT command"""
        response = aiml_interpreter.respond("METAMODEL INIT")
        assert_response_matches_any(response, 
            ["Holistic", "Metamodel", "initialized", "Eric Schwarz", "hierarchical"])
    
    @pytest.mark.holistic
    def test_holistic_metamodel_file_exists(self, aiml_files):
        """Verify holistic_metamodel.aiml file exists"""
        hm_files = [f for f in aiml_files if 'holistic_metamodel' in f.lower()]
        assert len(hm_files) >= 1, "holistic_metamodel.aiml not found"
    
    @pytest.mark.holistic
    def test_organizational_dynamics_file_exists(self, aiml_files):
        """Verify organizational_dynamics.aiml file exists"""
        od_files = [f for f in aiml_files if 'organizational_dynamics' in f.lower()]
        assert len(od_files) >= 1, "organizational_dynamics.aiml not found"
    
    @pytest.mark.holistic
    def test_holistic_commands_file_exists(self, aiml_files):
        """Verify holistic_commands.aiml file exists"""
        cmd_files = [f for f in aiml_files if 'holistic_commands' in f.lower()]
        assert len(cmd_files) >= 1, "holistic_commands.aiml not found"


class TestHierarchicalLevels:
    """Test the 7 hierarchical levels (1, 2, 3, 4, 7, 9, 11)"""
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_monad_level(self, aiml_interpreter):
        """Test MONAD (The 1) - Unity Principle"""
        response = aiml_interpreter.respond("MONAD")
        assert_response_matches_any(response, 
            ["Monad", "Unity", "1", "Hieroglyphic", "principle"])
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_duality_level(self, aiml_interpreter):
        """Test DUALITY (The 2) - Dialectical Pairs"""
        response = aiml_interpreter.respond("DUALITY")
        assert_response_matches_any(response, 
            ["Duality", "2", "Dialectical", "pairs", "complementarity"])
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_triad_level(self, aiml_interpreter):
        """Test TRIAD (The 3) - Being-Becoming-Relation"""
        response = aiml_interpreter.respond("TRIAD")
        assert_response_matches_any(response, 
            ["Triad", "3", "Being", "Becoming", "Relation"])
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_cycle_level(self, aiml_interpreter):
        """Test CYCLE (The 4) - Four-Phase Developmental Cycle"""
        response = aiml_interpreter.respond("CYCLE")
        assert_response_matches_any(response, 
            ["Cycle", "4", "phase", "developmental", "emergence"])
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_production_level(self, aiml_interpreter):
        """Test PRODUCTION (The 7) - Seven-Step Triad Production"""
        response = aiml_interpreter.respond("PRODUCTION")
        assert_response_matches_any(response, 
            ["Production", "7", "step", "Triad"])
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_ennead_level(self, aiml_interpreter):
        """Test ENNEAD (The 9) - Nine Aspects Meta-System"""
        response = aiml_interpreter.respond("ENNEAD")
        assert_response_matches_any(response, 
            ["Ennead", "9", "aspects", "meta-system"])
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_helix_level(self, aiml_interpreter):
        """Test HELIX (The 11) - Evolutionary Helix"""
        response = aiml_interpreter.respond("HELIX")
        assert_response_matches_any(response, 
            ["Helix", "11", "Evolutionary", "spiral", "stages"])


class TestOrganizationalStreams:
    """Test the 3 organizational dynamic streams"""
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_entropic_stream(self, aiml_interpreter):
        """Test ENTROPIC stream"""
        response = aiml_interpreter.respond("ENTROPIC")
        assert_response_matches_any(response, 
            ["Entropic", "entropy", "auto-vortis", "auto-morphosis"])
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_negnentropic_stream(self, aiml_interpreter):
        """Test NEGNENTROPIC stream"""
        response = aiml_interpreter.respond("NEGNENTROPIC")
        assert_response_matches_any(response, 
            ["Negnentropic", "stability", "auto-stasis", "auto-poiesis", "autognosis"])
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_identity_stream(self, aiml_interpreter):
        """Test IDENTITY STREAM"""
        response = aiml_interpreter.respond("IDENTITY STREAM")
        assert_response_matches_any(response, 
            ["Identity", "self-knowledge", "auto-gnosis", "auto-genesis"])


class TestAutogenesis:
    """Test autogenesis (self-creation) capabilities"""
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_autogenesis_status(self, aiml_interpreter):
        """Test AUTOGENESIS command"""
        response = aiml_interpreter.respond("AUTOGENESIS")
        assert_response_matches_any(response, 
            ["Autogenesis", "self-creation", "threshold", "status"])
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_awaken_autogenesis(self, aiml_interpreter):
        """Test AWAKEN AUTOGENESIS command"""
        response = aiml_interpreter.respond("AWAKEN AUTOGENESIS")
        assert response and len(response) > 0


class TestMetamodelStatus:
    """Test metamodel status commands"""
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_metamodel_status(self, aiml_interpreter):
        """Test METAMODEL command"""
        response = aiml_interpreter.respond("METAMODEL")
        assert_response_matches_any(response, 
            ["Metamodel", "Holistic", "status", "active"])
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_streams_status(self, aiml_interpreter):
        """Test STREAMS command"""
        response = aiml_interpreter.respond("STREAMS")
        assert_response_matches_any(response, 
            ["Streams", "Entropic", "Negnentropic", "Identity"])
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_integration_status(self, aiml_interpreter):
        """Test INTEGRATION command"""
        response = aiml_interpreter.respond("INTEGRATION")
        assert response and len(response) > 0


class TestHolisticExplanations:
    """Test holistic theory explanations"""
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_what_is_holistic_metamodel(self, aiml_interpreter):
        """Test WHAT IS HOLISTIC METAMODEL explanation"""
        response = aiml_interpreter.respond("WHAT IS HOLISTIC METAMODEL")
        # Accept any valid response
        assert response and len(response) > 0
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_what_is_autogenesis(self, aiml_interpreter):
        """Test WHAT IS AUTOGENESIS explanation"""
        response = aiml_interpreter.respond("WHAT IS AUTOGENESIS")
        assert_response_matches_any(response, 
            ["autogenesis", "self-creation", "self-generating"])
    
    @pytest.mark.holistic
    @pytest.mark.e2e
    def test_what_is_autopoiesis(self, aiml_interpreter):
        """Test WHAT IS AUTOPOIESIS explanation"""
        response = aiml_interpreter.respond("WHAT IS AUTOPOIESIS")
        assert response and len(response) > 0


class TestHolisticPatterns:
    """Test holistic pattern structure"""
    
    @pytest.mark.holistic
    def test_holistic_pattern_count(self, aiml_patterns):
        """Verify holistic metamodel has sufficient patterns"""
        holistic_patterns = [
            p for p in aiml_patterns.values() 
            if 'holistic' in p.file.lower() or 'organizational' in p.file.lower()
        ]
        assert len(holistic_patterns) >= 50, \
            f"Expected 50+ holistic patterns, found {len(holistic_patterns)}"
    
    @pytest.mark.holistic
    def test_hierarchical_level_patterns(self, aiml_patterns):
        """Verify hierarchical level patterns exist"""
        level_patterns = ["MONAD", "DUALITY", "TRIAD", "CYCLE"]
        
        found = sum(1 for p in level_patterns if p in aiml_patterns)
        assert found >= 3, f"Expected at least 3 level patterns, found {found}"
    
    @pytest.mark.holistic
    def test_stream_patterns(self, aiml_patterns):
        """Verify stream patterns exist"""
        stream_keywords = ['ENTROPIC', 'NEGNENTROPIC', 'IDENTITY']
        
        stream_patterns = [
            p for p in aiml_patterns 
            if any(kw in p for kw in stream_keywords)
        ]
        assert len(stream_patterns) >= 2, \
            f"Expected 2+ stream patterns, found {len(stream_patterns)}"
    
    @pytest.mark.holistic
    def test_holistic_configuration(self, bot_properties):
        """Verify holistic metamodel is configured"""
        metamodel_enabled = bot_properties.get('holistic_metamodel')
        assert metamodel_enabled == 'enabled', "holistic_metamodel should be enabled"


class TestHolisticIntegration:
    """Test integration between holistic and autognosis systems"""
    
    @pytest.mark.holistic
    @pytest.mark.autognosis
    def test_autognosis_as_stability(self, bot_properties):
        """Verify autognosis is configured as ontological stability"""
        autognosis_stability = bot_properties.get('autognosis_as_stability')
        assert autognosis_stability == 'true', "autognosis should be configured as stability"
    
    @pytest.mark.holistic
    def test_autogenesis_threshold(self, bot_properties):
        """Verify autogenesis threshold is configured"""
        threshold = bot_properties.get('autogenesis_threshold')
        assert threshold is not None, "autogenesis_threshold should be configured"
        assert float(threshold) > 0, "autogenesis_threshold should be positive"
    
    @pytest.mark.holistic
    def test_stream_integration_enabled(self, bot_properties):
        """Verify stream integration is enabled"""
        stream_integration = bot_properties.get('stream_integration')
        assert stream_integration == 'enabled', "stream_integration should be enabled"
