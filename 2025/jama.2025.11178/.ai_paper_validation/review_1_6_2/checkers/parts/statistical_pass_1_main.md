# Statistical pass 1 — main article

Runtime agent ID: root/statistics_pass_1. Model/effort: gpt-6.1-sol/high. Start mode: FRESH_SPAWN. Exact assigned inferential scope: DOC-001 REPORT, all14 physical PDF pages, every main-article model/test/estimate/interval/P/direction relationship. Output:43 compound relationships S001–S043,5 findings,5 excluded-observation rows. Other fresh pass1 agents cover the disjoint support REPORT and PLAN relationship ranges; the coordinator merges their parts after this handoff.

The complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read. Source-linked fresh maps and source renders were used; no earlier checker/report/candidate conclusions or external material were read. Complete values and checks are in statistics/relationship_inventory.md. Every one of the9 binary rows and21 continuous rows includes all three group estimates, all three contrasts, every95%CI, each omnibus P and every NNT/SMD. No individual contrast is inferred from an omnibus P. The stated all-test rule is two-sidedα=.05; every non-null statement below uses that level. All ordinary group/adjusted-difference/RR point-containment and endpoint-order checks reconcile. Missing numerical SDs, covariances and test statistics are not inferred.

Direct confirmation engine: Poppler pdftoppm26.01.0 CPU, main-09.png, main-10.png, main-11.png in preprocessing/stat1_main. Source physical pages9–11 were freshly rendered and visually compared with all table headings/cells/footnotes; main prose is retained in the fresh source-linked map. These derivatives are aids; the exact supplied PDF remains authority.

## Findings

Fresh direct prose confirmation: Poppler pdftotext26.01.0 CPU, command `pdftotext -layout -f 4 -l 8 jama_debar_2025_oi_250046_1755300121.13587.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat1_main/prose-p4-8.layout.txt`. This new derivative confirms the exact p4 reciprocal/SMD/test definitions, p7 secondary-significance and primary later-nonsignificance statements, and p8 modalities claim against the supplied source.

### F-ST1-001

**Finding:** The Table2 health-coach versus painTRAINER NNT interval pattern does not reconcile with null-containing relative-risk intervals and the stated nonsignificant later primary comparisons; the intensity12-month NNT also lies outside its own interval.

**Relationships:** S009, S010, S011, S012, S013, S015, S016; method/definition S004,S007; primary narrative S038.

**Locations and document roles:** REPORT [main Table2, physical p9](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), HC versus PT RR/NNT columns and footnotes d/e; REPORT [primary narrative, physical p7](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=7), final sentence of Primary Outcomes. Both locations are within the same REPORT; proposed relationship S_W.

| Outcome/time | Printed HC/PT RR95%CI | Printed HC−PT NNT95%CI | Direct comparison |
|---|---|---|---|
| Severity6months |1.13(0.98–1.30)|24(12–186)|RR interval includes1; narrative says the later HC/PT differences are no longer significant, while NNT endpoints are finite and positive. |
| Severity12months |1.07(0.96–1.19)|41(17–76)|Same conflict with printed nonsignificant comparison. |
| Intensity3months |1.11(0.93–1.33)|37(14–57)|RR null-containing vs finite positive NNT interval under the same reported response contrast. |
| Intensity6months |1.18(1.00–1.40)|21(11–5524)|Printed RR endpoint equals the null; positive finite NNT bounds. This row may reflect a rounded RR endpoint; preserve that alternative rather than infer the unprinted endpoint. |
| Intensity12months |1.05(0.92–1.20)|63(18–38)|The NNT point63 exceeds its upper95%limit38; RR interval includes1. |
| Interference6months |1.10(0.96–1.27)|26(11–67)|RR null-containing vs finite positive NNT interval. |
| Interference12months |1.07(0.97–1.18)|39(16–79)|RR null-containing vs finite positive NNT interval. |

**Printed rule and calculation:** Table2d defines NNT as1 divided by the difference in adjusted response proportions. Footnote e states that an absolute-risk-difference interval containing zero leads to a positive lower NNT limit extending to infinity and a negative upper limit extending to negative infinity. The printed HC/PT NNT pairs above instead show only two finite positive endpoints. In particular,63 is not in[18,38], requiring no inference about a model or covariance. Primary narrative explicitly says the HC/PT differences at6/12months are no longer significant, whereas the positive-only printed NNT intervals do not display that null-spanning inference. For the other outcomes the RR-versus-NNT contrast supplies the parallel pattern; alternative interval procedures are named below. All other NNT point recomputations are separately addressed in F-ST1-005 or the excluded precision observation, so this finding concerns the intervals, not those point differences.

