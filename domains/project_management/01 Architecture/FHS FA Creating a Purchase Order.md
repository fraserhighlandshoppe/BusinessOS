# FHS FA Creating a Purchase Order

## Overview
Standard process for creating purchase orders in FrontAccounting (FA).

## Normal Order of Operations
1. **Place purchase order**
2. **Supplier fulfills (ships) the order**
3. **Supplier invoices the order**
4. **Receive the order**
5. **Enter the Supplier Invoice**
6. **Pay the Supplier Invoice**

**Note**: Can go straight to Direct Purchase Invoice (generates PO, Reception, and Invoice in one step).

## Purchase Order Creation Steps

### Step 1: Access Purchase Order Entry
- Navigate to Purchase Order Tab
- Click Purchase Order Entry

### Step 2: Select Appropriate Data
- **Supplier**: Select from dropdown or type in code
- **Date**: Enter order date
- **Receive Into**: Select receiving location

### Step 3: Add Items
1. Type code or select from dropdown
2. Add number of items
3. Check price
4. Click Add Item

### Step 4: Add Additional Line Items
- **Shipping**: Add line entry for shipping (SHIP) if applicable
  - Estimate cost if unknown (start around $20)
- **Notes**: Add memo if appropriate

### Step 5: Finalize Order
- Click Place Order
- Click Print This Order
- **Optional**: Email order if supplier accepts POs by email
- **Optional**: If items have arrived, click Receive Items on this Purchase Order

## Direct Purchase Invoice (Alternative)
For immediate orders, can skip PO creation and:
1. Create Direct Purchase Invoice
2. Generates PO, Reception, and Invoice in one step
3. Faster processing for routine purchases

## Related Pages
- [FHS FA Receive Shipment](FHS_FA_Receive_Shipment.md)
- [FHS FA Paying a Supplier](FHS_FA_Paying_a_Supplier.md)
- [FHS FA Invoicing a Supplier Shipment](FHS_FA_Invoicing_a_Supplier_Shipment.md)

## Best Practices
- Always estimate shipping costs
- Use notes/memory box for important details
- Email POs when possible for faster processing
- Receive items at time of PO creation if already arrived