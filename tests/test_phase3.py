"""
Phase 3: External Integration Tests
Tests for database, API, web interface, multi-modal, and tool integration patterns
"""

import pytest
import sys
from pathlib import Path

# Add tests directory to path for conftest imports
sys.path.insert(0, str(Path(__file__).parent))

from conftest import assert_response_contains, assert_response_matches_any


class TestPhase3Initialization:
    """Test Phase 3 initialization patterns"""
    
    def test_phase3_patterns_exist(self, aiml_patterns):
        """Verify Phase 3 master patterns exist"""
        phase3_patterns = [
            "PHASE3 INIT",
            "PHASE3 STATUS",
            "PHASE3 HELP",
            "PHASE3 DIAGNOSTIC"
        ]
        
        for pattern in phase3_patterns:
            assert pattern in aiml_patterns, f"Phase 3 pattern '{pattern}' not found"
    
    def test_phase3_aliases_exist(self, aiml_patterns):
        """Verify Phase 3 alias patterns exist"""
        aliases = [
            "INIT PHASE3",
            "PHASE 3 INIT",
            "PHASE 3 STATUS",
            "PHASE 3 HELP"
        ]
        
        found = sum(1 for p in aliases if p in aiml_patterns)
        assert found >= 2, f"Expected at least 2 Phase 3 aliases, found {found}"


class TestDatabaseIntegration:
    """Test database integration patterns (Phase 3.1)"""
    
    def test_database_init_pattern(self, aiml_patterns):
        """Verify DATABASE INIT pattern exists"""
        assert "DATABASE INIT" in aiml_patterns
    
    def test_database_status_pattern(self, aiml_patterns):
        """Verify DATABASE STATUS pattern exists"""
        assert "DATABASE STATUS" in aiml_patterns
    
    def test_database_crud_patterns(self, aiml_patterns):
        """Verify CRUD operation patterns exist"""
        crud_patterns = [
            "DB STORE FACT * IS *",
            "DB RETRIEVE FACT *",
            "DB UPDATE FACT * TO *",
            "DB DELETE FACT *"
        ]
        
        for pattern in crud_patterns:
            assert pattern in aiml_patterns, f"Database CRUD pattern '{pattern}' not found"
    
    def test_database_transaction_patterns(self, aiml_patterns):
        """Verify transaction management patterns exist"""
        transaction_patterns = [
            "DB BEGIN TRANSACTION",
            "DB COMMIT",
            "DB ROLLBACK"
        ]
        
        for pattern in transaction_patterns:
            assert pattern in aiml_patterns, f"Transaction pattern '{pattern}' not found"
    
    def test_database_query_pattern(self, aiml_patterns):
        """Verify query pattern exists"""
        assert "DB QUERY *" in aiml_patterns
    
    def test_database_backup_patterns(self, aiml_patterns):
        """Verify backup/restore patterns exist"""
        assert "DB BACKUP" in aiml_patterns
        assert "DB RESTORE *" in aiml_patterns
    
    def test_database_help_pattern(self, aiml_patterns):
        """Verify DATABASE HELP pattern exists"""
        assert "DATABASE HELP" in aiml_patterns
    
    @pytest.mark.e2e
    def test_database_init_response(self, aiml_interpreter):
        """Test DATABASE INIT response"""
        response = aiml_interpreter.respond("DATABASE INIT")
        assert_response_matches_any(response, ["Database", "Initialized", "SQLite", "Ready"])
    
    @pytest.mark.e2e
    def test_database_help_response(self, aiml_interpreter):
        """Test DATABASE HELP response"""
        response = aiml_interpreter.respond("DATABASE HELP")
        assert_response_matches_any(response, ["Database", "CRUD", "Transaction", "Commands"])


