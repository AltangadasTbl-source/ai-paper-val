# Cross-Source Consistency Review

## Scope and method

This review checked the complete main and support quantitative evidence maps: all 41 main-map records (`N001`-`N028`, `S001`-`S013`) and all 20 support-map records (`N-SUP-001`-`N-SUP-013`, `S-SUP-001`-`S-SUP-007`). The direct-source scope was the abstract, main narrative, Tables 1-3, Figures 1-3 and captions/footnotes in PDF-001; the protocol (PDF-002); SAP (PDF-003); and results supplement/eTables (PDF-004). The legacy DOCX was deliberately excluded, as required. No supplied structured data, workbook, or CSV exists.

Each proposed comparison was matched first on population, observation period, treatment contrast/reference direction, analysis set, model/analysis framework, measure and scale, unit, and printed precision. A planned quantity was not compared as though it were an observed result. Direct PDFs were the evidence authority; mapped native/layout text and direct render records were used only to locate and transcribe the printed material.

## Matched-result coverage

Nineteen cross-source result or definition families were reviewed. The following records document the comparison logic and outcome; “no candidate” means that the printed differences were explained by a stated analysis framework, a planned-versus-observed distinction, an explicitly different population, or displayed precision.

1. **Trial setting, allocation, and analyzed population — no candidate.** The abstract and main narrative report 338 randomized infants (172 early, 166 late), with primary-outcome data for 159 early and 149 late infants. The flow diagram supplies the withdrawals and losses that distinguish randomized from analyzed populations. eTable 3 uses the randomized 172/166 denominators, whereas Table 2 and eTable 2 use 159/149; these are explicitly different analysis sets.
2. **Treatment definition and timing — no candidate.** Main-paper early repair is planned before discharge and late repair after discharge when older than 55 weeks’ postmenstrual age. The protocol’s approximate 55-60-week wording and the SAP’s “>55 weeks” wording are planned-treatment descriptions, not conflicting observed timing results.
3. **Primary endpoint time window — no candidate apart from Candidate 1’s threshold label.** Main results use any/at least one SAE during the 10-month observation period. Protocol and SAP descriptions identify enrollment/randomization through 10 months. The alternative enrollment versus randomization wording is not enough to show a different measured interval in the supplied sources; the threshold symbol/wording is addressed separately below.
4. **Primary-outcome counts and percentages — no candidate apart from Candidate 1’s endpoint label.** The abstract, Key Points, narrative, Table 2, Figure 3 overall row, and eTable 2 print the same 44/159 (28%) early and 27/149 (18%) late values for the matched analyzed population. Table 3 is an event-type table and expressly permits more than one event per infant; its event counts are therefore not a comparator for the number of infants with any SAE.
5. **Bayesian primary-effect result — no candidate.** The abstract, narrative, Table 2, and Figure 2 consistently give late relative to early: risk difference -7.9% (95% CrI -16.9% to 0), RR 0.68 (0.45-1.01), and 97% posterior probability of benefit. Figure 3 rounds the same overall risk difference as -0.08 (-0.17 to 0.002); the extra precision and percent-versus-proportion display account for the apparent endpoint difference.
6. **Frequentist primary-effect result — no candidate.** eTable 2 gives RD -9.0% (95% CI -16.5% to -2.0%), RR 0.65 (0.46-0.92), P=.01. These are identified as frequentist estimates, whereas the main paper’s principal estimates are Bayesian medians/CrIs; they are not same-model duplicates.
7. **Hospital-days descriptive result — no candidate.** The abstract, narrative, Table 2, and eTable 2 agree on early 19.0 (IQR 9.8-35/35.0) versus late 16.0 (7/7.0-38/38.0) days during the study period. Comma versus “to” separators and trailing zeroes are display precision only.
8. **Hospital-days model result — no candidate.** Table 2’s Bayesian RR 0.91 (95% CrI 0.74-1.11), 82% posterior benefit, and eTable 2’s frequentist RR 0.91 (95% CI 0.74-1.12), P=.36 are explicitly different frameworks and interval types. Neither source prints a risk difference for this count outcome.
9. **Planned sample size and observed stopping — no candidate.** Protocol/SAP/main planning values are 293 per group, 586 with primary-outcome data, and 615 planned enrollment; the actual 338 randomized is reported after the 97% interim probability crossed the 95% efficacy threshold. These are planned versus observed quantities, not competing totals.
10. **Interim-rule and interim-result wording — no candidate.** Protocol specifies efficacy stopping at a probability of decreased SAE greater than 95%; SAP and main paper report 97%, crossing that rule. The actual interim timing/population (February 2021; 309 data-available infants in the main paper) is not presented in the protocol’s prospective approximately-200-infant plan as an observed result.
11. **Analysis framework/model labels — no candidate.** The protocol’s prospective GLMM/lognormal plan, SAP’s final binary-logistic/negative-binomial definitions, and reported Bayesian plus frequentist analyses describe source-specific planned or realized analyses. The main paper/eTable footnotes explicitly identify the frequentist primary-outcome GEE substitution after mixed-model nonconvergence. No source presents those differently specified models as a single identical estimate.
12. **Subgroup primary results — no candidate.** Abstract 99% benefit statements for gestational age <28 weeks and bronchopulmonary dysplasia match the detailed narrative and Figure 3. Subgroup numerators/denominators, RRs, CrIs, and probabilities are not compared with overall Table 2 values because the populations differ.
13. **Baseline, flow, and centre counts — no candidate.** Table 1’s randomized-denominator footnotes for race/ethnicity, its 163/157 baseline columns, Figure 1’s flow counts, and eTable 3’s all-randomized centre totals are compatible after the printed denominators/missingness are respected.
14. **Event type, event count, and infant count — no candidate.** Table 3’s count/percentage rows are event-specific frequencies in the 159/149 analysis population. The main narrative’s “at least one serious adverse event” is an infant-level composite. The table’s multiple-event footnote prevents rate-versus-count conflation.
15. **Protocol/SAP SAE ascertainment and harm definitions — no candidate apart from Candidate 1’s threshold label.** The sources align on the SAE domains and 10-month ascertainment construct. Differences between detailed prospective definition language and the published adjudicated-event table do not create a numeric or measure contradiction.
16. **Protocol/SAP hospital-day hypothesis — Candidate 2.** The sources present two incompatible values for the same planned median hospital-day comparison. The SAP explicitly calls the earlier protocol values incorrect; this is a concrete cross-document textual/numeric correction.
17. **BSID-III and other secondary planned outcomes — no candidate.** The protocol/SAP describe planned 22-26-month neurodevelopmental assessment and its scale; the main paper does not display a final BSID treatment effect. No missing observed comparison is inferred.
18. **Protocol/SAP subgroup and prior specifications — no candidate.** Changes in planned interaction-prior wording and addition of exploratory surgical-approach/distance analyses are source-specific plan definitions. No identical displayed result is given under both specifications.
19. **Display precision and display-zero rule — no candidate.** No candidate was generated from P-value formatting. The only printed frequentist P values used in a matched result are .01 and .36. The main Bayesian displays use probabilities and CrIs, not a conflicting P-value.

