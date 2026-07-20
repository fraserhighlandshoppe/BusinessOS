Title: FrontAccounting is the System of Record

Status: Accepted

Context: Multiple systems (WooCommerce, AI agents, reports) will consume product and customer data.

Decision: FrontAccounting is the authoritative source for operational data. External systems consume or enrich that data but do not become the master.

Consequences:

No duplicate product databases.
Inventory, purchasing, pricing, and stock remain in FrontAccounting.
Integrations synchronize with FrontAccounting rather than replacing it.