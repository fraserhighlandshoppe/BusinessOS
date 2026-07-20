---
title: "Facebook Marketplace Dead Stock Liquidation"
description: "SOP for liquidating slow-moving inventory through Facebook Marketplace - identify, prepare, list, monitor"
author: "Business Operating System"
source: "https://www.facebook.com/business"
date: "2026"
tags:
  - domain:operations
  - type:sop
  - confidence:high
  - skill:inventory-management
  - skill:social-commerce
categories:
  - Operations
  - SOP
  - Inventory Management
  - Social Commerce

---

# SOP: Facebook Marketplace Dead Stock Liquidation

## Purpose

Liquidate slow-moving inventory through Facebook Marketplace to free up warehouse space and improve cash flow.

## Who

Marketing Operations agent, reviewed monthly by owner.

## When

- Monthly review of inventory for dead stock
- New items auto-listed when flagged
- Sold items synced nightly

## Prerequisites

1. Facebook Business Manager account with Commerce setup
2. Product media library populated in FA
3. Clearance criteria defined in FA (custom field or category)

## Procedure

### 1. Identify Dead Stock

Query FA for items matching:
```sql
SELECT sku, name, cost, stock, last_sold_date
FROM products
WHERE stock > 0
  AND (last_sold_date < DATE_SUB(NOW(), INTERVAL 180 DAY)
       OR clearance_flag = TRUE)
  AND category NOT IN ('High-end Bagpipes', 'Custom Orders')
```

### 2. Prepare Listings

For each item:
- Calculate price: `cost * 1.75` (minimum `cost * 1.5`)
- Select 3-5 high-quality photos from FA media library
- Write description: "Excellent condition, never used. Local pickup only. Serious inquiries welcome."
- Add hashtags: #HighlandDance #Bagpipes #Kilt #Calgary

### 3. Create Facebook Marketplace Listing

Using Facebook Catalog Manager:
1. Sign in to Business Manager
2. Navigate to Commerce Manager > Catalog > Products
3. Create new product:
   - Title: `[Category] - [Brand] - [Model/Sku]`
   - Price: calculated markdown
   - Condition: New/Like New/Used (as appropriate)
   - Availability: In Stock
   - Fulfillment: Local Pickup only
   - Location: Calgary, AB
   - Photos: upload from FA media folder

### 4. Monitor and Respond

- Check Marketplace messages daily
- Update status in FA when item sells
- Archive listings after 30 days if unsold

### 5. Sync Sold Items

Nightly process:
1. Export sold items from FA
2. Update stock levels to 0
3. Record sale in FA sales ledger

## Quality Checklist

- [ ] Price is `cost * 1.5` to `cost * 2.0`
- [ ] At least 3 clear photos included
- [ ] Description mentions local pickup only
- [ ] Listing includes relevant hashtags
- [ ] Item condition accurately described
- [ ] Stock level reduced when sold

## References
1. Facebook Business, "Catalog Manager Guide", facebook.com/business, 2026.

## Related
- [[BR013 Facebook Marketplace Dead Stock Liquidation]]
- [[Knowledge Base/Competitors.md]]
- [[Social Media Strategy]]

## Automation Opportunity

Script to:
1. Query FA for dead stock
2. Generate CSV for bulk import to Facebook Catalog
3. Sync sold items back to FA

## Revision History

- 2026-07-17: Initial version