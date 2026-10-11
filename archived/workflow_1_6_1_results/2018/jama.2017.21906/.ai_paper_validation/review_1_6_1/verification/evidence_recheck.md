# Mechanical evidence recheck

Fresh runtime agent: `/root/recheck_initial`; role `qc161_evidence_rechecker`; `gpt-6.1-sol` / `high`. Assigned stable IDs: C001 and C002. Both remain **Pending Human Adjudication**. This artifact records source facts and classification, without an adjudication or a proposed numerical replacement.

Read the complete `QUALITY_CONTROL_SCOPE.md`, review contract, report specification, performance profile and settings; the current canonical candidate ledger and initial screening table; the source, asset and tooling inventories; and the relevant current statistical-pass-1 and cross-source findings. Only supplied package evidence was used. Previous-run scientific conclusions were not read. Reused native/layout text served as a locator and transcription aid. The page images listed below, whose alignment to the current supplied PDFs is recorded in the current asset inventory or their direct-render provenance, were visually inspected for final confirmation. Selected current-PDF reads with direct `pdftotext -layout` independently confirmed the text and table alignment.

| ID | Evidence state | Review domain | Relationship type | All relationships | Classification change |
|---|---|---|---|---|---|
| C001 | reproduced | statistical_results | S_W | S_W | None; REPORT content and statistical-method identification confirmed |
| C002 | reproduced | protocol_report | P_R | P_R | None; prospective SAP PLAN content compared with main REPORT content confirmed |

Exactly two assigned IDs are covered. No cited-source inspection gap remains. Definitions needed to identify the time outputs and to connect the planned and reported age specifications remain unavailable as detailed separately below. Evidence state is an evidence-record fact, not a disposition.

## C001 — Identification of the adjusted time-effect outputs

**Evidence state:** reproduced

**Determining recheck fact:** Both Table 2 time rows, their distinct adjusted outputs, both footnote-b header references, and footnote c are present exactly as registered. The Statistical Analysis section describes the primary binary-outcome model and general adjustments but supplies no separate mapping from the two time-effect columns to their analysis targets. The registered method-identification gap remains after reading the complete table, footnotes and adjacent methods/narrative. No transcribed value or registered PDF page required alteration. The numerical differences establish distinct outputs; they are not treated as a requirement that a coefficient equal a marginal contrast.

**Finding provenance:** F-ST1-001; repeated pattern at door-to-balloon and door-to-needle time. Both affected rows are retained in this one ID.

### Exact location, source and comparator checks

