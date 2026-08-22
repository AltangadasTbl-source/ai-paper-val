# Numeric consistency review

## Scope, evidence, and rules

**Assigned inventory:** all 57 numeric/reporting relationships: N001-N035 and N501-N522.  The review used only the fresh maps `extraction/main_quantitative_evidence.md` and `extraction/support_quantitative_evidence.md`, their fresh native/layout text, and the rendered pages cited below.  Locations are physical PDF pages.

For every applicable relationship, I checked exact count/total and numerator/denominator identities; reported percentages with ordinary nearest-whole-percent tolerance (absolute rounding tolerance 0.5 percentage point unless a denominator or rule was not printed); median/IQR or range ordering; units, scale bounds, effect direction, and reference labels; and whether a reported model-derived quantity was being incorrectly treated as a subtraction of rounded marginal summaries.  Protocol quantities were kept distinct from published results.  A dependent-t-test or mixed-model effect was not called an arithmetic discrepancy solely because its rounded marginal means/changes did not reproduce it: participant-level pairing and missingness can differ unless the paper establishes otherwise.

`NO_ISSUE` means the stated rule reconciled within precision or the displayed values carried compatible population/scale/definition labels. `NO_APPLICABLE_NUMERIC_RESULT` is a complete coverage outcome, not a finding. `CANDIDATE NUMxxx` is a document-grounded quality-control observation pending human adjudication; it is not a severity or validity judgment.

## Candidate observations for later merging

### NUM001 — Abstract sex percentage is incompatible with the reported enrolled count

- **Relationships:** N002.
- **Exact locations and printed inputs:** DOC-001 PDF p. 1, Abstract Results: “Among 30 enrolled patients ... **22% men**”; DOC-001 PDF p. 4, Baseline Data: “**Twenty-two men and 8 women** ... were enrolled”; DOC-001 p. 5, Table 1 has subgroup men counts 13/16 and 7/11.
- **Rule and calculation:** A percentage described as men among the same 30 enrollees must equal the printed men count divided by 30, within whole-percent rounding.  `22 / 30 × 100 = 73.33%`, whose whole-percent display is 73%, not 22%.  The Table 1 subgroup counts also sum to 20 men among the 27 analyzed completers, and neither provides a path to 22% of 30.
- **Tolerance:** Whole-percent rounding allows [72.5%, 73.5%) for a displayed 73%; 22% is 51.33 percentage points from 73.33%.
- **Direct observation vs inference:** Directly observed are the abstract’s “22% men,” the p. 4 count 22 men/8 women, and the common enrolled N=30.  The inference is that the abstract percentage and count refer to the same stated population; the abstract itself supplies that matching key.
- **Alternative:** “22%” could be a typographical transposition or an unstated different denominator, but no such denominator is printed.
- **Quality-control relevance:** A demographic count-versus-percentage mismatch can be copied as a baseline characteristic into evidence summaries.
- **Human question:** Should the Abstract Results demographic field read “22 men” or approximately “73% men,” and is there any intended denominator other than the 30 enrolled patients?

### NUM002 — Printed INQoL 0-100 scale conflicts with displayed IQR endpoints above 100

- **Relationships:** N017.
- **Exact locations and printed inputs:** DOC-001 PDF p. 5, Table 1: INQoL composite score, median (IQR), CLCN1 `84.0 (74.5-110.3)` and SCN4A `98.0 (56.0-120.0)`; Table 1 footnote f on the same page: “Scale, **0 to 100**; a higher score indicates greater disease severity.”  DOC-001 PDF pp. 7-8, Table 2 footnote g repeats “Scale, 0 to 100; a higher score indicates greater disease severity.”
- **Rule and calculation:** If the reported composite is bounded 0-100, every quantile of it must be in [0,100].  The printed upper IQR endpoints exceed the stated maximum by `110.3 - 100 = 10.3` and `120.0 - 100 = 20.0` points.
- **Tolerance:** No rounding tolerance can place 110.3 or 120.0 at or below 100.
- **Direct observation vs inference:** The scale statements and table endpoints are direct observations.  The contradiction follows from the stated upper bound.  This does not assume which item-scoring convention is correct.
- **Alternative:** The scale footnote may be incorrect/incomplete for a composite score, or the endpoints may be on a differently bounded composite scale.
- **Quality-control relevance:** A scale-bound conflict can mislead extraction of baseline severity and direction.
- **Human question:** What is the intended numerical range of the INQoL composite score, and should the Table 1/Table 2 footnote or the reported IQR values be corrected?

