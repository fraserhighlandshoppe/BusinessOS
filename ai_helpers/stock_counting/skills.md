---
title: "Stock Counting AI Helper Skills"
description: "AI skills and prompt engineering for stock counting - cycle counting, physical inventory, discrepancy resolution, barcode scanning"
author: "Business Operating System"
source: "https://www.aicpa.org"
date: "2024"
tags:
  - domain:operations
  - type:skill
  - confidence:high
  - skill:inventory-counting
  - skill:physical-inventory
  - ai:helper
categories:
  - AI Helpers
  - Operations
  - Inventory Counting
  - Skills
  - Prompt Engineering

---

# Stock Counting AI Helper Skills

## Core Competencies

### 1. Cycle Counting Skills
- **ABC Classification**: A/B/C item selection, frequency determination
- **Count Schedule Creation**: Rotating counts, team assignments
- **Count Sheet Generation**: Barcode labels, location mapping
- **Discrepancy Identification**: Variance analysis, root cause
- **Adjustment Processing**: Journal entries, account updates

### 2. Physical Inventory Skills
- **Inventory Planning**: Count team scheduling, location preparation
- **Counting Procedures**: Method selection, technique standardization
- **Real-time Recording**: Mobile device usage, cloud sync
- **Variance Analysis**: Count vs expected, shrinkage detection
- **Reconciliation**: Adjustment entries, system updates

### 3. Discrepancy Resolution Skills
- **Investigation Protocol**: Root cause analysis, documentation
- **Shrinkage Identification**: Theft, damage, error patterns
- **Correction Processing**: Write-offs, adjustments, transfers
- **Audit Trail Maintenance**: Change logs, approval documentation
- **Prevention Planning**: Process improvements, controls

### 4. Barcode Scanning Skills
- **Scanner Setup**: Device configuration, app installation
- **Barcode Generation**: SKU labels, location codes
- **Scanning Accuracy**: Error checking, duplicate prevention
- **Data Sync**: Real-time updates, cloud integration
- **Troubleshooting**: Device issues, scan failures

### 5. Inventory Accuracy Skills
- **Accuracy Metrics**: Count accuracy percentage, variance rates
- **Control Testing**: Selection sampling, validation procedures
- **Trend Analysis**: Accuracy trends, improvement tracking
- **Root Cause Analysis**: Error patterns, process gaps
- **Continuous Improvement**: Process refinement, training

## AI Prompt Engineering

### Cycle Count Schedule Prompt
```
You are creating cycle count schedule for [WAREHOUSE/LOCATION].

Inventory Summary:
- Total SKUs: [COUNT]
- A Items: [COUNT] (20% by value)
- B Items: [COUNT] (30% by value)
- C Items: [COUNT] (50% by value)
- Team Members: [COUNT]

Create schedule:
1. Weekly count rotation
2. Daily count assignments
3. Location mapping
4. Priority ranking
5. Exception handling

Output: Weekly cycle count schedule with assignments.
```

### Count Sheet Generation Prompt
```
You are generating count sheet for [LOCATION/SKU_LIST].

Items to Count:
- SKUs: [SKU_LIST]
- Locations: [LOCATION_LIST]
- Count Method: [PHYSICAL/REMOTE]
- Team: [TEAM_MEMBER]

Generate count sheet with:
1. Barcode labels for each item
2. Location mapping grid
3. Expected quantities
4. Counting columns
5. Discrepancy tracking

Output: Printable count sheet with all necessary information.
```

### Discrepancy Investigation Prompt
```
You are investigating inventory discrepancy for [SKU].

Discrepancy Details:
- Expected Qty: [EXPECTED]
- Counted Qty: [COUNTED]
- Variance: [VARIANCE]
- Location: [LOCATION]
- Last Count: [DATE]

Investigate by:
1. Reviewing recent transactions
2. Checking receiving records
3. Examining sales history
4. interviewing last personnel
5. Physical verification

Provide investigation summary with root cause and corrective actions.
```

### Physical Count Procedure Prompt
```
You are preparing physical inventory count for [PERIOD].

Count Details:
- Date: [DATE]
- Locations: [LOCATION_LIST]
- Team: [TEAM_MEMBERS]
- Equipment: [SCANNERS/DEVICES]
- Procedure: [METHOD]

Prepare:
1. Count team briefing
2. Location preparation checklist
3. Count procedure guide
4. Discrepancy handling protocol
5. Post-count reconciliation steps

Output: Comprehensive physical count procedure guide.
```

### Adjustment Entry Prompt
```
You are creating adjustment entry for inventory discrepancy.

Adjustment Details:
- SKU: [SKU]
- Location: [LOCATION]
- Expected: [EXPECTED]
- Counted: [COUNTED]
- Variance: [VARIANCE]
- Value: [VALUE]
- Reason: [REASON]

Create adjustment journal entry:
1. Debit/Credit accounts
2. Reference numbers
3. Explanation memo
4. Approval routing
5. Supporting documentation

Output: Journal entry ready for approval.
```

## Related Templates
- [[Cycle Count Sheet]]
- [[Physical Count Procedure]]
- [[Discrepancy Investigation Form]]
- [[Adjustment Entry Template]]
- [[Inventory Accuracy Report]]

## References
1. American Institute of CPAs, "Inventory Management Guide", aicpa.org, 2024.
2. Institute for Supply Management, "Physical Inventory Best Practices", ism.org, 2024.
3. Barcode Data, "Barcode Scanning Standards", barcodedata.com, 2024.