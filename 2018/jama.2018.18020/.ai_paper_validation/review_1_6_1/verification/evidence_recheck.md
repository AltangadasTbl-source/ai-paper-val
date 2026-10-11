# Mechanical evidence recheck — Workflow 1.6.1

Runtime agent: `/root/evidence_rechecker`; fresh `qc161_evidence_rechecker`, `gpt-6.1-sol`/`high`. Assigned stable scope: C001, C002, C003, C004. The complete scope and review contract, current ledger, initial independent screen, checker finding details, and tooling record were read. This artifact records mechanical evidence and classification facts; every ID remains Pending Human Adjudication.

All cited locations below refer to physical PDF pages. The supplied PDFs are authority. Direct Poppler `pdftotext` 25.03.0 layout extraction reread main pages 3–8, protocol pages 40–42, and results-supplement pages 10–14. Fresh direct Poppler renders visually confirmed main pages 3, 4, 5, protocol page 41, and results-supplement pages 10, 11, 13. Existing current-run source renders aided visual confirmation of main pages 6, 7, 8; their text was separately read directly from the PDF. No reusable transcription was treated as final authority. No source or reused artifact was modified. No web, GPU, OCR, or Python scientific calculation was used.

## Classification summary

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Classification recheck |
|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main article Outcomes and scale footnotes vs REPORT main article Tables 1 and 2 INQoL summaries | reproduced | Confirmed: bounded-score quantitative logic within one REPORT. |
| C002 | protocol_report | P_R | P_R | PLAN prospective statistical specification vs REPORT results supplement eMethods 1–3 model code | reproduced | Confirmed: a primary-analysis prior specification differs between PLAN and REPORT. |
| C003 | statistical_results | S_W | S_W | REPORT main article dependent-t and sidedness statements vs REPORT main article Table 2 SF-36 mental and needle-EMG tuples | reproduced | Confirmed: estimate/test/interval logic within one REPORT. |
| C004 | statistical_results | S_W | S_W | REPORT main article primary genotype result vs REPORT main article Figure 2 CLCN1 group marker and interval | reproduced | Confirmed: matched primary effect and interval within one REPORT. |

There is no role, relationship, domain, source-value, or source-location revision. Each candidate has one relationship code, so precedence P_R > P_P > S_C > S_W introduces no competing primary type. Corroborating content does not create another relationship. Evidence states do not constitute dispositions.

## C001 — INQoL scale and summaries

**Location found; source and comparator matched:** Yes, at every retained location.

