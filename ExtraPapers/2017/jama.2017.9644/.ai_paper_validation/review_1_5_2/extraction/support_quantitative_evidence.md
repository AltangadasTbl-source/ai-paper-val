# Support Quantitative Evidence Map

## Scope and evidence basis

Complete assigned scope: `DOC-002` (`joi170084supp1_prod.pdf`, PDF pp. 1-14) and `DOC-003` (`joi170084supp2_prod.pdf`, PDF pp. 1-6). This map uses only the direct PDFs and fresh assets below `preprocessing/`; no prior audit derivative was consulted. Page references are PDF page numbers. `SUP-N` keys are numeric/reporting relationships and `SUP-S` keys are inferential-statistical relationships. They are provisional mapping keys, not candidate IDs.

Fresh asset references: `preprocessing/layout_text/DOC-002-p1.txt` through `DOC-002-p14.txt`; `preprocessing/layout_text/DOC-003-p1.txt` through `DOC-003-p6.txt`; rendered confirmation for DOC-002 pp. 3-7 and DOC-003 pp. 2, 4-6. The page-specific layout text supplies the quoted values; renders were used to confirm eTable/eFigure alignment and small labels.

## DOC-002 — protocol (pp. 1-14)

### Explicit no-applicable-unit coverage

| Pages | Coverage result |
|---|---|
| 1 | Administrative cover/version (`V1.1`, 24 July 2015); no trial-result display or result-relevant numeric relationship. |
| 8-11 | Monitoring, privacy, archival/publication content and references; no trial-result display or result-relevant quantitative definition beyond administrative time periods. |
| 12 | TICI-category reference annex; its threshold definitions are mapped in SUP-N005. |
| 13 | Modified Rankin Scale reference annex; its 0-6 scale is mapped in SUP-N006. |
| 14 | NIHSS external-reference notice only; no supplied score definition, result, or numeric relationship. |

### Observed quantitative and reporting relationships

| Key | Exact observed evidence and source | Relationship / match key |
|---|---|---|
| SUP-N001 | DOC-002 p.2, lines 23-43: published stent-retriever studies stated to obtain 58%-72% recanalization; ADAPT stated as `>90%`; an earlier observational comparison of 244 patients states complete recanalization 84% with ADAPT vs 68% with stent retriever, `P = 0.006`. | Historical/background quantities, not a result of the randomized trial. Preserve the 244-patient / 84% / 68% / P=.006 identity if compared with a later statement. |
| SUP-N002 | DOC-002 pp.2-3, lines 56-76: planned comparison of strategies; secondary planned outcomes include end-of-first-strategy recanalization, procedural delays, listed complication types, 24-hour cerebral hemorrhage, 3-month disability and death, and subgroup comparisons by occlusion site (middle cerebral, internal carotid, tandem) and clot length. | Protocol outcome-domain match keys for main Table 2/eFigures: strategy is first-line aspiration vs first-line stent retriever; follow-up windows are 24 hours and 3 months. |
| SUP-N003 | DOC-002 p.3, lines 79-107: age `>18`; anterior circulation carotid termination T or L, ACM1/ACM2; treatment access within 6 hours; centralized 1:1 randomization stratified by center and prior IV thrombolysis. | Population/randomization definition. Main-paper match key: randomized ITT treatment groups, center and IV-thrombolysis stratification. |
| SUP-N004 | DOC-002 p.4, lines 130-140: randomized ADAPT receives first distal aspiration and stent-retriever arm does not initially; maximum 3 passes before failure; rescue procedure at operator discretion. DOC-002 p.5, lines 215-221: no-follow-up/protocol-noncompliance patients are not excluded. | Intervention, permitted rescue, and population-retention definitions. Main-paper/eTable match key: first-line assigned group versus actual device/rescue use. |
| SUP-N005 | DOC-002 p.5, lines 175-202: primary criterion is percentage complete recanalization, final `TICI 2b-3`, at end of angiography, assessed by blinded independent evaluator. Secondary recanalization is `TICI 2b-3` at end of first strategy; NIHSS and a 4-point NIHSS gain at 24 h; mRS favorable at 3 months if `mRS ≤2`; hemorrhage at `24 h (+/-12 h)`; death within 3 months. DOC-002 p.12: revised TICI: 2B is distal-branch filling `≥50%`; 3 is complete perfusion. | Primary and secondary endpoint definitions. Main-paper match key: successful revascularization = mTICI 2b/3 after all endovascular procedures, denominator randomized group. The protocol spells `TICI` while article/supplement use `mTICI`; this is a terminology comparison point, not itself an inconsistency. |
| SUP-N006 | DOC-002 p.13: mRS categories 0-6, from no symptoms (0) through death (6); score 2 is slight disability, 3 moderate disability, and 4-5 increasingly severe disability. | Ordinal clinical-outcome scale definition. DOC-003 eFigure 1 uses this scale; it combines 5 and 6 in its model. |
| SUP-N007 | DOC-002 p.6, lines 235-241: total study duration 27 months, inclusion 24 months, maximum individual participation 3 months; schedule places mRS at inclusion and 90-day follow-up, NIHSS at inclusion and 24-hour follow-up. | Timepoint match keys. These are planned schedule definitions, not observed follow-up totals. |
| SUP-N008 | DOC-002 pp.6-7, lines 255-280: planned two-tailed alpha 5%, no interim analysis; quantitative values summarized mean/SD if Gaussian or median/IQR otherwise; categorical values as frequencies/percentages; ITT and per-protocol analyses. Primary: chi-square comparison, absolute and relative rate difference with 95% CI, center-stratified analysis and Breslow-Day interaction. Secondary: t test/Mann-Whitney U, chi-square/Fisher exact as applicable. | Protocol statistical-plan definitions. Compare only after accounting for version/time and model distinction; no conclusion is drawn here. |
| SUP-S001 | DOC-002 pp.6-7, lines 269-280: primary planned test/effect definitions as above. | Inferential relationship: two-sided alpha=.05; primary planned chi-square and 95% absolute/relative rate-difference CIs, with center interaction via Breslow-Day. |
| SUP-S002 | DOC-002 p.7, lines 283-295: sample-size premise = control complete recanalization 70%, ADAPT 85%, stated increase 21%, two-sided alpha 5%, power 90%, `161` per arm / `322` total. | Protocol sample-size relationship. The printed 85%-70%=15 percentage points, whereas the stated 21% is compatible with a relative increase (15/70=21.4%), not an absolute increase; preserve scale label for checking. |
| SUP-N009 | DOC-002 p.7, lines 283-295: values named in SUP-S002. | Arithmetic/scale key: 70% to 85% = +15 percentage points and approximately +21.4% relative to 70%. |

