# Main numeric and statistical coverage quality audit

Runtime audit agent: `/root/audit_main_statistical_coverage`; fresh quality-control audit shard, `gpt-6.1-sol`, `high`. Assigned artifact: `quality/statistical_main_coverage_audit.md`. Responsibility: S001–S079 and N001–N087, covering the 111 unique MAIN001–MAIN111 groups of REPORT DOC-001. Overlapping N/S records are tracking references, not additional independent source units. No stable candidate-card adjudication is assigned to this shard; the lead auditor owns candidate inclusion, screening, classifications, and the canonical audit.

Coverage status: COMPLETE for 79/79 assigned S records and 87/87 assigned N records, including every grouped component, blank, continuous dispersion, interval endpoint, test value, threshold and matched main-paper occurrence. New distinct threshold-meeting findings: 0. New F-QA IDs: none. No candidate-count goal, old candidate discovery list, other paper, or earlier-run conclusion controlled this audit. Existing registered patterns are cross-references only and are not rediscovered as separate findings.

## Inputs, authority and reproducibility

QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md were read completely. Current-run inputs were the main structured map through line 164, all assigned complete S vectors, all assigned N rows, both statistical pass records and their complete exclusion tables, relevant current numeric exclusions, tooling_record.md, and relevant execution-manifest rows. No web or external literature was used. Current-run checker/candidate mentions were audited as workflow outputs rather than used to limit scientific coverage. Every unique MAIN group is represented in the assigned inventories; group membership and component counts were checked against the supplied article.

Direct supplied PDF identity is `jama_bluth_2019_oi_190055_16092.pdf`. Physical page numbers are one-based, with printed pages 2292–2305 corresponding to physical pages 1–14. Source text was independently streamed with recorded-available Poppler `pdftotext -layout`: pages 1–2 for abstract, Key Points and design; 3–4 for flow, definitions, power and all statistical methods; 5–6 for every Table 1 vector; 7–8 for every Table 2 vector and related narrative; 9–10 for every Table 3 vector, footnote and Figure 2 vector; and 11–12 for matched claims and conclusions. These source reads create no persistent derivative and preserve source/reusable assets. Pages 13–14 have no trial-result relationship according to the complete page map; those administrative/reference units are covered by the mapper's native-text inspection, not by invented S rows.

Reproduction commands from the package root:

```bash
pdftotext -f 3 -l 4 -layout jama_bluth_2019_oi_190055_16092.pdf -
pdftotext -f 5 -l 6 -layout jama_bluth_2019_oi_190055_16092.pdf -
pdftotext -f 7 -l 8 -layout jama_bluth_2019_oi_190055_16092.pdf -
pdftotext -f 9 -l 10 -layout jama_bluth_2019_oi_190055_16092.pdf -
```

