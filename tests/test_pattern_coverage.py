"""
Pattern Coverage Analysis Tests
Tests for analyzing and reporting pattern coverage
"""

import pytest
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set


class TestPatternCoverageAnalysis:
    """Analyze pattern coverage across the codebase"""
    
    def test_total_pattern_count(self, aiml_patterns):
        """Verify total pattern count meets target"""
        assert len(aiml_patterns) >= 400, \
            f"Expected 400+ patterns, found {len(aiml_patterns)}"
    
    def test_file_coverage(self, aiml_files):
        """Verify all expected files are present"""
        expected_files = [
            'bot.aiml',
            'config.aiml',
            'advanced_metacog.aiml',
            'topics.aiml',
            'layer4_metacog.aiml',
            'math_logic.aiml',
            'programming_tech.aiml',
            'psychology_cognition.aiml',
            'ethics_philosophy.aiml',
            'natural_language.aiml',
            'performance_optimized.aiml',
            'emotional_intelligence.aiml',
            'autognosis.aiml',
            'autognosis_commands.aiml',
            'holistic_metamodel.aiml',
            'organizational_dynamics.aiml',
            'holistic_commands.aiml',
            'session_learning.aiml',
            'knowledge_base.aiml'
        ]
        
        found_files = [Path(f).name for f in aiml_files]
        missing = [f for f in expected_files if f not in found_files]
        
        assert len(missing) == 0, f"Missing files: {missing}"
    
    def test_category_distribution(self, aiml_patterns):
        """Analyze pattern distribution by category"""
        categories = defaultdict(list)
        
        for pattern_text, pattern in aiml_patterns.items():
            file_category = pattern.file.replace('.aiml', '')
            categories[file_category].append(pattern_text)
        
        # Generate report
        report = []
        for category, patterns in sorted(categories.items()):
            report.append(f"{category}: {len(patterns)} patterns")
        
        # Print coverage report
        print("\n=== Pattern Coverage Report ===")
        for line in report:
            print(f"  {line}")
        print(f"\nTotal: {len(aiml_patterns)} patterns across {len(categories)} files")
        
        # Verify minimum coverage per category
        for category, patterns in categories.items():
            assert len(patterns) >= 5, \
                f"{category} has only {len(patterns)} patterns (expected 5+)"


class TestPatternCategories:
    """Test pattern categorization"""
    
    def test_core_category_coverage(self, aiml_patterns):
        """Verify core category patterns"""
        core_files = ['bot', 'config', 'advanced_metacog', 'topics']
        
        for core in core_files:
            patterns = [
                p for p in aiml_patterns.values() 
                if core in p.file.lower()
            ]
            assert len(patterns) >= 10, \
                f"Core file {core} has only {len(patterns)} patterns"
    
    def test_domain_category_coverage(self, aiml_patterns):
        """Verify domain category patterns"""
        domain_files = ['math_logic', 'programming_tech', 'psychology_cognition', 'ethics_philosophy']
        
        for domain in domain_files:
            patterns = [
                p for p in aiml_patterns.values() 
                if domain.replace('_', '') in p.file.lower().replace('_', '')
            ]
            assert len(patterns) >= 20, \
                f"Domain file {domain} has only {len(patterns)} patterns"
    
    def test_phase2_category_coverage(self, aiml_patterns):
        """Verify Phase 2 category patterns"""
        phase2_files = [
            'emotional_intelligence',
            'autognosis', 
            'holistic_metamodel',
            'session_learning',
            'knowledge_base'
        ]
        
        for phase2 in phase2_files:
            patterns = [
                p for p in aiml_patterns.values() 
                if phase2.replace('_', '') in p.file.lower().replace('_', '')
            ]
            assert len(patterns) >= 10, \
                f"Phase 2 file {phase2} has only {len(patterns)} patterns"


class TestPatternTypes:
    """Test different pattern types"""
    
    def test_simple_patterns(self, aiml_patterns):
        """Count simple (no wildcard) patterns"""
        simple = [
            p for p in aiml_patterns 
            if '*' not in p and '_' not in p and '^' not in p and '#' not in p
        ]
        
        total = len(aiml_patterns)
        simple_count = len(simple)
        ratio = simple_count / total if total > 0 else 0
        
        print(f"\nSimple patterns: {simple_count}/{total} ({ratio:.1%})")
        
        # Most patterns should be simple for efficiency
        assert ratio > 0.5, f"Only {ratio:.1%} simple patterns (expected >50%)"
    
    def test_wildcard_patterns(self, aiml_patterns):
        """Count wildcard patterns"""
        wildcards = {
            '*': [],
            '_': [],
            '^': [],
            '#': []
        }
        
        for pattern in aiml_patterns:
            for wc in wildcards:
                if wc in pattern:
                    wildcards[wc].append(pattern)
        
        print("\n=== Wildcard Usage ===")
        for wc, patterns in wildcards.items():
            print(f"  '{wc}': {len(patterns)} patterns")
        
        # Should have reasonable wildcard usage
        assert len(wildcards['*']) > 10, "Expected some * wildcard patterns"
    
    def test_srai_patterns(self, aiml_patterns):
        """Count patterns using SRAI"""
        srai_count = 0
        
        for pattern in aiml_patterns.values():
            if '<srai>' in pattern.template.lower():
                srai_count += 1
        
        total = len(aiml_patterns)
        ratio = srai_count / total if total > 0 else 0
        
        print(f"\nSRAI patterns: {srai_count}/{total} ({ratio:.1%})")
        
        # Should have significant SRAI usage for reductions
        assert srai_count > 50, f"Only {srai_count} SRAI patterns"


