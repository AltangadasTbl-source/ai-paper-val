# Numeric Consistency Review

## Scope and method

Complete independent review of N001--N051 in the fresh canonical inventory. I used only fresh DOC-001, DOC-002, and DOC-003 evidence assets and fresh mapping output; no legacy audit derivative, external source, or new OCR was used. Counts and denominators were recomputed; ordinary one-decimal rounding allowed 0.05 percentage points (pp). Planning values and versioned definitions were tested only in their printed scopes. Every row below is **COMPLETE**.

## Complete relationship coverage

| ID | Exact fresh source(s) checked | Check result |
|---|---|---|
| N001 | DOC-001 `jama_jabre_2018_oi_180004.pdf#page=1`, `#page=4` Figure | 1020+1023=2043; abstract and Figure agree. **PASS.** |
| N002 | DOC-001 `#page=1`, `#page=4` | 1018+1022=2040; 2040/2043=99.85%, compatible with 99.8%. **PASS.** |
| N003 | DOC-001 `#page=4` Figure | 1014+6=1020 BMV; 979+44=1023 ETI. **PASS.** |
| N004 | DOC-001 `#page=4` Figure | 1020−2=1018 and 1023−1=1022 ITT. **PASS.** |
| N005 | DOC-001 `#page=4` Figure | PP=995+943=1938; stated exclusion reasons may overlap, so components were not summed. **PASS.** |
| N006 | DOC-001 `#page=4` Figure | Safety=1028+999=2027; actual-treatment crossover label explains BMV 1028. **PASS.** |
| N007 | DOC-001 `#page=5` Table 1 | Activity=934/936; etiology=1014/1015; rhythm=1016/1020; all equal printed denominators. **PASS.** |
| N008 | DOC-001 `#page=5`; DOC-002 `joi180004supp1_prod.pdf#page=123` | Mapped Table 1 count/denominator percentages reproduce to one decimal; nonmissing denominators/rounding are stated. **PASS.** |
| N009 | DOC-001 `#page=1`, `#page=4`, `#page=6` | 44/1018=4.322%→4.3 and 43/1022=4.208%→4.2; CPC components 35+9 and 37+6 agree. **PASS.** |
| N010 | DOC-001 `#page=4`; DOC-002 `#page=124` | Post-hoc 0.05%, 97.5% CI −1.70 to infinity uses a centre-random-effect model; distinct from unadjusted result. **PASS.** |
| N011 | DOC-001 `#page=4`, `#page=6` | PP 43/995=4.322%, 40/943=4.242%; difference=0.080 pp, matching 0.08. **PASS.** |
| N012 | DOC-001 `#page=1`, `#page=4`, `#page=6` | 55/1018=5.403%, 54/1022=5.284%, difference=0.119 pp→0.1. **PASS.** |
| N013 | DOC-001 `#page=1`, `#page=4`, `#page=6` | 294/1018=28.880%, 333/1022=32.583%, difference=−3.703 pp→−3.7. **PASS.** |
| N014 | DOC-001 `#page=4`, `#page=6` | 348/1018=34.185%, 397/1022=38.845%, difference=−4.660 pp→−4.7. **PASS.** |
| N015 | DOC-001 `#page=6` Table 2 | ITT CPC sums: 35+9+4+7+963=1018; 37+6+7+4+968=1022. **PASS.** |
| N016 | DOC-001 `#page=6` Table 2 | 54/995=5.427%, 51/943=5.408%, raw difference=0.019 pp→0.0, versus printed 0.1. **SIGNAL NUM-CAND-002.** |
| N017 | DOC-001 `#page=6` Table 2 | PP CPC sums are 995 and 943; CPC 1+2 are 43 and 40. **PASS.** |
| N018 | DOC-001 `#page=6` Table 2 | 289/995=29.045%, 312/943=33.086%, difference=−4.041 pp→−4.0. **PASS.** |
| N019 | DOC-001 `#page=6` Table 2 | 377/943=39.979%→40.0, not printed 30.0; raw difference=−5.607 pp→−5.6. **SIGNAL NUM-CAND-001.** |
| N020 | DOC-001 `#page=6`; DOC-002 `#page=124-125` | Printed 0.1 (−10 to 9.7) pp retained; supplied CI rule does not establish a mechanical contradiction or intended decimal. **PASS—clarification note.** |
| N021 | DOC-001 `#page=1`, `#page=4`, `#page=6` | 186/1027=18.111%, 134/996=13.454%, difference=4.657 pp→4.7. **PASS.** |
| N022 | DOC-001 `#page=1`, `#page=4`, `#page=6` | 69/1028=6.712%, 21/996=2.108%, difference=4.604 pp→4.6. **PASS.** |
| N023 | DOC-001 `#page=1`, `#page=4`, `#page=6` | 156/1027=15.190%, 75/999=7.508%, difference=7.682 pp→7.7. **PASS.** |
| N024 | DOC-001 `#page=6` Table 3 | ETI n=999: 20=2.0%, 102=10.2%, 7=0.7%, 5=0.5%. **PASS.** |
| N025 | DOC-001 `#page=4` | Centre 5 ETI 87%, BMV 86%, BMV−ETI=−1 pp: direction and labels agree. **PASS.** |
| N026 | DOC-001 `#page=4` | “Number of pauses” 27 vs 16 gives difference 11, but difference/CI are labelled seconds. **SIGNAL NUM-CAND-003.** |
| N027 | DOC-001 `#page=3`, `#page=6`; DOC-002 `#page=101-105` | CPC, CCF, VAS, IDS, and Han labels/scales match reported measures. **PASS.** |
| N028 | DOC-001 `#page=1-4`; DOC-002 `#page=75`, `#page=123` | Day-28 estimand, 28–35-day ascertainment, and ITT/PP/safety populations remain distinct. **PASS.** |
| N029 | DOC-002 `#page=9`, `#page=15`, `#page=17` | Day-28 survival plus CPC≤2 definition is internally coherent. **PASS.** |
| N030 | DOC-002 `#page=9-10`, `#page=15-16` | Secondary endpoints/failure components correctly distinguish binary, duration, and scale measures. **PASS.** |
| N031 | DOC-002 `#page=10`, `#page=24`, `#page=65` | 20×100=2000; 5/centre/month is a rounded expectation, not an actual-total claim. **PASS.** |
| N032 | DOC-002 `#page=10`, `#page=17` | Eligibility/exclusion and blocked centre-stratified randomization have no conflicting reported total. **PASS.** |
| N033 | DOC-002 `#page=20-21`, `#page=32` | Day-28 status and +7-day ascertainment window are compatible. **PASS.** |
| N034 | DOC-002 `#page=24`, `#page=50` | mRS 0–6; 6=dead. **PASS.** |
| N035 | DOC-002 `#page=51` | CPC 1–5; CPC 1–2 favourable. **PASS.** |
| N036 | DOC-002 `#page=52` fresh rendered/OCR asset | IDS=N1+N2+N3+N4+N5+N6+N7; category/infinity labels coherent. **PASS.** |
| N037 | DOC-002 `#page=53-54` | VAS 0–100 and Han 0–4 are distinct nonpercentage scales. **PASS.** |
| N038 | DOC-002 `#page=21`, `#page=32-33` | Broad CRF timing wording does not state an incompatible observed result or time. **PASS.** |
| N039 | DOC-002 `#page=57-66`, `#page=9-11` | Revised protocol repeats planned endpoint/target/CI/sample-size quantities. **PASS.** |
| N040 | DOC-002 `#page=64-65`, `#page=9-10` | Added endpoint/sign definitions are version changes, not same-population numeric conflicts. **PASS.** |
| N041 | DOC-002 `#page=70`, `#page=71`, `#page=122` | Primary day-28 CPC≤2 definition matches across supplied protocol/SAP. **PASS.** |
| N042 | DOC-002 `#page=92`, `#page=120` | 956/arm, 2000, 3%/2%, 1%, .8, .025 are planning inputs, not actual results. **PASS.** |
| N043 | DOC-002 `#page=91`, `#page=121`, `#page=124`; DOC-001 `#page=1`, `#page=4` | Lower CI must exceed −1%; main lower −1.64% does not. Scale/label coherent. **PASS.** |
| N044 | DOC-003 `joi180004supp2_prod.pdf#page=2` | 21 BMV centre counts=1018 and ETI centre counts=1022. **PASS.** |
| N045 | DOC-003 `#page=2` | All 42 count/arm-denominator percentages reproduce to one decimal. **PASS.** |
| N046 | DOC-003 `#page=3` | 43/971=4.428%→4.4; 39/978=3.988%→4.0; difference=.440 pp→.4; CI contains estimate/zero. **PASS.** |
| N047 | DOC-003 `#page=3` | 41/863=4.751%→4.8; 45/1174=3.833%→3.8; difference=.918 pp→.9; CI contains estimate/zero. **PASS.** |
| N048 | DOC-002 `#page=104`; DOC-001 `#page=6` | VAS 0–100; 20 (IQR 5–55) mm is in range. **PASS.** |
| N049 | DOC-002 `#page=103`; DOC-001 `#page=6` | IDS sum/infinity/bands match main range 0–infinity. **PASS.** |
| N050 | DOC-002 `#page=101-102` | mRS 0–6 and CPC 1–5 are not conflated. **PASS.** |
| N051 | DOC-002 `#page=110-116` | Versioned complications/failure definitions are not a matched-final-result conflict. **PASS.** |

