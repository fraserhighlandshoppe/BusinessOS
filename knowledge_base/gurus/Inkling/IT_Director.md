# IT Director — Role Description & Best Practices

Tags: #businessroles #it #director #security #infrastructure

References: `ITHowTo.md` (`Sections 1-6`); `Wiki WebsiteInfrastructureMustHaves.md`; `Wiki MauticandWordpressIntegration.md`; `Wiki UsingGITforBackupandRestore.md`

---

## Role Description
IT Director: owns website (`WP/WC`), marketing automation (`Mautic`), accounting (`FrontAccounting` — SOP references: `Create_Campaign.md`, `Inventory_Lifecycle_Management.md`, `Launch_Product.md`), containers (`Git` backup/restore — `UsingGITforBackupandRestore.md`), backups, `Ansible`, security (`2FA`, `TLS`), SOP index (`FHS-INTERNAL-INDEX.md`).

## Principles & Best Practices
- `Wiki` (`Infrastructure_Must_Haves.md`) = authoritative procedure; `Guru` (`Dubeau`/`Singer`/`Cardone`) = strategy; agreement: `document` + `test restore` + `reference source`; `no` direct conflict.
- `Social_Accounts` (`ITHowTo.md` `Section 2`): `WP` site → `Mautic` → `FA`; `containers` for isolation; `backups` (`Git`); `Ansible` (`SOP` automation); `security` (`2FA`/`DMARC`/`SPF`/`DKIM`/`TLS`).
