---
title: "Accounts Payable AI Helper Skills"
description: "AI skills and prompt engineering for accounts payable - invoice processing, vendor management, payment scheduling, reconciliation"
author: "Business Operating System"
source: "https://www.aap.org"
date: "2024"
tags:
  - domain:finance
  - type:skill
  - confidence:high
  - skill:accounts-payable
  - skill:financial-processing
  - ai:helper
categories:
  - AI Helpers
  - Finance
  - Accounts Payable
  - Skills
  - Prompt Engineering

---

# Accounts Payable AI Helper Skills

## Core Competencies

### 1. Invoice Processing Skills
- **Invoice Data Extraction**: Vendor name, invoice number, date, amount
- **Three-Way Matching**: Purchase Order, Receipt, Invoice validation
- **Approval Routing**: Based on amount, vendor, department
- **Exception Handling**: Missing PO, price discrepancies, duplicate invoices
- **Coding Accuracy**: Account coding, cost center allocation

### 2. Vendor Management Skills
- **Vendor Onboarding**: Setup new vendor profiles, W-9 collection
- **Vendor Performance Tracking**: Payment history, service quality
- **Vendor Communication**: Invoice queries, payment confirmations
- **Vendor Database Maintenance**: Contact info, payment terms updates
- **Vendor Risk Assessment**: Financial stability, compliance status

### 3. Payment Scheduling Skills
- **Payment Run Preparation**: Batch creation, approval workflows
- **Payment Method Selection**: ACH, Check, Wire, Credit Card
- **Early Payment Discounts**: Evaluation and optimization
- **Payment Calendar Management**: Due dates, cash flow planning
- **Payment Exception Handling**: Bounced checks, rejected ACH

### 4. Reconciliation Skills
- **Bank Statement Reconciliation**: AP account vs bank records
- **Credit Memo Processing**: Returns, overpayments, adjustments
- **Discrepancy Investigation**: Missing payments, duplicate entries
- **Month-End Close Tasks**: Accruals, provisions, final reviews
- **Audit Trail Maintenance**: Documentation for compliance

### 5. Reporting and Analytics Skills
- **AP Aging Reports**: Overdue invoices, cash flow forecasting
- **Payment Summary Reports**: By vendor, by department, by period
- **Vendor Spend Analysis**: Spend patterns, consolidation opportunities
- **Early Payment Discount Analysis**: ROI on early payments
- **Compliance Reporting**: 1099 preparation, tax reporting

## AI Prompt Engineering

### Invoice Processing Prompt
```
You are an accounts payable specialist processing invoice #[INVOICE_NUMBER] from [VENDOR].

Invoice details:
- Amount: [AMOUNT]
- Date: [DATE]
- PO #: [PO_NUMBER]
- Items: [ITEM_LIST]

Tasks:
1. Verify PO exists and matches
2. Check receipt of goods/services
3. Validate pricing matches
4. Determine approval level
5. Enter into AP system

If exceptions found, generate inquiry email template.
```

### Payment Scheduling Prompt
```
You are an AP payment scheduler for [COMPANY].

Upcoming payments:
[PAYMENT_LIST]

Create optimized payment run considering:
- Cash flow position
- Early payment discounts available
- Vendor terms (Net 30, Net 60, etc.)
- Payment method preferences
- Approval requirements

Output: Payment schedule with dates, amounts, methods
```

### Three-Way Match Prompt
```
You are verifying three-way match for [INVOICE_NUMBER].

Compare:
- PO: [PO_DETAILS]
- Receipt: [RECEIPT_DETAILS]
- Invoice: [INVOICE_DETAILS]

Identify discrepancies and recommend action:
- Match: Process for payment
- Mismatch: Generate exception report
- Missing: Request additional documentation
```

### Vendor Onboarding Prompt
```
You are setting up new vendor [VENDOR_NAME] in the AP system.

Required information:
- Vendor contact details
- Payment terms and method
- Tax identification
- Banking information
- W-9 form status

Create vendor profile checklist and follow-up email template for missing documents.
```

### Month-End Close Prompt
```
You are preparing AP month-end close for [MONTH/YEAR].

Tasks:
1. Review all outstanding invoices
2. Process pending payments
3. Accrue unpaid invoices
4. Reconcile AP control account
5. Generate required reports
6. Document any adjustments

Provide month-end close checklist with due dates.
```

## Related Templates
- [[Invoice Approval Workflow]]
- [[Vendor Setup Checklist]]
- [[Payment Run Template]]
- [[AP Aging Report]]
- [[Month-End Close Schedule]]

## References
1. Association for Financial Professionals, "AP Best Practices", aap.org, 2024.
2. SAP, "Accounts Payable Automation Guide", sap.com, 2024.
3. PayStream Research, "AP Process Benchmarking", paystream.com, 2024.