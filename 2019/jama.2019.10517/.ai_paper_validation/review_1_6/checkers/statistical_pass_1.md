# Statistical Consistency Pass 1

- Runtime ID: 01a1286a-d824-7281-a62a-c73b450e930c
- Model: gpt-6.1-sol
- Reasoning effort: high
- Start mode: FRESH_SPAWN
- Assigned scope: all inferential-statistical material in current main/support maps for all63 physical source pages; no sampling.
- Completed scope: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108.
- Relationship count:108 (37 displayed main results,25 historical/background results,9 graphical relationships,12 power scenarios,25 model/rule relations).
- Candidate count:1 local candidate, STAT1-CAND-01.
- Scientific coverage gaps:0.
- Pass state: PASS_1_COMPLETE for every S ID in statistics/relationship_inventory.md. Pass 2 awaits a different fresh high-effort runtime.

## Evidence and method

Read complete current scope, performance profile, review contract, report spec, settings; current tooling/source/asset/coverage inventories; main quantitative map; both disjoint support maps and their canonical union. Source-linked native/layout locators were used, then exact direct-source text was extracted for candidate locations. Reused result-figure images for eFigures8–9 and main Table4 were visually inspected; source PLAN p6 was newly rendered and visually inspected for historical test/df transcription. No old candidate set, dispositions, reports or classifications were read. No web, unbundled Python, GPU or Office processing was used.

For all37 main reported inferential results, every interval endpoint is ordered and every point estimate lies in its interval. All7 Cox HR intervals are positive; directions agree with the corresponding treatment/site/age contrast as printed. The primary and sensitivity HR intervals lie wholly below1 and reported P<.001. Other covariate intervals include1 and the P values exceed.05. The reported reference “remission vs near-remission” is preserved rather than reversed by clinical expectations. Abstract and narrative repetitions of all8 secondary estimates/CIs agree. Among16 within-group Table4 changes, none requires interval symmetry, particularly the median-change rows; missingness footnote prevents exact subtraction of marginal means/medians. All4 Table5 interval estimates contain0 and agree qualitatively with the narrative no significant difference. Identical total/LDL counts and intervals are legitimate separate endpoint records absent contrary evidence.

Every main secondary P is explicitly Holm-adjusted; CIs are not identified as simultaneous Holm intervals. It is therefore inappropriate to equate a CI-derived nominal two-sided tail with the printed adjusted P. No primary exact Wald, LR or score method/variance/CI-construction rule is supplied. We do not infer df, random-effect covariance, overdispersion estimation, multiplicity family membership or unadjusted P values.

All12 PLAN power-table scenarios were checked without a binomial or independence substitution for their stated survival/mixed simulations. Increasing relapse contrast, effect size or matched observation count increases displayed power; increasing matched attrition decreases it. Lipid dash cells are unreported scenarios, not zero power. Stated thresholds match .80 weight at8 observations/.35 effect, .84 lipid at4/.40, and .85 weight at4/.40 for open-label power. Current article's80% phrasing is compatible with PLAN table power.82 under15% attrition. Planned sample revision is disclosed and is not registered merely because observed randomization differs from the initial target.

All9 result figures were checked from the complete visual current map for mean/band ordering, direction, units, axis time and model matching. Shaded-band confidence levels are not printed on result-figure pages. Raw observed Table4 marginal means/changes do not replace model means/linear slopes. Quadratic time means positive initial slope contrasts can coexist with declining overall trajectories. Triglyceride subgroup curves cannot substitute for pattern-mixture-averaged estimates without pattern weights. Background ICC and IQCODE ranges are ranges across historical evaluations, not assumed confidence intervals.

## STAT1-CAND-01 — HbA1c model-effect unit differs from its reported outcome scale

