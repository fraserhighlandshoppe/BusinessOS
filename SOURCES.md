# BusinessOS Sources & Conventions

## Internal Wiki
- Base URL: http://fhsws002.ksfraser.com/infra/wiki/index.php?title=Main_Page
- Server: fhsws002.ksfraser.com (192.168.1.66), MediaWiki
- Harvest scope: pages tagged FHS, Business, or any GURU category
- Harvest method: text search AND Category membership (~/bos_work/wiki_harvest.py);
  text search alone misses ~half the pages (e.g. only 37 of 97 Grant Cardone pages)
- Known guru categories: Grant Cardone (+ Ventures), Troy White, Ali Brown,
  Andy Tanner, Blair Singer, Brian Tracy, Dan Kennedy, Dave Dubeau, Don Campbell,
  Eben Pagan (+ case variants), HubSpot

## Content Organization
- Raw source material (transcriptions, converted pages/PDFs): `knowledge_base/gurus/<GuruName>/`
- Distilled/consolidated knowledge: `domains/<domain>/` (marketing, sales, email, operations, ...)
- Domain master guides: `domains/<domain>/<Domain>HowTo.md` (with bibliography)

## File Requirements
Every knowledge `.md` must have:
1. **Attribution** - all guru(s)/sources involved (e.g. article by Jack in Joe's newsletter credits both)
2. **Subject hashtags** - e.g. `#sales #marketing #facebook #email`
3. **Guru hashtags** - full names, e.g. `#GrantCardone #RussellBrunson`
4. **Filename from source title** where non-generic (e.g. `10X Sales Process.html` -> `10XSalesProcess.md`)

## Processing Phases
1. Dedupe (identical copies consolidated into `knowledge_base/gurus/`), purge junk, commit/push
2. File non-duplicate strays into correct guru/domain folders
3. Summarize each source into domain knowledge files (tagged + attributed)
4. Merge per-domain into master "here's how to run your business" documents with bibliography
