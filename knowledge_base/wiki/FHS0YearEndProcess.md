---
title: "FHS 0 Year End Process"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=FHS_0_Year_End_Process"
type: wiki
categories: FHS
author: Fraser Highland Shoppe Wiki
---

 Related Processes:
 *[[FHS 0 Daily Process]]
 *[[FHS 0 Weekly Process]]
 *[[FHS 0 Monthly Process]]
 *[[FHS 0 Year End Process]]
==FHS Year End Process==
===Internal Audit===
Prepare the books for finalization
====Customer====
#Ensure all [http://localhost/fhs/frontaccounting/sales/inquiry/sales_orders_view.php?OutstandingOnly=1 outstanding Sales Orders] have been delivered or are current 
#Ensure all [http://localhost/fhs/frontaccounting/sales/inquiry/sales_deliveries_view.php?OutstandingOnly=1 Customer Invoicing] has been completed.
##Finalize (complete or cancel) any that aren't current
#Audit that all Sales Invoices and Payments have been printed and stapled (Go through file folder(s) ensuring that all Invoice Numbers are present)
##invoice on top.  Sales Order if applicable.  Payment Receipt on bottom.  Delivery and packing slips are not required.
##sort all invoices by order number.
#Check [http://localhost/fhs/frontaccounting/sales/allocations/customer_allocation_main.php? payment allocations].
#Accrue any revenue that can't be billed
##On Dec 31 move the revenue from revenue account into MAGIC CASH.
##On Jan 2nd move the revenue from MAGIC CASH back to revenue account.
###Jan 1st is used for closing the year.  Since the shop is "closed" there shouldn't be any revenue/expense type entries on that date!
#update the allowance for any doubtful accounts
#Run [http://localhost/fhs/frontaccounting/reporting/reports_main.php?Class=0&REP_ID=101 Customer Balances] report.
##The goal is that there aren't any customer balances.  However, there may be a few that have a few days left to pay off any balances.

====Suppliers====
#Ensure Vendor Invoicing is complete
##Audit that all Vendor Invoices have been entered
###check that all [http://localhost/fhs/frontaccounting/purchasing/inquiry/po_search.php Purchase Orders] that are not outstanding have been received into Front and printed
####Make sure to adjust search date range
###check that all POs have been Invoiced and printed
####Receive against Orders
####Invoice against received
####Scroll through Suppliers looking for [http://localhost/fhs/frontaccounting/purchasing/supplier_invoice.php?New=1 un-invoiced] items.
#####THIS WILL REQUIRE SCROLLING THROUGH EACH SUPPLIER TO SEE WHAT POPS UP AS NOT INVOICED.
###check that all Invoices have been paid and printed 
####[http://localhost/fhs/frontaccounting/reporting/reports_main.php?Class=6&REP_ID=704 GL Account Transactions](GL 2100 Accounts Payable will have list of in/out)
####Check Outstanding [http://localhost/fhs/frontaccounting/reporting/reports_main.php?Class=1&REP_ID=201 Vendor Balances] (due)
####Check vendor allocations
###ensure all have been stapled:
####Front version of Invoice on top
####Purchase Order
####Received printout if available
####Vendor Invoice
####Remittance
###sort by FA Invoice number
##Accrue any expenses that haven't had a Vendor Invoice for yet

====Inventory====
#Run a full store inventory
#Investigate shrinkage and overage
##Invoice shrinkage to Cash Sales
##Generate Purchase Orders.
###Trace where the goods would have come from.  Check historical vendor invoices against FA invoices.
#Compare Sales transaction listing to COGS.
##Looking for where sale price doesn't have a reasonable margin compared to COGS.
###Remember that the"sale" price may be PRE or POST discount. If a discount is applied at time of recording the payment as opposed to when the invoice is generated, then the DISCOUNTS GL will have the difference, and the regular retail price listed in the 4400 REVENUE GL.

====Banking====
#Audit that all bank account activity has been reconciled
##Print the year's statements for the following:
###Kevin's Visa and Savings accounts
###Square Up 
###Paypal 
##Reconcile those statements against their associated FrontAccounting ledgers
###Generate any entries in FA that we don't have
###Track down the source of those entries - should be a vendor remittance, customer payment or Expense payment.
##Put the printouts into the associated file folder
##Print last 1/2 page of each FA entries and staple to outside of file folder.
#Balance the cashbox
##Journal Entry using 1001 Magic Cash as opposite account
###Need to determine why it is out of balance!

====Payroll====
#Ensure Payroll is complete
##Accrue any wages
##Accrue any vacation banks
##Accrue benefits
##Calculate commissions
##Calculate Bonuses
====Expenses====
#Ensure all expenses for the year have been entered
##Each vendor till slip/invoice should be attached to a printout of the JL sheet.
##Each JL sheet should be filed in the appropriate file folder
##Compare Kevin and Kim's personal records for items purchased/payed for.
##Compare against ATB Mastercard printout from bank account reconcilliation.
###Mastercard should only have business expenses and/or vendor payments on it so each entry should have a correspondig JL into an account somewhere.
##Print each expense account Journal and ensure each entry has a printed JL sheet in its folder
###Some expenses may go into multiple Ledgers.  Make sure each Ledger has a copy of the Journal Entry.  Make sure one of the associated entries has the vendor till slip.
##If the expense is a subcontract (i.e. 1 day fixed price contract for labour at a games) ensure a copy of the signed contract is attached to the Journal Entry print.

