# Numeric Consistency Review

## Scope and method

Independent numeric review of canonical relationships N001--N098 in
`relationships/numeric_relationship_inventory.md`. Fresh native PDF text/layout
assets were checked for DOC-001, DOC-002, and DOC-003; the authorized existing
OCR transcription was used only where the inventory identifies it (DOC-002 p. 52).
No OCR was run, no old audit derivative was used as evidence, and no external
source was consulted. Percentages were recomputed as `100 x numerator / stated
denominator`; displayed one-decimal percentages/differences were allowed a
half-last-place tolerance of 0.05 percentage points (pp), subject to ordinary
rounding. Planning estimates, definitions, forms, and external-background
quantities were checked only against their stated scope and matching supplied
locations, rather than being treated as observed trial results.

Three candidate propositions are recorded below. They are pending human
adjudication; none has a stable candidate ID, severity, validity decision, or
disposition.

## Complete relationship coverage

| ID | Fresh source location and printed inputs checked | Check(s) and result |
|---|---|---|
| N001 | DOC-001 p. 1 and p. 4 Figure: 2043; 1020 BMV, 1023 ETI. | `1020 + 1023 = 2043`; checked, no candidate. |
| N002 | DOC-001 p. 1/p. 4: 2040; 1018 and 1022; 99.8%. | Sum and `2040/2043=99.85%`, compatible with 99.8%; no candidate. |
| N003 | DOC-001 pp. 1, 4, 6 Table 2: 44/1018 (4.3), 43/1022 (4.2), 0.11%. | Values give 4.322%, 4.208%, difference 0.114 pp; matched locations agree; no candidate. |
| N004 | DOC-001 pp. 1, 4, 6 Table 2: 55/1018 (5.4), 54/1022 (5.3), 0.1. | Values give 5.403%, 5.284%, difference 0.119 pp; no candidate. |
| N005 | DOC-001 pp. 1, 4, 6 Table 2: 294/1018 (28.9), 333/1022 (32.6), -3.7. | Values give 28.880%, 32.583%, difference -3.703 pp; no candidate. |
| N006 | DOC-001 pp. 4, 6 Table 2: 348/1018 (34.2), 397/1022 (38.9), -4.7. | Values give 34.185%, 38.845%, difference -4.660 pp; no candidate. |
| N007 | DOC-001 pp. 1, 4, 6 Table 3: 186/1027 (18.1), 134/996 (13.4), 4.7. | Values give 18.111%, 13.454%, difference 4.657 pp; no candidate. |
| N008 | DOC-001 pp. 1, 4, 6 Table 3: 69/1028 (6.7), 21/996 (2.1), 4.6. | Values give 6.712%, 2.108%, difference 4.604 pp; no candidate. |
| N009 | DOC-001 pp. 1, 4, 6 Table 3: 156/1027 (15.2), 75/999 (7.5), 7.7. | Values give 15.190%, 7.508%, difference 7.682 pp; no candidate. |
| N010 | DOC-001 p. 4 Figure: BMV 1020, received 1014, did not receive 6, ITT 1018, PP 995, safety 1028. | `1014+6=1020`; ITT and PP branches reconcile with stated non-overlap/overlap labels; no candidate. |
| N011 | DOC-001 p. 4 Figure: ETI 1023, received 979, did not receive 44, ITT 1022, PP 943, safety 999. | `979+44=1023`; downstream reasons are explicitly potentially overlapping; no candidate. |
| N012 | DOC-001 p. 4 Figure: actual-treatment safety 1028 BMV and 999 ETI. | `1028+999=2027`; the 14 crossover persons are assigned by actual treatment; no candidate. |
| N013 | DOC-001 p. 4 Figure: 146 rescue intubations, 55 failures, 100 regurgitations. | Figure says several reasons may apply; no impermissible person-total sum; no candidate. |
| N014 | DOC-001 p. 5 Table 1: ITT 1018/1022, sex and continuous baseline values. | Female percentages 332/1018=32.6% and 332/1022=32.5%; continuous units/labels preserved; no candidate. |
| N015 | DOC-001 p. 5 Table 1: 15 coexisting-condition rows. | Count/1018 or count/1022 checks are compatible with displayed one-decimal percentages; no candidate. |
| N016 | DOC-001 p. 5 Table 1: activity 492+255+115+72 and 528+254+91+63, denominators 934/936. | Both sums equal their row denominator; no candidate. |
| N017 | DOC-001 p. 5 Table 1: etiology totals under 1014/1015. | Category counts sum to their stated denominators and percentages are compatible with rounding; no candidate. |
| N018 | DOC-001 p. 5 Table 1: rhythm categories under 1016/1020. | Category counts sum to denominators and percentages are compatible with rounding; no candidate. |
| N019 | DOC-001 p. 5 Table 1: witness/CPR/EMS, drug/device/donation counts and time/dose summaries. | Count rows use the ITT denominators; median/IQR, minutes, mg, and percentage labels remain distinct; no candidate. |
| N020 | DOC-001 p. 6 Table 2: ITT CPC 1--5 and primary 44/43. | CPC counts sum to 1018/1022; CPC 1+2 is 44/43; no candidate. |
| N021 | DOC-001 p. 6 Table 2: PP survival 54/995, 51/943; printed 5.4/5.4 and 0.1. | The group percentages round to 5.4%, but raw proportions differ by 0.019 pp, which rounds to 0.0 pp, not printed 0.1; see NUM-CAND-002. |
| N022 | DOC-001 p. 6 Table 2: PP admission 289/995, 312/943; ROSC 342/995, 377/943. | Admission values/difference are compatible. ROSC ETI percentage is not; see NUM-CAND-001. |
| N023 | DOC-001 p. 6 Table 3: denominators 1027/996, 1028/996, 1027/999. | Each outcome uses its stated row-specific denominator; no candidate. |
| N024 | DOC-001 p. 6 Table 3: ETI 20, 102, 7, 5 of 999. | 2.0%, 10.2%, 0.7%, and 0.5% are compatible; unrecognized oesophageal intubation is textually zero, not a denominator conflict; no candidate. |
| N025 | DOC-001 p. 4: centre 5 n=115=56+59; CCF 86%/87%; pauses 27/16, difference 11 seconds. | Group sum and CCF direction are consistent. The difference unit conflicts with the named count measure; see NUM-CAND-003. |
| N026 | DOC-001 pp. 3--4: 3%/2%, 1% margin, 956/group, 80%, 5000 simulations, 2000 planned. | Planned-design quantities are internally scoped; 1912 required participants need not equal 2000 recruitment target; no candidate. |
| N027 | DOC-001 p. 4: hierarchical 0.05% and PP 0.08%, with matched CIs and PP 4.3/4.2. | Analysis population and estimate labels are preserved; PP raw primary proportions yield 0.080 pp; no candidate. |
| N028 | DOC-001 p. 6: post-hoc exclusions 91 and 155. | Different post-hoc populations are named; not summed or conflated; no candidate. |
| N029 | DOC-001 pp. 7--8: discussion repeat of 4.3% vs 4.2%. | Matches ITT day-28 CPC<=2 result after population/outcome matching; no candidate. |
| N030 | DOC-002 pp. 9, 15, 17: alive at day 28 and CPC<=2. | Protocol endpoint matches main outcome/time/threshold; no candidate. |
| N031 | DOC-002 pp. 9--10, 16: secondary-domain inventory. | Outcome, scale and time labels are definitions, not conflated values; no candidate. |
| N032 | DOC-002 p. 10: 2000, 20 centres, 24 months, 100/centre, 5/month. | `20x100=2000`; 100/24=4.17, so 5/month is a planning approximation; no candidate. |
| N033 | DOC-002 pp. 11, 37: 3%, 2%, 1%, 956/group, .8, .025, 2000, 5000. | Planned inputs match later support statements; no candidate. |
| N034 | DOC-002 pp. 11, 36: 50%/75% inclusion looks. | These are inclusion thresholds; no candidate. |
| N035 | DOC-002 p. 12: labelled external background values. | External-study quantities retained as background, not CAAM results; no candidate. |
| N036 | DOC-002 p. 13: labelled external background values. | External-study quantities retained as background, not CAAM results; no candidate. |
| N037 | DOC-002 p. 17: 20 centres, ID structure. | 15 France + 5 Belgium = 20; identifier components are not outcome values; no candidate. |
| N038 | DOC-002 pp. 18--21: day 28 with +7-day assessment window. | Assessment window is distinguished from outcome time; no candidate. |
| N039 | DOC-002 p. 18: transport estimate 20%--23%. | Explicit estimate, not observed flow; no candidate. |
| N040 | DOC-002 p. 20: delayed-consent estimate 3%--5%. | Explicit planning estimate, not observed denominator; no candidate. |
| N041 | DOC-002 p. 24: repeat recruitment table. | Matches N032 as the same planned set; no candidate. |
| N042 | DOC-002 p. 28: SAE 8/15-day deadlines. | Event-type deadlines are defined, not rates; no candidate. |
| N043 | DOC-002 p. 37: ITT missing primary = no success. | Rule is consistent with later SAP definition; no candidate. |
| N044 | DOC-002 p. 43: 1 year/90 days report deadlines. | Alternative administrative deadlines are correctly scoped; no candidate. |
| N045 | DOC-002 pp. 47--49: centres 01--20. | Matches original 20-centre protocol design; no candidate. |
| N046 | DOC-002 p. 50: mRS 0--6, death=6, higher worse. | Ordered-scale direction matches its definition; no candidate. |
| N047 | DOC-002 p. 51: CPC 1--5. | Ordinal CPC scale matches endpoint threshold usage; no candidate. |
| N048 | DOC-002 p. 52, authorized OCR: IDS total/components. | Sum score and difficulty cut-points retained as score, not proportion; no candidate. |
| N049 | DOC-002 p. 53: VAS 0--100. | Continuous scale correctly distinct from percentage; no candidate. |
| N050 | DOC-002 p. 54: Han 0--4. | Ordinal scale labels preserved; no candidate. |
| N051 | DOC-002 pp. 51--54: CPC/IDS/VAS/Han labels. | Measure/label/scale cross-check complete; no candidate. |
| N052 | DOC-002 p. 55: blank SAE identifier format. | No observed numerical result exists; no candidate. |
| N053 | DOC-002 p. 64: primary endpoint repeat. | Matches N030 after time/threshold matching; no candidate. |
| N054 | DOC-002 pp. 64--65: secondary outcomes. | Definitions match their stated measure/time domains; no candidate. |
| N055 | DOC-002 p. 65: 2000/20/24 recruitment. | Planned arithmetic agrees with N032/N041; no candidate. |
| N056 | DOC-002 p. 66: 95% CI lower bound > -0.01. | Contrast is bag minus tracheal and margin is -1 pp; no candidate. |
| N057 | DOC-002 p. 66: rate/quantitative analysis criteria. | Odds-ratio and risk-difference measures kept distinct; no candidate. |
| N058 | DOC-002 p. 66: 50%/75% interim. | Matches N034 and is explicitly planned; no candidate. |
| N059 | DOC-002 p. 66: sample-size inputs. | `956x2=1912`; 2000 exceeds it by 88 as planning recruitment; no candidate. |
| N060 | DOC-002 p. 67: cited trial n=830. | External background only; no candidate. |
| N061 | DOC-002 p. 67: 649359, 2.9%/367837 vs 1.0%/41972. | No supplied numerators permit recomputation; values correctly retained as external background; no candidate. |
| N062 | DOC-002 p. 67: 40/120=33%, 69/573=12%. | Values are 33.33% and 12.04%, compatible with display; no candidate. |
| N063 | DOC-002 p. 68: 10455=8487+1968. | Addition holds; no candidate. |
| N064 | DOC-002 p. 69: 1--4, 600000, >80%. | Background context has no internal denominator conflict; no candidate. |
| N065 | DOC-002 p. 71: endpoint/baseline-disability/technique-failure definitions. | Composite components are not treated as exclusive event counts; no candidate. |
| N066 | DOC-002 p. 71: technique-failure composite. | Mortality, regurgitation, and procedural failure labels are distinct components; no candidate. |
| N067 | DOC-002 p. 72: 15+5 centres. | `15+5=20`; no candidate. |
| N068 | DOC-002 p. 73: day 28 +7 and 20%--23%. | Follow-up rule and estimate are kept distinct; no candidate. |
| N069 | DOC-002 p. 75: day-28 status rule. | Later assessment reports day-28 status; no candidate. |
| N070 | DOC-002 p. 75: 3%--5% delayed consent. | Planning expectation only; no candidate. |
| N071 | DOC-002 p. 76: 24 months, day 28(+7). | Schedule/time labels are internally consistent; no candidate. |
| N072 | DOC-002 p. 78: 15-day notification, age >=18. | Deadline and eligibility rule are distinct; no candidate. |
| N073 | DOC-002 p. 79: 2000/20/24, 100, 5/month. | Arithmetic identifies 5/month as rounded operational planning target; no candidate. |
| N074 | DOC-002 pp. 79--80: assessment measure/time map. | 28-day measures and scale types retained; no candidate. |
| N075 | DOC-002 p. 83: 8/15-day SAE follow-up. | Deadlines correctly scoped by event type; no candidate. |
| N076 | DOC-002 p. 84: 7/15/8-day SUSAR timeline. | Sequential deadlines are internally labelled; no candidate. |
| N077 | DOC-002 pp. 85--90: 60-day/2-year/15-year retention rules. | Record-specific deadlines not conflated; no candidate. |
| N078 | DOC-002 p. 90: hypotheses at -0.01. | Boundary matches CI decision rule; no candidate. |
| N079 | DOC-002 p. 91: ITT/PP and 50%/75%. | Population and interim definitions agree with repeated protocol text; no candidate. |
| N080 | DOC-002 p. 92: safety/CI/missing/design statement. | Repeats plan with correct analysis distinctions; no candidate. |
| N081 | DOC-002 p. 97: final-report deadlines. | Matches N044; no candidate. |
| N082 | DOC-002 pp. 90--92: planned hypotheses/analysis. | Planned quantities are not compared as observed results; no candidate. |
| N083 | DOC-002 pp. 91--92: missing-data/design. | ITT and secondary missing-data rules retain distinct scope; no candidate. |
| N084 | DOC-002 p. 97: report deadline. | Repeat administrative rule consistent; no candidate. |
| N085 | DOC-002 pp. 101--102: late mRS/CPC definitions. | Repeats N046/N047 with same scale direction; no candidate. |
| N086 | DOC-002 pp. 104--105: VAS 0--100/Han 0--4. | Repeats N049/N050 with same measure labels; no candidate. |
| N087 | DOC-002 pp. 106--107: blank SAE form. | Instrument has no observed event counts; no candidate. |
| N088 | DOC-002 pp. 108,112--113: 20-1+6=25. | Amendment arithmetic holds; contribution rows need not be all participating centres; no candidate. |
| N089 | DOC-002 p. 110: endpoint/technique-failure amendment. | Definitions match planned endpoint and keep composite distinct; no candidate. |
| N090 | DOC-002 pp. 109--116: expected complications. | Named expected complications are not observed rates; no candidate. |
| N091 | DOC-002 p. 120: 3%/2%, 1%, 956/group, .8, .025, 2000, 5000. | SAP planning inputs and contrast agree with earlier protocol; no candidate. |
| N092 | DOC-002 pp. 121--124: BVM-TI, 95% CI, one-decimal nonmissing percentages. | Direction, rounding, and denominator conventions support matched main checks; no candidate. |
| N093 | DOC-002 pp. 122--124: endpoint, missing rule, ITT/PP/AT. | Population/missingness definitions are internally consistent; no candidate. |
| N094 | DOC-003 p. 2: eTable 1 1018/1022 and centre rows. | Centre counts sum to 1018/1022; row percentages are compatible to one decimal; no candidate. |
| N095 | DOC-003 p. 2; DOC-002 pp. 112--113: centre labels/amendment. | Absence of zero-contribution centres is compatible with contribution table; no candidate. |
| N096 | DOC-003 p. 3 row 1: 43/971 (4.4), 39/978 (4.0), 0.4. | Values 4.428%/3.988%, difference 0.440 pp; CI contains display; no candidate. |
| N097 | DOC-003 p. 3 row 2: 41/863 (4.8), 45/1174 (3.8), 0.9. | Values 4.751%/3.833%, difference 0.918 pp; CI contains display; no candidate. |
| N098 | DOC-003 p. 3; DOC-002 pp. 121--124: post-hoc labels/SAP. | Difference direction and outcome labels align; analysis-specific denominators are not mixed; no candidate. |

