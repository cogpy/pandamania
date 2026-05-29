"""
Performance Benchmark Tests
Tests for response time and pattern matching efficiency
"""

import pytest
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict


class TestPatternMatchingPerformance:
    """Test pattern matching performance"""
    
    @pytest.mark.performance
    @pytest.mark.slow
    def test_simple_pattern_response_time(self, aiml_interpreter):
        """Benchmark simple pattern response time"""
        # Warm up
        aiml_interpreter.respond("HELLO")
        
        # Measure
        start = time.perf_counter()
        for _ in range(100):
            aiml_interpreter.respond("HELLO")
        end = time.perf_counter()
        
        avg_time = (end - start) / 100 * 1000  # Convert to ms
        
        # Should be fast (under 50ms average)
        assert avg_time < 50, f"Average response time {avg_time:.2f}ms exceeds 50ms threshold"
    
    @pytest.mark.performance
    @pytest.mark.slow
    def test_wildcard_pattern_response_time(self, aiml_interpreter):
        """Benchmark wildcard pattern response time"""
        # Warm up
        aiml_interpreter.respond("WHAT IS RECURSION")
        
        # Measure
        start = time.perf_counter()
        for _ in range(50):
            aiml_interpreter.respond("WHAT IS SOMETHING")
        end = time.perf_counter()
        
        avg_time = (end - start) / 50 * 1000
        
        # Wildcards may be slower but should still be reasonable
        assert avg_time < 100, f"Average wildcard response time {avg_time:.2f}ms exceeds 100ms"
    
    @pytest.mark.performance
    @pytest.mark.slow
    def test_srai_chain_response_time(self, aiml_interpreter):
        """Benchmark SRAI chain response time"""
        # HOW ARE YOU triggers SRAI chain
        start = time.perf_counter()
        for _ in range(50):
            aiml_interpreter.respond("HOW ARE YOU")
        end = time.perf_counter()
        
        avg_time = (end - start) / 50 * 1000
        
        # SRAI chains may be slower but should complete
        assert avg_time < 200, f"Average SRAI chain time {avg_time:.2f}ms exceeds 200ms"


class TestMemoryUsage:
    """Test memory efficiency"""
    
    @pytest.mark.performance
    def test_pattern_load_count(self, aiml_patterns):
        """Verify patterns load within expected count"""
        count = len(aiml_patterns)
        
        # Should have reasonable number of patterns
        assert count >= 400, f"Expected 400+ patterns, got {count}"
        assert count < 2000, f"Pattern count {count} may indicate redundancy"
    
    @pytest.mark.performance
    def test_variable_count_reasonable(self, aiml_interpreter):
        """Test that variable count stays reasonable"""
        # Run some interactions
        aiml_interpreter.respond("SYSTEM INIT")
        aiml_interpreter.respond("HELLO")
        aiml_interpreter.respond("HOW ARE YOU")
        aiml_interpreter.respond("WHAT ARE YOU THINKING")
        
        # Check variable count
        var_count = len(aiml_interpreter.variables)
        
        # Should have reasonable number of variables
        assert var_count < 100, f"Variable count {var_count} may indicate memory leak"


class TestFileLoadPerformance:
    """Test file loading performance"""
    
    @pytest.mark.performance
    def test_xml_parse_time(self, aiml_files):
        """Benchmark XML parsing time"""
        total_time = 0
        
        for filepath in aiml_files:
            start = time.perf_counter()
            tree = ET.parse(filepath)
            root = tree.getroot()
            _ = len(root.findall('.//category'))
            end = time.perf_counter()
            
            total_time += (end - start)
        
        # All files should parse quickly (under 1 second total)
        assert total_time < 1.0, f"Total parse time {total_time:.2f}s exceeds 1s"
    
    @pytest.mark.performance
    def test_pattern_extraction_time(self, aiml_files):
        """Benchmark pattern extraction time"""
        start = time.perf_counter()
        
        patterns = []
        for filepath in aiml_files:
            tree = ET.parse(filepath)
            root = tree.getroot()
            
            for cat in root.findall('.//category'):
                pattern = cat.find('pattern')
                if pattern is not None:
                    patterns.append(''.join(pattern.itertext()))
        
        end = time.perf_counter()
        
        # Should extract quickly
        assert (end - start) < 0.5, f"Pattern extraction took {end-start:.2f}s"
        assert len(patterns) >= 400, f"Expected 400+ patterns, got {len(patterns)}"


