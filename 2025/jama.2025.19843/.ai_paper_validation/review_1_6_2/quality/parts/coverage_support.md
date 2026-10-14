# Support mapping and numeric relationship coverage audit

Runtime agent: /root/audit_mapping_support. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Audit completed UTC: 2026-10-11T19:11:27Z.

Assigned source scope: DOC-003 PDF pages 1–9, DOC-004 pages 1–18, DOC-005 pages 1–3, and DOC-006 page 1: 31 distinct pages. Assigned numeric scope: every N201–N310 group, 110 distinct groups. The protocol's 153-page mapping closure is assigned to the other coverage audit; this shard independently checks the arithmetic and stated rules of protocol-linked N294–N308 using targeted direct-source extraction. This artifact does not assign or audit stable candidate IDs; the canonical candidate auditor owns that task. No stable-ID heading is introduced here.

**Coverage status:** COMPLETE for all 31 assigned pages and all 110 assigned numeric groups. No additional finding was identified. This is a coverage and calculation conclusion, not an adjudication of registered candidates or the paper.

## Inputs, independence, bounds and provenance

Read the complete scope, review contract, report specification, settings and tooling record. Current-run scientific inputs were extraction/parts/support_core.md, relationships/parts/numeric_support.md, and checkers/parts/numeric_support.md. Source inventory, asset inventory, source coverage, coverage manifest, routing preflight and agent execution manifest supplied the operational crosswalk. Targeted current statistical records were consulted only to verify that eFigure 9 trace-versus-sHR interpretation has a separate assigned statistical relationship, S036–S038. No legacy candidate, screening, checker, classification or report conclusion was read. No expected or desired finding count was used. The counts below are observed coverage cardinalities.

The three principal scientific inputs contain 97,123 characters. Fresh direct text for four support sources and the 17 targeted protocol pages totals 94,086 characters. Their conservative combined character bound is 191,209, including generated administrative text that did not need full textual rereading because the entire corresponding pages were inspected visually. Small targeted statistical excerpts remain within the 200,000-character bound. Exactly 31 freshly rendered source pages were inspected, within the 32-page bound. The 110 assigned N groups are within the 120-relationship bound.

Every assigned support source was reopened directly with the pinned fallback helper. Fresh page counts are 9, 18, 3 and 1; all are unencrypted. The audit rendered and visually read every assigned page. No new OCR was needed: SAP text is empty, but all nine direct-source renderings are legible. GPU OCR from the coordinator was a locator in the mapper; it is not the authority for this audit.

Derivative root: preprocessing/audit_mapping_support. Engine for every DOC-003/004/005/006-info.json, every DOC-003/004/005/006-native.txt, every DOC-003/004/005/006-pNNN.png, and protocol-N.txt listed below: PyMuPDF 1.26.4 through workflow_1_6_2/scripts/pdf_tools.py using tooling/venv/bin/python. Text uses sorted reading order; rendering uses CPU, 130 dpi. There is no custom Python extraction or orchestration.

Reproducible command templates, with the exact source filenames in the page ledger:

```bash
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py info "SOURCE.pdf"
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text "SOURCE.pdf" --first 1 --last LAST ".ai_paper_validation/review_1_6_2/preprocessing/audit_mapping_support/DOC-NNN-native.txt" --layout
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render "SOURCE.pdf" --page N ".ai_paper_validation/review_1_6_2/preprocessing/audit_mapping_support/DOC-NNN-pNNN.png" --dpi 130
```

For protocol-N.txt, the text template uses the exact protocol filename joi250087supp1_prod_1766516490.96011.pdf and --first N --last N for N = 13, 16, 19, 21, 26, 37, 69, 71, 84, 107, 110, 115, 117, 130, 143, 144, 153. Tracked amendment wording on the last three pages is interpreted through the separately assigned protocol coverage audit and its direct visual mapping, rather than silently treating both deleted and active native text as active.