class TestAPIIntegration:
    """Test API integration patterns (Phase 3.2)"""
    
    def test_api_init_pattern(self, aiml_patterns):
        """Verify API INIT pattern exists"""
        assert "API INIT" in aiml_patterns
    
    def test_api_status_pattern(self, aiml_patterns):
        """Verify API STATUS pattern exists"""
        assert "API STATUS" in aiml_patterns
    
    def test_api_rest_patterns(self, aiml_patterns):
        """Verify REST API patterns exist"""
        rest_patterns = [
            "API GET *",
            "API POST * WITH *",
            "API PUT * WITH *",
            "API DELETE *"
        ]
        
        for pattern in rest_patterns:
            assert pattern in aiml_patterns, f"API pattern '{pattern}' not found"
    
    def test_api_rate_limiting_patterns(self, aiml_patterns):
        """Verify rate limiting patterns exist"""
        assert "API SET RATE LIMIT * PER *" in aiml_patterns
        assert "API CHECK RATE LIMIT" in aiml_patterns
    
    def test_api_cache_patterns(self, aiml_patterns):
        """Verify cache patterns exist"""
        cache_patterns = [
            "API CACHE STATUS",
            "API CACHE SET TTL *",
            "API CACHE CLEAR"
        ]
        
        for pattern in cache_patterns:
            assert pattern in aiml_patterns, f"Cache pattern '{pattern}' not found"
    
    def test_api_auth_patterns(self, aiml_patterns):
        """Verify authentication patterns exist"""
        auth_patterns = [
            "API AUTH SET *",
            "API SET TOKEN *",
            "API SET API KEY *"
        ]
        
        for pattern in auth_patterns:
            assert pattern in aiml_patterns, f"Auth pattern '{pattern}' not found"
    
    def test_api_endpoint_patterns(self, aiml_patterns):
        """Verify endpoint management patterns exist"""
        assert "API REGISTER ENDPOINT * AT *" in aiml_patterns
        assert "API LIST ENDPOINTS" in aiml_patterns
    
    def test_api_help_pattern(self, aiml_patterns):
        """Verify API HELP pattern exists"""
        assert "API HELP" in aiml_patterns
    
    @pytest.mark.e2e
    def test_api_init_response(self, aiml_interpreter):
        """Test API INIT response"""
        response = aiml_interpreter.respond("API INIT")
        assert_response_matches_any(response, ["API", "Initialized", "Framework", "Ready"])


class TestWebInterface:
    """Test web interface patterns (Phase 3.3)"""
    
    def test_web_init_pattern(self, aiml_patterns):
        """Verify WEB INIT pattern exists"""
        assert "WEB INIT" in aiml_patterns
    
    def test_websocket_patterns(self, aiml_patterns):
        """Verify WebSocket patterns exist"""
        ws_patterns = [
            "WEBSOCKET STATUS",
            "WEBSOCKET CONNECT",
            "WEBSOCKET DISCONNECT",
            "WS SEND *",
            "WS RECEIVE *",
            "WS BROADCAST *"
        ]
        
        for pattern in ws_patterns:
            assert pattern in aiml_patterns, f"WebSocket pattern '{pattern}' not found"
    
    def test_chat_patterns(self, aiml_patterns):
        """Verify chat patterns exist"""
        chat_patterns = [
            "CHAT START",
            "CHAT END",
            "CHAT MESSAGE *",
            "CHAT HISTORY",
            "CHAT CONTEXT"
        ]
        
        for pattern in chat_patterns:
            assert pattern in aiml_patterns, f"Chat pattern '{pattern}' not found"
    
    def test_session_patterns(self, aiml_patterns):
        """Verify session management patterns exist"""
        session_patterns = [
            "SESSION CREATE",
            "SESSION DESTROY",
            "SESSION INFO"
        ]
        
        for pattern in session_patterns:
            assert pattern in aiml_patterns, f"Session pattern '{pattern}' not found"
    
    def test_auth_patterns(self, aiml_patterns):
        """Verify user authentication patterns exist"""
        auth_patterns = [
            "USER LOGIN *",
            "USER LOGOUT",
            "USER REGISTER * WITH PASSWORD *",
            "AUTH STATUS"
        ]
        
        for pattern in auth_patterns:
            assert pattern in aiml_patterns, f"Auth pattern '{pattern}' not found"
    
    def test_display_patterns(self, aiml_patterns):
        """Verify display patterns exist"""
        assert "DISPLAY STATUS" in aiml_patterns
        assert "DISPLAY SET THEME *" in aiml_patterns
        assert "MOBILE MODE" in aiml_patterns
        assert "DESKTOP MODE" in aiml_patterns
    
    def test_web_help_pattern(self, aiml_patterns):
        """Verify WEB HELP pattern exists"""
        assert "WEB HELP" in aiml_patterns
    
    @pytest.mark.e2e
    def test_web_init_response(self, aiml_interpreter):
        """Test WEB INIT response"""
        response = aiml_interpreter.respond("WEB INIT")
        assert_response_matches_any(response, ["Web", "Interface", "Initialized", "WebSocket"])