### NUM003 — Table 2 secondary-outcome header labels the contrast opposite to the displayed treatment-effect signs

- **Relationships:** N020, N021, N022, N023, N024, N025, N026, N027, N028, N029.
- **Exact locations and printed inputs:** DOC-001 PDF p. 7, Table 2 secondary-outcome header prints “Treatment Effect **(Placebo-Mexiletine)**.”  Examples on the same page: SF-36 physical changes Pbo `+1.04`, Mx `+8.66`, effect `+7.81`; INQoL changes Pbo `-7.22`, Mx `-21.44`, effect `-14.22`; handgrip first Pbo `+0.46`, Mx `-2.39`, effect `-2.85`.  The table footnote d on PDF pp. 7-8 states “All statistically significant findings favored mexiletine treatment.”
- **Rule and calculation:** The header’s written contrast predicts `Pbo - Mx`.  The printed effect signs instead follow `Mx - Pbo`: for the three examples, `8.66-1.04=+7.62` (reported +7.81), `-21.44-(-7.22)=-14.22` (reported -14.22), and `-2.39-0.46=-2.85` (reported -2.85).  The small physical-component magnitude difference is not treated as a separate arithmetic finding because a paired analysis can use a differing complete-case set; the decisive observation is the repeated opposite sign convention.  The same sign pattern recurs in the secondary-outcome rows through PDF p. 8.
- **Tolerance:** Sign is categorical; rounding cannot reverse it.  The displayed label and values cannot both denote the same subtraction order.
- **Direct observation vs inference:** Header, values, and footnote are direct observations.  The inferred intended contrast is Mx minus Pbo, supported by the repeated signs and “favored mexiletine” statement; the source does not explicitly confirm a corrected header.
- **Alternative:** The header may be wrong while the values/effects are intended, or a nonstandard coding convention was intended but not stated.
- **Quality-control relevance:** A reversed treatment-contrast label can invert interpretation when effect estimates are abstracted or pooled.
- **Human question:** Is the secondary-outcome treatment-effect column intended to be “Mexiletine-Placebo” rather than “Placebo-Mexiletine,” or is another sign convention intended?

### NUM004 — Placebo `Any` adverse-reaction percentage does not reconcile with the table’s apparent denominator

- **Relationships:** N513.
- **Exact locations and printed inputs:** DOC-003 PDF p. 6, eTable 4: placebo GI `1 (3%)`, headache `1 (3%)`, `Any 2 (6%)`; mexiletine GI `21 (70%)`, any `27 (90%)`, dose reduction `3 (10%)`, and other 1/2-count percentages.  DOC-001 PDF p. 8 says GI discomfort occurred in `21 of 30 patients (70%)` during mexiletine periods.
- **Rule and calculation:** The table’s repeated count/percentage pairs and the main-paper statement establish an apparent 30-person denominator: `21/30=70%`, `27/30=90%`, `3/30=10%`, and `1/30=3.33%`, displayed 3%.  Under that same denominator, `2/30×100=6.67%`, which rounds to 7%, not the printed 6%.
- **Tolerance:** Nearest whole-percent rounding; 6% represents [5.5%,6.5%), while 2/30 is 6.67%.
- **Direct observation vs inference:** Counts/percentages and the 21-of-30 statement are direct.  The common placebo denominator is inferred from the table’s surrounding pairs; eTable 4 does not explicitly print its denominator.
- **Alternative:** A distinct placebo exposure denominator (for example 31) or truncation rather than nearest rounding could produce 6%; neither is stated in the table.
- **Quality-control relevance:** Denominator ambiguity changes the reported adverse-event percentage and may affect evidence extraction.
- **Human question:** What denominator and rounding rule apply to the placebo `Any` row, and should `2 (6%)` be revised or annotated?

### NUM005 — eMethods parameter prose reverses `mu_mex[i]` and `mu_plac[i]` relative to the code and data labels

