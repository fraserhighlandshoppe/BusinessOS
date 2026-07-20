---
title: "Inventory Lifecycle Management"
description: "Standard operating procedure for product inventory management - lifecycle stages, dead stock, reorder points, ABC analysis"
author: "Fraser Highland Shoppe"
source: "https://fraserhighlandshoppe.com"
date: "2024"
tags:
  - domain:operations
  - type:sop
  - confidence:high
  - skill:inventory-management
  - skill:operations
categories:
  - Operations
  - SOP
  - Inventory Management
  - Supply Chain

---

# Inventory Lifecycle Management

Standard operating procedure for product inventory management.

## Product Lifecycle Stages

### 1. New Arrival
- Product received into FA
- Media/photos uploaded
- Pricing set
- Added to featured products if appropriate
- Social media announcement

### 2. Active Selling
- Regular sales
- Featured in campaigns
- Customer reviews collected
- SEO optimized

### 3. Seasonal/Declining
- Sales slowing
- Consider promotional pricing
- Bundle with other items
- Email campaigns targeted

### 4. Dead Stock
- No sales for 180+ days
- Last sold date updated
- Flag as clearance candidate
- Consider Facebook Marketplace

### 5. Discontinued
- No longer stocked
- Final sale period
- Archive from active listings
- Historical data preserved

## Dead Stock Identification

```sql
SELECT sku, name, stock, cost, price
FROM products
WHERE stock > 0
  AND (last_sold_date < DATE_SUB(NOW(), INTERVAL 180 DAY)
       OR clearance_flag = TRUE)
  AND category NOT IN ('Custom Orders')
ORDER BY days_since_sold DESC
```

## Dead Stock Liquidation Process

### Option 1: Facebook Marketplace (Primary)
1. Apply markdown pricing (cost × 1.5-1.75)
2. Create listing with high-quality photos
3. Post to local marketplace
4. Sync sales back to FA nightly

### Option 2: Internal Promotion
1. Bundle with complementary items
2. Add to newsletter promotions
3. Offer with purchase minimum
4. Staff picks promotion

### Option 3: Staff/Community
1. Staff/family discount program
2. Community group sales
3. Trade with other retailers
4. Donation for tax receipt

## Reorder Point Management

### Standard Formula
```
Reorder Point = (Avg Daily Sales × Lead Time) + Safety Stock
```

### Category-Specific
| Category | Lead Time | Safety Stock |
|---|---|---|
| Reeds | 7 days | 30 units |
| Chanters | 14 days | 20 units |
| Bagpipes | 30 days | 5 units |
| Accessories | 30 days | 50 units |
| Highland Dress | 60 days | 100 units |

## ABC Analysis

### A Items (Top 20% by revenue)
- Monitor weekly
- Frequent promotions
- Priority for new arrivals
- Detailed product pages

### B Items (Middle 30% by revenue)
- Monitor monthly
- Seasonal promotions
- Standard product pages
- Bundle opportunities

### C Items (Bottom 50% by revenue)
- Monitor quarterly
- Clearance focus
- Basic product pages
- Dead stock candidates

## Monthly Inventory Review

### Week 1: Stock Count
- Physical count of high-value items
- Spot check of A/B items
- Verify FA records match

### Week 2: Dead Stock Analysis
- Run dead stock query
- Review 180+ day items
- Prioritize for liquidation

### Week 3: Reorder Planning
- Check reorder points
- Place orders for A/B items
- Review supplier lead times

### Week 4: Performance Review
- Sales by category
- Gross margin analysis
- Inventory turnover rates

## Key Metrics

| Metric | Target | Formula |
|---|---|---|
| Inventory Turnover | 4-6x/year | COGS / Avg Inventory |
| Dead Stock % | <10% | Dead Stock Value / Total Value |
| Fill Rate | >95% | Orders Shipped / Orders Received |
| Stockout Days | <5% | Days Out of Stock / Total Days |

## Suppliers & Lead Times

| Supplier | Lead Time | MOQ | Notes |
|---|---|---|---|
| Peter Henderson | 30 days | 12 units | Direct from Scotland |
| MacRae | 14 days | 6 units | US-based |
| Kinnaird Bagpipes | 7 days | 12 units | Reeds/accessories |
| Scot's Highland | 14 days | 24 units | Ontario |

## Seasonal Planning

### Q1 (Jan-Mar)
- Post-holiday clearance
- New year resolutions (practice equipment)
- Valentine's gifts

### Q2 (Apr-Jun)
- Spring games season
- Graduation gifts
- Summer camp prep

### Q3 (Jul-Sep)
- Peak game season
- Festival season
- Back-to-school

### Q4 (Oct-Dec)
- Christmas shopping
- Holiday gifts
- Year-end clearances

## References
1. Fraser Highland Shoppe, "Inventory Management SOP", fraserhighlandshoppe.com, 2024.
2. Supply Chain Management Best Practices, supplychain.org, 2024.

## Related
- [[FHS FA Inventory Transfer]]
- [[FHS FA Receive a Shipment]]
- [[Facebook Marketplace Liquidation]]