### Derived diagnostics and candidate signals (not candidate registration)

1. **SUP-N009 diagnostic:** the protocol calls 70% to 85% an “increase ... by 21%.” This reconciles as a relative increase (15/70=21.4%) but not as an absolute percentage-point change. The source does not specify the intended scale in that sentence. **Candidate signal:** label/scale ambiguity requiring later human comparison only if the printed sample-size calculation or a matched report uses an incompatible scale.
2. **SUP-S001/SUP-S002 diagnostic:** the protocol’s planned primary method/sample-size premise differs from the published main-paper statistical description (fresh DOC-001 p.3: mixed logistic regression, 190 per group/380 total, assumed 15% absolute increase). **Candidate signal:** a protocol-versus-report plan divergence exists, but the supplied documents do not establish whether an amended SAP/protocol superseded this 2015 version; do not characterize it as a reporting error without that missing provenance.

## DOC-003 — statistical supplement, eTable, and eFigures (pp. 1-6)

### Explicit no-applicable-unit coverage

| Pages | Coverage result |
|---|---|
| 1 | Contents/title page only; no standalone result value. |
| 3 | Reference list and completion of a missing-data statement; no new displayed outcome value beyond the `n=20`/`n=22` data-completion rule mapped in SUP-N012. |

### Observed methods, definitions, and statistical relationships

| Key | Exact observed evidence and source | Relationship / match key |
|---|---|---|
| SUP-S003 | DOC-003 p.2: secondary binary outcomes use mixed logistic models adjusted for stratification variables, reported as adjusted ORs/95% CIs. Adjusted absolute and relative RDs derive from marginal probabilities; 95% CIs use 2,000 bootstrap samples. | Statistical definition for secondary binary-outcome estimates; distinguish adjusted OR from marginal-probability RD. |
| SUP-S004 | DOC-003 p.2: 90-day mRS distribution combines scores 5 and 6 and uses mixed ordinal logistic regression with treatment and prior IV thrombolysis fixed effects and center random effect; reported as adjusted common OR. | eFigure 1/model match key: aspiration relative to stent retriever; ordinal mRS shift; adjusted common OR. |
| SUP-S005 | DOC-003 p.2: 24-hour NIHSS change uses cLDA adjusted for randomization stratification variables; baseline and postbaseline outcomes are dependent variables in linear mixed model with unstructured covariance; baseline means constrained equal; time-by-arm interaction estimates treatment effect. | Main Table 2 NIHSS-change statistical-definition key; model-adjustment/direction key. |
| SUP-S006 | DOC-003 p.2: times from groin puncture/clot contact to primary outcome and total device passes use Mann-Whitney U; standardized differences on rank-transformed data, 95% CIs via 2,000 bootstraps. | Main Table 2 time/passes relation and effect-scale key. |
| SUP-N010 | DOC-003 pp.2-3: no imputation for secondary outcomes or loss to follow-up. For mTICI: groin-access failure `n=4` treated as mTICI 0; absent core-lab reading replaced by site evaluation, `n=20` end procedure and `n=22` end first-line procedure, regardless of group. | Primary/angiographic endpoint handling. Fresh main-paper match key: DOC-001 p.4 gives same n=4/n=20 rule; Figure 2 repeats n=4/n=20. |