## Candidate propositions

### NUM-CAND-001 — Per-protocol ETI ROSC percentage conflicts with its printed count and denominator

- **Exact source location:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=6`, Table 2, Per-Protocol Analysis, “Return of spontaneous circulation”; corroborating fresh native layout text at `preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt` (Table 2).
- **Direct printed observation:** BMV `342 (34.4)` of `n=995`; ETI `377 (30.0)` of `n=943`; reported BMV-minus-ETI difference `-5.6 (-9.9 to -1.3)`.
- **Rule and calculation:** The percentage attached to a `No. of Patients (%)` cell must equal `100 x count / stated group denominator`, within 0.05 pp for one-decimal display. `377/943 x 100 = 39.979%`, which rounds to **40.0%**, not 30.0%. The same raw values give `34.372 - 39.979 = -5.607 pp`, compatible with the printed -5.6 pp; 30.0% would instead imply a +4.4 pp difference.
- **Tolerance:** 9.979 pp discrepancy, exceeding the 0.05-pp one-decimal tolerance.
- **Inference boundary and alternatives:** The inconsistency is directly observed between a printed numerator/denominator and its printed percentage; the likely intended display may be 40.0%, but that is an inference and not a correction. A denominator other than the explicitly headed PP `n=943` could explain 30.0% only if it were about 1257, which the table does not state.
- **Quality-control relevance:** The row joins a rate, its denominator, and its reported treatment difference. A wrong percentage can distort direct reading of the secondary outcome even though the displayed difference happens to agree with the raw counts.
- **Human question:** Should the ETI PP ROSC cell be `377 (40.0)` rather than `377 (30.0)`, and does any source version establish a different intended denominator?

### NUM-CAND-002 — Per-protocol day-28 survival difference is not supported by the printed raw values at its displayed precision

- **Exact source location:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=6`, Table 2, Per-Protocol Analysis, “Survival at 28 d”; fresh layout text asset cited above.
- **Direct printed observation:** BMV `54 (5.4)` of `n=995`; ETI `51 (5.4)` of `n=943`; reported BMV-minus-ETI difference `0.1 (-10 to 9.7)`.
- **Rule and calculation:** For the table's displayed percentage-point difference, `100 x (54/995 - 51/943) = 0.019 pp`; standard rounding to one decimal gives **0.0 pp**, not 0.1 pp. Both individual percentages round to 5.4%, as printed. This candidate is limited to the point estimate; the exact CI method is not sufficiently specified here to independently reproduce its bounds.
- **Tolerance:** Difference between 0.019 pp and 0.1 pp is 0.081 pp, exceeding 0.05 pp. The conclusion does not assume a sign or an alternative model beyond the table’s stated percentage-difference label.
- **Inference boundary and alternatives:** The raw count/denominator conflict with the displayed point estimate is direct. The actual analysis could have used unprinted data handling or a non-obvious estimator, but no such alternative denominator or estimator is stated for this row; the separate printed group percentages, counts, and PP headings all indicate a simple proportion difference.
- **Quality-control relevance:** This is a point-estimate/denominator consistency issue in a secondary outcome table. It is not an assessment of the study conclusion or confidence interval.
- **Human question:** What estimator and denominator produced the printed PP survival difference of 0.1 pp, or should its displayed value be 0.0 pp at one-decimal precision?

