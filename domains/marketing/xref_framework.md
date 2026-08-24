# RTM / XREF Framework — Tracking Source Incorporation
# Pattern established in Phase 4 master guides

## Guru-side file (kb/guru/<Guru>/xref_<Source>.md):
# Source: file path
# Format: para [N] src [file] [line/section] → dest [domain/file] [para/section]
# Example:
# para 28 src /gurus/Eben Pagan/Wiki/MarketingMindsets.md line 28 → MarketingHowTo.md Section 2

## Domain-side file (domains/<Domain>/xref_<Source>.md):
# Source → Destination mapping
# Format: para [N] src /gurus/<Guru>/<Source>.md line X → <Domain>HowTo.md para Y Section Z
# Example:
# para 28 src /gurus/Eben Pagan/Wiki/MarketingMindsets.md line 28 → MarketingHowTo.md Section 1b

## Purpose:
- Every sentence/paragraph from guru source material is tracked.
- Every incorporation is linked to domain guide section.
- Conflicts between gurus are documented in domain guides (not here — see HowTo.md Section 1b).

## Tracking location (EXTERNAL to source files — NOT inside kb/guru/):
- Domain-side xref files live in `domains/<Domain>/xref_<Source>.md` (e.g., `domains/marketing/xref_Eben_Pagan_MarketingMindsets.md`).
- Central framework / index lives in `domains/marketing/xref_framework.md` or a dedicated `kb/xref_index/` directory.
- NO files placed inside `kb/guru/<Guru>/` directories (those contain original source material only).
- Eben Pagan: MarketingMindsets.md (xref_MarketingMindsets.md created)
- Grant Cardone: Mistakes.md, Unbreakable.md, Cold_Prospecting.md (xref files pending)
- Dave Dubeau: Brand.md, Content.md, WebTV.md (xref files pending)
- Joanna Lindenbaum: Referral_Shame.md (xref pending)
- DigitalMarketer: Email_Playbook.md, Subject_Lines.md, Launch.md (xref pending)
