# Statistical pass 2 — tables B

Fresh runtime: root/stat2_tables_b; model gpt-6.1-sol; reasoning effort high; FRESH_SPAWN. This agent is independent of all pass-1 agents. Complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read. The full current candidate ledger, full exact-source evidence recheck and complete initial screening decision/justification handoff were read before review.

Exact disjoint scope: 66 inferential relationships S5001–S5066, REPORT results supplement eTables8–10 at physical PDF pp45–50 and eTable12 at physical p52. This agent owns statistics/parts/tables_b.md and this checker part; it does not update the inherited tables_b_plan.md or disjoint plan_methods.md. Inherited first-pass evidence is preserved, with fresh per-record reasoning and PASS_2_COMPLETE added to every assigned record. Sources and reused artifacts remain unchanged.

**Completion:** 66/66 relationships independently revisited; 44 estimate/interval pairs and 22 P-value relationships. Every record retains PASS_1_COMPLETE and now records PASS_2_COMPLETE. New findings: 0. Excluded-observation rows: 5. The existing C018 pattern is reproduced and retained without re-emission. All stable candidates remain Pending Human Adjudication.

## Exact source confirmation and inferential checks

Final authority was direct source PDF-native layout extraction, not copied checker values:

- [Results p45: eTable8 ordinal, independence and first ambulation row](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45).
- [Results p46: eTable8 ambulation continuation and adverse outcomes](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46).
- [Results p47: eTable9 ordinal, independence, ambulation and concordant adverse row](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47).
- [Results p48: eTable9 adverse continuation](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=48).
- [Results p49: eTable10 ordinal, independence, ambulation and concordant adverse row](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49).
- [Results p50: eTable10 adverse continuation](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=50).
- [Results p52: eTable12 four growth/outcome tests](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=52).
- REPORT [main p4](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4) and PLAN [analysis-specific SAP pp3–5](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=3) establish analysis-population, modified-Poisson/PIM, predicted-margins, exploratory and confidence/test context.

The 44 printed estimates are all inside their intervals, and every pair has ordered endpoints. Ratios use null1; risk differences use null0. Both favorable and adverse outcomes use the explicitly identified contrast. eTable8 compares imaging profiles with the concordant reference within each received-treatment arm; eTables9/10 compare randomized EVT versus MM within imaging profiles. These contrasts cannot be interchanged. C002 retains the planned-versus-reported treatment-allocation specification; C003 retains composite-core primary/prespecified versus sensitivity/post-hoc hierarchy. Neither issue permits replacing coherent printed estimates with crude calculations.

All 18 last-column P values in eTables8–10 are explicitly interaction tests. An individual effect interval excluding1 beside a nonsignificant interaction P is not an interval-versus-own-test conflict. No interaction coefficient/interval, pooled-model covariance or test statistic is supplied; independent-arm tests are not inferred. The main article states two-sided tests and .05 significance, but this does not supply the absent interaction covariance or test implementation.

eTable10 D1 ordinal OR1.80(1.00–3.22) has no paired own-effect P or significant-own-effect statement. The .61 is an interaction P. A printed endpoint at1 therefore does not itself establish a Route A category1 observation. No noninferiority/equivalence margin, multiplicity correction or stopping rule applies to these exploratory table effects; the supplied main methods explicitly state no multiplicity adjustment.

**Diagnostic center check:** For all 44 estimate/interval pairs, ratio geometric centers and risk-difference arithmetic centers were checked using half-unit intervals for every displayed estimate and endpoint. Every resulting center interval overlaps the printed estimate interval; gap0 and relative discrepancy0. These are diagnostic symmetry checks, not assertions of the actual CI construction. No source-supported reproducing method yields a greater-than-.05 discrepancy here. No standard error, degrees of freedom or own-effect P was inferred from these diagnostic centers.

## Complete-ledger and recheck implications