Main source links: [abstract](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), [design](../../../jama_bluth_2019_oi_190055_16092.pdf#page=2), [flow and original power](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), [methods](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), [Table 1 first page](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), [Table 1 continuation](../../../jama_bluth_2019_oi_190055_16092.pdf#page=6), [Table 2 first page](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), [Table 2 continuation](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), [Table 3 first page](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), [Table 3 continuation and Figure 2](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), [discussion](../../../jama_bluth_2019_oi_190055_16092.pdf#page=11), [conclusions](../../../jama_bluth_2019_oi_190055_16092.pdf#page=12). Relative paths resolve from this quality directory.

Mechanical inventory checks using `awk` found exactly 79 assigned S headings, 79 full printed-vector fields, 79 PASS_1_COMPLETE fields and 79 PASS_2_COMPLETE fields, plus 79 explicit main S rows in each checker pass table. The numeric inventory has exactly 87 assigned N rows. All assigned S links identify the source PDF and applicable physical page; matched ancillary main locations remain in semantic keys and the main map.

## Both statistical passes and source coverage

The manifest identifies `runtime:/root/statistical_pass_1` and `runtime:/root/statistical_pass_2` as distinct fresh `gpt-6.1-sol`/`high` statistical agents with distinct durable pass artifacts. Both explicitly covered S001–S079, and each S full-vector record carries both completion statuses. `runtime:/root/inclusion_screener` is a different fresh `gpt-6.1-sol`/`high` agent. No pass-2 finding requires a pass-2 screener in this assigned scope. This confirms the recorded routing and coverage; platform runtime identity is represented by the canonical names returned in this interactive team, not an independent external execution attestation.

The main map documents 14 total physical source pages, 14 reusable-backed pages, zero fresh-required pages and 14 mapped pages. Thus reusable plus fresh-required equals total and mapped equals total for DOC-001. Its complete source-order local relationship union MAIN001–MAIN111 closes the quantitative mapping scope: descriptive groups MAIN001–MAIN032 and inferential/matched groups MAIN033–MAIN111. A grouped record is complete only with its full source vector; none was treated as a sample or a finding cap.

## Scientific rules and bounded calculations

All participant/event counts are exact; count-rounding bounds were considered only as an additional conservative sensitivity, never as the normal interpretation of integer counts. Percentage, summary and effect displays receive their half-unit precision intervals. Every printed effect is contained within its ordered interval. Main direction claims agree with the relevant signed differences, displayed ratio directions and forest favorable labels. Blank cells remain unreported.

Original power: the normal fixed-design diagnostic with control .40, treatment .30, two-sided alpha .05 and power .80 gives approximately 355.943 per arm. Supplied plan counts 356 per arm and 748 total admit `2 × 356 × 1.05 = 747.6`, rounded to 748. This shows compatible additive allowance arithmetic, not an explicitly supplied algorithm. Revised power retains the disclosed sequential design, control .20, RR .75 and maximum 1912; `1912/.95 = 2012.632`, rounded to 2013. A fixed-design diagnostic cannot reproduce or contradict the East sequential maximum. Actual interim statistics are not supplied; continuation cannot be replayed. Final primary `.23 > .044` supports no detected superiority. No noninferiority/equivalence margin or claim is supplied.

Flow: `1011+1002=2013`; `993+991=1984`; `18+11=29`; `4+4=8`; `1984−8=1976=989+987`; `43+29=72`, `61+14=75`; `989−72=917`, `987−75=912`; PP total 1829. These are distinct randomization, treatment, complete-case and PP populations. Subgroup contributors are not silently substituted for full-arm denominators.

All 33 Table 2 longitudinal mean contrasts were inspected individually. Their rounded means/differences admit compatible underlying values. Examples: first-hour PEEP difference 7.9 is compatible with rounded 12.0 and 4.0; first SpO2 difference .7 is compatible with rounded 98.2 and 97.4; rounded zero interval endpoints do not establish interval/P incompatibility. No row-specific variance, test or contributor count is supplied from convention. Medians are not subtracted as an established estimator for the table's reported difference. Driving pressure is defined as plateau pressure minus PEEP, not peak pressure minus PEEP.

Table 3 retains the stated binary RR/95% interval label and chi-square hypothesis testing separately from Cox HR and hospital-free-day mean difference exceptions. The registered quantity-identity pattern covers the main binary and forest block. For orientation only, primary incidence `(211/989)/(233/987)=.903748` versus printed `.93`; this does not assert the authors' implemented estimator. The allocation-orientation diagnostic is a different quantity and remains diagnostic. Existing ratio identity must not be presented as an exact code reconstruction or as a demonstrated change to the primary P=.23 conclusion. Component events overlap and are not summed into people. Sparse-cell interval/P comparisons do not impose an unprovided interval/test inversion.

All five interaction P values (.08, .97, .35, .11, .65) exceed .05 and align with the immediate no-significant-interaction claim. Stratum CIs are not sufficient to reconstruct a fitted binomial interaction test: link, covariance and implementation remain unavailable. Two full-arm partitions sum exactly for BMI, saturation and incision; type-of-surgery and waist-to-hip contributors remain explicit and incomplete without implying primary-outcome losses.

## Explicit S completion inventory

Every row below audits the full corresponding printed vector and its definitions, together with both fresh pass records. COMPLETE denotes audit coverage, not scientific adjudication. MAIN key is S number plus 32.

| S ID | MAIN key | Complete vector scope and audit result | Pass 1 | Pass 2 | Audit |
|---|---|---|---|---|---|
| S001 | MAIN033 | Original power inputs and dropout arithmetic; compatible diagnostic, no prescribed algorithm inferred | COMPLETE | COMPLETE | COMPLETE |
| S002 | MAIN034 | Revised power, 618-person review and sequential monitoring; actual interim statistics absent | COMPLETE | COMPLETE | COMPLETE |
| S003 | MAIN035 | Primary .044, secondary .05 and exploratory multiplicity; primary .23 exceeds final threshold | COMPLETE | COMPLETE | COMPLETE |
| S004 | MAIN036 | ITT/complete-case/PP populations and withdrawal; flow totals reproduce | COMPLETE | COMPLETE | COMPLETE |
| S005 | MAIN037 | Primary binary RR/interval/chi-square methods; registered identity pattern retained | COMPLETE | COMPLETE | COMPLETE |
| S006 | MAIN038 | Primary Kaplan–Meier/Cox/PH methods; distinct estimand, missing event times named | COMPLETE | COMPLETE | COMPLETE |
| S007 | MAIN039 | Site-random-effect and composite sensitivities; no equality of distinct coefficients imposed | COMPLETE | COMPLETE | COMPLETE |
| S008 | MAIN040 | Other binary result methods and exceptions; registered identity pattern retained | COMPLETE | COMPLETE | COMPLETE |
| S009 | MAIN041 | Hospital-free-day t/mean-difference specification; interval and P compatible at supplied precision | COMPLETE | COMPLETE | COMPLETE |
| S010 | MAIN042 | Five-day Cox mortality specification; no crude-RR substitution | COMPLETE | COMPLETE | COMPLETE |
| S011 | MAIN043 | All five binary interaction partitions; no link/covariance inferred | COMPLETE | COMPLETE | COMPLETE |
| S012 | MAIN044 | PP, adjustment, composite and abdominal subgroup claims; model/population distinctions retained | COMPLETE | COMPLETE | COMPLETE |
| S013 | MAIN045 | All three tidal-volume summary/SD/difference/CI/P vectors; rounding admits compatibility | COMPLETE | COMPLETE | COMPLETE |
| S014 | MAIN046 | All three PEEP vectors and first-hour matched narrative; positive direction and precision agree | COMPLETE | COMPLETE | COMPLETE |
| S015 | MAIN047 | Recruitment any-use, three occasions and median/IQR; overlapping occasions not partition totals | COMPLETE | COMPLETE | COMPLETE |
| S016 | MAIN048 | All three peak-pressure vectors; positive H−L directions and intervals agree | COMPLETE | COMPLETE | COMPLETE |
| S017 | MAIN049 | All three driving-pressure vectors and definition; negative direction agrees | COMPLETE | COMPLETE | COMPLETE |
| S018 | MAIN050 | All three respiratory-rate vectors; rounded upper zero and .02 can coexist | COMPLETE | COMPLETE | COMPLETE |
| S019 | MAIN051 | All three FiO2 fraction vectors; later negative contrasts and units retained | COMPLETE | COMPLETE | COMPLETE |
| S020 | MAIN052 | All three SpO2 vectors; positive contrasts, summaries and precision agree | COMPLETE | COMPLETE | COMPLETE |
| S021 | MAIN053 | All three CO2 vectors; interval order/containment and positive directions agree | COMPLETE | COMPLETE | COMPLETE |
| S022 | MAIN054 | All three heart-rate vectors; locally resolved printed name and final negative effect | COMPLETE | COMPLETE | COMPLETE |
| S023 | MAIN055 | All three mean-arterial-pressure vectors; contained estimates and rounded mean differences | COMPLETE | COMPLETE | COMPLETE |
| S024 | MAIN056 | Both head-elevation categories, totals, percentages and shared .70 | COMPLETE | COMPLETE | COMPLETE |
| S025 | MAIN057 | Noninvasive ventilation vector; near-null contrast and ordered interval | COMPLETE | COMPLETE | COMPLETE |
| S026 | MAIN058 | Both anesthesia categories, full totals and shared .51 | COMPLETE | COMPLETE | COMPLETE |
| S027 | MAIN059 | Any epidural and both location rows; 80/81 nested denominators and separate shared tests | COMPLETE | COMPLETE | COMPLETE |
| S028 | MAIN060 | Blockade full vector and percentage context; no new identity issue | COMPLETE | COMPLETE | COMPLETE |
| S029 | MAIN061 | Monitoring fractions/CI/P; existing peripheral screening, no primary denominator consequence | COMPLETE | COMPLETE | COMPLETE |
| S030 | MAIN062 | Reversal fractions/CI/P; same monitoring/reversal pattern, no new issue | COMPLETE | COMPLETE | COMPLETE |
| S031 | MAIN063 | Both fluid/crystalloid median/IQR and difference vectors; estimator not supplied by subtraction | COMPLETE | COMPLETE | COMPLETE |
| S032 | MAIN064 | Colloid amount and any-use separately; ordered containing intervals | COMPLETE | COMPLETE | COMPLETE |
| S033 | MAIN065 | Urine median/IQR and contrast; reconstruction limited by absent estimator/data | COMPLETE | COMPLETE | COMPLETE |
| S034 | MAIN066 | All four blood-product vectors; counts, percentages, direction and intervals retained | COMPLETE | COMPLETE | COMPLETE |
| S035 | MAIN067 | Blood-loss mean/SD and difference; rounded inputs compatible | COMPLETE | COMPLETE | COMPLETE |
| S036 | MAIN068 | Temperature mean/SD and rounded zero estimate/endpoints; precision-compatible | COMPLETE | COMPLETE | COMPLETE |
| S037 | MAIN069 | Both duration vectors and PBW formulas; blanks/method limits retained | COMPLETE | COMPLETE | COMPLETE |
| S038 | MAIN070 | Primary PPC full vector and all main matches; identity registered, null conclusion separated | COMPLETE | COMPLETE | COMPLETE |
| S039 | MAIN071 | Mild respiratory full vector; registered definition and identity patterns retained | COMPLETE | COMPLETE | COMPLETE |
| S040 | MAIN072 | Moderate respiratory full vector; no actual membership change inferred | COMPLETE | COMPLETE | COMPLETE |
| S041 | MAIN073 | Severe respiratory full vector; containment/order/direction agree | COMPLETE | COMPLETE | COMPLETE |
| S042 | MAIN074 | Atelectasis full vector; negative direction and intervals agree | COMPLETE | COMPLETE | COMPLETE |
| S043 | MAIN075 | Pleural-effusion full vector and main narrative; positive direction, nominal test identified | COMPLETE | COMPLETE | COMPLETE |
| S044 | MAIN076 | New-infiltrate full vector; contained estimates and negative direction | COMPLETE | COMPLETE | COMPLETE |
| S045 | MAIN077 | Cardiopulmonary-edema full vector; source test/interval distinction retained | COMPLETE | COMPLETE | COMPLETE |
| S046 | MAIN078 | Bronchospasm full vector; common identity occurrence rather than separate finding | COMPLETE | COMPLETE | COMPLETE |
| S047 | MAIN079 | Infection equal-event vector; rounding/contributor totals do not add distinct finding | COMPLETE | COMPLETE | COMPLETE |
| S048 | MAIN080 | Aspiration sparse-cell full vector; no specified rare-cell option inferred | COMPLETE | COMPLETE | COMPLETE |
| S049 | MAIN081 | ARDS full vector; positive direction, ordered intervals, registered identity | COMPLETE | COMPLETE | COMPLETE |
| S050 | MAIN082 | Pneumothorax full vector; negative direction, sparse options unprovided | COMPLETE | COMPLETE | COMPLETE |
| S051 | MAIN083 | Severe PPC full vector; mild-exclusion definition retained without reclassification claim | COMPLETE | COMPLETE | COMPLETE |
| S052 | MAIN084 | Extrapulmonary composite full vector; binary and Cox estimands kept distinct | COMPLETE | COMPLETE | COMPLETE |
| S053 | MAIN085 | SIRS full vector; positive direction and ordered intervals | COMPLETE | COMPLETE | COMPLETE |
| S054 | MAIN086 | Sepsis full vector; containment/order and source method limits retained | COMPLETE | COMPLETE | COMPLETE |
| S055 | MAIN087 | Severe-sepsis full vector; negative direction and registered identity | COMPLETE | COMPLETE | COMPLETE |
| S056 | MAIN088 | Septic-shock full vector; near-null sparse-cell options not inferred | COMPLETE | COMPLETE | COMPLETE |
| S057 | MAIN089 | GI any-use and all four grades; explicit 49/46 totals and one distribution P | COMPLETE | COMPLETE | COMPLETE |
| S058 | MAIN090 | Kidney any-use and all four grades; exact 31/32 totals and one distribution P | COMPLETE | COMPLETE | COMPLETE |
| S059 | MAIN091 | Extrapulmonary-infection full vector; positive direction and ordered intervals | COMPLETE | COMPLETE | COMPLETE |
| S060 | MAIN092 | Hepatic-failure equal-event vector; common-block context retained | COMPLETE | COMPLETE | COMPLETE |
| S061 | MAIN093 | Coma equal-event sparse vector; ordered interval and no added finding | COMPLETE | COMPLETE | COMPLETE |
| S062 | MAIN094 | DIC 1/0, finite ratio/CI and >.99; identity registered, separate inversion conditional | COMPLETE | COMPLETE | COMPLETE |
| S063 | MAIN095 | MI zero/zero and all blank effect/CI/P cells; no manufactured zero test | COMPLETE | COMPLETE | COMPLETE |
| S064 | MAIN096 | Wound-healing full vector; negative direction and ordered intervals | COMPLETE | COMPLETE | COMPLETE |
| S065 | MAIN097 | Unexpected ICU full vector; positive direction, endpoint window retained | COMPLETE | COMPLETE | COMPLETE |
| S066 | MAIN098 | Both hospital-free-day summaries and repeated mean difference; t-test exception explicit | COMPLETE | COMPLETE | COMPLETE |
| S067 | MAIN099 | Hypoxemia full vector and abstract occurrence; local missing-minus context resolves | COMPLETE | COMPLETE | COMPLETE |
| S068 | MAIN100 | Hypotension full vector; positive difference/ratio matches narrative | COMPLETE | COMPLETE | COMPLETE |
| S069 | MAIN101 | Bradycardia full vector; positive difference/ratio and .001 match narrative | COMPLETE | COMPLETE | COMPLETE |
| S070 | MAIN102 | Hospital mortality full vector; distinct window from five-day Cox outcome | COMPLETE | COMPLETE | COMPLETE |
| S071 | MAIN103 | Rescue full vector; negative direction and post hoc designation retained | COMPLETE | COMPLETE | COMPLETE |
| S072 | MAIN104 | Vasoactive full vector; positive H−L direction and fewer-L narrative agree | COMPLETE | COMPLETE | COMPLETE |
| S073 | MAIN105 | Five-day mortality full vector; explicit Cox exception and .48/.484 precision match | COMPLETE | COMPLETE | COMPLETE |
| S074 | MAIN106 | Both surgical strata and .08 interaction; partial contributors not full-arm losses | COMPLETE | COMPLETE | COMPLETE |
| S075 | MAIN107 | Both BMI strata and .97 interaction; full-arm/event partition totals reproduce | COMPLETE | COMPLETE | COMPLETE |
| S076 | MAIN108 | Both saturation strata and .35 interaction; full-arm/event partition totals reproduce | COMPLETE | COMPLETE | COMPLETE |
| S077 | MAIN109 | Both incision strata and .11 interaction; full-arm/event partition totals reproduce | COMPLETE | COMPLETE | COMPLETE |
| S078 | MAIN110 | Both waist-to-hip strata and .65 interaction; explicit contributors and local unit context | COMPLETE | COMPLETE | COMPLETE |
| S079 | MAIN111 | All-patient vector, forest axes and main subgroup claim; exact primary match | COMPLETE | COMPLETE | COMPLETE |

## Explicit N completion inventory

Each row audits every printed component of the referenced current N record. Codes describe completed audit work, not outcomes or scientific dispositions: D = descriptive counts, denominators, partitions, units and precision; F = flow and matched totals; K = design/population/endpoint/method keys; T = all table summaries, differences, dispersion and units; B = full binary count/percentage/difference/effect/interval vector, with registered identity pattern retained; G = nested grade partitions and explicit denominator; H = hospital-free-day mean/median exception; X = five-day Cox exception; U = full subgroup counts, partitions, direction and displayed effect vector. Every applicable code includes source transcription and contextual inclusion review. No code supplies a missing test or analysis denominator.

| N ID | MAIN groups | Checks | Audit |
|---|---|---|---|
| N001 | MAIN001 | D | COMPLETE |
| N002 | MAIN002 | D | COMPLETE |
| N003 | MAIN003 | D | COMPLETE |
| N004 | MAIN004 | D | COMPLETE |
| N005 | MAIN005 | D | COMPLETE |
| N006 | MAIN006 | D | COMPLETE |
| N007 | MAIN007 | D | COMPLETE |
| N008 | MAIN008 | D | COMPLETE |
| N009 | MAIN009 | D | COMPLETE |
| N010 | MAIN010 | D | COMPLETE |
| N011 | MAIN011 | D | COMPLETE |
| N012 | MAIN012 | D | COMPLETE |
| N013 | MAIN013 | D | COMPLETE |
| N014 | MAIN014 | D | COMPLETE |
| N015 | MAIN015 | D | COMPLETE |
| N016 | MAIN016 | D | COMPLETE |
| N017 | MAIN017 | D | COMPLETE |
| N018 | MAIN018 | D | COMPLETE |
| N019 | MAIN019 | D | COMPLETE |
| N020 | MAIN020 | D | COMPLETE |
| N021 | MAIN021 | D | COMPLETE |
| N022 | MAIN022 | D, K | COMPLETE |
| N023 | MAIN023 | F | COMPLETE |
| N024 | MAIN024 | F | COMPLETE |
| N025 | MAIN025 | F | COMPLETE |
| N026 | MAIN026 | D, F | COMPLETE |
| N027 | MAIN027, MAIN028, MAIN029 | K | COMPLETE |
| N028 | MAIN030, MAIN031, MAIN032 | K | COMPLETE |
| N029 | MAIN033, MAIN034, MAIN035, MAIN036 | F, K | COMPLETE |
| N030 | MAIN037, MAIN038, MAIN039, MAIN040, MAIN041, MAIN042, MAIN043, MAIN044 | K | COMPLETE |
| N031 | MAIN045, MAIN046, MAIN047, MAIN048, MAIN049, MAIN050, MAIN051, MAIN052, MAIN053, MAIN054, MAIN055 | T | COMPLETE |
| N032 | MAIN056 | D, T | COMPLETE |
| N033 | MAIN057 | D, T | COMPLETE |
| N034 | MAIN058 | D, T | COMPLETE |
| N035 | MAIN059 | D, T | COMPLETE |
| N036 | MAIN060 | D, T | COMPLETE |
| N037 | MAIN061 | D, T; monitoring pattern already screened | COMPLETE |
| N038 | MAIN062 | D, T; reversal pattern already screened | COMPLETE |
| N039 | MAIN063 | T | COMPLETE |
| N040 | MAIN064 | D, T | COMPLETE |
| N041 | MAIN065 | T | COMPLETE |
| N042 | MAIN066 | D, T | COMPLETE |
| N043 | MAIN067 | T | COMPLETE |
| N044 | MAIN068 | T | COMPLETE |
| N045 | MAIN069 | T, K | COMPLETE |
| N046 | MAIN070 | B | COMPLETE |
| N047 | MAIN071 | B, K | COMPLETE |
| N048 | MAIN072 | B, K | COMPLETE |
| N049 | MAIN073 | B | COMPLETE |
| N050 | MAIN074 | B | COMPLETE |
| N051 | MAIN075 | B | COMPLETE |
| N052 | MAIN076 | B | COMPLETE |
| N053 | MAIN077 | B | COMPLETE |
| N054 | MAIN078 | B | COMPLETE |
| N055 | MAIN079 | B | COMPLETE |
| N056 | MAIN080 | B | COMPLETE |
| N057 | MAIN081 | B | COMPLETE |
| N058 | MAIN082 | B | COMPLETE |
| N059 | MAIN083 | B, K | COMPLETE |
| N060 | MAIN084 | B | COMPLETE |
| N061 | MAIN085 | B | COMPLETE |
| N062 | MAIN086 | B | COMPLETE |
| N063 | MAIN087 | B | COMPLETE |
| N064 | MAIN088 | B | COMPLETE |
| N065 | MAIN089 | B, G | COMPLETE |
| N066 | MAIN090 | B, G | COMPLETE |
| N067 | MAIN091 | B | COMPLETE |
| N068 | MAIN092 | B | COMPLETE |
| N069 | MAIN093 | B | COMPLETE |
| N070 | MAIN094 | B | COMPLETE |
| N071 | MAIN095 | D; all inferential blanks preserved | COMPLETE |
| N072 | MAIN096 | B | COMPLETE |
| N073 | MAIN097 | B | COMPLETE |
| N074 | MAIN098 | H | COMPLETE |
| N075 | MAIN099 | B; abstract sign context retained | COMPLETE |
| N076 | MAIN100 | B | COMPLETE |
| N077 | MAIN101 | B | COMPLETE |
| N078 | MAIN102 | B | COMPLETE |
| N079 | MAIN103 | B | COMPLETE |
| N080 | MAIN104 | B | COMPLETE |
| N081 | MAIN105 | X | COMPLETE |
| N082 | MAIN106 | U | COMPLETE |
| N083 | MAIN107 | U | COMPLETE |
| N084 | MAIN108 | U | COMPLETE |
| N085 | MAIN109 | U | COMPLETE |
| N086 | MAIN110 | U | COMPLETE |
| N087 | MAIN111 | U | COMPLETE |

## Excluded observations audit

All pass-1 and pass-2 excluded tables were read; the main-bearing observations were independently checked in both directions. None meets all four inclusion criteria as a new distinct issue. Existing candidate patterns are retained by the lead and are not suppressed. Observations from support-only S080 onward are outside this disjoint shard and belong to the support auditor.

| Main scope / location | Audited observation and reason threshold is not met | Reason code |
|---|---|---|
| S001, N029; original power | Additive allowance arithmetic reconciles supplied counts; the exact dropout convention is not explicitly stated and is not imposed | CONTEXT_RESOLVES |
| S002, N029; revised power | Fixed-design normal approximation cannot replace the disclosed sequential maximum or demonstrate a mismatch | CONDITIONAL_OR_UNREPORTED |
| S002; monitoring | Actual interim statistics are absent; supplied boundaries alone cannot establish a contradictory observed decision | CONDITIONAL_OR_UNREPORTED |
| S004, N023–N026; population | Disclosed exclusions and complete cases explain analyzed-set missingness and 989/987; no alternate primary denominator | CONTEXT_RESOLVES |
| S013–S023, S035–S036, N031, N043–N044 | Rounded means/differences/zero endpoints admit compatible underlying quantities | ROUNDING_OR_DISPLAY_PRECISION |
| S013–S037; Table 2 | Missing row tests, variance choices and contributors do not establish a contradicted result | CONDITIONAL_OR_UNREPORTED |
| S031–S033, S037; medians | Printed medians do not establish the contrast estimator or underlying participant distribution | CONDITIONAL_OR_UNREPORTED |
| S022, S078, N017; labels/units | Heart-rate values, ratio cutoffs and clinical lab scale identify intended label/unit immediately | NOTATION_OR_TYPOGRAPHY |
| S062, N070; DIC | Separate CI/P incompatibility requires unprovided sparse-cell interval/test assumptions; declared identity already lies within the registered pattern | CONDITIONAL_OR_UNREPORTED |
| S067, N075; abstract sign | Point −8.6, lower −11.1, P<.001 and matched table −6.1 identify the intended minus immediately | NOTATION_OR_TYPOGRAPHY |
| N001–N022, N066; percentage last digits | Explicit exact counts/denominators determine the value at once; no primary/key result/population choice is unclear | CONTEXT_RESOLVES |
| N026; abstract allocation wording | Completed 1976 and flow 1011/1002 with exclusions identify analyzed 989/987 immediately | CONTEXT_RESOLVES |
| N020, N026; abdominal fractions | Descriptive fractions do not change primary 989/987 or key-secondary event denominators; pooled 1778/1973 gives 90.1% | PERIPHERAL_COMPARISON |
| N002, N020, N082–N086; subgroup contributors | Cutoffs and variable-specific complete cases differ; no contradictory primary-analysis total follows | PERIPHERAL_COMPARISON |
| S029–S030, N037–N038; monitoring/reversal | Existing screened pattern concerns procedural contributor fractions, with no changed primary/key secondary result, analysis-population size or planned decision rule | PERIPHERAL_COMPARISON |
| S057–S058, N065–N066; graded outcomes | Explicit subset grade denominators are not asserted complete for all any-event cases; a missing grade is not an absent outcome | CONDITIONAL_OR_UNREPORTED |
| S006–S007, S010, S012, S073; Cox and sensitivity matches | Separate Cox, random-effect and composite estimates are not required to equal the binary vector or each other | MODEL_VERSUS_CRUDE |

No finding rests on a P value displayed as zero. No display-zero observation was promoted. All scientific observations were assessed on the stated threshold, without a requested or expected candidate number.

## Supportable record repairs and coordinator handoff

The following are record clarifications, not new scientific findings. Inputs are preserved by this shard; repairs to shared current-run records are owned by the coordinator.

Coordinator handoff completed: both requested clarifications were applied in the current numeric inventory and pass-2 checker record; the S001 pass-1 allowance explanation was also qualified. The repaired snippets were reread. The coordinator recorded the reasons in run_state.md. Stable IDs, evidence vectors, coverage assignments and screening decisions were unchanged.

| Repair request | Reason | Effect on scientific coverage or registration |
|---|---|---|
| In pass-2 original-power exclusion, replace “supplied additive allowance convention” with “additive allowance arithmetic consistent with the supplied 356-per-arm and 748 totals,” or equivalent | The source supplies counts and five-percent dropout but does not explicitly state the calculation algorithm; distinguish reproduced arithmetic from inferred convention | No new finding; both power records remain covered |
| In N037 and N038, state two count/denominator/percentage pairs per row and four across the consolidated monitoring/reversal pattern | Each N row contains two arm fractions; “all four” is only accurate for the combined pattern | No new finding or candidate; existing peripheral screen remains covered |

## Limits

This shard confirms the complete assigned numeric/statistical maps and main-bearing exclusion logic. It does not claim independent reproduction of participant-data statistics, event-time models, unknown variance/test implementations, subgroup covariance, implemented endpoint field values or actual interim decisions. Those inputs are absent in the package and were named rather than inferred. It does not independently reopen administrative/reference pages with no result relationship after the mapper's documented unit inspection. Source hashes, all direct-source coverage rows, screening cardinality, candidate classifications, full stable-ID inclusion audit and report-card equality are lead-auditor responsibilities. No paper-level or unbounded downstream consequence is inferred here. All candidates remain Pending Human Adjudication; this artifact assigns no severity or disposition and no human-adjudication subfields.
