# Workflow 1.6.2 Candidate Ledger

Pending Human Adjudication. Twelve issues were registered only after the independent screen of all 22 findings. No stable ID may be removed or suppressed. Evidence states and inclusion audits are provisional until their independent stages finish.

IDs follow the first affirmative conflicting source statement: DOC-001 physical-page order, named section/display order within a page, then PLAN-only DOC-002 and the SAP-only specified-output absence. Merely affected-result mentions and corroborating locations do not move an issue earlier. On article p. 5, the fallback rule precedes the subgroup-nonreporting statement; on p. 6, Table 2 precedes the primary-outcome text.

## Classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main article SCDE interval vs REPORT main article P value (pp. 1, 6, 7) | reproduced | CONFIRMED | F-NUM-001 |
| C002 | protocol_report | P_R | P_R | PLAN protocol pp. 12, 14, 16 vs REPORT main article pp. 3, 4, 6 | reproduced | CONFIRMED | F-XS-007 |
| C003 | protocol_report | P_R | P_R, S_C | PLAN protocol pp. 10, 11, 24 vs REPORT main article p. 4 and REPORT results supplement p. 6 | reproduced | CONFIRMED | F-XS-001 |
| C004 | protocol_report | P_R | P_R, S_W | PLAN protocol pp. 11, 12, 16 and PLAN SAP p. 5 vs REPORT main article pp. 4, 7 | reproduced | CONFIRMED | F-XS-002 |
| C005 | protocol_report | P_R | P_R, P_P | PLAN protocol p. 16 vs PLAN SAP pp. 1-4 and REPORT main article pp. 4, 5, 7 | reproduced | CONFIRMED | F-XS-005 |
| C006 | protocol_report | P_R | P_R | PLAN protocol p. 16 and PLAN SAP pp. 2, 3 vs REPORT main article pp. 5, 7 | reproduced | CONFIRMED | F-XS-006 |
| C007 | protocol_report | P_R | P_R | PLAN protocol p. 16 and PLAN SAP p. 6 vs REPORT main article p. 5 and complete REPORT result set | reproduced | CONFIRMED | F-XS-003 |
| C008 | statistical_results | S_W | S_W | REPORT main article p. 6 respiratory-rate interval vs REPORT main article p. 6 Holm-adjusted P value; significance rule p. 5 | reproduced | CONFIRMED | F-ST1-002 |
| C009 | protocol_report | P_R | P_R | PLAN protocol pp. 10, 16 vs REPORT main article pp. 6, 7, 9 and complete REPORT result set | reproduced | CONFIRMED | F-ST1-011 |
| C010 | protocol_report | P_R | P_R, P_P | PLAN protocol p. 12 vs PLAN SAP p. 5 and REPORT main article p. 7 | reproduced | CONFIRMED | F-XS-009 |
| C011 | plan_material | P_P | P_P | PLAN protocol p. 14 mortality power input vs PLAN protocol p. 29 power appendix | reproduced | CONFIRMED | F-NUM-101 |
| C012 | protocol_report | P_R | P_R | PLAN SAP pp. 4, 5 vs REPORT main article pp. 4-7 and complete REPORT results supplement | reproduced | CONFIRMED | F-XS-004 |

## Registration and evidence records

## C001 — SCDE absolute-effect interval and displayed P value give different null readings

**Candidate statement:** SCDE absolute-effect interval and displayed P value give different null readings.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article SCDE interval vs REPORT main article P value (pp. 1, 6, 7)

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Classification rationale:** Both conflicting interval and test are within the same report document; supplemental counts only corroborate the outcome.

**Classification ambiguity:** None

