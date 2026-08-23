---
title: "FHS FA Customer Return"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=FHS_FA_Customer_Return"
type: wiki
categories: FHS
author: Fraser Highland Shoppe Wiki
---

Using the Customer Credit Note there are a couple reasons to "return" an item:
*We goofed on data entry.  Straight return/refund/... (item returned to stock)
*Customer is returning an item
**Doesn't fit need (we knew about in advance)
**Doesn't fit need (bought wrong size) - EXCHANGE ONLY?
**Doesn't fit need (bought wrong thing e.g. gift)
**Defective (Warranty should be run first)
**Buyers remorse - not really our problem.  use TRADE/CONSIGNMENT.

==Walk-in Process==
#Generate [http://fhsws002.ksfraser.com/ksfii/SuiteCRM/index.php?action=ajaxui#ajaxUILoc=index.php%3Fmodule%3DCases%26action%3DEditView%26return_module%3DCases%26return_action%3DDetailView CAS] against customer record in CRM (case number is RMA number)
##This records the interaction even if we deny the return
##Support - Case
##Create Case
###Product/Open/High/New
###Select Account
###Subject RMA FAI123 <name of item>
###Describe WHY the item is being returned
###Assign To.
##Save (If not immediately resolvable)
#Ensure that any item being returned is allowed within the [[FHS Refund Policy]]
##Advise/remind customer of policy.
##determine any restocking fees.  Advise Customer.
##Record reason for return in CASE
#locate the original customer invoice
##ideally the customer has a paper copy but if not look through customer transactions.
===Update Case===
#Locate [http://fhsws001.ksfraser.com/devel/fhs/SuiteCRM/index.php?action=ajaxui#ajaxUILoc=index.php%3Fmodule%3DCases%26action%3Dindex%26return_module%3DCases%26return_action%3DDetailView appropriate case] in SuiteCRM.
#Update RMA CASE
##State whether exchange or refund.
#Upload copy of Invoice if it isn't already associated against Account
##Update CASE with Document
===Close Case===
#Locate [http://fhsws001.ksfraser.com/devel/fhs/SuiteCRM/index.php?action=ajaxui#ajaxUILoc=index.php%3Fmodule%3DCases%26action%3Dindex%26return_module%3DCases%26return_action%3DDetailView appropriate case] in SuiteCRM.
#Actions - Edit
##State to CLOSED
##Resolution if known (Return to Manufacturer/Write-off)
#handle Accounting (Customer Credit Note/payment)

==Online Process==
#Ensure that any item being returned is allowed within the [[FHS Refund Policy]]
##determine any restocking fees
#generate a [http://fhsws001.ksfraser.com/devel/fhs/SuiteCRM/index.php?action=ajaxui#ajaxUILoc=index.php%3Fmodule%3DCases%26action%3DEditView%26return_module%3DCases%26return_action%3DDetailView CASE in SuiteCRM] for the customer. [http://fhsws001.ksfraser.com/devel/fhs/SuiteCRM]
#locate the original customer invoice
##look through [http://fhs-laptop1/fhs/frontaccounting/sales/inquiry/customer_inquiry.php? customer transactions in FA] or [http://fhsws001.ksfraser.com/devel/fhs/SuiteCRM/index.php Documents against the Account].
##Support - Case
##Create Case
###Product/Open/High/New
###Select Account
###Subject RMA FAI123 <name of item>
###Describe WHY the item is being returned
###Assign To.
##Save (If not immediately resolvable)
===Update Case===
#Locate [http://fhsws001.ksfraser.com/devel/fhs/SuiteCRM/index.php?action=ajaxui#ajaxUILoc=index.php%3Fmodule%3DCases%26action%3Dindex%26return_module%3DCases%26return_action%3DDetailView appropriate case] in SuiteCRM.
#Update RMA CASE
##State whether exchange or refund.
#Upload copy of Invoice if it isn't already associated against Account
##Update CASE with Document
===Close Case===
#Locate [http://fhsws001.ksfraser.com/devel/fhs/SuiteCRM/index.php?action=ajaxui#ajaxUILoc=index.php%3Fmodule%3DCases%26action%3Dindex%26return_module%3DCases%26return_action%3DDetailView appropriate case] in SuiteCRM.
#Actions - Edit
##State to CLOSED
##Resolution if known (Return to Manufacturer/Write-off)
#handle Accounting (Below)

==Processing a Return in  Front Accounting==
 Ensure that any item being returned is allowed within the [[FHS Refund Policy]]

Under SALES tab in FA, open Customer Credit Note.
#Select the customer
#select the branch
#ensure the proper price list is selected (SALES TYPE)
#ensure the correct shipping company is selected
#select the correct dimensions
#Scan or enter the items.
##Double check that the price that comes up is in line with our returns policy.  Lower of:
###CURRENT RETAIL (from appropriate price book (SALES TYPE) ) 
###SALES price 
###WHAT THEY PAID (need to have pulled the original invoice from customer transaction)
##Add the restocking fee discount percent in line with our returns policy.
###20% on in original UNOPENED packaging.
###30% in opened packaging but resellable, no signs of wear or tear.
###50% for items showing wear and tear (will have to be sold as USED)
###75% for items that are questionable whether we will be able to resell.
#Enter a shipping cost if applicable 
##We don't refund shipping so the value must be '''''0 or negative'''''.
#Ensure the Credit Note Type is correct
##Items being returned to inventory must have that selected as well as which store location.
#Enter a MEMO as to why the return is being accepted.  Also make reference to SuiteCRM CASE Number
#Hit Process Note.
#'''Print Note 2 copies'''(One copy for customer, one copy for our records)
##ensure it uploads into SuiteCRM. 
###Associate to the CASE
##We can also email the credit note.
#Affiliate and Referral programs need to be checked against the original purchase for adjustment
#Process a Payment in FA and provide refund (as applicable) to customer

[[Image: FA Customer Return.png]]


[[Category: Fraser Highland Shoppe]]
[[Category: FHS]]
[[Category: Accounting]]
[[Category: Front Accounting]]