| Exact location | Role by content | Direct-source matched content | Function |
|---|---|---|---|
| [Main page 3, Outcomes secondary-outcome paragraph](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3) | REPORT: defines outcomes assessed in the reported trial. | Individual Neuromuscular Quality of Life questionnaire composite score, 0–100 scale; higher indicates greater disease severity. | Scale comparator. |
| [Main page 5, Table 1 INQoL composite row and genotype headings](../../../jama_stunnenberg_2018_oi_180136.pdf#page=5) | REPORT: reports baseline summaries. | CLCN1 N=16: median 84.0, IQR 74.5–110.3; SCN4A N=11: median 98.0, IQR 56.0–120.0. | Both affected upper quartiles matched separately. |
| [Main page 5, Table 1 footnote f](../../../jama_stunnenberg_2018_oi_180136.pdf#page=5) | REPORT: defines the reported table's scale. | Scale, 0 to 100; higher indicates greater disease severity. | Repeated scale comparator. |
| [Main page 7, Table 2 heading and INQoL row](../../../jama_stunnenberg_2018_oi_180136.pdf#page=7) | REPORT: reports frequentist trial results. | Total NDM N=27; baseline mean 96.89 (SD 38.49); placebo change −7.22 (95% CI −14.5 to −0.29); mexiletine change −21.44 (−30.90 to −11.95); treatment effect −14.22 (−24.71 to −3.74), P=.01. | Affected baseline mean/SD and the score unit attached to changes/effect. |
| [Main page 8, Table 2 footnote g](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8) | REPORT: defines the reported table's scale. | Scale, 0 to 100; higher indicates greater disease severity. | Repeated scale comparator. |

**Consistency rule applicable:** Yes. Quartiles of observations on a bounded 0–100 score cannot exceed 100. Independently, if observations x are in [0,100], x²≤100x, so the sample variance satisfies s²≤n/(n−1)m(100−m). This bounded-score rule does not compare different baseline populations or require identical paired treatment contributors. The treatment effect itself is not asserted to violate a score-range bound.

**Calculation and display-precision interval check reproduced:** Yes. The two upper-quartile intervals are [110.25,110.35] and [119.95,120.05], neither intersecting [0,100]. Closing rounding boundaries is conservative and cannot reconcile them. The mean interval is [96.885,96.895] and SD interval [38.485,38.495]. Over that mean interval, m(100−m) is largest at 96.885. Thus the n=27 upper SD bound is sqrt((27/26)×96.885×3.115)=17.703230. Even without assigning the precise baseline contributor count, n≥2 implies n/(n−1)≤2 and SD≤sqrt(2×96.885×3.115)=24.568141. Both bounds are below 38.485. The ledger's slightly more conservative 17.704 and 24.569 bounds describe the same nonoverlap; this is numerical refinement, not a source transcription revision.

**Necessary inputs available:** Yes for the quartile bound and the conservative SD test: repeated score limits, two upper quartiles, baseline mean/SD, and the total-group heading. Exact individual scores are unnecessary for this bound.

**Exact missing inputs or definitions:** The score calculation, raw-score range, any normalization/transformation, and a mapping from that transformation to both tables are absent from these defining locations. The exact number contributing to the baseline INQoL summary is not separately given; the bound valid for every n≥2 removes dependence on that missing count.

**Source-grounded alternative interpretation:** The tables could use a wider raw composite while the prose describes a normalized scale, or the scale designation and displayed summaries could require clarification. The source repeatedly calls the quantity a composite score but supplies no alternative transformation that chooses among these readings.

**Direct observation versus inferred explanation:** The printed quartiles, mean/SD, and repeated 0–100 descriptions are direct observations. Their incompatibility follows from the stated bounded-score rules. A wider raw score or different transformation is a possible explanation, not an observed implementation. No replacement score or effect is inferred.

**Classification:** Every compared location is REPORT content in the same main article. Primary relationship S_W; all relationships S_W; domain statistical_results. This concerns numerical scale and bounded-summary logic, rather than attribution of a result to a different outcome or analysis set. Classification ambiguity: the intended score transformation is unresolved, but the document roles and relationship are clear.

**Evidence state:** reproduced. Determining fact: both source upper quartiles remain above the repeated maximum after display precision, and the baseline SD remains beyond the bounded-score maximum.

**Exact remaining human question:** Which score definition and transformation produced the INQoL quantities in Tables 1 and 2, and on which explicitly defined scale should baseline 96.89 (SD 38.49) and treatment effect −14.22 (95% CI −24.71 to −3.74) be extracted?

## C002 — Planned and reported variance priors

**Location found; source and comparator matched:** Yes, including every occurrence of the retained variance-prior-family pattern. The candidate basis is the explicit variance-family contrast only.

| Exact location | Role by content | Direct-source matched content | Function |
|---|---|---|---|
| [Protocol page 40, section 9.1 and prior elicitation](../../../joi180136supp1_prod.pdf#page=40) | PLAN: prospective hierarchical-model and prior specifications, written in future tense. | Patient, genotype and centre grouping; common within-person residual variance; almost noninformative priors for parameters other than elicited treatment effects. | Establishes the prospective primary model/prior context. |
| [Protocol page 41, first paragraph](../../../joi180136supp1_prod.pdf#page=41) | PLAN: prospective distribution specifications. | Identifies means and variances; variation parameters will use inverse gamma distributions with shape and scale both 0.001. | Conflicting variance-family comparator. |
| [Protocol page 41, robustness paragraph](../../../joi180136supp1_prod.pdf#page=41) | PLAN: prospective sensitivity provision. | Replace elicited priors with noninformative priors to check robustness. | Context; not a separate candidate basis. |
| [Protocol page 42, interim-analysis paragraph](../../../joi180136supp1_prod.pdf#page=42) | PLAN: prospective stopping-advice analysis. | Interim analyses will use noninformative priors only. | Confirms the interim branch; does not specify a different variation family. |
| [Results supplement page 10, eMethods 1](../../../joi180136supp2_prod.pdf#page=10) | REPORT: code and parameter definitions for the reported individual interim analysis. | sigma_plac~dunif(0.01,10), sigma_mex~dunif(0.01,10); tau_plac=1/sigma_plac², tau_mex=1/sigma_mex²; both sigma variables expressly defined as standard deviations. | Two affected prior statements, both matched. |
| [Results supplement page 11, eMethods 2 code](../../../joi180136supp2_prod.pdf#page=11) | REPORT: code for reported total-group effect estimation. | sigma.within, sigma.mex, sigma.plac each ~dunif(0.01,10), each corresponding tau=1/sigma². | Three affected prior statements, all matched. |
| [Results supplement page 12, eMethods 2 definitions](../../../joi180136supp2_prod.pdf#page=12) | REPORT: continuation of model-variable definitions. | sigma.within is an individual-measurement SD, same in both arms; tau.within=1/sigma.within²; population effect is mu.plac−mu.mex. | Confirms parameter/contrast identity; no independent conflict. |
| [Results supplement page 13, eMethods 3 code](../../../joi180136supp2_prod.pdf#page=13) | REPORT: code for reported genotype subgroup effect estimation. | sigma.within, sigma.mex, sigma.plac each ~dunif(0.01,10), each corresponding tau=1/sigma²; genotype contrasts formed from placebo minus mexiletine means. | Three affected prior statements, all matched. |
| [Results supplement page 14, eMethods 3 definitions](../../../joi180136supp2_prod.pdf#page=14) | REPORT: continuation of model-variable definitions. | Gen_Pat=1 for CLCN1, 0 for SCN4A; arm SDs shared across genotypes; within-person SD common to both arms and genotypes. | Confirms parameter identity; no independent conflict. |
| [Main page 3, Bayesian Analysis](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3) | REPORT: describes analyses performed for this trial. | Individual posterior analysis points to eMethods 1; aggregated total and genotype analyses point to eMethods 2 and 3. | Corroborates result-producing role; adds no conflicting relationship. |
| [Main page 4, Primary Outcome Measure](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4) | REPORT: reports posterior trial results. | Individual clinically meaningful effectiveness in 24/27; overall effect 3.06 (95% CrI 1.96–4.15), CLCN1 3.84 (2.52–5.16), SCN4A 1.94 (0.35–3.53); meaningful-effect probabilities 100%, 100%, 93%. | Corroborates affected primary results; adds no conflict. |

**Consistency rule applicable:** Yes. A distribution specified on variance is compared with the variance distribution induced by the reported explicit SD prior. Merely calling both noninformative does not equate their distributions. The clinical-mean-prior counterpart's absence is not an independent basis for C002.

**Logical comparison and calculation reproduced:** Yes. For sigma uniform on (a,b)=(0.01,10), v=sigma² has density f(v)=1/[2(b−a)sqrt(v)] on (a²,b²)=(0.0001,100). Under the protocol's usual inverse-gamma variance parameterization, f(v) is proportional to v^(−1.001)exp(−0.001/v), supported on all v>0. The bounded support and different density establish different families even without computing a posterior. The source directly names variances and identifies reported sigmas as SDs via definitions and tau=1/sigma².

**Display-precision interval check:** The code literals and prospective prior parameters are mathematical specifications, not rounded measured summaries. Even allowing unusually broad half-last-unit intervals around the finite uniform endpoints or around positive inverse-gamma shape/scale would leave one induced variance prior bounded above and the inverse-gamma variance prior unbounded. Numerical rounding cannot reconcile the distribution-family contrast.

**Necessary inputs available:** Yes for the specification comparison: named family and parameters in PLAN, all eight uniform-SD statements across three REPORT models, and definitions linking sigma to variance/precision. No raw stiffness data, posterior samples, or model execution is necessary to establish this contrast.

**Exact missing inputs or definitions:** Executed model files and run identifiers, a result-to-executed-prior mapping for each primary analysis, and a supplied amendment or explanation linking uniform-SD code to the prospective variation-prior specification are absent. These inputs would be needed to identify execution and any numerical influence. A clinical-prior output is not required for the retained variance-family comparison, and its absence supplies no additional comparison here.

**Source-grounded alternative interpretation:** The published code might be an illustration or a later amended implementation; the robustness provision permits replacement of elicited priors with noninformative priors. The supplied package does not identify an illustrative-code distinction or amendment, and the robustness text does not explicitly replace the named variation-prior family with uniform-SD priors.

**Direct observation versus inferred explanation:** Future-tense inverse-gamma variation priors and all eight uniform-SD code statements are direct observations. The induced variance density/support is a mathematical transformation. Whether the reported posterior results actually used that code, whether there was an amendment, and whether numerical results would change are unresolved explanations or consequences, not direct observations.

**Classification:** Protocol pages 40–42 are PLAN by their prospective analysis and stopping specifications. Results-supplement pages 10–14 are REPORT by their model-code descriptions of the reported analyses. Main pages 3–4 are corroborating REPORT content. Primary relationship P_R; all relationships P_R; domain protocol_report. No S_C relationship is present because the two REPORT documents do not supply conflicting variance priors; the main article links to and supports the supplement. Classification ambiguity: executed-code status or a nonsupplied amendment could explain the contrast, without changing the content roles.

**Evidence state:** reproduced. Determining fact: the directly matched inverse-gamma variance specification and all eight uniform-SD code priors define different variance distributions; no source transcription or location revision was needed.

**Exact remaining human question:** Which variation priors were executed for the individual interim, total-population, and genotype primary Bayesian analyses, and what documented specification or amendment links them to the prospective inverse-gamma variation priors?

## C003 — Paired-test P and confidence intervals

**Location found; source and comparator matched:** Yes for both affected rows and every supporting method location.

| Exact location | Role by content | Direct-source matched content | Function |
|---|---|---|---|
| [Main page 3, Frequentist Analysis final paragraph](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3) | REPORT: states analyses performed. | For other normally distributed secondary outcomes, dependent t tests calculate mean treatment effects, significance levels, and confidence intervals at total NDM group level. | Same-analysis method comparator. |
| [Main page 4, Frequentist Analysis continuation](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4) | REPORT: states test conventions. | All P values 2-sided; significance P<.05; secondary P values unadjusted and exploratory; all available data included. | Sidedness/adjustment matched. |
| [Main page 7, Table 2 heading and SF-36 mental component row](../../../jama_stunnenberg_2018_oi_180136.pdf#page=7) | REPORT: reports treatment-effect statistics. | Total NDM N=27; effect 6.78, 95% CI 1.64–11.92, P=.001. | First affected tuple matched. |
| [Main page 8, Table 2 needle-EMG row](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8) | REPORT: reports treatment-effect statistics. | Effect 0.67, 95% CI 0.23–1.11, P<.001. | Second affected tuple matched. |
| [Main page 8, Table 2 footnote a](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8) | REPORT: identifies table methods. | IVR uses linear mixed model; other secondary mean effects use dependent t tests; genotype n=16 and n=11. | Confirms non-IVR dependent-t attribution. |

**Consistency rule applicable:** Yes under the expressly stated common dependent-t analysis for effects, intervals and significance levels. For a two-sided test of zero and its 95% t confidence interval, h=(U−L)/2=t_(.975,nu)×SE, and |d|/h=|t_observed|/t_(.975,nu). The necessary upper-tail quantile ratio t_(1−P/2,nu)/t_(.975,nu) is at least its normal-limit ratio for positive Student-t degrees of freedom. Consequently the normal-limit thresholds are conservative necessary conditions; finite degrees of freedom cannot rescue a smaller observed ratio. No alternative row-specific test or interval construction is identified locally.

**Calculation and display-precision interval check reproduced:** Yes, separately for both occurrences.

| Affected row | Printed halfwidth and ratio | Conservative rounding-compatible ratio maximum | Necessary ratio for the printed P | Comparison |
|---|---|---|---|---|
| SF-36 mental | h=(11.92−1.64)/2=5.14; 6.78/5.14=1.319066 | d≤6.785; h≥(11.915−1.645)/2=5.135; ratio≤1.321324 | Rounded P=.001 allows [0.0005,0.0015]; even the weakest boundary requires z_(.99925)/z_(.975)=3.174684/1.959964=1.619766. | 1.321324<1.619766; no allowed combination reconciles. |
| Needle EMG | h=(1.11−0.23)/2=0.44; 0.67/0.44=1.522727 | d≤0.675; h≥(1.105−0.235)/2=0.435; ratio≤1.551724 | P<.001 requires ratio greater than the normal boundary z_(.9995)/z_(.975)=3.290527/1.959964=1.678871. | 1.551724<1.678871; no allowed combination reconciles. |

All effect and interval entries received ±0.005. Closed bounds and independent maximization of d and minimization of h deliberately allow more combinations than exact midpoint constraints permit, strengthening the conservative nature of the test. These are ratio bounds, not replacement P values or reconstructed row outputs. The two rows are one repeated same-test compatibility pattern.

**Necessary inputs available:** Yes for the compatibility bound: estimate, both interval endpoints, 95% confidence level, dependent-t method, sidedness, and absence of multiplicity adjustment. The conclusion does not assign degrees of freedom or infer them from the N=27 heading; the separate 31-treatment-set count on page 4 is not used as a paired sample size.

**Exact missing inputs or definitions:** Row-specific paired counts, degrees of freedom, SEs, test statistics, executed SPSS output, handling/aggregation of repeated treatment sets, and any distinct test or CI construction for these two columns are absent. They prevent an exact P reconstruction and selection of a replacement quantity, while not preventing the conservative same-test compatibility check.

**Source-grounded alternative interpretation:** The P and CI columns could have come from distinct analyses or output summaries, but the source collectively attributes these quantities to dependent t tests and supplies no such mapping. Exploratory/unadjusted designation explains the interpretation of secondary tests, not the different numerical precision implied by a CI and P value.

**Direct observation versus inferred explanation:** Both tuples and the method/sidedness statements are direct observations. The ratio nonoverlap follows mathematically from the same-test rule. Distinct output sources or analyses remain possible explanations. No exact replacement P, CI, or SE is inferred, and the observation does not assert a change in significance at .05.

**Classification:** All compared locations are REPORT in the same article. Primary relationship S_W; all relationships S_W; domain statistical_results. The issue concerns statistical test/interval logic inside each result, not a peripheral comparison of secondary values between displays. Classification ambiguity: unreported row output and contributor definitions limit the exact intended statistics, without ambiguity in document roles.

**Evidence state:** reproduced. Determining fact: both directly confirmed effect/interval ratios remain below necessary same-test P thresholds after the full display-precision allowances; no source-value or location revision was needed.

**Exact remaining human question:** Which paired-test outputs, contributing pairs, and degrees of freedom produced the SF-36 mental and needle-EMG effects, 95% confidence intervals, and P values, and were each row's interval and test columns generated by the same stated analysis?

## C004 — CLCN1 primary plot and narrative

**Location found; source and comparator matched:** Yes. The CLCN1 group marker is the dark-blue middle marker inside the right-hand Groups bracket, not the dark-blue patient 29 marker inside the Patients bracket.

| Exact location | Role by content | Direct-source matched content | Function |
|---|---|---|---|
| [Main page 4, Primary Outcome Measure genotype paragraph](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4) | REPORT: numerical primary Bayesian results. | CLCN1 subgroup n=16, mean reduction 3.84, 95% CrI 2.52–5.16; paragraph explicitly refers to Figure 2 and Figure 3A. | Numerical comparator. |
| [Main page 5, Figure 2 group legend, marker, interval and caption](../../../jama_stunnenberg_2018_oi_180136.pdf#page=5) | REPORT: graphical primary Bayesian results. | CLCN1 n=16 is dark blue; y-axis is reduction in IVR stiffness score, mean and 95% CrI; caption says genotype estimates use information from all patients in light of genotype. | Affected point and upper endpoint matched at graphical precision. |
| [Main page 6, Figure 3A and caption](../../../jama_stunnenberg_2018_oi_180136.pdf#page=6) | REPORT: primary posterior graphical results. | Same CLCN1 n=16 and all-patient-information description; dark-blue posterior density peaks near 3.8. | Corroborates narrative magnitude and matched analysis context; no independent conflict. |

**Consistency rule applicable:** Yes. Matched primary genotype population, stiffness-reduction direction, posterior mean/95% credible interval labels, n=16, and hierarchical all-patient description support comparison of the numerical summary with the Figure 2 group summary. The main narrative points to that figure; no caption assigns it a different population, prior, model, or stage. A posterior-density peak in Figure 3A is not treated as a numerical mean or independently reconstructed credible limit.

**Graphical comparison and display-precision interval check reproduced:** Yes. Fresh source rendering at maximum dimension 2200 pixels permits conservative bounds of 3.45–3.65 for the dark-blue CLCN1 group point and 4.65–4.90 for its upper interval endpoint. The point is slightly above the 3.5 halfway position between integer y-axis ticks, and the upper cap is below the 5.0 tick near 4.8. These bounds intentionally exceed marker thickness and visual reading uncertainty; they are approximate graphical intervals, not exact exported coordinates. Narrative rounding intervals [3.835,3.845] for the mean and [5.155,5.165] for the upper limit do not intersect those graphical bounds. Even the closest gaps are 0.185 and 0.255 score points, respectively. No discrepancy is asserted for the lower endpoint, other genotype/total group markers, or individual patients.

**Necessary inputs available:** Yes for this conservative graphical comparison: exact numerical summary; readable axis ticks; legend and group bracket; genotype n; endpoint, direction and CrI labels; matching narrative and captions. Exact plot coordinates are not available, so no exact point or interval replacement is claimed.

**Exact missing inputs or definitions:** Exported CLCN1 group plotting coordinates, posterior-summary files, and a Figure 2-specific model/run identifier or population/prior mapping are absent. Those are needed to identify the exact plotted summary and explain any different output version.

**Source-grounded alternative interpretation:** The figure and narrative could represent different model runs or output versions. Their matching labels, explicit figure reference and shared information-borrowing description do not identify such a distinction. Figure 3A is compatible with the narrative magnitude at readable graphical precision, but cannot establish the exact numerical mean or upper limit by itself.

**Direct observation versus inferred explanation:** The exact narrative values, group identity and caption descriptions are direct observations. The plotted point and cap are directly visible but numerically bounded through conservative graphical reading. A different model/output version is an inferred possible explanation, not source-established execution. No exact plotted values are fabricated.

**Classification:** All compared and corroborating locations are REPORT in the same main article. Primary relationship S_W; all relationships S_W; domain statistical_results because the affected quantities are a primary mean effect and credible limit. Figure 3A only corroborates one side, and creates no additional relationship. Classification ambiguity: exact model/run identity behind the graphic remains unknown, without ambiguity in the source roles or relationship.

**Evidence state:** reproduced. Determining fact: the directly matched CLCN1 group point and upper-end graphical bounds do not overlap the narrative rounding intervals, with the group identity and primary analysis context matched. No location or numerical transcription revision was needed.

**Exact remaining human question:** Which exact exported CLCN1 group estimate and 95% credible interval should Figure 2 display, and which model output produced its group marker relative to the narrative 3.84 (2.52–5.16)?

## Derivative provenance and completion

Seven unique derivatives were produced below `preprocessing/` with direct Poppler `pdftoppm` 25.03.0, CPU only, using `-f N -l N -singlefile -scale-to 2200 -png SOURCE OUTPUT_PREFIX`:

| Derivative relative to the review directory | Exact supplied source | Physical page | Engine |
|---|---|---:|---|
| preprocessing/recheck-main-page3.png | jama_stunnenberg_2018_oi_180136.pdf | 3 | pdftoppm 25.03.0 |
| preprocessing/recheck-main-page4.png | jama_stunnenberg_2018_oi_180136.pdf | 4 | pdftoppm 25.03.0 |
| preprocessing/recheck-main-page5.png | jama_stunnenberg_2018_oi_180136.pdf | 5 | pdftoppm 25.03.0 |
| preprocessing/recheck-plan-page41.png | joi180136supp1_prod.pdf | 41 | pdftoppm 25.03.0 |
| preprocessing/recheck-results-page10.png | joi180136supp2_prod.pdf | 10 | pdftoppm 25.03.0 |
| preprocessing/recheck-results-page11.png | joi180136supp2_prod.pdf | 11 | pdftoppm 25.03.0 |
| preprocessing/recheck-results-page13.png | joi180136supp2_prod.pdf | 13 | pdftoppm 25.03.0 |

Direct layout extraction streamed to standard output with `pdftotext -layout -f FIRST -l LAST SOURCE -`; no text derivatives were written. JavaScript arithmetic reproduced the bounded-score and ratio calculations, and inverse-normal numerical evaluation reproduced the conservative quantile boundaries; neither selected nor classified candidates. No fallback capability was needed. The current-run render aids inspected were `preprocessing/xs-main-page5.png`, `preprocessing/screen-main-page6.png`, `preprocessing/screen-main-page7.png`, and `preprocessing/screen-main-page8.png`; all were preserved.

Covered IDs: C001, C002, C003, C004. Evidence states: reproduced=4; reproduced_after_transcription_correction=0; not_reproduced=0. All affected and corroborating assigned locations were found and read; no assigned location remains uncovered. Remaining human inputs are the INQoL score transformation, executed variation-prior specifications and amendment mapping, paired-test row outputs/contributor definitions, and exact CLCN1 plot coordinates/model output. These limits concern explanation or exact reconstruction, not source-location coverage. No adjudication, severity, validity, acceptance, exclusion, or final numerical change is assigned.
