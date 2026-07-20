---
title: "Payroll AI Helper Skills"
description: "AI skills and prompt engineering for payroll processing - salary calculation, tax compliance, benefits administration, employee self-service"
author: "Business Operating System"
source: "https://www.shrm.org"
date: "2024"
tags:
  - domain:finance
  - type:skill
  - confidence:high
  - skill:payroll
  - skill:hr-payments
  - ai:helper
categories:
  - AI Helpers
  - Finance
  - Payroll
  - Skills
  - Prompt Engineering

---

# Payroll AI Helper Skills

## Core Competencies

### 1. Salary and Wage Calculation Skills
- **Gross Pay Calculation**: Regular, overtime, commissions, bonuses
- **Deduction Processing**: Taxes, garnishments, benefits, retirement
- **Net Pay Determination**: Gross minus all deductions
- **Pay Period Management**: Weekly, bi-weekly, semi-monthly, monthly
- **Special Payment Types**: Reimbursements, expense reports, prize payments

### 2. Tax Compliance Skills
- **Tax Rate Updates**: Federal, state, local, FICA rates
- **Withholding Calculations**: W-4 allowances, additional withholding
- **Tax Filing Preparation**: W-2s, 1099s, quarterly filings
- **Tax Deposit Scheduling**: Deposit schedules, due dates
- **Tax Error Correction**: Amended returns, penalty calculations

### 3. Benefits Administration Skills
- **Benefits Enrollment**: Health, dental, vision, life insurance
- **Premium Deductions**: Employee, employer portions, COBRA
- **Leave Management**: PTO accrual, sick leave, holiday pay
- **Retirement Plan Contributions**: 401(k), pension calculations
- **Benefits Communication**: Enrollment guides, plan summaries

### 4. Employee Self-Service Skills
- **Pay Stub Generation**: Detailed breakdowns, tax information
- **Direct Deposit Management**: Account updates, verification
- **Time Off Requests**: PTO balances, approval workflows
- **Personal Information Updates**: Address, marital status, exemptions
- **Document Access**: W-2s, pay stubs, tax forms

### 5. Payroll Reporting Skills
- **Payroll Register Generation**: Detailed payment lists
- **YTD Reporting**: Year-to-date totals, tax withholdings
- **Compliance Reports**: Form 941, W-3, state reports
- **Audit Trail Maintenance**: Documentation, change logs
- **Budget vs. Actual Analysis**: Payroll cost reporting

## AI Prompt Engineering

### Payroll Calculation Prompt
```
You are a payroll specialist calculating pay for [EMPLOYEE_NAME].

Employee Details:
- Pay Rate: [RATE]
- Hours Worked: [HOURS]
- Overtime Eligible: [YES/NO]
- Pay Period: [PERIOD]

Deductions:
- Federal Tax: [FED_TAX]
- State Tax: [STATE_TAX]
- FICA: [FICA]
- Benefits: [BENEFITS]
- Other: [OTHER]

Calculate gross pay, total deductions, and net pay.
Include overtime calculation if applicable.
```

### Tax Withholding Prompt
```
You are a tax specialist calculating withholding for [EMPLOYEE_NAME].

Employee Info:
- Filing Status: [STATUS]
- Allowances: [ALLOWANCES]
- Additional Withholding: [ADDITIONAL]
- State: [STATE]

Calculate:
1. Federal income tax withholding
2. State income tax withholding
3. FICA (Social Security, Medicare)
4. Any local taxes

Provide total withholding amount and breakdown.
```

### Benefits Enrollment Prompt
```
You are processing benefits enrollment for [EMPLOYEE_NAME].

Selected Benefits:
- Medical: [PLAN]
- Dental: [PLAN]
- Vision: [PLAN]
- Life: [AMOUNT]
- 401k: [PERCENTAGE]

Calculate:
- Employee premiums
- Employer contributions
- Net payroll impact
- Effective dates

Generate enrollment confirmation email with details.
```

### PTO Accrual Prompt
```
You are calculating PTO accrual for [EMPLOYEE_NAME].

Current Status:
- Accrual Rate: [RATE]
- Hours Worked: [HOURS]
- PTO Used: [USED]
- PTO Balance: [BALANCE]

Calculate:
- New accrual amount
- Updated PTO balance
- Any carryover rules
- Expiration dates

Update employee record and generate balance notification.
```

### Year-End W-2 Prompt
```
You are preparing W-2 for [EMPLOYEE_NAME] for tax year [YEAR].

Salary Information:
- Box 1 (Wages): [AMOUNT]
- Box 2 (Federal Tax): [AMOUNT]
- Box 3 (SS Wages): [AMOUNT]
- Box 4 (FICA Tax): [AMOUNT]
- Box 5 (State Wages): [AMOUNT]
- Box 6 (State Tax): [AMOUNT]

Additional Information:
- Employer ID: [ID]
- Employee ID: [ID]
- State: [STATE]

Generate W-2 form with all boxes filled correctly.
Include copy distribution instructions.
```

## Payroll Processing Templates

### Template: Pay Stub Header
```
[COMPANY LOGO]
[COMPANY NAME]
[COMPANY ADDRESS]
Pay Period: [START_DATE] - [END_DATE] | Pay Date: [PAY_DATE]

Employee: [NAME] | ID: [ID] | Department: [DEPT]
Hours: [REGULAR]/[OVERTIME] | Pay Rate: [RATE]
```

### Template: Payroll Notification
```
Subject: Your Paycheck is Ready - [PAY_PERIOD]

Dear [NAME],

Good news! Your paycheck for [PAY_PERIOD] is ready for pickup/direct deposit.

Net Pay: [AMOUNT]
Gross Pay: [AMOUNT]
Taxes Withheld: [AMOUNT]

View detailed pay stub: [LINK]

Questions? Contact Payroll at [EMAIL] or [PHONE].

Thank you,
Payroll Department
```

### Template: Benefits Confirmation
```
Subject: Benefits Enrollment Confirmation

Dear [NAME],

Your benefits enrollment has been processed successfully.

Effective Date: [DATE]
Medical: [PLAN] - $[EMPLOYEE]/$[EMPLOYER]
Dental: [PLAN] - $[EMPLOYEE]/$[EMPLOYER]
Vision: [PLAN] - $[EMPLOYEE]/$[EMPLOYER]
401k: [PERCENTAGE]%

Your first deduction will appear on the [DATE] paycheck.

Welcome to the team!

Best regards,
Benefits Administration
```

## Related Templates
- [[Employee Handbook]]
- [[Time Off Policy]]
- [[Benefits Enrollment Form]]
- [[Payroll Calendar]]
- [[Tax Filing Checklist]]

## References
1. Society for Human Resource Management, "Payroll Management Guide", shrm.org, 2024.
2. IRS, "Employer Tax Guide", irs.gov, 2024.
3. ADP, "Payroll Best Practices", adp.com, 2024.