class TestPatternQuality:
    """Test pattern quality metrics"""
    
    def test_duplicate_detection(self, aiml_patterns):
        """Detect duplicate patterns"""
        seen = {}
        duplicates = []
        
        for pattern_text, pattern in aiml_patterns.items():
            key = pattern_text.strip().upper()
            if key in seen:
                duplicates.append((key, seen[key], pattern.file))
            else:
                seen[key] = pattern.file
        
        # Report duplicates (some may be intentional)
        if duplicates:
            print(f"\n=== Potential Duplicates ({len(duplicates)}) ===")
            for pattern, file1, file2 in duplicates[:10]:
                print(f"  '{pattern}' in {file1} and {file2}")
        
        # Allow some duplicates (topic overrides, etc.)
        assert len(duplicates) < 20, f"Found {len(duplicates)} duplicate patterns"
    
    def test_pattern_length_distribution(self, aiml_patterns):
        """Analyze pattern length distribution"""
        lengths = [len(p.split()) for p in aiml_patterns]
        
        avg_length = sum(lengths) / len(lengths) if lengths else 0
        max_length = max(lengths) if lengths else 0
        min_length = min(lengths) if lengths else 0
        
        print(f"\n=== Pattern Length Stats ===")
        print(f"  Avg words per pattern: {avg_length:.1f}")
        print(f"  Max words: {max_length}")
        print(f"  Min words: {min_length}")
        
        # Patterns shouldn't be excessively long
        assert max_length < 20, f"Max pattern length {max_length} is too long"
    
    def test_template_length_distribution(self, aiml_patterns):
        """Analyze template length distribution"""
        lengths = [len(p.template) for p in aiml_patterns.values()]
        
        avg_length = sum(lengths) / len(lengths) if lengths else 0
        max_length = max(lengths) if lengths else 0
        
        print(f"\n=== Template Size Stats ===")
        print(f"  Avg template size: {avg_length:.0f} chars")
        print(f"  Max template size: {max_length} chars")
        
        # Templates shouldn't be excessively large
        assert max_length < 10000, f"Max template size {max_length} is very large"


class TestCoverageReporting:
    """Generate coverage reports"""
    
    def test_generate_coverage_summary(self, aiml_patterns, aiml_files):
        """Generate comprehensive coverage summary"""
        from collections import Counter
        
        files = Counter(p.file for p in aiml_patterns.values())
        
        # Calculate metrics
        total_patterns = len(aiml_patterns)
        total_files = len(aiml_files)
        
        # Categorize patterns
        has_srai = sum(1 for p in aiml_patterns.values() if '<srai>' in p.template.lower())
        has_think = sum(1 for p in aiml_patterns.values() if '<think>' in p.template.lower())
        has_condition = sum(1 for p in aiml_patterns.values() if '<condition>' in p.template.lower())
        has_set = sum(1 for p in aiml_patterns.values() if '<set' in p.template.lower())
        has_get = sum(1 for p in aiml_patterns.values() if '<get' in p.template.lower())
        
        print("\n" + "=" * 60)
        print("PANDAMANIA PATTERN COVERAGE REPORT")
        print("=" * 60)
        print(f"\nTotal Patterns: {total_patterns}")
        print(f"Total Files: {total_files}")
        print(f"Average per File: {total_patterns/total_files:.1f}")
        print(f"\nPattern Features:")
        print(f"  - With SRAI: {has_srai} ({has_srai/total_patterns*100:.1f}%)")
        print(f"  - With <think>: {has_think} ({has_think/total_patterns*100:.1f}%)")
        print(f"  - With <condition>: {has_condition} ({has_condition/total_patterns*100:.1f}%)")
        print(f"  - With <set>: {has_set} ({has_set/total_patterns*100:.1f}%)")
        print(f"  - With <get>: {has_get} ({has_get/total_patterns*100:.1f}%)")
        print(f"\nFile Distribution:")
        for file, count in sorted(files.items(), key=lambda x: -x[1]):
            bar = "█" * (count // 5)
            print(f"  {file:<35} {count:>3} {bar}")
        print("=" * 60)
        
        # Assertions
        assert total_patterns >= 400, "Insufficient pattern coverage"
        assert total_files >= 15, "Insufficient file coverage"
        assert has_srai > 50, "Insufficient SRAI usage"
