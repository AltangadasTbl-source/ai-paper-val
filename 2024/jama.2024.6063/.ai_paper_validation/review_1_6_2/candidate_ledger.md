# Workflow 1.6.2 Candidate Ledger

Pending Human Adjudication. Thirteen stable candidates were registered only after the independent initial inclusion screen. IDs follow source order using the screen's disjoint consolidation groups. Every included finding is preserved; no assigned ID is deleted. Source roles follow content. All thirteen evidence states were assigned reproduced by the independent rechecker; the independent auditor confirmed inclusion of all thirteen IDs after reviewing the complete screening and excluded-observation records. The complete source passages, calculations and alternatives for each registration are retained in the corresponding descriptive consolidation group in screening/inclusion_screen.md and the cited canonical checker findings; this ledger preserves every affected location.

## Classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_C | S_C, S_W | REPORT main Key Points vs REPORT main abstract/Table 2/text and REPORT results original/VAS24 copies | reproduced | CONFIRMED | F-NUM-001, F-XS-001 |
| C002 | statistical_results | S_W | S_W | REPORT main Methods vs REPORT main Discussion placebo percentages | reproduced | CONFIRMED | F-NUM-002, F-XS-008 |
| C003 | protocol_report | P_R | P_R | PLAN protocol primary VAS definition vs REPORT main primary VAS definition and Table 1 footnote | reproduced | CONFIRMED | F-XS-002, F-ST1-005 |
| C004 | statistical_results | S_W | S_W | REPORT main ICOAP scoring ranges vs REPORT main item-count/scoring definition | reproduced | CONFIRMED | F-NUM-003 |
| C005 | protocol_report | P_R | P_R | PLAN protocol adopted power inputs vs REPORT main power inputs | reproduced | CONFIRMED | F-XS-005, F-ST1-004 |
| C006 | protocol_report | P_R | P_R | PLAN protocol/SAP primary model vs REPORT main primary producing model | reproduced | CONFIRMED | F-XS-003, F-ST1-006 |
| C007 | protocol_report | P_R | P_R | PLAN protocol/SAP per-protocol primary analysis vs REPORT main/results supplied efficacy analyses | reproduced | CONFIRMED | F-XS-004, F-ST1-007 |
| C008 | statistical_results | S_W | S_W | REPORT main ICOAP within-display and REPORT results WOMAC/hsCRP within-display modeled contrasts | reproduced | CONFIRMED | F-NUM-004, F-NUM-101, F-NUM-102, F-ST1-001 |
| C009 | statistical_results | S_C | S_C | REPORT main adverse-event treatment counts vs REPORT results detailed adverse-event treatment counts | reproduced | CONFIRMED | F-NUM-104, F-XS-006 |
| C010 | statistical_results | S_C | S_C | REPORT main serious-event relatedness summary vs REPORT results serious-event relatedness classifications | reproduced | CONFIRMED | F-XS-007 |
| C011 | plan_material | P_P | P_P | PLAN protocol effusion power inputs vs PLAN protocol claimed power and statistical specification | reproduced | CONFIRMED | F-ST1-003 |
| C012 | statistical_results | S_W | S_W | REPORT results glucose12 and REPORT main/results WOMAC total24 within-display contrast intervals vs arm intervals and reproducing rows | reproduced | CONFIRMED | F-ST1-002, F-ST2-001 |
| C013 | statistical_results | S_W | S_W | REPORT results WORMS smaller-one-unit counts vs percentages and totals in one display | reproduced | CONFIRMED | F-NUM-103 |

## C001 — Primary signed contrast differs between report locations