Mechanical calculations and structural checks use Node 18.19.1 in [mechanical_checks.js](../../preprocessing/audit_mapping_support/mechanical_checks.js), with the complete results in [mechanical_checks.txt](../../preprocessing/audit_mapping_support/mechanical_checks.txt). This script performs arithmetic, link resolution and identifier closure only; scientific scope and inclusion judgments were made by the auditor. sha256sum confirmed all six direct-source hashes and all 116 reusable-artifact hashes unchanged at this audit snapshot; the reused check is retained in preprocessing/audit_mapping_support/reused_integrity_check.txt. The coordinator repeats the checks at completion.

## Direct-source page closure

Each row is a separate inspected page and matches one support-core mapping record. PLAN/REPORT roles below are assigned from content. Roster and sharing content are retrospective REPORT materials without prospective statistical design; they receive explicit non-applicability records rather than omission.

| Source page | Role | Independently confirmed mapping content | Audit status |
|---|---|---|---|
| [DOC-003 p.1](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=1) | PLAN | Final SAP version and signatures 11/04/2025; administrative cover, no result quantity | COMPLETE |
| [DOC-003 p.2](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=2) | PLAN | Contents; every endpoint and method destination mapped | COMPLETE |
| [DOC-003 p.3](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=3) | PLAN | Primary success definition, D30 event window, D60 adjudication, two competing events | COMPLETE |
| [DOC-003 p.4](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=4) | PLAN | All secondary and safety definitions, windows and MACE components | COMPLETE |
| [DOC-003 p.5](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=5) | PLAN | Flow, 206/103 allocation, 101 events, power inputs, ITT and descriptive rules | COMPLETE |
| [DOC-003 p.6](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=6) | PLAN | Event/censoring states, time origins, Gray test, Fine–Gray etiology adjustment and Cox sensitivity | COMPLETE |
| [DOC-003 p.7](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=7) | PLAN | Secondary survival and duration methods, RMST, adjusted models, disclosed MBP revision, SOFA threshold | COMPLETE |
| [DOC-003 p.8](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=8) | PLAN | Catecholamine/MV/RRT rules, hierarchical LV net benefit, bootstrap interval and safety Poisson model | COMPLETE |
| [DOC-003 p.9](../../../../joi250087supp2_prod_1766516490.96511.pdf#page=9) | PLAN | Recurrent-event comparison, two-sided alpha, missingness, change control, R version and reference | COMPLETE |
| [DOC-004 p.1](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=1) | REPORT | Contents identifies all six tables and nine figures; no independent result | COMPLETE |
| [DOC-004 p.2](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=2) | REPORT | Full eligibility and consent description; clinical thresholds transcribed | COMPLETE |
| [DOC-004 p.3](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=3) | REPORT | Every eTable 1 numerator, denominator, percentage and total; superscript 1 is a footnote | COMPLETE |
| [DOC-004 p.4](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=4) | REPORT | All three csHR/CI/P triples and etiology-adjusted Cox footnote | COMPLETE |
| [DOC-004 p.5](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=5) | REPORT | First eTable 3 page, every continuous and binary result, signed zeros and n=100 LVEF | COMPLETE |
| [DOC-004 p.6](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=6) | REPORT | Remaining eTable 3 rows, D60 dialysis dashes, population/measurement/bootstrap/RR footnotes and P omission | COMPLETE |
| [DOC-004 p.7](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=7) | REPORT | All 20 drug/day rows and all contributor counts, medians, IQRs and dashes; placebo-first column order | COMPLETE |
| [DOC-004 p.8](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=8) | REPORT | All eTable 5 exposures, denominators and duration distributions; other-drug footnote | COMPLETE |
| [DOC-004 p.9](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=9) | REPORT | All six other-etiology categories in each 21-patient arm and their percentages | COMPLETE |
| [DOC-004 p.10](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=10) | REPORT | Every eFigure 1 labelled trajectory count and percentage, six categories and two arm totals | COMPLETE |
| [DOC-004 p.11](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=11) | REPORT | Every D30/D60 mortality risk/event array label, logrank P=.47/.56 and legend | COMPLETE |
| [DOC-004 p.12](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=12) | REPORT | All 60 SOFA proportion bars, six components, two arms, five times and four score categories | COMPLETE |
| [DOC-004 p.13](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=13) | REPORT | Every D30/D60 MACE risk/event label, P=.87/.94, composite caption and legend | COMPLETE |
| [DOC-004 p.14](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=14) | REPORT | All seven MBP contributor counts, 60-mmHg threshold, arm legend and trajectories | COMPLETE |
| [DOC-004 p.15](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=15) | REPORT | All three dose panels, dose unit, arm legend, median/IQR shapes and sparse epinephrine observations | COMPLETE |
| [DOC-004 p.16](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=16) | REPORT | Hospital/ICU distributions and exact RMST labels 28/35 and 17.5/19 | COMPLETE |
| [DOC-004 p.17](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=17) | REPORT | Every event-multiplicity category and labelled patient frequency in both arms | COMPLETE |
| [DOC-004 p.18](../../../../joi250087supp3_prod_1766516490.97011.pdf#page=18) | REPORT | All four subgroup sHR/CI pairs, labels, treatment colors, time axes and curves | COMPLETE |
| [DOC-005 p.1](../../../../joi250087supp4_prod_1766516490.97511.pdf#page=1) | REPORT | Complete collaborator roster page; no statistical quantity or prospective design | COMPLETE / NOT_APPLICABLE |
| [DOC-005 p.2](../../../../joi250087supp4_prod_1766516490.97511.pdf#page=2) | REPORT | Complete collaborator roster page; no statistical quantity or prospective design | COMPLETE / NOT_APPLICABLE |
| [DOC-005 p.3](../../../../joi250087supp4_prod_1766516490.97511.pdf#page=3) | REPORT | Complete collaborator roster page; no statistical quantity or prospective design | COMPLETE / NOT_APPLICABLE |
| [DOC-006 p.1](../../../../joi250087supp5_prod_1766516490.97511.pdf#page=1) | REPORT | Sharing unavailable, bibliographic/registry identity; no independent outcome or statistical plan | COMPLETE / NOT_APPLICABLE |

For these four direct sources, reusable plus fresh-required units close as 9+0=9, 18+0=18, 3+0=3 and 1+0=1; mapped units are respectively 9, 18, 3 and 1, each COMPLETE. The latest package ledger separately closes DOC-002 with 150 reusable and three fresh-required pages, 153 mapped. Package totals are 191 reusable + three fresh-required = 194 total = 194 mapped. That protocol partition update does not alter this shard's 31 reusable-backed pages.

## Every assigned numeric relationship

All identifiers below are present exactly once and in order in the assigned inventory. Each grouped row states the independently audited rule; it is not a selection or sampling boundary.

| Explicit covered IDs | Numeric family and independently audited rule | Status |
|---|---|---|
| N201, N202, N203, N204, N205, N206, N207, N208, N209, N210, N211 | All 24 consent percentage cells, arm and category sums; 146+59=205, 69+32=101, 77+27=104; footnote superscripts distinguished | COMPLETE |
| N212, N213, N214, N215, N216, N217, N218, N219, N220, N221 | All ten continuous median/IQR/difference/CI rows; point containment and endpoint order; half-unit median-difference comparison | COMPLETE |
| N222, N223, N224, N225, N226, N227, N228, N229, N230, N231, N232, N233, N234 | Every eTable 3 binary count, percentage, RD/RR and interval; D60 dialysis absent rather than zero; LVEF n=100 and last-before-death definition retained | COMPLETE |
| N235, N236, N237, N238, N239, N240, N241, N242, N243, N244, N245, N246, N247, N248, N249, N250, N251, N252, N253, N254 | All 20 daily dose rows, contributor bounds, IQR order, nonnegative units and table/plot arm alignment; sparse epinephrine line interpolation not treated as observed missing days | COMPLETE |
| N255, N256, N257, N258 | All eight exposure percentage cells and four drug-duration rows; overlapping treatments not summed as disjoint participants | COMPLETE |
| N259, N260, N261, N262, N263, N264, N265 | All 12 other-etiology percentages, arm sums of 21, rounded percentage sums | COMPLETE |
| N266, N267, N268, N269, N270, N271, N272 | All ten trajectory percentages, every printed category count, 101/104 stack totals; unlabelled categories remain unlabelled | COMPLETE |
| N273, N274, N275, N276, N277, N278, N279, N280, N281 | All mortality/MACE risk and event arrays, monotonicity and bounds, final MACE agreement; instantaneous risk and inclusive cumulative events not assumed complementary | COMPLETE |
| N282, N283, N284 | Seven MBP contributor counts, all 60 SOFA bars, four RMST labels; graphic coordinates and unlabelled histogram bins not invented | COMPLETE |
| N285, N286 | All SAE multiplicity frequencies; patient sums 101/104, event sums 140/139, participants with at least one SAE 59/61 | COMPLETE |
| N287, N288, N289, N290, N291, N292, N293 | Four subgroup sHR/CI pairs and three csHR/CI/P triples; estimate containment, limits and model identity; no crude ratio substituted for hazards | COMPLETE |
| N294, N295, N296, N297, N298, N299, N300 | Plan totals, event diagnostic, stated sample-size input limits, recruitment arithmetic/precision and randomization parameters | COMPLETE |
| N301, N302, N303, N304, N305, N306, N307, N308 | Event/adjudication windows, event/censor states, dose/timing and nominal preparation quantities, weaning/stopping thresholds, secondary hierarchy, historical background quantities | COMPLETE |
| N309, N310 | Results cover/eligibility descriptions and complete roster/sharing records; no additional numeric result omitted | COMPLETE |

Arithmetic independently reproduced all 76 displayed count/denominator/percentage cells in the support report. Each has overlapping half-unit intervals: gap zero. All 11 observed binary risk differences and seven printed risk ratios overlap the recomputed intervals. Four zero-event RRs remain unestimated in accordance with the printed footnote. All ten continuous differences overlap half-unit intervals. Every reported median lies within its IQR and every point estimate within its ordered confidence limits. The risk arrays are nonincreasing; cumulative event arrays are nondecreasing and individually bounded by initial arm totals. The four logrank P values and three csHR P values are fully transcribed and assigned to the statistical lane; no P value is inferred from unprinted data.

This audit confirms numeric reconciliation, not identity between distinct estimands. It does not infer that medians of duration plus free days sum to 30, that participant counts equal event totals, that RMST equals an ordinary arithmetic mean, or that sHR equals final crude success risk. In eFigure 9, curves cross or terminate before the full reported outcome window; their graphic endpoints do not supply a same-method reconstruction or establish a reversed time-weighted hazard contrast. That limitation is explicitly mapped rather than omitted.

## Independent audit of the support checker's seven exclusions

No exclusion below produces an additional Route A or Route B finding in this assigned numeric scope. Planned/report semantic issues remain separately reviewed; numeric reconciliation does not screen those issues out.

| Excluded observation | Independent rule check | Audit result |
|---|---|---|
| eTable 3 MV duration: 21/22 medians versus −0 difference | Source values reproduced. Half-unit recomputation [20.5,21.5]−[21.5,22.5]=[−2,0] intersects [−0.5,0.5]. Gap zero, within precision rule. No interval/test conflict is present. | ROUNDING_OR_DISPLAY_PRECISION supported |
| Consent/etiology/trajectory category percentages sum to 100.1% or 100.2% | Integer categories exactly exhaust the stated populations. Four-category and six-category half-unit percentage-sum intervals contain 100%. No count/denominator discrepancy exceeds the threshold. | ROUNDING_OR_DISPLAY_PRECISION supported |
| Recruitment 206/14 versus 15.8 per site | Half-unit recomputation [14.172414,15.296296], printed [15.75,15.85], gap 0.453704; relative discrepancy 0.028715 ≤0.05. Also administrative rather than an altered population or decision rule. | ROUNDING_OR_DISPLAY_PRECISION supported |
| Net-benefit formula omits grouping around wins minus losses | Adjacent pairwise hierarchy, net-benefit name and positive-benefit interpretation establish the grouping. No numerical output changes; this is not a printed numeric slip or an interval/test conflict. | NOTATION_OR_TYPOGRAPHY supported |
| Protocol fixed-band preparation recipes versus nominal dose prose | Recorded concentrations/flow arithmetic is reproducible under the named nominal diluent convention. The comparison is inside prospective operational material; it does not establish an administered dose or an in-focus statistical-design discrepancy. No REPORT-side differing actual-dose input is supplied in this numeric group. | OUT_OF_FOCUS supported for this plan-internal observation |
| 206 subjects not uniquely reconstructible from the stated event-count inputs | Full-precision normal-quantile diagnostic gives 100.250777 success events, ceiling 101. No complete supplied equation/competing-event/accrual/censoring specification establishes a uniquely reproducing method for 206. No conflicting printed subject calculation or other-row reproduction is established. | CONDITIONAL_OR_UNREPORTED supported |
| Risk plus cumulative event labels sometimes exceed initial total | Both exact source arrays are retained. A risk set at an instant and events through that instant need not be disjoint; source curves contain event-time steps. No display asserts their sum is a participant partition. Each array and final event totals satisfy its stated bound. | CONTEXT_RESOLVES supported |

No exclusion is based solely on a displayed zero P value. There is no source interval/P or point/interval conflict hidden by a precision exclusion in this shard. Calculations concern the supported displays; unreported method inputs are named rather than assumed.

## Structural, integrity and wording checks; coordinator repairs

The 31 support-map source links, six numeric-inventory local links and 14 support-checker links all resolve: 51 in total. Every PDF link has a truthful physical #page=N anchor within the freshly confirmed page count. Numeric rows carry exact document/page/display locations, with the complete transcription crosswalk supplying the repeated rows. No workbook, CSV or Office pagination is fabricated.

Every coverage-manifest row inspected contains exactly one plain relative artifact path. Mapping, numeric and inventory rows are complete; subsequent recheck, statistical-pass-2 and canonical-audit stages remain the coordinator's completion obligations at this snapshot. This shard does not claim those later stages complete. The execution manifest records this agent once, with high effort and a distinct fresh runtime ID, and records the existing mapper/checker scopes without agent reassignment. The mandatory auditor must check the final two-pass/screening/ledger/recheck identity conditions after those artifacts are complete.

Neutral vocabulary scan found only the permitted established term referring to graphical uncertainty bars, with no prohibited description of the authors' work or reported values in the three assigned scientific inputs. No grading, severity, acceptance or suggested disposition is supplied here. Missing plot coordinates and raw data are bounded reconstruction limitations rather than evidence of a reporting inconsistency.

Repairs recorded for coordinator-owned metadata:

| Repair | Concrete reason | Status |
|---|---|---|
| Replace completed numeric scope wording that still said stable IDs pending | Inventory now explicitly contains N001–N095 and N201–N310, so completion scope should name the actual IDs | Coordinator confirmed completed |
| Replace hypothetical blank-page wording for protocol pp.4/49 and account for the newly audited signed p.95 | Direct-source inspection identifies signed version pages; scientific closure and asset partition must describe the actual content and direct inspection | Coordinator confirmed completed; latest source ledger shows 150+3=153 protocol units |
| Merge this assigned shard without dropping its page, ID, exclusion and provenance records | Canonical audit must cover the disjoint union and preserve all closure facts | Coordinator completion task |

No source value, checker finding, screening decision or stable ID was altered by this shard. No additional F-QAS finding, candidate registration or source-value repair is requested.

## Bounded limitations and final assigned-scope closure

Legacy extraction/renderer versions are unspecified; fresh renderings and text use the recorded pinned engine. Native SAP extraction is empty, but complete visual rereading closes all nine pages. Plots do not print exact coordinates, SOFA subgroup denominators, uncertainty-bar definitions or histogram-bin counts; this audit checks their printed labels and mapped qualitative content. No participant-level records, fitted model objects, bootstrap replicates or complete subject-count equation are supplied. This shard does not infer those inputs or broaden into clinical or raw-data auditing.

Final assigned scope: 31/31 direct support pages; 110/110 N groups; seven/seven support checker exclusions independently audited; 51/51 local links resolving; no unresolved source-unit or relationship-unit gap. Candidate inclusion audits and final whole-run structural closure are delegated to the canonical auditor, with this complete durable handoff.
