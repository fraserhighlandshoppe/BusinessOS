# Session Notes / Skills — Phase 4 OS Build (BusinessOS)
# Date: current session (commit 577226a, branch dedupe)
# Agent: opencode / assistant

---

## What was built / completed

### Master guides (Phase 4) — rebuilt as verbose OS manuals
- MarketingHowTo.md (174 lines) — Sections 1b (full guru incorporation) + 2-8 expanded
- EmailHowTo.md (71 lines) — Section 1b (DigitalMarketer + Pagan + Cardone + Lindenbaum)
- SalesHowTo.md (118 lines) — Section 1b (Cardone + Camp + Ziglar + conflicts)
- BusinessHowTo.md (231 lines) — rebuilt as Shareholder/C-Suite OS manual with sub-dept refs
- SocialMediaHowTo.md, WebConversionHowTo.md, MindsetHowTo.md, OperationsHowTo.md, TradingHowTo.md — updated with source tags / incorporation notes
- ITHowTo.md (154 lines) — new; WP/WC + Mautic + FA + containers + backups + Ansible + support
- FinanceHowTo.md (89 lines) — new; AR/AP + loans + debt + reporting + SOP refs
- LinkedInHowTo.md — new; profile/company page + engagement + measurement
- HRHowTo.md — new; hiring/onboarding + SOP ref + performance/culture

### Source incorporation pattern (Section 1b in guides; full in Marketing)
- Common paragraph for agreement across gurus (e.g., marketing = key money-maker: Pagan + Cardone agree)
- Separate paragraph per guru source (actual text or distilled claim) with `.md` file path
- Conflict notes (e.g., Pagan = audience/test first; Cardone = spend/promote fast) with recommendation
- Every sentence traces to source `.md` file (`knowledge_base/gurus/` or `knowledge_base/wiki/` or `domains/`)

### Guru sources incorporated (not exhaustive — pattern established)
- Eben Pagan: MarketingMindsets.md, Customer_Avatar.md, Email framework (118 docs synthesized)
- Grant Cardone: Mistakes.md, Unbreakable.md, Cold_Prospecting.md, CRM.md, Ventures.md, Wealth Principles.md
- Dave Dubeau: Brand.md (22 docs), Content.md (36 docs), Facebook.md, Email.md, WebTV.md
- Claude Hopkins: Scientific_Advertising.md
- Blair Singer: Branding.md
- Joanna Lindenbaum: Referral_Shame.md
- Jim Camp: Negotiating System.md
- Zig Ziglar: Closing the Sale.md
- DigitalMarketer: Email_Playbook.md, Subject_Lines.md, Launch.md, Customer_Avatar.md
- Mirasee / Iny: Launch.md
- Troy White: CashFlow_Calendar.md, Maximum_Profits.md
- FHS Owner / Kevin Fraser: FHSKevinOwnerBio.md, BookOwnershipIssues.md
- Wiki infrastructure: WebsiteInfrastructureMustHaves.md, UsingGITforBackupandRestore.md, MauticandWordpressIntegration.md, FHS-INTERNAL-INDEX.md

### RTM / XREF tracking framework (table format, external)
- Guru-side: `knowledge_base/gurus/<Guru>/ABC_xref.md` (alphabetical adjacency: `ABC.md` then `ABC_xref.md`)
- Domain-side: `domains/<Domain>/BCD_xref.md`
- Framework/index: `domains/marketing/xref_framework.md`
- Table format: `| Para | Source reference (line/section) | Destination domain/file (para/section) |`
- Conflicts in HowTo.md Section 1b, not in xref table (table = mapping only)
- Example: `MarketingMindsets_xref.md` (guru) + `Eben_Pagan_MarketingMindsets_xref.md` (domain)

### Design decisions / conventions
- Conflict resolution: present both guru views + recommendation based on stage (e.g., Pagan first 90 days → Cardone scale; Camp negotiation + Cardone closing; Singer brand + Cardone delivery)
- Verbose guides: written so 16-year-old or AI agent can follow step by step
- Tags: `Tags: #domain #howto #masterguide` + guru/domain hashtags at bottom; References linking to bibliography
- References in master guides: Bibliography links to `gurus/`, `wiki/`, `domains/`, `swipe/` files
- Phase 3 batch tag audit applied (`f677f31`); YAML errors fixed (`d3af9a0` — 15 business files)
- Joanna Lindenbaum: spelling corrected (`Joanna`, not `Joanne`); file incorporated fully; TODO cleared (`96bde24`)
- Swipe/formula system: `swipe/headline_formulas.md` (7 Power), `swipe/salesletter_formulas.md` (Hero's Journey), `swipe/swipe_verb/noun/adjective/number/audience.txt`

### Git branches / key commits
- `dedupe` branch; final `577226a`
- Key: `4e3d0df` Phase 1, `58fec24` Phase 2, `f52319d` Wiki harvest, `b590fcd` Phase 4 guides, `ee10e30` Email/swipe, `89b28c1` Social/Web/Mindset/Operations/Trading, `e3fa692` Phase 3 audit + JL TODO, `f677f31` Phase 3 tags, `b590fcd` Business rebuilt, `96bde24` JL spelling/incorporation, `d3af9a0` Business rebuilt + YAML fix, `c58fb83` IT + Finance + OS structure, `917cda8` Marketing Section 1b, `7e296cc` Email full, `49ec2a5` Sales/IT, `108dd4f` Marketing Section 1b expanded, `0e1c81b` Marketing Sections 2-8, `ffeb4fa` Marketing expanded + framework, `577226a` HR + LinkedIn + xref framework final

### What remains / next
- Full swipe verification: map filtered headline lines to 7 formulas; test substitution
- Full Phase 3 attribution: audit any remaining untagged domain source files
- Additional master guides: HR/LinkedIn created; remaining sub-domains (blog/post production, podcast, events) can follow OS pattern
- All guides expandable: read additional `knowledge_base/gurus/` source files and add Section 1b-style incorporation
- XREF expansion: apply `ABC_xref.md` + `BCD_xref.md` to remaining guru files (Cardone, Pagan, Dubeau, DigitalMarketer, Lindenbaum)