**Finding IDs:** F-NUM-001, F-XS-001.
**Qualifying route:** Route A, category 2.
**Registration:** Key Points +0.30 conflicts with matched negative primary values, including −0.3 in the main report and −0.27 in the original sensitivity table. The signed intervals leave gap .545/.30 = 1.8167. The affected extraction is the direction of the primary 24-week VAS contrast.
**Exact source locations:** DOC-001 [p1 abstract](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=1), [p2 Key Points](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2), [p6 Table 2](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), [p7 primary text](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7); DOC-004 [p2 original row](../../joi240048supp3_prod_1727199125.83025.pdf#page=2), [p5 VAS24](../../joi240048supp3_prod_1727199125.83025.pdf#page=5).
**Classification rationale:** Both within-main and cross-report values are compared; S_C takes precedence over S_W. No PLAN conflict is assigned.
**Classification ambiguity:** None; the rechecker confirmed the supplementary copies are directly conflicting comparators.
**Human question:** Which signed treatment contrast belongs to the primary estimate and its interval?

## C002 — Placebo composition percentages differ by a decimal place

**Finding IDs:** F-NUM-002, F-XS-008.
**Qualifying route:** Route A, category 2.
**Registration:** Methods .5% and Discussion .05% both parenthetically describe less than 5 mg/g other omega-3. Percentage intervals leave gap .395, relative .79 against .5%; 5 mg/g converts to .5%. The affected extraction is comparator composition.
**Exact source locations:** DOC-001 [p2 intervention last line](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2), [p3 continuation](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3), [p9 Discussion](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=9).
**Classification rationale:** Conflicting percentages occur within the main REPORT; S_W.
**Classification ambiguity:** None.
**Human question:** Which concentration bound and parenthetical percentage describe the placebo?

## C003 — Primary VAS recall periods differ between plan and report

**Finding IDs:** F-XS-002, F-ST1-005.
**Qualifying route:** Route B.
**Registration:** The planned primary question rates pain today; the report rates pain over the past seven days. Common scale and 24-week follow-up do not identify a shared recall window. The primary outcome definition is affected, with no supplied questionnaire or amendment bridge.
**Exact source locations:** DOC-001 [p3 primary outcome](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3), [p5 Table 1 footnote b](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=5); DOC-002 [p6 primary definition](../../joi240048supp1_prod_1727199125.7845.pdf#page=6), [p8 primary question](../../joi240048supp1_prod_1727199125.7845.pdf#page=8).
**Classification rationale:** PLAN versus REPORT endpoint window; P_R and protocol_report.
**Classification ambiguity:** An unsupplied amended instrument could reconcile the windows.
**Human question:** Which recall period was administered for the primary VAS, and what amendment connects the definitions?

## C004 — ICOAP item count does not identify the scoring denominator

**Finding IDs:** F-NUM-003.
**Qualifying route:** Route B.
**Registration:** Eight intermittent items with scores 0–4 imply maximum 32 versus printed intermittent range 0–24; five constant items imply 20, while the stated total maximum is 44 rather than 52. Conservative interval multiplication [26.25,38.25] versus [23.5,24.5] leaves gap 1.75/24 = .0729. No unscored-item or weighting bridge is supplied. This affects raw-to-0–100 normalization definitions.
**Exact source locations:** DOC-001 [p4 post hoc scoring](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p5 Table 1 footnote g](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=5), [p6 ICOAP rows/descriptions](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6).
**Classification rationale:** Quantitative scoring definition within one REPORT; S_W and statistical_results.
**Classification ambiguity:** A field-specific item convention is possible but no external definition is used.
**Human question:** How do the printed item count and raw maxima identify the scored items and normalization denominator?

## C005 — Adopted power specifications differ between plan and report

**Finding IDs:** F-XS-005, F-ST1-004.
**Qualifying route:** Route B.
**Registration:** Planned pain change SD 25.5 versus reported 23.8 leaves interval gap 1.60/25.5 = .06275; planned effusion power 96% versus reported 90% leaves gap 5/96 = .05208. Planned 20% of area mean 2.24 cm² and reported 4.5 mL are dimensionally different targets. The unchanged 130/arm does not identify which prospectively adopted specification governed design.
**Exact source locations:** DOC-001 [p4 power](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4); DOC-002 [p2 effusion hypothesis](../../joi240048supp1_prod_1727199125.7845.pdf#page=2), [p12 adopted power](../../joi240048supp1_prod_1727199125.7845.pdf#page=12).
**Classification rationale:** PLAN versus REPORT adopted design inputs; P_R. The plan-internal reproduction is separately C011.
**Classification ambiguity:** An unsupplied prospective amendment or retrospective summary may explain the inputs.
**Human question:** Which dated calculation prospectively adopted the dispersion and effusion effect/power inputs?

## C006 — Reported primary model differs from the supplied planned model

**Finding IDs:** F-XS-003, F-ST1-006.
**Qualifying route:** Route A, category 5.
**Registration:** Planned change-score linear regression is compared with the producing longitudinal mixed model using treatment/month/interaction, participant and center random intercepts, and a month random slope. The supplied report contains no separate original-model primary result. Both model choices may be coherent; the issue concerns prespecification or amendment of the primary analysis.
**Exact source locations:** DOC-001 [p4 statistical methods](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p7 continuation](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7); DOC-002 [p12 Statistics](../../joi240048supp1_prod_1727199125.7845.pdf#page=12); DOC-003 [p1 lines 5–7](../../joi240048supp2_prod_1727199125.8245.pdf#page=1).
**Classification rationale:** PLAN protocol/SAP versus REPORT model; P_R. Agreement between the two plan copies does not add P_P.
**Classification ambiguity:** An unsupplied model amendment or operational elaboration is possible.
**Human question:** Where is the prespecification or amendment connecting the two primary models, or the original-model primary result?

## C007 — Planned per-protocol primary efficacy analysis is not reported

**Finding IDs:** F-XS-004, F-ST1-007.
**Qualifying route:** Route A, category 5.
**Registration:** Both supplied plans unconditionally prescribe per-protocol analyses for participants consuming at least 80% of capsules. Full main pp1–10 and results pp1–15 inspection finds no adherence-restricted primary efficacy estimate. Adherence counts, age adjustment, and imputation sensitivities are distinct records.
**Exact source locations:** DOC-002 [p12 Statistics](../../joi240048supp1_prod_1727199125.7845.pdf#page=12); DOC-003 [p1 lines 8–9](../../joi240048supp2_prod_1727199125.8245.pdf#page=1); DOC-001 [p4 methods](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p6 efficacy table](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), [p7 methods/results](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7); DOC-004 [p2 sensitivity table](../../joi240048supp3_prod_1727199125.83025.pdf#page=2), [p3 adherence](../../joi240048supp3_prod_1727199125.83025.pdf#page=3).
**Classification rationale:** Planned primary analysis versus its absence from REPORT efficacy material; P_R. Neither the agreement of plan copies nor adherence descriptives add another relationship.
**Classification ambiguity:** An unsupplied analysis or amendment could explain reporting status.
**Human question:** Where is the planned adherence-restricted primary estimate and population definition, or the amendment removing it?

## C008 — Repeated modeled arm-change and point-contrast discrepancies

**Finding IDs:** F-NUM-004, F-NUM-101, F-NUM-102, F-ST1-001.
**Qualifying route:** Route A, category 4.
**Registration:** The placebo-minus-krill subtraction reproducing other modeled rows yields ICOAP total24 [1.60,1.80] versus printed [2.045,2.055] (relative gap .11951), WOMAC weight-bearing4 [−20,−18] versus [2.5,3.5] (6.8333), and hsCRP12 [.76,.78] versus [.065,.075] (9.7857). This compares printed model changes with model contrasts rather than crude marginal means. One repeated rule failure retains all three occurrences.
**Exact source locations:** DOC-001 [p6 ICOAP total/intermittent](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6); DOC-004 [p5 weight-bearing/function week4](../../joi240048supp3_prod_1727199125.83025.pdf#page=5), [p6 hsCRP12/24 and glucose12](../../joi240048supp3_prod_1727199125.83025.pdf#page=6). Producing model corroboration: DOC-001 [p4](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p7](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7).
**Classification rationale:** Each numeric contrast conflicts within its own REPORT display; S_W. Different-outcome patterns across documents and corroborating methods add no conflicting S_C relationship.
**Classification ambiguity:** Row-specific distinct models or marginalizations are not supplied.
**Human question:** Which arm changes and contrasts belong to each affected endpoint/time row, and were they produced by the same model?

## C009 — Selected adverse-event counts change treatment attribution

**Finding IDs:** F-NUM-104, F-XS-006.
**Qualifying route:** Route A, category 2.
**Registration:** Main krill/placebo reflux 1/3 versus supplementary 3/1; main krill abdominal discomfort 0 versus supplementary 3; main placebo cough 0 versus supplementary 2. Explicit-number half-unit gaps exceed the rule; blank supplementary cells remain blank. The repeated treatment-attribution pattern retains three event types.
**Exact source locations:** DOC-001 [p8 Table 3](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8); DOC-004 [p10 cough and treatment headers](../../joi240048supp3_prod_1727199125.83025.pdf#page=10), [p11 gastrointestinal rows](../../joi240048supp3_prod_1727199125.83025.pdf#page=11).
**Classification rationale:** Counts conflict across two REPORT documents; S_C and statistical_results.
**Classification ambiguity:** Different undisclosed coding or subsets remain possible.
**Human question:** Which treatment-specific counts apply to the three event types, and are the counting definitions shared?

## C010 — Serious-event relatedness classifications do not reconcile

**Finding IDs:** F-XS-007.
**Qualifying route:** Route B.
**Registration:** Main serious-event relatedness is summarized as all unrelated with treatment-related 0/0, while the supplement labels krill anaemia Probable and other entries Possible. No threshold or later-assessment bridge is supplied. Possible entries are not automatically counted as related, and no adjacent integer comparison bypasses the precision rule. The affected extraction is the final related-SAE classification/result.
**Exact source locations:** DOC-001 [p8 Table 3, footnote b, narrative](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8); DOC-004 [p14 eTable 8 relatedness entries](../../joi240048supp3_prod_1727199125.83025.pdf#page=14).
**Classification rationale:** Reported statistical safety classifications across two REPORT documents; S_C and statistical_results.
**Classification ambiguity:** An unsupplied final investigator assessment may reconcile preliminary labels.
**Human question:** Which assessment and mapping govern the final related-SAE summary, particularly the probable anaemia entry?

## C011 — Planned effusion power does not reproduce from supplied inputs

**Finding IDs:** F-ST1-003.
**Qualifying route:** Route B.
**Registration:** The plan states 96% power for a 20% difference using mean 2.24 cm², change SD 1.35, and 117/130 per arm at two-sided .05. Labelled normal diagnostics give 71.844%/76.286%; favorable half-unit effect/SD inputs with fixed n give at most 78.778%, leaving gap 16.722/96 = .1742. The mechanical rechecker additionally allowed n=130±.5, obtaining favorable power 78.93133% and gap 16.56867/96 = .1725903; the discrepancy remains. An additional effect, variance, or efficiency assumption is not supplied. This concerns the stated planned detectable effusion target, not a preferred analysis.
**Exact source locations:** DOC-002 [p2 effusion hypothesis](../../joi240048supp1_prod_1727199125.7845.pdf#page=2), [p12 Power/Statistics](../../joi240048supp1_prod_1727199125.7845.pdf#page=12); DOC-003 [p1 model and significance corroboration](../../joi240048supp2_prod_1727199125.8245.pdf#page=1).
**Classification rationale:** Conflict lies within PLAN power inputs and claimed power; P_P and plan_material. The SAP corroborates the specification.
**Classification ambiguity:** Exact adopted power formula and efficiency assumptions are absent.
**Human question:** What supplied calculation and additional assumption produce the stated 96% effusion power?

## C012 — Repeated contrast-interval widths differ from a reproducing display rule

**Finding IDs:** F-ST1-002, F-ST2-001.
**Qualifying route:** Route A, category 4.
**Registration:** The empirical root-sum-square arm-CI-half-width rule reproduces neighboring glucose24 and metabolic rows and all five earlier WOMAC total-pain time points. Glucose12 arm intervals imply half-width [.21570,.22984], versus printed 1.26; interval endpoints leave relative gaps .8573 and .7670. Its .07(−1.19,1.33), P=.92 tuple also matches hsCRP12. WOMAC total24 arm intervals imply half-width [32.526912,33.941125], versus printed 27.5; main 3.0 estimate yields lower/upper endpoint relative gaps .207371 and .128287, and supplementary integer 3 yields .188621 and .113771. Independent pass-2 screening consolidated this occurrence into the existing C012 because both fail the same supported empirical width rule and separate causes are not established. Exact variance/covariance or critical-value conventions remain human questions; CI/null/P significance agrees in both rows. A distinct fresh pass-2 rechecker reproduced expanded C012, including all witness relationships and both affected outcomes.
**Exact source locations:** DOC-004 [p6 glucose12/24, TG12, HDL12, LDL12, hsCRP12 and adjustment footnote](../../joi240048supp3_prod_1727199125.83025.pdf#page=6), [p5 WOMAC total4/8/12/16/20/24](../../joi240048supp3_prod_1727199125.83025.pdf#page=5); DOC-001 [p6 WOMAC total24 and glucose24 corroboration](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), [p4 model methods](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p7 model continuation](../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7).
**Classification rationale:** Each conflicting interval and its reproducing rule are compared within its own REPORT display; S_W. Main/results WOMAC copies agree, so no conflicting S_C relationship is added. Model-method corroboration adds no relationship.
**Classification ambiguity:** Exact row-specific covariance and CI methods are absent.
**Human question:** What row-specific covariance, critical values or interval calculations produced glucose12 and WOMAC total24, and why do they not reproduce under the rule supporting adjacent metabolic rows and all five earlier total-pain rows?

## C013 — WORMS smaller-one-unit percentages differ from their counts

**Finding IDs:** F-NUM-103.
**Qualifying route:** Route A, category 3.
**Registration:** Krill 10/107 and placebo 16/109 are both printed 12%. Half-unit percentage envelopes [8.8372,9.8592] and [14.1553,15.2074] versus [11.5,12.5] leave relative gaps .1367/.1379. Counts sum to the displayed arm totals. One count/percentage pattern retains both arms.
**Exact source locations:** DOC-004 [p8 eTable 5 smaller-one-unit and totals](../../joi240048supp3_prod_1727199125.83025.pdf#page=8).
**Classification rationale:** Counts, percentages and denominators are in one REPORT display; S_W and statistical_results.
**Classification ambiguity:** None.
**Human question:** What numerator and denominator produce each smaller-one-unit percentage?