C018's disjoint-count pattern survives direct source rereading. eTable9 MM D2 has ambulation3/11 and adverse10/11, so3+10=13>11. eTable10 MM D2 has ambulation4/12 and adverse11/12, and independence2/12 and adverse11/12, giving15>12 and13>12. Printed percentage-sum intervals[118.1,118.3], [124.9,125.1] and[108.3,108.5]% against conservatively permitted100±.5 yield relative minimum gaps.176,.244,.078, each above.05. CTP/MRI favorable-event attribution also differs: eTable8 EVT1/12 and3/12, MM0/11, versus eTable9 MM1/11 and3/11, EVT0/12. C018 already includes all affected pp45–50 and the corroborating eFigure20x distribution. Its reproduced evidence state and statistical_results/S_W classification reconcile with these facts. No fitted effect or original arm allocation is selected as a replacement.

Ordinal D2 ORs2.46 and2.66 can indicate shifts within poor ordinal categories even when favorable-threshold events are scarce; this is not independently contradictory. The reproduced C018 count issue leaves the exact source data/model mapping a human question and does not identify amended adjusted estimates or interaction Ps.

Three eTable8 EVT RR/RD point-direction reversals are directly printed:
- D2 independence RR.85(.12–5.79) versus RD+.010(−.395,.415).
- D1 ambulation RR.86(.43–1.71) versus RD+.043(−.125,.211).
- D2 ambulation RR1.19(.43–3.28) versus RD−.065(−.421,.291).

For a single common positive risk pair, the RR−1 and RD signs agree. However, neither the main methods nor specific SAP supplies a shared fitted-risk pair, a standardization rule, RD derivation, or common confidence construction. Similar regression-model language does not establish that identity, and the specific SAP permits a different calibrated model for marginal probability plots. Thus no common-risk identity is inferred for these separately labeled adjusted quantities. Both intervals contain their own nulls in all three reversals. The MM D1 adverse RR.69(.49–.97)/RD−.076(−.248,.096) has differing null inclusion but no own-effect P and no common confidence transformation. The complete F-ST1-401 decision addresses this same distinction between different adjusted scales and an actual interval-versus-own-test conflict; it is preserved without re-emission. A mapping-only concern remains conditional, rather than an established contradiction.

eTable12 groups290+46 and240+96 each sum to336; all displayed medians lie within ordered IQRs. Larger growth in unfavorable functional groups agrees with the reported direction. IQRs are outcome distribution intervals, not confidence intervals for a tested difference. Their overlap does not contradict P<.001. Summary quantiles and group counts do not supply full ranks, actual test statistic or variance needed to reproduce numerical Ps.

All other ledger candidates and recheck classifications were read for implications. C015's corrected PLAN-only P_P classification and C011/C012's historical-PLAN ambiguity introduce no additional conflict in the current REPORT table scope. Uncovered plan-method relationships remain assigned to the separate fresh plan-method pass-2 agent.

## New findings

None. No F-ST2 ID is assigned to a check that reconciles or to an already screened observation.

## Excluded observations

These rows consolidate apparent issues considered and not newly emitted; reconciled routine checks remain in the per-S records.

| Location | Observation | Reason code |
|---|---|---|
| REPORT eTable8 pp45–46, S5001–S5024 | Adjusted effects differ from crude profile comparisons, notably EVT D1 independence adjustedRR.51 versus crude(21/76)/(10/75)=2.072. Source labels adjustment; no source-defined crude reproduction of other adjusted rows is established. | MODEL_VERSUS_CRUDE |
| REPORT eTables8–10 pp45–50, S5025–S5030,S5041–S5046,S5057–S5062 | Apparent effect-CI versus last-column-P conflicts pair individual treatment/profile effects with explicitly different interaction tests. Rereading headings does not reproduce an own-analysis interval/test conflict. | NOT_REPRODUCED |
| REPORT eTable8 pp45–46, S5009–S5012,S5015–S5016,S5019–S5020 | Opposing RR/RD point directions and differing null-inclusion readings require a common fitted-risk/CI mapping absent from the source; no own-effect P, shared estimand construction or same-display reproducing method establishes that mapping. | CONDITIONAL_OR_UNREPORTED |
| REPORT eTable12 p52, S5063–S5066 | Reconstructing P<.001 from medians/IQRs alone requires absent ranks/test output; distribution IQRs do not supply a matched effect CI or contradiction. | CONDITIONAL_OR_UNREPORTED |
| REPORT eTables8–10 pp45–50, concordant/discordant D2 favorable and adverse counts; S5003–S5004,S5009–S5010,S5015–S5016,S5021–S5024,S5033,S5040,S5049,S5056 and their associated interaction/context records | Disjoint MM outcome counts and competing favorable-event arm attribution reproduce the exact pattern already screened INCLUDE and registered as C018; all affected locations remain in that candidate. | DUPLICATE_OF_INCLUDED |