- Linked statistical relationships: S016, S062; corroborating within-arm rows S027–S028.
- Primary category proposal: Measure, label, or scale inconsistency.
- Compared locations and roles:
  - REPORT [DOC-001 physical p1, Results abstract](../../../jama_flint_2019_oi_190079.pdf#page=1): HbA1c daily contrast is printed “−0.0002 mg/dL” with95%CI “−0.0021 to0.0016.”
  - REPORT [DOC-001 physical p7, Secondary Outcomes](../../../jama_flint_2019_oi_190079.pdf#page=7): repeats “−0.0002 mg/dL” and the same95%CI, adjustedP=.99.
  - REPORT [DOC-001 physical p8, Table4 HbA1c row](../../../jama_flint_2019_oi_190079.pdf#page=8): outcome label is “HbA1c, %”; baseline O5.9/P5.9, termination O5.7/P5.9 and unadjusted changes−0.2/0.1.
  - REPORT [DOC-003 physical p9, eFigure8](../../../joi190079supp2_prod.pdf#page=9): title matches HbA1c randomized mixed-model means; ordinate “HbA1c (%)”; Day scale, ticks5.6–6.2.
- Proposed relationships: S_W for the main abstract/narrative versus main Table4 unit; S_C for main results versus results-supplement outcome unit. S_C has precedence if the coordinator registers this combined identical scale rule. PLAN is not a conflicting comparator.
- Printed-versus-comparator: mass-concentration mg/dL attached to a daily HbA1c coefficient versus percentage scale attached to the same named modeled outcome and its raw measure.
- Reproducible rule: a time coefficient for an outcome remains in that outcome's unit per time unless an explicitly supplied transformation or conversion maps it to another scale. Percent and mg/dL are distinct labels; no HbA1c transformation/conversion to mg/dL appears in the supplied model definitions.
- Direct observation: exactly those labels are supplied; repeated effect estimate/CIs agree across main locations.
- Derived observation: different estimands (mixed linear-time effect versus raw change) prevent numerical equality, but do not by themselves explain changing the underlying HbA1c measurement unit.
- Calculation: no numerical conversion proposed or required; unit identity comparison only. Do not reinterpret−0.0002 as a prescribed corrected numeric quantity.
- Source-grounded alternative: model output may have undergone an undocumented unit/response transformation; supplied material contains no such mapping. Table4's raw endpoint and model-effect estimands differ, which remains relevant when checking intended coefficient units.
- Missing definition / human question: On which outcome scale was the daily HbA1c treatment×linear-time coefficient fit/reported, and which unit was intended for the coefficient andCI? Inspect original model specification/output and original Table4/eFigure8 labels.
- Quality-control relevance: if confirmed, a data extractor could copy a daily HbA1c slope into the wrong unit; no assertion of conclusion change.
- Status: Pending Human Adjudication. Coordinator assigns stable C ID and mechanical classification/evidence state.

## Diagnostic calculations that do not establish additional candidates

Rscript4.5.2 (2025-10-31) was used locally for direct arithmetic/distribution calculations. These are auxiliary calculations, not review orchestration. Commands used base R pchisq, pf, pt, pnorm and qnorm; no installation or network.

### Cox interval-tail diagnostics (S001–S007)

Rounded log-normal Wald approximation: log-scale SE=(log upper−log lower)/(2×qnorm(.975)); approximate two-sided tail from logHR/SE. The supplied report does not identify this CI/test/variance construction, so these cannot replace actual reported inference.

| S ID | Printed HR | Approximate log-scale SE | Approximate normal-Wald P | Printed P |
|---|---:|---:|---:|---|
| S001 | .25 | .333234 | .0000318069 | <.001 |
| S002 | .78 | .317847 | .434390 | .44 |
| S003 | 2.45 | .467712 | .0553782 | .06 |
| S004 | 1.53 | .459818 | .355039 | .36 |
| S005 | 1.09 | .518768 | .868062 | .88 |
| S006 | 1.80 | .409316 | .150996 | .15 |
| S007 | .22 | .347788 | .0000133925 | <.001 |

All signs/null classifications agree. S005's diagnostic .868 versus .88 is not a qualifying mismatch: exact unrounded HR and compatible CI/test rule are missing. No denominator/model equivalence is inferred.

### Historical explicit distribution labels (S039–S046)

Historical PLAN [DOC-002 p6](../../../joi190079supp1_prod.pdf#page=6) prints chi-square/F statistics anddf:
chi-square(1)=9.53 gives upper-tail .002021401 (printed.002);
chi-square(1)=4.4 gives .03593893 (printed.036);
F(1,226)=14.51 gives .0001796963 (printed.0002).
PLAN [DOC-002 p7](../../../joi190079supp1_prod.pdf#page=7) F(3,149)=3.16 gives .02648964, compatible with p<.03.
No covariance/SE reconstruction is required for these statistic-to-tail checks.

For historical t statistics, sidedness is not independently defined for the historical analyses. Under a labelled two-sided diagnostic only, t(211)=2.65 yields.0086589 (printed.009), t(166)=.36 yields.719305 (printed.72), and t(102)=1 yields.319677 (printed.32). These examples do not import the prospective plan's H1–H3 sidedness into historical studies.

### Unequal-variance df diagnostic (S045)

PLAN p6 lines295–301 prints blood-subset young66/old102, exposure magnitude1128.9±737.6 versus1027.1±477.6 ug/mL*h and “unequal variances t[102]=1.0, p=.32.” Direct p6 rendering confirms all characters, including df102 and younger weight-dispersion4.0 elsewhere on the page.

If and only if ± denotes sample SD, those exact blood counts are the effective analyzed group sizes, and an ordinary independent-sample Welch–Satterthwaite calculation was used, a=737.6²/66, b=477.6²/102 give t=(1128.9−1027.1)/sqrt(a+b)=.9944361 and df=(a+b)²/[a²/65+b²/101]=100.3006. Varying each displayedSD by±.05 gives approximate df100.2889–100.3122. The printed t and P remain compatible; df differs under this diagnostic.

No candidate is registered because variance estimator/df method, dispersion definition and blood-subset-to-analysis matching are not supplied; those inputs cannot be inferred from convention or the phrase “unequal variances” alone. This is a precise reconstruction limitation, not an assertion that102 is wrong.

### Simpson-Angus response/link diagnostic (S037,S063,S078)

REPORT main p7 prints0.022 “points” weekly contrast and states a Poisson mixed model on pp4–5; result eFigure9 p10 shows O≈.56→.73/P≈.685→.40 over36weeks. Using approximate endpoints gives response-scale mean differential secant:
[(.73−.56)−(.40−.685)]/36≈.0126 points/week.
As a labelled hypothetical log-scale diagnostic, [log(.73/.56)−log(.40/.685)]/36≈.0223/week, close to the printed number. This resemblance does not establish the actual link function, coefficient/derivative or marginal contrast. Exact curve coordinates and the printed0.022 estimand mapping are missing. Thus no extra candidate is registered solely by presuming a Poisson log link or constant response-scale point change.

### Other quantity diagnostics

Historical completer weight standardized difference (16.6−10.7)/sqrt[(16.5²+11.3²)/2]=.4172243, compatible with printed.42 under this explicitly equal-weight SD diagnostic; exact standardization is not provided.

Main crude risk difference34/62−13/64=.3452621 yields reciprocal~2.896. Printed NNT2.8 is described as based onHR rather than the crude risk contrast; absent survival horizon/baseline/method, the package does not establish identity with that crude reciprocal, so no independent NNT candidate is emitted here. Numeric/cross-source lanes may track the text separately without this pass presuming equivalence.

## Display-zero exclusion and missing definitions

No supplied result in this completed inferential inventory is a coherent finite-precision display-zero P value. The mandated exclusion rule remains DISPLAY_ZERO_NOT_CANDIDATE; no candidate was registered from notation, numeric underflow or a computed tiny positive tail.

Missing exact CI/test definitions, df, covariance, variance estimator, multiplicity-family membership, pattern weights, plot coordinates, power simulation specification, historical effective samples and intended scale mappings are retained per S record. None creates a source-coverage gap or a candidate solely because unreported. All63 mapped source pages are accounted for, including PLAN bibliography/admin pages and REPORT/administrative covers with no applicable inference.

## Derivative provenance

New candidate-confirmation derivatives, direct Poppler26.01.0:
- preprocessing/stat1-main-p01.txt: direct pdftotext physical main p1, native.
- preprocessing/stat1-main-p07.txt: direct pdftotext physical main p7, native.
- preprocessing/stat1-main-p08-layout.txt: direct pdftotext -layout physical main p8.
- preprocessing/stat1-plan-p06.png: pdftoppm -f6 -l6 -singlefile -scale-to1800 -png physical PLAN p6, visually inspected.

Reused result/main images were opened from preprocessing/JAMA2019-10517-D03/rendered_pages/page-009.png, page-010.png and preprocessing/JAMA2019-10517-D01/rendered_pages/page-008.png. Their historical rendering engine/version remains curator-recorded; direct PDFs remain authority. No reused/source file changed. Record these four new derivative paths individually in coverage_manifest.md if derivative-stage rows are maintained.

