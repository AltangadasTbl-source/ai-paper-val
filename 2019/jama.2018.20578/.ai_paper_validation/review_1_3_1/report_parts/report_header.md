# Quantitative Quality-Control Consistency Review 1.3.1

> **Pending Human Adjudication**  
> This report records source-grounded quality-control candidates. It does not assign validity,
> importance, action, or a final correction. Every candidate below requires human adjudication.

## Executive Quality-Control Summary

The complete supplied package review registered **24 distinct candidates** (`C001`-`C024`). All 24
are reported below in stable-ID order and remain **Pending Human Adjudication**. The review covered
every direct source page and every registered quantitative/statistical relationship represented by
the reusable evidence assets. The candidates are proofreading and reporting-consistency observations;
their presence does not establish that the paper's conclusions are wrong.

## Package and Reused-Evidence Provenance

The package contains three unchanged, readable, unencrypted PDFs totaling 46 pages:

| Document | Identity and role | Pages | Pre-review SHA-256 |
|---|---|---:|---|
| [DOC-001 — `jama_flint_2019_oi_190079.pdf`](<../jama_flint_2019_oi_190079.pdf#page=1>) | Flint et al. main article; DOI `10.1001/jama.2019.10517` | 10 | `bc0a0760a27cbb664dd094b4ee12659acb000baf7c1207930f2558cb39affa45` |
| [DOC-002 — `joi180151supp1_prod.pdf`](<../joi180151supp1_prod.pdf#page=1>) | Zheng and Roddick protocol supplement; DOI `10.1001/jama.2018.20578` | 7 | `d47557e5447470a6d517fe82e52441b897d764ab96736d65d0e94ca564ce7e58` |
| [DOC-003 — `joi180151supp2_prod.pdf`](<../joi180151supp2_prod.pdf#page=1>) | Zheng and Roddick methods/tables/figures supplement; DOI `10.1001/jama.2018.20578` | 29 | `971a6088660ab2c02bbe5e73540d0c3231c779ca551a77a561295738500fb8a0` |

Forty-seven pre-existing evidence assets were inventoried and individually hashed before review:
29 were `USABLE`, 5 `PARTIAL`, 2 `STALE`, 11 `DUPLICATE`, and 0 `UNREADABLE`. They comprised document
maps, page manifests, native/normalized text, rendered pages, CPU OCR text/metadata, and full-document
layout text. Reused assets served only as locators and transcription aids. Every candidate was reopened
at its exact direct-PDF page. The stale DOC-001 manifest's statements about pages 7-9 OCR were not used;
the present page-level files and metadata were used as the asset record.

To close registered visual gaps, DOC-003 pages 7-26 were rendered at 180 dpi and pages 22-26 received
targeted Tesseract CPU OCR. DOC-001 page 8 was directly rendered for rotated-table confirmation. These
current-run derivatives were not added to the pre-review reused-asset hash inventory and were not
treated as source authority.

## Scope, Complete Coverage, and Exclusions

Complete source coverage comprised DOC-001 pages 1-10, DOC-002 pages 1-7, and DOC-003 pages 1-29.
Coverage included abstracts, narrative, methods, protocol definitions, Figures 1-2, Tables 1-5,
eMethods, eTables 1-6, eFigures 1-4, captions, footnotes, and every result-relevant numeric or
inferential relationship mapped from those units. DOC-003 reference-only pages 27-29 were inspected
and contained no additional result-relevant relationship.

The review was restricted to numeric/arithmetic, denominator/proportion/total, statistical reporting,
cross-location numeric, measure/label/scale, and rate-versus-count consistency. It did not perform a
broad methodology, study-design, clinical, novelty, misconduct, or raw-data audit. No web or external
literature was used.

**Important package limitation:** DOC-001 belongs to DOI `10.1001/jama.2019.10517`, whereas DOC-002
and DOC-003 belong to DOI `10.1001/jama.2018.20578`. The package lacks the matching main article for
DOC-002/DOC-003 and lacks the matching supplement for DOC-001. Internal matching within DOC-001 and
between DOC-002 and DOC-003 was completed, but a matched main-to-supplement result comparison could
not be performed for either identity. No scientific comparison was made across the two DOIs.

## Quantitative and Statistical Relationship Coverage

The numeric/reporting register contains 76 complete vectors:

`N001`, `N002`, `N003`, `N004`, `N005`, `N006`, `N007`, `N008`, `N009`, `N010`, `N011`, `N012`,
`N013`, `N014`, `N015`, `N016`, `N017`, `N018`, `N019`, `N020`, `N021`, `N022`, `N023`, `N024`,
`N025`, `N026`, `N027`, `N028`, `N029`, `N030`, `N031`, `N032`, `N033`, `N034`, `N035`, `N036`,
`N037`, `N038`, `N039`, `N040`, `N041`, `N042`, `N043`, `N044`, `N045`, `N046`, `N047`, `N048`,
`N049`, `N050`, `N051`, `N052`, `N053`, `N054`, `N055`, `N056`, `N057`, `N058`, `N059`, `N060`,
`N061`, `N062`, `N063`, `N064`, `N065`, `N066`, `N067`, `N068`, `N069`, `N070`, `N071`, `N072`,
`N073`, `N074`, `N075`, `N076`.

These vectors cover all 60 DOC-001 mapped relationships plus all support definitions and result
structures: 44 DIC/model rows, 13 trial outcome-definition rows, 13 risk-of-bias rows, 44 ARD cells,
18 NNT/NNH values, 4 total-stroke population rows, 88 participant-year rates, 44 sensitivity cells,
all study-flow counts, all 7 risk-of-bias graph domains, the complete Egger vector, and all 130 forest
study rows plus pooled records. All 130 displayed study RRs reproduced from their event counts and
totals at displayed precision; pooled participant totals reproduced; rounded weights summed within
their expected accumulation tolerance.

The inferential-statistical register contains 53 relationships:

`S001`, `S002`, `S003`, `S004`, `S005`, `S006`, `S007`, `S008`, `S009`, `S010`, `S011`, `S012`,
`S013`, `S014`, `S015`, `S016`, `S017`, `S018`, `S019`, `S020`, `S021`, `S022`, `S023`, `S024`,
`S025`, `S026`, `S027`, `S028`, `S029`, `S030`, `S031`, `S032`, `S033`, `S034`, `S035`, `S036`,
`S037`, `S038`, `S039`, `S040`, `S041`, `S042`, `S043`, `S044`, `S045`, `S046`, `S047`, `S048`,
`S049`, `S050`, `S051`, `S052`, `S053`.

Every relationship has an explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` record. Pass 1 examined
each inferential vector independently. Pass 2 revisited all 53 after registration of all 24 candidates
and after mechanical source recheck, considering denominator, arithmetic, population, label/scale,
duplicate-value, and cross-source implications. Pass 2 produced no new candidate. Thirty cross-source
match groups were also completed: 11 DOC-001 internal groups, 18 DOC-002/DOC-003 groups, and the
package identity boundary.

## Candidate Index

| ID | Candidate | Category | Status |
|---|---|---|---|
| C001 | HbA1c narrative and table units differ | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C002 | UKU rule permits a score above the stated maximum | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C003 | Placebo living-arrangement block omits two participants | Denominator, proportion, or total inconsistency | Pending Human Adjudication |
| C004 | Hyperlipidemia percentages reproduce opposite-arm denominators | Denominator, proportion, or total inconsistency | Pending Human Adjudication |
| C005 | Barnes participant counts use decimal formatting | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C006 | AIMS participant counts use decimal formatting | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C007 | Relapse-hospitalization percentage is a rounding-boundary mismatch | Denominator, proportion, or total inconsistency | Pending Human Adjudication |
| C008 | Total-cholesterol absolute difference does not reproduce | Numeric or arithmetic inconsistency | Pending Human Adjudication |
| C009 | LDL absolute difference does not reproduce | Numeric or arithmetic inconsistency | Pending Human Adjudication |
| C010 | Total-cholesterol and LDL result vectors are exact duplicates | Numeric or arithmetic inconsistency | Pending Human Adjudication |
| C011 | Protocol ARD subtraction wording conflicts with the sign rule | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C012 | Incident-cancer selected model conflicts with the printed rule | Statistical reporting inconsistency | Pending Human Adjudication |
| C013 | eTable 3 omits the ARD display scale | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C014 | All-patient major-bleeding ARD/NNH compatibility is conditional | Numeric or arithmetic inconsistency | Pending Human Adjudication |
| C015 | High-risk major-bleeding ARD and NNH do not reconcile | Numeric or arithmetic inconsistency | Pending Human Adjudication |
| C016 | Diabetes major-bleeding ARD and NNH do not reconcile | Numeric or arithmetic inconsistency | Pending Human Adjudication |
| C017 | Low/high-risk stroke events do not sum to all-participant events | Denominator, proportion, or total inconsistency | Pending Human Adjudication |
| C018 | Detection-bias table and graph imply different trial counts | Denominator, proportion, or total inconsistency | Pending Human Adjudication |
| C019 | Egger coefficient/SE do not reproduce the printed t statistic | Statistical reporting inconsistency | Pending Human Adjudication |
| C020 | Twelve-study stroke event totals differ between table and forest plot | Numeric or arithmetic inconsistency | Pending Human Adjudication |
| C021 | NNT is printed although the displayed ARD CI reaches zero | Statistical reporting inconsistency | Pending Human Adjudication |
| C022 | Diabetes stroke endpoint is called both CrI and CI | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C023 | Sensitivity endpoint is called both CrI and CI | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C024 | ASCEND ischemic-stroke row appears in a total-stroke forest plot | Measure, label, or scale inconsistency | Pending Human Adjudication |

## Candidate Evidence Cards