### eTable: device counts

| Key | Exact observed evidence and source | Relationship / match key |
|---|---|---|
| SUP-N011 | DOC-003 p.4 eTable, frontline strategy: assigned/treated headers are aspiration first `n=174`, stent retriever first `n=175`. Aspiration column: ACE64 65, ACE60 12, ACE68 1, 3MAX 5, 4MAX 10, 5MAX 63, SOFIA 17, ARC6F 1; all named stent retrievers 0. Stent-retriever column: ACE64 1, 3MAX 1, 5MAX 2, SOFIA 1, SOLITAIRE FR 101, TREVO 56, EMBOTRAP 9, EMBOLYS 5*21 1, CATCH 3*15 1, ERIC 3, PHENOX 8, REVIVE 2 (all other listed rows 0). | Device-use counts by first-line assigned group. Fresh main-paper match key: DOC-001 p.4 flow reports 174 received contact aspiration as randomized and 170 received stent retriever as randomized, while eTable’s stent-first header is 175. Interpret denomination/device count after confirming eTable definition. |
| SUP-N012 | DOC-003 p.4 eTable, rescue strategy headers: aspiration-first `n=63`, stent-retriever-first `n=45`. Counts (aspiration/stent): ACE64 7/10, ACE60 0/0, 3MAX 3/2, 4MAX 3/0, 5MAX 8/13, SOFIA 2/9, SOLITAIRE FR 23/16, TREVO 24/16, EMBOTRAP 1/1, ERIC 7/5, PHENOX 5/1, MAVERICK 0/1, REVIVE 1/0. | Rescue device-use counts. Main-paper match key: DOC-001 p.7 says rescue treatment occurred in 63 (32.8%) and 45 (23.8%) patients. |

### eFigure 1: mRS distribution

| Key | Exact observed evidence and source | Relationship / match key |
|---|---|---|
| SUP-N013 | DOC-003 p.5 eFigure 1: aspiration group `n=181`, mRS 0-6 counts `24, 35, 23, 25, 25, 14, 35`; stent-retriever group `n=182`, counts `40, 38, 13, 26, 17, 13, 35`. | 90-day mRS ordinal distribution. Within-column sums are 181 and 182, respectively. Main-paper match key: DOC-001 p.7 reports 363 (95.3%) with mRS assessment at 3 months. |
| SUP-S007 | DOC-003 p.5: comparison P=.15 from mixed ordinal logistic model adjusted for center and prior IV thrombolysis; common OR for aspiration relative to stent retriever = `0.76` (95% CI `0.53 to 1.10`). Scores 5 and 6 are combined in the model (DOC-003 p.2). | Ordinal mRS inferential result. Direction label is aspiration relative to stent retriever; CI contains 1 and corresponds to displayed P=.15. |

### eFigure 2: primary-outcome subgroup display