class TestPatternDistribution:
    """Test pattern distribution efficiency"""
    
    @pytest.mark.performance
    def test_file_size_distribution(self, aiml_files):
        """Test that AIML files are reasonably sized"""
        sizes = []
        
        for filepath in aiml_files:
            size = Path(filepath).stat().st_size
            sizes.append((Path(filepath).name, size))
        
        # No single file should be more than 100KB (allowing for larger feature files)
        for name, size in sizes:
            assert size < 100000, f"{name} is {size} bytes, exceeds 100KB"
    
    @pytest.mark.performance
    def test_patterns_per_file_distribution(self, aiml_patterns):
        """Test pattern distribution across files"""
        from collections import Counter
        
        files = Counter(p.file for p in aiml_patterns.values())
        
        # Calculate statistics
        counts = list(files.values())
        avg_patterns = sum(counts) / len(counts)
        max_patterns = max(counts)
        min_patterns = min(counts)
        
        # Should have reasonable distribution
        assert max_patterns < 100, f"Max patterns per file ({max_patterns}) is too high"
        assert avg_patterns > 10, f"Average patterns per file ({avg_patterns:.1f}) is too low"
    
    @pytest.mark.performance
    def test_wildcard_usage(self, aiml_patterns):
        """Test wildcard pattern usage"""
        wildcard_patterns = [
            p for p in aiml_patterns 
            if '*' in p or '_' in p or '^' in p or '#' in p
        ]
        
        total = len(aiml_patterns)
        wildcards = len(wildcard_patterns)
        ratio = wildcards / total if total > 0 else 0
        
        # Wildcards should be minority but present
        assert ratio < 0.5, f"Wildcard ratio {ratio:.2%} is too high"
        assert wildcards > 10, f"Expected more wildcard patterns, got {wildcards}"


class TestSRAIEfficiency:
    """Test SRAI chain efficiency"""
    
    @pytest.mark.performance
    def test_srai_target_coverage(self, aiml_patterns):
        """Test that SRAI targets are defined"""
        srai_targets = set()
        defined_patterns = set(aiml_patterns.keys())
        
        for pattern_text, pattern in aiml_patterns.items():
            template = pattern.template
            # Extract SRAI targets
            import re
            matches = re.findall(r'<srai>([^<]+)</srai>', template)
            for match in matches:
                # Normalize
                target = match.strip().upper()
                # Remove wildcards for comparison
                target = ' '.join(p for p in target.split() if p not in ['*', '_', '^', '#'])
                if target:
                    srai_targets.add(target)
        
        # Check coverage
        undefined = srai_targets - defined_patterns
        coverage = 1 - (len(undefined) / len(srai_targets)) if srai_targets else 1
        
        # Should have high coverage (some may be dynamic)
        assert coverage > 0.5, f"SRAI target coverage is only {coverage:.1%}"
    
    @pytest.mark.performance
    def test_srai_chain_depth(self, aiml_patterns):
        """Test that SRAI chains don't get too deep"""
        import re
        
        # Build dependency graph
        dependencies = {}
        for pattern_text, pattern in aiml_patterns.items():
            template = pattern.template
            matches = re.findall(r'<srai>([^<]+)</srai>', template)
            targets = []
            for match in matches:
                target = match.strip().upper()
                target = ' '.join(p for p in target.split() if p not in ['*', '_', '^', '#'])
                if target:
                    targets.append(target)
            dependencies[pattern_text] = targets
        
        # Check for very long chains
        def get_depth(pattern, visited=None):
            if visited is None:
                visited = set()
            if pattern in visited:
                return 0  # Cycle detected
            if pattern not in dependencies:
                return 0
            
            visited.add(pattern)
            targets = dependencies[pattern]
            if not targets:
                return 0
            
            return 1 + max(get_depth(t, visited.copy()) for t in targets)
        
        max_depth = 0
        for pattern in dependencies:
            depth = get_depth(pattern)
            max_depth = max(max_depth, depth)
        
        # Chains shouldn't be excessively deep
        assert max_depth < 10, f"Max SRAI chain depth {max_depth} is too deep"


class TestBenchmarkResults:
    """Collect and report benchmark results"""
    
    @pytest.mark.performance
    def test_overall_pattern_stats(self, aiml_patterns, aiml_files):
        """Report overall pattern statistics"""
        from collections import Counter
        
        total_patterns = len(aiml_patterns)
        total_files = len(aiml_files)
        
        files = Counter(p.file for p in aiml_patterns.values())
        
        stats = {
            'total_patterns': total_patterns,
            'total_files': total_files,
            'avg_patterns_per_file': total_patterns / total_files,
            'max_patterns_file': max(files.items(), key=lambda x: x[1]),
            'min_patterns_file': min(files.items(), key=lambda x: x[1]),
        }
        
        # Just verify we can collect stats
        assert stats['total_patterns'] >= 400
        assert stats['total_files'] >= 15
        
        # Print stats for reference
        print(f"\n=== Pattern Statistics ===")
        print(f"Total patterns: {stats['total_patterns']}")
        print(f"Total files: {stats['total_files']}")
        print(f"Avg per file: {stats['avg_patterns_per_file']:.1f}")
        print(f"Max: {stats['max_patterns_file']}")
        print(f"Min: {stats['min_patterns_file']}")
