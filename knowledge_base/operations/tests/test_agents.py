#!/usr/bin/env python3
"""
Test suite for Marketing Manager AI agents
Tests cross-agent interactions and compliance checking
"""
import asyncio
import json
import unittest
import sys
from pathlib import Path
from datetime import datetime

# Import agents
sys.path.insert(0, '/home/fhs_kevin/BusinessOS/knowledge_base/operations')

from Agents.Master_Marketing_Manager import MasterMarketingManager
from Agents.BrandAgent import BrandAgent
from Agents.CopywriterAgent import CopywriterAgent
from Agents.FBAgent import FBAgent
from Agents.InstagramAgent import InstagramAgent
from Agents.YouTubeAgent import YouTubeAgent

class TestBrandAgent(unittest.TestCase):
    def setUp(self):
        self.agent = BrandAgent()
    
    def test_brand_agent_initialization(self):
        """Test BrandAgent initializes correctly"""
        self.assertEqual(self.agent.knowledge_base, Path("/home/fhs_kevin/BusinessOS/knowledge_base"))
        self.assertIsInstance(self.agent.guru_frameworks, dict)
    
    async def test_create_brand_identity(self):
        """Test brand identity creation with multiple guru perspectives"""
        brand_config = {
            'tone': 'professional yet approachable',
            'colors': ['#FF0000', '#006400'],
            'value_prop': 'Transform your business'
        }
        
        result = await self.agent.create_brand_identity(brand_config)
        
        self.assertIn('brand_voice', result)
        self.assertIn('cross_references', result)
        self.assertGreater(len(result['cross_references']), 0)
        self.assertIn('conflicting_views', result)
    
    async def test_compliance_check(self):
        """Test compliance checking against brand guidelines"""
        content = {'text': 'Buy now with our amazing offer!'}
        result = await self.agent.check_compliance(content)
        
        self.assertIn('compliant', result)
        self.assertIn('violations', result)

class TestCopywriterAgent(unittest.TestCase):
    def setUp(self):
        self.agent = CopywriterAgent()
    
    def test_copywriter_initialization(self):
        """Test CopywriterAgent initializes correctly"""
        self.assertEqual(self.agent.knowledge_base, Path("/home/fhs_kevin/BusinessOS/knowledge_base"))
    
    async def test_create_variants(self):
        """Test creation of copy variants from multiple gurus"""
        campaign_config = {
            'campaign_name': 'Test Campaign',
            'target': 'entrepreneurs'
        }
        
        variants = await self.agent.create_variants(campaign_config)
        
        self.assertIn('grant_cardone_style', variants)
        self.assertIn('ali_brown_style', variants)
        self.assertIn('dm_style', variants)
        self.assertIn('unified_approach', variants)
        
        # Check cross-references exist
        for style in ['grant_cardone_style', 'ali_brown_style']:
            self.assertIn('cross_references', variants[style])
            self.assertGreater(len(variants[style]['cross_references']), 0)

class TestFBAgent(unittest.TestCase):
    def setUp(self):
        self.agent = FBAgent()
    
    def test_fb_agent_initialization(self):
        """Test FBAgent initializes correctly"""
        self.assertEqual(self.agent.knowledge_base, Path("/home/fhs_kevin/BusinessOS/knowledge_base"))
        self.assertIn('google_ad_library', self.agent.compliance_rules)
        self.assertIn('dm_facebook_framework', self.agent.compliance_rules)
    
    async def test_optimize(self):
        """Test Facebook optimization"""
        variants = {
            'grant_cardone_style': {'key_phrases': ['massive action', 'multiply']},
            'ali_brown_style': {'key_phrases': ['authentic', 'transformational']}
        }
        
        result = await self.agent.optimize(variants)
        
        self.assertIn('primary_text', result)
        self.assertIn('headline', result)
        self.assertIn('compliance_check', result)
        self.assertIn('cross_references', result)
    
    async def test_compliance_check(self):
        """Test Facebook compliance checking"""
        content = {
            'primary_text': 'This ad has too much text overlay',
            'headline': 'Click here now'
        }
        
        # Would normally fail text percentage check
        result = await self.agent._check_compliance(content)
        self.assertIn('compliant', result)
        
    def test_extract_max_text_percentage(self):
        """Test extraction of max text percentage from rules"""
        # Test with default
        self.assertEqual(self.agent._extract_max_text_percentage(), 20)
        
        # Test with custom rules
        self.agent.compliance_rules['dm_facebook_framework'] = {
            'best_practices': {
                'text_percentage': '< 15%'
            }
        }
        self.assertEqual(self.agent._extract_max_text_percentage(), 15)
        
        self.agent.compliance_rules['dm_facebook_framework'] = {
            'best_practices': {
                'text_percentage': '25%'
            }
        }
        self.assertEqual(self.agent._extract_max_text_percentage(), 25)