## Pre-ID candidates for human adjudication

### Candidate 1 — SAE endpoint threshold is printed as “more than 1” in protocol/SAP/eTable material but as “at least 1” in the main result

- **Category:** Measure, label, or scale inconsistency.
- **Exact linked locations:**
  - [PDF-001, abstract — PDF p. 1](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1): 44/159 versus 27/149 “had at least 1 serious adverse event.”
  - [PDF-001, Table 2 — PDF p. 6](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6): “Had ≥1 serious adverse event,” 44 (28) versus 27 (18).
  - [PDF-002, abstract — PDF p. 2](../../../joi240020supp1_prod_1710443209.74911.pdf#page=2): protocol primary hypothesis/outcome says the proportion with “>1 SAE.”
  - [PDF-002, Specific Aims — PDF p. 3](../../../joi240020supp1_prod_1710443209.74911.pdf#page=3): “The primary outcome measure is the proportion of infants with >1 SAE.”
  - [PDF-003, Objectives/Hypothesis — PDF pp. 2-3](../../../joi240020supp2_prod_1710443209.75411.pdf#page=2): the SAP repeats “>1 serious adverse event” in the objective and hypothesis; [PDF p. 3](../../../joi240020supp2_prod_1710443209.75411.pdf#page=3) begins the same section.
  - [PDF-003, final analysis framework — PDF p. 4](../../../joi240020supp2_prod_1710443209.75411.pdf#page=4): frequentist/Bayesian analysis is described for the “proportion of children with ≥ 1 SAE.”
  - [PDF-003, primary outcome — PDF p. 7](../../../joi240020supp2_prod_1710443209.75411.pdf#page=7): “whether an infant experienced any SAEs.”
  - [PDF-004, eTable 2 — PDF p. 5](../../../joi240020supp3_prod_1710443209.75411.pdf#page=5): row label “Infant had > 1 SAE,” with the same 44 (28%) versus 27 (18%) values.
- **Printed values/statements compared:** Strictly read, “>1 SAE” means at least two SAEs; “≥1,” “at least 1,” and “any” mean one or more SAEs. The eTable’s “>1” row nevertheless carries the same 44/159 and 27/149 counts as the main paper’s one-or-more endpoint.
- **Matched attributes and comparison logic:** The population (preterm randomized-trial infants with complete primary-outcome data), early-versus-late contrast, 10-month endpoint, counts/denominators, and eTable/main frequentist-versus-Bayesian framework are all matched before comparing the endpoint label. The logical rule is set inclusion: the number of infants with two or more events cannot be assumed equal to the number with one or more events; the printed threshold must identify which estimand the shared counts represent.
- **Supported source-grounded alternatives:** The repeated identical 44/159 and 27/149 counts, the main Table 2 “≥1” label, and SAP “any SAEs” wording support that one or more SAE may be the intended endpoint and that the `>` sign is a threshold-label error. Alternatively, if `>1` was intended literally in a protocol/SAP/eTable location, the main-paper endpoint label and/or the shared counts require clarification. The supplied sources do not identify which production location should be corrected.
- **Human verification steps:** Inspect the signed/final protocol and SAP versions or the study’s endpoint/adjudication definition in the supplied trial records; determine whether the endpoint is one-or-more or two-or-more SAEs; then confirm that the 44 and 27 infants were tabulated under that definition before choosing any correction.
- **Pending Human Adjudication:** Yes. This is a pre-ID reporting-consistency candidate only; no validity, severity, or corrective action is assigned here.

### Candidate 2 — The protocol prints two different planned median hospital-day values, and the SAP explicitly identifies one as incorrect

- **Category:** Cross-document numeric inconsistency.
- **Exact linked locations:**
  - [PDF-002, Specific Aims — PDF p. 3](../../../joi240020supp1_prod_1710443209.74911.pdf#page=3): for the planned 3-day reduction in median total hospital days, “18 hospital days for early IH repair versus 15 for late IH repair.”
  - [PDF-002, Statistical Analysis Plan/sample size — PDF p. 12](../../../joi240020supp1_prod_1710443209.74911.pdf#page=12): for the same planned 3-day median difference, “median=8, mean=18” for early and “median=5, mean=13” for late.
  - [PDF-003, Secondary Hypotheses — PDF p. 3](../../../joi240020supp2_prod_1710443209.75411.pdf#page=3): “8 total hospital days for early IH repair versus 5 for late repair,” followed by: “the expected median total number of hospital days was listed as 18 for early IH repair and 15 for the late repair group (page 3), which is incorrect. The correct values were presented on page 12 of the final protocol.”
- **Printed values/statements compared:** The protocol p. 3 planned medians are 18 early and 15 late; protocol p. 12 planned medians are 8 early and 5 late (with means 18 and 13). Both pairs retain a 3-day between-group median difference, but they are not the same absolute planned medians.
- **Matched attributes and comparison logic:** These are both prospective hospital-day design assumptions, for early versus late repair during the study observation period, stated as median total hospital days. They are not compared to the observed main-paper medians of 19.0 and 16.0, which concern trial results. The comparison rule is direct identity of the same planned measure, time window, contrast, and scale: 18 is not 8 and 15 is not 5.
- **Supported source-grounded alternatives:** The SAP expressly supports treating the p. 12 values (median 8/5, mean 18/13) as the intended design inputs and identifies p. 3’s 18/15 median wording as incorrect. A human reviewer should nevertheless confirm whether the final protocol was amended/versioned such that the earlier page was retained historically rather than requiring an erratum or correction notice.
- **Human verification steps:** Compare the protocol version/date and amendment history for pp. 3 and 12; verify whether p. 3’s “18/15” was intended to be means or medians; confirm the SAP’s stated correction against the final approved protocol before deciding how the source record should be described or corrected.
- **Pending Human Adjudication:** Yes. This is a pre-ID reporting-consistency candidate only; no validity, severity, or corrective action is assigned here.

## Limitations

- This is a cross-source consistency review, not an arithmetic, broad methodological, clinical, or raw-data audit. The separately assigned numeric and statistical reviewers address their own scopes.
- Protocol/SAP statements were treated as planned definitions unless the documents explicitly presented the same quantity as an observed final result. This prevents planned-versus-observed differences from being miscalled as conflicts.
- PDF-004’s reusable native text had corrupted glyphs; the mapped eTable values were based on direct visual PDF confirmation. No DOC/DOCX, workbook, or CSV evidence was available for a further structured-data comparison.

## Counts and handoff

- **Mapped records reviewed:** 61 (41 main-map and 20 support-map records).
- **Distinct matched result/definition families reviewed:** 19.
- **Pre-ID qualifying candidates emitted:** 2.
- **Stable candidate IDs assigned:** none.
- **Artifact:** `.ai_paper_validation/review_1_5_3/checkers/cross_source_consistency.md`.