The three pertinent pass1_tables_b_plan exclusion rows were reread against exact source and the Route A catalogue. MODEL_VERSUS_CRUDE remains applicable; no mislabeled crude-effect claim or reproducing method was found. The apparent interaction/individual interval conflict remains NOT_REPRODUCED. The eTable12 numerical-P reconstruction remains conditional because no contradictory test/CI/statistic is supplied. The additional RR/RD review above does not infer the absent covariance/estimand mapping.

## Limitations and provenance

No scientific-coverage gap remains in the assigned66 records. Exact adjusted fits, confidence/test implementations, interaction covariance and eTable12 ranks are unavailable; they are named limits of numerical reconstruction, not inferred contradictions. Current-source direct text sufficed; no persistent derivative or duplicate rendering was created.

CPU; Poppler pdftotext26.01.0, as recorded in tooling_record.md. Commands:
```text
pdftotext -layout -f 45 -l 52 joi240006supp5_prod_1708623115.01733.pdf -
pdftotext -layout -f 4 -l 4 jama_sarraj_2024_oi_240006_1708623114.96234.pdf -
pdftotext -layout -f 3 -l 5 joi240006supp4_prod_1708623115.00733.pdf -
```

Per-record output: statistics/parts/tables_b.md. Checker output: checkers/statistical_parts/pass2_tables_b.md. These parts are ready for the coordinator's canonical merge.


## Complete agent-authored per-relationship record

The coordinator mechanically copied the fresh reviewer's 66 current inventory records below to make every S ID and second-pass reasoning explicit in this checker artifact. No scientific text or value was changed.

### S5001 — eTable8 ordinal D1 EVT

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 0.91 (0.50,1.65)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms OR0.91 inside[.50,1.65], including1; D1-versus-concordant within EVT differs from across-arm treatment effects. No own-effect P; C002 supplies the population context.

### S5002 — eTable8 ordinal D1 MM

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.50 (0.94,2.40)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms OR1.50 inside[.94,2.40], including1; MM within-arm D1 contrast has no own-effect P. Interaction.20 tests effect modification rather than this coefficient.

### S5003 — eTable8 ordinal D2 EVT

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.01 (0.53,1.92)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms OR1.01 inside[.53,1.92], including1. D2 EVT ordinal effect can coexist with sparse favorable binary counts; C018 identifies separately conflicting cross-table attribution.

### S5004 — eTable8 ordinal D2 MM

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 0.65 (0.43,0.99)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms OR.65 inside[.43,.99], excluding1 toward worse D2 MM outcome. Interaction.26 is not its own-effect P; MM6(6,6) supplies descriptive context, not an effect CI.

### S5005 — eTable8 mRS0–2 D1 EVT RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.51 (0.16,1.56)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR.51 inside[.16,1.56], including1. Adjusted profile effect need not equal crude(21/76)/(10/75)=2.072; no method reproducing these adjusted rows from crude counts is established.

### S5006 — eTable8 mRS0–2 D1 EVT RD

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.055 (−0.201,0.092)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RD−.055 inside[−.201,.092], including0; its sign agrees with paired adjusted RR.51. Do not replace adjustment with observed28%−13%=15 percentage points.

