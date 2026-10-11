# Statistical pass 1 — main article

Runtime agent ID: root/statistics_pass_1. Model/effort: gpt-6.1-sol/high. Start mode: FRESH_SPAWN. Exact assigned inferential scope: DOC-001 REPORT, all14 physical PDF pages, every main-article model/test/estimate/interval/P/direction relationship. Output:43 compound relationships S001–S043,5 findings,5 excluded-observation rows. Other fresh pass1 agents cover the disjoint support REPORT and PLAN relationship ranges; the coordinator merges their parts after this handoff.

The complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read. Source-linked fresh maps and source renders were used; no earlier checker/report/candidate conclusions or external material were read. Complete values and checks are in statistics/relationship_inventory.md. Every one of the9 binary rows and21 continuous rows includes all three group estimates, all three contrasts, every95%CI, each omnibus P and every NNT/SMD. No individual contrast is inferred from an omnibus P. The stated all-test rule is two-sidedα=.05; every non-null statement below uses that level. All ordinary group/adjusted-difference/RR point-containment and endpoint-order checks reconcile. Missing numerical SDs, covariances and test statistics are not inferred.

Direct confirmation engine: Poppler pdftoppm26.01.0 CPU, main-09.png, main-10.png, main-11.png in preprocessing/stat1_main. Source physical pages9–11 were freshly rendered and visually compared with all table headings/cells/footnotes; main prose is retained in the fresh source-linked map. These derivatives are aids; the exact supplied PDF remains authority.

## Findings

Fresh direct prose confirmation: Poppler pdftotext26.01.0 CPU, command `pdftotext -layout -f 4 -l 8 jama_debar_2025_oi_250046_1755300121.13587.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat1_main/prose-p4-8.layout.txt`. This new derivative confirms the exact p4 reciprocal/SMD/test definitions, p7 secondary-significance and primary later-nonsignificance statements, and p8 modalities claim against the supplied source.

### F-ST1-001

**Finding:** The Table2 health-coach versus painTRAINER NNT interval pattern does not reconcile with null-containing relative-risk intervals and the stated nonsignificant later primary comparisons; the intensity12-month NNT also lies outside its own interval.

**Relationships:** S009, S010, S011, S012, S013, S015, S016; method/definition S004,S007; primary narrative S038.

**Locations and document roles:** REPORT [main Table2, physical p9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), HC versus PT RR/NNT columns and footnotes d/e; REPORT [primary narrative, physical p7](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=7), final sentence of Primary Outcomes. Both locations are within the same REPORT; proposed relationship S_W.

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

**Locations and document roles:** REPORT [main Table3 p10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), all three SMD columns for every outcome/time row; REPORT [Table3 p11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), both global-impression blocks and footnote d; REPORT [Statistical Analysis p4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), definition of adjusted SMD. Proposed relationship S_W.

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

