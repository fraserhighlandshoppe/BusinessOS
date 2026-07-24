#!/usr/bin/env python3
"""
Instagram Agent - Optimizes content for Instagram with hashtag auditing
References DigitalMarketer's 2018 Social Media Resource Guide
"""
import json
import re
from pathlib import Path
from typing import Dict, List

class InstagramAgent:
    def __init__(self):
        self.knowledge_base = Path("/home/fhs_kevin/BusinessOS/knowledge_base")
        self.instagram_frameworks = self._load_instagram_frameworks()
        self.hashtag_audit = self._load_hashtag_audit_framework()
        self.compliance_rules = self._load_compliance_rules()
        
    async def initialize(self):
        pass
    
    def _load_instagram_frameworks(self) -> List[Dict]:
        frameworks = []
        ig_dirs = ['DM', 'Grant Cardone', 'Ali Brown']
        
        for guru in ig_dirs:
            guru_path = self.knowledge_base / "gurus" / guru / "Instagram"
            if guru_path.exists():
                for file_path in guru_path.glob("*.md"):
                    if 'consolidated' in file_path.name:
                        frameworks.append({
                            'guru': guru,
                            'file': file_path,
                            'content': file_path.read_text()[:2000],
                            'path': str(file_path.relative_to(self.knowledge_base))
                        })
        return frameworks
    
    def _load_hashtag_audit_framework(self) -> Dict:
        audit_path = self.knowledge_base / "gurus" / "DM" / "Social_Media_Mindmaps_Framework.md"
        if audit_path.exists():
            return {'content': audit_path.read_text()[:1000], 'path': str(audit_path)}
        return {'content': '', 'path': ''}
    
    def _load_compliance_rules(self) -> Dict:
        """Load Instagram compliance rules from framework files"""
        rules = {
            'instagram_basics': {
                'max_hashtags': 30,
                'min_hashtags': 5,
                'optimal_hashtags': 15,
                'banned_hashtags': ['#likeforlike', '#followme', '#spam', '#photography', '#picoftheday'],
                'recommended_hashtag_mix': {
                    'broad': 0.3,
                    'medium': 0.5,
                    'niche': 0.2
                }
            },
            'dm_framework': {
                'posting_frequency': {
                    'feed': ['Tue', 'Thu', 'Sat'],
                    'stories': ['Mon', 'Wed', 'Fri'],
                    'reels': ['Fri', 'Sun']
                }
            }
        }
        
        # Extract specific rules from loaded frameworks
        for framework in self.instagram_frameworks:
            content = framework['content'].lower()
            guru = framework['guru']
            
            # Look for hashtag count rules
            hashtag_match = re.search(r'(\d+)\s*(?:hashtags|tags).*?(?:optimal|recommended|max|min)', content)
            if hashtag_match:
                rules.setdefault('framework_rules', []).append({
                    'guru': guru,
                    'rule': f'Hashtag count: {hashtag_match.group(1)}',
                    'source': framework['path']
                })
            
            # Look for posting schedule rules
            if 'post' in content and ('tue' in content or 'mon' in content or 'wed' in content):
                days_found = re.findall(r'(?:mon|tue|wed|thu|fri|sat|sun)(?:day)?', content)
                if days_found:
                    rules.setdefault('framework_rules', []).append({
                        'guru': guru,
                        'rule': f'Posting days mentioned: {", ".join(set(days_found))}',
                        'source': framework['path']
                    })
        
        return rules
    
    async def optimize(self, copy_variants: Dict) -> Dict:
        optimized = {
            'caption': '',
            'hashtags': [],
            'posting_schedule': {},
            'story_content': '',
            'reel_script': '',
            'audit_results': {},
            'cross_references': []
        }
        
        optimized['caption'] = self._optimize_caption(copy_variants)
        optimized['hashtags'] = await self._audit_hashtags(copy_variants)
        
        # Merge DM framework schedule with extracted schedule rules
        optimized['posting_schedule'] = {
            'dm_base': self._get_dm_schedule(),
            'extracted_rules': self._get_extracted_schedule_rules(),
            'final_schedule': self._merge_schedules()
        }
        
        optimized['story_content'] = self._optimize_story(copy_variants)
        optimized['reel_script'] = self._optimize_reel(copy_variants)
        
        return optimized
    
    def _get_dm_schedule(self) -> Dict:
        """Get base schedule from DM framework"""
        if 'dm_framework' in self.compliance_rules:
            return self.compliance_rules['dm_framework'].get('posting_frequency', {})
        return {'feed': ['Tue', 'Thu', 'Sat'], 'stories': ['Mon', 'Wed', 'Fri'], 'reels': ['Fri', 'Sun']}
    
    def _get_extracted_schedule_rules(self) -> List[Dict]:
        """Get schedule rules extracted from frameworks"""
        return self.compliance_rules.get('framework_rules', [])
    
    def _merge_schedules(self) -> Dict:
        """Merge DM base schedule with extracted rules"""
        base = self._get_dm_schedule()
        extracted_rules = self._get_extracted_schedule_rules()
        
        # Apply extracted rules if they exist (simplified merging)
        merged = base.copy()
        for rule in extracted_rules:
            if 'posting days' in rule.get('rule', '').lower():
                days = re.findall(r'(?:mon|tue|wed|thu|fri|sat|sun)(?:day)?', rule['rule'], re.IGNORECASE)
                if days and 'feed' in merged:
                    # Use extracted days as override for feed posting
                    merged['feed'] = [d.rstrip('day') for d in days[:3]]  # Use first 3 unique days
        
        return merged
    
    def _optimize_caption(self, variants: Dict) -> str:
        return "Your breakthrough moment starts here. ✨ Tap link in bio for actionable strategies that drive real results."
    
    async def _audit_hashtags(self, variants: Dict) -> Dict:
        audit = {
            'recommended': ['#businessgrowth', '#marketingtips', '#entrepreneur'],
            'avoid': ['#likeforlike', '#followme', '#spam'],
            'niche_specific': [],
            'performance_data': {},
            'reference': self.hashtag_audit.get('path', ''),
            'rule_source': 'DM Social Media Mindmaps Framework'
        }
        
        # Check against banned hashtags from compliance rules
        banned = self.compliance_rules.get('instagram_basics', {}).get('banned_hashtags', [])
        audit['avoid'] = banned.copy()
        
        for style, variant in variants.items():
            audit['niche_specific'].extend(variant.get('key_phrases', [])[:2])
        
        return audit
    
    def _get_optimal_schedule(self) -> Dict:
        return {
            'posts': ['Tue', 'Thu', 'Sat'],
            'stories': ['Mon', 'Wed', 'Fri'],
            'reels': ['Friday morning', 'Sunday evening'],
            'based_on': 'DM Social Media Resource Guide 2018 and extracted framework rules'
        }
    
    def _optimize_story(self, variants: Dict) -> str:
        return "Behind the scenes: Today we're implementing the #ContentThatConverts framework. Swipe up for details!"
    
    def _optimize_reel(self, variants: Dict) -> str:
        return "3 Signs your marketing is stuck... and how to 10X your results! \n\n[Hook] → [Problem] → [Solution] → [CTA]"

if __name__ == "__main__":
    agent = InstagramAgent()
    print("InstagramAgent initialized")