### S5007 — eTable8 mRS0–2 D1 MM RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.26 (0.17,9.43)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR1.26 inside[.17,9.43], including1; positive adjusted D1 MM direction agrees with paired RD+.040. No matched own-effect test printed.

### S5008 — eTable8 mRS0–2 D1 MM RD

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.040 (−0.059,0.138)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RD+.040 inside[−.059,.138], including0; same direction as RR1.26. Exact confidence/test reconstruction needs the absent fit and variance output.

### S5009 — eTable8 mRS0–2 D2 EVT RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.85 (0.12,5.79)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR.85 inside[.12,5.79], including1; paired RD+.010 points oppositely. No shared fitted-risk pair, standardization or RD derivation is supplied, so a common-risk identity is not assumed.

### S5010 — eTable8 mRS0–2 D2 EVT RD

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.010 (−0.395,0.415)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RD+.010 inside[−.395,.415], including0; paired RR.85 reverses point direction. The observed count1/12 remains separate from an adjusted estimand; missing RR/RD mapping is recorded without a new finding.

### S5011 — eTable8 mRS0–3 D1 EVT RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.86 (0.43,1.71)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR.86 inside[.43,1.71], including1; paired RD+.043 on p46 reverses point direction. A shared fitted-risk identity is absent and cannot be inferred from similar-model wording.

### S5012 — eTable8 mRS0–3 D1 EVT RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.043 (−0.125,0.211)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD+.043 inside[−.125,.211], including0; opposite paired RR.86 direction is the same conditional mapping observation, consolidated in the pass-2 exclusion table.

### S5013 — eTable8 mRS0–3 D1 MM RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.24 (0.38,4.07)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR1.24 inside[.38,4.07], including1; positive direction agrees with RD+.060. MM19/63 and8/82 are descriptive risks, not replacements for the adjusted estimate.

### S5014 — eTable8 mRS0–3 D1 MM RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.060 (−0.075,0.196)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD+.060 inside[−.075,.196], including0, agreeing in direction with RR1.24. Interaction.72 is a distinct contrast; no interval/test conflict is reproduced.

### S5015 — eTable8 mRS0–3 D2 EVT RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.19 (0.43,3.28)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR1.19 inside[.43,3.28], including1; paired RD−.065 reverses point direction. Source supplies no common RR/RD risk pair or transformation, so conditional identity is not promoted.

### S5016 — eTable8 mRS0–3 D2 EVT RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.065 (−0.421,0.291)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD−.065 inside[−.421,.291], including0. Paired RR1.19 has opposing direction; the same missing-model-mapping observation is consolidated once.

### S5017 — eTable8 mRS5–6 D1 EVT RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.92 (0.57,1.48)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR.92 inside[.57,1.48], including1; lower adjusted D1 EVT adverse risk agrees with RD−.077. The25/76 crude proportion does not identify the adjusted risk.

### S5018 — eTable8 mRS5–6 D1 EVT RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.077 (−0.244,0.091)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD−.077 inside[−.244,.091], including0 and agreeing with RR.92 direction. Effect-adjustment and own-effect variance remain unavailable.

### S5019 — eTable8 mRS5–6 D1 MM RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.69 (0.49,0.97)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR.69 inside[.49,.97], excluding1; paired RD−.076 includes0. Distinct adjusted scales/confidence constructions do not supply a matched interval-versus-own-test conflict under the complete screening rationale.

### S5020 — eTable8 mRS5–6 D1 MM RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.076 (−0.248,0.096)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD−.076 inside[−.248,.096], including0. Paired RR.69 is directionally concordant but has different null inclusion; no shared confidence transform or own-effect P establishes a contradiction.

### S5021 — eTable8 mRS5–6 D2 EVT RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.08 (0.69,1.68)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR1.08 inside[.69,1.68], including1; positive direction agrees with RD+.143. D2 EVT8/12 adverse and3/12 ambulation do not exceed12.

