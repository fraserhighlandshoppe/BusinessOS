---
title: "FHS Generate Product Labels"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=FHS_Generate_Product_Labels"
type: wiki
categories: FHS
author: Fraser Highland Shoppe Wiki
---

#lookup the delivery number for the items you want to generate (http://fhs-laptop1.ksfraser.com/fhs/frontaccounting/purchasing/inquiry/supplier_inquiry.php?)
#Run the "Generate Catalogue" module (http://fhs-laptop1.ksfraser.com/fhs/frontaccounting/modules/ksf_generate_catalogue/ksf_generate_catalogue.php?action=polabelsfile)
##Enter the DELIVERY number, not PO number
#check email.  Download CSV
##check the SKUs.  Not everything needs a label i.e. shipping
#Convert CSV into Database (new database, connect to existing spreadsheet...)
#Create a new Labels doc
##Title, barcode, stock_id.
##Center 3 fields in label
##change Barcode to free 3 of 9, 22pts
##sync labels
#print (use mail merge wizard on fhs-laptop1)


[[Category: All Pages]]
[[Category: FHS]]
[[Category: Fraser Highland Shoppe]]