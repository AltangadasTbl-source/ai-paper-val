# Appended-ID Mechanical Evidence Recheck — Statistical Pass 2

Runtime task: `/root/pass_2_rechecker`. Fresh named `qc162_evidence_rechecker`, run model `gpt-6.1-sol`, reasoning effort `high`. Assigned scope: **C007 only**, including the target, all five same-page comparator results and the reported statistical method. C001–C006 and the canonical recheck artifact were not modified. C007 remains **Pending Human Adjudication**.

Authority: exact supplied main article PDF pp.3 and6. Direct CPU Poppler `pdftotext -layout -f 3 -l 3 jama_urashima_2019_oi_190023.pdf -` and the analogous p.6 command reread those source pages. Their current-run direct-source renders, `preprocessing/cross-main-p3.png` and `preprocessing/recheck-main-p6.png`, were inspected visually. Both tools were recorded as available in `tooling_record.md`; device CPU. No OCR, fresh derivative file, fallback, external evidence or source/reused-asset mutation was needed. The registered candidate, new checker finding and independent pass-2 screen served as locators; their source assertions were independently confirmed. The numerical calculation below was independently recomputed in JavaScript.

| ID | Evidence state | Primary relationship type | All relationships | Review domain | Classification correction |
|---|---|---|---|---|---|
| C007 | reproduced | S_W | S_W | statistical_results | None |

## C007 — Age-adjusted interval and P value lack a joint solution under a same-page reproducing calculation

**Location found / source value matched / comparator matched:** Yes, separately for every compared location:

| Exact supplied-source location | Role by content | Source-confirmed value or statement | Recheck fact |
|---|---|---|---|
| [Main PDF p.6, right-column age-quartile-adjusted relapse/death paragraph](../../../../jama_urashima_2019_oi_190023.pdf#page=6) | REPORT | Adjusted HR 0.66; 95% CI 0.43–0.99; P=.048. HRs adjusted by age quartile because the vitamin D group was older. The paragraph says relapse/death cumulative hazard was significantly less in that group. | Target attribution and all three printed numbers matched direct PDF text and source raster. |
| [Main PDF p.6, Figure 2A](../../../../jama_urashima_2019_oi_190023.pdf#page=6) | REPORT | Relapse or death: HR 0.76; 95% CI 0.50–1.14; P=.18. | S001 comparator found and matched visually and in direct source text. |
| [Main PDF p.6, Figure 2B](../../../../jama_urashima_2019_oi_190023.pdf#page=6) | REPORT | Death: HR 0.95; 95% CI 0.57–1.57; P=.83. | S002 comparator found and matched visually and in direct source text. |
| [Main PDF p.6, Figure 2C and right-column first relapse paragraph](../../../../jama_urashima_2019_oi_190023.pdf#page=6) | REPORT | Relapse by competing-risk analysis: subdistribution HR 0.75; 95% CI 0.48–1.17; P=.21. Narrative states no significant difference. | Both occurrences of S003 found; their values match. The distinct subdistribution effect label is retained. |
| [Main PDF p.6, right-column middle-baseline relapse paragraph](../../../../jama_urashima_2019_oi_190023.pdf#page=6) | REPORT | Middle baseline 25(OH)D subgroup: subdistribution HR 0.44; 95% CI 0.21–0.89; P=.02; relapse significantly lower in vitamin D group. | S009 comparator found and matched. No P value from the separate interaction or low-baseline result is substituted. |
| [Main PDF p.6, adjusted-death sentence adjacent to target](../../../../jama_urashima_2019_oi_190023.pdf#page=6) | REPORT | Adjusted death HR 0.81; 95% CI 0.48–1.36; P=.42; no significant difference. | S017 comparator found and matched; its adjacency and adjusted status are confirmed. |
| [Main PDF p.3, Statistical Analysis and post hoc analyses](../../../../jama_urashima_2019_oi_190023.pdf#page=3) | REPORT | Cox proportional-hazards model determines HRs and 95% CIs; values with two-sided P<.05 are significant. Competing-risk regression uses subdistribution HRs and 95% CIs. HRs adjusted by age quartiles or stage I status are expressly post hoc. Stata14.0 named. | Relevant method, interval level, sidedness and age adjustment matched. The text does not specify the target row's named test or CI construction. |

The six result rows comprise the one target plus five supporting comparators; the comparators are not additional discrepant results. No repeated target occurrence with another printed value was registered in C007. Every registered location has been reread, including both Figure2C and its narrative copy.

**Consistency rule applicable:** Yes, with an explicit diagnostic boundary. The registered rule is symmetric log-Wald inference: b=ln(H), q=1.959963984540054, L=exp(b−q×SE), U=exp(b+q×SE), and two-sided P=2Φ(−abs(b)/SE). Joint symmetry requires H²=L×U. This calculation numerically reproduces all five other complete same-page triples, including the adjacent adjusted-death result, after allowing every input its display interval. It is not attributed to the authors as their actual method. The method names on p.3 establish outcome/model context and two-sided significance, without establishing the exact inferential construction.

**Calculation reproduced / display-precision interval check:** Yes. The target's half-unit intervals are H∈[.655,.665), L∈[.425,.435), U∈[.985,.995), and printed P∈[.0475,.0485). Allowing the HR and both CI limits jointly, rather than inserting their rounded centers separately, yields these conservative closed-bound extrema:

| Joint diagnostic extremum | H | L | U | SE | abs(b)/SE | Two-sided diagnostic P |
|---|---:|---:|---:|---:|---:|---:|
| Minimum P | .655 | .435 | .986264367816 | .208824859934 | 2.026195748348 | .042744729167580 |
| Maximum P | .655 | .431180904523 | .995 | .213324073718 | 1.983461294226 | .047315926395588 |

To confirm that these are joint extrema: for fixed H, diagnostic P increases with U; admissibility imposes U≥H²/.435. At fixed U<1, P decreases with H. On the lower-U feasibility boundary U=H²/.435, P increases with H. Thus both extrema use the minimum H=.655, with U=.995 for maximum P and L=.435 for minimum P. The feasible maximum H is additionally restricted by H²≤.435×.995; that restriction does not enlarge either bound. Closed endpoints conservatively allow more values than the actual half-open rounding intervals, so neither exclusion of the boundary .435 or .995 nor ordinary tie handling can increase the maximum.

The joint diagnostic interval **[.042744729167580,.047315926395588]** is below the printed interval [.0475,.0485). Remaining gap is **.000184073604412**; relative gap divided by printed .048 is **.003834866758583**. This small relative discrepancy is reported transparently. Under the registered Route A, category1 interval-versus-P/test rule, the general .05 relative-discrepancy exemption does not apply. The source CI excludes1 and the source P is below.05: **nominal significance agrees**, and no significance reversal is inferred.

The independently recomputed compatible examples for every supporting row are:

| Supporting relationship / printed result | Compatible unrounded H | Compatible L | Compatible U | Diagnostic P | Rounding compatibility |
|---|---:|---:|---:|---:|---|
| S001: .76 (.50–1.14); .18 | .755025 | .502246867360 | 1.135025 | .176686709753 | All four intervals satisfied |
| S002: .95 (.57–1.57); .83 | .945025 | .570644079567 | 1.565025 | .826109001109 | All four intervals satisfied |
| S003: .75 (.48–1.17); .21 | .746525 | .475025209363 | 1.173200 | .205007266743 | All four intervals satisfied |
| S009: .44 (.21–.89); .02 | .435025 | .213832095845 | .885025 | .021617031427 | All four intervals satisfied |
| S017: .81 (.48–1.36); .42 | .805025 | .477888983574 | 1.356100 | .415003737171 | All four intervals satisfied |

These are constructive numerical examples, not recovered author outputs. They confirm support for the same diagnostic calculation; they do not prove a shared actual inference method for Cox and competing-risk results.

For independent numerical verification, two-sided normal tails were computed by composite Simpson integration of the standard-normal density from the positive statistic to10, using80,000 and160,000 subintervals in JavaScript. The target extrema changed by less than3×10⁻¹⁵ when the integration resolution doubled; the comparator tails changed by less than6×10⁻¹⁴. The omitted tail beyond10 is below2×10⁻²³. The refined values agree with the independent inclusion screener; the checker's approximately4.4×10⁻⁹ normal-approximation difference is a calculation-precision refinement, not a corrected source value or location.

**Necessary inputs available:** Target HR, both CI limits, printed P, their decimal precision,95% confidence level, two-sided significance threshold, age-quartile adjustment, outcome/model attribution, and all five comparator HR/CI/P triples. These suffice for the registered bounded diagnostic and its rounding check.

**Exact missing inputs or definitions:** Actual unrounded coefficient and standard error; covariance or variance estimator; named row-specific test; test statistic and any degrees of freedom; whether the P and CI use the same test; and exact CI construction. Participant-level event/censoring data and analysis code are not supplied. Those missing inputs prevent reproducing or identifying the actual author inference, distinct from reproducing the stated diagnostic incompatibility.

**Source-grounded alternative interpretation:** The source names a Cox model,95% CI and two-sided significance without naming Wald, score or likelihood-ratio inference. A score or likelihood-ratio P with a Wald CI, a different CI construction, or a separate test could therefore explain the printed tuple. The supplied method text does not establish any such explanation. Neither Stata use nor numerical compatibility of neighboring rows is treated as proof of the actual test. No replacement P, interval or preferred method is assigned.

**Direct observation versus inferred explanation:** Direct: the target and all comparator printed tuples; age-quartile adjustment; primary relapse/death attribution;95% confidence level; two-sided threshold; and lack of a named target-row inferential construction in the cited methods. Recomputed: joint diagnostic interval separation and compatible comparator examples. Inferred only: a common actual log-Wald method, a mixed CI/test construction, a separate test or a production mechanism. None of those inferred explanations is asserted as fact.

**Classification confirmation:** Every compared location is trial methods or trial results within one main article, therefore REPORT by content. The comparison is internal to that one REPORT: **Primary relationship type: S_W**; **All relationships: S_W**; **Review domain: statistical_results**, because the issue concerns estimate/interval/test logic. No PLAN is a conflicting side and no second REPORT document is compared. Precedence is unambiguous with only S_W. Classification ambiguity: none for role/type/domain; actual inferential construction is a bounded evidence limitation. No classification correction.

**Evidence state: reproduced.** Determining fact: exact source rereading confirms all registered printed values and locations, and the joint rounding diagnostic does not yield a P in the printed [.0475,.0485) interval, while the five supporting rows have compatible solutions. Source transcription required no correction. The diagnostic nature, method alternatives and unchanged nominal significance remain explicit limits of this evidence fact; they do not become an AI disposition.

**Exact remaining human question:** Which confidence-interval and two-sided test constructions, and which unrounded coefficient/standard error or test statistic, jointly produced the age-quartile-adjusted relapse/death HR.66,95% CI.43–.99 and P=.048?

**Completion:** One assigned stable ID, C007, covered in full; seven cited source-location groups found; target plus all five comparison triples matched; both Figure2C and its narrative copy checked; diagnostic reproduced with independent interval bounds; classification confirmed without correction. Remaining unresolved item: the actual row-specific inferential construction and unrounded outputs named above. No scientific-coverage gap in this assigned scope. Pending Human Adjudication.
