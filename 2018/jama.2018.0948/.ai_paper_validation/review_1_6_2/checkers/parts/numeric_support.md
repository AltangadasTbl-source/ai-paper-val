# Support numeric consistency checker

Runtime ID: 01a129b8-0e37-7521-8c6c-85aed6ede96e. Optional disjoint numeric shard, gpt-6.1-sol / medium, fresh spawn. Scope: all internal numeric relationships DOC-002 pp. 1–37 (PLAN), DOC-003 pp. 1–7 (PLAN), DOC-004 pp. 1–14 (REPORT), grouped in 93 records N080–N172 in relationships/parts/numeric_support_inventory.md. Main article relationships and source-to-source matching are separately assigned. Statistical inferential compatibility and printed SAP implementation are assigned to statistical specialists. Read QUALITY_CONTROL_SCOPE.md and review_contract.md completely; used current source-linked mapper evidence and targeted direct source extraction, no legacy scientific conclusion or external evidence.

## Methods and complete check coverage

Direct tools: Poppler pdftotext 25.03.0 layout extraction of DOC-004 pp. 1–7 and 8–14, DOC-003 pp. 1–7, DOC-002 pp. 14–15 and 29–30. Derivatives: preprocessing/numeric-support-results-p1-7.txt, preprocessing/numeric-support-results-p8-14.txt, preprocessing/numeric-support-sap.txt, preprocessing/numeric-support-protocol-p14-15.txt, preprocessing/numeric-support-protocol-p29-30.txt. Direct visual confirmation of DOC-002 p. 29 used Poppler pdftoppm 25.03.0, CPU, 100 dpi, preprocessing/numeric-support-protocol-p29.png. The package tooling record establishes native text and rendering available; no OCR, fallback interpreter, source modification, or reused-asset modification occurred.

All 21 hospital rows and both arm totals in eTable 2 and eTable 3 were checked. Exact eTable 2 totals reproduced:
- PEWS discharges 26664/50173/76837; mortality 52/97; non-DNR mortality 26/42.
- Usual care discharges 46718/94366/141084; mortality 61/147; non-DNR mortality 16/47.
- Every hospital baseline+post discharge count equals its printed total; every mortality count/rate reconciles; non-DNR counts never exceed total deaths.

Exact eTable 3 totals reproduced:
- PEWS patient-days 129700/251859; deterioration 80/127; arrest 15/27; potentially preventable arrest 11/21.
- Usual care patient-days 162497/307584; deterioration 144/259; arrest 18/32; potentially preventable arrest 12/29.
- All six event-rate cells per hospital and per total satisfy half-unit precision; potentially preventable arrest ≤ arrest ≤ deterioration in both periods.

eTable 4: patient denominators 393/686/531/967; every mortality, predicted mortality and technology-use count/percentage checked in all four groups; all 15 effect identities agree with linear mean-difference or binomial identity risk-difference methods. Four median/IQR rows, all mean/SD summaries, ICU aggregation, VFD 0–28 and PELOD 0–71 ranges checked. All point estimates lie within properly ordered 95% intervals; inferential compatibility reviewed independently by the statistical agents. No crude-column subtraction was used to dispute adjusted effects.

eTable 5: anticipated deaths 99389×5.1/1000 = 506.8839 → 507; anticipated deterioration events 397556×2/1000 = 795.112 → 795. Actual 244/144539×1000 = 1.68813 → 1.7 and 386/559443×1000 = 0.689972 → .69. Actual discharges 50173+94366 = 144539; actual patient-days 251859+307584 = 559443; actual events 97+147 = 244 and 127+259 = 386. Coefficient/standard-deviation comparison satisfies half-unit intervals, as detailed in N170. Figure documentation caption 2588+2832 = 5420; hospital identifiers 10+11 = 21. No exact histogram frequencies were fabricated from unlabeled bars.

Protocol: all current support map quantities reviewed; 686+1388 = 2074 historical validation patients; 14 historical hospital mortality rates average 5.10643 → 5.11; 397556/99389 = 4 days LOS; .31×2 = .62 SCDE reduction; .41×.75 = .3075 → .3 code-blue reduction. Statistical agents own sample-size model reproduction and planned-versus-reported design comparisons. One reproduced protocol numeric inconsistency remains below.

## Findings

### F-NUM-101

**Title:** Protocol mortality absolute reduction printed as 0.9% in the appendix versus 0.09% in the power specification.

