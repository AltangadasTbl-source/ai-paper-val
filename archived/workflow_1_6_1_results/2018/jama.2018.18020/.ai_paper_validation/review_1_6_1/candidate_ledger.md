# Workflow 1.6.1 Stable Candidate Ledger

Pending Human Adjudication. Four stable IDs were assigned only after the independent inclusion screen. IDs follow the earliest retained REPORT location and section order: main p3 Outcomes, Bayesian Analysis, Frequentist Analysis, then p4 Primary Outcome. Corroborating locations are retained without creating additional conflicting relationships. No stable ID is deleted or adjudicated by this review.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main article scale definitions vs REPORT main article INQoL summaries | reproduced | CONFIRMED | F-NUM-001 |
| C002 | protocol_report | P_R | P_R | PLAN protocol variance priors vs REPORT results supplement Bayesian model code | reproduced | CONFIRMED | F-XS-002 |
| C003 | statistical_results | S_W | S_W | REPORT main article dependent-t methods vs REPORT main article SF-36 mental and needle-EMG statistics | reproduced | CONFIRMED | F-ST1-001 |
| C004 | statistical_results | S_W | S_W | REPORT main article CLCN1 narrative result vs REPORT main article Figure 2 group display | reproduced | CONFIRMED | F-XS-001 |

## C001 — INQoL score scale and reported summaries do not reconcile

