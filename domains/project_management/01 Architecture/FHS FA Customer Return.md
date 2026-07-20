---
title: "FHS FA Customer Return"
description: "Process for handling customer returns using Customer Credit Notes in FrontAccounting - return reasons, CRM case, credit note entry"
author: "Fraser Highland Shoppe"
source: "https://frontaccounting.com"
date: "2024"
tags:
  - domain:project-management
  - type:sop
  - confidence:high
  - skill:returns
  - skill:frontaccounting
categories:
  - Project Management
  - SOP
  - Returns
  - FrontAccounting

---

# FHS FA Customer Return

## Overview
Process for handling customer returns using Customer Credit Notes in FrontAccounting.

## Return Reasons
### Valid Reasons
- Data entry error (straight return/refund)
- Doesn't fit need (knew in advance)
- Wrong size (exchange only)
- Wrong item (gift)
- Defective (warranty first)
- Buyers remorse (use TRADE/CONSIGNMENT)

## Walk-in Process

### Step 1: Create CRM Case
1. Generate case in SuiteCRM
2. Record interaction (even if denying return)
3. Create Case:
   - Product/Open/High/New
   - Select Account
   - Subject: RMA FAI123 <item name>
   - Describe why item being returned
   - Assign To
4. Save (if not immediately resolvable)

### Step 2: Verify Return Policy
1. Ensure return allowed under [[FHS Refund Policy]]
2. Advise/remind customer of policy
3. Determine restocking fees
4. Record reason in CASE

### Step 3: Locate Original Invoice
1. Customer has paper copy (ideal)
2. Look through customer transactions
3. Check documents against Account

### Step 4: Update Case
1. Locate appropriate case in SuiteCRM
2. Update RMA CASE:
   - State exchange or refund
3. Upload copy of Invoice if not associated

### Step 5: Close Case
1. Locate case in SuiteCRM
2. Actions - Edit:
   - State CLOSED
   - Resolution (Return to Manufacturer/Write-off)
3. Handle Accounting (Customer Credit Note)

## Online Process

### Step 1: Verify Policy
1. Ensure return allowed per FHS Refund Policy
2. Determine restocking fees
3. Generate CASE in SuiteCRM

### Step 2: Locate Invoice
1. Check customer transactions in FA
2. Check documents against Account

### Step 3-5: Same as Walk-in Process

## Processing a Return in FrontAccounting

### Credit Note Entry
Under SALES tab, open Customer Credit Note:

1. **Select customer**
2. **Select branch**
3. **Ensure proper price list** (SALES TYPE)
4. **Ensure correct shipping company**
5. **Select correct dimensions**
6. **Scan or enter items**

### Price Verification
Double check price is in line with returns policy (lower of):
- CURRENT RETAIL (from price book)
- SALES price
- WHAT THEY PAID (original invoice)

### Restocking Fees
Add discount percent per policy:
- 20% for original UNOPENED packaging
- 30% for opened but resellable (no wear)
- 50% for items with wear (will be USED)
- 75% for questionable resale items

### Shipping Cost
Enter $0 or negative (we don't refund shipping)

### Credit Note Type
- Select correct type
- Select store location for inventory returns

### Final Steps
1. Enter MEMO with reason and SuiteCRM CASE Number
2. Hit Process Note
3. **Print Note 2 copies**:
   - One for customer
   - One for records
4. Associate to CASE in SuiteCRM
5. Email credit note (optional)

### Post-Processing
1. Affiliate/Referral programs adjustment
2. Process Payment in FA
3. Provide refund to customer (as applicable)

## References
1. FrontAccounting, "Customer Return Documentation", frontaccounting.com, 2024.

## Related
- [[FHS Refund Policy]]
- [[FHS FA Customer Payment]]
- [[FHS FA Invoicing a Supplier Shipment]]