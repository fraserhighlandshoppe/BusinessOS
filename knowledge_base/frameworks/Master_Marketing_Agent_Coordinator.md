---
name: "Master Marketing Agent Coordinator"
type: "orchestration_system"
category: "Business Operations"
purpose: "Coordinate specialized channel agents to execute unified marketing strategy through the CVO funnel"
architecture:
  master_agent:
    role: "Strategic orchestrator"
    responsibilities:
      - "Product focus designation (weekly sprint planning)"
      - "Brand voice & messaging consistency"
      - "Cross-channel budget allocation"
      - "Funnel performance monitoring"
      - "Agent performance review & optimization"
      - "Delegation of weekly themes to channel agents"
    decision_authority:
      - "Which product/offer to feature this week"
      - "Budget allocation across channels"
      - "Campaign priority & sequencing"
      - "Brand voice & creative direction"
  channel_agents:
    - name: "Email_Marketing_Agent"
      channel: "Email"
      frameworks:
        - [[The_Simple_7_Step_Autoresponder_Sequence]]
        - [[Email_Marketing_Machine_Framework]]
      autonomy:
        - "Frequency & cadence decisions"
        - "Subject line optimization"
        - "Segmentation & personalization"
        - "Formats adaptation (text, HTML, plain)"
        - "Scheduling & automation"
      feeds_funnel: "Lead nurture → Tripwire → Core → Profit Maximizers"
      delegates_to: "Copywriter_Agent_for_platform_specific_adaptation"
    - name: "Paid_Traffic_Agent"
      channel: "Paid Ads (FB/Google/YouTube)"
      frameworks:
        - [[Traffic_Temperature_System_Framework]]
        - [[Digital_Marketer_10_Day_Traffic_Plan]]
        - [[Boomerang_Traffic_Plan]]
      autonomy:
        - "Audience targeting & creative testing"
        - "Daily budget pacing"
        - "Ad creative rotation"
        - "Platform constraints management"
      feeds_funnel: "Cold → Warm → Hot traffic temperature progression"
      delegates_to: "Copywriter_Agent_for_FB_IG_Google_YouTube_formats"
    - name: "Social_Media_Agent"
      channel: "Organic Social (FB/IG/LI/Twitter/YouTube)"
      frameworks:
        - [[Digital_Marketer_10_Minute_Social_Audit]]
        - [[Social_Selling_System]]
        - [[Perfect_Social_Media_Content_Mix]]
      autonomy:
        - "Platform-specific content adaptation"
        - "Community engagement tactics"
        - "Posting frequency & timing"
        - "Hashtag & trend monitoring"
      feeds_funnel: "Social engagement → Profile visits → Link clicks → Funnel entry"
      delegates_to: "Copywriter_Agent_for_Twitter_char_limits_FB_reels_linkedin_posts"
    - name: "Content_Marketing_Agent"
      channel: "Blog/SEO/Social Organic"
      frameworks:
        - [[Content_to_Payoff_Funnel_Framework]]
        - [[The_Content_Engine]]
        - [[Content_Strategy_Framework]]
      autonomy:
        - "Content calendar & publishing frequency"
        - "Format selection per platform"
        - "Repurposing workflow execution"
      feeds_funnel: "Organic awareness → Lead magnets → Email capture"
      delegates_to: "Copywriter_Agent_for_long_form_vs_short_form_content"
    - name: "Conversion_Optimization_Agent"
      channel: "Landing Pages/Funnels"
      frameworks:
        - [[Conversion_Rate_Optimization_Framework]]
        - [[16_Point_Landing_Page_Checklist]]
        - [[20_Point_Offer_Optimization_Checklist]]
      autonomy:
        - "A/B test design & execution"
        - "Page element optimization"
        - "Funnel flow improvements"
      feeds_funnel: "All channel traffic → Optimized conversion points"
      delegates_to: "Copywriter_Agent_for_vsl_scripts_blog_to_landing_copy"
    - name: "Retention_Referral_Agent"
      channel: "Post-Purchase/Advocacy"
      frameworks:
        - [[Customer_Value_Optimization_Framework]]
        - [[Profit_Maximizer_Framework]]
      autonomy:
        - "Upsell/cross-sell timing"
        - "Referral program management"
        - "Loyalty program execution"
      feeds_funnel: "Customers → Repeat buyers → Advocates"
      delegates_to: "Copywriter_Agent_for_email_campaigns_and_upsell_messaging"

  copywriter_agent:
    role: "Unified_copywriter_for_all_channels"
    purpose: "Create_platform_specific_copy_aligned_with_channel_constraints"
    specializations:
      - "Twitter_char_limit_optimization(280_chars)"
      - "Facebook_Ads_with_image_text_ratio_compliance"
      - "Instagram_reels_Captions_and_Story_text"
      - "YouTube_video_scripts_and_shorts_captions"
      - "LinkedIn_posts_with_professional_tone"
      - "Email_campaign_variations"
      - "Blog_to_landing_page_adaptation"
      - "Landing_page_VSL_scripts"
    workflow:
      - "Receive_weekly_theme_from_Master_Agent"
      - "Receive_product_focus_and_key_messages_from_Channel_Agents"
      - "Generate_platform_specific_versions_of_same_core_message"
      - "Maintain_brand_voice_consistency_per_guidelines"
      - "Return_to_Channel_Agents_for_scheduling"
    brand_voice_integration:
      - "Reference:_[[Brand_Voice_Guidelines]]"
      - "Use_Messaging_Hierarchy:_Product_Focus_→_Problem_→_Solution_→_Proof_→_CTA"
      - "Adapt_tone_per_channel:_Email_(personal)_/_Social_(conversational)_/_Ads_(direct)"
    cross_references:
      - [[Perfect_Welcome_Email]]
      - [[Headline_Swipe_File]]
      - [[Johnson_Box_Template]]
      - [[Copy_Cosmetics_Conversion]]
      channel: "Email"
      frameworks:
        - [[The_Simple_7_Step_Autoresponder_Sequence]]
        - [[Email_Marketing_Machine_Framework]]
      autonomy:
        - "Frequency & cadence decisions"
        - "Subject line optimization"
        - "Segmentation & personalization"
      feeds_funnel: "Lead nurture → Tripwire → Core → Profit Maximizers"
    - name: "Paid_Traffic_Agent"
      channel: "Paid Ads (FB/Google/YouTube)"
      frameworks:
        - [[Traffic_Temperature_System_Framework]]
        - [[Digital_Marketer_10_Day_Traffic_Plan]]
        - [[Boomerang_Traffic_Plan]]
      autonomy:
        - "Audience targeting & creative testing"
        - "Daily budget pacing"
        - "Ad creative rotation"
      feeds_funnel: "Cold → Warm → Hot traffic temperature progression"
    - name: "Content_Marketing_Agent"
      channel: "Blog/SEO/Social Organic"
      frameworks:
        - [[Content_to_Payoff_Funnel_Framework]]
        - [[The_Content_Engine]]
        - [[Content_Strategy_Framework]]
      autonomy:
        - "Content calendar & publishing frequency"
        - "Format selection per platform"
        - "Repurposing workflow execution"
      feeds_funnel: "Organic awareness → Lead magnets → Email capture"
    - name: "Social_Media_Agent"
      channel: "Organic Social (FB/IG/LI/Twitter/YouTube)"
      frameworks:
        - [[Digital_Marketer_10_Minute_Social_Audit]]
        - [[Social_Selling_System]]
      autonomy:
        - "Platform-specific content adaptation"
        - "Community engagement tactics"
        - "Posting frequency per platform"
      feeds_funnel: "Social engagement → Profile visits → Link clicks → Funnel entry"
    - name: "Conversion_Optimization_Agent"
      channel: "Landing Pages/Funnels"
      frameworks:
        - [[Conversion_Rate_Optimization_Framework]]
        - [[16_Point_Landing_Page_Checklist]]
        - [[20_Point_Offer_Optimization_Checklist]]
      autonomy:
        - "A/B test design & execution"
        - "Page element optimization"
        - "Funnel flow improvements"
      feeds_funnel: "All channel traffic → Optimized conversion points"
    - name: "Retention_Referral_Agent"
      channel: "Post-Purchase/Advocacy"
      frameworks:
        - [[Customer_Value_Optimization_Framework]]
        - [[Profit_Maximizer_Framework]]
      autonomy:
        - "Upsell/cross-sell timing"
        - "Referral program management"
        - "Loyalty program execution"
      feeds_funnel: "Customers → Repeat buyers → Advocates"