- **Relationships:** N517, N518.
- **Exact locations and printed inputs:** DOC-003 PDF p. 11, eMethods 2 code: `Stiff_Plac[i,t] ~ dnorm(mu_plac[i],...)` and `Stiff_Mex[i,t] ~ dnorm(mu_mex[i],...)`; its Real data labels identify Stiff_Plac as placebo and Stiff_Mex as mexiletine.  On PDF p. 12, Estimated model parameters instead print `mu_mex[i] mean IVR score ... during the placebo treatment` and `mu_plac[i] ... during the mexiletine treatment`.  DOC-003 PDF pp. 13-14 eMethods 3 repeats the same code/data pairing and the same reversed two prose definitions.
- **Rule and comparison:** A model-parameter label must identify the treatment assigned to that parameter in the printed likelihood and real-data definition.  The code maps `mu_plac` to `Stiff_Plac`/placebo and `mu_mex` to `Stiff_Mex`/mexiletine; the two prose labels give the opposite mapping.
- **Tolerance:** Not applicable; treatment identity is categorical.
- **Direct observation vs inference:** All code and prose strings are direct observations.  The conclusion that prose labels are reversed follows directly from the source’s own likelihood/data definitions; it does not reconstruct an analysis.
- **Alternative:** The code/data labels could have been intentionally reversed upstream, but then the adjacent `diff=mu.plac-mu.mex` descriptions and published positive placebo-minus-mexiletine convention require clarification.
- **Quality-control relevance:** Swapped parameter labels can reverse a reader’s interpretation of the Bayesian contrast and impede reproduction.
- **Human question:** Which mapping is authoritative for `mu_mex[i]` and `mu_plac[i]`, and should the eMethods 2/3 parameter prose be corrected to match the supplied code?

### NUM006 — eMethods 3 describes the CLCN1 contrast as applying to SCN4A patients

- **Relationships:** N518.
- **Exact location and printed inputs:** DOC-003 PDF p. 14, eMethods 3 defines `diff_CLCN1 <- mu.plac_CLCN1 - mu.mex_CLCN1`; its Estimated model parameters section then prints `diff_CLCN1 mu.plac – mu.mex for **SCN4A patients**`.  The immediately surrounding `diff_SCN4A` line is correctly labelled SCN4A; P2/P3 entries separately name each genotype.
- **Rule and comparison:** A genotype-indexed parameter’s descriptive label must match its printed definition/subscript.  The CLCN1 subscript/code conflicts with the prose’s SCN4A label.
- **Tolerance:** Not applicable; genotype identity is categorical.
- **Direct observation vs inference:** The source strings are direct observations; the mismatch is a literal label comparison.
- **Alternative:** The prose phrase may be a local copy/edit error.
- **Quality-control relevance:** This could lead a reader to assign the CLCN1 subgroup effect to the wrong genotype.
- **Human question:** Should the `diff_CLCN1` description identify CLCN1 rather than SCN4A patients?

### NUM007 — `sigma.mex` is described as placebo-period variation

- **Relationships:** N517, N518.
- **Exact locations and printed inputs:** DOC-003 PDF p. 12, eMethods 2: `sigma.mex Standard deviation ... during **placebo** treatment`; PDF p. 14, eMethods 3 repeats the same phrase.  On both pages, `mu.mex` is explicitly labeled mexiletine treatment, and the code/data blocks use `Stiff_Mex` with `mu_mex`/`tau.mex`.
- **Rule and comparison:** The suffix and likelihood/data association identify `sigma.mex` as the mexiletine-period parameter.  Calling it placebo-period variation conflicts with its adjacent mexiletine-labelled mean/likelihood structure.
- **Tolerance:** Not applicable; treatment identity is categorical.
- **Direct observation vs inference:** The strings are direct; the expected treatment association follows from the source’s own model naming and likelihoods.
- **Alternative:** This can be a repeated copy/edit error in prose rather than an error in executed code.
- **Quality-control relevance:** Incorrect variance-component labeling can misstate the model and confuse attempts to reproduce it.
- **Human question:** Is `sigma.mex` intended to describe mexiletine-treatment variation, and should both eMethods descriptions be amended?

## Complete relationship-by-relationship outcomes

