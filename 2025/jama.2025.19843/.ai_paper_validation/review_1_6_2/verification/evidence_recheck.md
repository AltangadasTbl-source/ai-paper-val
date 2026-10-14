# Mechanical evidence recheck — Workflow 1.6.2

Pending Human Adjudication. Fresh runtime agent: `root/evidence_recheck`; model `gpt-6.1-sol`; reasoning effort `high`. Scope: every assigned stable ID C001, C002, C003, C004, C005, C006, C007, with every location in the registered endpoint, analysis and SAP catalogues. Evidence states record source facts only.

## Direct-source method and bounded reading waves

Direct supplied PDFs were freshly extracted with the recorded pinned fallback interpreter and `workflow_1_6_2/scripts/pdf_tools.py text SOURCE --first N --last N OUTPUT --layout`, engine PyMuPDF 1.26.4 sorted reading order. Fresh derivatives are under `preprocessing/evidence_recheck/`: `main-direct.txt` (DOC-001 pp.1–10), `results-direct.txt` (DOC-004 pp.1–18), `roster-direct.txt` (DOC-005 pp.1–3), `sharing-direct.txt` (DOC-006 p.1), and `protocol-N.txt` for each of the 20 protocol pages listed below. The extraction reports exact page scope; native text was checked together with page context and targeted source renders, rather than treating reusable OCR as authority.

Reading wave A: DOC-002 pp.8,14,15,35,37,53,59,60,81,82,83,84,99,105,106,107,127,128,129,130; 20 unique native-source pages, 74312 extracted characters, no image-only candidate evidence. Wave B: DOC-001 pp.1–10 and DOC-003 pp.1–9; 19 unique pages, 88164 native characters plus the bounded ledger/control context, 14 page images (five main and nine SAP). Wave C: DOC-004 pp.1–18, DOC-005 pp.1–3 and DOC-006 p.1; 22 unique pages, 38504 extracted characters, 12 page images. No reading wave exceeded 200000 normalized evidence characters, 32 rendered pages, or 60 candidate IDs. The union is 61 unique source pages; repeat citations were retained without counting them twice.

Fresh CPU rendering used `pdf_tools.py render SOURCE --page N OUTPUT --dpi 150` for main pp.2,3,4,6,7 and results pp.5,6,9,10,14,15. This run's exact-source CPU renders were inspected for SAP pp.1,2,3,5,6 (`preprocessing/inclusion_initial/sap-N.png`), SAP pp.4,7,8,9 (`preprocessing/cross_source/sap-N.png`) and results pp.11,12,13,16,17,18 (`preprocessing/inclusion_initial/results-N.png`). Their exact PDF/page provenance is documented in the current screening/checker artifacts. No new OCR was necessary. The recorded device is GPU_USER_REQUESTED for OCR; these PDF renders used CPU. Reusable OCR is a locator only. Sources and reused assets were not modified.

The absence comparisons below are bounded to all supplied REPORT material: main pp.1–10, results supplement pp.1–18, collaborator roster pp.1–3 and data-sharing statement p.1. Every page was inspected through fresh native text; image-based scientific displays were additionally read visually. Roster pages identify collaborators and sharing states data are unavailable; neither contains outcome outputs. No absence is asserted about unsupplied files, participant data, external registrations, or later amendments.

## Source-location union: every repeated occurrence found

Document roles are assigned from the actual content: the article's methods/results and the results supplement are REPORT; prospective protocol versions and the SAP's planned endpoints/models are PLAN. Administrative roster/sharing content belongs to the supplied REPORT package and has no compared inferential result.

### Endpoint catalogue E — PLAN, all nine occurrences

Each location contains the same relevant endpoint/subgroup statements: D30/D60 ECMO-free days, D30/D60 ventilation-free days, MACE including dialysis, D30 LV function by echocardiography, and primary/secondary assessments in acute-MI, myocarditis, post-cardiac-surgery and post-cardiac-arrest subgroups. All listed lines were found and matched in fresh direct-source text; none is represented by a sampled version.