**Display precision:** RouteA category1 does not use the rounding exclusion. For the containment example even allowing integer half-units gives estimate[62.5,63.5] and upper limit[37.5,38.5], a gap24 (24/63=.3810). Infinity, negative-branch interpretation and endpoint signs cannot be supplied by choosing decimals inside those intervals. The intensity6 RR endpoint1.00 may hide an unprinted positive lower limit; that possibility cannot reconcile the independent intensity12 containment or explicit later-severity nonsignificance conflicts.

**Focus area:** B, with C for the reciprocal-interval definition. **Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category1.

**Affected result or extracted value:** The health-coach versus painTRAINER adjusted NNT95%CI for primary severity at6/12months and the five secondary outcome-time rows above, including the intensity12month point/interval combination.

**Why context does not resolve it:** The point-outside-interval observation and printed interval-versus-nonsignificant test claim belong to the always-register category. Footnote e explains a disconnected interval interpretation but names a negative branch absent from the printed endpoint pairs. A data extractor cannot know whether to retain the positive signs, read one endpoint as negative, or use another interval construction.

**Source-grounded alternatives and missing definitions:** The two endpoints might be intended as disconnected branches with an omitted sign; alternatively RR and risk-difference intervals might have used different procedures, or one displayed endpoint may represent a different contrast. The source names the same response comparison and confidence level, but does not print the absolute-risk-difference intervals or the numerical covariance calculation. These alternatives do not remove the printed containment/test conflict. The intensity6 endpoint may be due to output rounding, as explicitly noted.

**Exact human question:** What signed/disconnected95%NNT limits and underlying adjusted risk-difference intervals apply to each of these HC/PT rows, and how should63(18–38) and the finite-positive later-severity intervals be read alongside the nonsignificant HC/PT comparisons?

### F-ST1-002

**Finding:** The printed Table3 SMD block does not reconcile with its own intervals and the source-defined common-SD standardization of the adjusted contrasts.

**Relationships:** S005,S017,S019,S021–S037; S018 and S020 were also checked and their standalone identity comparisons reconcile within precision. This is one consolidated block pattern, retaining all affected locations rather than issuing a finding for each cell.

**Locations and document roles:** REPORT [main Table3 p10](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), all three SMD columns for every outcome/time row; REPORT [Table3 p11](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), both global-impression blocks and footnote d; REPORT [Statistical Analysis p4](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), definition of adjusted SMD. Proposed relationship S_W.

**Printed rule:** Footnote d defines the adjusted between-group mean difference divided by the SD of change in the UC group at the same time. The same positive denominator for a row means HC−PT SMD equals HC−UC SMD minus PT−UC SMD; signs and interval null membership should agree with the same unstandardized contrast under the stated simple rescaling. The footnote supplies no separate model/estimand mapping for SMDs.

**Direct interval observations, all cells retained:**

