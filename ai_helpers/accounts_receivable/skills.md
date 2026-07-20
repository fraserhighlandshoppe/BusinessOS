---
title: "Accounts Receivable AI Helper Skills"
description: "AI skills and prompt engineering for accounts receivable - invoice generation, collections, customer statements, credit management"
author: "Business Operating System"
source: "https://www.aap.org"
date: "2024"
tags:
  - domain:finance
  - type:skill
  - confidence:high
  - skill:accounts-receivable
  - skill:financial-processing
  - ai:helper
categories:
  - AI Helpers
  - Finance
  - Accounts Receivable
  - Skills
  - Prompt Engineering

---

# Accounts Receivable AI Helper Skills

## Core Competencies

### 1. Invoice Generation Skills
- **Invoice Creation**: Sales order to invoice conversion
- **Pricing Validation**: Correct rates, discounts, taxes
- **Customer-Specific Pricing**: Contract terms, volume discounts
- **Invoice Formatting**: Professional layout, clear breakdown
- **Delivery Methods**: Email, portal download, mail

### 2. Collections Management Skills
- **Aging Analysis**: 0-30, 31-60, 61-90, 90+ days
- **Collection Strategy**: Soft reminders to aggressive pursuit
- **Dispute Resolution**: Invoice issues, product problems
- **Payment Plan Setup**: Installment agreements, partial payments
- **Written-Off Management**: Bad debt, recovery attempts

### 3. Customer Statement Skills
- **Statement Generation**: Periodic billing summaries
- **Balance Explanation**: Current, past due, credits
- **Payment Posting**: Recording customer payments
- **Discrepancy Resolution**: Unapplied payments, overpayments
- **Customer Communication**: Clear, professional tone

### 4. Credit Management Skills
- **Credit Application Review**: Financial statements, references
- **Credit Limit Setting**: Based on financial strength, history
- **Credit Hold Management**: Applying, monitoring, releasing
- **Customer Risk Assessment**: Payment patterns, behavior
- **Collateral Evaluation**: Security for credit extension

### 5. Cash Application Skills
- **Payment Matching**: Lockbox, wire, check deposits
- **Overpayment Handling**: Credits, refunds, future applications
- **Partial Payment Processing**: Applying to specific invoices
- **Unidentified Payment Research**: Bank statements, customer inquiries
- **Cash Forecast Integration**: Daily cash position updates

## AI Prompt Engineering

### Invoice Generation Prompt
```
You are an AR invoice specialist generating invoice #[INVOICE_NUMBER] for [CUSTOMER_NAME].

Sales Order Details:
- Items: [ITEMS]
- Quantities: [QTY]
- Unit Prices: [PRICES]
- Discounts: [DISCOUNTS]
- Tax Rate: [TAX_RATE]

Create professional invoice with:
1. Customer header
2. Line item details
3. Subtotal, tax, total
4. Payment terms
5. Due date
6. Contact information

Format: PDF, email-ready
```

### Collections Call Prompt
```
You are an AR collections specialist calling [CUSTOMER_NAME] about overdue invoice #[INVOICE_NUMBER].

Account Status:
- Balance: [AMOUNT]
- Days Past Due: [DPD]
- Last Contact: [DATE]
- Payment History: [HISTORY]

Call script should:
1. Friendly greeting and introduction
2. Acknowledge any payment made
3. Address reason for non-payment
4. Propose payment arrangement
5. Confirm next steps
6. Document call outcome
```

### Customer Statement Prompt
```
You are preparing monthly statement for [CUSTOMER_NAME].

Customer Details:
- Account: [ACCOUNT_NUMBER]
- Current Balance: [BALANCE]
- Past Due: [PAST_DUE]
- Total Invoiced: [TOTAL]

Include:
- Invoice summary with dates
- Payment history
- Current balance breakdown
- Payment instructions
- Contact information

Format: Professional PDF, email attachment
```

### Credit Limit Recommendation Prompt
```
You are evaluating credit request for [CUSTOMER_NAME].

Financial Information:
- Annual Revenue: [REVENUE]
- Cash Flow: [CASH_FLOW]
- Bank References: [REFERENCES]
- Trade References: [TRADE_REFS]
- Business History: [HISTORY]

Recommend credit limit considering:
- Financial stability
- Payment history
- Industry risk
- Account relationship
- Collateral available

Provide recommendation with justification.
```

### Escalated Account Prompt
```
You are escalating [CUSTOMER_NAME]'s account due to [REASON].

Account Details:
- Balance: [AMOUNT]
- DPD: [DAYS]
- Previous Efforts: [EFFORTS]
- Legal Considerations: [LEGAL]

Escalation actions:
1. Notify management
2. Engage collection agency (if applicable)
3. Legal counsel consultation
4. Account write-off consideration
5. Customer communication freeze

Generate escalation report with timeline and recommended actions.
```

## Collections Templates

### Template: Initial Reminder
```
Subject: Friendly Reminder - Invoice #[INVOICE_NUMBER]

Dear [NAME],

We're following up on invoice #[INVOICE_NUMBER] dated [DATE] for [AMOUNT], which was due on [DUE_DATE].

Current balance: [AMOUNT]

Please process payment at your earliest convenience. If you've already sent payment, please disregard this notice.

Questions? Contact us at [PHONE] or [EMAIL].

Thank you,
[NAME]
Accounts Receivable
```

### Template: Final Notice
```
Subject: Final Notice - Account Overdue

Dear [NAME],

This is a final notice regarding your outstanding balance of [AMOUNT] for invoice #[INVOICE_NUMBER].

Unless we receive payment by [DATE], we will be forced to:
- Refer this account to collections
- Report to credit agencies
- Suspend future shipments/services

We value our relationship and hope to resolve this amicably.

Please contact us immediately: [PHONE]

Sincerely,
[NAME]
Accounts Receivable
```

## Related Templates
- [[Invoice Template]]
- [[Customer Statement Template]]
- [[Collection Call Script]]
- [[Credit Application]]
- [[Payment Terms Policy]]

## References
1. Association for Financial Professionals, "AR Best Practices", aap.org, 2024.
2. Bill.com, "Accounts Receivable Automation", bill.com, 2024.
3. McKinsey, "AR Optimization Strategies", mckinsey.com, 2024.