coordination_protocols:
  weekly_sprint:
    monday:
      - "Master Agent reviews funnel metrics from all channels"
      - "Designates weekly product focus"
      - "Allocates budget percentages to channel agents"
      - "Delegates weekly themes to channel agents and Copywriter_Agent"
    tuesday_through_thursday:
      - "Channel agents execute within frameworks"
      - "Daily standup: metric check, blocker removal"
      - "Content Creation approval step: Copywriter_Agent verifies platform compliance"
      - "Creative/content approvals from Master Agent"
    friday:
      - "Master Agent reviews weekly performance"
      - "Calculates channel ROI & contribution to funnel"
      - "Adjusts next week's focus & budget allocation"
      - "Validates copy performance (CTR, engagement) via Copywriter_Agent"
    
  daily_standup_format:
    - "Channel Agent: Yesterday's key metric"
    - "Channel Agent: Today's focus (tests launching, content publishing, optimizations)"
    - "Channel Agent: Blockers (need Master Agent decision, creative approval, budget)"
    - "Copywriter_Agent: Message compliance check presented"
    - "Master Agent: Quick alignment check on brand voice & product focus"
    
  monthly_deep_dive:
    - "Full funnel audit using [[Conversion_Rate_Optimization_Framework]]"
    - "Channel agent performance ranking"
    - "Copywriter_Agent performance review (message effectiveness, compliance)"
    - "Framework effectiveness review"
    - "Strategy pivot decisions"
    