**Candidate statement:** The repeatedly stated 0–100 INQoL composite range does not reconcile with subgroup upper quartiles above 100 or the overall baseline mean/SD, leaving the reported score unit unclear.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article scale definitions vs REPORT main article INQoL summaries
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-001
**Checker provenance:** Numeric consistency reviewer; N016, S022, S063. Independently included by the initial screener.
**Classification rationale:** Definitions and conflicting summaries occur within the same REPORT document; score-scale/quantitative logic belongs to statistical_results.
**Classification ambiguity:** None in document roles or relationship; the intended score transformation is unknown.
**Exact source locations:** [main p3 Outcomes](../../jama_stunnenberg_2018_oi_180136.pdf#page=3); [main p5 Table 1 INQoL row and footnote f](../../jama_stunnenberg_2018_oi_180136.pdf#page=5); [main p7 Table 2 INQoL row](../../jama_stunnenberg_2018_oi_180136.pdf#page=7); [main p8 footnote g](../../jama_stunnenberg_2018_oi_180136.pdf#page=8).
**Source evidence:** Range 0–100; CLCN1 median84.0 (IQR74.5–110.3), SCN4A median98.0 (56.0–120.0); overall baseline96.89 (SD38.49); treatment effect−14.22 (95%CI−24.71 to−3.74).
**Reasoning procedure:** Quartiles of bounded observations remain within their bounds. For bounded observations, sample variance cannot exceed n/(n−1)m(100−m).
**Calculation:** Upper-quartile rounding intervals [110.25,110.35) and [119.95,120.05) remain above100. At n27 and precision-compatible mean96.89, maximum SD≈17.704; even n≥2 allows no more than≈24.569, below reported SD interval[38.485,38.495).
**Affected result or extracted value:** INQoL baseline96.89(SD38.49) and treatment effect−14.22 with its CI require an identifiable score scale for extraction.
**Why context does not resolve it:** Repeated definitions specify0–100; no alternate raw-score range or normalization formula identifies which score unit the tables use.
**Alternative source-grounded interpretations:** A wider raw composite could be reported under a normalized-score description, or the displayed summaries/scale definition could require clarification. No replacement scale or value is assigned.
**Human question:** Which score definition and transformation produced the Tables1/2 INQoL quantities, and on which explicitly defined scale should they be extracted?
**Status:** Pending Human Adjudication

## C002 — Planned and reported Bayesian variance-prior families differ

**Candidate statement:** The prospective inverse-gamma variation-prior specification differs from uniform standard-deviation priors in the reported individual, population and genotype model code.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol variance priors vs REPORT results supplement Bayesian model code
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-002
**Checker provenance:** Cross-source reviewer F-XS-002; statistical F-ST1-002 is screened DUPLICATE_OF_INCLUDED for its reproduced variance-family component. S001, S105, S109, S110, S111. The unreported clinical-prior counterpart is not an independent candidate basis.
**Classification rationale:** The conflicting prospective specification is PLAN; the reported analysis model code in the results supplement is REPORT. P_R determines protocol_report. Main article pointers and posterior results corroborate relevance without creating another relationship.
**Classification ambiguity:** A supplied analysis amendment or executed-model file could clarify the change; neither is supplied. No numerical prior influence is inferred.
**Exact source locations:** [protocol p40 section9.1](../../joi180136supp1_prod.pdf#page=40); [protocol p41 variation priors](../../joi180136supp1_prod.pdf#page=41); [protocol p42 interim distinction](../../joi180136supp1_prod.pdf#page=42); [results supplement p10 eMethods1](../../joi180136supp2_prod.pdf#page=10); [p11 eMethods2](../../joi180136supp2_prod.pdf#page=11); [p12 definitions](../../joi180136supp2_prod.pdf#page=12); [p13 eMethods3](../../joi180136supp2_prod.pdf#page=13); [p14 definitions](../../joi180136supp2_prod.pdf#page=14). Corroboration: [main p3 Bayesian Analysis](../../jama_stunnenberg_2018_oi_180136.pdf#page=3); [main p4 posterior results](../../jama_stunnenberg_2018_oi_180136.pdf#page=4).
**Source evidence:** Protocol inverse-gamma shape=scale=.001 for variation parameters; report sigma parameters~dunif(.01,10), tau=1/sigma². Pattern occurs for individual arm SDs and population/genotype within-person and arm between-person SDs.
**Reasoning procedure and calculation:** Uniform SD over(.01,10) implies variance support(.0001,100) and density proportional to v^(−1/2), different from inverse-gamma variance priors with positive unbounded support. Naming both noninformative does not make their distributions identical.
**Affected result or extracted value:** Analysis specification attached to individual primary stopping probabilities and overall3.06(95%CrI1.96–4.15), CLCN1 3.84(2.52–5.16), SCN4A1.94(.35–3.53) posterior effects and meaningful-effect probabilities.
**Why context does not resolve it:** No supplied amendment or local explanation maps the explicit variance-family change; the permitted noninformative clinical-mean robustness branch does not establish identical variance priors.
**Alternative source-grounded interpretations:** A later analysis amendment or illustrative code could explain the difference; the package does not establish either. No preferred prior or result change is proposed.
**Human question:** Which variation priors were executed for the three primary Bayesian analyses, and what documented specification or amendment links them to the prospective plan?
**Status:** Pending Human Adjudication

## C003 — Paired-t P values and confidence intervals do not reconcile

**Candidate statement:** Two Table2 total-group secondary effects have printed P values that do not reconcile with their95% CIs under the stated common two-sided dependent-t analysis, after display precision is allowed.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article dependent-t methods vs REPORT main article SF-36 mental and needle-EMG statistics
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-001
**Checker provenance:** Statistical pass1; S005, S006, S062, S088. One repeated compatibility pattern retains both affected rows.
**Classification rationale:** Stated methods and conflicting test/interval tuples are within one REPORT; this is statistical_results.
**Classification ambiguity:** Row-specific paired counts, degrees of freedom and executed output are absent; the calculation uses necessary bounds valid without assigning them.
**Exact source locations:** [main p3 Frequentist Analysis](../../jama_stunnenberg_2018_oi_180136.pdf#page=3); [main p4 two-sided-test statement](../../jama_stunnenberg_2018_oi_180136.pdf#page=4); [main p7 Table2 SF-36 mental row](../../jama_stunnenberg_2018_oi_180136.pdf#page=7); [main p8 EMG row and footnote a](../../jama_stunnenberg_2018_oi_180136.pdf#page=8).
**Source evidence:** SF-36 mental6.78 (95%CI1.64–11.92),P=.001; needle EMG.67 (.23–1.11),P<.001. Methods specify dependent t tests and all P values two-sided.
**Reasoning procedure:** For the same two-sided t test/95% CI, |d|/h=t_observed/t(.975,ν), with h half interval width. Necessary small-P quantile ratios are no smaller than their normal-limit values for positive t degrees of freedom.
**Calculation:** Precision-compatible maximum ratios6.785/5.135≈1.3213 and.675/.435≈1.5517 are below necessary thresholds≈1.6198 for roundedP=.001 (P<.0015) and≈1.6788 forP<.001. Normal-limit P readouts are diagnostics only; no replacement P is assigned.
**Affected result or extracted value:** The SF-36 mental and needle-EMG P values/precision quantities attached to the reported secondary treatment effects.
**Why context does not resolve it:** Methods/footnote attach the effects, CIs and P values to dependent t tests and identify no separate analyses. Both remain significant at.05 under possible interpretations, but intended exact statistics cannot be selected uniquely.
**Alternative source-grounded interpretations:** The P values or CIs may come from distinct analyses or outputs; supplied text does not map those alternatives. No preferred analysis is proposed.
**Human question:** Which paired-test outputs produced the effect,95%CI and P for each affected row, and were the interval and test columns generated by the same stated analysis?
**Status:** Pending Human Adjudication

## C004 — CLCN1 primary Bayesian plot and narrative differ

**Candidate statement:** The primary CLCN1 Bayesian group point and upper credible limit in Figure2 differ from the corresponding narrative result beyond conservative graphical and numerical precision.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article CLCN1 narrative result vs REPORT main article Figure 2 group display
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-001
**Checker provenance:** Cross-source F-XS-001; statistical F-ST1-003 screened DUPLICATE_OF_INCLUDED. S007/S052. Every location is retained in this one issue.
**Classification rationale:** Both conflicting outputs are within the same REPORT; numerical effect/CrI logic belongs to statistical_results. Figure3 is corroboration only.
**Classification ambiguity:** No exact exported plot coordinates or distinct model identifier is supplied.
**Exact source locations:** [main p4 primary genotype result](../../jama_stunnenberg_2018_oi_180136.pdf#page=4); [main p5 Figure2 group legend, dark-blue CLCN1 marker/interval and caption](../../jama_stunnenberg_2018_oi_180136.pdf#page=5); corroborating [main p6 Figure3A/caption](../../jama_stunnenberg_2018_oi_180136.pdf#page=6).
**Source evidence:** Narrative CLCN1 n16 effect3.84 (95%CrI2.52–5.16). Figure2 matches n16, primary stiffness reduction, mean/95%CrI and all-patient hierarchical description; conservative graphical point bounds3.45–3.65, upper-end bounds4.65–4.90. These bounds are approximate, not reconstructed exact values.
**Reasoning procedure and calculation:** Narrative half-unit intervals[3.835,3.845] and[5.155,5.165] do not overlap conservative plotted bounds. No discrepancy is asserted for the lower endpoint or other groups.
**Affected result or extracted value:** Primary CLCN1 mean stiffness reduction and its upper95%credible limit when graph versus text is used for extraction.
**Why context does not resolve it:** Narrative explicitly refers to Figure2; caption identifies no distinct population/model/analysis stage to explain the different group output.
**Alternative source-grounded interpretations:** A different output/model version might underlie the figure or narrative; supplied labels do not identify it. Figure3 corroborates the narrative magnitude.
**Human question:** Which exact exported CLCN1 group estimate/interval should Figure2 display, and which model output produced its group marker relative to the narrative?
**Status:** Pending Human Adjudication
