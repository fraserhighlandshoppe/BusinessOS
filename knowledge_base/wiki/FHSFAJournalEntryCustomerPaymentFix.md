---
title: "FHS FA Journal Entry Customer Payment Fix"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=FHS_FA_Journal_Entry_Customer_Payment_Fix"
type: wiki
categories: FHS
author: Fraser Highland Shoppe Wiki
---

====Correcting Payment Records via Journal Entry====
 This is a step that the Bookkeeper should perform.
In this case 1 customer payment was recorded for the entire amount even though the payment was split (part went to the cash box, part went to Kim to pay for the materials).  To correct the records, we need to make a journal entry.

[[Image: Journal Entry bank account entries.png]]

The first line is the account the money is coming out of.  The next 2 lines are the entries that should have been made via 2 separate payments.

Please ensure that the transaction date in the top left is correct so that daily balances are correct.

The quick entry box can be ignored for this case as it is meant for regularly occurring entries that pre-fill some entries.


[[Category: FHS]]
[[Category: Fraser Highland Shoppe]]

====Correcting Payment Records via edit====
A payment record can be edited.  Load the Payment Record through [[http://fhsws002.ksfraser.com/fhs/frontaccounting/sales/inquiry/customer_inquiry.php Customer Transaction Enquiry]]:

[[Image: FA Customer Inquiry Screen.png]]

Click on the Pencil for the record you want to edit.

You can now change the allocation, the amounts, and how (account) the customer paid by.

[[Image: FA Customer Payment.png]]

*In order to save this edit, you MUST change the reference number (add an "a" behind the number to show the edit revision) (Older FA)
*Submit a print of the edit to the bookkeeper!
[[Category: Accounting]]
[[Category: Front Accounting]]