| ID | Fresh evidence location(s) checked | Checks applied and outcome |
|---|---|---|
| N001 | DOC-001 pp. 1, 4; Figure 1/2 | `38-8=30`; `1+7=8`; `30-3=27`; `2+1=3`; all reconcile. NO_ISSUE. |
| N002 | DOC-001 pp. 1, 4-5; Table 1 | Age range/sex/genotype population checked. Abstract `22% men` conflicts with 22 men/30: CANDIDATE NUM001. |
| N003 | DOC-001 pp. 1-2 | `4+4+1+2=11` weeks; 200 mg three times/day =600 mg/day. NO_ISSUE. |
| N004 | DOC-001 pp. 1-3, 6 | IVR 1-9, higher-worse, 0.75 threshold/direction and 20%/0.43 context checked. NO_ISSUE. |
| N005 | DOC-001 p. 4 | `23+(4×2)=31` sets and `23+4=27` completers. NO_ISSUE. |
| N006 | DOC-001 p. 4 | `773/868=89.06%→89%`; `2676/2728=98.09%→98%`. NO_ISSUE. |
| N007 | DOC-001 pp. 1,4-5 | `24+3=27`; `24/27=88.89%→89%`; `3/27=11.11%→11%`. NO_ISSUE. |
| N008 | DOC-001 pp. 1,4-6 | `5.56-2.50=3.06`; placebo-minus-mexiletine direction and Bayesian labels match. NO_ISSUE. |
| N009 | DOC-001 pp. 4-6 | `16+11=27`; hierarchical subgroup estimates not treated as weighted totals. NO_ISSUE. |
| N010 | DOC-001 pp. 1,4,6 | Threshold, posterior probability, N, and figure sequence labels compatible. NO_ISSUE. |
| N011 | DOC-001 pp. 3-4 | Order/period P values retain stated model context. NO_ISSUE. |
| N012 | DOC-001 pp. 1,5,10 | 3.12 versus 2.69 is explicitly cross-study/descriptive; no same-population equality rule. NO_ISSUE. |
| N013 | DOC-001 p. 6 | Secondary IVR scale, higher-worse direction, .75 probability threshold checked. NO_ISSUE. |
| N014 | DOC-001 p. 5 Table 1 | `13/16=81%`, `7/11=64%`, `2/16=13%`, `7/16=44%`, `5/11=45%`; `16+11=27`. NO_ISSUE. |
| N015 | DOC-001 p. 5 Table 1 | Each median is within printed IQR; IVR 1-9 direction retained. NO_ISSUE. |
| N016 | DOC-001 p. 5 Table 1 | Median/IQR ordering and seconds/time direction checked. NO_ISSUE. |
| N017 | DOC-001 p. 5 Table 1; pp.7-8 Table 2 | Median/IQR ordering holds, but IQR endpoints > stated 0-100 INQoL bound: CANDIDATE NUM002. |
| N018 | DOC-001 pp.7-8 Table 2 | IVR 1-9 direction/period labels checked; mixed-model effect not recomputed from rounded marginal means. NO_ISSUE. |
| N019 | DOC-001 p.7 Table 2 | IVR scale and contrast labels checked; model effects kept distinct. NO_ISSUE. |
| N020 | DOC-001 p.7 Table 2 | SF-36 scale/direction checked; secondary treatment-effect header sign mismatch: CANDIDATE NUM003. |
| N021 | DOC-001 p.7 Table 2 | INQoL direction checked; secondary treatment-effect header sign mismatch: CANDIDATE NUM003. |
| N022 | DOC-001 pp.7-8 Table 2 | Seconds/direction checked; secondary treatment-effect header sign mismatch: CANDIDATE NUM003. |
| N023 | DOC-001 p.7 Table 2 | Subgroup label/direction checked; secondary treatment-effect header sign mismatch: CANDIDATE NUM003. |
| N024 | DOC-001 p.7 Table 2 | Seconds/direction checked; secondary treatment-effect header sign mismatch: CANDIDATE NUM003. |
| N025 | DOC-001 p.7 Table 2 | Timed Up&Go seconds/direction checked; secondary treatment-effect header sign mismatch: CANDIDATE NUM003. |
| N026 | DOC-001 p.7 Table 2; p.8 footnote | Relaxation-time units/direction checked; secondary treatment-effect header sign mismatch: CANDIDATE NUM003. |
| N027 | DOC-001 p.7 Table 2; p.8 footnote | Force N, 0-600, lower-worse checked; secondary treatment-effect header sign mismatch: CANDIDATE NUM003. |
| N028 | DOC-001 p.7 Table 2; p.8 footnote | Percent 0-100/higher-worse and subgroup labels checked; secondary treatment-effect header sign mismatch: CANDIDATE NUM003. |
| N029 | DOC-001 p.8 Table 2 | EMG grade 0-3/higher-worse and contrast label checked; secondary treatment-effect header sign mismatch: CANDIDATE NUM003. |
| N030 | DOC-001 p.8 | 24 responders matches N007; follow-up range is ordered. NO_ISSUE. |
| N031 | DOC-001 pp.1,8; DOC-003 p.6 eTable 4 | 21/30=70%, 1/30=3%; event labels/cross-locations match. NO_ISSUE. |
| N032 | DOC-001 p.8 | μg/mL and mg/day units, range, patients 4/13 values, and timing checked. NO_ISSUE. |
| N033 | DOC-001 p.8 | `26/31=83.87%→84%`; set denominator matches N005. NO_ISSUE. |
| N034 | DOC-001 pp.1-2,5,7-8,10 | Repeated 27/3.12/2.69 results retain their frequentist and scale labels. NO_ISSUE. |
| N035 | DOC-001 p.3 | `1.29-1.75=-0.46`; simulated n/replicate context retained. NO_ISSUE. |
| N501 | DOC-002 p.7 | Planned duration and dose escalation identities checked; plan not equated to observed trial. NO_ISSUE. |
| N502 | DOC-002 pp.12-17 Table 1 | Planned visits/week windows and daily-IVR definition checked; no result count inferred. NO_ISSUE. |
| N503 | DOC-002 pp.13-14,31-34 | Scale, frequency/severity, seconds, force, and EMG-grade units separated. NO_ISSUE. |
| N504 | DOC-002 pp.18-21 | Protocol population, 0.75 threshold, 10/arm and simulation labels checked. NO_ISSUE. |
| N505 | DOC-002 p.21 | Four 2×2 cells retain prior/pair labels; design values not observed results. NO_ISSUE. |
| N506 | DOC-002 pp.22,30 | 200 mg TID=600 mg/day; planned pharmacokinetic statements compatible. NO_ISSUE. |
| N507 | DOC-002 pp.29-30 | Cited external meta-analysis/safety values retained as background, not trial occurrence matches. NO_ISSUE. |
| N508 | DOC-002 pp.38-39 | `3/30=10%`; DSMB thresholds retain planned-population context. NO_ISSUE. |
| N509 | DOC-002 pp.40-42 | Posterior threshold, outcome, prior, and stop-rule direction checked. NO_ISSUE. |
| N510 | DOC-002 pp.44-45 | `20+10=30`; RUNMC components `10+5+5=20`, Maastricht `5+2+3=10`; planned only. NO_ISSUE. |
| N511 | DOC-003 pp.3-4 eTable 2 | All 30 rows treated as baseline 1-9 values, not post-treatment effects; identifiers retained. NO_ISSUE. |
| N512 | DOC-003 p.4 eTable 2 note | Family markers are relationship labels, not duplicate observations; gene definitions compatible. NO_ISSUE. |
| N513 | DOC-003 p.6 eTable 4; DOC-001 p.8 | Overlap rule applied; placebo `Any 2 (6%)` fails apparent n=30 nearest rounding: CANDIDATE NUM004. |
| N514 | DOC-003 p.7 eFigure 1 | `4+23=27`; three named dropouts excluded; set/participant distinction retained. NO_ISSUE. |
| N515 | DOC-003 p.8 eFigure 2 | N=27, four endpoint labels, .75 threshold and posterior-AUC definition match. NO_ISSUE. |
| N516 | DOC-003 p.9 eFigure 3; p.6 eTable 4 | Patient 7/event/time match one serious skin reaction; n=30 percentage context retained. NO_ISSUE. |
| N517 | DOC-003 pp.10-12 eMethods 1-2 | Formula direction and precision labels checked; prose parameter swaps and sigma label conflict: CANDIDATES NUM005, NUM007. |
| N518 | DOC-003 pp.13-14 eMethods 3 | Genotype direction/code checked; parameter prose swap, CLCN1/SCN4A label, and sigma label conflict: CANDIDATES NUM005-NUM007. |
| N519 | DOC-003 pp.15-16 eMethods 4 Table 1 | N=1000/missing=0, ordered summary bounds, null truth, and diff direction checked. NO_ISSUE. |
| N520 | DOC-003 p.16 eMethods 4 Table 2 | `1000+0=1000`; 0/1000=0.00; `p2_effect` classification, not a P-value display. NO_ISSUE. |
| N521 | DOC-003 pp.16-17 eMethods 4 Tables 3-4 | `315+685=1000`; `685/1000=68.5%`; `1.29-1.75=-0.46`. NO_ISSUE. |
| N522 | DOC-004 p.1 | Data-sharing statement has no numeric result/denominator/endpoint. NO_APPLICABLE_NUMERIC_RESULT. |

## Coverage result and limitations

- **Relationships checked:** 57/57 (N001-N035, N501-N522).
- **Distinct provisional candidate observations:** 7 (NUM001-NUM007); each may be independently merged or retained by the later candidate-registration stage only under its exact printed comparator and rule.
- **No display-zero P-value observation was registered:** no candidate rests on `P=0`, `p=0.000`, or similar notation.
- **Limitations:** PDF-native/layout text and targeted renders were sufficient; no raw participant dataset, calculation code execution log, or unprinted adverse-event denominator was supplied.  Accordingly, model-based effect magnitudes were not reconstructed from rounded marginal summaries, and NUM004 explicitly retains its denominator/rounding alternative for human review.