**Relationship inventory:** N087.  
**Compared locations and roles:** PLAN DOC-002 [PDF p. 29, Power & Sample Size Appendix, all-cause mortality paragraph](../../../../joi180015supp1_prod.pdf#page=29); PLAN DOC-002 [PDF p. 14, section 2.11 Sample size and assumptions](../../../../joi180015supp1_prod.pdf#page=14); PLAN DOC-002 [PDF p. 1, mortality power summary](../../../../joi180015supp1_prod.pdf#page=1). Both compared locations are prospective PLAN content. Within one protocol, provisional relationship type P_P; all relationships P_P; proposed review domain plan_material. No classification ambiguity.

**Printed inputs:** Appendix p. 29: 18% relative risk reduction corresponds to absolute risk reduction 0.9%; same page baseline 5.1 deaths/1000 discharges. Section 2.11 p. 14: 18% relative risk reduction, absolute risk reduction 0.09%, baseline 5.1/1000. Summary p. 1 uses 0.9 deaths/1000 admissions, corroborating the smaller percentage scale. Shared inputs are 20-hospital power base, alpha .05 and power 80%.

**Rule and calculation:** Convert deaths per thousand to a percentage, then multiply by relative reduction. 5.1×.18/10 = .0918% absolute reduction. With printed baseline half-unit [5.05,5.15]/1000 and relative reduction [17.5%,18.5%], the recomputed absolute-percentage interval is [.088375%,.095275%]. Printed .9% has half-unit interval [.85%,.95%]; minimum gap = .85−.095275 = .754725 percentage points; relative discrepancy = .754725/.9 = .8385833, above .05. For the two printed percentage copies, .09% has interval [.085%,.095%], so minimum gap to .9% is .755 percentage points, relative discrepancy .755/.9 = .8388889. The appendix absolute reduction also exceeds its stated baseline risk .51%, establishing the differing magnitude independently.

**Focus area:** D, power assumptions for primary hospital mortality.  
**Qualifying route:** Route A, category 2.  
**Affected result or extracted value:** The absolute mortality reduction underlying the planned primary-outcome power calculation: a reader may extract .9% from the appendix or .09% from the main power specification.  
**Why context does not resolve it:** Route A category 2 applies to the reproduced decimal/scale discrepancy that changes the printed magnitude. The smaller percentage is reconstructible, but the explicitly printed appendix quantity remains a distinct extractable power input.  
**Alternative interpretations:** The appendix may intend .9 deaths per thousand (approximately .09%) while displaying a percent sign, or may intend a different absolute-reduction scenario. The latter does not reconcile with the same paragraph’s 18% relative reduction and the printed baseline mortality. No different scenario or amendment is disclosed there.  
**Exact human question:** Which absolute mortality reduction was intended for the appendix’s 18% power scenario, and how should the printed .9% be reconciled with .09% in section 2.11 and .9 deaths per thousand in the summary?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 p.11, eTable 3, low event-rate cells: E post arrest/PP; F post PP; H post arrest and baseline/post PP; I baseline arrest and baseline/post PP; J baseline/post arrest and baseline/post PP; O baseline arrest/PP and post PP; Q baseline PP; T baseline PP | Some crude relative differences from two-decimal rates exceed .05 before allowing displayed precision. Every exact quotient falls within its printed rate’s ±.005 interval; half-unit input intervals broaden this overlap. Examples 1/17779×1000=.056246 lies within .06±.005; 1/28698×1000=.034846 lies within .03±.005. Remaining discrepancy zero. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 p.30, Stat Calls power paragraph | 8.13×.181=1.47153 versus printed1.45. Half-unit product interval[1.4665625,1.4765025], output[1.445,1.455], gap.0115625; relative gap.00797414≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-004 pp.7,13, PIM2 upper illustrative probability | Inverse-logit(+9.7778)×100 = 99.99433072% versus99.9%. The rounded input interval gives approximately[99.99433044%,99.99433100%]; output[99.85%,99.95%]; gap .04433044/99.9 = .00044375≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 p.30, Code Blue power paragraph | Wording repeats the per-thousand scale in “0.3/1000 events per thousand patient days”; printed .75 rate and .41 reduction immediately determine about .3 events/1000. The arithmetic and intended scale are clear. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-004 p.12, eTable 4 exclusion caption | 55(3.2%) has no explicit percentage denominator. Using the post-period population before exclusion,1653+55=1708, yields3.22014%. Assuming all baseline+post patients instead would be unsupported; no printed denominator conflicts. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-004 pp.12–13, eTable 4 effect column | Several adjusted differences differ from crude descriptive-column subtraction (for example total ICU LOS9.4−9.0=.4 versus1.28). Hospital-baseline-adjusted GEE is explicitly used; no effect is stated crude. | MODEL_VERSUS_CRUDE |
| REPORT DOC-004 p.11, eTable 3 PEWS baseline deterioration total | Additional glyph after80 does not alter the count: individual rows sum80 and80/129700×1000=.616808 rounds.62; typography makes the numeric reading clear. | NOTATION_OR_TYPOGRAPHY |

## Completion and limitations

93 support relationships complete, 1 finding, 7 excluded-observation patterns. No scientific coverage limitation. Raw patient records and fitted GEE output are not supplied; this limits reproduction of model-based means/effects but does not prevent checking all supplied numeric relationships. Figure bars are unlabeled; only truthful approximate visual values from the current map were used as context. Candidate IDs and human adjudication are reserved to downstream stages.