### S5022 — eTable8 mRS5–6 D2 EVT RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.143 (−0.212,0.498)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD+.143 inside[−.212,.498], including0; agrees with RR1.08 direction. Exact regression reconstruction requires absent covariate rows/fitted probabilities.

### S5023 — eTable8 mRS5–6 D2 MM RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.28 (1.01,1.63)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR1.28 inside[1.01,1.63], excluding1 toward greater D2 MM adverse risk. Paired RD+.324 excludes0 consistently; interaction.02 is separately defined.

### S5024 — eTable8 mRS5–6 D2 MM RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.324 (0.165,0.483)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD+.324 inside[.165,.483], excluding0 in the same direction as RR1.28. eTable8 MM10/11 adverse plus0/11 favorable reconciles internally; C018 concerns competing eTables9/10 copies.

### S5025 — eTable8 interaction ordinal D1

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.20
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 identifies P=.20 as D1 ordinal treatment interaction. It is not the test for OR.91 or1.50; absent interaction covariance/coefficient prevents exact P reconstruction.

### S5026 — eTable8 interaction ordinal D2

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.26
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 identifies P=.26 as D2 ordinal treatment interaction, not the test for MM OR.65 excluding1. No interaction interval is printed to form its own interval/test conflict.

### S5027 — eTable8 interaction mRS0–2 D1

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.78
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 identifies P=.78 as D1 functional-independence interaction, not an individual EVT/MM profile effect P. No test statistic or covariance supplies an exact numerical comparison.

### S5028 — eTable8 interaction mRS0–3 D1

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.72
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 identifies P=.72 as D1 ambulation interaction. The different point directions in RR/RD do not establish an interaction coefficient; no own interaction CI is supplied.

### S5029 — eTable8 interaction mRS5–6 D1

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.14
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 identifies P=.14 as D1 mRS5–6 interaction. An MM RR CI below1 beside.14 is a different contrast, so the apparent interval/P conflict is not reproduced.

### S5030 — eTable8 interaction mRS5–6 D2

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.02
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 identifies P=.02 as D2 mRS5–6 interaction. It is significant at the main stated.05 level but no own interaction CI/statistic permits further numerical compatibility reproduction.

### S5031 — eTable9 ordinal concordant

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.60 (1.18,2.18)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms OR1.60 inside[1.18,2.18], excluding1 toward better EVT ordinal outcome. Randomized within-profile comparison is distinct from eTable8 as-treated within-arm contrast, with C002 retained.

### S5032 — eTable9 ordinal D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.87 (1.28,2.74)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms OR1.87 inside[1.28,2.74], excluding1; P=.66 belongs to D1 interaction rather than this treatment contrast. Point containment/order and better-EVT direction reconcile.

### S5033 — eTable9 ordinal D2

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 2.46 (1.14,5.32)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms OR2.46 inside[1.14,5.32], excluding1. Better EVT ordinal outcome can involve shifts within poor categories despite printed zero favorable events; C018 retains the separate event-attribution issue.

### S5034 — eTable9 mRS0–2 concordant

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 4.62 (1.27,16.71)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR4.62 inside[1.27,16.71], excluding1 for EVT functional independence.10/74 versus3/83 is descriptive support; adjusted RR is not required to equal its crude ratio.

### S5035 — eTable9 mRS0–2 D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.68 (1.25,5.76)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR2.68 inside[1.25,5.76], excluding1 for D1 EVT functional independence; interaction.56 tests between-profile modification, not this effect.

### S5036 — eTable9 mRS0–3 concordant

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.98 (1.44,6.17)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR2.98 inside[1.44,6.17], excluding1 for concordant-profile EVT ambulation. No own-effect P or standard error is supplied; count-based crude replacement is unsupported.

### S5037 — eTable9 mRS0–3 D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.90 (1.29,2.78)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR1.90 inside[1.29,2.78], excluding1 for D1 EVT ambulation; interaction.38 is a separate contrast. Endpoint order and direction agree.