| Source block/time | Printed SMD PT−UC; HC−UC; HC−PT | Direct interval observation |
|---|---|---|
| Severity12months,p10 |−0.25(−0.24,0.01);−0.36(−0.35,−0.12);−0.11(−0.11,0.12)|First two points below printed lower limits; PT/UC SMDCI contains0 while corresponding adjusted-differenceCI(−0.6,−0.2) excludes0. |
| Intensity12months,p10 |−0.16(−0.16,0.00);−0.27(−0.26,−0.12);−0.03(−0.03,0.11)|HC/UC point below lower limit; PT/UC SMDCI touches0 while differenceCI(−0.4,−0.1) excludes0. |
| Interference12months,p10 |−0.26(−0.25,0.01);−0.37(−0.36,−0.11);−0.12(−0.12,0.12)|First two points below lower limits; PT/UC SMDCI contains0 while differenceCI(−0.7,−0.3) excludes0. |
| Social3months,p10 |0.12(0.23,0.11);0.01(0.12,−0.00);0.20(0.29,0.19)|All three endpoint orders reversed; ordered intervals have opposite null membership from MD for all three contrasts. |
| Social6months,p10 |0.18(0.23,0.05);0.06(0.11,−0.06);0.26(0.30,0.15)|All three endpoint orders reversed; HC/UC SMD spans0 despite MD(0.8,2.2); HC/PT SMD excludes0 despite MD(−0.4,1.1). |
| Social12months,p10 |0.19(0.21,0.01);0.07(0.09,−0.10);0.27(0.28,0.12)|All three endpoint orders reversed; HC/UC SMD spans0 despite MD(0.6,2.1); HC/PT SMD excludes0 despite MD(−0.7,0.9). |
| Physical3months,p10 |0.09(0.16,0.07);−0.02(0.05,−0.04);0.16(0.22,0.15)|All three endpoint orders reversed; ordered SMD intervals have opposite null membership from MD for all three contrasts. |
| Physical6months,p10 |0.15(0.09,−0.06);0.02(−0.03,−0.18);0.22(0.16,0.05)|All three endpoint orders reversed; all three points outside even ordered intervals. PT/UC SMD spans0 despite MD(0.1,1.2); HC/UC SMD excludes0 despite MD(−0.1,0.9); HC/PT SMD excludes0 despite MD(−0.8,0.3). |
| Physical12months,p10 |0.20(0.18,−0.03);0.07(0.04,−0.16);0.27(0.25,0.09)|All three endpoint orders reversed; all three points outside even ordered intervals; all three contrasts have opposite null membership from MD. |
| Global impression pain12months,p11 |−0.55(−0.50,0.05);−0.57(−0.54,−0.08);−0.29(−0.25,0.14)|All three points below lower limits; PT/UC SMDCI contains0 despite MD(−0.8,−0.5); HC/PT positiveMD0.1 contrasts with negativeSMD−0.29 under a positive-SD definition. |

There are18 reversed SMD endpoint pairs (all social/physical cells) and14 points outside their own intervals even after sorting endpoints (2severity12,1intensity12,2interference12,3physical6,3physical12,3global-pain12). Other SMD interval checks were completed in the inventory, including the rows with contained estimates. Reordering endpoints alone does not reconcile the14 containment observations or the null/sign comparisons.

**Reproduced common-denominator calculation and display precision:** Let A be PT−UC SMD, B HC−UC SMD and C HC−PT SMD. Recomputed B−A interval allows±.010 from two printed two-decimal inputs; printed C allows±.005. The following17 rows retain a relative gap above.05. These are source-defined contrast identities, not a comparison with crude group ratios or an assumed variance estimator. Other rows are retained in the relationship inventory and not selected away.

| Outcome/time | Recomputed B−A interval | Printed C interval | Gap | Relative discrepancy |
|---|---|---|---:|---:|
| Severity3months |[−.100,−.080]|[−.135,−.125]|.025|.1923|
| Intensity6months |[−.110,−.090]|[−.045,−.035]|.045|1.1250|
| Intensity12months |[−.120,−.100]|[−.035,−.025]|.065|2.1667|
| Interference3months |[−.100,−.080]|[−.135,−.125]|.025|.1923|
| Interference6months |[−.110,−.090]|[−.145,−.135]|.025|.1786|
| Social3months |[−.120,−.100]|[.195,.205]|.295|1.4750|
| Social6months |[−.130,−.110]|[.255,.265]|.365|1.4038|
| Social12months |[−.130,−.110]|[.265,.275]|.375|1.3889|
| Physical3months |[−.120,−.100]|[.155,.165]|.255|1.5938|
| Physical6months |[−.140,−.120]|[.215,.225]|.335|1.5227|
| Physical12months |[−.140,−.120]|[.265,.275]|.385|1.4259|
| Global pain3months |[−.010,.010]|[−.375,−.365]|.355|.9595|
| Global pain6months |[−.020,.000]|[−.295,−.285]|.265|.9138|
| Global pain12months |[−.030,−.010]|[−.295,−.285]|.255|.8793|
| Global general3months |[−.010,.010]|[−.405,−.395]|.385|.9625|
| Global general6months |[−.050,−.030]|[−.245,−.235]|.185|.7708|
| Global general12months |[−.060,−.040]|[−.285,−.275]|.215|.7679|

The common-denominator identity reproduces intensity3 exactly(−.29−(−.21)=−.08), severity12 exactly(−.36−(−.25)=−.11), and interference12 within half-unit intervals; severity6 has remaining relative gap.0417 and is separately screened as display precision. Containment/null conflicts qualify independently of this numeric identity; no unknown numerical SD needs to be supplied to reproduce them.