| Exact location | Content location | Found / matched | Applies to |
|---|---|---|---|
| [DOC-002 PDF p.8](../../../joi250087supp1_prod_1766516490.96011.pdf#page=8) | Version 1.1 summary, printed p.6/45 | Yes / yes | C003, C004, C005, C006 |
| [DOC-002 PDF p.14](../../../joi250087supp1_prod_1766516490.96011.pdf#page=14) | Version 1.1 section 3.2, printed p.12/45 | Yes / yes | C003, C004, C005, C006 |
| [DOC-002 PDF p.15](../../../joi250087supp1_prod_1766516490.96011.pdf#page=15) | Version 1.1 section 4.1.2, printed p.13/45 | Yes / yes | C003, C004, C005, C006 |
| [DOC-002 PDF p.53](../../../joi250087supp1_prod_1766516490.96011.pdf#page=53) | Version 2.0 summary, printed p.6/46 | Yes / yes | C003, C004, C005, C006 |
| [DOC-002 PDF p.59](../../../joi250087supp1_prod_1766516490.96011.pdf#page=59) | Version 2.0 section 3.2, printed p.12/46 | Yes / yes | C003, C004, C005, C006 |
| [DOC-002 PDF p.60](../../../joi250087supp1_prod_1766516490.96011.pdf#page=60) | Version 2.0 section 4.1.2, printed p.13/46 | Yes / yes | C003, C004, C005, C006 |
| [DOC-002 PDF p.99](../../../joi250087supp1_prod_1766516490.96011.pdf#page=99) | Version 3.0 summary, printed p.6/46 | Yes / yes | C003, C004, C005, C006 |
| [DOC-002 PDF p.105](../../../joi250087supp1_prod_1766516490.96011.pdf#page=105) | Version 3.0 section 3.2, printed p.12/46 | Yes / yes | C003, C004, C005, C006 |
| [DOC-002 PDF p.106](../../../joi250087supp1_prod_1766516490.96011.pdf#page=106) | Version 3.0 section 4.1.2, printed p.13/46 | Yes / yes | C003, C004, C005, C006 |

### Analysis catalogue A — PLAN, all ten occurrences

| Exact location | Source statement found and matched | Applies to |
|---|---|---|
| [DOC-002 PDF p.35](../../../joi250087supp1_prod_1766516490.96011.pdf#page=35) | Version 1.1 section 12.1 systematically unadjusted and adjusted comparisons; relevant models depend on variable distribution/type | C007 |
| [DOC-002 PDF p.37](../../../joi250087supp1_prod_1766516490.96011.pdf#page=37) | Version 1.1 section 12.1.8 qualitative logistic, quantitative linear and mortality Cox adjustment | C007 |
| [DOC-002 PDF p.81](../../../joi250087supp1_prod_1766516490.96011.pdf#page=81) | Version 2.0 section 12.1 unadjusted comparisons, adjustment continues next page | C007 |
| [DOC-002 PDF p.82](../../../joi250087supp1_prod_1766516490.96011.pdf#page=82) | Version 2.0 adjusted-comparison continuation; committee-validated detailed plan | C007 |
| [DOC-002 PDF p.83](../../../joi250087supp1_prod_1766516490.96011.pdf#page=83) | Version 2.0 section 12.1.8 logistic/linear models and mortality survival analysis | C007 |
| [DOC-002 PDF p.84](../../../joi250087supp1_prod_1766516490.96011.pdf#page=84) | Version 2.0 mortality Cox-adjustment continuation | C007 |
| [DOC-002 PDF p.127](../../../joi250087supp1_prod_1766516490.96011.pdf#page=127) | Version 3.0 section 12.1 unadjusted comparisons, adjustment continues next page | C007 |
| [DOC-002 PDF p.128](../../../joi250087supp1_prod_1766516490.96011.pdf#page=128) | Version 3.0 adjusted-comparison continuation; committee-validated detailed plan | C007 |
| [DOC-002 PDF p.129](../../../joi250087supp1_prod_1766516490.96011.pdf#page=129) | Version 3.0 section 12.1.8 logistic/linear models and mortality survival analysis | C007 |
| [DOC-002 PDF p.130](../../../joi250087supp1_prod_1766516490.96011.pdf#page=130) | Version 3.0 mortality Cox-adjustment continuation | C007 |

All ten were found; cross-page paragraphs were read as continuations. They corroborate the later SAP's explicit secondary prescriptions; no inference is made that every generic protocol option remained the final model.

### SAP catalogue S — PLAN, all nine pages visually inspected

| Exact location | Found / source content matched | Candidate relevance |
|---|---|---|
| [DOC-003 PDF p.1](../../../joi250087supp2_prod_1766516490.96511.pdf#page=1) | Yes: final SAP 11/04/2025, study identity/signatures | Complete-plan boundary for C006 |
| [DOC-003 PDF p.2](../../../joi250087supp2_prod_1766516490.96511.pdf#page=2) | Yes: contents, no subgroup-analysis heading | Complete-plan boundary for C006 |
| [DOC-003 PDF p.3](../../../joi250087supp2_prod_1766516490.96511.pdf#page=3) | Yes: primary success/competing/censoring definitions | Complete-plan boundary for C006 |
| [DOC-003 PDF p.4](../../../joi250087supp2_prod_1766516490.96511.pdf#page=4) | Yes: secondary list; ECMO D30/D60, ventilation D30/D60, five-member MACE, SOFA >2 | C002, C003, C005; boundary C006 |
| [DOC-003 PDF p.5](../../../joi250087supp2_prod_1766516490.96511.pdf#page=5) | Yes: sample size, ITT and descriptive/primary methods | Complete-plan boundary for C006 |
| [DOC-003 PDF p.6](../../../joi250087supp2_prod_1766516490.96511.pdf#page=6) | Yes: primary Fine–Gray adjusted on primary etiology (including other causes), cause-specific sensitivity; no subgroup prescription | Corroboration C001; C006 boundary |
| [DOC-003 PDF p.7](../../../joi250087supp2_prod_1766516490.96511.pdf#page=7) | Yes: Cox mortality/stays, adjusted ECMO/free-day/organ analyses, five-member MACE and SOFA >2 | C002, C003, C005, C007; boundary C006 |
| [DOC-003 PDF p.8](../../../joi250087supp2_prod_1766516490.96511.pdf#page=8) | Yes: adjusted ventilation/free-day and RRT models; hierarchical LV Global Net Benefit and recurrent drug-reaction model | C003, C004, C007; boundary C006 |
| [DOC-003 PDF p.9](../../../joi250087supp2_prod_1766516490.96511.pdf#page=9) | Yes: etiology-adjusted Poisson adverse/serious-event comparisons, alpha, missing data and change-management | C007; complete-plan boundary C006 |

There is no subgroup-analysis prescription anywhere in these nine pages. The p.6 etiology adjustment list is not itself a subgroup-analysis prescription.

## Classification and evidence-state facts

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state |
|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main Randomization/Statistical Analysis vs REPORT Table 2 footnote c; PLAN SAP corroborates only | reproduced |
| C002 | protocol_report | P_R | P_R | PLAN SAP vs REPORT main Outcomes/results eTable 3 | reproduced |
| C003 | protocol_report | P_R | P_R | PLAN protocol/SAP vs REPORT main/results supplement | reproduced |
| C004 | protocol_report | P_R | P_R | PLAN SAP vs REPORT main Outcomes/results eTable 3 | reproduced |
| C005 | protocol_report | P_R | P_R, P_P, S_C | PLAN protocol vs PLAN SAP vs REPORT main/results supplement | reproduced |
| C006 | protocol_report | P_R | P_R | PLAN protocol/SAP vs REPORT main Figure 3/results eTable 6/eFigure 9 | reproduced |
| C007 | protocol_report | P_R | P_R | PLAN protocol/SAP vs REPORT main/results supplement | reproduced |

No registered role, relationship or domain requires a correction. C001's checker footnote-d locator had already been changed to footnote c before stable registration; the registered ledger correctly identifies c, so its state is `reproduced`, not `reproduced_after_transcription_correction`.

## C001 — Primary adjustment covariate descriptions do not reconcile

**Location found:** Yes, all registered locations: REPORT [main p.2 Randomization](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=2), [p.3 Statistical Analysis](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3), [p.6 Table 2 footnote c](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=6); PLAN SAP catalogue S p.6, corroboration only. All three main locations were freshly rendered and visually read.

**Source value/text matched:** Yes. Randomization uses primary cardiogenic-shock etiology and center. The Statistical Analysis paragraph says the primary analysis was adjusted on minimization stratification factors. Table 2 prints primary successful-weaning sHR 1.02 (0.74–1.39).

**Comparator matched:** Yes. Table 2 footnote c describes the Fine–Gray model as adjusted for cardiogenic-shock etiology, with no center specified; SAP p.6 likewise explicitly lists etiology. Footnote d concerns censoring and P-value omission and is not the adjustment footnote.

**Consistency rule applicable:** Focus C, Route B: descriptions needed to identify the fitted primary model should specify a coherent covariate set. Center and etiology are distinct minimization factors, not two names for the same variable.

**Calculation or logical comparison reproduced:** The general text implies {etiology, center}; the specific footnote identifies {etiology}. The printed estimate cannot establish whether the footnote is exhaustive. Thus the source-established recheck fact is inconsistent completeness of primary-adjustment descriptions, leaving center inclusion unclear, not a recomputed alternative sHR. Display-precision intervals are inapplicable to categorical covariate membership; no numeric discrepancy is asserted for 1.02 or its interval.

**Necessary inputs available:** Yes, the randomization factor list, general analysis sentence and specific table footnote are available for this logical comparison. **Exact missing inputs or definitions:** actual model formula/design matrix, center coding and a statement that footnote c is exhaustive or abbreviated.

**Source-grounded alternative interpretation:** The etiology footnote could be abbreviated while the fitted model included center; alternatively, the general adjustment sentence could refer loosely to etiology alone. Neither is demonstrated by the supplied model output.

**Direct observation versus inferred explanation:** Direct observations are the two printed descriptions and the factor list. Center omission from the fitted model is not observed and is not inferred as fact.

**Exact remaining human question:** Which covariates, including whether center was included, produced the reported adjusted primary sHR 1.02 (95% CI 0.74–1.39)?

**Classification:** `S_W`; all relationships `S_W`; domain `statistical_results`. Both conflicting descriptions are REPORT within DOC-001. SAP is PLAN but only corroborates the etiology wording, so it adds no P_R relationship. **Classification ambiguity:** the actual fitted formula is missing; content roles and precedence are clear.

**Evidence state:** `reproduced`. Determining fact: correctly located footnote c specifies etiology while the primary general adjustment description refers to the minimization factors, which p.2 identifies as etiology and center. The pre-registration locator repair does not alter any printed value.

## C002 — Organ-failure threshold differs between SAP and report

**Location found:** Yes: PLAN SAP catalogue S pp.4,7; REPORT [main p.3 Outcomes](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3), [results p.5 eTable 3 first two rows](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5), [results p.12 eFigure 3](../../../joi250087supp3_prod_1766516490.97011.pdf#page=12). All were visually confirmed; both repeated SAP occurrences were independently read.

**Source value/text matched:** Yes: SAP failure is SOFA score >2 in at least one of six organ systems, repeated in the secondary analysis paragraph.

**Comparator matched:** Yes: main report organ-failure-free days require SOFA score 0–1 for every component. The results figure distinguishes categories 0,1,2,3–4. eTable 3 prints free-day medians 12 (0–21)/14 (0–23), difference −2 (−10 to 4), and failure-day medians 9 (6–17)/12 (6–18), difference −3 (−5 to 2).

**Consistency rule applicable:** Focus D, Route B: planned/report thresholds for the same organ-failure/free-day endpoint must classify the component-score boundary consistently.

**Calculation or logical comparison reproduced:** For a living patient's day with one component exactly 2 and all others 0/1, no component exceeds 2, whereas not all components are 0/1. Thus absence of SAP-defined failure and the report-defined free-day criterion differ at a directly displayed integer category. Death-zero coding does not reconcile this living-day example. Display-precision intervals do not apply to an operational score cutoff; these are decision thresholds, not rounded measurements. No numerical discrepancy in the displayed medians or differences is asserted.

**Necessary inputs available:** Yes, both explicit cutoffs and the existence of category 2. **Exact missing inputs or definitions:** actual endpoint coding rule, handling of missing daily components and participant-level score histories; the number of affected days and revised summary values cannot be calculated from the package.

**Source-grounded alternative interpretation:** The SAP >2 text may be a shortened threshold description or the report 0–1 criterion may describe a different operational free-day definition. No supplied text states that score-2 days are handled separately in a way reconciling the two definitions.

**Direct observation versus inferred explanation:** The two criteria and extracted medians are direct. The hypothetical living-day example establishes logical non-equivalence; it does not establish that such a day occurred or quantify the effect on observed medians.

**Exact remaining human question:** Which component-score rule, especially for a score of 2, generated the organ-failure and organ-failure-free day summaries in eTable 3?

**Classification:** `P_R`; all relationships `P_R`; domain `protocol_report`. Prospective SAP content is PLAN; actual endpoint description and results are REPORT. The figure supports the score-category distinction rather than creating another report/report conflict. **Classification ambiguity:** None in content roles; operational coding remains missing.

**Evidence state:** `reproduced`. Determining fact: both exact-source SAP occurrences print >2, while the exact-source report prints 0–1 for each component, so the classification of score-2 living days differs.

## C003 — Planned day-60 free-day results are absent from supplied reports

**Location found:** Yes, every endpoint-catalogue E occurrence; SAP catalogue S pp.4,7,8; REPORT [main p.1 abstract](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=1), [main p.3 Outcomes](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3), [main p.6 Table 2 ECMO-free row](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=6), [results p.5 ventilation-free row](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5). The complete supplied REPORT boundary stated above was additionally checked for alternative outputs.

**Source value/text matched:** Yes. All nine protocol occurrences prescribe ECMO-free and ventilation-free days at D30 and D60; SAP pp.4,7,8 repeat the corresponding windows. Main Outcomes itself repeats 30 and 60 days, with death counted as zero.

**Comparator matched:** Yes. Table 2 supplies ECMO-free by day 30: 24 (0–26)/23 (12–26), difference 1 (−1 to 4). eTable 3 supplies ventilation-free by day 30: 6 (3–11)/6 (3–13), difference −0 (−3 to 2). The supplied result material contains no corresponding D60 free-day distribution or contrast. D60 mortality, lengths of stay and the follow-up period used to confirm D30 ECMO-weaning success are distinct quantities.

**Consistency rule applicable:** Focus D, Route A category 5: a planned key-secondary analysis is missing from supplied reports. Both outcomes are secondary outcomes named in the abstract, satisfying the workflow's key-secondary definition.

**Calculation or logical comparison reproduced:** The matched planned-window set is {D30,D60}; the corresponding reported free-day summaries identify {D30}. Absence was checked against all 32 REPORT pages, including all nine supplementary figure displays. Numeric half-unit intervals do not apply to prespecified day labels; no arithmetic can convert a D30 quantity into the D60 quantity merely by rounding.

**Necessary inputs available:** Yes, explicit endpoint windows and complete supplied report scope. **Exact missing inputs or definitions:** D60 free-day summaries and treatment comparisons, or a supplied dated decision removing those analyses. Participant histories required to derive the D60 results are unavailable.

**Source-grounded alternative interpretation:** D60 outputs may exist separately or have been removed under an unsupplied amendment. Complete provided reports do not establish either possibility.

**Direct observation versus inferred explanation:** Planned windows and printed D30 outputs are direct; lack of a named D60 output is a bounded source-coverage observation. It is not evidence that D60 data were never collected or analyzed.

**Exact remaining human question:** Where are the prespecified D60 ECMO-free and ventilation-free results, or what documented revision explains their absence from the supplied report package?

**Classification:** `P_R`; all relationships `P_R`; domain `protocol_report`. PLAN protocol/SAP specify the analyses; REPORT outputs do not contain the corresponding windows. Agreement among the plan versions adds no P_P relationship, and the main-report endpoint list is corroboration. **Classification ambiguity:** None; unprovided amendments remain a limitation.

**Evidence state:** `reproduced`. Determining fact: explicit repeated D60 free-day prescriptions with only D30 free-day outputs across complete supplied reports.

## C004 — Planned hierarchical LV-function composite differs from reported LVEF contrast

**Location found:** Yes, all nine protocol endpoint E occurrences (D30 LV function context); PLAN SAP catalogue S p.8 Left Ventricular Function; REPORT [main p.3 Outcomes](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3), [results p.5 LVEF row](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5), [results p.6 footnotes a/b](../../../joi250087supp3_prod_1766516490.97011.pdf#page=6). SAP and result row/footnotes were visually read.

**Source value/text matched:** Yes. SAP p.8 explicitly specifies Global Net Benefit at D30, hierarchical death, heart transplantation, then LV-function improvement/LVEF >30%; pairwise experimental/control comparisons determine wins/losses/ties, with a bootstrap confidence interval.

**Comparator matched:** Yes. Main Outcomes describes D30 echocardiographic LVEF. eTable 3 reports medians 45 (30–50), n=100, and 40 (25–50), difference 5 (−0 to 10). Footnote a uses D30 LVEF for survivors and the last available pre-death LVEF for patients who died; footnote b describes a median difference and bootstrap CI. No Global Net Benefit or hierarchical outcome output appears in the complete reports.

**Consistency rule applicable:** Focus D, Route A category 5: the planned hierarchical composite's definition is replaced in the supplied outcome presentation by an LVEF-only summary; category 5 applies to a changed prespecified composite even without key-secondary status.

**Calculation or logical comparison reproduced:** A marginal LVEF median/difference does not encode the death-first and transplant-second pairwise hierarchy or a normalized wins-minus-losses statistic. Printed medians differ by 45−40=5, which is consistent with the printed difference, and is not itself the candidate. As a check, integer-display medians [44.5,45.5] and [39.5,40.5] permit a difference interval [4,6], overlapping printed 5 interval [4.5,5.5]: gap 0, relative discrepancy 0. This numeric agreement cannot reconcile the two different outcome quantities. No rounding interval equates percentage-point LVEF difference and Global Net Benefit.

**Necessary inputs available:** Yes for identifying different outcome definitions/summary types. **Exact missing inputs or definitions:** participant death/transplant/LVEF records, pairwise wins/losses/ties and the planned net-benefit estimate/interval; detailed operational tie/improvement coding. The Global Net Benefit cannot be recomputed from marginal medians.

**Source-grounded alternative interpretation:** The LVEF row might be an additional descriptive summary, with the hierarchical analysis performed but omitted. That would preserve rather than resolve the missing supplied composite output. No inference is made about an unprovided analysis.

**Direct observation versus inferred explanation:** The hierarchical prescription and marginal median row are direct. Replacement versus addition is an unresolved explanation; the observed supplied outcome presentation lacks the planned hierarchy/net benefit.

**Exact remaining human question:** Was the planned death/transplant/LV-function hierarchical Global Net Benefit analysis performed, and what output or documented amendment connects it to the reported LVEF medians?

**Classification:** `P_R`; all relationships `P_R`; domain `protocol_report`. PLAN SAP prescribes the hierarchy; REPORT content supplies an LVEF contrast. Protocol D30 LV-function wording corroborates the endpoint context without conflicting with the more detailed SAP. **Classification ambiguity:** Whether the LVEF row is a substitute or an additional summary is unresolved; content roles remain clear.

**Evidence state:** `reproduced`. Determining fact: the actual supplied row and footnotes define a marginal LVEF summary, not the exact-source SAP's hierarchical composite/net-benefit quantity.

## C005 — Dialysis membership differs across MACE definitions

**Location found:** Yes, all nine protocol endpoint E occurrences; PLAN SAP catalogue S pp.4,7; REPORT [main p.3 MACE definition](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3), [results p.1 eFigure 4 contents title](../../../joi250087supp3_prod_1766516490.97011.pdf#page=1), [results p.5 D30 rows](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5), [results p.6 D60 rows](../../../joi250087supp3_prod_1766516490.97011.pdf#page=6), [results p.13 eFigure 4 title/curves](../../../joi250087supp3_prod_1766516490.97011.pdf#page=13). All image-based title/curve/count and table evidence was visually inspected.

**Source value/text matched:** Yes. Protocol and main define MACE using death, cardiac transplantation, permanent LVAD, stroke, dialysis and heart-failure rehospitalization.

**Comparator matched:** Yes. SAP pp.4,7 and results contents/figure title define MACE using the other five members, omitting dialysis. D30 MACE is 35/101 versus 36/104, RR 1.00 (0.69–1.46); D60 is 36/101 versus 39/104, RR 0.95 (0.66–1.36). D30 dialysis is 29/101 versus 38/104; D60 dialysis entries are dashes. Figure 4 repeats final D30 event counts 35/36 and D60 counts 36/39 and log-rank P=.87/.94.

**Consistency rule applicable:** Focus D, Route A category 5: the component set of a prespecified composite differs across supplied plan/report definitions. No component summation is needed or appropriate because participant overlap is unknown.

**Calculation or logical comparison reproduced:** Six-member set minus five-member set = {dialysis}, reproduced at every listed definition occurrence. The supplementary numeric copies match their figure final counts; there is no same-quantity count-copy discrepancy. A contextual subset diagnostic is also recorded: if D30 dialysis and MACE use the same population/window and dialysis is a composite member, the union count must be at least the dialysis count. The placebo printed counts 36 MACE and 38 dialysis do not satisfy the exact-integer subset condition; overlap cannot reduce a union below one component. However, under the workflow's mandatory display-precision rule, component interval [37.5,38.5] versus union interval [35.5,36.5] leaves gap 1; relative discrepancy 1/36=0.0277778, at most 0.05. Thus this diagnostic does not establish a separately qualifying numerical reporting issue or Route A category 3. The registered reproduced fact remains the explicit composite-definition change, for which numeric rounding does not apply to membership.

**Necessary inputs available:** Yes, every definition's component list, table headers N=101/104 and matching D30/D60 event rows. **Exact missing inputs or definitions:** participant-level composite membership/event dates, whether dialysis was included in computed MACE, whether a different dialysis eligibility subset or timing definition was used, and any dated component amendment. No revised MACE count is inferred.

**Source-grounded alternative interpretation:** The analyzed composite could be the five-component SAP/figure definition, with the main/protocol list retaining dialysis; alternatively, the analyzed definition could include dialysis and the figure/SAP wording be abbreviated. A distinct dialysis coding population would alter the subset diagnostic's applicability. None is specified in supplied text.

**Direct observation versus inferred explanation:** Component inclusion/omission, counts and figure labels are direct. The event-membership implementation and any production mechanism are not observed. The bounded subset comparison does not prove which definition produced the reported effect estimates.

**Exact remaining human question:** Did the reported D30/D60 MACE counts and contrasts include dialysis, and what component/window/population definition and documented plan revision apply?

**Classification:** `P_R`; all relationships `P_R, P_P, S_C`; domain `protocol_report`. Protocol versus SAP is PLAN/PLAN (`P_P`); main versus results supplement is REPORT/REPORT across documents (`S_C`); protocol/SAP versus conflicting report definitions is PLAN/REPORT (`P_R`). Precedence P_R > P_P > S_C > S_W selects P_R. The eTable dialysis row alone does not add another within-report definition conflict. **Classification ambiguity:** Actual composite coding is unavailable, but printed-definition relationships are clear.

**Evidence state:** `reproduced`. Determining fact: every six-member protocol/main list includes dialysis and both SAP repetitions plus the results figure's repeated title give a five-member list without it. The contextual count diagnostic is explicitly screened by the display-precision rule and is not the evidence-state basis.

## C006 — Planned post-arrest subgroup differs from reported predefined other-etiology subgroup

**Location found:** Yes, all nine protocol endpoint E occurrences and [protocol p.107 allocation](../../../joi250087supp1_prod_1766516490.96011.pdf#page=107); every SAP catalogue S page; REPORT [main p.4 Statistical Analysis](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=4), [main p.7 Figure 3/caption and subgroup Results](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=7), [results p.9 eTable 6](../../../joi250087supp3_prod_1766516490.97011.pdf#page=9), [results p.18 eFigure 9](../../../joi250087supp3_prod_1766516490.97011.pdf#page=18). Full REPORT scope was checked for a separate post-arrest analysis.

**Source value/text matched:** Yes. Every protocol endpoint list prescribes primary/secondary analyses in four predefined etiologic groups ending with post-cardiac-arrest patients. Protocol p.107 separately uses other causes and center as minimization factors; this is an allocation specification, not a statement prescribing other-subgroup analysis. The entire SAP includes no subgroup-analysis prescription.

**Comparator matched:** Yes. Main methods call primary subgroup analyses predefined, with the minimization factor in parentheses; Figure 3 and its narrative call them predefined/prespecified. Fourth displayed subgroup is Other, successful weaning 15/21 levosimendan versus 12/21 placebo, sHR 1.61 (0.78–3.33). Its caption and eTable 6 include six diagnostic groups. Cardiac arrest contributes 5/21 versus 1/21. Figure 9 repeats the Other/Others population and sHR rather than showing a post-arrest-specific panel.

**Consistency rule applicable:** Focus D, Route A category 5: the report labels a broader subgroup analysis prespecified while the supplied endpoint prescriptions identify a narrower post-arrest subgroup; a planned primary post-arrest analysis is absent from supplied results.

**Calculation or logical comparison reproduced:** Other-group total =21+21=42; its arrest component =5+1=6. The plan's population and report's population are not synonyms. For the numeric population-size diagnostic, half-unit summation yields Other [41,43] versus arrest [5,7], gap 34 and relative discrepancy 34/42=0.809524 (>0.05); the substantive comparison is population membership and analysis prespecification. These counts do not reproduce a post-arrest treatment effect, and no such effect is inferred. The complete SAP and complete supplied reports contain no separate post-arrest model/output or explicit other-subgroup plan amendment.

**Necessary inputs available:** Yes, repeated endpoint prescriptions, allocation text, report prespecification text and exact diagnosis counts. **Exact missing inputs or definitions:** a dated subgroup-analysis plan/amendment prespecifying Other, the post-arrest-specific primary effect/output and patient event times required to compute it.

**Source-grounded alternative interpretation:** Investigators may have planned the minimization categories as analytic subgroups in an unsupplied detailed amendment, or broadened the arrest group because only six patients belonged to it. Neither is established by the allocation paragraph or current SAP.

**Direct observation versus inferred explanation:** Different subgroup definitions and reported counts/effect are direct. Reasons for broadening or not supplying the planned arrest analysis are inferred possibilities only.

**Exact remaining human question:** What supplied or dated analysis prescription supports the reported Other subgroup as prespecified, and what happened to the planned post-cardiac-arrest primary subgroup analysis?

**Classification:** `P_R`; all relationships `P_R`; domain `protocol_report`. PLAN endpoint prescriptions are compared with REPORT analytic populations and prespecification statements. The allocation category is a distinct planning function and does not create a P_P conflict by itself; agreement between main and supplement adds no S_C conflict. **Classification ambiguity:** Possible unsupplied detailed subgroup amendment; content roles are clear.

**Evidence state:** `reproduced`. Determining fact: exact-source planned endpoint lists name post-cardiac arrest, while the prespecified report output concerns a 42-person heterogeneous Other group with only six cardiac-arrest patients and no separate arrest output.

## C007 — Planned adjusted key-secondary analyses lack supplied outputs

**Location found:** Yes, every analysis-catalogue A occurrence; PLAN SAP catalogue S pp.7,8,9; REPORT [main p.1 abstract](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=1), [main p.4 methods/results](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=4), [main p.6 Table 2/footnotes](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=6), [main p.7 Table 3](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=7), results [p.5](../../../joi250087supp3_prod_1766516490.97011.pdf#page=5), [p.6](../../../joi250087supp3_prod_1766516490.97011.pdf#page=6), [p.11 mortality](../../../joi250087supp3_prod_1766516490.97011.pdf#page=11), [p.13 MACE](../../../joi250087supp3_prod_1766516490.97011.pdf#page=13), [p.16 stays](../../../joi250087supp3_prod_1766516490.97011.pdf#page=16), [p.17 serious events](../../../joi250087supp3_prod_1766516490.97011.pdf#page=17). All 32 REPORT pages form the absence boundary; visual scientific displays were inspected in addition to native text.

**Source value/text matched:** Yes. SAP p.7 prescribes etiology-adjusted Cox mortality and ICU/hospital-stay models and adjusted general linear ECMO-duration/free-day and organ-failure/free-day models; p.8 adjusted ventilation-duration/free-day models; p.9 etiology-adjusted Poisson serious-adverse-event comparisons. Protocol's systematic adjusted-comparison and secondary model paragraphs are found at all ten repeated locations. The abstract names mortality, ECMO-, ventilation- and organ-failure-free days, ICU/hospital stay and serious adverse events, making these endpoints key secondary under the supplied scope.

**Comparator matched:** Yes. Printed outputs include mortality RR 1.11 (0.70–1.75), ECMO median difference −1 (−2 to 1), ECMO-free difference 1 (−1 to 4), ICU RMST difference −1 (−5 to 3), hospital RMST difference −7 (−12 to −2), organ-free difference −2 (−10 to 4), ventilation-free difference −0 (−3 to 2), and serious-event patient counts 59/101 and 61/104. Mortality/MACE figures identify log-rank tests; stay figure labels RMSTs; serious-event figure supplies a frequency histogram. They do not identify the planned adjusted secondary treatment coefficient/output. The supplied regression output identifies the primary Fine–Gray model and its cause-specific sensitivity, not these adjusted secondary effects.

**Consistency rule applicable:** Focus D, Route A category 5: explicit planned key-secondary analyses are not supplied. The issue is absence of the prespecified adjusted output, not that an adjusted value differs from crude arithmetic or that a preferred alternative method was not used.

**Calculation or logical comparison reproduced:** Match each abstract-named endpoint to its explicit SAP regression prescription, then inspect the full REPORT union for an adjusted treatment effect/output. Mortality: planned adjusted Cox versus RR/log-rank outputs. ECMO/free days and organ/ventilation free days: planned adjusted general linear models versus marginal medians/differences. ICU/hospital stays: planned adjusted Cox versus RMST contrasts/log-rank methods. Serious-event counts: planned adjusted Poisson versus any-event patient counts and an event-frequency histogram. No matched adjusted secondary output is found. Numeric half-unit intervals cannot reconcile different estimands/models or create absent coefficients; no result is recomputed from counts as if it were the planned adjusted estimate.

**Necessary inputs available:** Yes, explicit planned models, abstract key-secondary identification, full supplied report coverage and each printed output's labels/footnotes. **Exact missing inputs or definitions:** adjusted treatment coefficients/contrasts and intervals for these endpoints, model formulas and inputs needed to reproduce them, or a documented revision removing the planned adjusted analyses. Their numerical values cannot be derived from aggregate summaries.

**Source-grounded alternative interpretation:** Adjusted models may have been fitted but omitted from the supplied package, or replaced under a revision not supplied. Generic report methods and missing secondary P values do not establish either. Table footnotes explain omission of secondary P values for multiplicity concerns, not omission of adjusted-effect estimates.

**Direct observation versus inferred explanation:** The model prescriptions and marginal outputs are direct. Absence is confined to the supplied REPORT union; no claim is made that the models were never fitted or that results would differ.

**Exact remaining human question:** Where are the prescribed etiology-adjusted treatment outputs for the named key-secondary endpoints, or what documented analysis-plan revision explains their absence?

**Classification:** `P_R`; all relationships `P_R`; domain `protocol_report`. Prospective analysis prescriptions are PLAN, observed methods/displays are REPORT. MACE-adjustment, catecholamine/RRT-adjustment and nonserious/recurrent drug-reaction passages were also found at the retained source locations but are contextual non-key occurrences and do not broaden the qualifying absence pattern. Agreement among plans or reports adds no relationship. **Classification ambiguity:** Unsupplied amendment or omitted outputs remain possible; roles and primary relationship are clear.

**Evidence state:** `reproduced`. Determining fact: the exact-source SAP explicitly calls for adjusted key-secondary models, while the complete supplied report displays/footnotes provide no identified output from those models. The D60 window absence remains separately registered as C003.

## Recheck closure

Seven of seven stable IDs covered; all seven evidence states `reproduced`; no registered transcription/value/location changes, no not-reproduced state, no source-location gap and no classification correction. Every repeated protocol occurrence and every relevant SAP occurrence was directly confirmed. Remaining items are the seven precise human questions and named missing operational/model outputs; they are not missing scientific coverage. No stable ID is removed and no human disposition is assigned.