### S5038 — eTable9 mRS5–6 concordant

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.76 (0.61,0.95)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR.76 inside[.61,.95], excluding1 toward lower EVT adverse risk. C018's D2 mismatch does not justify a numerical replacement for this concordant adjusted estimate.

### S5039 — eTable9 mRS5–6 D1

- Location/role: [DOC-006 physical p48](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.72 (0.49,1.05)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p48 confirms RR.72 inside[.49,1.05], including1 for D1 adverse risk; interaction.83 is separately labeled. No same-effect statistical conclusion conflicts.

### S5040 — eTable9 mRS5–6 D2

- Location/role: [DOC-006 physical p48](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.59 (0.37,0.96)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p48 confirms RR.59 inside[.37,.96], excluding1 for D2 adverse risk; interaction.40 is not its own P. C018 recheck reproduces MM3+10>11 in this same profile but does not determine an amended fitted RR.

### S5041 — eTable9 interaction ordinal D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.66
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 identifies ordinal D1 interaction P=.66. Across-arm OR intervals cannot reconstruct it without pooled-model covariance; no explicit interaction statistic is supplied.

### S5042 — eTable9 interaction ordinal D2

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.18
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 identifies ordinal D2 interaction P=.18. The OR2.46 CI excluding1 tests a different effect, and C018 count issues do not supply an alternative interaction value.

### S5043 — eTable9 interaction mRS0–2 D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.56
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 identifies independence D1 interaction P=.56. It is not the test for RR2.68; no matched interaction interval, covariance or statistic is available.

### S5044 — eTable9 interaction mRS0–3 D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.38
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 identifies ambulation D1 interaction P=.38. It is not the test for RR1.90; no new interval/test conflict is reproduced.

### S5045 — eTable9 interaction mRS5–6 D1

- Location/role: [DOC-006 physical p48](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.83
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p48 identifies D1 adverse interaction P=.83; RR.72 is a within-D1 treatment effect. Both printed contrasts are distinct; covariance and exact test definition are absent.

### S5046 — eTable9 interaction mRS5–6 D2

- Location/role: [DOC-006 physical p48](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.40
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p48 identifies D2 adverse interaction P=.40, not the test for RR.59 whose CI excludes1. C018 is preserved without substituting count-derived interaction inference.

### S5047 — eTable10 ordinal concordant

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.65 (1.26,2.16)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms OR1.65 inside[1.26,2.16], excluding1 for concordant composite-profile EVT benefit. C003 addresses planned composite hierarchy; no additional estimate conflict is supplied.

### S5048 — eTable10 ordinal D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.80 (1.00,3.22)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms OR1.80 inside[1.00,3.22], containing printed null1. No own-effect P or significant narrative is paired with it, so this endpoint alone is not a category1 finding; interaction.61 is distinct.

### S5049 — eTable10 ordinal D2

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 2.66 (1.34,5.28)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms OR2.66 inside[1.34,5.28], excluding1. Composite D2 ordinal improvement remains possible within poor mRS categories; C018 concerns disjoint favorable/adverse counts, not this estimate's containment.

### S5050 — eTable10 mRS0–2 concordant

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.88 (1.34,6.20)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR2.88 inside[1.34,6.20], excluding1 for concordant composite-profile EVT independence; crude18/112 versus8/118 is not an adjusted-model reproduction.

### S5051 — eTable10 mRS0–2 D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 3.71 (0.93,14.82)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR3.71 inside[.93,14.82], including1 for composite D1 independence. No significant own-effect statement is printed, and interaction.71 is another contrast.

### S5052 — eTable10 mRS0–3 concordant

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.21 (1.41,3.48)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR2.21 inside[1.41,3.48], excluding1 for concordant composite-profile ambulation. C003 hierarchy provenance remains separate from the numerically coherent interval.

### S5053 — eTable10 mRS0–3 D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.83 (1.04,3.22)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR1.83 inside[1.04,3.22], excluding1 for composite D1 ambulation. P=.68 is the interaction and does not contradict this within-stratum interval.

### S5054 — eTable10 mRS5–6 concordant

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.75 (0.60,0.92)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR.75 inside[.60,.92], excluding1 toward lower concordant-profile EVT adverse risk. Count comparison is descriptive; no own-effect P, statistic or standard error printed.

### S5055 — eTable10 mRS5–6 D1

- Location/role: [DOC-006 physical p50](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.90 (0.52,1.56)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p50 confirms RR.90 inside[.52,1.56], including1 for composite D1 adverse risk. Interaction.92 is distinct; no matched test conflict.

### S5056 — eTable10 mRS5–6 D2

- Location/role: [DOC-006 physical p50](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.59 (0.39,0.88)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p50 confirms RR.59 inside[.39,.88], excluding1 for composite D2 adverse risk. Recheck C018 reproduces MM4+11>12 and2+11>12; this source count pattern is already screened and no fitted replacement is inferred.

### S5057 — eTable10 interaction ordinal D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.61
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 identifies composite ordinal D1 interaction P=.61; CI1.00–3.22 is for the within-D1 effect. No own interaction interval/statistic exists.

### S5058 — eTable10 interaction ordinal D2

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.13
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 identifies composite ordinal D2 interaction P=.13. CI1.34–5.28 is for the treatment effect, so the apparent interval/P mismatch uses different contrasts.

### S5059 — eTable10 interaction mRS0–2 D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.71
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 identifies composite independence D1 interaction P=.71. The RR3.71 interval is not an interaction interval; supplied summary values cannot reconstruct pooled covariance.

### S5060 — eTable10 interaction mRS0–3 D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.68
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 identifies composite ambulation D1 interaction P=.68, distinct from RR1.83 whose interval excludes1. No same-analysis interval/test conflict is reproduced.

### S5061 — eTable10 interaction mRS5–6 D1

- Location/role: [DOC-006 physical p50](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.92
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p50 identifies composite D1 adverse interaction P=.92. It is not the null test for RR.90; coefficient/covariance/test statistic remain absent.

### S5062 — eTable10 interaction mRS5–6 D2

- Location/role: [DOC-006 physical p50](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.38
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p50 identifies composite D2 adverse interaction P=.38, distinct from RR.59 whose interval excludes1. C018 counts remain registered without inventing their inferential effect.

### S5063 — eTable12 CTP/MRI growth by independence

- Location/role: [DOC-006 physical p52](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS3–6 N290:102(61–167); mRS0–2 N46:45(32–88); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p52 confirms290+46=336, medians102/45 inside ordered IQR61–167/32–88, and P<.001. The quantiles are IQRs, not effect CIs; ranks/statistic needed for exact P are absent.

### S5064 — eTable12 composite growth by independence

- Location/role: [DOC-006 physical p52](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS3–6 N290:77(31–127); mRS0–2 N46:23.5(11–48); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p52 confirms290+46=336, composite medians77/23.5 inside IQR31–127/11–48, P<.001. Direction agrees with greater growth in dependence; no CI/test pairing is supplied.

### S5065 — eTable12 CTP/MRI growth by ambulation

- Location/role: [DOC-006 physical p52](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS4–6 N240:110.5(65.5–174.5); mRS0–3 N96:65.5(32.5–100.5); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p52 confirms240+96=336, medians110.5/65.5 inside IQR65.5–174.5/32.5–100.5, P<.001. Overlap of IQRs does not contradict a between-group test.

### S5066 — eTable12 composite growth by ambulation

- Location/role: [DOC-006 physical p52](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS4–6 N240:85.5(36–144); mRS0–3 N96:31.5(10–67); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p52 confirms240+96=336, composite medians85.5/31.5 inside IQR36–144/10–67, P<.001. Full ranked data/test output is needed for numerical P reconstruction; no unsupported normal approximation is used.


