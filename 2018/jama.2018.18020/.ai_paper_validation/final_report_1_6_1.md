# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.1

**Pending Human Adjudication**

This review identifies candidate reporting issues in the supplied paper package. Evidence states and inclusion audits describe the review record; human reviewers determine validity, importance and action. All four candidates remain Pending Human Adjudication.

## Executive Quality-Control Summary

Complete review of four supplied PDFs, comprising 83 physical pages, identified **4 stable candidates: C001, C002, C003 and C004**. Three concern quantitative or statistical results within the main article; one concerns an explicit prospective-versus-reported Bayesian variance-prior specification. Every candidate has reproduced direct-source evidence and a CONFIRMED inclusion audit. These findings do not establish a change in the paper's conclusions or a downstream consequence.

The candidates concern the INQoL score scale and summaries, the Bayesian variance-prior family, paired-t confidence-interval/P-value compatibility in two secondary outcome rows, and the primary CLCN1 graphical versus narrative summary. Seven checker findings received independent inclusion decisions: four INCLUDE and three SCREENED_OUT. Two screened findings duplicate included issues; one is resolved by immediate context. No screened-out finding receives a separate evidence card.

## Package and Reused-Evidence Provenance

The package reports aggregated N-of-1 trials of mexiletine in nondystrophic myotonia. Source roles were assigned by content. The prospective protocol is PLAN even though supplied as a supplement; the results supplement and retrospective data-sharing statement are REPORT.

| Source ID | Actual supplied filename | Role | Physical pages | SHA-256 |
|---|---|---|---:|---|
| DOC-001 | jama_stunnenberg_2018_oi_180136.pdf | REPORT | 10 | 4cfcd14bc825f4bd96a4f072dffc4c9a38f316c68d8bb778226bd7c521e9919f |
| DOC-002 | joi180136supp1_prod.pdf | PLAN | 55 | 79ba649c5d57a953b46ee5a550cf6f9ba17f784864bc486b75f50cb96292622f |
| DOC-003 | joi180136supp2_prod.pdf | REPORT | 17 | 9a88d1fbef0b8fab112d6b22f53591444c9a73e66b0e69a7de292f9716e3a208 |
| DOC-004 | joi180136supp3_prod.pdf | REPORT | 1 | 86b09282d61f560447283d78f9aeacee958ee531282e336e1c9114618d2d48db |

Fresh discovery reused 95 extraction assets below `.ai_paper_validation/review_1_5_2/preprocessing/`: four native-text files, four layout-text files, four metadata records and 83 rendered PNG pages. Their assessed fitness was 88 USABLE, six PARTIAL and one DUPLICATE; no STALE or UNREADABLE asset was recorded. Complementary images cover graphical content absent from partial text. Form-feed record N locates physical PDF page N; trailing empty records do not add pages. No existing OCR, standalone table/workbook extraction or separate source-location map was found.

Current Poppler native-text and metadata streams matched all four reusable source families byte for byte. Two layout streams differed in rotated-label placement while retaining identical token histograms; spatial reading used page images. Legacy image-generator versions are unknown, and complete PNG pixel identity is not asserted. Supplied PDFs remained final authority. Thirteen current-run Poppler renders supplied targeted visual confirmation and have individual source/page/engine records. Sources and reused assets were preserved; prior scientific candidate sets, screening decisions and reports were excluded from discovery inputs.

Durable provenance: [source inventory](review_1_6_1/source_inventory.md), [evidence-asset inventory](review_1_6_1/evidence_asset_inventory.md), [source before-hash manifest](review_1_6_1/source_hashes_before.sha256), and [reused-asset before-hash manifest](review_1_6_1/reused_artifact_hashes_before.sha256).

## Scope, Complete Coverage, and Exclusions

Review covered counts and denominators, estimate and test logic, statistical method logic, and planned versus reported statistical design. Every direct-source page was mapped, including figures, tables, model code, simulation cells, background, references and administrative pages. Pages without applicable quantitative relationships have explicit coverage records. There is no scientific source-coverage gap.

| Source | Total pages | Reusable-backed | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | 55 | 55 | 0 | 55 | COMPLETE |
| DOC-003 | 17 | 17 | 0 | 17 | COMPLETE |
| DOC-004 | 1 | 1 | 0 | 1 | COMPLETE |
| **Total** | **83** | **83** | **0** | **83** | **COMPLETE** |

Reusable-backed and fresh-required counts partition each source total; mapped counts equal totals. Zero fresh-required pages describes preprocessing availability, while scientific mapping and targeted direct-source rereading were fresh review stages. No Office, workbook or CSV source was supplied. See [source coverage](review_1_6_1/source_coverage.md) and [coverage manifest](review_1_6_1/coverage_manifest.md).