### NUM-CAND-003 — Centre-5 pause difference uses a time unit for a named count outcome

- **Exact source location:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=4`, Results, Post-Hoc Analyses; fresh layout text asset at `preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt`.
- **Direct printed observation:** The report describes the “number of pauses greater than 2 seconds during CPR,” then gives BMV `27` versus ETI `16`, “difference, `11 seconds` [95% CI, 7 to 15].” It also separately reports chest-compression fraction as `86%` vs `87%`.
- **Rule and calculation:** `27 - 16 = 11` is arithmetically consistent with a **count of pauses**. A difference derived from that named count should retain a count unit (pauses), whereas seconds is the duration threshold that defines which pauses are counted. The observed text therefore pairs the same difference with an incompatible unit/measure label.
- **Tolerance:** None: this is categorical unit/measure consistency, not rounding.
- **Inference boundary and alternatives:** The wording directly identifies a count outcome and directly labels its difference in seconds. It is possible that 27 and 16 are undisclosed time summaries rather than counts, but that would conflict with the explicit phrase “number of pauses”; only an underlying results dataset or clarified analysis could resolve it.
- **Quality-control relevance:** Mislabeling count versus time can impede correct extraction of effect measures and units for later evidence products.
- **Human question:** Were 27 and 16 counts of pauses (so the difference/CI should be labeled in pauses), or time quantities requiring the outcome description to be revised?

## Limitations

DOC-002 p. 134 is empty in both fresh native-text assets and has no authorized OCR, as documented in source coverage; no numeric relationship was registered for that page. This review does not recalculate model-dependent confidence intervals, P values, medians/IQRs, or unreported numerators, and it does not make clinical, methodological, or adjudicative judgments.

**Coverage:** 98/98 relationships checked (N001--N098). **Candidate propositions:** 3 (NUM-CAND-001 through NUM-CAND-003). **Checked with no candidate:** 95 relationships.