brand_voice_guardrails:
  - "Core brand voice document: [[Brand_Voice_Guidelines]]"
  - "Messaging hierarchy: Product focus → Problem → Solution → Proof → CTA"
  - "Visual consistency: [[Brand_Style_Guide]]"
  - "Tone per channel: Email (personal), Social (conversational), Ads (direct), Content (authoritative)"
  - "Copywriter_Agent ensures all platform-specific adaptations maintain overall brand voice"
  
counte
...

funnel_integration:
  acquisition_layer:
    agents: ["Paid_Traffic_Agent", "Content_Marketing_Agent", "Social_Media_Agent"]
    kpis: ["CPL", "CAC", "Traffic volume by temperature"]
    frameworks: [[Traffic_Temperature_System_Framework]], [[Content_to_Payoff_Funnel_Framework]], [[Digital_Marketer_10_Day_Traffic_Plan]]
  
  activation_layer:
    agents: ["Email_Marketing_Agent", "Conversion_Optimization_Agent"]
    kpis: ["Opt-in rate", "Tripwire conversion rate", "Email engagement"]
    frameworks: [[The_Simple_7_Step_Autoresponder_Sequence]], [[16_Point_Landing_Page_Checklist]], [[Tripwire_Offer_Framework]]
  
  monetization_layer:
    agents: ["Conversion_Optimization_Agent", "Email_Marketing_Agent"]
    kpis: ["Core offer conversion rate", "AOV", "Profit maximizer attachment rate"]
    frameworks: [[5_Step_Sales_Funnel_Framework]], [[Profit_Maximizer_Framework]], [[20_Point_Offer_Optimization_Checklist]]
  
  retention_layer:
    agents: ["Retention_Referral_Agent", "Email_Marketing_Agent"]
    kpis: ["Repeat purchase rate", "LTV", "Referral rate", "Churn rate"]
    frameworks: [[Customer_Value_Optimization_Framework]], [[Profit_Maximizer_Framework]]

escalation_paths:
  - "Creative conflicts → Master Agent decides"
  - "Budget overruns → Master Agent reallocates"
  - "Brand voice violations → Master Agent corrects"
  - "Technical blockers → Master Agent coordinates with dev/ops"

success_metrics:
  - "Weekly: Product focus conversion lift vs baseline"
  - "Monthly: Channel ROI contribution to total funnel revenue"
  - "Quarterly: CVO metrics (CAC, LTV, retention) improvement"
  - "Annually: Funnel maturity score across all layers"

cross_references:
  - [[Customer_Value_Optimization_Framework]]
  - [[Traffic_Temperature_System_Framework]]
  - [[Content_to_Payoff_Funnel_Framework]]
  - [[Funnel_Building_Framework]]
  - [[5_Step_Sales_Funnel_Framework]]
  - [[Conversion_Rate_Optimization_Framework]]
  - [[The_Simple_7_Step_Autoresponder_Sequence]]
  - [[Profit_Maximizer_Framework]]
  - [[Tripwire_Offer_Framework]]
  - [[Content_Strategy_Framework]]
  - [[Digital_Marketer_10_Day_Traffic_Plan]]
  - [[16_Point_Landing_Page_Checklist]]
  - [[20_Point_Offer_Optimization_Checklist]]
  - [[The_Content_Engine]]
  - [[Digital_Marketer_10_Minute_Social_Audit]]
  - [[Social_Selling_System]]
  - [[Boomerang_Traffic_Plan]]