## Candidate signals requiring human adjudication

### NUM-CAND-001 — PP ROSC ETI percentage does not reconcile

- **Exact source/comparator:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=6`, Table 2, PP “Return of spontaneous circulation”: BMV `342 (34.4)` of n=995; ETI `377 (30.0)` of n=943; BMV−ETI `−5.6 (−9.9 to −1.3)`.
- **Direct observation and rule:** The ETI count and denominator print in the same row. (100×377/943=39.979%→40.0%), not 30.0%; (100×342/995−100×377/943=−5.607) pp→−5.6 pp.
- **Tolerance:** 9.979 pp from the printed ETI percentage, exceeding 0.05 pp.
- **Alternative:** An unprinted denominator near 1257 would yield 30.0%, but none is shown. “40.0” is a possible correction, not an adjudication.
- **Quality-control relevance:** The rate, denominator, and contrast in a secondary-outcome row cannot all be true.
- **Human question:** Should ETI read 377 (40.0%), or does another supplied source establish a different denominator/value?

### NUM-CAND-002 — PP day-28-survival point difference does not round from printed raw inputs

- **Exact source/comparator:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=6`, Table 2, PP “Survival at 28 d”: BMV `54 (5.4)` of n=995; ETI `51 (5.4)` of n=943; printed BMV−ETI difference `0.1`.
- **Direct observation and rule:** The header defines a percentage contrast. (100×(54/995−51/943)=0.019) pp, which rounds to 0.0 pp at one decimal rather than 0.1 pp.
- **Tolerance:** 0.081 pp, exceeding 0.05 pp. The confidence interval is not recalculated because its exact procedure is not fully reproducible from the display.
- **Alternative:** An unprinted estimator, data handling method, or denominator could explain 0.1, but none is printed.
- **Quality-control relevance:** The table's displayed proportion difference is unsupported by its displayed counts/denominators.
- **Human question:** Which estimator/denominator produced 0.1 pp, or should it round to 0.0 pp?

### NUM-CAND-003 — Centre-5 pause contrast pairs a count outcome with a time unit

- **Exact source/comparator:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=4`, Post-Hoc Analyses: “number of pauses greater than 2 seconds during CPR,” BMV 27 versus ETI 16, “difference, 11 seconds [95% CI, 7 to 15].”
- **Direct observation and rule:** 27−16=11 is a difference in counts of pauses. Seconds is the threshold used to define the counted pauses, not the unit for a count.
- **Tolerance:** Not applicable; this is a measure/unit-label check.
- **Alternative:** 27 and 16 might be unreported time summaries, but that conflicts with the explicit “number of pauses” wording.
- **Quality-control relevance:** A count-versus-duration label can cause an incorrect effect measure/unit to be extracted.
- **Human question:** Are 27 and 16 pause counts (requiring a count-unit difference/CI), or time quantities (requiring a revised outcome description)?

## Limitations and counts

No model-dependent CI, P value, median/IQR, or unprinted data-handling computation was reconstructed. N020’s PP-survival CI text is preserved as a clarification note because the supplied sources do not mechanically establish its intended scale.

**Coverage:** 51/51 COMPLETE. **Candidate signals:** 3. **PASS/no qualifying candidate:** 48.
