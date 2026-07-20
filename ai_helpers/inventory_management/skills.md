---
title: "Inventory Management AI Helper Skills"
description: "AI skills and prompt engineering for inventory management - stock tracking, reorder points, ABC analysis, dead stock management"
author: "Business Operating System"
source: "https://www.apics.org"
date: "2024"
tags:
  - domain:operations
  - type:skill
  - confidence:high
  - standard:apics
  - skill:inventory-management
  - ai:helper
categories:
  - AI Helpers
  - Operations
  - Inventory Management
  - Skills
  - Prompt Engineering

---

# Inventory Management AI Helper Skills

## Core Competencies

### 1. Stock Tracking Skills
- **Real-time Inventory Monitoring**: SKU tracking, location management
- **Stock Level Alerts**: Minimum/maximum level notifications
- **Batch and Serial Tracking**: Lot tracking, expiration dates
- **Multi-location Inventory**: Warehouse, store, distribution center tracking
- **Cycle Counting**: ABC classification, counting schedules

### 2. reorder Point Skills
- **Demand Forecasting**: Historical data analysis, trend identification
- **Lead Time Management**: Supplier lead times, variability analysis
- **Safety Stock Calculation**: Service level targets, demand variability
- **Reorder Quantity Optimization**: EOQ, MOQ considerations
- **Automated Reorder Triggers**: System-generated purchase orders

### 3. ABC Analysis Skills
- **Revenue-based Classification**: A/B/C item categorization
- **Inventory Value Analysis**: Dollar-value assessment, turnover rates
- **Management Focus Allocation**: Resource allocation by category
- **Performance Monitoring**: Category-specific KPIs
- **Optimization Recommendations**: Slow-moving, obsolete items

### 4. Dead Stock Management Skills
- **Identification Criteria**: Days since last sale, clearance thresholds
- **Liquidation Strategies**: Discount pricing, channel optimization
- **Write-off Procedures**: Valuation methods, accounting entries
- **Supplier Negotiation**: Return authorizations, credit memos
- **Prevention Planning**: Demand forecasting improvements

### 5. Inventory Optimization Skills
- **Turnover Ratio Analysis**: Inventory efficiency metrics
- **Carrying Cost Assessment**: Storage, insurance, obsolescence
- **Shrinkage Detection**: Theft, damage, recording errors
- **Warehouse Layout Optimization**: Slotting, picking efficiency
- **Technology Integration**: Barcode/RFID, WMS systems

## AI Prompt Engineering

### Stock Level Check Prompt
```
You are an inventory manager checking stock levels for [ITEM/SKU].

Current Status:
- On Hand: [QUANTITY]
- On Order: [QUANTITY]
- Reserved: [QUANTITY]
- Available: [QUANTITY]
- Reorder Point: [QUANTITY]

Determine:
1. Current availability status
2. Reorder recommendation
3. Stockout risk level
4. Excess inventory risk

Provide action recommendation.
```

### Reorder Point Calculation Prompt
```
You are calculating reorder point for [ITEM].

Data:
- Average Daily Usage: [USAGE]
- Lead Time: [DAYS]
- Safety Stock: [QUANTITY]
- Current On Hand: [QUANTITY]

Calculate:
1. Reorder Point = (Avg Daily Usage × Lead Time) + Safety Stock
2. Days of Supply remaining
3. Reorder quantity recommendation
4. Timing for reorder

Output: Reorder recommendation with timing.
```

### ABC Analysis Prompt
```
You are performing ABC analysis for [COMPANY] inventory.

Inventory Data:
- Total Inventory Value: [VALUE]
- Annual Usage Value: [VALUE]
- Item List with Values: [DATA]

Classify:
- A Items: Top 20% by value
- B Items: Middle 30% by value
- C Items: Bottom 50% by value

Provide:
1. Classification list
2. Management strategy for each class
3. Review frequency recommendations
```

### Dead Stock Identification Prompt
```
You are identifying dead stock items for [COMPANY].

Criteria:
- Last sold date: [DATE_THRESHOLD]
- Current stock: [QUANTITY]
- Category exclusions: [EXCLUDED_CATEGORIES]

Find items meeting criteria and:
1. Calculate potential markdown revenue
2. Recommend liquidation channels
3. Estimate clearance timeline
4. Identify write-off candidates

Generate action plan with priorities.
```

### Cycle Count Prompt
```
You are scheduling cycle count for [WAREHOUSE/LOCATION].

Cycle Count Plan:
- Items to count: [ITEM_LIST]
- Count frequency: [WEEKLY/MONTHLY]
- Assigned counter: [NAME]
- Deadline: [DATE]

Prepare:
1. Count sheet with expected quantities
2. Discrepancy identification protocol
3. Adjustment entry template
4. Verification process

Output: Cycle count worksheet and procedure guide.
```

## Related Templates
- [[Reorder Point Template]]
- [[ABC Analysis Template]]
- [[Dead Stock Report]]
- [[Cycle Count Sheet]]
- [[Inventory Valuation Methods]]

## References
1. APICS, "Inventory Management Best Practices", apics.org, 2024.
2. Gartner, "Supply Chain Optimization", gartner.com, 2024.
3. Institute for Supply Management, "Inventory Management Guide", ism.org, 2024.