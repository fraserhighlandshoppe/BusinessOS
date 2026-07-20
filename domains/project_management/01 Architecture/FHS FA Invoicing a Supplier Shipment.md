---
title: "FHS FA Invoicing a Supplier Shipment"
description: "Process for creating supplier invoices in FrontAccounting after receiving shipments - invoice creation, shipping costs, GL entries"
author: "Fraser Highland Shoppe"
source: "https://frontaccounting.com"
date: "2024"
tags:
  - domain:project-management
  - type:sop
  - confidence:high
  - skill:invoicing
  - skill:frontaccounting
categories:
  - Project Management
  - SOP
  - Invoicing
  - FrontAccounting

---

# FHS FA Invoicing a Supplier Shipment

## Overview
Process for creating supplier invoices in FrontAccounting after receiving shipments.

## Access Points
- From **Purchase** tab
- After clicking **Process Receive Items**

## Step-by-Step Process

### Step 1: Create Invoice
After clicking Process Receive Items:
- Click **Entry purchase invoice for this receival**

### Step 2: Enter Invoice Details
**Invoice Entry**:
1. Choose Supplier from Dropdown Menu
2. Type in Supplier Reference Number (or today's date if unavailable)
3. Ensure dates are reasonable (accrual accounting at EOM)
4. Confirm quantities and prices (match to supplier invoice)

### Step 3: Handle Shipping Costs
- Update shipping cost to $0.01
- Add GL Entry for Shipping:
  - Account 5100 (Shipping)
  - Account 2310 (GST Payable on Shipping)

### Step 4: Add Line Items
- Click **ADD** button for each verified item
- **OR** click **Add All Items** button (if entire invoice verified)

**Note**: Adding items one-by-one makes accounting audit easier if multiple invoices apply.

### Step 5: Finalize Invoice
- Click **Enter Invoice**

### Step 6: Print Invoice
On next page:
- Click **View This Invoice** link (pop-up window)
- At bottom of pop-up, click **PRINT**
- Print **2 copies** (ensure bookkeeper gets copy)

## Next Steps
If needed, proceed to [[FHS FA Paying a Supplier]]

## References
1. FrontAccounting, "Invoice Processing Documentation", frontaccounting.com, 2024.

## Related
- [[FHS FA Receive a Shipment]]
- [[FHS FA Paying a Supplier]]