Display precision, immediately interpretable notation or terminology, model-versus-crude differences, conditional or unreported details, peripheral comparisons and matters outside the specified quantitative scope were excluded under the scope contract. Peripheral comparisons qualify only if they change a primary/key-secondary result, analysis-population size or planned decision rule. This review does not perform a raw-data, broad design, clinical, novelty or misconduct audit, and proposes no preferred analysis. Only supplied package evidence was used.

## Quantitative and Statistical Relationship Coverage

The complete maps contain **39 numeric parent families**: N001–N028 in the main article and N101–N111 in support material. Statistical coverage comprises **103 parent relationships**: S001–S092 and S101–S111, together with **27 subordinate individual-result tuples under S107**. Grouping preserves every subordinate row, marker and cell.

Coverage includes all 14 main baseline comparison rows, 34 main outcome/group rows, four interaction rows, 27 Figure 2 participant markers and three group markers, all Figure 3 panels and 54 sequential markers, 30 supplementary baseline patients, 27 individual primary outcomes, 12 adverse-reaction/category rows, four supplementary posterior density curves, all three printed Bayesian models, and both complete simulation summaries and decision-frequency tables. Numeric checks retain all 96 simulation-summary cells and 12 valid/missing pairs. Counts, scales, effects, intervals, tests, contrasts, analysis populations, priors, stopping rules, multiplicity and prospective design specifications were reviewed with their source-linked definitions.

Statistical pass 1 ran in fresh runtime `root/statistics_pass_1`; pass 2 ran after the complete ledger, screening and recheck in distinct fresh runtime `root/statistics_pass_2`. Both used `gpt-6.1-sol`/`high` and covered all 103 parent relationships and all 27 S107 tuples. All 130 parent/subordinate records contain PASS_1_COMPLETE and PASS_2_COMPLETE. Pass 2 emitted no new finding, so a second inclusion screen was not applicable. Exact reconstruction limits were named without removing those relationships from coverage.

The three disjoint quality-audit scopes were merged losslessly into the [canonical evidence-quality audit](review_1_6_1/quality/evidence_quality_audit.md). It confirms complete page, numeric, statistical, candidate and screening coverage. The maps and registers are available as [main evidence](review_1_6_1/extraction/main_quantitative_evidence.md), [support evidence](review_1_6_1/extraction/support_quantitative_evidence.md), [numeric inventory](review_1_6_1/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_6_1/statistics/relationship_inventory.md), [pass 1](review_1_6_1/checkers/statistical_pass_1.md), and [pass 2](review_1_6_1/checkers/statistical_pass_2.md).

## Inclusion Screening Summary

A finding was included only if reproduced from exact supplied locations, in focus, unresolved by immediate context for a statistically literate field reader, and plausibly relevant to interpretation or extraction of a named result. The independent screen reread cited source locations and consolidated repeated issues. Counts reconcile to the seven rows in the [screening log](review_1_6_1/screening/inclusion_screen.md).

| Decision | Reason code | Findings |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 4 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 2 |
| SCREENED_OUT | CONTEXT_RESOLVES | 1 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| **Total screened** | **4 included + 3 screened out** | **7** |

F-NUM-001 maps to C001; F-XS-002 to C002; F-ST1-001 to C003; F-XS-001 to C004. F-ST1-002 and F-ST1-003 are screened duplicates of C002 and C004 respectively, with their provenance and locations retained under those issues. F-XS-003 is screened out as CONTEXT_RESOLVES because the protocol's nonexclusive general and cardiac safety guidance can coexist and its shared three-patient parenthesis identifies the intended boundary.

Checker self-exclusions are separate from the seven finding decisions: numeric 21, cross-source 20, statistical pass 1 22, and statistical pass 2 23, totaling **86 observations**. All seven screening decisions and all 86 exclusions were audited in both directions; no audit reversal or additional candidate was required. The numeric 5/11-versus-46% documentation was clarified using the explicit count and denominator, without changing a stable ID.

## Review-Domain Summary

`statistical_results` covers counts, estimates, intervals, tests and statistical method logic in REPORT material. `report_internal_inconsistency` covers conflicting attribution of a number to an outcome, time point, analysis set or comparison within REPORT material. `protocol_report` covers statistical design or analysis differences between PLAN and REPORT. `plan_material` covers plan-internal statistical design inconsistencies relied upon by the reported analysis.

| Review domain | Candidates |
|---|---:|
| statistical_results | 3 |
| report_internal_inconsistency | 0 |
| protocol_report | 1 |
| plan_material | 0 |
| **Total** | **4** |

| Primary relationship type | Meaning | Candidates |
|---|---|---:|
| S_W | Within one REPORT document | 3 |
| S_C | Between distinct REPORT documents | 0 |
| P_R | PLAN versus REPORT | 1 |
| P_P | Within PLAN material | 0 |
| **Total** | | **4** |

Each candidate has only its listed primary relationship in All relationships; corroboration adds no conflicting relationship. Mixed-type precedence P_R > P_P > S_C > S_W therefore requires no competing selection here.