- **Included Finding IDs:** F-NUM-001.
- **Duplicate Finding IDs:** F-ST1-001.
- **Checker provenance:** numeric_consistency_reviewer and statistics_pass_1; relationships N053/N065/N074 and S011.
- **Source-order key:** DOC-001 / p.1 / abstract Results / SCDE absolute effect.
- **Conflicting locations and roles:** REPORT [main p.1 abstract Results](../../jama_parshuram_2018_oi_180015.pdf#page=1), REPORT [main p.6 Secondary Outcome](../../jama_parshuram_2018_oi_180015.pdf#page=6), REPORT [main p.7 Table 3 SCDE row and footnotes a/f](../../jama_parshuram_2018_oi_180015.pdf#page=7); REPORT [main p.5 two-sided significance rule](../../jama_parshuram_2018_oi_180015.pdf#page=5) supplies the comparison level.
- **Printed source and comparator:** RD −0.34 per 1000 patient-days, 95% CI −0.73 to 0.05; RR 0.77, 95% CI 0.61 to 0.97; P=.03; significance .05. The ratio is baseline adjusted, while footnote a explicitly excludes baseline adjustment for the SCDE absolute difference.
- **Rule/calculation:** −0.73 < 0 < 0.05, so the absolute interval includes its null, but .03 < .05; 0.61 < 0.77 < 0.97 < 1 makes the ratio interval agree with P=.03. Endpoint half-unit bounds [−0.735,−0.725] and [0.045,0.055], and P bounds [.025,.035], cannot change these null readings. The display-relative threshold does not apply to this category-1 comparison.
- **Qualifying route:** Route A, category 1; focus B.
- **Proposed classification:** statistical_results; primary relationship S_W; all relationships S_W; no role ambiguity. Supplementary event counts may corroborate the named outcome but are not a conflicting relationship.
- **Affected extracted result:** Significance/test attribution for the key-secondary absolute effect −0.34 (−0.73 to 0.05), particularly its pairing with P=.03 in the abstract.
- **Context and alternatives:** P=.03 may belong solely to the baseline-adjusted RR, while the RD uses another model. This is strongly supported by the source footnotes and ratio interval and must accompany the card, but category 1 explicitly retains comparisons attributed to different analyses. No separate RD P value is displayed.
- **Bounded human question:** Which test applies to the absolute SCDE difference, and should P=.03 be extracted only with the relative effect?

## C002 — Planned all-seven documentation analysis is replaced by last-set ≥5 completeness

**Candidate statement:** Planned all-seven documentation analysis is replaced by last-set ≥5 completeness.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol pp. 12, 14, 16 vs REPORT main article pp. 3, 4, 6

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-007

**Classification rationale:** The prospective documentation definition differs from the reported constructed endpoint; supplement measurement is corroboration.

**Classification ambiguity:** The report discloses revision before analysis; no dated amendment is supplied.

- **Included Finding IDs:** F-XS-007.
- **Duplicate Finding IDs:** F-ST1-009.
- **Checker provenance:** cross_source_consistency_reviewer and statistics_pass_1; relationships S030/S053.
- **Source-order key:** DOC-001 / p.3 / final paragraph announcing revision, continued on p.4.
- **Conflicting locations and roles:** PLAN [protocol p.12 documentation process outcome](../../joi180015supp1_prod.pdf#page=12), PLAN [protocol p.14 preceding-24-hour documentation measurement](../../joi180015supp1_prod.pdf#page=14), PLAN [protocol p.16 all-seven-item analysis](../../joi180015supp1_prod.pdf#page=16); REPORT [main p.3 documentation revision introduction](../../jama_parshuram_2018_oi_180015.pdf#page=3), REPORT [main p.4 revision details](../../jama_parshuram_2018_oi_180015.pdf#page=4), REPORT [main p.6 Table 2 completeness row and footnotes](../../jama_parshuram_2018_oi_180015.pdf#page=6).
- **Corroboration:** REPORT [results p.4 eFigure 2](../../joi180015supp3_prod.pdf#page=4) and REPORT [results p.5 caption](../../joi180015supp3_prod.pdf#page=5) confirm last-set measurement; they do not add S_C.
- **Printed source and comparator:** Plan compares number of times all seven score items were documented in sampled patients. Main explicitly says, before analyses, all observation sets were replaced by the last one, and the threshold was reduced from7 to5 for consistency with minimum score calculation requirements. Table2 reports ≥5 vital-sign last sets and adjusted difference38.1 percentage points (20.8–55.4), P<.001.
- **Rule/calculation:** A last set with five or six items qualifies for the reported completeness indicator but not the planned all-seven definition; an all-set count and last-set indicator also differ in measurement/analysis unit. These categorical membership changes are not rounding. Individual vital-sign-frequency outputs remain reported and are not alleged to be absent.
- **Qualifying route:** Route A, category 5; focus D; changed prespecified constructed endpoint/analysis definition.
- **Proposed classification:** protocol_report; primary P_R; all relationships P_R; no role ambiguity.
- **Affected extracted result:** Meaning of the documentation-completeness 38.1 percentage-point effect and whether it represents all-seven frequency or last-set ≥5 completeness.
- **Context and alternatives:** The timing before analysis and clinical rationale are explicitly disclosed; a formal amendment may exist elsewhere. Disclosure identifies the replacement but does not make the two endpoints identical or remove category5.
- **Bounded human question:** What prospective amendment establishes last-set ≥5 completeness, and is the planned all-seven/all-set comparison available?

## C003 — SCDE composite components differ between protocol and report, with a report fluid-boundary difference

**Candidate statement:** SCDE composite components differ between protocol and report, with a report fluid-boundary difference.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C

**Compared document roles:** PLAN protocol pp. 10, 11, 24 vs REPORT main article p. 4 and REPORT results supplement p. 6

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Classification rationale:** Plan/report composite changes establish P_R; the fluid boundary between two report documents adds S_C. P_R takes precedence.

**Classification ambiguity:** No dated amendment or event-level membership data is supplied.

- **Included Finding IDs:** F-XS-001.
- **Duplicate Finding IDs:** F-ST1-007.
- **Checker provenance:** cross_source_consistency_reviewer and statistics_pass_1; relationships S031/S068.
- **Source-order key:** DOC-001 / p.4 / Study Outcomes / main-secondary definition.
- **Conflicting locations and roles:** PLAN [protocol p.24 Table 5 categories 4 and7](../../joi180015supp1_prod.pdf#page=24); PLAN [protocol pp.10–11 main-secondary definition](../../joi180015supp1_prod.pdf#page=10); REPORT [main p.4 SCDE definition](../../jama_parshuram_2018_oi_180015.pdf#page=4); REPORT [results p.6 eTable 1 SCDE definition](../../joi180015supp3_prod.pdf#page=6).
- **Affected-result occurrences, not extra conflicting relationships:** REPORT [main p.1 abstract](../../jama_parshuram_2018_oi_180015.pdf#page=1), REPORT [main p.7 Table 3](../../jama_parshuram_2018_oi_180015.pdf#page=7), REPORT [results p.11 eTable 3](../../joi180015supp3_prod.pdf#page=11).
- **Printed source and comparator:** Plan circulatory category requires >60 mL/kg fluid in 12 h AND any inotrope/vasopressor; main allows vasoactive medication OR fluid boluses ≥60 mL/kg; eTable 1 says >60 mL/kg AND/OR vasoactive therapy. Plan death category specifies ward death and no transfer; report definitions also include death within the first hour of urgent ICU admission. Plan p.10 general therapy window does not change Table 5's explicit ward-only death row.
- **Rule/calculation:** Fluid-only or vasoactive-only membership satisfies the reported OR but fails planned AND; post-ICU death falls inside reported death membership but outside planned category7. Exactly60 is admitted by the main ≥60 wording but excluded by the supplement >60 wording. This is logical composite membership, not a recomputed printed value; no numeric relative discrepancy is applicable and no number of boundary cases is inferred.
- **Qualifying route:** Route A, category 5; focus D.
- **Proposed classification:** protocol_report; primary P_R; all relationships P_R, S_C; P_R has precedence. The PLAN–REPORT component changes establish P_R; the two REPORT fluid boundaries establish S_C.
- **Affected extracted result:** The 386-event SCDE numerator (127 versus259), its rates, RR0.77 (0.61–0.97), RD−0.34 (−0.73–0.05), and which composite those values represent.
- **Context and alternatives:** An earlier protocol definition may have been amended; the main cutoff may summarize the eTable, and a death after ICU admission may also satisfy a therapy/CPR component. Such overlap does not make the printed membership rules identical. Aggregate results cannot establish which operational rule was used or how many cases are affected.
- **Bounded human question:** Which circulatory combination, fluid boundary and death-location window generated the analyzed SCDE events, and where is the corresponding prespecified or amended definition?

## C004 — Planned secondary outcome/analysis status differs from reported post-hoc or nonprespecified status

**Candidate statement:** Planned secondary outcome/analysis status differs from reported post-hoc or nonprespecified status.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_W

**Compared document roles:** PLAN protocol pp. 11, 12, 16 and PLAN SAP p. 5 vs REPORT main article pp. 4, 7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

**Classification rationale:** Plan/report status comparisons establish P_R, and main prespecified versus post-hoc lists add S_W. P_R takes precedence; differing ICU populations and primary-family sensitivities are bounded separately.

**Classification ambiguity:** The SAP is undated; post hoc may refer to analysis models or multiplicity treatment rather than outcome collection.

- **Included Finding IDs:** F-XS-002.
- **Duplicate Finding IDs:** F-ST1-004.
- **Checker provenance:** cross_source_consistency_reviewer and statistics_pass_1; relationships S012/S013/S015/S016/S017/S018/S020/S021/S031/S035.
- **Source-order key:** DOC-001 / p.4 / Study Outcomes / prespecified and nonprespecified lists.
- **Conflicting locations and roles:** PLAN [protocol p.11 preventable cardiac arrest](../../joi180015supp1_prod.pdf#page=11), PLAN [protocol p.12 readmissions and calls/consultations](../../joi180015supp1_prod.pdf#page=12), PLAN [protocol p.16 PIM2-score model](../../joi180015supp1_prod.pdf#page=16); REPORT [main p.4 outcome-status lists](../../jama_parshuram_2018_oi_180015.pdf#page=4); REPORT [main p.7 Table 3 Post hoc Outcomes and footnote g](../../jama_parshuram_2018_oi_180015.pdf#page=7). PLAN [SAP p.5 urgent-ICU-admission shell row](../../joi180015supp2_prod.pdf#page=5) is a further timing-ambiguous occurrence.
- **Result corroboration:** REPORT [results p.12 eTable 4 PIM2-score row](../../joi180015supp3_prod.pdf#page=12) prints 0.13 (−0.11 to0.37), P=.29; it confirms the analyzed score but makes no conflicting status claim, so it does not add S_C.
- **Printed source and comparator:** Protocol secondary preventable cardiac arrest, hospital/ICU readmissions, immediate physician and resuscitation-team calls, and urgent ICU consultations appear under the main Table 3 Post hoc Outcomes heading. Main p.4 independently calls preventable arrest and both readmissions prespecified. Protocol p.16 explicitly plans the PIM2 score mean analysis, whereas main p.4 calls PIM2 score not prespecified. SAP p.5 includes urgent ICU admissions, which main p.4 also calls not prespecified.
- **Rule/calculation:** Exact named outcome/analysis matches establish a prospective-plan versus reported-status contrast; numeric precision does not apply. Outcome measurement and analysis timing may differ, but Table 3's heading does not specify which element is post hoc.
- **Qualifying route:** Route A, category 5; focus D.
- **Proposed classification:** protocol_report; primary P_R; all relationships P_R, S_W. P_R arises from protocol/SAP versus main; S_W arises from main p.4 prespecified versus Table 3 post-hoc designation. No P_P contrast is alleged merely because an undated SAP adds a shell row.
- **Independently bounded occurrences:** Main p.4 labels overall ICU mortality prespecified, while Table 3's two overall-ICU-mortality scales are post hoc: this is retained as a main-internal S_W occurrence, without equating that population to protocol urgent-admission mortality. Protocol urgent-ICU mortality and eTable 4 urgent-ICU mortality agree in population and are not an independent post-hoc conflict. Non-DNR mortality appearing beneath Table 3 Primary Outcome is compatible with the primary-family sensitivity context and is excluded as CONTEXT_RESOLVES within the pattern, rather than claimed as a primary-status elevation. Overall cardiac-arrest rate has no matched explicit protocol outcome-status claim and is not included as a conflict. Urgent-ICU-admission SAP/report contrast is retained with uncertainty about when the undated SAP specified that analysis, not asserted to prove original-protocol prespecification. Footnote g's exploratory designation supplies interpretation context; exploratory alone is not a separate timing discrepancy.
- **Affected extracted result:** Prespecification and inferential status of named Table 3 effects and the PIM2-score comparison, including whether an extractor should treat them as planned or added analyses.
- **Context and alternatives:** Post hoc may describe models or multiplicity treatment rather than outcome collection; the SAP may record subsequent analyses. These explanations require defining the status element and timing. PIM2 score and predicted mortality are distinct, but the protocol explicitly names the score itself.
- **Bounded human question:** For each matched result, does post hoc/nonprespecified refer to the outcome, analysis model or multiplicity treatment, and what dated specification establishes PIM2-score and urgent-admission analysis status?

## C005 — Protocol weighted hospital-logit primary analysis differs from SAP/reported GEE specification

**Candidate statement:** Protocol weighted hospital-logit primary analysis differs from SAP/reported GEE specification.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN protocol p. 16 vs PLAN SAP pp. 1-4 and REPORT main article pp. 4, 5, 7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005

**Classification rationale:** The protocol differs from both report and SAP model specifications, establishing P_R and P_P; P_R takes precedence. SAP/report agreement corroborates the implemented side.

**Classification ambiguity:** The SAP is undated; equivalence of implicit weights and a prospective amendment cannot be established.

- **Included Finding IDs:** F-XS-005.
- **Duplicate Finding IDs:** F-ST1-008.
- **Checker provenance:** cross_source_consistency_reviewer and statistics_pass_1; relationships S026/S029/S049/S051/S052.
- **Source-order key:** DOC-001 / p.4 / Data Analyses / GEE specification, with p.5 predictor/stratum details.
- **Conflicting locations and roles:** PLAN [protocol p.16 primary and secondary analysis paragraphs](../../joi180015supp1_prod.pdf#page=16); PLAN [SAP p.1 binomial model/predictors](../../joi180015supp2_prod.pdf#page=1), PLAN [SAP p.2 cbind event/non-event GEE](../../joi180015supp2_prod.pdf#page=2), PLAN [SAP pp.3–4 count and individual-continuous GEE specifications](../../joi180015supp2_prod.pdf#page=3); REPORT [main p.4 GEE methods](../../jama_parshuram_2018_oi_180015.pdf#page=4), REPORT [main p.5 two predictors, individual ICU analyses and removal of strata](../../jama_parshuram_2018_oi_180015.pdf#page=5); REPORT [main p.7 Table 3 primary outputs](../../jama_parshuram_2018_oi_180015.pdf#page=7).
- **Printed source and comparator:** Protocol primary dependent variable is logit of hospital mortality proportion, with treatment, baseline logit and hospital-size stratum, weighted by hospital size. SAP/report use binomial GEE with exchangeable hospital clustering; SAP code models cbind(x,n−x) using intervention+baseline logit, and main specifies two predictors. Main discloses removal of stratification because only three hospitals had >200 eligible beds. Protocol secondary logit/Poisson/within-hospital-mean models also include size stratum; continuous analyses use hospital-size weights, whereas SAP/report describe individual-level continuous GEE for relevant ICU outcomes.
- **Rule/calculation:** The printed response/likelihood descriptions and predictor sets differ; no original weighted hospital-logit/size-stratified primary output is supplied. The common removal of the planned size stratum and associated hospital-level versus individual/GEE descriptions form one specification-change pattern. Do not infer whether GEE implicitly creates numerically equivalent weights, whether fitted effects would change, or an unstated model implementation. The SCDE RD's separate omission of baseline adjustment is C006, not duplicated here.
- **Qualifying route:** Route A, category 5; focus D; planned primary analysis is replaced/not reported.
- **Proposed classification:** protocol_report; primary P_R; all relationships P_R, P_P. Protocol versus report establishes P_R and protocol versus SAP establishes P_P; P_R takes precedence. SAP/report agreement is corroboration for the implemented side and is not another relationship.
- **Affected extracted result:** Governing specification for primary mortality OR1.01 (0.61–1.69), P=.96, RD0.01 (−0.80–0.81), with linked planned secondary model/stratum specifications retained as pattern locations.
- **Context and alternatives:** The SAP may be an approved later revision; GEE may be considered a related implementation of broad logit regression. Stratification removal is disclosed. None establishes the original specification's output or dated amendment, and no preferred model is proposed.
- **Bounded human question:** What dated analysis specification governs the primary result, and how were the planned hospital-logit response, hospital weights and size stratum changed or implemented in the reported GEE?

## C006 — Key-secondary SCDE absolute-effect analysis omits SAP baseline adjustment

**Candidate statement:** Key-secondary SCDE absolute-effect analysis omits SAP baseline adjustment.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol p. 16 and PLAN SAP pp. 2, 3 vs REPORT main article pp. 5, 7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-006

**Classification rationale:** The planned baseline-adjusted key-secondary absolute-effect model differs from the reported fallback covariate specification.

**Classification ambiguity:** The report discloses a nonconvergence fallback, but a dated prospective fallback specification is not supplied.

- **Included Finding IDs:** F-XS-006.
- **Duplicate Finding IDs:** None.
- **Checker provenance:** cross_source_consistency_reviewer; linked statistical relationship S011/S052 and count identity specification.
- **Source-order key:** DOC-001 / p.5 / nonconvergence fallback rule; row-specific implementation p.7 footnote a.
- **Conflicting locations and roles:** PLAN [SAP p.2 count identity model introduction](../../joi180015supp2_prod.pdf#page=2), PLAN [SAP p.3 baseline predictor/identity-link fit](../../joi180015supp2_prod.pdf#page=3); REPORT [main p.5 identity-model fallback](../../jama_parshuram_2018_oi_180015.pdf#page=5), REPORT [main p.7 Table 3 SCDE row and footnote a](../../jama_parshuram_2018_oi_180015.pdf#page=7). PLAN [protocol p.16 SCDE Poisson baseline-event specification](../../joi180015supp1_prod.pdf#page=16) supports the general planned baseline adjustment.
- **Affected-result occurrence:** REPORT [main p.1 abstract RD](../../jama_parshuram_2018_oi_180015.pdf#page=1) is an output occurrence, not a separate conflict.
- **Printed source and comparator:** SAP count-rate identity model includes intervention and baseline rate. Main allows removal of baseline adjustment if identity GEE does not converge, and footnote a explicitly names SCDE among rate-difference models not baseline adjusted. The output is −0.34 (−0.73 to0.05); ratio0.77 remains baseline adjusted.
- **Rule/calculation:** Baseline-adjusted planned absolute-effect fit and reported non-baseline-adjusted absolute-effect fit have different covariate specifications; the ratio does not supply the planned absolute effect. No fallback provision was found in the complete seven-page SAP. This is categorical design comparison, with no numeric gap calculation or fabricated adjusted RD.
- **Qualifying route:** Route A, category 5; focus D.
- **Proposed classification:** protocol_report; primary P_R; all relationships P_R. Exploratory non-baseline-adjusted Table 3 rows corroborate the fallback pattern but are not additional planned key-secondary omission claims. No S_W is inferred merely from the word adjusted in the abstract because hospital clustering remains accounted for.
- **Affected extracted result:** Analysis specification and interpretation of the main-secondary absolute effect and CI extracted from the abstract/Table 3.
- **Context and alternatives:** The source gives nonconvergence as the general fallback reason, but no SCDE-specific convergence record or prospective fallback amendment is supplied. This disclosed explanation does not remove category5. This group is distinct from C001's interval/P attribution and C005's original primary model/stratum replacement.
- **Bounded human question:** Was baseline-removal fallback prospectively specified for the SCDE RD, and which SCDE fit/convergence facts explain replacement of the SAP baseline-adjusted absolute-effect model?

## C007 — Planned subgroup analyses of primary/key-secondary effects are not supplied

**Candidate statement:** Planned subgroup analyses of primary/key-secondary effects are not supplied.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol p. 16 and PLAN SAP p. 6 vs REPORT main article p. 5 and complete REPORT result set

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003

**Classification rationale:** Named planned subgroup analyses applicable to primary/key-secondary effects are not supplied in the report materials; the narrower SAP list does not establish P_P by itself.

**Classification ambiguity:** The SAP is undated; the exact outcome assignment of every subgroup should not be inferred.

- **Included Finding IDs:** F-XS-003.
- **Duplicate Finding IDs:** F-ST1-005.
- **Checker provenance:** cross_source_consistency_reviewer and statistics_pass_1; relationship S029.
- **Source-order key:** DOC-001 / p.5 / Data Analyses / four subgroup analyses not reported.
- **Conflicting locations and roles:** PLAN [protocol p.16 A-priori Subgroup analyses](../../joi180015supp1_prod.pdf#page=16), PLAN [SAP p.6 Subgroup Analysis Plan](../../joi180015supp2_prod.pdf#page=6), REPORT [main p.5 nonreporting statement](../../jama_parshuram_2018_oi_180015.pdf#page=5). REPORT complete main pp.1–11 and [results pp.1–14](../../joi180015supp3_prod.pdf#page=1) provide no subgroup estimate/interaction result.
- **Printed source and comparator:** Protocol says four subgroups will be performed: <200/≥200 eligible ward beds, with/without MET, with/without ECMO, and ward-initiated urgent PICU admission. SAP plans treatment effects in ECMO/MET groups and one-term GEE treatment-by-subgroup interactions. Main states four planned subgroup analyses, including rapid-response-team presence, are not reported herein.
- **Rule/calculation:** Named planned analyses applicable to primary/key-secondary treatment effects lack corresponding supplied result sets, and main expressly confirms nonreporting. No numeric reproduction is possible for absent estimates; the conflict is specified analysis versus output, not a missing model-detail conjecture.
- **Qualifying route:** Route A, category 5; focus D. Planned primary/key-secondary subgroup analyses are outside the peripheral survey/process-omission catalogue.
- **Proposed classification:** protocol_report; primary P_R; all relationships P_R. The narrower SAP subgroup list is additional planned scope, not by itself a P_P contradiction.
- **Affected extracted result:** Effect modification/subgroup estimates and interaction tests for primary mortality and main-secondary SCDE, plus the protocol ward-origin urgent-admission subgroup specification.
- **Context and alternatives:** Outputs may have been reserved for another publication, or sparse clusters may have prompted a revision; removal of size stratification from adjustment does not supply the subgroup analyses. The source does not establish that all four subgroups use identical outcomes, so the card should not fabricate a four-by-all-outcomes result matrix.
- **Bounded human question:** Which planned primary/key-secondary subgroup effects and MET/ECMO interactions were performed, where are their outputs, and which prospective change explains any omission?

## C008 — Respiratory-rate interval excludes zero while Holm-adjusted P is nonsignificant

**Candidate statement:** Respiratory-rate interval excludes zero while Holm-adjusted P is nonsignificant.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article p. 6 respiratory-rate interval vs REPORT main article p. 6 Holm-adjusted P value; significance rule p. 5

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002

**Classification rationale:** The interval and adjusted P value appear within one report document; different multiplicity adjustment is a source-grounded alternative.

**Classification ambiguity:** None

- **Included Finding IDs:** F-ST1-002.
- **Duplicate Finding IDs:** None.
- **Checker provenance:** statistics_pass_1; relationships S002/S028.
- **Source-order key:** DOC-001 / p.6 / Table 2 respiratory-rate row.
- **Conflicting locations and roles:** REPORT [main p.6 Table 2 respiratory-rate row and footnotes c/d](../../jama_parshuram_2018_oi_180015.pdf#page=6); REPORT [main p.5 significance/multiplicity methods](../../jama_parshuram_2018_oi_180015.pdf#page=5).
- **Printed source and comparator:** Difference0.85, 95% CI0.02–1.68; raw P=.05; adjusted P=.18. Table footnote c identifies baseline/hospital-adjusted GEE and footnote d Holm multiplicity adjustment. Methods state two-sided P=.05 significant and Holm applied post hoc to21 prespecified outcomes.
- **Rule/calculation:** 0.02>0, so the95% interval excludes zero, but .18>.05. Half-unit lower-limit bounds [.015,.025] remain positive and adjusted-P bounds [.175,.185] remain nonsignificant; category1 does not permit a display-relative exclusion. A normal-Wald diagnostic SE≈.83/1.96=.4235 and z≈2.007 suggests raw P≈.045, consistent with raw P rounded to.05; this diagnostic is contextual and does not reconstruct the reported GEE test.
- **Qualifying route:** Route A, category1; focusB.
- **Proposed classification:** statistical_results; primary S_W; all relationships S_W; no role ambiguity.
- **Affected extracted result:** Respiratory-rate documentation effect and its multiplicity-adjusted statistical reading.
- **Context and alternatives:** The interval is likely an unadjusted marginal95% interval while .18 is family-adjusted. Labels distinguish these analyses; category1 explicitly retains that explanation. The raw P=.05 comparison is not asserted as an independent discrepancy, and no adjusted interval is supplied.
- **Bounded human question:** Is the displayed95% interval intended solely for the unadjusted inference, and which interval/test pairing should accompany Holm-adjusted P=.18 in extraction?

## C009 — Planned mortality-following-DNR sensitivity is not matched by displayed mortality-without-DNR output

**Candidate statement:** Planned mortality-following-DNR sensitivity is not matched by displayed mortality-without-DNR output.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol pp. 10, 16 vs REPORT main article pp. 6, 7, 9 and complete REPORT result set

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-011

**Classification rationale:** The named planned following-DNR primary-mortality sensitivity is compared with the supplied result set; descriptive supplemental counts corroborate output coverage without adding S_C.

**Classification ambiguity:** After-DNR sensitivity may describe a mortality subset or exclusion of such deaths; the exact model output remains unidentified.

- **Included Finding IDs:** F-ST1-011.
- **Duplicate Finding IDs:** None.
- **Checker provenance:** statistics_pass_1; relationships S010/S050.
- **Source-order key:** DOC-001 / p.6 / Primary Outcome / non-DNR modeled output, compared with planned following-DNR analysis.
- **Conflicting locations and roles:** PLAN [protocol p.16 secondary analysis d](../../joi180015supp1_prod.pdf#page=16); REPORT [main p.6 non-DNR result](../../jama_parshuram_2018_oi_180015.pdf#page=6), REPORT [main p.7 Table 3 mortality without DNR](../../jama_parshuram_2018_oi_180015.pdf#page=7), REPORT [main p.9 sixth limitation referring to sensitivity of mortality after DNR order](../../jama_parshuram_2018_oi_180015.pdf#page=9). PLAN [protocol p.10 with/without-DNR rationale](../../joi180015supp1_prod.pdf#page=10) supplies context.
- **Corroboration and absence scope:** REPORT [results p.9 eTable 2](../../joi180015supp3_prod.pdf#page=9) supplies hospital mortality and mortality without DNR, not a modeled following-DNR estimate. Full main/results inspection found no corresponding following-DNR model output; that table is additional output scope, not a conflicting S_C relationship.
- **Printed source and comparator:** Protocol says an identical primary logit model will analyze all-cause mortality following DNR orders. Main reports155/244 deaths after DNR but the named comparative result is mortality without DNR:42 versus47 deaths, OR2.05 (0.64–6.61), P=.23, RD0.36 (−0.53–1.25). Main limitation refers to a sensitivity analysis of mortality after DNR order.
- **Rule/calculation:** 244−(42+47)=155 reconciles the aggregate following-DNR count, and97−42=55 versus147−47=100 provides arm-specific descriptive complementary counts, but complements do not reproduce the planned baseline-adjusted following-DNR OR/interval/test. No crude OR is proposed as the missing planned fit. The omitted specified primary-mortality sensitivity output is a categorical planned-analysis comparison; display-relative arithmetic is inapplicable.
- **Qualifying route:** Route A, category5; focusD.
- **Proposed classification:** protocol_report; primary P_R; all relationships P_R. Main p.9 is evidence of the named analysis/context, not proof that OR2.05 was attributed to after-DNR mortality; therefore no additional S_W attribution contradiction is asserted.
- **Affected extracted result:** Availability/identity of the planned primary-mortality following-DNR sensitivity and whether OR2.05 can represent it (its displayed label says without DNR).
- **Context and alternatives:** After-DNR sensitivity may be shorthand for removing such deaths, or the planned fit may have been omitted. The protocol's with/without rationale supports broader sensitivity intent, but its explicit following-DNR model is not supplied. This is distinct from C004's unsupported status-elevation occurrence.
- **Bounded human question:** Which output corresponds to the planned mortality-following-DNR analysis, and does the stated after-DNR sensitivity instead mean the displayed without-DNR analysis?

## C010 — ICU-readmission rate denominator changes from planned hospital to reported ICU discharges

**Candidate statement:** ICU-readmission rate denominator changes from planned hospital to reported ICU discharges.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN protocol p. 12 vs PLAN SAP p. 5 and REPORT main article p. 7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-009

**Classification rationale:** The endpoint denominator differs between protocol and report and between protocol and SAP, establishing P_R and P_P; P_R takes precedence.

**Classification ambiguity:** The SAP is undated and may supersede a broad protocol denominator sentence.

- **Included Finding IDs:** F-XS-009.
- **Duplicate Finding IDs:** F-ST1-010.
- **Checker provenance:** cross_source_consistency_reviewer and statistics_pass_1; relationships S020/S069.
- **Source-order key:** DOC-001 / p.7 / Table 3 ICU readmission <48 h row and footnote h.
- **Conflicting locations and roles:** PLAN [protocol p.12 ICU readmission definition and denominator sentence](../../joi180015supp1_prod.pdf#page=12); PLAN [SAP p.5 ICU-readmission shell row](../../joi180015supp2_prod.pdf#page=5); REPORT [main p.7 ICU readmission row and footnote h](../../jama_parshuram_2018_oi_180015.pdf#page=7). REPORT [main p.5 Table 1 baseline ICU discharge counts](../../jama_parshuram_2018_oi_180015.pdf#page=5) supplies the baseline denominator witness.
- **Printed source and comparator:** Protocol says PICU mortality and unplanned hospital/PICU readmission are represented per1000 hospital discharges. SAP divides ICU readmission by PatientDischargesICU; main footnote h explicitly says per1000 ICU discharges. Baseline64(34.43) versus73(28.09); intervention94(28.40) versus108(21.25). Hospital intervention discharges are50173/94366; baseline ICU discharges1859/2599.
- **Rule/calculation:** Baseline64/1859×1000=34.42711135 and73/2599×1000=28.0877 match displayed ICU rates; planned hospital-denominator counterparts64/26664×1000=2.40024 and73/46718×1000=1.56257 differ in quantity. Intervention hospital-denominator counterparts94/50173×1000=1.87352 and108/94366×1000=1.14448 versus displayed28.40/21.25. Even half-unit count and denominator bounds give intervention hospital-rate intervals [1.86353354,1.88350192] and [1.13917545,1.14978461], separated from displayed rate intervals [28.395,28.405]/[21.245,21.255]; relative gaps using displayed rates are .93350345 and .94565719. No crude calculation is used to dispute adjusted OR1.11.
- **Qualifying route:** Route B; focus D. B1: planned endpoint/denominator definition is in focus. B2: the hospital versus ICU population change has no supplied timing/amendment reconciliation. B3: it changes the named extractable readmission rates and their unit. This is not a peripheral copy of a contributor count.
- **Proposed classification:** protocol_report; primary P_R; all relationships P_R, P_P. Protocol versus main establishes P_R; protocol versus SAP establishes P_P; P_R has precedence. Main/SAP agree on the implemented unit and do not add another conflicting relationship.
- **Affected extracted result:** ICU readmission rates28.40/21.25 and RD4.95 per1000 ICU discharges, compared with planned per1000 hospital discharges.
- **Context and alternatives:** The protocol denominator sentence may summarize families too broadly, or the SAP may supersede it. The actual reported unit is clear, but the prospective endpoint change remains a human question. Exact intervention ICU denominators are not printed; they are unnecessary to establish the competing definition and are not fabricated.
- **Bounded human question:** Was the ICU-readmission endpoint denominator prospectively revised from hospital discharges to ICU discharges, and which specification defines the intended endpoint for comparison/extraction?

## C011 — Protocol mortality power appendix prints 0.9% versus body 0.09%

**Candidate statement:** Protocol mortality power appendix prints 0.9% versus body 0.09%.

**Status:** Pending Human Adjudication

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol p. 14 mortality power input vs PLAN protocol p. 29 power appendix

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-101

**Classification rationale:** Both conflicting percentage inputs are within plan material. Protocol summary and main report corroborate the smaller scale and do not establish P_R.

**Classification ambiguity:** None

- **Included Finding IDs:** F-NUM-101.
- **Duplicate Finding IDs:** F-XS-008, F-ST1-003.
- **Checker provenance:** numeric_consistency_reviewer, cross_source_consistency_reviewer, statistics_pass_1; relationships N087/S025.
- **Source-order key:** DOC-002 / p.14 / section 2.11 absolute-reduction input, compared with p.29.
- **Conflicting locations and roles:** PLAN [protocol p.14 section 2.11](../../joi180015supp1_prod.pdf#page=14) and PLAN [protocol p.29 power appendix, mortality paragraph and scenario](../../joi180015supp1_prod.pdf#page=29).
- **Corroborating locations:** PLAN [protocol p.1 summary](../../joi180015supp1_prod.pdf#page=1) prints 0.9 deaths/1000 admissions; REPORT [main p.4 sample-size paragraph](../../jama_parshuram_2018_oi_180015.pdf#page=4) prints 0.9/1000. Neither contradicts the body value and neither creates P_R.
- **Printed source and comparator:** Body: 18% relative reduction, absolute reduction 0.09%, baseline 5.1/1000. Appendix: 18% relative reduction corresponds to absolute reduction 0.9%; baseline scenario 5.1/1000, relative reduction 0.178. Both cite 20 hospitals, .05 alpha and 80% power.
- **Rule/calculation:** 5.1 × .18 / 10 = .0918%. Half-unit inputs [5.05,5.15]/1000 and [17.5%,18.5%] yield recomputed absolute-percent interval [.088375%,.095275%]. Printed .9% interval [.85%,.95%] has gap .754725 percentage points and relative discrepancy .754725/.9 = .838583. Comparing body [.085%,.095%] with appendix [.85%,.95%] gives gap .755 and relative discrepancy .838889. Both exceed .05; .9% also exceeds the same stated baseline risk .51%.
- **Qualifying route:** Route A, category 2; focus D (also C).
- **Proposed classification:** plan_material; primary P_P; all relationships P_P; no role ambiguity.
- **Affected extracted result:** Absolute effect-size assumption for the primary mortality power calculation, .9% versus .09%.
- **Context and alternatives:** The appendix may intend .9 per 1000 or .09%. The surrounding inputs reconstruct the smaller scale, but an extractable printed magnitude differing beyond precision remains category 2. No alternative power scenario is identified in that paragraph.
- **Bounded human question:** Which absolute mortality-reduction value and unit were used, and how should the appendix .9% reconcile with the body .09% and summary .9/1000?

## C012 — SAP model-choice sensitivity outputs for primary/key-secondary effects are not supplied

**Candidate statement:** SAP model-choice sensitivity outputs for primary/key-secondary effects are not supplied.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP pp. 4, 5 vs REPORT main article pp. 4-7 and complete REPORT results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004

**Classification rationale:** The specified primary/key-secondary sensitivity set is compared with the complete supplied report outputs; the reported baseline-adjusted GEE is excluded from the absent set.

**Classification ambiguity:** The SAP is undated and uses retrospective wording; prospective timing is not established.

- **Included Finding IDs:** F-XS-004.
- **Duplicate Finding IDs:** F-ST1-006.
- **Checker provenance:** cross_source_consistency_reviewer and statistics_pass_1; relationships S064/S065.
- **Source-order key:** DOC-003 / p.4 / Sensitivity to model choice (no affirmative report claim of sensitivity output).
- **Conflicting locations and roles:** PLAN [SAP p.4 Sensitivity to model choice](../../joi180015supp2_prod.pdf#page=4) and PLAN [SAP p.5 remaining probability/rate models](../../joi180015supp2_prod.pdf#page=5), versus REPORT [main pp.4–5 analysis methods](../../jama_parshuram_2018_oi_180015.pdf#page=4), REPORT [main pp.6–7 primary/main-secondary outputs](../../jama_parshuram_2018_oi_180015.pdf#page=6) and full REPORT [results pp.1–14](../../joi180015supp3_prod.pdf#page=1).
- **Printed source and comparator:** SAP says models for ORs, probabilities and rate ratios were also run. Eight relative-scale approaches comprise post-only GEE/GLMER, pre/post treatment-time GEE/GLMER, baseline-adjusted GEE/GLMER, inverse-variance weighted linear and quasi-binomial/Poisson models; five absolute-scale approaches comprise post-only GEE, pre/post GEE, baseline-adjusted GEE, weighted linear and quasi-binomial identity-link models. Report supplies baseline-adjusted GEE and selected identity-model fallback outputs, with no alternative-model estimates or robustness summary.
- **Rule/calculation:** The listed baseline-adjusted GEE approach is already reported and is not an absent output; the remaining stated sensitivity set for primary/key-secondary effect measures is not supplied. Complete main/results layout inspection, including every figure/table, found no alternative-model result set. Numeric precision is not applicable to absence of specified analyses.
- **Qualifying route:** Route A, category 5; focus D.
- **Proposed classification:** protocol_report; primary P_R; all relationships P_R. SAP is PLAN by specification content despite retrospective tense.
- **Affected extracted result:** Model-choice robustness of mortality OR1.01/RD0.01 and SCDE RR0.77/RD−0.34; no alternative effects are invented.
- **Context and alternatives:** The undated SAP's retrospective wording may document internal completed checks rather than a prospective commitment, or outputs may exist outside the package. The stated sensitivity set and missing supplied outputs remain the observable comparison; timing is a classification ambiguity, not proof of a prospective sequence.
- **Bounded human question:** Which listed sensitivity models applied to mortality and SCDE, what were their estimates/intervals, and when was the sensitivity specification adopted?


