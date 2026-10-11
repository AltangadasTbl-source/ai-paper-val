# Workflow 1.6.2 Candidate Ledger

Pending Human Adjudication. Seven stable IDs were assigned only after independent inclusion screening. Initial IDs are ordered by the first issue-bearing REPORT location: main p.2 outcome status; main p.3 analysis specifications (checker-source order resolves same-page ties); main p.5 denominator display; main p.7 direction footnote. Earlier corroborating summaries do not change the issue anchor. C007 was appended after the fresh pass-2 screen; IDs are never deleted or renumbered.

Classification records the fresh source recheck and independent inclusion audit; it pre-fills human review without adjudication. Finding IDs in the classification table are the INCLUDE roots; duplicate findings are retained separately as provenance and map to the same candidate in the screening table.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R, P_P | REPORT main article pp.2–3 and8 vs PLAN final synopsis p19, body p25 and amendment p45; PLAN synopsis p19 vs body p25 | reproduced_after_transcription_correction | CONFIRMED | F-XS-001 |
| C002 | protocol_report | P_R | P_R | REPORT main article methods p3 and figures pp.6–7 vs PLAN initial SAP p14, final synopsis p19 and SAP p31 | reproduced | CONFIRMED | F-XS-002 |
| C003 | protocol_report | P_R | P_R | REPORT main article methods p3 and relapse/safety displays pp.6–8 vs PLAN initial SAP p14 and final SAP p31 | reproduced | CONFIRMED | F-XS-003 |
| C004 | protocol_report | P_R | P_R | REPORT main article high-baseline subgroup specification and omission pp.3–8 vs PLAN final SAP p31 and amendment p45 | reproduced | CONFIRMED | F-XS-004 |
| C005 | statistical_results | S_W | S_W | REPORT main article Table1 p5 arm headers vs genotype count/percentage rows and footnotes | reproduced | CONFIRMED | F-NUM-002 |
| C006 | statistical_results | S_W | S_W | REPORT main article Table2 p7 direction footnote vs its estimates and treatment interpretations pp.3–4 and6–7 | reproduced | CONFIRMED | F-NUM-001 |
| C007 | statistical_results | S_W | S_W | REPORT main article p6 age-adjusted result vs p6 comparator displays and p3 method description | reproduced | CONFIRMED | F-ST2-001 |

## C001 — De novo cancer outcome status differs across final plan and report

**Candidate statement:** De novo cancer is tertiary in the final plan body and amendment, while the final synopsis and report retain adverse-event/safety status.

**Qualifying route:** Route A, category 5.

**Finding IDs:** F-XS-001. **Checker provenance:** F-XS-001 (included), F-ST1-004 (duplicate retained). Statistical relationships S099 and S086.

