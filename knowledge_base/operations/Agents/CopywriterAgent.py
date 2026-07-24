#!/usr/bin/env python3
"""
Copywriter Agent - Creates copy variants with cross-guru perspectives
Handles opposing viewpoints by citing sources
"""
import json
import re
from pathlib import Path
from typing import Dict, List

class CopywriterAgent:
    def __init__(self):
        self.knowledge_base = Path("/home/fhs_kevin/BusinessOS/knowledge_base")
        self.copy_frameworks = self._load_copy_frameworks()
        
    async def initialize(self):
        """Initialize with copy frameworks from all gurus"""
        pass
    
    def _load_copy_frameworks(self) -> Dict:
        """Load copy frameworks from different gurus"""
        frameworks = {}
        copy_dirs = {
            'Grant Cardone': ['Sales', 'Email'],
            'Ali Brown': ['Content', 'Email'],
            'Dan Kennedy': ['Content', 'Sales'],
            'DM': ['Content', 'Email', 'Facebook', 'Social']
        }
        
        for guru, topics in copy_dirs.items():
            for topic in topics:
                topic_path = self.knowledge_base / "gurus" / guru / topic
                if topic_path.exists():
                    for file_path in topic_path.glob("*.md"):
                        if 'consolidated' in file_path.name:
                            if guru not in frameworks:
                                frameworks[guru] = {}
                            if topic not in frameworks[guru]:
                                frameworks[guru][topic] = []
                            frameworks[guru][topic].append({
                                'file': file_path,
                                'content': file_path.read_text()[:2000],  # First 2000 chars
                                'path': str(file_path.relative_to(self.knowledge_base))
                            })
        return frameworks
    
    async def create_variants(self, campaign_config: Dict) -> Dict:
        """Create copy variants referencing different guru approaches"""
        variants = {
            'grant_cardone_style': self._create_grant_cardone_variant(campaign_config),
            'ali_brown_style': self._create_ali_brown_variant(campaign_config),
            'dm_style': self._create_dm_variant(campaign_config),
            'dan_kennedy_style': self._create_dan_kennedy_variant(campaign_config),
            'unified_approach': self._create_unified_variant(campaign_config)
        }
        return variants
    
    def _create_grant_cardone_variant(self, config: Dict) -> Dict:
        """Create copy in Grant Cardone's style"""
        return {
            'style': 'aggressive, high-income focus',
            'tone': 'direct, no-nonsense',
            'key_phrases': [
                'massive action',
                'average is a failing formula',
                'multiply your efforts'
            ],
            'structure': 'Attention → Interest → Decision → Action',
            'references': [f['path'] for f in self.copy_frameworks.get('Grant Cardone', {}).get('Sales', [])[:3]]
        }
    
    def _create_ali_brown_variant(self, config: Dict) -> Dict:
        """Create copy in Ali Brown's style"""
        return {
            'style': 'feminine empowerment, authenticity',
            'tone': 'encouraging, relatable',
            'key_phrases': [
                'authentic leadership',
                'transformative growth',
                'strategic influence'
            ],
            'structure': 'Story → Problem → Solution → Invitation',
            'references': [f['path'] for f in self.copy_frameworks.get('Ali Brown', {}).get('Content', [])[:3]]
        }
    
    def _create_dm_variant(self, config: Dict) -> Dict:
        """Create copy in DigitalMarketer's style"""
        return {
            'style': 'conversion-focused, systematic',
            'tone': 'educational, results-oriented',
            'key_phrases': [
                'customer journey',
                'value optimization',
                'traffic track system'
            ],
            'structure': 'Hook → Story → Offer → CTA',
            'references': [f['path'] for f in self.copy_frameworks.get('DM', {}).get('Content', [])[:3]]
        }
    
    def _create_dan_kennedy_variant(self, config: Dict) -> Dict:
        """Create copy in Dan Kennedy's style"""
        return {
            'style': 'controversial, direct-response',
            'tone': 'provocative, contrarian',
            'key_phrases': [
                'marketing without apologies',
                'customer is always wrong until proven otherwise',
                'no such thing as a bad market'
            ],
            'structure': 'Problem Amplification → Authority Positioning → Irresistible Offer',
            'references': [f['path'] for f in self.copy_frameworks.get('Dan Kennedy', {}).get('Sales', [])[:3]]
        }
    
    def _create_unified_variant(self, config: Dict) -> Dict:
        """Create unified copy incorporating multiple perspectives"""
        # Combine the best elements from each guru
        unified = {
            'voice': 'Direct yet authentic, with clear value progression',
            'tone': 'Authoritative but relatable, action-oriented',
            'structure': 'Hook → Authority → Value → Social Proof → CTA',
            'tactics': [
                'Grant Cardone: Massive action emphasis',
                'Ali Brown: Authentic storytelling',
                'DM: Value journey mapping',
                'Dan Kennedy: Problem amplification'
            ],
            'cross_references': self._get_key_cross_references()
        }
        return unified
    
    def _get_key_cross_references(self) -> List[Dict]:
        """Get cross references showing where viewpoints differ"""
        conflicts = []
        # Example: Grant Cardone vs others on pricing
        conflicts.append({
            'topic': 'Pricing Philosophy',
            'grant_cardone': 'Charge more for perceived value',
            'ali_brown': 'Price based on transformation delivered',
            'dm': 'Price based on customer lifetime value',
            'dan_kennedy': 'Price based on market tolerance'
        })
        return conflicts

if __name__ == "__main__":
    agent = CopywriterAgent()
    print("CopywriterAgent initialized")