**Focus areas:** B and C. **Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category1 for point containment/null-versus-stated-inference conflicts; the source-defined common-denominator identity also qualifies by Route A, category4 where the identity reproduces other rows of the same display. Endpoint reversals and quantity/direction discrepancies are retained as affected parts of the same SMD-block issue.

**Affected result or extracted value:** Table3 adjusted SMDs and95%CIs for the named outcome-time/contrast cells, including estimates used to describe intervention effect magnitude, direction and statistical support.

**Why context does not resolve it:** Point estimates outside their own CIs are always-register observations. Printed column labels do not show a common permutation or interval reordering that resolves both containment and the stated same-SD contrast identity. A reader extracting an SMD cannot tell whether its point, interval or contrast label applies.

**Source-grounded alternatives and missing definitions:** The SMD columns or limits may represent another contrast/order, the numerical block may have a display/transcription pattern, or another calculation may have been used instead of the printed adjusted-difference/UC-SD definition. The numerical UC SDs and an alternative SMD model are not supplied in the main article. Any different-analysis interpretation must be specified; it does not remove the direct point/interval conflicts. No independent-sample or crude standardization is substituted for the reported method.

**Exact human question:** Which point estimates, ordered95%limits, contrast assignments and UC SD denominators should be extracted for these Table3 SMD cells, and what calculation reconciles them with the defined standardized adjusted contrasts?

### F-ST1-003

**Finding:** The statement that the two modalities did not differ at6/12months conflicts with the significant6-month global-impression-of-general-change contrast.

**Relationships:** S036,S042.