**Exact source locations:** [REPORT main p2 Outcomes](../../jama_urashima_2019_oi_190023.pdf#page=2), [REPORT main p3 continuation and analysis populations](../../jama_urashima_2019_oi_190023.pdf#page=3), [REPORT main p8 Table3 de novo row and population footnotes](../../jama_urashima_2019_oi_190023.pdf#page=8), [PLAN final synopsis p19](../../joi190023supp1_prod.pdf#page=19), [PLAN final body p25 tertiary outcome](../../joi190023supp1_prod.pdf#page=25), [PLAN amendment p45](../../joi190023supp1_prod.pdf#page=45), and [PLAN initial synopsis p4 historical context](../../joi190023supp1_prod.pdf#page=4).

**Source evidence and comparison:** The same de novo cancer in organs other than the primary site after medication starts is a tertiary outcome in final body p25; amendment p45 separates it from secondary and safety outcomes. Final synopsis p19 instead includes it as an adverse event, not an outcome. The report names it among safety outcomes. Table3 distinguishes until-censoring per-protocol 15/227 (6.6%) versus 8/147 (5.4%), more-than-one-year per-protocol 16/243 (6.6%) versus 9/160 (5.6%), and randomized 16/251 (6.4%) versus 9/166 (5.4%). These are labeled different populations, not inconsistent counts.

**Reasoning and calculation:** Match endpoint organ restriction and post-medication timing; compare explicit outcome hierarchy. The comparison is categorical, so display-precision arithmetic is not applicable. Route A5 applies to a changed outcome status. Four source-linked labels do not identify a subsequent status amendment.

**Affected result or extracted value:** De novo cancer hierarchy and which reported analysis population/event counts represent its main analysis.

**Alternative source-grounded interpretations:** The final synopsis may retain earlier wording; a tertiary endpoint may have been presented in a safety table; a later amendment may exist but is not supplied. No subsequent amendment is inferred.

**Classification rationale:** REPORT versus PLAN conflict establishes P_R; final PLAN synopsis/body independently conflict, establishing P_P. P_R has precedence and requires protocol_report. Historical initial synopsis corroborates the earlier status only.

**Classification ambiguity:** None in document roles or relationship precedence; unprovided later amendments remain an evidence limitation.

**Registration transcription provenance:** The initial screener changed the de novo amendment date from locator/checker2012.12.8 to2012.12.18 for registration. The fresh180dpi direct-source recheck found2012.12.8 in the de novo paragraph, while the version heading and subgroup paragraph print2012.12.18. The registered evidence date is therefore corrected back to2012.12.8; the evidence state records this registration transcription correction, with the status inconsistency still reproduced. This date difference is not a standalone candidate.

**Remaining human question:** What final prespecified and reported outcome hierarchy and analysis population apply to de novo cancer?

## C002 — Planned Kaplan–Meier curves and reported Nelson–Aalen curves

**Candidate statement:** The plan specifies ITT Kaplan–Meier survival curves for primary relapse-free and key secondary overall survival; reported curves use Nelson–Aalen cumulative hazards, with no reported Kaplan–Meier counterpart.

**Qualifying route:** Route A, category 5.

**Finding IDs:** F-XS-002. **Checker provenance:** F-XS-002 (included), F-ST1-002 (duplicate retained). Statistical relationships S098, S080 and S001, S002, S004, S005, S006, S007.

**Exact source locations:** [PLAN initial SAP p14 method5c](../../joi190023supp1_prod.pdf#page=14), [PLAN final synopsis p19](../../joi190023supp1_prod.pdf#page=19), [PLAN final SAP p31 method5c](../../joi190023supp1_prod.pdf#page=31), [PLAN amendment p45](../../joi190023supp1_prod.pdf#page=45), [REPORT main p3 Methods](../../jama_urashima_2019_oi_190023.pdf#page=3), [REPORT main p6 Figure2A/B and caption](../../jama_urashima_2019_oi_190023.pdf#page=6), [REPORT main p7 Figure3 and caption](../../jama_urashima_2019_oi_190023.pdf#page=7), with [REPORT abstract p1](../../jama_urashima_2019_oi_190023.pdf#page=1) and [REPORT results p4](../../jama_urashima_2019_oi_190023.pdf#page=4) supplying survival-percentage context. The complete results-supplement map was searched for a planned-curve counterpart.

**Source evidence and comparison:** Both SAP versions prescribe Kaplan–Meier survival curves on ITT analysis. Main Methods and figure captions specify Nelson–Aalen cumulative hazards. Primary five-year survival is 77%/69% and OS 82%/81%; the report does not name the estimator for those percentages. Cox HRs 0.76 (0.50–1.14), P=.18 and 0.95 (0.57–1.57), P=.83 retain their reported labels and are not themselves numerically challenged.

**Reasoning and calculation:** Match randomized populations, endpoints and time origins; survival probability and cumulative hazard are different quantities and estimators. A named Nelson–Aalen display is not a reported planned Kaplan–Meier curve. This planned primary/key-secondary analysis comparison is categorical; display-precision arithmetic does not apply.

**Affected result or extracted value:** Planned survival-curve analysis and identification of the estimator underlying the five-year survival summaries.

**Alternative source-grounded interpretations:** Kaplan–Meier may have generated the percentages while Nelson–Aalen was used for presentation; a curve-method amendment may be unprovided. Neither is asserted as observed.

**Classification rationale:** REPORT versus PLAN method specification establishes P_R and protocol_report. The initial and final plans agree; no P_P conflict is involved.

**Classification ambiguity:** None.

**Remaining human question:** Was the planned Kaplan–Meier analysis performed or replaced, and which estimator produced the five-year survival percentages?

## C003 — Planned relapse and safety risk-ratio evaluations lack reported counterparts

**Candidate statement:** SAP method5e specifies risk ratios for relapse and safety, while the report supplies post hoc relapse subdistribution HRs and descriptive safety counts without the specified RR analyses.

**Qualifying route:** Route B.

**Finding IDs:** F-XS-003. **Checker provenance:** F-XS-003 (included), F-ST1-003 (duplicate retained). Statistical relationships S083, S086, S003, S008 and S009.

**Exact source locations:** [PLAN initial SAP p14 method5e](../../joi190023supp1_prod.pdf#page=14), [PLAN final SAP p31 method5e](../../joi190023supp1_prod.pdf#page=31), [REPORT main p3 post hoc competing-risk method](../../jama_urashima_2019_oi_190023.pdf#page=3), [REPORT main p6 Figure2C and relapse narrative](../../jama_urashima_2019_oi_190023.pdf#page=6), [REPORT main p7 Table2 relapse rows](../../jama_urashima_2019_oi_190023.pdf#page=7), and [REPORT main p8 Table3 all safety rows and footnotes](../../jama_urashima_2019_oi_190023.pdf#page=8). Complete report maps contain no relapse/safety RR counterpart.

**Source evidence and comparison:** Both SAP versions specify risk-ratio evaluation for relapse and safety. Report relapse subdistribution HRs are total 0.75 (0.48–1.17), P=.21; low-baseline 1.18 (0.64–2.19), P=.59; middle-baseline 0.44 (0.21–0.89), P=.02. Safety Table3 prints counts and percentages in three stated populations, without RRs or RR intervals.

**Reasoning and calculation:** Match endpoint definitions and compare planned versus reported measure identity and analysis status. RR and subdistribution HR are different estimands; descriptive counts do not identify whether the planned RR evaluation occurred. The issue does not require a modeled HR to equal a crude ratio. Categorical specification comparison has no applicable display-precision arithmetic. Route B: explicit statistical analysis specification is in focus; the post hoc label does not resolve the planned RR status; extraction of the named relapse/safety comparison can depend on that status. The same method5e pattern is one consolidated issue.

**Affected result or extracted value:** Relapse effect-measure coding and the status of the prespecified relapse/safety treatment comparisons.

**Alternative source-grounded interpretations:** Planned RRs may have been calculated but omitted, or a revised analysis may have replaced them; descriptive safety reporting may have been intentional. No preferred analysis is proposed.

**Classification rationale:** REPORT versus PLAN analysis specification establishes P_R and protocol_report. Both plan versions agree.

**Classification ambiguity:** None; inclusion uses Route B rather than asserting every safety/relapse result is a key secondary endpoint.

**Remaining human question:** Were the prespecified RR evaluations performed, replaced or unreported, and which reported quantities are their counterparts?

## C004 — Prespecified high-baseline vitamin-D subgroup analysis was omitted

**Candidate statement:** The final SAP includes the >40 ng/mL efficacy subgroup, while the report explicitly omits its analysis and restricts interactions to low/middle groups because only five high-baseline patients were available.

**Qualifying route:** Route A, category 5.

**Finding IDs:** F-XS-004. **Checker provenance:** F-XS-004 (included), F-ST1-005 (duplicate retained). Statistical relationships S106 and S092.

**Exact source locations:** [PLAN final SAP p31 subgroup list and interaction rule](../../joi190023supp1_prod.pdf#page=31), [PLAN amendment p45](../../joi190023supp1_prod.pdf#page=45), [REPORT main p3 low/middle interaction specification](../../jama_urashima_2019_oi_190023.pdf#page=3), [REPORT main p4 subgroup population and omission](../../jama_urashima_2019_oi_190023.pdf#page=4), [REPORT main p5 Table1 high-group counts](../../jama_urashima_2019_oi_190023.pdf#page=5), [REPORT main p7 Figure3 caption](../../jama_urashima_2019_oi_190023.pdf#page=7), and [REPORT main p8 limitations](../../jama_urashima_2019_oi_190023.pdf#page=8); [REPORT abstract p1](../../jama_urashima_2019_oi_190023.pdf#page=1) corroborates the two-group interaction context.

**Source evidence and comparison:** Final SAP lists low<20, middle20–40 and high>40 ng/mL efficacy subgroup analyses. Report says high group was not evaluated because of small numbers. The high count is 4 vitamin D plus 1 placebo, total5. Report interactions are low/middle only, including primary relapse/death P=.04 and OS P=.13.

**Reasoning and calculation:** 4+1=5 reconciles. The issue is a listed primary/key-secondary subgroup analysis omitted from reporting, not a count conflict. The supplied SAP states no minimum subgroup-size condition. Route A5 applies independently of the openly disclosed practical rationale. Categorical analysis-scope comparison has no numerical discrepancy interval.

**Affected result or extracted value:** Prespecified subgroup coverage and the two-group scope of the interaction tests.

**Alternative source-grounded interpretations:** A minimum-size condition or analysis amendment may have authorized omission, but is not supplied. The small-n rationale is observed and retained. No analysis of five patients is proposed or preferred.

**Classification rationale:** REPORT versus PLAN scope specification establishes P_R and protocol_report.

**Classification ambiguity:** None; the screen independently treated the planned efficacy subgroup as analysis of primary/key-secondary endpoints under Route A5.

**Registration transcription provenance:** Amendment p45 subgroup date2012.12.18 was independently confirmed in the direct-source recheck. Separate DBP and de novo paragraphs print2012.12.8; no date-only candidate is registered.

**Remaining human question:** Was a minimum subgroup-size condition or amendment part of the final specification governing this omission?

## C005 — Genotype percentages use unstated denominators differing from printed arm headers

**Candidate statement:** Twenty-two genotype count/percentage cells in Table1 do not reconcile with its printed 251/166 arm headers under display precision; locus-specific category sums reconstruct alternative available-case denominators that the table does not state.

**Qualifying route:** Route A, category 3.

**Finding IDs:** F-NUM-002. **Checker provenance:** Numeric finding independently screened; statistical pass1 also covers the relationship in S104, with N033–N038 and N095 numeric records.

**Exact source location:** [REPORT main p5 Table1 repeated headers, BsmI, Cdx2, ApaI, TaqI, DBP1 and DBP2 rows and all footnotes](../../jama_urashima_2019_oi_190023.pdf#page=5). The supplement genotype displays corroborate category counts only, and do not add a conflicting-document relationship.

**Source evidence and calculation:** The two table halves print vitamin D n=251 and placebo n=166. Footnote a addresses rounding of percentage totals, b BMI, and c pathology, without a genotype denominator exception. For count c, printed denominator n and integer percentage p, recompute [100(c−0.5)/(n+0.5),100(c+0.5)/(n−0.5)] and compare with [p−0.5,p+0.5]. Divide the remaining interval gap by p; all 22 affected cells exceed0.05. The complete affected-cell calculation table is retained below and in the numeric checker and independent screen.

**Affected result or extracted value:** Baseline genotype proportions and their locus-specific analysis-population denominators.

**Why context does not resolve it:** Route A3 applies to reproduced within-display count/denominator/percentage discrepancies. Inferring another denominator from category sums does not make that denominator a printed instruction.

**Alternative source-grounded interpretations:** Available-case category sums give BsmI/ApaI/TaqI/DBP2 231/150, Cdx2 230/150, and DBP1 231/148; using them reconciles all percentage cells under the precision rule. This provides a plausible missing-genotype explanation, not an assigned denominator or replacement percentage. The separate DBP1 placebo57/59 cross-location copy difference is below the workflow threshold and is not another candidate.

**Classification rationale:** All conflicting counts, headers and percentages are in one REPORT display; S_W and statistical_results apply.

**Classification ambiguity:** None; inferred available-case denominators remain an alternative interpretation.

**Remaining human question:** Which denominator should be retained for each baseline genotype proportion and subgroup-population extraction?

| Locus / genotype | Arm and printed denominator | Printed count (%) | Recomputed interval, % | Printed percentage interval | Relative discrepancy |
|---|---|---|---|---|---|
| BsmI GG | Vitamin D,251 | 175 (76) | [69.383698,70.059880] | [75.5,76.5] | 0.071581 |
| BsmI GG | Placebo,166 | 119 (79) | [71.171171,72.205438] | [78.5,79.5] | 0.079678 |
| Cdx2 GG | Vitamin D,251 | 89 (39) | [35.188867,35.728543] | [38.5,39.5] | 0.071063 |
| Cdx2 GA | Vitamin D,251 | 103 (45) | [40.755467,41.317365] | [44.5,45.5] | 0.070725 |
| Cdx2 AA | Vitamin D,251 | 38 (17) | [14.910537,15.369261] | [16.5,17.5] | 0.066514 |
| Cdx2 GG | Placebo,166 | 49 (33) | [29.129129,29.909366] | [32.5,33.5] | 0.078504 |
| Cdx2 GA | Placebo,166 | 77 (51) | [45.945946,46.827795] | [50.5,51.5] | 0.072004 |
| ApaI GG | Vitamin D,251 | 96 (42) | [37.972167,38.522954] | [41.5,42.5] | 0.070882 |
| ApaI GT | Vitamin D,251 | 104 (45) | [41.153082,41.716567] | [44.5,45.5] | 0.061854 |
| ApaI GG | Placebo,166 | 69 (46) | [41.141141,41.993958] | [45.5,46.5] | 0.076218 |
| ApaI GT | Placebo,166 | 61 (40) | [36.336336,37.160121] | [39.5,40.5] | 0.058497 |
| TaqI TT | Vitamin D,251 | 172 (74) | [68.190855,68.862275] | [73.5,74.5] | 0.062672 |
| TaqI TT | Placebo,166 | 115 (77) | [68.768769,69.788520] | [76.5,77.5] | 0.087162 |
| TaqI TC | Placebo,166 | 31 (21) | [18.318318,19.033233] | [20.5,21.5] | 0.069846 |
| DBP1 TT | Vitamin D,251 | 134 (58) | [53.081511,53.692615] | [57.5,58.5] | 0.065645 |
| DBP1 TG | Vitamin D,251 | 87 (38) | [34.393638,34.930140] | [37.5,38.5] | 0.067628 |
| DBP1 TT | Placebo,166 | 82 (55) | [48.948949,49.848943] | [54.5,55.5] | 0.084565 |
| DBP1 TG | Placebo,166 | 57 (39) | [33.933934,34.743202] | [38.5,39.5] | 0.096328 |
| DBP2 CC | Vitamin D,251 | 115 (50) | [45.526839,46.107784] | [49.5,50.5] | 0.067844 |
| DBP2 CA | Vitamin D,251 | 91 (39) | [35.984095,36.526946] | [38.5,39.5] | 0.050591 |
| DBP2 CC | Placebo,166 | 81 (54) | [48.348348,49.244713] | [53.5,54.5] | 0.078802 |
| DBP2 CA | Placebo,166 | 58 (39) | [34.534535,35.347432] | [38.5,39.5] | 0.080835 |

## C006 — Table2 hazard-ratio direction definition reverses the report interpretation

**Candidate statement:** Table2's shared footnote assigns decreased outcome probability to HR values greater than1, while its adverse-outcome contrasts and narrative interpret values below1 as lower under vitamin D.

**Qualifying route:** Route A, category 2.

**Finding IDs:** F-NUM-001. **Checker provenance:** F-NUM-001 (included), F-XS-005 and F-ST1-001 (duplicates retained). Statistical relationship S100 and all nine Table2 estimate records; numeric N054 and N097.

**Exact source locations:** [REPORT main p7 Table2 footnote a and all nine outcome/stratum estimates](../../jama_urashima_2019_oi_190023.pdf#page=7), [REPORT main p3 Statistical Analysis](../../jama_urashima_2019_oi_190023.pdf#page=3), [REPORT main p4 treatment-effect narrative](../../jama_urashima_2019_oi_190023.pdf#page=4), [REPORT main p6 relapse narrative/Figure2C](../../jama_urashima_2019_oi_190023.pdf#page=6), and [REPORT main p7 Figure3 corroboration](../../jama_urashima_2019_oi_190023.pdf#page=7).

**Source evidence and comparison:** Footnote states HR values greater than1 indicate decreased outcome probability under vitamin D. Table2 total/low/middle relapse values are 0.75,1.18,0.44; cancer-specific-death values1.09,1.45,0.78; noncancer-death values0.70,1.11,0.39. Main p6 calls middle relapse subdistribution HR0.44 (0.21–0.89), P=.02 significantly lower in vitamin D; source treatment/figure context supports vitamin D versus placebo.

**Reasoning and calculation:** For that event-hazard contrast, above1 indicates higher hazard and below1 lower hazard. The footnote assigns the opposite direction. The0.44 half-unit interval [0.435,0.445] remains below1; the four above-null values retain their side of1. Reciprocal-reference diagnostic for0.44 is [2.247191,2.298851], disjoint from its printed interval, and is not a proposed replacement estimate. Direction reversal, rather than an estimate-versus-crude calculation, qualifies under Route A2. One shared footnote affects all nine table comparisons, so the pattern is one candidate.

**Affected result or extracted value:** Treatment-reference and direction coding of all nine relapse and cause-specific-death estimates in Table2.

**Why context does not resolve it:** Route A2 applies even when adjacent text allows an intended direction to be reconstructed; a reader can still take the printed table direction rule.

**Alternative source-grounded interpretations:** The footnote may intend the reciprocal treatment contrast or the opposite inequality; neither harmonizes all printed statements without a clarification. The numeric estimates are not assigned replacement values.

**Classification rationale:** One REPORT contains both the footnote and conflicting interpretation; S_W and statistical_results apply. Plan material does not create a conflicting relationship for this issue.

**Classification ambiguity:** None.

**Remaining human question:** Which treatment-reference direction and above/below1 interpretation apply to Table2?

## C007 — Age-adjusted interval and P value lack a joint solution under a same-page reproducing calculation

**Candidate statement:** The age-quartile-adjusted relapse-free-survival HR0.66, 95%CI0.43–0.99 and P=.048 do not jointly reproduce under the symmetric log-Wald diagnostic calculation that reproduces all five other complete same-page triples after rounding.

**Qualifying route:** Route A, category 1.

**Finding IDs:** F-ST2-001. **Checker provenance:** Fresh statistical pass2; independent fresh pass2 inclusion screen. S016 was covered in both statistical passes; pass1 excluded the conditional diagnostic, and pass2 reread that exclusion under Route A1 and registered the reproduced conflict.

**Exact source locations:** [REPORT main p6 adjusted relapse/death and adjacent adjusted-death paragraphs](../../jama_urashima_2019_oi_190023.pdf#page=6); [REPORT main p6 Figure2A](../../jama_urashima_2019_oi_190023.pdf#page=6); [REPORT main p6 Figure2B](../../jama_urashima_2019_oi_190023.pdf#page=6); [REPORT main p6 Figure2C and relapse narrative](../../jama_urashima_2019_oi_190023.pdf#page=6); [REPORT main p6 middle-baseline relapse paragraph](../../jama_urashima_2019_oi_190023.pdf#page=6); [REPORT main p3 Statistical Analysis and post hoc age adjustment](../../jama_urashima_2019_oi_190023.pdf#page=3).

**Source evidence and comparison:** Target HR0.66 (0.43–0.99), P=.048. Same-page comparators: S001 .76 (.50–1.14), .18; S002 .95 (.57–1.57), .83; S003 .75 (.48–1.17), .21; S009 .44 (.21–.89), .02; S017 .81 (.48–1.36), .42. Methods name Cox models, 95%CI, age-quartile adjustment and two-sided significance, without row-specific interval or test construction.

**Reasoning and calculation:** Diagnostic b=ln(H), L=exp(b−1.95996398454×SE), U=exp(b+1.95996398454×SE), P=2Φ(−abs(b)/SE); joint symmetry H²=L×U. Target half-unit intervals H[.655,.665), L[.425,.435), U[.985,.995), P[.0475,.0485). Independent normal-tail integration gives conservative joint diagnostic P[.0427447292,.0473159264]. Maximum uses H=.655, U=.995, L=.4311809045, SE=.2133240737 and z=1.9834612942. Printed lower P boundary .0475 remains above maximum by .0001840736, relative .0038348668. Checker's rounded approximation differs by ~4.4e-9, without decision impact. Full five compatible unrounded examples and exact interval calculations are preserved in screening/inclusion_screen_pass_2.md and checkers/statistical_pass_2.md. Route A1 applies independently of the general .05 relative display rule.

**Affected result or extracted value:** Mapping of the adjusted primary relapse/death P=.048 to HR.66 and CI.43–.99.

**Why context does not resolve it:** Route A category1 interval-versus-test diagnostic discrepancy; immediate text does not identify the numerical CI/test mapping. Both printed interval and P indicate significance; no significance reversal is claimed.

**Alternative source-grounded interpretations:** A score or likelihood-ratio P with a Wald CI, another interval construction, or a separate test may explain the tuple. Actual unrounded coefficient/standard error, variance estimator, test statistic, degrees of freedom and row-specific CI/test construction are unprovided. Log-Wald is explicitly diagnostic rather than attributed to the authors. No replacement P is assigned.

**Classification rationale:** All compared locations belong to the same REPORT; S_W establishes statistical_results. PLAN is not a conflicting side; nearby results support the reproducing diagnostic only.

**Classification ambiguity:** None for role/domain; exact inferential construction is a bounded evidence limitation.

**Remaining human question:** Which confidence-interval and two-sided test constructions and unrounded inferential outputs jointly produced the printed tuple?
