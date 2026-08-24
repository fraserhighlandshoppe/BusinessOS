# IT Operations Manual — Here's How To Run It

*Shareholder / C-Suite IT Guide for Fraser Highland Shoppe.*
*Every claim traces to source file or wiki reference. Step by step for new hires or AI agents.*

Tags: #it #infrastructure #support #howto #masterguide

---

## How to use this guide
1. Read Section 1 (foundations) to understand our stack.
2. Read Section 2 (infra) for components; Section 3 (hosting/containers/backups); Section 4 (support); Section 5 (security/config).
3. Each subsection: step-by-step; source reference; conflict notes (if any).

---

## 1. Foundations: Our Technology Stack

Per `knowledge_base/wiki/WebsiteInfrastructureMustHaves.md` and current implementation:

- **Website**: WordPress + WooCommerce (WP/WC)
- **Accounting / ERP**: FrontAccounting (FA)
- **Marketing automation**: Mautic (`knowledge_base/wiki/MauticandWordpressIntegration.md`)
- **Version control / backup**: Git (`knowledge_base/wiki/UsingGITforBackupandRestore.md`)
- **Infrastructure**: Local hosting via containers; Ansible for configuration
- **Social accounts**: Linked business profiles; platform accounts (FB, IG, X, YouTube, LinkedIn)

---

## 2. Infrastructure Components (What We Need)

### 2.1 Social Accounts
- Facebook business page + Marketplace (`Social Media Platform Strategies.md`; `Facebook Strategy.md`)
- Instagram business account (`Social Media Image Size Guide.md` dimensions)
- YouTube channel (keywords in title + spoken; video = KLT builder — `Dubeau Web TV.md` reference)
- LinkedIn company page (`linkedin/` domain guides)
- X / Twitter account

Setup step: create account → verify business → add brand promise in bio → link to website landing page. Reference: `SocialMediaHowTo.md`.

### 2.2 Website (WordPress / WooCommerce)
- Setup: install WP + WC; configure SSL; set permalinks; install theme; configure checkout (`Checkout Page Essentials.md`); set landing page templates (`Landing Page Checklist.md`).
- Plugins: backup plugin; security plugin; caching; SEO.
- Updates: test updates in container/staging first; apply to production; verify checkout and landing pages after update.

Source: `knowledge_base/wiki/WebsiteInfrastructureMustHaves.md`; `domains/web/`

### 2.3 CRM / Marketing Automation (Mautic)
- Integration with WordPress (`MauticandWordpressIntegration.md`).
- Setup: configure segments (`Segments.md`); lead scoring (`Grant Cardone CRM System.md`); automation flows (`Automation.md`).
- Data hygiene: suppress cold non-responders; segment by behavior (engaged, buyer, VIP, cold).

### 2.4 Accounting / ERP (FrontAccounting)
- Source files: `domains/operations/sop/` (Purchase Order, Invoice Supplier, Customer Payment, Inventory Transfer, etc.)
- Setup: company settings; chart of accounts; supplier/customer records; tax settings.
- Processes: purchasing (create PO → receive → pay supplier); invoicing (create invoice → receive payment → record); inventory lifecycle (`Inventory Lifecycle Management.md`).
- Reports: monthly P&L; AR aging; inventory valuation.

---

## 3. Hosting, Containers, Backups, and Configuration

### 3.1 Local Hosting & Containers
- Our infrastructure runs locally using containers. Each service (WP/WC, Mautic, FA) runs in its own container for isolation.
- Setup: define container images; network configuration; volume mounts for persistent data; health checks.
- Reference: `knowledge_base/wiki/UsingGITforBackupandRestore.md` (version control applies to infrastructure config too)

### 3.2 Backups
- **Git backup**: all configuration and custom code tracked in Git (`UsingGITforBackupandRestore.md`).
- **Database backups**: scheduled exports of WP (posts, orders, users), Mautic (leads, segments, campaigns), FA (accounts, transactions).
- **File backups**: media uploads, plugin files, theme files, container volumes.
- **Restore procedure**: verify backup integrity monthly; test restore in staging; document restore steps.

### 3.3 Ansible for Configuration
- All server/container configuration managed via Ansible playbooks.
- Playbooks: install containers; configure networks; apply security updates; deploy code; set backups.
- Source control: playbooks in Git; versioned; reviewed before deployment.
- Execution: run playbook from control node; verify health checks; rollback if failure.