| Exact supplied-source location | Found | Role by content | Printed content matched and comparison role |
|---|---|---|---|
| [Main PDF p. 6, Table 2 title and both effect-column headers](../../../jama_huffman_2018_oi_170166.pdf#page=6), printed p. 572 | Yes | REPORT | Table title identifies process-of-care and time-based outcomes adjusted for within-hospital clustering and temporal trends. Headers are Difference, % (95% CI), and Odds Ratio or β-Coefficient (95% CI); each has superscript b. These labels distinguish outputs but do not state each time target. |
| [Main PDF p. 6, Table 2 door-to-balloon time (STEMI) row, all four result columns](../../../jama_huffman_2018_oi_170166.pdf#page=6) | Yes | REPORT | Median (IQR), min: control 65 (53–105), n=4022; intervention 77 (55–118), n=3639. Difference 6.18 (−4.78 to 17.14); β-coefficient 13.00 (3.64–22.36), superscript c. All printed values and their alignment match the ledger. |
| [Main PDF p. 6, Table 2 door-to-needle time (STEMI) row, all four result columns](../../../jama_huffman_2018_oi_170166.pdf#page=6) | Yes | REPORT | Median (IQR), min: control 44 (30–67), n=1455; intervention 45 (27–75), n=1433. Difference 0.40 (−5.23 to 6.03); β-coefficient 5.00 (−5.20–15.20), superscript c. All printed values and their alignment match the ledger. |
| [Main PDF p. 6, Table 2 footnotes a, b and c](../../../jama_huffman_2018_oi_170166.pdf#page=6) | Yes | REPORT | Footnote a identifies eligible participants with reported process measures and exceptions to count/percentage presentation. Footnote b describes intervention versus control, marginal-effects differences with intervention minus control, mixed-effects logistic or quantile regression, a random-effects term for hospital clustering, and temporal trends. Its grammatical subject is odds ratios and β-coefficients, while both effect headers refer to it. Footnote c identifies β-Coefficient. No column-specific time estimand, quantile or standardization population is printed. |
| [Main PDF p. 3, Statistical Analysis section](../../../jama_huffman_2018_oi_170166.pdf#page=3), printed p. 569 | Yes | REPORT | Describes baseline adjustment for clustering and time; for primary 30-day MACE, mixed-effects logistic regression with random hospital effect and fixed effect for each four-month step; secondary GRACE adjustment; intention-to-treat reporting. This is not a distinct specification of each continuous-time output. The comparator text matches the cited registration. |
| [Main PDF p. 6, paragraph beginning with Table 2 below the table](../../../jama_huffman_2018_oi_170166.pdf#page=6) | Yes | REPORT | Context describes Table 2 as unadjusted and adjusted associations with clustering and temporal trends; individual binary medication effects are discussed. It provides no time-column mapping. This surrounding context was inspected together with the registered table location. |
| [Main PDF p. 7, process-of-care narrative preceding Primary Analysis](../../../jama_huffman_2018_oi_170166.pdf#page=7), printed p. 573 | Yes | REPORT | Narrative continues the binary procedure and discharge-medication effects. It supplies no separate door-to-balloon or door-to-needle effect definition. This is contextual evidence, not a new conflicting result or relationship. |

The source values and comparator text are therefore matched for every registered affected/contextual location. All locations are REPORT by their retrospective trial methods/results content, independently of filenames. The common percent header does not form the basis of this recheck: the row labels immediately identify the observed time measurements in minutes.

### Applicable rule and reproduced comparison

**Consistency rule applicable:** Yes, for focus C, statistical-method identification. When two reported adjusted outputs are candidates for extraction of an intervention time effect, the supplied analysis description must identify the quantity each represents sufficiently to distinguish their analyses. The rule is not arithmetic equality between the two outputs, a comparison of modeled effects with crude medians, or an assumed quantile-regression formula. No explicit source statement establishes that the two columns should equal one another.

**Logical comparison reproduced:** Yes. Both headers refer to the same footnote b; the source names logistic or quantile regression and marginal effects, identifies beta coefficients by footnote c, and reports different adjusted time outputs. It does not associate the two time columns with separate quantiles, scales, reference populations, conditional/marginal targets or other column-specific analysis definitions. Reading the primary-MACE logistic-model description on p. 3 and the p. 6–7 process narrative adds no such mapping. The absence is the registered method-identification observation, rather than an assertion that an unreported method was used.

**Calculation and display-precision interval check:** Each two-decimal estimate or CI endpoint is allowed its half-unit interval ±0.005. Closed bounds below conservatively include rounding ties. Counts n are exact counts; integer-display medians and IQR endpoints can be allowed ±0.5 minute, but do not supply identities for adjusted effects.

| Time output | Printed estimate (95% CI) | Estimate display interval | Lower-endpoint display interval | Upper-endpoint display interval |
|---|---|---|---|---|
| Balloon, difference | 6.18 (−4.78 to 17.14) | [6.175, 6.185] | [−4.785, −4.775] | [17.135, 17.145] |
| Balloon, β-coefficient | 13.00 (3.64 to 22.36) | [12.995, 13.005] | [3.635, 3.645] | [22.355, 22.365] |
| Needle, difference | 0.40 (−5.23 to 6.03) | [0.395, 0.405] | [−5.235, −5.225] | [6.025, 6.035] |
| Needle, β-coefficient | 5.00 (−5.20 to 15.20) | [4.995, 5.005] | [−5.205, −5.195] | [15.195, 15.205] |

Balloon β minus difference is 13.00−6.18=6.82, with possible displayed-input gap [12.995−6.185, 13.005−6.175]=[6.810, 6.830]. Needle β minus difference is 5.00−0.40=4.60, gap [4.590, 4.610]. Neither pair can coincide within display precision. All four estimates are contained in their own ordered intervals throughout these bounds. Balloon difference CI spans zero throughout the endpoint bounds; balloon beta CI excludes zero because its lower endpoint is at least 3.635. Both needle intervals span zero throughout their bounds. These facts establish distinct numerical and interval readings but do not prove either output fails its own statistical rule. Rounding cannot define which target produced each column. No P value, test statistic or normal-Wald identity is reconstructed.

**Necessary inputs available:** Yes for locating the outputs, reading their contrast, hospital/time adjustment, time-outcome units, eligible row counts, 95% CIs and printed model-family language; yes for the display-precision and method-description comparison. No for reproducing either adjusted model from data or identifying each column's exact estimand. Raw medians are not substituted for modeled quantities.

**Exact missing inputs or definitions:** Column-specific continuous-time model and output target; quantile if quantile regression was used; outcome transformation/link or scale if one was used; method of obtaining each marginal contrast versus coefficient; standardization/reference population and treatment of hospital random effects in prediction; output-scale units beyond the obvious minute observations; and interval construction/variance procedure. Individual data and fitted model/code are not supplied for exact refitting. The evidence does not establish whether all these operations were needed; their column-specific mapping is unavailable.

**Source-grounded alternative interpretation:** Footnote b's marginal-effects language and footnote c's beta label permit intentionally distinct marginal and conditional/quantile outputs as a possible interpretation. Distinct scales, quantiles or models could also explain two adjusted columns. The source does not identify which applies, and no equality or particular transformation is presumed. A reader may recognize the general quantile-regression family from the minute/median rows and footnote b, but that recognition does not itself identify how the separate difference and beta outputs were obtained. This alternative remains explicit for human review.

**Direct observation versus inferred explanation:** Directly observed: exact paired outputs, different balloon zero-inclusion readings, shared footnote references, named model families, and no separate target mapping in the compared descriptions. Inferred possibilities only: conditional versus marginal contrasts, differing transformations or quantiles, or any particular software operation. No cause is established by the numerical gap.

**Affected result or extracted value:** The adjusted intervention effect on the two reperfusion times, particularly door-to-balloon 6.18 (−4.78, 17.14) versus 13.00 (3.64, 22.36), and the quantity to which an extractor assigns each interval. No paper-level conclusion change is inferred.

**Exact remaining human question:** Which column-specific model, estimand, scale/units, quantile if applicable, and reference population generated the difference and beta-coefficient outputs for each time outcome in Table 2, and which adjusted time result belongs to each specified analysis?

### Classification confirmation

**Compared document roles:** REPORT main Table 2 title, headers, time rows and footnotes versus REPORT main Statistical Analysis; REPORT p. 6–7 narrative is context.

**Relationship type:** S_W

**All relationships:** S_W

**Review domain:** statistical_results

**Classification rationale:** The method/output comparison is within the single main REPORT. It concerns statistical-method identification, rather than conflicting assignment of an otherwise defined result to an outcome or time point. No PLAN statement or different REPORT document supplies a conflicting comparator, so no P_R, P_P or S_C relationship arises. Precedence has only S_W to apply. Classification matches registration; no change is needed.

**Classification ambiguity:** The outputs may intentionally be distinct targets, but their mapping is not supplied. This concerns the scientific description, not the content-based REPORT role or relationship code.

## C002 — Planned and reported age-subgroup specification

**Evidence state:** reproduced

**Determining recheck fact:** The SAP expressly prints age <65 years and >65 years within a priori primary-endpoint subgroups. The main report identifies prespecified age subgroup results and prints <50, 50–69 and ≥70 in Figure 3. All registered effects, counts, locations and the contextual SAP-referencing statement match the source. The reported middle category crosses the planned boundary, so the membership partitions remain distinct after precision checks and irrespective of assigning age exactly 65. No transcribed value or registered PDF page required alteration.

**Finding provenance:** Included F-XS-001 and duplicate statistical-pass-1 provenance F-ST1-002 describe this one specification issue. F-ST1-002 retains its SCREENED_OUT/DUPLICATE_OF_INCLUDED screening decision and contributes the p. 2 contextual location; it does not add a distinct stable ID or relationship.

### Exact location, source and comparator checks

| Exact supplied-source location | Found | Role by content | Printed content matched and comparison role |
|---|---|---|---|
| [SAP PDF p. 7, section 7.5 primary endpoint analyses, lines 1229–1238](../../../joi170166supp2_prod.pdf#page=7) | Yes | PLAN | Prospective 30-day MACE model: mixed-effects logistic regression, random hospital effects and fixed four-month time effects. This adjacent content establishes the endpoint and prospective analysis role of the subgroup list. |
| [SAP PDF p. 7, section 7.5.2, lines 1243–1254, especially line 1251](../../../joi170166supp2_prod.pdf#page=7) | Yes | PLAN | Subgroup analyses are a priori and will evaluate heterogeneity of effect; participant age groups are <65 years and >65 years. Both inequality signs are visually confirmed exactly as printed. This is the conflicting planned specification. |
| [Main PDF p. 3, Statistical Analysis subgroup sentence](../../../jama_huffman_2018_oi_170166.pdf#page=3), printed p. 569 | Yes | REPORT | Reports results by prespecified subgroups of participant age, sex, STEMI/NSTEMI, hospital size and hospital type, with interaction effects tested. The sentence names age but does not state numerical age boundaries. It supplies the reported prespecification claim, not an independent 50/70 boundary statement. |
| [Main PDF p. 9, Figure 3 title and age <50 row](../../../jama_huffman_2018_oi_170166.pdf#page=9), printed p. 575 | Yes | REPORT | Title identifies 30-day MACE by prespecified subgroups after hospital/time adjustment. Age <50: intervention 58/2079 (2.8%), control 68/2045 (3.3%); adjusted difference 1.42% (−0.71 to 3.54), OR 1.53 (0.83 to 2.79). All source values match registration. |
| [Main PDF p. 9, Figure 3 age 50–69 row](../../../jama_huffman_2018_oi_170166.pdf#page=9) | Yes | REPORT | Intervention 297/6606 (4.5%), control 326/5863 (5.6%); adjusted difference −0.57% (−2.02 to 0.88), OR 0.89 (0.67 to 1.19). Source alignment and printed category match registration. |
| [Main PDF p. 9, Figure 3 age ≥70 row](../../../jama_huffman_2018_oi_170166.pdf#page=9) | Yes | REPORT | Intervention 247/2623 (9.4%), control 251/2158 (11.6%); adjusted difference −0.23% (−3.32 to 2.85), OR 0.98 (0.71 to 1.35). Source alignment and ≥ sign match registration. |
| [Main PDF p. 9, paragraph beginning with Figure 3 below the figure](../../../jama_huffman_2018_oi_170166.pdf#page=9) | Yes | REPORT | Repeats that Figure 3 shows the intervention effect on 30-day MACE by prespecified subgroups, including age. It states a similar effect pattern across subgroups. This consistent repetition does not add an S_W conflict. |
| [Main PDF p. 2, Study Design paragraph continued in the upper right column](../../../jama_huffman_2018_oi_170166.pdf#page=2), printed p. 568 | Yes | REPORT | States study conduct according to protocol in Supplement 1 and analysis according to the statistical analysis plan in Supplement 2. This is the F-ST1-002 additional contextual location. It identifies the supplied plan but does not disclose revised age boundaries or independently conflict with another report statement. |
| [Main PDF p. 7, Table 3 30-day MACE row and column arm totals](../../../jama_huffman_2018_oi_170166.pdf#page=7), printed p. 573 | Yes | REPORT | Contextual aggregate match: intervention n=11308, events 602; control n=10066, events 645. These are comparators for the age-row accounting check, not a separate reporting inconsistency. |

The age split appears in prospective SAP subsection 7.5.2, so that location is PLAN by content. The main trial methods, figure and narrative report completed analyses/results, so they are REPORT by content. The source values/text and all comparator statements match for the full union of F-XS-001 and F-ST1-002 locations.

### Applicable rule and reproduced comparison

**Consistency rule applicable:** Yes, focus D, planned-versus-reported statistical analysis of the primary endpoint. Match age-subgroup specifications by participant membership boundaries for the same 30-day MACE endpoint and intervention/control contrast. The issue is not a preferred age cutoff, a peripheral per-time-point count comparison, or an unreported analysis inferred solely from absence.

**Logical comparison reproduced:** Yes. The planned boundary is 65; the displayed categories separate at 50 and 70. Ages 60 and 68 would both fall in the report's 50–69 category but fall on opposite sides of the planned split at 65. Consequently, merging whole reported categories cannot reproduce the planned partition, and splitting the middle category requires inputs absent from the displayed rows. The SAP's omission of age exactly 65 from its literal inequalities is not the basis of this comparison. Changing that single boundary convention does not align a 50/70 specification with a 65 specification. The compared report statements affirm prespecification but do not name a revised plan version or explain the mapping.

**Calculation and display-precision interval check:** Counts are exact integers: intervention denominators 2079+6606+2623=11308 and events 58+297+247=602; control denominators 2045+5863+2158=10066 and events 68+326+251=645. These sums match Table 3's aggregate arm counts/events. Thus the age rows account for the same primary MACE population; no count inconsistency is asserted.

| Reported age group | Intervention fraction → computed percent | Printed-percent half-unit interval | Control fraction → computed percent | Printed-percent half-unit interval |
|---|---|---|---|---|
| <50 | 58/2079 → 2.789803% | 2.8% → [2.75, 2.85]% | 68/2045 → 3.325183% | 3.3% → [3.25, 3.35]% |
| 50–69 | 297/6606 → 4.495913% | 4.5% → [4.45, 4.55]% | 326/5863 → 5.560293% | 5.6% → [5.55, 5.65]% |
| ≥70 | 247/2623 → 9.416698% | 9.4% → [9.35, 9.45]% | 251/2158 → 11.631140% | 11.6% → [11.55, 11.65]% |

All six percentages reconcile. Every adjusted OR/difference estimate and endpoint in the three rows has two decimals, with half-unit interval ±0.005. Each estimate remains within its own ordered CI. All three adjusted-difference CIs span zero and all three OR CIs span one throughout endpoint bounds; no inferential conflict is asserted within an age row. No crude-effect equality is imposed on these adjusted estimates.

Age labels are categorical analysis definitions, not rounded estimates. Even a deliberately permissive hypothetical ±0.5-year display allowance gives 65 boundary [64.5,65.5], 50 boundary [49.5,50.5], and 70 boundary [69.5,70.5], which are disjoint and leave ages 60 and 68 on opposite sides of the planned split but in the same reported middle category. Thus numeric precision cannot reconcile the specification. Counts and displayed adjusted effects do not identify the allocation of the middle row around age 65 or permit reconstruction of its separate model-based effects by averaging.

**Necessary inputs available:** Yes for reproducing the planned and reported category comparison, identifying the primary endpoint and reported adjustment, confirming all six effect/interval outputs and count accounting, and applying precision bounds. No for establishing the finalized prospective age specification or deriving the unreported 65-split effects.

**Exact missing inputs or definitions:** A supplied later plan/amendment or other dated prospective specification that defines the report's <50/50–69/≥70 categories; an explicit statement linking those categories to section 7.5.2; whether the SAP's 65-split analysis was additionally performed, replaced or reported elsewhere; and assignment of participants exactly age 65 in that prospective split. Raw age/outcome data, model covariance and subgroup-model output would be needed to reconstruct adjusted effects at 65; the three displayed effects alone cannot do so. The lack of a supplied amendment does not establish that none existed.

**Source-grounded alternative interpretation:** The SAP could have been superseded by a later prospective age specification not supplied. Figure 3 could display an additional three-category age analysis, while the planned two-category analysis was performed separately. The report's prespecified age wording could refer to age as an effect-modification family rather than the exact displayed cutoffs. These possibilities preserve the source facts but require the absent link between the two specifications; none is established by the compared locations.

**Direct observation versus inferred explanation:** Directly observed: different categorical boundaries, the SAP's a priori wording, repeated report prespecification wording, all printed age effects and counts, and an aggregate population match. Inferred possibilities only: a later amendment, additional or replaced analyses, or the timing/reason for adopting a specification. The source comparison does not establish when or why the categories were selected.

**Affected result or extracted value:** Figure 3's three adjusted 30-day MACE age-specific differences and ORs, and whether those displayed results represent the supplied prospective age-subgroup specification. A planned <65/>65 effect cannot be identified with an entire displayed row or recovered from its adjusted effects. No change in the overall primary result is inferred.

**Exact remaining human question:** Which dated prospective specification or disclosed amendment defines the Figure 3 age categories <50, 50–69 and ≥70, and how do these displayed MACE analyses relate to the SAP's planned <65/>65 analysis, including whether the latter was also performed or replaced?

### Classification confirmation

**Compared document roles:** PLAN SAP section 7.5.2 versus REPORT main Statistical Analysis, Figure 3 age rows/title and subgroup narrative. REPORT main p. 2 plan reference and p. 7 aggregate MACE totals are context.

**Relationship type:** P_R

**All relationships:** P_R

**Review domain:** protocol_report

**Classification rationale:** A prospective primary-endpoint age-subgroup analysis in PLAN differs from the displayed age specification described as prespecified in REPORT. P_R therefore applies and requires protocol_report. Report repetitions agree with each other and do not create S_W; contextual aggregate counts agree and do not add a relationship. No two conflicting PLAN locations were identified in the registered comparison, so P_P does not apply. No different REPORT document is a conflicting comparator, so S_C does not apply. P_R is the sole relationship and consequently has precedence. Classification matches registration; no change is needed.

**Classification ambiguity:** A later prospective specification may be outside the supplied package. This limits attribution of the change, but not the content-based PLAN/REPORT assignment or the observed comparison of supplied specifications. P_R does not itself imply a protocol violation.

## Inspection provenance and bounded limitations

Visual authority inspected: source-hash-matched reusable `review_1_5_2/preprocessing/rendered_pages/DOC-001-06.png`, `DOC-001-07.png` and `DOC-001-09.png`; current `review_1_6_1/preprocessing/screen-initial-main2.png`, `screen-initial-main3.png` and `xs-sap7.png`. The reusable page images' engine is historical direct `pdftoppm`, 180 dpi, recorded in the asset inventory; historical engine version is not asserted. Current renders are direct CPU `pdftoppm` 25.03.0 at 120 dpi from their exact named source pages. Current source text/alignment confirmation used direct Poppler `pdftotext -layout` 25.03.0 to standard output for main physical pp. 2–3, 6–7 and 9, and SAP physical p. 7. No new extraction, OCR or image derivative was needed or created by this rechecker. No GPU, web evidence or Python scientific review was used. Supplied sources and reused artifacts were preserved.

All evidence links above are relative to this verification artifact and end in truthful physical-PDF `#page=N` locations. There are no Office or structured-source locations in the assigned scope. Two IDs were rechecked; two evidence states are reproduced, zero are reproduced_after_transcription_correction and zero are not_reproduced. Classification counts: one statistical_results/S_W and one protocol_report/P_R. The unresolved items are the C001 time-output target mapping and C002 prospective age-specification link, not missing source inspection.
