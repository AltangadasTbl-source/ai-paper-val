# Stable Candidate Ledger

Pending Human Adjudication. Seven stable candidates were registered after independent screening of all15 checker findings. IDs follow the first directly conflicting REPORT location, then PLAN-only locations; shared conventions and corroborating locations do not alter source order. Every affected location from duplicate findings is retained. Evidence states are reproduced after exact-source recheck; all seven inclusion audits are CONFIRMED after the independent final audit; these fields are not adjudications. IDs will never be deleted or renumbered.

## Classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | REPORT main article pp4/5/7 vs PLAN original/final protocol and SAP pp41/103/140/160 | reproduced | CONFIRMED | F-XS-001 |
| C002 | statistical_results | S_C | S_C, S_W | REPORT main article p5 vs REPORT results supplement pp20/21/23; within REPORT results supplement pp20/21 | reproduced | CONFIRMED | F-NUM-003 |
| C003 | statistical_results | S_C | S_C | REPORT main article pp6/7/8 vs REPORT results supplement p19 | reproduced | CONFIRMED | F-NUM-002 |
| C004 | statistical_results | S_W | S_W | REPORT main article p8 Table2 point estimate, interval and test cells | reproduced | CONFIRMED | F-NUM-004 |
| C005 | statistical_results | S_W | S_W | REPORT results supplement p13 FigureS4 count, percentage and denominator | reproduced | CONFIRMED | F-NUM-001 |
| C006 | protocol_report | P_R | P_R | PLAN original/final SAP pp142/162 vs REPORT results supplement p24 TableS11 | reproduced | CONFIRMED | F-ST1-003 |
| C007 | plan_material | P_P | P_P | PLAN original protocol pp11/12/18/40/41 sample-size inputs and event forecast | reproduced | CONFIRMED | F-ST1-005 |

## C001 — BMI subgroup partition and prespecification

