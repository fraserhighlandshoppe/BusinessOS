---
title: "Welcome Email Series"
description: "Three-part welcome email sequence for new subscribers - introduction, story, value and community"
author: "Fraser Highland Shoppe"
source: "https://www.mailchimp.com"
date: "2024"
tags:
  - domain:email
  - type:template
  - confidence:high
  - skill:email-marketing
  - skill:welcome-series
categories:
  - Email
  - Welcome Series
  - Templates
  - Marketing

---

# Welcome Email Series

Three-part welcome sequence for new subscribers.

## Email 1: Welcome & Introduction (sent immediately)

**Subject**: Welcome to Fraser Highland Shoppe!

**Preheader**: Your pipe band starts here.

**Content**:
```
Hi {{first_name}},

Welcome to the Fraser Highland Shoppe family!

We're Kevin and Kim — owner Pipe Major and staff — and we're thrilled to have you join our community of pipers, drummers, dancers, and Scottish culture lovers.

What you'll get from us:
• Weekly piping/drumming tips
• Early access to new products
• Event updates from Calgary games
• Special offers for our community

As a thank-you, here's 10% off your first order:
Code: WELCOME10

Best regards,
Kevin (Pipe Major)
```

**CTA**: Shop Now (link to website)

---

## Email 2: Our Story (sent 1 day later)

**Subject**: Who we are & why we started

**Preheader**: From the Saskatchewan plains to your practice room.

**Content**:
```
Hi {{first_name}},

When Rob Kinnaird (yes, our competitor!) moved to Saskatoon in 2000, he faced a problem: keeping reeds moist on the Canadian Prairies.

That frustration led to the Piper's Pal — and to us.

I started FHS in 2010 because I saw how hard it was for beginners to find quality, affordable gear in Canada. We stock what we play, recommend what we trust.

Today, we're proud to be Calgary's source for:
• Bagpipes (Henderson, MacRae, McCallum)
• Drum equipment (snare sticks, heads, cases)
• Highland Dance outfits
• Kinds & accessories

Our door is always open for questions. Just reply to this email.

- Kevin
```

**CTA**: Browse Products

---

## Email 3: Value & Community (sent 3 days later)

**Subject**: 3 tips from our shop + a question

**Preheader**: Practice smarter, not harder.

**Content**:
```
Hi {{first_name}},

Quick tip #1: Store your chanter reed in a moist reed case, not directly in your mouth.

Tip #2: Clean your practice chanter weekly with warm soapy water.

Tip #3: For new pipers: start with a medium-grade chanter before upgrading.

Question for you: What's your biggest challenge with your instrument?

Reply to this email — we love hearing from our customers.

Upcoming events:
• Calgary Highland Games: July 25-26
• Pipe Band Workshop: Aug 5

- Kim, Store Manager
```

**CTA**: View Events Calendar

## Automation Setup

**Trigger**: New subscriber added to list

**Conditions**: 
- Email address is valid
- Double opt-in confirmed

**Actions**:
1. Send Email 1 immediately
2. Wait 1 day, send Email 2
3. Wait 2 days, send Email 3

**Fallback**: If no engagement after series, move to monthly content

## References
1. Mailchimp, "Welcome Email Best Practices", mailchimp.com, 2024.
2. Fraser Highland Shoppe, "Email Marketing Strategy", fraserhighlandshoppe.com, 2024.

## Related
- [[Email Workflow]]
- [[Customer Journey Map]]
- [[Sales Funnel]]