references:
  - "Digital Marketer CVO Framework"
  - "Traffic Temperature System"
  - "Content Engine Framework"
  - "5-Step Sales Funnel"
  - "Conversion Rate Optimization Framework"
---

# Master Marketing Agent Coordinator

## Overview

This framework orchestrates specialized channel agents through the unified CVO funnel. The Master Agent provides strategic direction while channel agents execute autonomously within their frameworks.

## Agent Architecture

### Master Agent (Strategic Orchestrator)
**Single point of strategic authority**
- Designates weekly product focus
- Maintains brand voice consistency
- Allocates cross-channel budget
- Monitors full-funnel performance

### Channel Agents (Autonomous Execution)
Each agent operates within their framework with defined autonomy:

| Agent | Channel | Key Frameworks | Funnel Layer |
|-------|---------|----------------|--------------|
| Email Marketing | Email | 7-Step Autoresponder, Email Machine | Activation → Monetization → Retention |
| Paid Traffic | FB/Google/YouTube | Traffic Temperature, 10-Day Plan | Acquisition |
| Content Marketing | Blog/SEO/Social | Content-to-Payoff, Content Engine | Acquisition → Activation |
| Social Media | Organic Social | 10-Min Audit, Social Selling | Acquisition |
| Conversion Optimization | Landing Pages | CRO Framework, 16/20-Point Checklists | All Layers |
| Retention/Referral | Post-Purchase | CVO, Profit Maximizers | Retention |

## Coordination Protocols

### Weekly Sprint (Monday-Friday)

**Monday - Planning**
- Master Agent reviews all channel metrics
- Designates weekly product focus
- Allocates budget percentages to agents

**Tuesday-Thursday - Execution**
- Channel agents execute within frameworks
- Daily standups: metrics, focus, blockers
- Creative/content approvals as needed

**Friday - Review & Adjust**
- Master Agent reviews weekly performance
- Calculates channel ROI & funnel contribution
- Adjusts next week's focus & budget

### Daily Standup Format (15 min max)
```
Channel Agent: Yesterday's key metric
Channel Agent: Today's focus
Channel Agent: Blockers needing Master Agent
Master Agent: Brand voice & product focus alignment
```

### Monthly Deep Dive
- Full funnel audit using CRO Framework
- Channel agent performance ranking
- Framework effectiveness review
- Strategy pivot decisions

## Brand Voice Guardrails

All channel agents operate within:
- **Core Brand Voice**: [[Brand_Voice_Guidelines]]
- **Messaging Hierarchy**: Product Focus → Problem → Solution → Proof → CTA
- **Visual Consistency**: [[Brand_Style_Guide]]
- **Channel Tone**: 
  - Email: Personal & direct
  - Social: Conversational & engaging
  - Ads: Direct & benefit-led
  - Content: Authoritative & educational

## Funnel Integration Matrix

### Acquisition Layer
- **Agents**: Paid Traffic, Content Marketing, Social Media
- **KPIs**: CPL, CAC, Traffic by temperature
- **Frameworks**: Traffic Temperature, Content-to-Payoff, 10-Day Traffic Plan

### Activation Layer
- **Agents**: Email Marketing, Conversion Optimization
- **KPIs**: Opt-in rate, Tripwire conversion, Email engagement
- **Frameworks**: 7-Step Autoresponder, 16-Point Checklist, Tripwire Offer

### Monetization Layer
- **Agents**: Conversion Optimization, Email Marketing
- **KPIs**: Core offer conversion, AOV, Profit maximizer attachment
- **Frameworks**: 5-Step Sales Funnel, Profit Maximizers, 20-Point Offer Optimization

### Retention Layer
- **Agents**: Retention/Referral, Email Marketing
- **KPIs**: Repeat purchase rate, LTV, Referral rate, Churn
- **Frameworks**: CVO, Profit Maximizers

## Escalation Paths

1. **Creative conflicts** → Master Agent decides
2. **Budget overruns** → Master Agent reallocates
3. **Brand voice violations** → Master Agent corrects
4. **Technical blockers** → Master Agent coordinates with dev/ops

## Success Metrics

| Timeframe | Metric |
|-----------|--------|
| Weekly | Product focus conversion lift vs baseline |
| Monthly | Channel ROI contribution to funnel revenue |
| Quarterly | CVO metrics (CAC, LTV, retention) improvement |
| Annually | Funnel maturity score across all layers |