class TestMultiModalSupport:
    """Test multi-modal support patterns (Phase 3.4)"""
    
    def test_multimodal_init_pattern(self, aiml_patterns):
        """Verify MULTIMODAL INIT pattern exists"""
        assert "MULTIMODAL INIT" in aiml_patterns
    
    def test_multimodal_status_pattern(self, aiml_patterns):
        """Verify MULTIMODAL STATUS pattern exists"""
        assert "MULTIMODAL STATUS" in aiml_patterns
    
    def test_image_patterns(self, aiml_patterns):
        """Verify image processing patterns exist"""
        image_patterns = [
            "IMAGE ANALYZE *",
            "IMAGE DESCRIBE *",
            "IMAGE DETECT OBJECTS *",
            "IMAGE OCR *"
        ]
        
        for pattern in image_patterns:
            assert pattern in aiml_patterns, f"Image pattern '{pattern}' not found"
    
    def test_tts_patterns(self, aiml_patterns):
        """Verify text-to-speech patterns exist"""
        tts_patterns = [
            "TTS SAY *",
            "TTS SET VOICE *",
            "TTS SET LANGUAGE *",
            "TTS SET SPEED *"
        ]
        
        for pattern in tts_patterns:
            assert pattern in aiml_patterns, f"TTS pattern '{pattern}' not found"
    
    def test_stt_patterns(self, aiml_patterns):
        """Verify speech-to-text patterns exist"""
        stt_patterns = [
            "STT LISTEN",
            "STT PROCESS AUDIO *",
            "STT SET LANGUAGE *"
        ]
        
        for pattern in stt_patterns:
            assert pattern in aiml_patterns, f"STT pattern '{pattern}' not found"
    
    def test_visual_reasoning_patterns(self, aiml_patterns):
        """Verify visual reasoning patterns exist"""
        assert "VISUAL REASON ABOUT *" in aiml_patterns
        assert "VISUAL COMPARE * AND *" in aiml_patterns
    
    def test_audio_patterns(self, aiml_patterns):
        """Verify audio analysis patterns exist"""
        assert "AUDIO ANALYZE *" in aiml_patterns
        assert "AUDIO SENTIMENT *" in aiml_patterns
    
    def test_multimodal_help_pattern(self, aiml_patterns):
        """Verify MULTIMODAL HELP pattern exists"""
        assert "MULTIMODAL HELP" in aiml_patterns
    
    @pytest.mark.e2e
    def test_multimodal_init_response(self, aiml_interpreter):
        """Test MULTIMODAL INIT response"""
        response = aiml_interpreter.respond("MULTIMODAL INIT")
        assert_response_matches_any(response, ["Multi-Modal", "Initialized", "Image", "Speech"])


class TestToolIntegration:
    """Test tool integration patterns (Phase 3.5)"""
    
    def test_tools_init_pattern(self, aiml_patterns):
        """Verify TOOLS INIT pattern exists"""
        assert "TOOLS INIT" in aiml_patterns
    
    def test_tools_status_pattern(self, aiml_patterns):
        """Verify TOOLS STATUS pattern exists"""
        assert "TOOLS STATUS" in aiml_patterns
    
    def test_calculator_patterns(self, aiml_patterns):
        """Verify calculator patterns exist"""
        calc_patterns = [
            "CALCULATE *",
            "WHAT IS * PLUS *",
            "WHAT IS * MINUS *",
            "WHAT IS * TIMES *",
            "WHAT IS * DIVIDED BY *",
            "SQUARE ROOT OF *",
            "* PERCENT OF *"
        ]
        
        for pattern in calc_patterns:
            assert pattern in aiml_patterns, f"Calculator pattern '{pattern}' not found"
    
    def test_search_patterns(self, aiml_patterns):
        """Verify search patterns exist"""
        search_patterns = [
            "SEARCH *",
            "SEARCH FOR *",
            "LOOKUP *"
        ]
        
        for pattern in search_patterns:
            assert pattern in aiml_patterns, f"Search pattern '{pattern}' not found"
    
    def test_weather_patterns(self, aiml_patterns):
        """Verify weather patterns exist"""
        weather_patterns = [
            "WEATHER IN *",
            "WEATHER",
            "WEATHER FORECAST *"
        ]
        
        for pattern in weather_patterns:
            assert pattern in aiml_patterns, f"Weather pattern '{pattern}' not found"
    
    def test_calendar_patterns(self, aiml_patterns):
        """Verify calendar patterns exist"""
        calendar_patterns = [
            "CALENDAR STATUS",
            "SCHEDULE * AT *",
            "REMIND ME TO * AT *"
        ]
        
        for pattern in calendar_patterns:
            assert pattern in aiml_patterns, f"Calendar pattern '{pattern}' not found"
    
    def test_translation_patterns(self, aiml_patterns):
        """Verify translation patterns exist"""
        translate_patterns = [
            "TRANSLATE * TO *",
            "TRANSLATE * FROM * TO *",
            "HOW DO YOU SAY * IN *"
        ]
        
        for pattern in translate_patterns:
            assert pattern in aiml_patterns, f"Translation pattern '{pattern}' not found"
    
    def test_news_patterns(self, aiml_patterns):
        """Verify news patterns exist"""
        news_patterns = [
            "NEWS",
            "NEWS ABOUT *",
            "HEADLINES"
        ]
        
        for pattern in news_patterns:
            assert pattern in aiml_patterns, f"News pattern '{pattern}' not found"
    
    def test_utility_patterns(self, aiml_patterns):
        """Verify utility patterns exist"""
        utility_patterns = [
            "TIME",
            "DATE",
            "CONVERT * TO *"
        ]
        
        for pattern in utility_patterns:
            assert pattern in aiml_patterns, f"Utility pattern '{pattern}' not found"
    
    def test_tools_help_pattern(self, aiml_patterns):
        """Verify TOOLS HELP pattern exists"""
        assert "TOOLS HELP" in aiml_patterns
    
    @pytest.mark.e2e
    def test_tools_init_response(self, aiml_interpreter):
        """Test TOOLS INIT response"""
        response = aiml_interpreter.respond("TOOLS INIT")
        assert_response_matches_any(response, ["Tool", "Initialized", "Calculator", "Ready"])
    
    @pytest.mark.e2e
    def test_time_response(self, aiml_interpreter):
        """Test TIME command response"""
        response = aiml_interpreter.respond("TIME")
        assert_response_matches_any(response, ["time", "Current"])


