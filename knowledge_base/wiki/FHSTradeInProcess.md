---
title: "FHS Trade In Process"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=FHS_Trade_In_Process"
type: wiki
categories: FHS
author: Fraser Highland Shoppe Wiki
---

==FHS Trade In Process==
When a customer trades in a sellable good, we need to follow these steps to get items and accounting lined up:
#Ensure the ''item (used)'' exists.
#create a purchase order - Direct Invoice from vendor "Trade In" for the item.
##this gets the item into inventory
##This gets the invoice created
###vendor Trade In uses account Discount Given as its AP holding tank.  Other side of 2entry is Inventory.
#Pay the supplier for the agreed amount.
##use petty cash as the source of the payment.  This reverses the Discount Given amount.
#create the Customer Invoice (direct invoice) with any payment type not ''cash''
#Create a customer payment.  
##For the allocation, put in the agreed amount
##enter a discount of the amount, minus a penny.
###this puts an entry into the Prompt Payment Discount account
##pay into petty cash.
#Print the receipt.  It will show the balance owing by the customer.
#Collect payment as normal for the balance.
#Do a journal entry transferring the amount from Petty Cash to Prompt Payment Discount.
##this reverses the Prompt Payment Discount amount, while leaving the cost in Inventory.

[[Category: FHS]]
[[Category: Fraser Highland Shoppe]]
[[Category: All Pages]]
[[Category: Front Accounting]]