---

## 4. Support Team Operations

### 4.1 Support request handling
- Channel: email support / ticket system.
- Triage: categorize (technical, billing, marketing, operations); assign owner (`FHS-INTERNAL-INDEX.md` SOP references).
- Response: acknowledge within 1 hour; resolve within 24 hours for standard; escalate if complex.
- Documentation: update SOP if new issue type appears.

### 4.2 Technical support steps
1. Reproduce the issue in staging container.
2. Check logs (WP, Mautic, container logs, server logs).
3. Apply fix via Ansible (update playbook → test → deploy → verify).
4. If data issue: restore from backup (see Section 3.2); verify data integrity.
5. Update SOP and document in wiki.

---

## 5. Security & Compliance

- Access control: role-based (shareholder, C-suite, team member, support); least privilege.
- Password management: strong passwords; 2FA on all admin accounts.
- Updates: security patches applied within 48 hours; tested in container first.
- Data protection: backups encrypted; access logs maintained; compliance with relevant regulations.

---

## 6. Finance Operations Manual

*Shareholder / C-Suite Finance Guide.*

Tags: #finance #operations #howto #masterguide

---

### 6.1 Accounts Receivable (AR)
- Process: create invoice (`domains/operations/sop/`); send to customer; track due date; send reminder at day 7; follow up at day 30; escalate to collection if overdue.
- Tools: FrontAccounting (`FA Customer Payment.md`); reports (`FHS-INTERNAL-INDEX.md`).
- Metrics: days sales outstanding (DSO); collection rate.

### 6.2 Accounts Payable (AP)
- Process: receive supplier invoice (`FA Invoicing Supplier.md`); match to purchase order and receipt; approve for payment; schedule payment (`FA Paying Supplier.md`); record in books.
- Tools: `FrontAccounting`.
- Metrics: days payable outstanding; supplier performance (quality, delivery, price).

### 6.3 Loans & Debt
- Track loans (`GC Debt.md`): principal, interest rate, term, monthly payment.
- Ensure payments on time; review refinancing opportunities; separate personal and business debt (`GC Money Rules.md`).
- Source: `gurus/Grant Cardone/` (wealth/debt principles) + `FHS-INTERNAL-INDEX.md`

### 6.4 Cash Flow & Reporting
- Monthly reports (`FHS 0 Monthly Process.md`): P&L, balance sheet, cash flow, AR aging, AP aging, inventory valuation.
- CashFlow Calendar (`Troy White CashFlow Calendar.md`): plan promotions and cash needs 3-6 months ahead.
- Metrics per event: cost and result tracked; no ROI = redirect.

---

## 7. HR / People Operations (Future Guide)

*Placeholder — full HR guide to include: hiring process (`FHS Job Offer to Hired Process.md`), onboarding (`Employee Policies.md`), performance reviews, compensation, culture (`Leadership and High Performance.md`).*

---

## 8. Bibliography & Source References

- WordPress / WooCommerce / Mautic / Git / Containers / Ansible: `knowledge_base/wiki/WebsiteInfrastructureMustHaves.md`, `UsingGITforBackupandRestore.md`, `MauticandWordpressIntegration.md`
- Operations SOP files: `domains/operations/sop/`
- Finance: `gurus/Grant Cardone/` (Wealth Principles, Debt, Money Rules); `gurus/Troy White/` (CashFlow Calendar); `FHS-INTERNAL-INDEX.md`
- Marketing / Social: `SocialMediaHowTo.md`, `MarketingHowTo.md`, `swipe/` system
- Sales: `domains/sales/`, `gurus/Grant Cardone/`, `gurus/Jim Camp/`
- Owner / Shareholder docs: `knowledge_base/wiki/BookOwnershipIssues.md`, `FHSKevinOwnerBio.md`, `FHSKimOwnerBio.md`

---
*This guide links to source files, wiki pages, and SOP references. Where guru sources don't cover infrastructure, the wiki and SOP files provide the authoritative procedure. For shareholder-level strategy, see the wiki Owner Docs and the rebuilt `BusinessHowTo.md` (shareholder / C-suite version).*