class TestInstagramAgent(unittest.TestCase):
    def setUp(self):
        self.agent = InstagramAgent()
    
    def test_instagram_agent_initialization(self):
        """Test InstagramAgent initializes correctly"""
        self.assertEqual(self.agent.knowledge_base, Path("/home/fhs_kevin/BusinessOS/knowledge_base"))
    
    async def test_optimize(self):
        """Test Instagram optimization"""
        variants = {
            'unified_approach': {'key_phrases': ['growth', 'results', 'transformation']}
        }
        
        result = await self.agent.optimize(variants)
        
        self.assertIn('caption', result)
        self.assertIn('hashtags', result)
        self.assertIn('posting_schedule', result)
        self.assertIn('audit_results', result)
        self.assertIn('reference', result['hashtags'])
    
    async def test_hashtag_audit(self):
        """Test hashtag auditing"""
        variants = {'style': 'test'}
        audit = await self.agent._audit_hashtags(variants)
        
        self.assertIn('recommended', audit)
        self.assertIn('avoid', audit)
        self.assertIn('#likeforlike', audit['avoid'])
        self.assertIn('#followme', audit['avoid'])
        self.assertIn('#spam', audit['avoid'])
        
    def test_load_compliance_rules(self):
        """Test that compliance rules are loaded from frameworks"""
        rules = self.agent.compliance_rules
        self.assertIn('instagram_basics', rules)
        self.assertIn('dm_framework', rules)
        self.assertIn('max_hashtags', rules['instagram_basics'])
        self.assertEqual(rules['instagram_basics']['max_hashtags'], 30)
        self.assertIn('banned_hashtags', rules['instagram_basics'])
        self.assertIn('#likeforlike', rules['instagram_basics']['banned_hashtags'])

class TestYouTubeAgent(unittest.TestCase):
    def setUp(self):
        self.agent = YouTubeAgent()
    
    def test_youtube_agent_initialization(self):
        """Test YouTubeAgent initializes correctly"""
        self.assertEqual(self.agent.knowledge_base, Path("/home/fhs_kevin/BusinessOS/knowledge_base"))
    
    async def test_optimize(self):
        """Test YouTube optimization"""
        campaign_config = {
            'topic': 'marketing',
            'campaign_name': 'Test Video',
            'script_style': 'template'
        }
        
        result = await self.agent.optimize(campaign_config)
        
        self.assertIn('title', result)
        self.assertIn('script', result)
        self.assertIn('seo_tags', result)
        self.assertIn('thumbnails', result)

class TestAgentIntegration(unittest.TestCase):
    def setUp(self):
        self.manager = MasterMarketingManager()
    
    async def test_full_campaign_workflow(self):
        """Test complete campaign workflow"""
        campaign_config = {
            'campaign_name': 'Integration Test',
            'target_market': 'entrepreneurs',
            'brand_guidelines': {
                'colors': ['#FF0000', '#006400'],
                'tone': 'professional yet approachable'
            },
            'posting_schedule': {
                'facebook': ['Mon', 'Wed'],
                'instagram': ['Tue', 'Fri'],
                'youtube': ['Friday morning']
            }
        }
        
        # Initialize all agents
        await self.manager.initialize_agents()
        
        # Create campaign
        result = await self.manager.create_campaign(campaign_config)
        
        # Verify all components exist
        self.assertIn('brand_check', result)
        self.assertIn('copy_variants', result)
        self.assertIn('platform_optimizations', result)
        self.assertIn('email_sequence', result)
        self.assertIn('schedule', result)
        
        # Verify platform optimizations
        platforms = ['facebook', 'instagram', 'youtube']
        for platform in platforms:
            self.assertIn(platform, result['platform_optimizations'])
    
    async def test_cross_reference_handling(self):
        """Test that conflicting viewpoints are properly documented"""
        await self.manager.initialize_agents()
        
        brand_config = {'tone': 'test'}
        result = await self.manager.agents['brand'].create_brand_identity(brand_config)
        
        # Check that cross-references exist
        self.assertGreater(len(result.get('cross_references', [])), 0)
        
        # Check if conflicts were identified
        if len(result.get('conflicting_views', [])) > 0:
            for conflict in result['conflicting_views']:
                self.assertIn('guru', conflict)
                self.assertIn('conflict', conflict)

# Helper to run async tests in unittest
def async_test(coro):
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(coro(*args, **kwargs))
    return wrapper

# Apply async_test decorator to async test methods
for test_class in [TestBrandAgent, TestCopywriterAgent, TestFBAgent, TestInstagramAgent, TestYouTubeAgent, TestAgentIntegration]:
    for method_name in dir(test_class):
        if method_name.startswith('test_') and asyncio.iscoroutinefunction(getattr(test_class, method_name)):
            setattr(test_class, method_name, async_test(getattr(test_class, method_name)))

if __name__ == "__main__":
    unittest.main()