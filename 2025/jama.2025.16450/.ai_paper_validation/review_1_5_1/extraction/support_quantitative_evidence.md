# Canonical Support Quantitative Evidence Map

## Merge scope and authority

This is the lossless canonical index of support mapping from DOC-002 through DOC-005. It incorporates the complete, page-specific records in `parts/support_protocol.md`, `parts/support_manual_001_081.md`, `parts/support_manual_082_162.md`, and `parts/support_sap_results.md`. For DOC-004 pp.16-48, `parts/support_sap_016_048_repair.md` is authoritative and supersedes the original encoding-limited wording while preserving that original extraction-gap provenance.

All source records remain preserved verbatim in their part artifacts; the canonical numeric and statistical inventories give every source record a stable N/S identifier and retain the originating provisional identifier, exact location, values/definitions, and match key by reference. No candidate diagnosis is made here.

| Source | Complete page scope | Direct mapping status | Result-relevant record families | Explicit no-applicable scope |
|---|---|---|---|---|
| DOC-002 protocol | pp.1-35 | COMPLETE direct rendered review; source text encoding limited | PRO-N001–N024; PRO-S001–S010 | Administrative/background/reference pages as itemized page-by-page in `parts/support_protocol.md` |
| DOC-003 manual | pp.1-162 | COMPLETE direct rendered review; source text encoding limited | MAN1-N001–N008; MAN2-N001–N019 | All remaining pages explicitly mapped as no applicable in the two manual part artifacts |
| DOC-004 SAP | pp.1-48 | COMPLETE; pp.1-15 original direct/visual map and pp.16-48 repaired direct visual map | SAP-N001–N005, SAP-S001–S005; SAPR-N001–N022, SAPR-S001–S010 | pp.1-7 administrative; pp.20,31,46-47 no additional/applicable relationship as page maps state |
| DOC-005 results supplement | pp.1-16 | COMPLETE direct-PDF confirmation | RES-N001–N008; RES-S001–S004 | p.1 title/inventory only; all other no-applicable details are explicit in `parts/support_sap_results.md` |

## Canonicalization map

| Canonical IDs | Source records retained without change | Exact-source/value/label/match-key authority |
|---|---|---|
| N044–N067 | PRO-N001–PRO-N024, one-to-one | `parts/support_protocol.md`, Numeric/reporting relationships table and page coverage |
| N068–N075 | MAN1-N001–MAN1-N008, one-to-one | `parts/support_manual_001_081.md`, Quantitative/statistical relationship table |
| N076–N094 | MAN2-N001–MAN2-N019, one-to-one | `parts/support_manual_082_162.md`, Result-relevant quantitative relationships table |
| N095–N099 | SAP-N001–SAP-N005, one-to-one | `parts/support_sap_results.md`, SAP relationships and matching keys table |
| N100–N121 | SAPR-N001–SAPR-N022, one-to-one | `parts/support_sap_016_048_repair.md`, Numeric/reporting relationships table; authoritative for DOC-004 pp.16-48 |
| N122–N129 | RES-N001–RES-N008, one-to-one | `parts/support_sap_results.md`, DOC-005 numeric relationship inventory |
| S028–S037 | PRO-S001–PRO-S010, one-to-one | `parts/support_protocol.md`, Inferential-statistical relationships table |
| S038–S042 | SAP-S001–SAP-S005, one-to-one | `parts/support_sap_results.md`, SAP relationships and matching keys table |
| S043–S052 | SAPR-S001–SAPR-S010, one-to-one | `parts/support_sap_016_048_repair.md`, Statistical relationships table |
| S053–S056 | RES-S001–RES-S004, one-to-one | `parts/support_sap_results.md`, eTables 3-4 statistical definitions |

## Material support-specific cross-source anchors

- Protocol/SAP prospective planning: 58% to 48% target primary risk; 550/group simulation, 1160 planned after 5% attrition; final alpha .044 after interim spending. These are planning values, not final outcomes.
- SAP repair: primary ITT robust-Poisson RR with log link and site/gestational-age adjustment; primary composite at 36 weeks PMA; safety as treated/SAF.
- Results eTable 4 p.8 uses `RR = risk difference` in its abbreviation line while the table header/model text use relative risk. This is preserved as `RES-S004` label evidence only; no candidate conclusion is made.
- Results eTables 6-7 are event-frequency tables, not participant-incidence tables; retain quantity type before comparison.

## Limitations

DOC-002 through DOC-004 have embedded font encoding failures. Fresh direct source rendering and visual review were used where stated; original native/layout/OCR outputs are retained only as extraction provenance. All support sources except DOC-005 are protocols, SAP, or manual content; planned definitions/values must not be treated as final results without an exact population/time/model match.