**Locations and roles:** REPORT [Discussion p8](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=8): “Outcomes between the2remote CBT-CP programs at6-and12-month follow-up did not differ”; REPORT [Table3 p11](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Patient Global Impression of Change–General,6months, HC versus PT adjusted difference and SMD columns. Proposed relationship S_W.

**Printed values:** HC−PT adjusted difference−0.2(95%CI−0.4 to−0.1); SMD−0.24(95%CI−0.41 to−0.07); row omnibusP<.001. Two-sidedα=.05 is stated onp4. Scores are1–7,higher worse, so the negative contrast favors HC. Omnibus significance is not used as the pairwise evidence: the pairwise differenceCI itself excludes0.

**Rule and calculation:** −0.4<−0.2<−0.1<0; likewise−0.41<−0.24<−0.07<0. Both printed95%CIs exclude the no-difference value; a statement that these outcomes did not differ conflicts with that pairwise inference at the stated level. The omnibus gate is open independently(P<.001). No standard error, degrees of freedom or covariance need be assumed for this null-exclusion check.

**Display precision:** RouteA category1 is not screened by rounding; even the0.05-unit upper-limit interval[−.15,−.05] cannot reach0. The SMDCI provides independent corroboration, rather than an assumed transformed test.

**Focus area:** B. **Proposed review domain:** statistical_results. **Qualifying route:** Route A, category1.

**Affected result or extracted value:** The6-month health-coach versus painTRAINER comparison in global perception of overall change, and the conclusion that the two modalities show no later outcome differences.

**Why context does not resolve it:** The printed CI contradicts the stated nonsignificance claim, an always-register category. The sentence uses plural“outcomes” after discussing pain, functioning and patient-global outcomes, and supplies no restriction excluding the general-change measure.

**Alternatives and missing definition:** The narrative might have intended only the binary primary severity outcome, or a different adjusted/multiplicity analysis than Table3. Primary-severity HC/PT6/12CIs do contain1. This explains a possible narrower intended claim but does not remove the printed broader inference conflict; the required narrative outcome scope/test is missing.

**Exact human question:** Does the no-difference statement apply only to primary pain severity, or what analysis reconciles it with the printed significant6-month HC/PT global-general contrast?

### F-ST1-004

**Finding:** The secondary-outcome narrative says both interventions had significantly better3-month scores, while the physical-function PT versus UC interval includes no difference.

**Relationships:** S029,S040; testing rule S007.

**Locations and roles:** REPORT [Secondary Outcomes p7](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=7), first sentence: “with significantly better scores for both the painTRAINER and health coach groups compared with usual care plus at3months, persisting over12-month follow-up”; REPORT [Table3 p10](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Physical functioning3months PT versus UC adjusted mean difference. Proposed relationship S_W.

**Printed values:** PT−UC adjusted difference0.4(95%CI−0.1 to0.9); HC−UC0.7(0.2 to1.2); omnibusP=.02. Global two-sidedα=.05 is stated. The PT contrast interval includes0, while the HC contrast excludes0; thus omnibus significance is coherent without making both pairwise comparisons significant. PT/UC SMD0.09(0.16 to0.07) is a different already-consolidated display issue F-ST1-002 and is not used to supersede the unstandardized interval here.

**Rule/calculation:** −0.1<0<0.9 for the pairwise PT contrast. This conflicts with a categorical“significantly better scores for both”statement applied to the displayed3-month secondary outcomes. The omnibusP=.02 only states that some group difference exists and cannot supply significance for this individual contrast.

**Display precision:** RouteA category1 does not receive a rounding exclusion; the displayed endpoints are plainly on opposite sides of0.

**Focus area:** B. **Proposed review domain:** statistical_results. **Qualifying route:** Route A, category1.

**Affected result or extracted value:** The3-month physical-functioning painTRAINER versus usual-care-plus inference and the narrative interpretation that both interventions have significant benefits for the reported secondary scores.

**Why context does not resolve it:** The explicit significance claim and printed pairwiseCI are an always-register test conflict. The introductory“overall patterns”phrase may signal a broad summary, but it does not identify which score or comparison is exempted from“both.”

**Alternatives and missing definition:** The narrative may intend most secondary outcomes rather than each outcome, may refer to omnibus rather than pairwise significance, or may use a separate analysis. The source does not state such a restricted outcome set or test mapping in that sentence. These alternatives are retained for the independent inclusion screen; no preferred analysis is proposed.

**Exact human question:** Which secondary scores and statistical comparisons does the3-month“significantly better ...for both”statement cover, given the PT/UC physical-functionCI−0.1 to0.9?

### F-ST1-005

**Finding:** Two6-month HC versus UC NNT point estimates do not reproduce from the same table's adjusted response percentages under the printed reciprocal definition and the workflow display-precision rule.

**Relationships:** S004,S009,S015.

**Locations and roles:** REPORT [main Table2, physical p9](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), Pain severity6months HC/UC adjusted responses/NNT and Pain-related interference6months HC/UC adjusted responses/NNT; REPORT same page footnote d and [main Statistical Analysis p4](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), NNT definition. Proposed relationship S_W.

**Printed values and rule:** Severity6months HC37.1%,UC22.9%,HC/UC NNT8; interference6months HC40.9%,UC24.3%,HC/UC NNT7. Footnote d defines NNT as1 divided by the difference in adjusted proportions, consistent with the main Methods definition. This comparison uses adjusted probabilities and an adjusted NNT from the same display; it is not a comparison with crude counts.

**Calculation including display precision:** Both input percentages have0.05percentage-point half-units; their difference allows0.10percentage points.

| Row | Probability-difference interval | Recomputed NNT interval | Printed NNT half-unit interval | Gap | Relative discrepancy |
|---|---|---|---|---:|---:|
| Severity6months HC/UC |[.141,.143]|[1/.143,1/.141]=[6.993007,7.092199]|8±.5=[7.5,8.5]|7.5−7.092199=.407801|.407801/8=.050975|
| Interference6months HC/UC |[.165,.167]|[1/.167,1/.165]=[5.988024,6.060606]|7±.5=[6.5,7.5]|6.5−6.060606=.439394|.439394/7=.062771|

The same reciprocal method reproduces the other25 NNT points of the display within the specified threshold. For example, severity3months HC32.0% versus UC20.8% implies[8.849558,9.009009], overlapping printed9±.5; severity6months PT32.9% versus UC22.9% implies[9.900990,10.101010], overlapping printed10±.5. The above two residual relative gaps exceed.05 even after both input/output half-unit intervals.

**Focus areas:** B and C. **Proposed review domain:** statistical_results. **Qualifying route:** Route A, category4.

**Affected result or extracted value:** The6-month HC versus UC NNT point estimates8 for severity and7 for interference.

**Why context does not resolve it:** A defined reciprocal method reproduces other rows but leaves above-threshold gaps for these two printed quantities, an always-register category. The source does not state an alternative rounding or NNT point calculation rule.

**Source-grounded alternatives and missing definition:** Upward rounding to the next integer could produce8 from an inverse near7.04 and7 from an inverse near6.02; it is a concrete alternative to ordinary half-unit display rounding and may be the intended NNT presentation. An unprinted alternate risk-difference estimator or rounding policy is also possible. Neither the table footnote nor main Methods specifies upward-integer rounding. This finding asks for that policy, without proposing another analysis.

**Exact human question:** Were these NNT points intentionally rounded upward to the next integer, or which adjusted probability differences and presentation rule generate8 and7 from the same-row percentages?

**Full same-display alternative check:** A policy that rounds an unprinted reciprocal upward to an integer can reproduce every one of the27 printed Table2 NNT points when the printed response percentages retain their0.05percentage-point input intervals. The table below gives all corresponding inverse ranges, in the source contrast order PT−UC;HC−UC;HC−PT, and the printed NNT triplet. Every printed integer is attainable by a ceiling operation on some value in its inverse interval. This is a concrete fully reproducing alternative, not merely a generic mention of rounding; no nearest-integer policy is claimed to be necessary. The finding records the mandated half-unit comparison and asks which presentation policy applies.

| Outcome/time | Inverse ranges for all three contrasts | Printed NNTs |
|---|---|---|
| Severity3months |[16.9492,17.5439];[8.8496,9.0090];[18.1818,18.8679]|18;9;19|
| Severity6months |[9.9010,10.1010];[6.9930,7.0922];[23.2558,24.3902]|10;8;24|
| Severity12months |[11.2360,11.4943];[8.8496,9.0090];[40.0000,43.4783]|12;9;41|
| Intensity3months |[14.9254,15.3846];[10.6383,10.8696];[35.7143,38.4615]|16;11;37|
| Intensity6months |[16.9492,17.5439];[9.2593,9.4340];[20.0000,20.8333]|18;10;21|
| Intensity12months |[17.2414,17.8571];[13.5135,13.8889];[58.8235,66.6667]|18;14;63|
| Interference3months |[13.6986,14.0845];[8.1301,8.2645];[19.6078,20.4082]|14;9;21|
| Interference6months |[7.8125,7.9365];[5.9880,6.0606];[25.0000,26.3158]|8;7;26|
| Interference12months |[10.9890,11.2360];[8.4746,8.6207];[35.7143,38.4615]|12;9;39|


## Excluded observations

Only apparent issues decided not to emit are listed; reconciled routine checks remain in the inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT mainp4 Sample Size | Exact2331/90% simulation result cannot be regenerated from rates,retention and10000 simulations alone: joint outcome/cluster/covariate generation parameters and simulation precision are not supplied. There is no contradictory printed simulation input/result, so an independent-sample power approximation is not substituted. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p9 Table2, the25 NNT points other than HC/UC severity6 and interference6 | Half-unit reciprocal calculations overlap the printed NNT interval or leave a relative gap at most.05. The two above-threshold points are F-ST1-005, not excluded. Largest remaining gap is HC/UC interference3: inverse[8.1301,8.2645] vs printed9 half-unit[8.5,9.5], gap.2355/9=.0262. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp10 Table3 severity6SMD contrast identity | B−A=−.36−(−.26)=−.10 versusC−.12. Recomputed[−.110,−.090],printed[−.125,−.115],gap.005/.12=.0417≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp7 secondary SMD narrative vsTable3p10 | PT−.26 vs−.25 half-unit intervals touch;HC−.36 vs−.34 leaves gap.010/.36=.0278≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp11 Table3global blocks,heading/footnotes h/i | Heading“mean change from baseline”could be read as subtraction, but the named one-item Patient Global Impression of Change and1–7 footnotes show these2.0–2.9group entries are mean perceived-change ratings. Immediate context resolves the quantity. | CONTEXT_RESOLVES |

## Limitations and complete coverage

No scientific main-page or table-cell gap. Numerical UC SDs, covariance matrices, individual pairwise P values and full simulation-generating inputs are absent; methods are checked only to the supplied precision/definitions. Main sample-size simulation is not reconstructed by replacing its stated method. Main text supplies no numerical standard errors or test statistics and no noninferiority/equivalence/interim/stopping decision. All43S records are PASS_1_COMPLETE and await a fresh PASS 2 agent. Numeric-only counts/means/safety are assigned to the independent numeric reviewer. Support methods were read solely to clarify main-model steps; support/plan scientific ownership remains disjoint.
