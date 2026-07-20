---
title: "Facebook Marketplace Strategy"
description: "Facebook Marketplace strategy for dead stock liquidation and excess inventory - listing requirements, pricing, automation"
author: "Fraser Highland Shoppe"
source: "https://www.facebook.com/business"
date: "2024"
tags:
  - domain:operations
  - type:strategy
  - confidence:high
  - skill:social-commerce
  - skill:inventory-management
categories:
  - Operations
  - Strategy
  - Social Commerce
  - Inventory Management

---

# Facebook Marketplace Strategy

For dead stock liquidation and excess inventory.

## Objectives

- Convert idle inventory to cash flow
- Reach local buyers efficiently
- Reduce warehouse holding costs
- Clear seasonal/clearance items

## Target Products

| Category | Markup Strategy | Notes |
|---|---|---|
| Practice equipment | Cost × 1.5-1.75 | High turnover |
| Reeds/accessories | Cost × 1.75 | Competitive category |
| Giftware | Cost × 1.5 | Seasonal items |
| Highland dress basics | Cost × 1.5-2.0 | Kilts, sporrans, jewelry |
| Books/CDs | Cost × 1.5 | Educational products |

## Out of Scope

- High-end bagpipes/drums (handle via direct sales)
- Custom orders
- Items requiring repair
- International shipping (local pickup only)

## Listing Requirements

### Title Format
`[Category] - [Brand] - [Model] - [Condition]`
Example: `Practice Chanter - Sirocco - Kintail - Like New`

### Description Template
```
Excellent condition [item description]. 

Originally purchased for [reason]. 
Never used / lightly used / stored in smoke-free environment.

Local pickup only from Calgary. 
Phone: [store phone] 
Serious inquiries welcome!

#HighlandDance #Bagpipes #Calgary
```

### Photo Requirements
- Minimum 3 photos
- White background for main shot
- Include scale reference
- Show any wear or defects
- Use consistent lighting

## Pricing Strategy

| Condition | Multiplier |
|---|---|
| New, unopened | Cost × 2.0 |
| Like new | Cost × 1.75 |
| Very good | Cost × 1.5 |
| Good | Cost × 1.25 |

**Minimum floor**: Cost × 1.25 for all items

## Automation Workflow

1. **Daily**: Query FA for items with `stock > 0` AND `last_sold_date < 180 days`
2. **Filter**: Exclude high-value items, reserved stock
3. **Generate**: CSV with product data + calculated prices
4. **Import**: Bulk upload to Facebook Catalog
5. **Sync**: Nightly check for sold status, update FA inventory

## Performance Tracking

- Conversion rate (inquiries to sales)
- Average days to sell
- Profit margin after fees
- Customer feedback/repeat buyers

## Compliance

- CASL compliance in descriptions
- Accurate product condition
- No prohibited items (per Facebook policy)
- Clear pickup terms

## References
1. Facebook Business, "Marketplace Selling Guide", facebook.com/business, 2024.
2. Fraser Highland Shoppe, "Facebook Marketplace Strategy", fraserhighlandshoppe.com, 2024.

## Related
- [[Facebook Marketplace Liquidation]]
- [[Inventory Lifecycle Management]]
- [[Social Media Strategy]]