**Locations and roles:** REPORT [Discussion p8](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=8): “Outcomes between the2remote CBT-CP programs at6-and12-month follow-up did not differ”; REPORT [Table3 p11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Patient Global Impression of Change–General,6months, HC versus PT adjusted difference and SMD columns. Proposed relationship S_W.

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

**Locations and roles:** REPORT [Secondary Outcomes p7](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=7), first sentence: “with significantly better scores for both the painTRAINER and health coach groups compared with usual care plus at3months, persisting over12-month follow-up”; REPORT [Table3 p10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Physical functioning3months PT versus UC adjusted mean difference. Proposed relationship S_W.

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

**Locations and roles:** REPORT [main Table2, physical p9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), Pain severity6months HC/UC adjusted responses/NNT and Pain-related interference6months HC/UC adjusted responses/NNT; REPORT same page footnote d and [main Statistical Analysis p4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), NNT definition. Proposed relationship S_W.

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
# Statistical pass 1 — REPORT supplement shard

Runtime agent: /root/statistics_pass_1_reports. Fresh fixed gpt-6.1-sol/high role. Exact assigned scope: DOC-004 pp1–7; DOC-005 pp1–16 and19, with methods applicable to eTables3,4,5,7,8,9,10; DOC-006 worksheet eTable 3!A1:J115. Entire eTable11 pp17–18 was reassigned before registration and is excluded from this shard's findings, relationship IDs and exclusions.

Completed scope:120 S records(S101–S220),67 coefficient rows,39 outcome/time rows with117 explicit pairwise contrast cells,14 method/selection/numeric families. All525 workbook cells and every nonempty selection-P cell inspected. Full exact row evidence and checks are in statistics/parts/relationship_inventory_reports.md. Six findings and seven excluded-observation families below. No candidate IDs or adjudications assigned.

Evidence uses supplied sources only. New direct images: Poppler pdftoppm26.01.0 CPU,source-07.png through source-11.png andsource-14.png through source-17.png in preprocessing/stat1_reports; page17 was unused after reassignment. Source values for findings on pp7–10 and14 visually confirmed. Workbook source XML and shared strings directly confirm E3,E82,E83 and the selection-P cells. Models and method statements were read from source-linked complete transcription; copied equations were visually mapped by the current mapper. No old scientific conclusions used.

### F-ST1-101

**Title:** Seven imputation coefficients have95% intervals excluding zero alongside P values above.05.

**Locations and document roles:** REPORT [DOC-005 p8,eTable3](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8),each coefficient's estimate,95% CI andP cells. Method context is REPORT [DOC-005 pp4–5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5): linear GEE imputation model,robust standard errors. Relationship IDs:S106,S107,S112,S114,S119,S120,S126.

| Exact coefficient row | Estimate |95% CI|P|
|---|---:|---|---:|
|Pattern:2 observed follow-ups|−.28|(−.47,−.08)|.150|
|Pattern:1 observed follow-up|−.20|(−.36,−.03)|.226|
|Pattern2 × painTRAINER|−.30|(−.58,−.02)|.280|
|Pattern2 × Health Coach|−.47|(−.74,−.19)|.090|
|Site3|.19|(.08,.29)|.069|
|Site4|.15|(.05,.24)|.124|
|Education:AA degree,second occurrence|.16|(.07,.25)|.077|

**Rule and calculation:** Each printed95% interval lies wholly on one side of zero,while the corresponding P exceeds.05. Each estimate is contained and endpoints are ordered; the discrepancy is the interval-versus-test reading,not containment. Even allowing±.005 to every two-decimal interval limit,the closest-to-null bounds remain−.075,−.025,−.015,−.185,.075,.045,.065 respectively. The P rounding bands do not approach.05. No covariance or reference distribution is needed for this significance comparison. Display-precision screening does not apply to RouteA1; relative discrepancy is not applicable.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W;all compared content is REPORT in one source.
**Qualifying route:** Route A, category 1.
**Affected result or extracted value:** The inferential reading of seven fitted imputation-model coefficients used to construct the primary outcome analysis.
**Why context does not resolve it:** RouteA1 requires registration of the printed interval/test conflict. These are individual coefficient rows,not omnibus versus pairwise tests.

**Alternatives and missing definition:** P values might use another variance calculation,test reference distribution or analysis than the intervals. The report does not identify such a separation. Normal-Wald inverse calculations would be diagnostic only and are not needed for this finding.
**Exact human question:** Which interval and test specifications apply to these seven coefficients,and which printed inferential values should a reader extract?

### F-ST1-102

**Title:** Three printed coefficient intervals touch the null while corresponding P values are below.05.

**Locations and document roles:** REPORT [DOC-005 p9,eTable4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9),Age≥65 and second Education:AA degree row; REPORT [DOC-005 p10,eTable5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10),PEG score. S140,S149,S165.

**Printed values:** Age RR1.15,95% CI(1,1.33),P=.046; second AA education RR1.16,95% CI(1,1.33),P=.046; PEG OR.96,95% CI(.92,1.00),P=.037.

**Rule and calculation:** Null is1 for RR/OR. All three printed closed intervals include1 at an endpoint,while P<.05. Bounds are correctly ordered and estimates contained. This is the reverse interval/test significance conflict. Display-precision screening is inapplicable under RouteA1; no relative discrepancy is assigned.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.
**Qualifying route:** Route A, category 1.
**Affected result or extracted value:** The significance reading of age,education and PEG coefficients in the primary estimation and weighting model summaries.
**Why context does not resolve it:** RouteA1 is always registered for the printed interval-versus-test reading.

**Alternatives and missing definition:** A more precise unrounded lower limit slightly above1 for age/education,or upper limit slightly below1 for PEG,could reconcile the underlying test. The display does not provide that precision. Different test/interval constructions are another possibility. Neither possibility is asserted as the reported analysis.
**Exact human question:** What are the unrounded confidence limits,and do the printed confidence intervals and P values refer to the same inferential specification?

### F-ST1-103

**Title:** Binary education adjustment in the selection summary does not match the fitted primary model parameterization.

**Locations and document roles:** REPORT [DOC-005 p7,eTable2](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7),final variables selected for imputation and estimation; REPORT [DOC-005 p8,eTable3](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8),three education coefficient rows; REPORT [DOC-005 p9,eTable4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9),three education coefficient rows. S125,S126,S127,S148,S149,S150,S218.

**Printed values/statements:** eTable2 specifies education“any college vs.HS degree or less.” eTable3 prints education coefficients−.02,.16,.39,each with HS or less as reference; eTable4 prints educationRR.97,1.16,1.35. The first two coefficient rows carry the same AA label,and the third is Graduate degree.

**Rule and calculation:** A binary contrast against HS or less has one education coefficient. The fitted displays contain three separately estimated education coefficients against the same reference,consistent with a multi-level parameterization. Repeated labels alone are not the basis: the numerical coefficient set conflicts with the reported binary coding. Display rounding is not relevant to this discrete model-definition comparison.

**Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.
**Qualifying route:** Route B.
**Affected result or extracted value:** The education adjustment specification in the imputation and primary MCID estimation models.
**Why context does not resolve it:** A reader cannot tell whether the primary model used the reported binary collapse or distinct education categories. This changes which analysis specification accompanies extracted primary effects.

**Alternatives and missing definition:** eTable2 may describe a collapsed selection model and eTables3/4 may describe a separate final parameterization,but that change is not identified. Duplicate AA wording may refer to the college category; that wording observation is separately excluded because it is not the numerical issue.
**Exact human question:** Was education binary or multi-level in the fitted primary imputation and estimation models,and how does the final parameterization relate to the selection model?

### F-ST1-104

**Title:** Selected weighting covariates and the displayed fitted weight model do not match.

**Locations and document roles:** REPORT [DOC-005 p7,eTable2](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7),final nonresponse-weight model covariates; REPORT [DOC-005 p10,eTable5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10),all fitted covariate rows; REPORT [DOC-005 pp5–6](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5),nonresponse selection/model description. S163,S214,S218,S219. Supporting REPORT workbook: [DOC-006](../../../joi250046supp5_prod_1755300121.16087.xlsx),eTable 3!H12:J12,H18:J18,H39:I39,H81:I81,H84:I84,H108:I108.

**Printed statements/values:** eTable2 lists PEG,PHQ8,GAD7,any negative social determinant and education as additional weighting covariates. eTable5 displays PEG OR.96,PHQ8 .97,GAD7 .99,no negative social determinant1.34 and not employed1.49(1.11,2.00),P=.008; there is no education row. The printed base covariates in eTable2/pp5–6 do not include employment. Workbook unemployment H18<.001,I18=.0228 andJ18=.0591;education H12=.0156,J12=.05 andI12 blank.

**Rule and calculation:** The named final weighting model changes membership: education is selected in eTable2 but absent in its fitted model summary,while employment appears in the fit without appearing in that selected list or stated base set. This comparison requires no raw data. The blankI12 is not interpreted as a P value or proof of a failed selection test. Display rounding is not relevant.

**Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W. The workbook corroborates the unemployment selection criteria; it does not add a conflict relationship.
**Qualifying route:** Route B.
**Affected result or extracted value:** The nonresponse weights incorporated into the primary weighted MCID analysis,and the covariate list extracted as its model specification.
**Why context does not resolve it:** The printed selected list and fitted table are both presented as final model information. A reader cannot identify the actual weighting specification from their different membership.

**Alternatives and missing definition:** Education might be omitted from an otherwise incomplete coefficient summary,or eTable2 may describe another model stage. Employment might be carried into the weight model by an unstated additional rule. Neither is disclosed in the named final-list/fitted-model mapping.
**Exact human question:** Which exact covariates produced the nonresponse weights used in the primary analysis,and how should the eTable2 list be matched to eTable5?

### F-ST1-105

**Title:** One sensitivity NNT does not reproduce under the printed reciprocal definition and half-unit display rule.

**Locations and document roles:** REPORT [DOC-005 p14,eTable8](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14),Reminder Letters Added,6 months,PTvsUC;footnote d. S181,S216.

**Printed values:** PT35.6%,UC21.3%,NNT8(5,14). Footnote d defines NNT as one over the difference in adjusted improvement percentages.

**Rule and calculation:** Point reciprocal100/(35.6−21.3)=6.99300699. Percentage rounding bands[35.55,35.65] and[21.25,21.35] yield RD[14.20,14.40] percentage points and reciprocal[6.94444444,7.04225352]. Printed integer8 gives[7.5,8.5]. Interval gap=.45774648;relative gap=.45774648/8=.05721831>.05. The same reciprocal/display method reconciles the other44 sensitivity NNT cells under the zero-gap or≤.05 rule,as explicitly recorded in eachS row. For example,eTable8 Letters3 PT/UC100/(31.6−20.5)=9.0090 with printed9;Letters6 HC/PT100/(40.6−35.6)=20 with printed20.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.
**Qualifying route:** Route A, category 4.
**Affected result or extracted value:** PTvsUC6-month sensitivity NNT after reminder letters.
**Why context does not resolve it:** Under the required half-unit display rule,the displayed reciprocal result differs by more than.05 relative discrepancy. RouteA4 registers a row not reproduced by a method that reproduces the rest of the same display.

**Alternatives and missing definition:** A deliberate upward integer rounding convention could reconcile8 when the unrounded reciprocal lies just above7. This convention is supported by several other NNT cells;for example,eTable7 Complete3 PT/UC reciprocal12.195 is displayed13,and eTable8 Letters3 HC/UC reciprocal7.353 is displayed8. The supplied footnote does not state a ceiling convention. The independent inclusion screener must consider that source-supported alternative under the normative display rule; no correction is proposed.
**Exact human question:** Which NNT integer-rounding convention was used,and what unrounded adjusted risks and NNT underlie the printed8?

### F-ST1-106

**Title:** The workbook current-depression count and percentage do not reconcile with its stated missingness-adjusted denominator.

**Locations and document roles:** REPORT [DOC-006 workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx),worksheet eTable 3!E82,current depression in All Observed;comparator E3 population,E83 missing,andA110 denominator rule. S220.

**Printed values:** E82“711(73.2)”;E3“N=1568”;E83 missing2. A110 says missing observations are excluded from the percentage denominator.

**Rule and calculation:** Count denominator1568−2=1566.100×711/1566=45.40229885%,not73.2%. Conservative half-unit intervals on all displayed inputs: count[710.5,711.5],population[1567.5,1568.5],missing[1.5,2.5],denominator[1565,1567],recomputed percentage[45.34141672,45.46325879]. Printed percentage interval[73.15,73.25]. Gap27.68674121 percentage points;relative gap27.68674121/73.2=.37823417>.05. Integer counts taken as exact would make the discrepancy stronger.

**Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.
**Qualifying route:** Route A, category 3.
**Affected result or extracted value:** The prevalence of current depression among participants with all primary-outcome follow-ups observed.
**Why context does not resolve it:** RouteA3 applies to the count/percentage/denominator discrepancy in a single display.

**Alternatives and missing definition:** An unstated denominator around971 would yield73.2% for711,but the displayed All Observed population and missingness row provide1566. No separate analysis subset is identified.
**Exact human question:** Which denominator and percentage correspond to the printed711 current-depression participants in the All Observed group?

## Excluded observations

Each row is one apparent issue family; checks that reconcile are recorded only in the S inventory.

|Location|Observation|Reason code|
|---|---|---|
|REPORT DOC-005 p7 eTable1 observed-pattern counts|188+283+1568=2039 versus2036; implied observations5458 versus5449. Conservative half-unit gaps1/2036=.00049 and4.5/5449=.00083,within.05 scope rule.|ROUNDING_OR_DISPLAY_PRECISION|
|REPORT DOC-005 p8 eTable3 Time6M,SexMale,Age≥65,1+musculoskeletal conditions and interaction rows without a null/test conflict|Normal-Wald back-calculated P values can differ from exact printedP—for example Time6M diagnosticSE(.19−.07)/3.92=.03061,Z4.247 versusP.025. Exact test distribution,sidedness and variance mapping are not supplied; an exact-test mismatch is not established. The seven observable null/test conflicts are emitted asF-ST1-101.|CONDITIONAL_OR_UNREPORTED|
|REPORT DOC-005 pp8–9 eTables3–4 repeated AA education wording|Two education rows carry AA labels. Level ordering and other categories suggest a college label;wording alone is not registered. The conflicting binary versus multi-level model specification is separatelyF-ST1-103.|TERMINOLOGY_OR_WORDING|
|REPORT DOC-005 p11 eTable7 andp14 eTable8 NNT cells other thanF-ST1-105|Small reciprocal-versus-integer differences all have zero interval gap or relative gap≤.05;each of44 individual computations is retained in itsS record.|ROUNDING_OR_DISPLAY_PRECISION|
|REPORT DOC-005 p14 eTable8,before8/9/2021,listed3-month arm counts|149+153+152=454 randomized,while only366 have any follow-up. This comparison concerns a per-time-point contributor label and does not change the randomized analysis-population size or decision rule.|PERIPHERAL_COMPARISON|
|REPORT DOC-005 p15 eTable9 caption“adjusted relative risk” versus prose/footnote|Surrounding heading,paragraph and explicit footnote all identify GEE without adjustment,weighting or imputation. Analysis identity is immediately recoverable.|CONTEXT_RESOLVES|
|REPORT DOC-005 p16 eTable10 social/physical median differences versus mean contrasts|The group statistics are explicitly medians/IQRs,while the contrasts are GEE mean differences. Subtraction of medians is not a test of the stated mean-analysis identity.|CONDITIONAL_OR_UNREPORTED|

## Limitations and completion

All assigned relationship families are PASS_1_COMPLETE;pass2 is pending for a different fresh agent. No exact coefficient reference distribution,covariance matrix,degrees of freedom or sidedness is inferred. Diagnostic normal approximations cannot replace the reported analysis. Histograms have no exact printed bin heights. eTable11 is outside the amended shard and is assigned separately. No scientific gap remains in this shard. Inclusion screening remains independent;all emitted findings retain their source-grounded alternatives.

# Statistical pass 1 — PLAN specifications and implementation

- Runtime agent ID: root/statistics_pass_1_plans.
- Model and effort: gpt-6.1-sol / high; FRESH_SPAWN, pass 1 only.
- Exact scope: DOC-002 protocol physical pages 1–77 and DOC-003 SAP physical pages 1–29. Matching REPORT methods and result labels were used to assess implementation of planned specifications. REPORT estimate/interval/test pairs are assigned to separate statistical shards.
- Relationship scope: S221–S288, 68 relationships. Every record is PASS_1_COMPLETE; pass 2 is pending.
- Findings: 3, F-ST1-221, F-ST1-222, F-ST1-223. Excluded apparent observations: 11. No finding count was targeted.

QUALITY_CONTROL_SCOPE.md and the complete review contract were read. The four fresh PLAN map parts, relevant raw source OCR, amendment histories and direct page images were consulted. Direct visual checks include protocol pages 56–57, SAP pages 19–21, results supplement pages 4/9 and main article page 4. Main and supplement method passages were matched to outcome, time, contrast and population before comparison. PLAN font-corrupted native text was not treated as scientific authority. New REPORT page renders used direct Poppler pdftoppm 26.01.0 at 140 dpi, CPU, saved to preprocessing/stat1_plans/report-p04.png, report-p09.png and main-p04.png. Pre-existing page images were preserved. No web, external reference, old checker conclusion or unpermitted Python was used.

## Findings

### F-ST1-221

**Title:** Age is called a prespecified base adjustment variable without being part of the supplied fixed primary model specification.

**Relationships:** S262. Proposed relationship type P_R; all relationships P_R. Focus area D. Proposed review domain protocol_report.

**Exact locations and document roles:**

- PLAN [protocol physical page 56, section 15.5](../../../joi250046supp1_prod_1755300121.14087.pdf#page=56): primary-model adjustment paragraph.
- PLAN [SAP physical page 20, section 14.0](../../../joi250046supp2_prod_1755300121.15087.pdf#page=20): primary-model adjustment paragraph, with section 13.0 on the same page as contextual alternative.
- PLAN [SAP physical pages 2–4, amendment history](../../../joi250046supp2_prod_1755300121.15087.pdf#page=2): no recorded addition of age as a fixed primary-adjustment variable; age subgroup analysis is expressly added on page 2.
- REPORT [results supplement physical page 4, Adjustment paragraph](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4): list immediately after “base set of pre-specified adjustment variables.”
- REPORT [results supplement physical page 5, Non-Response Weighting paragraph](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5): prespecified prediction-variable list also includes age.
- REPORT [results supplement physical pages 8–10, eTables 3–5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8): fitted imputation, estimation and weight models print an age term, establishing application to the reported primary analysis.

**Printed statements compared:** Both operative PLAN primary paragraphs specify baseline pain severity, sex, clinical site, rural/medically underserved residency, multisite pain and co-occurring mental health condition. The REPORT's base prespecified list adds “age” to those six covariate concepts. SAP section 13.0 lists age among demographic/descriptive candidate variables and age ≥65 among moderators, but does not specify age as a fixed primary adjustment covariate. Its dated age amendment adds subgroup analyses rather than primary fixed adjustment.

**Rule and reproduced comparison:** An analysis described as prespecified must appear in the supplied plan at the corresponding analysis role. Set comparison of the enumerated fixed primary covariates leaves REPORT age without a corresponding fixed-primary PLAN term. This is a textual specification comparison; display rounding and numerical recomputation are not applicable. The age term is present in all three fitted primary-analysis model summaries, so the observation concerns an implemented specification rather than an unused variable. Directly inspected eTable 4 prints the indicator “Age >=65 (vs. <65),” RR 1.15, 95% CI 1–1.33, P .046; those inferential values are tracked by the separately assigned REPORT statistical shard, while this finding concerns the adjustment's prespecification status.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The reported primary 3-month adjusted pain-severity response, RR and interval, and their imputation/weighting specification; interpretation of age adjustment as prespecified rather than added.

**Why context does not resolve it:** This is the always-register category for an analysis described as prespecified that the supplied plan does not contain in the claimed role. The general candidate-variable paragraph and moderator listing do not specify which demographic candidates must enter the fixed primary model.

**Source-grounded alternatives and missing definition:** The authors may have regarded the broad section 13.0 candidate list as authorization for age adjustment, or a separately documented fixed-model revision may exist outside this supplied package. The REPORT may have added age as a chosen adjustment variable while retaining the label prespecified. No direction or magnitude of its impact is inferred.

**Exact human question:** Which supplied prospective specification makes age a fixed base adjustment variable for the primary imputation, estimation and nonresponse-weight models, and how should its prespecification status be read alongside the enumerated protocol/SAP primary covariates?

### F-ST1-222

**Title:** The SAP's primary MAR description and the report's primary MNAR analysis have different stated roles.

**Relationships:** S264–S266. Proposed relationship type P_R; all relationships P_R. Focus area D. Proposed review domain protocol_report.

**Exact locations and document roles:**

- PLAN [SAP physical page 19, section 11.0 Missing Data](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19): first primary-analysis sentences and sensitivity-trigger paragraph.
- PLAN [SAP physical page 4, 07/17/24 IPW amendment](../../../joi250046supp2_prod_1755300121.15087.pdf#page=4): missing-all weighting amendment, preserving the all-randomized interpretation.
- REPORT [main article physical page 4, Statistical Analysis](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4): primary missingness addressed by nonignorable pattern-mixture imputation and missing-all IPW.
- REPORT [results supplement physical page 4, first Missing Data paragraph](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4): claims the SAP prespecified criteria for the primary analysis to use an MNAR imputation approach with weighting and regression adjustment.
- REPORT [results supplement physical page 11, eTable 7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11): complete-case approach is reported as a sensitivity analysis rather than the principal result.

**Printed statements compared:** The SAP says that for primary analyses patients with follow-up will be analyzed and missing data assumed MAR given baseline covariate adjustment. It then calls for sensitivity analyses when >15% are missing the 3-month outcome or arm missingness differs, and describes pattern-mixture imputation plus missing-all IPW as its first approach and worst/best case as its second approach. The REPORT says the >15%/differential criteria prespecified an MNAR primary analysis, and implements pattern-mixture/IPW as primary. The REPORT prints 77.1% 3-month completeness overall, 79.9% UC, 69.8% painTRAINER and 81.6% health coach.

**Rule and reproduced comparison:** Keep method identity separate from its planned primary/sensitivity role. Pattern-mixture and IPW are indeed in the SAP; this finding concerns the explicitly stated primary MAR role versus the implemented primary MNAR role and the REPORT's claim of a prespecified switch. The supplied SAP does not expressly say that meeting the trigger replaces the primary MAR analysis with the MNAR approach. Arithmetic confirms the trigger was met: 100−77.1=22.9% missing at 3 months, exceeding 15%; arm completeness also differs. There is no rounding-sensitive numeric inconsistency: the logical discrepancy is the analysis role. Recomputed numeric interval for overall missingness is [22.85%,22.95%] from completeness 77.1±0.05%, entirely above the displayed 15±0.5% threshold.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The principal adjusted 3-month MCID response/RR and intervals, and whether they represent the planned primary MAR analysis or a promoted missing-data sensitivity approach.

**Why context does not resolve it:** This is the always-register category for a planned primary analysis that is replaced, and for a claimed prespecified analysis role absent from the explicit supplied specification. The SAP's first-approach language supplies a possible interpretation of the switch, but does not explicitly reconcile its earlier primary-MAR sentences.

**Source-grounded alternatives and missing definition:** The first approach after the trigger may have been intended as the conditional primary analysis, with worst/best case alone designated sensitivity; the prose can support that interpretation. Alternatively, both approaches may have been planned sensitivities while the REPORT selected MNAR as primary. The July2024 amendment authorizes weighting for an all-randomized estimand but does not separately state a replacement of the primary MAR role. No judgment about a preferred missing-data method is made.

**Exact human question:** Did the >15%/differential-missingness trigger prospectively replace the SAP's stated MAR primary analysis with the MNAR pattern-mixture/IPW analysis, and where does the supplied plan explicitly define that primary-versus-sensitivity role?

### F-ST1-223

**Title:** Reported baseline adjustment for key secondary outcomes includes the outcome's own baseline, beyond the operative secondary plan paragraph.

**Relationships:** S267–S268. Proposed relationship type P_R; all relationships P_R. Focus area D. Proposed review domain protocol_report.

**Exact locations and document roles:**

- PLAN [protocol physical page 57, section 15.6](../../../joi250046supp1_prod_1755300121.14087.pdf#page=57): final secondary-model paragraph.
- PLAN [SAP physical page 21, section 15.0](../../../joi250046supp2_prod_1755300121.15087.pdf#page=21): final secondary-model paragraph.
- REPORT [main article physical page 4, Statistical Analysis](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4): secondary models use the same modeling structures “with added adjustment for the given baseline secondary outcome.”
- REPORT [main article physical page 9, Table 2](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9): adjusted intensity/interference MCID results; [physical pages 10–11, Table 3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10): adjusted continuous severity, intensity, interference and functioning results.

**Printed statements compared:** The operative protocol and SAP secondary paragraphs specify baseline levels of pain severity and all stratification variables as covariates. They prescribe continuous linear and binary/count Poisson GEE with arm×time terms. The main REPORT states that the secondary analysis uses the same primary-model structures with additional adjustment for the given baseline secondary outcome. For intensity, interference, social function and physical function, that own-baseline measure is a distinct covariate from the specified composite baseline pain severity.

**Rule and reproduced comparison:** Match each secondary measure before comparing model covariates. Composite baseline severity is not identical to baseline intensity, baseline interference or baseline PROMIS function. The reported explicit addition is absent from the operative secondary specification; the supplied amendment histories do not record adding own-baseline secondary adjustment. This is a textual specification comparison with no numerical rounding interval or relative discrepancy applicable. Continuous overall severity is not counted as a distinct discrepancy because its own baseline equals the plan's baseline pain-severity measure. Global impression is not included in the affected list because no baseline PGIC collection is planned.

**Qualifying route:** Route B.

**Affected result or extracted value:** The adjusted secondary intensity/interference MCID RRs and the adjusted between-group continuous intensity, interference, social-function and physical-function differences and intervals in Tables 2–3; these outcomes also appear in the abstract and therefore are key secondary under this workflow.

**Why context does not resolve it:** The plan and report identify different covariate sets for the same outcome/time contrasts. The phrase “same proposed approach as Aim 1” establishes shared modeling structure, but does not specify the additional own-baseline covariate later described in the REPORT. Which planned covariate set produced the tabulated results matters for analysis extraction.

**Source-grounded alternatives and missing definition:** The plan's listed covariates may have been intended as a minimum rather than an exhaustive list, or own-baseline secondary adjustment may have been understood as part of that shared approach. A separate prespecified expansion is not supplied. The REPORT explicitly discloses its adjustment, so this finding does not assert that the fitted result is unidentified or that a different analysis should have been used.

**Exact human question:** Were the distinct baseline intensity, interference and PROMIS function covariates prospectively included in the secondary models, and how should the explicit REPORT addition be reconciled with the protocol/SAP secondary covariate paragraph?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN protocol pp22–23; SAP p11; explicit secondary analysis protocol p57/SAP p21 | Intensity/interference MCID measured-by cells omit 3 months while time-frame cells and explicit analysis specify 3 months; immediate analysis text supplies intended collection/analysis time. | CONTEXT_RESOLVES |
| PLAN protocol p22; SAP p11 | Interference MCID description repeats the word intensity, but the row names interference and the 7-item interference subscale; the intended endpoint is immediate. | TERMINOLOGY_OR_WORDING |
| PLAN protocol p25 versus pp57–58; SAP pp14,22 | Moderator overview says 6 months while operative interaction paragraph says primary comparison 3 months; no reported moderator result depends on either in this efficacy package. | PERIPHERAL_COMPARISON |
| PLAN protocol p27/SAP p15 versus protocol p58/SAP pp22–23 | Perceived support is measured at notification rather than baseline while mediation prose describes baseline-to3-month change; mediation results are absent and this is outside primary analysis used by this report. | PERIPHERAL_COMPARISON |
| PLAN SAP p23 | Mediation Step3a prose adjusts baseline confounders but printed assignment formula omits them; no reported mediation result uses this model. | PERIPHERAL_COMPARISON |
| PLAN protocol p5 versus p32; SAP pp3,17; REPORT main p2 | Historical KP encounter-separation amendment30 days versus operative>60 days; report follows operative>60 days and supplied evidence does not establish a changed analysis-population size or primary decision rule. | PERIPHERAL_COMPARISON |
| PLAN SAP p4; REPORT results supplement pp4,6 | Amendment rationale missing-all12.1% versus reported12.7%; the rationale is a historical missingness summary, not a conflicting primary result or analyzed population count. | PERIPHERAL_COMPARISON |
| PLAN protocol/SAP power tables pp55/16 | “Relative change” might be read as percentage increase, but table explicitly defines it as %Intervention/%UC;150%,206.7%,184.7%,172% reconcile as ratios. | TERMINOLOGY_OR_WORDING |
| PLAN primary sample-size passages; REPORT main p4 | Simple two-arm independent-proportion normal approximation need not give exactly621/arm, but reported power uses10000modified-Poisson simulations with LSD gate. Exact simulated power event/third-arm configuration are absent; no source-supported reproducing calculation is available. | CONDITIONAL_OR_UNREPORTED |
| PLAN SAP pp18,21; REPORT main p5 | Broad all-randomized wording versus exclusion of two UC EHR-ineligible participants: SAP separately qualifies eligible subjects, and the report flow explicitly locates the exclusions. This reading is immediately resolved by population qualification. | CONTEXT_RESOLVES |
| PLAN SAP pp19–20; REPORT results supplement pp4–7 | Additional predictor-selection thresholdP<.10 and exact imputation/weight covariates are detailed in REPORT but not fully in SAP. These additional variables are expressly described as selected rather than all prespecified; absent detail alone is not a finding. This does not subsume the age-prespecification issue. | CONDITIONAL_OR_UNREPORTED |

## Coverage, reconciled checks and limitations

Every assigned inferential relationship is recorded in statistics/parts/relationship_inventory_plans.md. Reconciled checks include primary endpoint status, 11-item composite, 30% threshold and 3-month time; 6/12-month secondary times; all abstract secondary outcomes and their planned status; allocation and strata; modified-Poisson RR family/link and GEE variance rationale; power input arithmetic and retention; hierarchy and LSD omnibus gate; explicit missing-data trigger and IPW amendment; worst/best-case sensitivity; after 8/9/2021 onboarding sensitivity; as-treated conditional rule; adherence 75%=6/8; planned safety descriptives/no formal testing; and no formal efficacy/futility interim analysis. No numerical interval/test conflict is printed in this PLAN scope. The planned mediation/economic specifications were completely inventoried, but absent result implementations were not invented. No broad study-design, clinical or preferred-analysis review was performed.

All106 assigned PLAN physical pages are covered by fresh source maps and this complete planned relationship inventory. Bibliography and administrative units do not add original inferential results. Exact power simulation details are absent, so no unsupported sample-size contradiction is claimed. No scientific coverage gap. Findings concern supplied textual analysis specifications, with source-grounded alternatives for independent screening and human adjudication.
# Statistical pass 1 — raw-score REPORT shard

Agent runtime task: /root/statistics_pass_1_raw. Fixed model: gpt-6.1-sol; reasoning effort: high; FRESH_SPAWN. Exact assigned scope: DOC-005 eTable11 physical pp17–18, all21 outcome/time rows, all63 raw group summaries, all63 mean-difference/95%CI pairs, all21 omnibus P values and source headers/footnote. DOC-001 p11 Table3 h/i was inspected solely to establish the global-impression measurement definition. Complete relationship records: statistics/parts/relationship_inventory_raw.md, S401–S422, every relationship PASS_1_COMPLETE; pass2 pending. Finding count1; excluded-observation count3.

The complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read. The current routing preflight is PASS and tooling record establishes direct Poppler tools with CPU processing. Sources and reusable evidence were preserved; no old scientific selection record or web source was used. New direct layout text and CPU page renders at preprocessing/stat1_raw/ were visually inspected. The source images confirm the source's explicit distinction between median/quartile group columns and GEE mean-difference/CI columns.

## Checked results

Every one of the63 contrast estimates lies within its ordered interval. Every group median lies within its ordered printed quartiles. All21 linear-contrast transitivity comparisons reconcile after half-unit rounding (interval gap0). Every significant omnibus P is accompanied by at least one null-excluding contrast CI; physical3mo P=.212 and all three contrast intervals include0. An omnibus P and an individual contrast CI have different hypotheses, so they were not mechanically equated. Unreported test statistics, covariance, sidedness and degrees of freedom were not inferred. Rounded−0.0/0.0 interval endpoints do not establish an unprinted individual-contrast P value. There are no noninferiority/equivalence margins or interim/stopping conclusions in this table. Individual contrasts were not obtained by subtracting medians. No exact Wald-P diagnostic is presented as reproduction of a reported analysis.

### F-ST1-401

**Title:** Global-impression raw-score summaries do not consistently match the printed median quantity.

**Relationships:** S417, S418, S419, S420, S422. **Compared locations and document roles:** REPORT DOC-005 [eTable11, physical p17](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17), title and “Raw Score Median (25%-tile, 75%tile)” header versus five cells listed below; REPORT DOC-001 [Table3 footnotes h/i, physical p11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), which defines both global-impression outcomes as one item with response categories1–7. REPORT DOC-005 [physical p18 footnote b](../../../joi250046supp4_prod_1755300121.15587.pdf#page=18) describes linear-GEE mean differences and CIs but does not redefine the group-summary columns.

**Printed values/statements:** The median header applies to every group summary, including Global Impression–Pain PT6mo2.8(2.7,2.9), PT12mo2.8(2.7,2.9), UC12mo2.2(2.1,2.3); Global Impression–General PT3mo2.7(2.6,2.7), UC6mo1.8(1.7,1.9). The main footnotes state one item, range1–7, with seven integer response categories from “much better” through “much worse.” Other cells include3mo HC2.0(1.0,3.0) for pain and2.0(1.0,2.0) for general, which are compatible with genuine medians/quartiles and prevent simply assuming a uniform mean/CI summary without clarification.

**Rule and calculation:** For raw single-item integer responses, an ordinary sample median is an integer (odd sample size) or the average of two integers (even size), hence belongs to {1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7}. The printed one-decimal median is allowed its ±0.05 interval. The permissible median values are exact values implied by the categorical source definition, rather than rounded input estimates. The nearest permissible value is used, making the test conservative.

| Exact eTable11 cell, REPORT p17 | Printed median | Allowed printed interval | Closest permissible median / exact interval | Remaining gap | Relative discrepancy |
|---|---:|---|---|---:|---:|
| Global pain6mo, PT column | 2.8 | [2.75,2.85] | 3.0 / [3.0,3.0] | 0.15 | 0.15/2.8=0.05357 |
| Global pain12mo, PT column | 2.8 | [2.75,2.85] | 3.0 / [3.0,3.0] | 0.15 | 0.05357 |
| Global pain12mo, UC column | 2.2 | [2.15,2.25] | 2.0 / [2.0,2.0] | 0.15 | 0.15/2.2=0.06818 |
| Global general3mo, PT column | 2.7 | [2.65,2.75] | 2.5 / [2.5,2.5] | 0.15 | 0.15/2.7=0.05556 |
| Global general6mo, UC column | 1.8 | [1.75,1.85] | 2.0 / [2.0,2.0] | 0.15 | 0.15/1.8=0.08333 |

The five remaining gaps exceed0.05 relative discrepancy. This is a reproduced incompatibility of numeric group-summary values with their declared quantity, consolidated as one summary-definition pattern. No conclusion is drawn about the actual unprinted medians or about a mean-minus-median equality.

**Focus area:** C (effect/summary-measure identity and analysis-to-number mapping), with B numeric interpretation. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_C (all relationships S_C): the scale definition and reported median quantity occur in different REPORT documents. If the rechecker treats the main definition solely as corroboration of the meaning of the scale, S_W is a source-grounded alternative classification for the internal eTable11 header/cell conflict.

**Qualifying route:** Route B. B1: the conflict concerns a reported statistical summary quantity. B2: the source does not explain whether fractional single-item values are raw medians, fitted/averaged scores, or a mixture of summaries. B3: the distinction affects extracting a median/IQR versus a mean/CI and using the printed global-impression group values in evidence synthesis.

**Affected result or extracted value:** The five named global-impression group summaries, their summary statistic, and whether the parentheses denote quartiles as printed. This finding does not itself establish a change in any omnibus or pairwise inferential conclusion.

**Why context does not resolve it:** Some3mo HC cells have integer medians with broad quartiles, while other cells have fractional centers incompatible with ordinary raw medians beyond the scope's display tolerance. The GEE footnote explicitly describes the between-group means and their CIs; it does not label the raw group cells as means or explain a mixed summary. A reader cannot choose the intended extraction quantity from the stated table definition alone.

**Source-grounded alternatives and missing definition:** The linear-GEE analysis makes fitted means a possible interpretation of some fractional centers, but the source labels those group cells medians and the footnote only defines between-group estimates. The table could use different group summaries in different cells, or a transformed/interpolated/nonordinary median of another quantity, but such a procedure is not supplied. The required definition is the exact statistic producing each raw-score group center and its two accompanying limits, and whether any noninteger preprocessed responses entered this single-item summary. No replacement values or preferred method are proposed.

**Exact human question:** What summary statistic and accompanying limits were used for the five named global-impression group cells in eTable11, and how do those definitions reconcile the fractional printed values with the stated raw-score median of a single1–7 response item?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-005 REPORT eTable11 p17, all21 rows and p18 method | The displayed group-median differences often have a different direction/magnitude from GEE mean contrasts, suggesting a possible group-column pattern. Raw medians need not equal fitted means; no source establishes their equality, so a column permutation cannot be reproduced from subtracting these medians. | CONDITIONAL_OR_UNREPORTED |
| DOC-005 REPORT eTable11 pp17–18 | Exact omnibus-P and CI-width reproduction would require covariance/variance/test implementation not supplied for this table. Missing inputs alone provide no conflicting printed numerical statement. | CONDITIONAL_OR_UNREPORTED |
| DOC-005 REPORT eTable11 p17, remaining fractional global-impression medians2.9,2.1,1.9,1.6,2.6 | Distances to the nearest permissible ordinary median after ±0.05 display allowance are at most0.05 relative discrepancy; these individual cells do not independently reproduce the numeric threshold used for F-ST1-401. Integer2.0 and half-integer2.5 centers reconcile and are not excluded observations. | ROUNDING_OR_DISPLAY_PRECISION |

## Limitations

All assigned source cells and footnotes were inspected. The source does not supply individual records, group arithmetic means for this table, a fitted covariance matrix, per-row analysis counts or test statistics; no convention was substituted for these missing inputs. The finding concerns the printed summary quantity and named numeric cells, not a raw-data audit. Independent inclusion screening and exact-source mechanical recheck remain the coordinator's next stages.