| Evidence state | Candidates |
|---|---:|
| reproduced | 4 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **4** |

Inclusion audits: CONFIRMED = 4; QUESTIONED = 0. These are review-record fields, not human adjudications.

## Candidate Index

| ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | INQoL score scale and summaries | statistical_results | S_W | reproduced | CONFIRMED |
| C002 | Bayesian variance-prior specification | protocol_report | P_R | reproduced | CONFIRMED |
| C003 | Paired-t interval/P compatibility | statistical_results | S_W | reproduced | CONFIRMED |
| C004 | Primary CLCN1 graphic/narrative summary | statistical_results | S_W | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — INQoL score scale and reported summaries do not reconcile

**Status: Pending Human Adjudication**

**Candidate statement:** The repeatedly stated 0–100 INQoL composite range does not reconcile with two subgroup upper quartiles above 100 or the overall baseline mean/SD, leaving the score unit attached to the reported summaries and treatment contrast unclear.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article scale definitions vs REPORT main article INQoL summaries

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Classification rationale:** Scale definitions and conflicting summaries are within the same REPORT document. The issue concerns quantitative scale/dispersion logic, so the domain is statistical_results. No PLAN or distinct REPORT document supplies a conflicting comparator.

**Classification ambiguity:** None in document roles or relationship; the intended score transformation is unknown.

**Exact source locations:**