===Tax Reports===
====Generate reports for tax purposes====
#Run [http://fhs-laptop1.ksfraser.com/fhs/frontaccounting/reporting/reports_main.php?Class=2&REP_ID=306 Inventory Purchase Report]
##Check items - remove things like Charges (office supplies?) and Shipping (freight).
##Remaining total goes onto line 8320 Purchases during the year
#Run  [http://fhs-laptop1.ksfraser.com/fhs/frontaccounting/reporting/reports_main.php?Class=0&REP_ID=114 sales summary sheet]
##Use these to check against P/L and GST calcs.
###Note that discounts given are NOT accounted for in these totals!
##Gives Tax Collected (payable)
##Gives (mostly) Gross Business Income (Line 8299/17)
#Run [http://fhs-laptop1.ksfraser.com/fhs/frontaccounting/reporting/reports_main.php?Class=6&REP_ID=706 Balance Sheet] as of last day of year
##validate Assets and Liabilities
###compare against last year accounting for cash flow, purchases, sales, etc.
#Run [http://fhs-laptop1.ksfraser.com/fhs/frontaccounting/reporting/reports_main.php?Class=6&REP_ID=707 Profit/Loss] as of last day of year
##validate expenses.
###compare against budget
###compare against last year
#Transfer GST totals from Collected (2311)/Payed(2312) account into 2310 CRA GST Payable on Jan 1st of next fiscal year so that reports run against the year has the EOY total.

====Calculate totals that need to go on T2125/T5013====
#Gross Income + Net GST
#Net GST Collected
#Adjusted Gross Sales (Gross - GST, taxes, adjustments, etc)
#Look up Closing Income from last year - becomes Opening Income for this year.
#Calculate Purchases during the year (Inventory Purchase Report above)
#Calculate Subcontract costs
#Calculate other Costs
#Calculate Closing Inventory (Balance Sheet above)
#Calculate COGS (P/L report above should be close to Turbotax number)
#Calculate Expenses
##Advertising
##Meals and Entertainment
##Bad Debts (check that process to qualify has been followed)
##Insurance
##Interest
##Business taxes, licenses, dues, memberships
##Office Expenses
##Supplies
##Legal, Accounting, Prof
##Management and Admin
##Rent
##Maintenance and Repairs
##Salaries and benefits
##Property Taxes
##Travel (Transportation, accomodations)
##Telephone and Utils
##Fuel (except auto)
##Delivery, Freight, Express
##Motor Vehicle Expenses that are calculated elsewhere on tax form
##CCA
###Depreciation
##Other Expenses (i.e. Highland Games entries)
#Calculate Net Income
#Calculate Income Taxes owed (corporation)

====Calculate Assets and resulting CCA====
#Class 8 (20%) (1820 -> 5952) 
#Class 12 (100%) (1521, 1770 -> 5660)
#class 10 (30%) (1850 -> 5951)

===Close Temporary Accounts===
 When "closing" the accounts, transfer the amounts that were on the TAX forms using the line memo of "TAX FORM"
 so that we can see where some past-dated adjustment in the future affects the results against what was reported.
Income statement accounts:
*revenues, 
*expenses, 
*gains, 
*losses
#transfer Owner Drawing Accounts to the Equity accounts
#transfer the CCA values (from ASSET accounts into accumulated amortization EXPENSE Accounts)
#transfer the Revenue and Expense accounts into a Retained Earnings account
##then transfer each owner's share of the Retained Earnings into their Equity account (partnerships ONLY.  Corporations don't do this!)
#Update Company Setup for the current Fiscal Year
#Update the Fiscal Years to close the year that just finished.


[[Category: Fraser Highland Shoppe]]
[[Category: FHS]]
[[Category: All Pages]]

==Inventory==
*Inventory Count
**Generate an invoice for any shrinkage (use 0cash customer and write-off branch).
***100% discount or the items so that there is no generated revenue.
**For any items we have an over-abundance in stock, generate a credit note (use 0cash customer and write-off branch).
***If we can find a sales invoice, we can do a "return".

==Strategy and Planning==
===Marketing===
*What advertising where
**Publications
**social media
**competition/games program books
*what competitions to attend
*What highland Games to attend
*what community groups to sponsor
*Review marketing calendar
**dates of interest (scottish cultural, canadian historical)
**When are sales
**when are competitions and Games

===Products===
*review sales, turnover
*What new lines to carry
*what lines to discontinue
===Systems and Software===
*Confirm workflows
**Discuss changes for improvements
**Discuss/document process in software/systems
*Enhancements
**discuss desired workflow changes
**discuss system/software changes to support workflow
**prioritize changes
***impact
***Needed before dates