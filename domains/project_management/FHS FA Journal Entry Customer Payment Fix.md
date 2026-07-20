# FHS FA Journal Entry Customer Payment Fix

## Overview
Process for correcting payment records in FrontAccounting when payments are recorded incorrectly.

## When to Use
- Customer payment recorded for wrong amount
- Payment split between multiple accounts
- Payment allocation incorrect
- Need to correct transaction history

## Method 1: Journal Entry Correction

### Use Case
Customer payment recorded for entire amount, but payment was split (part to cash box, part to Kim for materials).

### Process
1. Create journal entry to correct records
2. First line: Account money is coming out of
3. Next lines: Entries that should have been separate payments

**Important**: Verify transaction date for correct daily balances.

**Note**: Quick entry box can be ignored (for recurring entries only).

## Method 2: Payment Record Edit

### Access Payment Record
1. Load Payment Record through Customer Transaction Enquiry
2. Click pencil icon for record to edit

### Edit Details
- Change allocation amounts
- Modify account payment came from
- Update reference number

**CRITICAL**: To save edit, MUST change reference number (add "a" behind number for revision)

### Finalize
- Submit print of edit to bookkeeper

## Related Pages
- [FHS FA Customer Payment](FHS_FA_Customer_Payment.md)
- [FHS FA Receive Shipment](FHS_FA_Receive_a_Shipment.md)

## Best Practices
- Bookkeeper should perform corrections
- Always verify dates for balance accuracy
- Keep printed records of all edits
- Update reference numbers for audit trail