- [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 3, Outcomes](<../jama_stunnenberg_2018_oi_180136.pdf#page=3>): INQoL scale definition.
- [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 5, Table 1 INQoL row and footnote f](<../jama_stunnenberg_2018_oi_180136.pdf#page=5>): both affected genotype quartiles and repeated scale definition.
- [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 7, Table 2 INQoL row](<../jama_stunnenberg_2018_oi_180136.pdf#page=7>): overall baseline mean/SD and changes/treatment effect.
- [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 8, Table 2 footnote g](<../jama_stunnenberg_2018_oi_180136.pdf#page=8>): repeated scale definition.

**Source evidence:** Outcomes and both table footnotes define a 0–100 composite score, with higher values indicating greater disease severity. Table 1 reports CLCN1 N = 16, median 84.0 (IQR 74.5–110.3), and SCN4A N = 11, median 98.0 (IQR 56.0–120.0). Table 2's total NDM heading is N = 27; its INQoL baseline is 96.89 (SD 38.49), placebo change −7.22 (95% CI −14.5 to −0.29), mexiletine change −21.44 (−30.90 to −11.95), and treatment effect −14.22 (−24.71 to −3.74), P = .01.

**Reported-versus-comparator:** Upper quartiles 110.3 and 120.0 and baseline 96.89 (SD 38.49) are compared with the repeatedly printed 0–100 observation range. Treatment changes and the −14.22 contrast are affected by the unresolved unit; the contrast itself is not asserted to violate a bounded-change rule.

**Reasoning procedure:** Quartiles of observations bounded by 0 and 100 remain within those limits. Independently, x² ≤ 100x for each bounded observation; therefore sample variance satisfies s² ≤ [n/(n−1)] m(100−m). Allow each displayed input its half-last-unit rounding interval before comparing the summaries with these necessary bounds. The all-n ≥ 2 bound avoids assigning an unreported baseline contributor count.

**Calculation:** Upper-quartile rounding intervals [110.25, 110.35] and [119.95, 120.05] remain wholly above 100. The mean interval is [96.885, 96.895] and SD interval [38.485, 38.495]. Over the mean interval, m(100−m) is largest at m = 96.885. At n = 27, s ≤ √[(27/26) × 96.885 × 3.115] = 17.703230, conservatively rounded upward to 17.704. For any integer n ≥ 2, n/(n−1) ≤ 2, giving s ≤ √[2 × 96.885 × 3.115] = 24.568141, conservatively 24.569. Both are below 38.485. Closed endpoints make these allowances conservative.

**Affected result or extracted value:** The INQoL baseline 96.89 (SD 38.49), the arm changes, and treatment effect −14.22 with 95% CI −24.71 to −3.74 require an identifiable score scale for extraction or comparison with other INQoL results.

**Why context does not resolve it:** The immediate definitions repeatedly specify 0–100. Neither defining text nor table footnotes supply a wider raw-score range or normalization formula that identifies the table unit. This is a quantity-changing scale issue attached to treatment reporting, rather than a peripheral comparison of descriptive baseline values.

**Alternative source-grounded interpretations:** A wider raw composite might be reported while the prose describes a normalized score, or the displayed summaries and scale designation might require clarification. The package does not select either explanation. No alternative range, transformation or replacement value is assigned.

**Mechanical evidence recheck:** All four locations and both genotype quartiles were directly matched to the supplied PDF. Direct layout rereading and source renders confirmed the text/table alignment. The quartile and sample-variance comparisons reproduced with full rounding allowances; necessary inputs are available without raw scores or an exact baseline contributor count. No source transcription or location revision was required. The numerical bounds are deductions from directly printed quantities; a wider raw score remains an inferred possible explanation. See the [C001 recheck](review_1_6_1/verification/evidence_recheck.md#c001).

**Potential downstream evidence impact:** If confirmed, an extractor could copy the baseline or treatment contrast with a scale designation that the reported summaries do not establish, affecting unit alignment or comparability. No propagation or change in a synthesis or trial conclusion is established.

**Human verification steps:** Inspect all four source locations, identify the scoring algorithm and any transformation used for Tables 1 and 2, and match both baseline and treatment outputs to that definition. Remaining question: Which score definition and transformation produced the tables' INQoL quantities, and on which explicitly defined scale should they be extracted?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Planned and reported Bayesian variance-prior families differ

**Status: Pending Human Adjudication**

**Candidate statement:** The prospective inverse-gamma variation-prior specification differs from the uniform standard-deviation priors printed in the individual, population and genotype model code for the reported Bayesian analyses.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol variance priors vs REPORT results supplement Bayesian model code

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

**Classification rationale:** The prospective variance-prior specification is PLAN; the results supplement's reported analysis model code is REPORT. P_R determines protocol_report. Main-article pointers and posterior results corroborate the relevance of that code without creating another conflicting relationship. Actual execution is not established by the printed code alone.

**Classification ambiguity:** A supplied analysis amendment or executed-model file could clarify the change; neither is supplied. No numerical prior influence is inferred.

**Exact source locations:**

- [joi180136supp1_prod.pdf — PDF p. 40, section 9.1](<../joi180136supp1_prod.pdf#page=40>): prospective hierarchical model and prior-elicitation context.
- [joi180136supp1_prod.pdf — PDF p. 41, variation priors and robustness paragraph](<../joi180136supp1_prod.pdf#page=41>): inverse-gamma variance specification and contextual robustness provision.
- [joi180136supp1_prod.pdf — PDF p. 42, interim analysis](<../joi180136supp1_prod.pdf#page=42>): noninformative interim branch.
- [joi180136supp2_prod.pdf — PDF p. 10, eMethods 1](<../joi180136supp2_prod.pdf#page=10>): both individual arm-SD prior statements and definitions.
- [joi180136supp2_prod.pdf — PDF p. 11, eMethods 2](<../joi180136supp2_prod.pdf#page=11>): population within-person and both arm-SD priors.
- [joi180136supp2_prod.pdf — PDF p. 12, eMethods 2 definitions](<../joi180136supp2_prod.pdf#page=12>): SD/precision and population contrast identities.
- [joi180136supp2_prod.pdf — PDF p. 13, eMethods 3](<../joi180136supp2_prod.pdf#page=13>): genotype within-person and both arm-SD priors.
- [joi180136supp2_prod.pdf — PDF p. 14, eMethods 3 definitions](<../joi180136supp2_prod.pdf#page=14>): genotype coding and common SD definitions.
- Corroboration: [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 3, Bayesian Analysis](<../jama_stunnenberg_2018_oi_180136.pdf#page=3>) and [PDF p. 4, primary posterior results](<../jama_stunnenberg_2018_oi_180136.pdf#page=4>).

**Source evidence:** The protocol specifies inverse-gamma distributions for variation parameters, with shape and scale both 0.001, after identifying means and variances. Report eMethods 1 gives `sigma_plac ~ dunif(0.01,10)` and `sigma_mex ~ dunif(0.01,10)`. Each of eMethods 2 and 3 gives `sigma.within`, `sigma.mex` and `sigma.plac` the same uniform prior. All eight occurrences link to precision through tau = 1/sigma², and definitions identify sigma as standard deviation. Population and genotype models share within-person variability; arm variability is shared across genotypes. The main article links the individual, aggregate and genotype analyses to these eMethods.

**Reported-versus-comparator:** The report's explicit uniform-SD priors induce a variance distribution distinct from the prospectively specified inverse-gamma variance family. The protocol's clinical-mean-prior elicitation, permitted noninformative robustness replacement and interim distinction are retained as context. Absence of a clinical-prior counterpart is not an independent candidate basis. F-ST1-002's reproduced variance-family component is screened DUPLICATE_OF_INCLUDED and retained as checker provenance for this same issue.

**Reasoning procedure:** Compare distributions on the same variance parameter, using the report's sigma-to-precision definitions. Transform the uniform SD prior to variance support and density, then compare with the inverse-gamma family. Establish only the printed specification difference; do not reconstruct posteriors, assume code execution or infer a numerical prior effect.

**Calculation:** For sigma ∼ Uniform(a,b), a = 0.01 and b = 10, v = sigma² has density f(v) = 1/[2(b−a)√v] on (a²,b²) = (0.0001,100). Under the usual inverse-gamma variance parameterization, the planned prior has density proportional to v^(−1.001) exp(−0.001/v) for every v > 0. Finite bounded support and the different density do not reconcile with positive unbounded inverse-gamma support. These are code/prior specifications rather than rounded measurements. Even broad finite endpoint rounding cannot equate bounded and unbounded support. Naming both noninformative does not make them the same distribution.

**Affected result or extracted value:** The documented analysis specification attached to individual primary stopping probabilities, clinically meaningful effectiveness in 24/27, and the primary posterior summaries: overall 3.06 (95% CrI 1.96–4.15), CLCN1 3.84 (2.52–5.16), SCN4A 1.94 (0.35–3.53), with meaningful-effect probabilities 100%, 100% and 93% respectively.

**Why context does not resolve it:** No supplied amendment or local explanation maps the explicit variance-family change. The permitted clinical-prior robustness branch does not specify replacing inverse-gamma variation priors with uniform-SD priors, and the interim noninformative description does not identify that replacement either. Thus the package does not uniquely establish which variation specification produced each primary output.

**Alternative source-grounded interpretations:** The published code could be illustrative or represent a later amended implementation. The protocol permits noninformative replacement for robustness. Neither an illustrative-code distinction nor a variance-family amendment is supplied. These possibilities do not establish actual execution or a change in any numerical result; no preferred prior is proposed.

**Mechanical evidence recheck:** Direct-source rereading located protocol pp. 40–42 and results pp. 10–14; source renders confirmed the protocol distribution and all eight reported uniform-SD statements. SD/precision identities and the induced variance density/support reproduced. Main pp. 3–4 corroborate the code's reported-analysis role and named outputs. Necessary specification inputs are available; executed model files, run identifiers, result-to-prior mapping and any amendment are absent. No source-value/location revision was required. See the [C002 recheck](review_1_6_1/verification/evidence_recheck.md#c002).

**Potential downstream evidence impact:** If confirmed, an evidence review could extract a different documented prior family for the individual, population or genotype primary analyses depending on which source it uses. The package does not establish a posterior-magnitude, stopping-decision or paper-conclusion change.

**Human verification steps:** Inspect each prospective and reported prior statement, obtain the executed model files and run identifiers, and map them to the individual, population and genotype primary outputs and any documented amendment. Remaining question: Which variation priors were executed for those three analyses, and what documented specification or amendment links them to the prospective inverse-gamma variation priors?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Paired-t P values and confidence intervals do not reconcile

**Status: Pending Human Adjudication**

**Candidate statement:** Two Table 2 total-group secondary effects have printed P values that do not reconcile with their 95% confidence intervals under the stated common two-sided dependent-t analysis, after full display-precision allowances.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article dependent-t methods vs REPORT main article SF-36 mental and needle-EMG statistics

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-001

**Classification rationale:** The stated methods, sidedness and affected test/interval tuples are REPORT content within the same article. The issue concerns estimate/test/interval logic, so the domain is statistical_results. The two rows form one repeated compatibility pattern.

**Classification ambiguity:** Row-specific paired counts, degrees of freedom and executed output are absent; the calculation uses necessary bounds valid without assigning them.

**Exact source locations:**

- [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 3, Frequentist Analysis](<../jama_stunnenberg_2018_oi_180136.pdf#page=3>): dependent-t effects, significance levels and confidence intervals.
- [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 4, Frequentist Analysis continuation](<../jama_stunnenberg_2018_oi_180136.pdf#page=4>): two-sided, unadjusted exploratory secondary tests.
- [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 7, Table 2 SF-36 mental component row](<../jama_stunnenberg_2018_oi_180136.pdf#page=7>): first affected tuple.
- [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 8, needle-EMG row and Table 2 footnote a](<../jama_stunnenberg_2018_oi_180136.pdf#page=8>): second affected tuple and repeated method attribution.

**Source evidence:** Methods state that dependent t tests calculate total-group mean treatment effects, significance levels and confidence intervals for other normally distributed secondary outcomes; all P values are two-sided and secondary tests are unadjusted/exploratory. Table 2 gives SF-36 mental effect 6.78 (95% CI 1.64–11.92), P = .001, and needle EMG effect 0.67 (95% CI 0.23–1.11), P < .001. Footnote a separates IVR linear mixed-model analysis from dependent-t analysis of the other secondary mean effects.

**Reported-versus-comparator:** Each printed treatment-effect P value is compared with its own effect and 95% CI under the source-stated same two-sided dependent-t procedure. This does not compare peripheral secondary values across displays or impose a common sample size from the N = 27 heading.

**Reasoning procedure:** For a two-sided t test of zero and its corresponding 95% t confidence interval, h = (U−L)/2 = t_(.975,ν) × SE and |d|/h = |t_observed|/t_(.975,ν). For any positive Student-t degrees of freedom, the necessary small-P quantile ratio is no smaller than its normal-limit counterpart. Maximize |d| and minimize h within independent half-last-unit rounding intervals; this permits more combinations than exact midpoint constraints and gives conservative upper bounds. Compare these maxima with the weakest necessary thresholds for the printed P displays.

**Calculation:**

| Row | Printed ratio | Maximum with ±0.005 input allowances | Necessary normal-limit threshold | Comparison |
|---|---|---|---|---|
| SF-36 mental | h = (11.92−1.64)/2 = 5.14; 6.78/5.14 = 1.319066 | d ≤ 6.785; h ≥ (11.915−1.645)/2 = 5.135; ratio ≤ 1.321324 | Rounded P = .001 allows [0.0005,0.0015]; even P = .0015 requires z_(.99925)/z_(.975) = 3.174684/1.959964 = 1.619766 | 1.321324 < 1.619766 |
| Needle EMG | h = (1.11−0.23)/2 = 0.44; 0.67/0.44 = 1.522727 | d ≤ 0.675; h ≥ (1.105−0.235)/2 = 0.435; ratio ≤ 1.551724 | P < .001 requires a ratio above z_(.9995)/z_(.975) = 3.290527/1.959964 = 1.678871 | 1.551724 < 1.678871 |

Finite positive t degrees of freedom cannot reconcile a smaller observed ratio. Closed rounding boundaries further favor reconciliation and still leave both comparisons separated. These are necessary ratio bounds, not replacement P values, confidence limits or reconstructed row outputs. Neither the total-group N = 27 nor the separate 31-treatment-set count is used to assign degrees of freedom.

**Affected result or extracted value:** The SF-36 mental and needle-EMG P values and precision quantities attached to the reported secondary treatment effects. Both occurrences remain one same-test compatibility issue.

**Why context does not resolve it:** The methods and footnote collectively attach the effects, intervals and significance levels to dependent t tests without identifying distinct analyses for the columns. Exploratory/unadjusted labeling does not identify which precise test or interval output should be extracted. Possible interpretations can preserve significance at .05, but the intended exact statistics are not uniquely determined.

**Alternative source-grounded interpretations:** P values and intervals could originate from distinct analyses or output summaries, but no such mapping is supplied. Row-specific paired contributors, degrees of freedom, SEs, test statistics, repeated-set aggregation and any separate interval construction are missing. No preferred analysis or replacement statistic is proposed.

**Mechanical evidence recheck:** Both affected rows and all method/sidedness locations were directly matched to the source PDF. Full rounding-compatible ratio bounds reproduced without an assumed sample size, covariance or degrees of freedom. The source-stated method and tuple inputs suffice for the necessary compatibility check; missing row outputs prevent exact reconstruction. No source-value/location revision was required. Printed quantities are direct observations; separate-analysis explanations remain possibilities. See the [C003 recheck](review_1_6_1/verification/evidence_recheck.md#c003).

**Potential downstream evidence impact:** If confirmed, an extractor could copy a P value or derive precision from an interval that the same stated test cannot jointly generate. The review does not establish a change in significance at .05, a primary-result conclusion change or an actual effect on evidence synthesis.

**Human verification steps:** Inspect both tuples and method statements, then obtain each row's paired-test output, contributing pairs, degrees of freedom and repeated-set aggregation details. Remaining question: Which outputs produced each effect, 95% CI and P value, and were the interval and test columns generated by the same stated analysis?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — CLCN1 primary Bayesian plot and narrative differ

**Status: Pending Human Adjudication**

**Candidate statement:** The primary CLCN1 Bayesian group point and upper credible limit in Figure 2 differ from the corresponding narrative result beyond conservative graphical and numerical precision.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article CLCN1 narrative result vs REPORT main article Figure 2 group display

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Classification rationale:** Both conflicting summaries are within the same REPORT article and concern a primary effect estimate and credible limit, so the domain is statistical_results. Figure 3A corroborates the narrative magnitude and analysis context without adding another relationship. F-ST1-003 remains screened duplicate provenance for this same issue.

**Classification ambiguity:** No exact exported plot coordinates or distinct model identifier is supplied.

**Exact source locations:**

- [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 4, Primary Outcome Measure genotype result](<../jama_stunnenberg_2018_oi_180136.pdf#page=4>): numerical CLCN1 comparator and explicit figure references.
- [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 5, Figure 2 Groups bracket, legend and caption](<../jama_stunnenberg_2018_oi_180136.pdf#page=5>): affected dark-blue CLCN1 group point and upper interval endpoint.
- Corroboration: [jama_stunnenberg_2018_oi_180136.pdf — PDF p. 6, Figure 3A and caption](<../jama_stunnenberg_2018_oi_180136.pdf#page=6>): CLCN1 posterior graphical context.

**Source evidence:** Narrative gives CLCN1 n = 16, mean stiffness reduction 3.84 (95% CrI 2.52–5.16), referring to Figures 2 and 3A. Figure 2 identifies dark-blue CLCN1 n = 16 in the Groups bracket and labels mean reduction in IVR stiffness score with 95% CrI; its caption describes genotype estimates using information from all patients in light of genotype. The relevant group marker is distinct from dark-blue patient 29 in the Patients bracket. Conservative graphical bounds are 3.45–3.65 for the group point and 4.65–4.90 for its upper endpoint. Figure 3A has matching group and information-borrowing descriptions, with a dark-blue density peak near 3.8; the peak is not treated as an exact numerical mean.

**Reported-versus-comparator:** Narrative mean 3.84 and upper credible limit 5.16 are compared with the matched Figure 2 group's approximate point and upper-end bounds. No discrepancy is asserted for the lower endpoint, other groups or individual patients. Figure 3A is corroboration only.

**Reasoning procedure:** Match genotype, n, primary outcome, direction, mean/95% CrI labels and hierarchical information context before comparing quantities. Read the source-rendered Groups marker against integer axis ticks with bounds wider than marker thickness and visual reading uncertainty. Allow narrative half-last-unit rounding intervals and test their overlap with the conservative graphical bounds. Do not invent exact plot coordinates or a replacement summary.

**Calculation:** The narrative mean rounding interval [3.835,3.845] does not intersect the graphical point bounds [3.45,3.65]; the closest gap is 3.835−3.65 = 0.185 score points. The upper-limit interval [5.155,5.165] does not intersect [4.65,4.90]; its closest gap is 5.155−4.90 = 0.255. The point is slightly above the halfway position at 3.5, and the upper cap is below 5.0 near 4.8. These graphical intervals are deliberately broad approximate readings, not reconstructed exported values.

**Affected result or extracted value:** The primary CLCN1 mean stiffness reduction and upper 95% credible limit when extraction uses Figure 2 rather than the narrative.

**Why context does not resolve it:** The narrative explicitly refers to Figure 2, and the matching captions/labels identify no different population, prior, model or analysis stage that explains the separated group summaries. Matching n = 16 and all-patient hierarchical descriptions support comparison but do not identify which output should be extracted.

**Alternative source-grounded interpretations:** Figure and narrative could reflect different model runs or output versions. The supplied labels do not establish that distinction. Figure 3A is compatible with the narrative magnitude at readable graphical precision but cannot establish an exact mean or credible limit. Exported plotting coordinates, posterior-summary files and Figure 2-specific run/population/prior mapping are absent.

**Mechanical evidence recheck:** All three locations were found and matched; direct source rendering confirmed group identity separately from patient 29, readable axes and conservative bounds. Both numerical/graphical nonoverlaps reproduced without source-value or location revision. Necessary inputs for bounded comparison are present; exact exported coordinates and run identity remain unavailable. Numerical narrative values are direct observations, graphical values are visually bounded, and a different output version is a possible explanation. See the [C004 recheck](review_1_6_1/verification/evidence_recheck.md#c004).

**Potential downstream evidence impact:** If confirmed, graph-based and text-based extraction could yield different primary CLCN1 means and upper credible limits. The beneficial direction remains visible; no actual propagation, synthesis change or paper-level conclusion change is established.

**Human verification steps:** Inspect the exact dark-blue CLCN1 Groups marker and narrative references, then compare exported plotting coordinates and posterior summaries with their model/run identifiers. Remaining question: Which exact CLCN1 group estimate and 95% credible interval should Figure 2 display, and which output produced that marker relative to the narrative 3.84 (2.52–5.16)?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Quantitative extraction may reuse a score scale, prior specification, interval or P value, or a figure-derived subgroup summary. Human adjudication can identify the appropriate source quantity and document any clarification before those quantities enter a systematic review, meta-analysis or guideline evidence table. The candidate cards identify plausible extraction points only. This package review does not establish that any candidate propagated, changed a conclusion or caused harm.

## Limitations and Missing Definitions

All four sources and 83 pages were mapped. The remaining limits concern explanation or exact reconstruction, rather than omitted locations. The package supplies one protocol version, a main article, a results supplement and a data-sharing statement. It supplies no individual participant data, executed model objects, exported numerical plot coordinates, separate SAP, protocol amendments or DSMB charter; this does not establish their absence elsewhere.

Candidate-specific missing inputs are the INQoL scoring transformation; actual variance-prior execution and amendment mapping; row-specific paired contributors, degrees of freedom and output; and CLCN1 plot coordinates/model identifiers. Additional reconstruction limits include rank-test ranks/ties, mixed-model covariance/SE details, marginal arm-change interval construction, posterior distribution shapes, usable observations and consent status for dropouts, adherence denominators, adverse-category exhaustiveness, and simulation seeds/draws/indexing. None is supplied by assumption.

Unlabeled graphical quantities remain approximate. Model-based estimates are distinguished from crude arithmetic, Bayesian credible intervals from frequentist confidence intervals, and individual interim from hierarchical aggregate analyses. CPU OCR and Office conversion are unavailable, but affect no source unit: all supplied sources are PDFs with usable text/images and available direct rendering. No fallback environment or global installation was needed. Legacy extraction/image generator versions are unknown; current source/text identity and exact PDF authority are retained. See [limitations](review_1_6_1/limitations.md).

## Human Adjudication Checklist

1. Inspect every affected and corroborating source location in each card.
2. Confirm the matched outcome, population, contrast, time point, analysis and quantity definition.
3. Reproduce the stated rule with the full display-precision or graphical allowances.
4. Obtain the named missing scoring definitions, executed outputs or model/run documentation when needed to select an intended quantity.
5. Record validity, importance, action, initials and notes in the blank fields. Keep candidate identity and provenance when recording the human decision.

Every candidate remains Pending Human Adjudication. No human field has been prefilled with a decision.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The review used supplied local evidence, CPU tools and fresh specialist stages with durable artifact handoffs. Routing preflight records PASS, coordinator `gpt-6.1-sol`/`high`, ordinary specialists `gpt-6.1-sol`/`medium`, statistical/screening/recheck/audit specialists `gpt-6.1-sol`/`high`, ten verified named presets, Coordinator inference: PASS, INTERACTIVE_CLI execution and Provider: CURRENT_SESSION. See [routing preflight](review_1_6_1/routing_preflight.md).

Available direct engines include Poppler pdfinfo, pdftotext, pdftoppm and pdftocairo 25.03.0, GNU sha256sum, and Pandoc 3.1.11.1. Native/layout rereads were streamed; current-run renders record exact physical pages and direct Poppler commands. Tesseract and LibreOffice were unavailable. Fallback environment: NOT_NEEDED; capabilities used: None; removal state: NOT_CREATED. See [tooling record](review_1_6_1/tooling_record.md).

The completed numeric/asset audit independently matched all four source hashes and all 95 reused-asset hashes against the before manifests. Sources and reused evidence remain unchanged in that audit. Final coordinator recomputation, timing finalization, standalone HTML rendering and mechanical validation follow Markdown assembly; this report does not preclaim a final validator result. The [ledger](review_1_6_1/candidate_ledger.md), [recheck](review_1_6_1/verification/evidence_recheck.md), [quality audit](review_1_6_1/quality/evidence_quality_audit.md) and report contain the identical stable set C001, C002, C003 and C004. All cards repeat the ledger classification fields and retain the exact human placeholders.

### Agent execution

Every actual runtime is recorded once below, using the manifest's canonical IDs without a leading slash. Every specialist start mode is FRESH_SPAWN; the coordinator uses CURRENT_SESSION. Audit shards supplement the mandatory audit stage.

| Stage | Agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN |
| cross_source_consistency_reviewer | root/cross_source_checker | gpt-6.1-sol | medium | FRESH_SPAWN |
| statistics_pass_1 | root/statistics_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN |
| inclusion_screener | root/inclusion_screener | gpt-6.1-sol | high | FRESH_SPAWN |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_2 | root/statistics_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN |
| quality_control_numeric_coverage_shard | root/numeric_coverage_auditor | gpt-6.1-sol | high | FRESH_SPAWN |
| quality_control_statistical_coverage_shard | root/statistical_coverage_auditor | gpt-6.1-sol | high | FRESH_SPAWN |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN |

Primary durable artifact assignments are in the [execution manifest](review_1_6_1/agent_execution_manifest.md), with all additional artifacts listed individually in the coverage manifest. The conditional pass-2 screener was not needed because pass 2 emitted no finding.

### Reproducibility performance

The exact timing fields below are copied from run_state.md. The coordinator finalizes the pending values immediately after this complete Markdown assembly. The planning range does not limit coverage or candidate count; local rendering and mechanical validation are outside observed review duration unless a later model repair requires updated timing.

- **Target basis:** Four supplied PDFs contain 83 pages, all backed by reusable native text and rendered pages; no page requires fresh preprocessing. No Office conversion or workbook reconstruction is needed. Visual tables and figures require source-grounded mapping, and protocol/report comparisons, concurrent mapper and checker waves, independent screening, two statistical passes, recheck, audit, and report assembly remain mandatory. These bounded requirements support a 25-40 minute planning range.
- **Total source units:** 83
- **Fresh-source units:** 0
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T02:52:51Z
- **Finished UTC:** 2026-10-11T03:35:34Z
- **Observed elapsed minutes:** 42.72
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Complete 103-family high-effort statistical passes and mechanical recheck; context-bounded three-part audit and repair bookkeeping; complete four-card report assembly; mechanical validator heading and ID-register repairs