**Candidate statement:** The report calls all forest-plot subgroup analyses prespecified, but reports BMI<25 versus≥25 where every supplied subgroup plan specifies three categories.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Finding IDs:** F-XS-001
**Checker provenance:** cross_source_consistency_reviewer F-XS-001; duplicate statistics_pass_1 F-ST1-002.
**Qualifying route:** Route A, category 5.
**Classification rationale:** A REPORT analysis specification differs from PLAN prespecification; both protocol and SAP versions are PLAN by content.
**Classification ambiguity:** None; a separate unsupplied amendment remains a source-grounded alternative.
**Exact source locations:** REPORT [mainp4 prespecification sentence](../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4), [p5 subgroup narrative](../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5), [p7 both BMI rows and interaction](../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=7); PLAN [original protocolp41 line760](../../joi240088supp2_prod_1746815064.36071.pdf#page=41), [final protocolp103 line1779](../../joi240088supp2_prod_1746815064.36071.pdf#page=103), [original SAPp140 line2358](../../joi240088supp2_prod_1746815064.36071.pdf#page=140), [final SAPp160 line2768](../../joi240088supp2_prod_1746815064.36071.pdf#page=160). Original-SAP line2357 in a checker transcription was corrected to2358 by screening before registration.
**Source evidence:** PLAN<25,25–30,≥30kg/m²; REPORT<25 HR0.17(0.05–0.57),≥25 HR0.48(0.21–1.11), interactionP=.17, with8/139 versus17/142 events in≥25.
**Reasoning procedure:** Match primary composite, population, follow-up, BMI factor and all category boundaries; compare exact prespecification and reported analysis partition.
**Calculation:** Three planned levels become two reported levels; no supplied amendment authorizes pooling the upper categories. Display precision is not applicable.
**Affected result or extracted value:** BMI≥25 HR0.48 and interactionP=.17, and whether that exact analysis was prespecified.
**Why context does not resolve it:** RouteA category5 applies to an analysis called prespecified absent in the supplied plan in its reported form.
**Alternative source-grounded interpretations:** A later grouping choice or an unsupplied amendment may explain the contrast; prespecification of the factor alone does not specify the merged strata.
**Remaining human question:** Which supplied prespecification authorizes the two-level contrast, and how does it relate to the planned three-level BMI interaction?

## C002 — Sensitivity-analysis population headers

**Candidate statement:** TableS7 arm headers do not reconcile with its exhaustive site totals, and TableS8 per-protocol headers differ from the per-protocol population sizes printed elsewhere.

**Review domain:** statistical_results
**Relationship type:** S_C
**All relationships:** S_C, S_W
**Finding IDs:** F-NUM-003
**Checker provenance:** numeric_consistency_reviewer F-NUM-003; duplicate statistics_pass_1 F-ST1-006.
**Qualifying route:** Route A, category 3. The TableS8 matched per-protocol population discrepancy also qualifies by RouteB.
**Classification rationale:** Cross-REPORT comparisons and within-supplement totals coexist; precedence selectsS_C overS_W. One repeated sensitivity-header pattern retains both tables without asserting a production mechanism.
**Classification ambiguity:** None; an undisclosed population rule remains an alternative.
**Exact source locations:** REPORT [mainp5 Figure1 final per-protocol boxes](../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5); REPORT [supplementp20 TableS7 both headers, both site totals and all arm event rows](../../joi240088supp1_prod_1746815064.21247.pdf#page=20), [p21 TableS8 title, both headers, primary and all three component rows](../../joi240088supp1_prod_1746815064.21247.pdf#page=21), [p23 TableS10 per-protocol section](../../joi240088supp1_prod_1746815064.21247.pdf#page=23).
**Source evidence:** S7 headers233/238 sum471; site categories256 and245 sum501. S8 labels per-protocol but headers249/252; main flow andS10 per-protocol give233/238. S8 primary/component counts9/33,6/4,1/18,3/20 and percentages3.9/13.9,2.6/1.7,0.4/7.6,1.3/8.4 are retained as affected rows.
**Reasoning procedure:** Check exhaustive within-display totals; match the per-protocol analysis population across exact report locations; separate population-copy conflicts from individual percentage gaps screened within precision.
**Calculation:** S7 half-unit sum intervals[470,472] versus[500,502] leave28/471=.059448. S8 BA249 versus233 leaves15/249=.060241; AMM252 versus238 leaves13/252=.051587. All exceed.05. Individual S8 percentage gaps alone are not claimed above threshold.
**Affected result or extracted value:** Primary center-interaction and per-protocol sensitivity population sizes, every TableS8 component denominator, and per-protocol HR0.27(0.13–0.56).
**Why context does not resolve it:** S7 qualifies by routeA within-display counts. S8 leaves competing primary/per-protocol Ns attached to reported sensitivity results.
**Alternative source-grounded interpretations:** S7 may describe the full501 cohort with other headers; S8 may describe233/238 per-protocol patients with broader headers; neither population split is stated.
**Remaining human question:** Which arm sizes apply to each sensitivity display and its primary/component results?

## C003 — Center-adjusted primary event count

**Candidate statement:** The center-adjusted primary table gives nine balloon-group events while the main primary display gives eleven under the same N=249 population header.

**Review domain:** statistical_results
**Relationship type:** S_C
**All relationships:** S_C
**Finding IDs:** F-NUM-002
**Checker provenance:** numeric_consistency_reviewer F-NUM-002; duplicates cross_source_consistency_reviewer F-XS-003 and statistics_pass_1 F-ST1-007.
**Qualifying route:** Route B.
**Classification rationale:** Two REPORT documents conflict about the primary observed event count; model adjustment is distinguished from a crude/model effect comparison. The separately screened center-status wording observation is not a PLAN relationship for this candidate.
**Classification ambiguity:** None; an undisclosed restricted model cohort remains an alternative.
**Exact source locations:** REPORT [mainp7 Figure2 overall row](../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=7), [p8 Table2 primary row/headers](../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8), [p6 adjusted HR/narrative with no different cohort](../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6); REPORT [supplementp19 TableS6 primary row, headers, endpoint and adjustment footnotes](../../joi240088supp1_prod_1746815064.21247.pdf#page=19). [Supplementp21 TableS8](../../joi240088supp1_prod_1746815064.21247.pdf#page=21) is an alternative-population locator only.
**Source evidence:** Main11(4.4)/249 versusS6 9(3.9)/249; medical34(13.5)/252 in both. Adjusted HR0.32(0.16–0.62),P=.001; main HR0.32(0.16–0.63),P<.001. No HR discrepancy is claimed.
**Reasoning procedure:** Match full composite, arm, declared N, follow-up and raw count fields; assess whether adjustment identifies a changed cohort.
**Calculation:** Count half-unit intervals[10.5,11.5] versus[8.5,9.5] leave1/11=.090909; percentage intervals[4.35,4.45] versus[3.85,3.95] leave.40/4.4=.090909. Both exceed.05. The small within-S6 count/percentage gap is screened within precision.
**Affected result or extracted value:** Balloon primary event count/risk and population associated with the center-adjusted HR.
**Why context does not resolve it:** B1 primary count is in focus; B2 no new population/window explains9 versus11; B3 different counts can be extracted for the adjusted primary analysis.
**Alternative source-grounded interpretations:** An undisclosed complete-case/restricted cohort or another descriptive population could explain fewer events; similarity to a per-protocol count does not identifyS6's actual cohort.
**Remaining human question:** What observed event count and analysis population produced the adjusted result, and how does its count relate to the main11/249?

## C004 — Outside-territory stroke difference interval

**Candidate statement:** The one-year outside-territory stroke difference−0.4 lies outside its printed95%CI[−2.4,−1.7], which excludes zero alongside a nonsignificant same-row P=.72.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Finding IDs:** F-NUM-004
**Checker provenance:** numeric_consistency_reviewer F-NUM-004; duplicate statistics_pass_1 F-ST1-001.
**Qualifying route:** Route A, category 1.
**Classification rationale:** The conflicting point estimate/interval/test cells are within one REPORT table. A plan is not a conflicting comparator.
**Classification ambiguity:** None; incidence differences and Cox tests may be different analyses, retained as an alternative without removing containment conflict.
**Exact source locations:** REPORT [mainp8 Table2 one-year outside-territory stroke row: counts, difference/interval, HR/CI and P cells](../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8), with confidence/significance conventions at [p4](../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4).
**Source evidence:** BA3/249(1.2),AMM4/252(1.6); difference−0.4(−2.4 to−1.7); HR0.76(0.17–3.40);P=.72. Difference is post hoc; HR is Cox-derived.
**Reasoning procedure:** Check point containment, interval order/null and test compatibility; retain producing-analysis distinctions; use a method reproducing the other display rows only as an additional diagnostic.
**Calculation:**−0.4>−1.7; estimate[−.45,−.35] and upper bound[−1.75,−1.65] remain disjoint. Unpooled binomial Wald diagnostic yields difference−.382482 andCI[−2.436163,+1.671198]; it reproduces every other distinct non-NA Table2 difference row. Half-unit input propagation gives upper[+1.264896,+2.078084], gap2.914896/1.7=1.714645. Category1 is never rounding.
**Affected result or extracted value:** Outside-territory stroke incidence-difference interval and whether it excludes no difference.
**Why context does not resolve it:** RouteA category1 always registers the reproduced point/interval and interval/test conflict, even with a reconstructed alternative sign.
**Alternative source-grounded interpretations:** Separate Cox and incidence-difference analyses could explain test attribution; a positive upper-bound reading is a diagnostic alternative, not a final correction. The CI-construction algorithm is unstated.
**Remaining human question:** Which interval belongs to−0.4, and which analysis produced its interval and same-row test?

## C005 — Ninety-day mRS count and percentage

**Candidate statement:** The balloon-group mRS2 label at90days gives50 and2.0% under N249, and the displayed category counts total294.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Finding IDs:** F-NUM-001
**Checker provenance:** numeric_consistency_reviewer F-NUM-001; duplicate statistics_pass_1 F-ST1-004.
**Qualifying route:** Route A, category 3.
**Classification rationale:** Count, percentage and denominator conflict in one REPORT supplement figure. Main mRS inference corroborates relevance but is not a conflicting second REPORT.
**Classification ambiguity:** None.
**Exact source locations:** REPORT [supplementp13 FigureS4 balloon header and all seven category annotations, especially mRS2 2.0(N=50)](../../joi240088supp1_prod_1746815064.21247.pdf#page=13); [mainp8 mRS90-day generalized OR](../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8) is corroborative only.
**Source evidence:** BA N249; categorycounts205,36,50,2,0,0,1; percentage series82.3,14.5,2.0,.8,0,0,.4. Current source image confirmsN50.
**Reasoning procedure:** Recompute the category percentage with half-unit inputs and check exhaustive totals; preserve printed count instead of substituting a plausible intended count.
**Calculation:**50/249×100=20.080321%; recomputed[19.839679,20.321932]% versusprinted[1.95,2.05]% leaves17.789679/2.0=8.894840. Counts sum294; half-unit sum[290.5,297.5] versusN[248.5,249.5] leaves41/249=.16466.
**Affected result or extracted value:** BA90-day mRS2 count and the complete ordinal outcome distribution.
**Why context does not resolve it:** RouteA category3 always registers a within-display count/percentage/denominator conflict aboveprecision.
**Alternative source-grounded interpretations:** A hypothetical count5 fits the percentage/total, whereas count50 requires another percentage/distribution. These are alternatives; no final correction is assigned.
**Remaining human question:** Which count/distribution should be extracted and which complete ordinal counts correspond to the reported functional-outcome analysis?

## C006 — Safety-test specification

**Candidate statement:** Three safety rows label chi-square testing while both supplied SAP versions specify Fisher testing for grouped adverse events.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Finding IDs:** F-ST1-003
**Checker provenance:** statistics_pass_1 F-ST1-003.
**Qualifying route:** Route B.
**Classification rationale:** PLAN prospective method statements differ from REPORT producing-test labels; no numeric P mismatch is independently asserted.
**Classification ambiguity:** None; the chi-square variant and any method-selection amendment are unstated.
**Exact source locations:** PLAN [original SAPp142 §12.4](../../joi240088supp2_prod_1746815064.36071.pdf#page=142), [final SAPp162 lines2801–2806](../../joi240088supp2_prod_1746815064.36071.pdf#page=162); REPORT [supplementp24 TableS11 overall, nervous-system and disabling-stroke rows, superscriptsc/d and test footnotes](../../joi240088supp1_prod_1746815064.21247.pdf#page=24). [Mainp6 disabling-stroke P=.02 narrative](../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6) corroborates result relevance only.
**Source evidence:** BA249/AMM252; overall12/14,P=.84; nervous-system7/12,P=.35; disabling-stroke6/18,P=.02. Three rows footnoted chi-square, othersFisher. Source disability threshold≥2 matches main; derivative>2 is not a source conflict.
**Reasoning procedure:** Compare exact planned and reported test specifications; check possible producing routines without assuming a preferred chi-square variant.
**Calculation:** Fisher diagnostics.840916,.350060,.019621 reproduceprintedvalues. Pearson diagnostics.710285,.253089,.013126; continuity-corrected chi-square.864965,.363360,.023139 remains compatible within displayprecision (.0238,.0239,0 relative gaps after P halfunits). No changed significance is claimed.
**Affected result or extracted value:** Producing tests for the three safetyPvalues, especially disabling-stroke P=.02.
**Why context does not resolve it:** B1 method specification in focus; B2 plan/table differ without an amendment or selection rule; B3 data extraction cannot identify the actual test from printed values alone.
**Alternative source-grounded interpretations:** Fisher may have produced the values with a different footnote, or a continuity-corrected chi-square analysis may have replaced the plan; choice itself is not criticized.
**Remaining human question:** Which tests produced thesePvalues and how do reported method labels relate to the supplied Fisher specification?

## C007 — Original planned event forecast

**Candidate statement:** The original plan forecasts91 endpoint events among686 participants while its1-year risks and1:1 allocation imply approximately63 first-year events.

**Review domain:** plan_material
**Relationship type:** P_P
**All relationships:** P_P
**Finding IDs:** F-ST1-005
**Checker provenance:** statistics_pass_1 F-ST1-005.
**Qualifying route:** Route B.
**Classification rationale:** The event forecast and quantitative comparators are solely PLAN content. Main original-design history only corroborates relevance; it does not createP_R. Later512 amendment is disclosed and is not the conflict.
**Classification ambiguity:** Required-event information target versus expected first-year events is a retained missing definition.
**Exact source locations:** PLAN [original protocolp11 sample-size synopsis](../../joi240088supp2_prod_1746815064.36071.pdf#page=11), [p12 expansion728→802](../../joi240088supp2_prod_1746815064.36071.pdf#page=12), [p18 primary hypothesis/allocation](../../joi240088supp2_prod_1746815064.36071.pdf#page=18), [p40 detailed statistics](../../joi240088supp2_prod_1746815064.36071.pdf#page=40), [p41 original sample-size calculation](../../joi240088supp2_prod_1746815064.36071.pdf#page=41). [Mainp3 original802 design history](../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=3) is corroboration only; planp126 discloses later512 amendment.
**Source evidence:**686cases, estimated91events;1-year control12.2%,balloon6.25%, allocation1:1, exponential hazards13.01%/6.45%, adjustedcontrol12.76% after5%crossover at3months; nexttargets728 then802. “90%confidence” is preserved, not converted to90%power.
**Reasoning procedure:** Compare stated first-year risk/event forecast under the printed allocation; distinguish an expected count from an unstated event-information/accrual target; keep final512 design separate.
**Calculation:**343×(.122+.0625)=63.2835events. Half-unit inputs allow[63.048863,63.518413]; printed91 allows[90.5,91.5], gap26.981587/91=.296501>.05. Crossover-adjusted control hazard lowers its first-year risk toapproximately11.98%, not a higher forecast.
**Affected result or extracted value:** Original planned event target/forecast and numeric basis of686→728→802 design history; no claim against the final512target.
**Why context does not resolve it:** B1 sample-size/power inputs are in focus; B2 no horizon/accrual/event-counting step connects91 to these inputs; B3 a reader can extract materially different original event-information quantities.
**Alternative source-grounded interpretations:**91 may be a required event-information target or refer to another accumulation horizon/accrual calculation. An identified event-driven target can be coherent, but the connecting steps are not supplied.
**Remaining human question:** What quantity does91 denote, and what supplied horizon/counting/accrual calculation links it to686 and the arm risks?