| Key | Exact observed evidence and source | Relationship / match key |
|---|---|---|
| SUP-N014 | DOC-003 p.6 eFigure 2 overall: aspiration `164/192 (85.4)`; stent retriever `157/189 (83.1)`; OR `1.20 (0.68 to 2.10)`, P=.53. Outcome is core-lab mTICI 2b/3 after all endovascular procedures. | Main Table 2 primary-outcome match key; values match fresh DOC-001 p.6 Table 2. |
| SUP-N015 | DOC-003 p.6: prior IV rt-PA—No: 56/66 (84.8) vs 50/65 (76.9); Yes: 108/126 (85.7) vs 107/124 (86.3). | Subgroup counts reconcile to the overall numerators/denominators: aspiration 56+108=164 and 66+126=192; stent 50+107=157 and 65+124=189. |
| SUP-S008 | DOC-003 p.6: prior-IV-rt-PA ORs (aspiration vs stent) are 1.69 (0.68-4.17), P=.28 for No and 0.96 (0.46-1.98), P=.96 for Yes; `P Het=.34`. | Subgroup effect/interaction key. P Het is defined as heterogeneity P value across subgroups. |
| SUP-N016 | DOC-003 p.6: occlusion site—M1-MCA 83/100 (83.0) vs 87/104 (83.7); M2-MCA 43/48 (89.6) vs 26/31 (83.9); ICA 20/22 (90.9) vs 30/33 (90.9). | Subgroup categories/denominators. They do not cover every randomized patient (170/192 and 168/189), so are subgroup-specific available data, not a complete primary-outcome partition. |
| SUP-S009 | DOC-003 p.6: occlusion-site ORs are M1-MCA .95 (.45-2.01), P=.90; M2-MCA 1.73 (.44-6.68), P=.43; ICA .95 (.14-6.36), P=.96; `P Het=.75`. | Occlusion subgroup inferential key. |
| SUP-N017 | DOC-003 p.6: clot burden score (CBS) `≥6`: 74/88 (84.1) vs 66/76 (86.8); `<6`: 36/41 (87.8) vs 38/49 (77.6). CBS is a 0-10 semiquantitative clot-extent scale, where higher clot burden means lower CBS. | CBS scale, direction, and subgroup counts. These denominators (129/192 and 125/189) are not full-group partitions. |
| SUP-S010 | DOC-003 p.6: CBS ORs .73 (.33-1.59), P=.43 for ≥6 and 1.49 (.62-3.58), P=.37 for <6; `P Het=.25`. | CBS subgroup inferential key. |
| SUP-N018 | DOC-003 p.6: unplanned clot-length subgroup: `<8 mm` 18/24 (75.0) vs 28/33 (84.8); `≥8 mm` 107/123 (87.0) vs 93/113 (82.3). | Unplanned subgroup and counts. These denominators (147/192 and 146/189) are not full-group partitions. |
| SUP-S011 | DOC-003 p.6: clot-length ORs .74 (.26-2.11), P=.57 for <8 mm and 1.27 (.64-2.48), P=.49 for ≥8 mm; `P Het=.17`; footnote marks this subgroup unplanned. | Unplanned subgroup inferential key. |

### Derived diagnostics and candidate signals (not candidate registration)

1. **SUP-N011 diagnostic:** frontline device-row totals are 174 for aspiration first and 186 for stent retriever first, whereas the headers are n=174 and n=175. **SUP-N012 diagnostic:** rescue device-row totals are 84 and 74 versus headers n=63 and n=45. The table title reports device details rather than a mutually exclusive participant category; fresh main-paper DOC-001 p.7 reports multiple revascularization attempts (ranges 0-11 and 0-15) and device switching/rescue is allowed. **Candidate signal:** the displayed device totals should not be used as participant totals without a supplied statement that rows are mutually exclusive; no arithmetic inconsistency is established.
2. **SUP-N011 cross-document signal:** DOC-003 p.4 labels stent-retriever frontline `n=175`, while fresh DOC-001 p.4 flow says 170 received a stent retriever as randomized (and 189 were randomized to that strategy). The different terms may identify device use rather than patients receiving assigned treatment; the supplement does not define its denominator sufficiently to resolve the mismatch. **Candidate signal:** denominator/label comparison for human adjudication; preserve exact values and definitions.
3. **SUP-N014/SUP-S008-SUP-S011 diagnostic:** eFigure 2’s overall counts, percent calculations, and primary OR/CI/P match main Table 2 (DOC-001 p.6); IV-rt-PA subgroup counts sum to the overall values. The site/CBS/clot-length subgroups have incomplete denominators, consistent with missing or unclassified subgroup data rather than an arithmetic contradiction. **No candidate signal** from the incomplete subgroup sums alone.
4. **SUP-S007 diagnostic:** eFigure 1’s OR=.76, 95% CI .53-1.10 includes null and its P=.15 is coherent at displayed precision. **No display-zero or interval/P-value candidate signal.**

## Coverage count and limitations

- Pages reviewed: DOC-002 14/14; DOC-003 6/6.
- Provisional numeric/reporting relationships: 18 (`SUP-N001` to `SUP-N018`).
- Provisional inferential-statistical relationships: 11 (`SUP-S001` to `SUP-S011`).
- Candidate signals flagged for downstream checking: 4 (protocol 21%-scale wording; protocol-to-publication plan/sample-size divergence pending amendment provenance; eTable device totals versus participant headers; eTable stent-frontline n=175 versus main-flow 170 received as randomized). These are signals only, not candidate IDs or dispositions.
- Limitations: protocol is a 2015 version and no supplied amendment/SAP version history resolves planned-versus-published differences; eTable does not state whether device rows are mutually exclusive per patient; subgroup denominators can be incomplete because source does not state availability/missingness for each subgroup variable. Native/layout text was legible; no OCR limitation affects these pages.
