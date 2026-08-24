# RTM / XREF Framework — Tracking Source Incorporation (table format)
# Pattern: para-by-para from source file, ordered, in table format.

## Guru-side tracking: knowledge_base/gurus/<Guru>/xref_<Source>.md
- Table: | Para | Source reference (line/section) | Destination domain/file (para/section) |
- Example: Eben Pagan/xref_MarketingMindsets.md (para 1, 13, 26, 28, 42 mapped)

## Domain-side tracking: domains/<Domain>/xref_<Source>.md
- Table: | Para | Source guru/file (line) | Destination domain/file (para/section) |
- Example: marketing/Eben_Pagan_MarketingMindsets_xref.md (same mapping, domain-oriented)

## Purpose:
- Every paragraph from guru source tracked to domain incorporation.
- Every domain incorporation tracked back to guru source paragraph.
- Conflicts documented in HowTo.md Section 1b (not in xref table — table is mapping only).

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
- Domain-side xref files live in `domains/<Domain>/xref_<Source>.md` (e.g., `domains/marketing/Eben_Pagan_MarketingMindsets_xref.md`).
- Central framework / index lives in `domains/marketing/xref_framework.md` or a dedicated `kb/xref_index/` directory.
- NO files placed inside `kb/guru/<Guru>/` directories (those contain original source material only).
- Eben Pagan: MarketingMindsets.md (xref_MarketingMindsets.md created)
- Grant Cardone: Mistakes.md, Unbreakable.md, Cold_Prospecting.md (xref files pending)
- Dave Dubeau: Brand.md, Content.md, WebTV.md (xref files pending)
- Joanna Lindenbaum: Referral_Shame.md (xref pending)
- DigitalMarketer: Email_Playbook.md, Subject_Lines.md, Launch.md (xref pending)