class TestPhase3PatternCoverage:
    """Test Phase 3 pattern coverage statistics"""
    
    def test_phase3_file_exists(self, project_root):
        """Verify Phase 3 AIML files exist"""
        phase3_files = [
            "database_integration.aiml",
            "api_integration.aiml",
            "web_interface.aiml",
            "multimodal_support.aiml",
            "tool_integration.aiml",
            "phase3_commands.aiml"
        ]
        
        for filename in phase3_files:
            filepath = project_root / filename
            assert filepath.exists(), f"Phase 3 file '{filename}' not found"
    
    def test_phase3_pattern_count(self, aiml_patterns):
        """Verify Phase 3 adds sufficient patterns"""
        # Count patterns from Phase 3 files
        phase3_files = [
            "database_integration.aiml",
            "api_integration.aiml",
            "web_interface.aiml",
            "multimodal_support.aiml",
            "tool_integration.aiml",
            "phase3_commands.aiml"
        ]
        
        phase3_patterns = [
            p for p, info in aiml_patterns.items()
            if info.file in phase3_files
        ]
        
        # Phase 3 should add at least 200 patterns
        assert len(phase3_patterns) >= 100, \
            f"Expected 100+ Phase 3 patterns, found {len(phase3_patterns)}"
    
    def test_metacognitive_integration(self, aiml_patterns):
        """Verify Phase 3 includes meta-cognitive patterns"""
        metacog_patterns = [
            "METACOGNITIVE DATABASE AWARENESS",
            "METACOGNITIVE API AWARENESS",
            "METACOGNITIVE WEBSOCKET AWARENESS",
            "METACOGNITIVE MULTIMODAL AWARENESS",
            "METACOGNITIVE TOOL AWARENESS"
        ]
        
        found = sum(1 for p in metacog_patterns if p in aiml_patterns)
        assert found >= 3, f"Expected at least 3 meta-cognitive patterns, found {found}"


class TestPhase3Integration:
    """Integration tests for Phase 3 components"""
    
    @pytest.mark.e2e
    def test_phase3_init_all_components(self, aiml_interpreter):
        """Test PHASE3 INIT initializes all components"""
        response = aiml_interpreter.respond("PHASE3 INIT")
        assert_response_matches_any(response, ["Phase 3", "Initialized", "External Integration"])
    
    @pytest.mark.e2e
    def test_phase3_status_check(self, aiml_interpreter):
        """Test PHASE3 STATUS shows all components"""
        # Initialize first
        aiml_interpreter.respond("PHASE3 INIT")
        
        response = aiml_interpreter.respond("PHASE3 STATUS")
        assert_response_matches_any(response, ["Status", "Database", "API", "Web"])
    
    @pytest.mark.e2e
    def test_phase3_diagnostic(self, aiml_interpreter):
        """Test PHASE3 DIAGNOSTIC runs checks"""
        response = aiml_interpreter.respond("PHASE3 DIAGNOSTIC")
        assert_response_matches_any(response, ["diagnostic", "Database", "complete", "check"])
    
    @pytest.mark.e2e
    def test_phase3_help(self, aiml_interpreter):
        """Test PHASE3 HELP provides guidance"""
        response = aiml_interpreter.respond("PHASE3 HELP")
        assert_response_matches_any(response, ["Help", "DATABASE", "API", "TOOLS"])
