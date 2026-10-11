# Statistical consistency review — pass 2

Runtime task ID: /root/statistics_pass_2. Fresh named qc162_statistical_consistency_reviewer, gpt-6.1-sol / high; distinct from /root/statistics_pass_1. Scope: every S001–S106 relationship and C001, C002, C003, C004, C005, C006. All 106 relationships receive explicit PASS_2_COMPLETE below and in the canonical inventory. All 39 initial checker excluded-observation rows were independently revisited: numeric 9, cross-source 16, statistical pass 1 14. One new finding is emitted; 38 original exclusion rows remain excluded, representing 28 distinct apparent observations after cross-checker consolidation.

Read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md; all 106 S records; complete current ledger, single screening table and justifications, mechanical recheck and lossless checker excluded-observation union. Current initial decisions and stable-ID evidence were used only as required pass-2 inputs. No old-run conclusions, external literature, raw data or unreported model conventions were used. Document roles remain main/result supplements REPORT and protocol/SAP/amendments PLAN.

Source authority: supplied PDFs. Direct CPU Poppler pdftotext -layout reread main pp.3 and6, final SAP p.31, results supplement pp.4 and21. Current direct-source render preprocessing/recheck-main-p6.png was visually inspected against the supplied source reading. The existing exact-source recheck supplies the six candidates' complete comparison-location facts. No fresh rendering/OCR, source change, reused-asset change or additional preprocessing artifact was required. JavaScript arithmetic is auxiliary diagnostic calculation, not review orchestration.

## New findings

### F-ST2-001 — Age-adjusted relapse-free-survival interval and P value do not jointly reproduce under the same-page reproducing calculation

**Exact locations and document roles:** [REPORT main PDF p.6, age-quartile-adjusted relapse/death paragraph](../../../jama_urashima_2019_oi_190023.pdf#page=6), S016; [REPORT main PDF p.3 Statistical Analysis](../../../jama_urashima_2019_oi_190023.pdf#page=3) supplies Cox models, 95% confidence intervals, age-quartile adjustment and two-sided .05 significance. Same-page comparators are [REPORT main PDF p.6 Figure2A, Figure2B, Figure2C, middle-baseline relapse narrative and adjacent age-adjusted-death paragraph](../../../jama_urashima_2019_oi_190023.pdf#page=6), respectively S001, S002, S003, S009 and S017. All compared locations are REPORT within one document.

**Printed values:** Age-adjusted relapse/death HR 0.66, 95% CI 0.43–0.99, P=.048; adjacent age-adjusted death HR 0.81, CI 0.48–1.36, P=.42. Other complete p.6 triples are 0.76 (0.50–1.14), .18; 0.95 (0.57–1.57), .83; 0.75 (0.48–1.17), .21; and middle relapse 0.44 (0.21–0.89), .02. Source raster confirms the three age-adjusted relapse/death numbers exactly.

**Rule and calculation:** Explicitly labeled diagnostic symmetric log-Wald calculation: coefficient b=ln(HR); lower and upper limits exp(b−1.95996398454 SE), exp(b+1.95996398454 SE); two-sided P=2Φ(−abs(b)/SE). This method numerically reproduces every other complete effect/CI/P triple printed on p.6, including the adjacent adjusted-death result. It is not assumed to be the authors' actual test. Compatible examples below retain all three input rounding intervals and the printed P rounding interval, rather than inserting rounded centers independently.

| Relationship / printed triple | Compatible HR | Compatible lower | Compatible upper | Diagnostic two-sided P |
|---|---:|---:|---:|---:|
| S001: .76 (.50–1.14), .18 | .755025 | .502246867 | 1.135025 | .176686718 |
| S002: .95 (.57–1.57), .83 | .945025 | .570644080 | 1.565025 | .826109034 |
| S003: .75 (.48–1.17), .21 | .746525 | .475025209 | 1.173200 | .205007279 |
| S009: .44 (.21–.89), .02 | .435025 | .213832096 | .885025 | .021617030 |
| S017: .81 (.48–1.36), .42 | .805025 | .477888984 | 1.356100 | .415003729 |

For S016, HR permits [.655,.665), lower [.425,.435), upper [.985,.995), and printed P permits [.0475,.0485). Symmetry imposes HR²=lower×upper. Enforcing these constraints jointly gives the conservative diagnostic P range [.042744725,.047315922]. At the upper-P limiting combination HR=.655, upper=.995, lower=.431180905, SE=.213324074, z=1.983461294, diagnostic P=.047315922. At the lower-P limit HR=.655, lower=.435, upper=.986264368, P=.042744725. Closed endpoint bounds are conservatively allowed for this diagnostic, so half-open rounding conventions cannot increase the upper limit. Remaining interval gap is at least .0475−.047315922=.000184078; gap/.048=.003834955. Route A category 1 has no display-precision exemption once an interval-versus-test discrepancy is reproduced. The small relative gap is recorded transparently and is not the basis for exclusion. This is not a CI-null/significance disagreement: both printed CI and printed P indicate significance.

**Focus area:** B, estimate and test logic, with missing test-construction definition under C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 1. The reproducible joint estimate/interval/P discrepancy uses a calculation that reproduces all other complete same-page triples; absence of a named test construction is retained as the human question. No previously screened finding records this issue; it was only an excluded pass-1 observation.

**Affected result or extracted value:** The age-quartile-adjusted relapse-free-survival treatment comparison, specifically its .048 P value and the analysis mapping of that P to HR .66 and CI .43–.99.

**Why context does not resolve it:** Route A category 1 applies to the joint interval/test discrepancy. Adjacent consistent significance wording does not specify which test and CI construction produced the three printed values; it therefore does not identify their numerical mapping.

**Source-grounded alternatives and missing definitions:** A score or likelihood-ratio test may have generated P while a Wald interval generated the CI; another interval/test construction or separate test may have been used. The supplied text names Cox models and two-sided tests but gives no row-specific Wald/score/likelihood-ratio identification, CI construction, unrounded coefficient/SE, covariance/variance estimator, test statistic or degrees of freedom. None is inferred from Stata use or convention. This finding does not assert that the reported analysis necessarily used log-Wald inference, and does not assign a replacement value or challenge the stated Cox choice. The same-page reproducing examples establish the diagnostic basis required by the contract, rather than merely relying on a conventional approximation.

**Exact human question:** Which confidence-interval and two-sided test constructions, and which unrounded coefficient/standard error or test statistic, jointly produced the age-adjusted HR .66, CI .43–.99 and P=.048?

## Complete relationship-by-relationship pass-2 review

Every finite effect row was independently checked for endpoint order, estimate containment, null/significance agreement, randomized versus achieved-level contrast, reference direction, and narrative/test matching. Count and denominator implications, method/design context and current recheck facts were revisited for every row. No exact interaction covariance, interim output, imputation pooling variance or raw event times were inferred. Findings already in the screening log are cross-referenced without re-emission. All statements below are pass-2 checks, not adjudications.

| S ID | Pass-2 review fact | Pass 2 |
|---|---|---|
| S001 | Primary .76/.50–1.14/.18 reconciles across abstract/text/Fig2; no superiority claim; 251/166 population coherent; planned curve status remains C002. | PASS_2_COMPLETE |
| S002 | OS .95/.57–1.57/.83 reconciles across locations; death rather than relapse endpoint; no superiority claim; C002 supplies curve-method question. | PASS_2_COMPLETE |
| S003 | Relapse subdistribution .75/.48–1.17/.21 has ordered containing CI, nonsignificance and lower event direction; distinct from crude RR; C003/C006 retained. | PASS_2_COMPLETE |
| S004 | Low RFS 1.15/.65–2.05/.63 ordered, containing and nonsignificant; composite endpoint and available-baseline population retained. | PASS_2_COMPLETE |
| S005 | Middle RFS .46/.24–.86/.02 ordered, containing and significant; interaction .04 separately significant and exploratory; neither changes null overall result. | PASS_2_COMPLETE |
| S006 | Low OS 1.36/.66–2.81/.41 ordered, containing and nonsignificant; no effect-modification conclusion inferred. | PASS_2_COMPLETE |
| S007 | Middle OS .60/.28–1.30/.20 ordered, containing and nonsignificant; interaction .13 also nonsignificant; differs in endpoint from S005. | PASS_2_COMPLETE |
| S008 | Low relapse 1.18/.64–2.19/.59 agrees on nonsignificance and higher event direction; shared Table2 direction issue C006 retained. | PASS_2_COMPLETE |
| S009 | Middle relapse .44/.21–.89/.02 significant; interaction .04 separate; same-page rounded diagnostic compatible; C003/C006 retained. | PASS_2_COMPLETE |
| S010 | Total cancer-specific death 1.09/.58–2.01/.80 ordered/containing/nonsignificant; 27/16 cause-specific counts distinguish it from all-cause death; C006 retained. | PASS_2_COMPLETE |
| S011 | Low cancer-specific death 1.45/.63–3.38/.38 ordered/containing/nonsignificant; C006 direction question retained. | PASS_2_COMPLETE |
| S012 | Middle cancer-specific death .78/.29–2.10/.63 ordered/containing/nonsignificant; interaction .35 distinct and nonsignificant; C006 retained. | PASS_2_COMPLETE |
| S013 | Total noncancer death .70/.29–1.73/.44 ordered/containing/nonsignificant; 10/9 counts reconcile with primary-cancer complement; C006 retained. | PASS_2_COMPLETE |
| S014 | Low noncancer death 1.11/.26–4.65/.89 ordered/containing/nonsignificant; C006 retained. | PASS_2_COMPLETE |
| S015 | Middle noncancer death .39/.11–1.39/.15 ordered/containing/nonsignificant; interaction .27 distinct and nonsignificant; C006 retained. | PASS_2_COMPLETE |
| S016 | Printed .66/.43–.99/.048 has coherent nominal significance but joint symmetric-log-Wald bounds do not meet printed P; new F-ST2-001 retains unidentified construction. | PASS_2_COMPLETE |
| S017 | Adjacent age-adjusted OS .81/.48–1.36/.42 ordered/containing/nonsignificant and jointly log-Wald-compatible after rounding; does not resolve S016 test identity. | PASS_2_COMPLETE |
| S018 | Paired vitamin-D assay medians/IQR 21→41 and P<.001 support stated rise under signed-rank method; IQR is not an inferential CI. | PASS_2_COMPLETE |
| S019 | Paired placebo 21→20 and P=.91 support stated no significant change; rank statistic unavailable, no conflicting result supplied. | PASS_2_COMPLETE |
| S020 | 87% versus 0% patient change-ratio summaries and Mann–Whitney P<.001 are not ratios of printed group medians; no contradicted arithmetic identity. | PASS_2_COMPLETE |
| S021 | Vitamin-D calcium rounded median 9.3→9.3/P=.09 does not imply all paired changes zero; signed-rank structure appropriate to stated paired data. | PASS_2_COMPLETE |
| S022 | Placebo calcium 9.3→9.3/P=.44 likewise permits paired distributions with nonzero changes; no inferential interval supplied. | PASS_2_COMPLETE |
| S023 | Both calcium change-ratio medians 0% with between-arm P=.10 can coexist; summaries do not identify full rank distributions. | PASS_2_COMPLETE |
| S024 | Achieved-mean RFS 20–<30 HR .62/.37–1.02/.06 ordered/containing/nonsignificant; not randomized subgroup contrast. | PASS_2_COMPLETE |
| S025 | Corresponding AHR .61/.37–1.01/.05 contains null; .05 does not satisfy stated P<.05 rule; no interval/test threshold conflict. | PASS_2_COMPLETE |
| S026 | Achieved-mean death 20–<30 HR .66/.35–1.24/.20 ordered/containing/nonsignificant; correct reference <20. | PASS_2_COMPLETE |
| S027 | Death AHR .64/.34–1.20/.16 ordered/containing/nonsignificant; treatment-adjustment label preserved. | PASS_2_COMPLETE |
| S028 | RFS 30–<40 HR .47/.27–.84/.01 ordered/containing/significant, lower event hazard. | PASS_2_COMPLETE |
| S029 | RFS AHR .44/.24–.82/.009 ordered/containing/significant; added treatment covariate does not imply crude-risk identity. | PASS_2_COMPLETE |
| S030 | Death HR .39/.18–.84/.02 ordered/containing/significant; eFig1B same matched contrast and estimate. | PASS_2_COMPLETE |
| S031 | Death AHR .33/.15–.74/.007 ordered/containing/significant; separate adjusted result preserved. | PASS_2_COMPLETE |
| S032 | RFS 40–<50 HR .29/.11–.74/.01 ordered/containing/significant; eFig1A matched duplicate reconciles. | PASS_2_COMPLETE |
| S033 | RFS AHR .26/.10–.71/.008 ordered/containing/significant; zero placebo patients in achieved group does not establish impossible treatment-adjusted model. | PASS_2_COMPLETE |
| S034 | Death HR .44/.17–1.16/.10 ordered/containing/nonsignificant; no inference of association from RFS result. | PASS_2_COMPLETE |
| S035 | Death AHR .34/.12–.96/.04 ordered/containing/significant; adjustment can change estimate/test without a conflict. | PASS_2_COMPLETE |
| S036 | RFS ≥50 HR .44/.21–.96/.04 ordered/containing/significant; actual achieved group rather than baseline high group. | PASS_2_COMPLETE |
| S037 | RFS AHR .40/.18–.92/.03 ordered/containing/significant; not an unreported baseline-high counterpart for C004. | PASS_2_COMPLETE |
| S038 | Death HR .55/.24–1.29/.17 ordered/containing/nonsignificant; matched population retained. | PASS_2_COMPLETE |
| S039 | Death AHR .43/.17–1.08/.07 ordered/containing/nonsignificant; no null/threshold conflict. | PASS_2_COMPLETE |
| S040 | Imputed low RFS 1.15/.65–2.05/.63 internally coherent; printed equality with available-case output does not demonstrate absent imputation. | PASS_2_COMPLETE |
| S041 | Imputed middle RFS .46/.24–.86/.02 coherent significance; imputed versus available-case output identity alone not a discrepancy. | PASS_2_COMPLETE |
| S042 | Imputed low OS 1.36/.66–2.81/.41 internally coherent; no pooling output supplied for further reproduction. | PASS_2_COMPLETE |
| S043 | Imputed middle OS .60/.28–1.30/.20 internally coherent; missing post-imputation subgroup counts alone not a contradicted analysis. | PASS_2_COMPLETE |
| S044 | FokI CC .65/.34–1.26/.20 ordered/containing/nonsignificant; interaction .65 independently nonsignificant; genotype denominator implications C005 cross-linked. | PASS_2_COMPLETE |
| S045 | FokI CT .77/.42–1.43/.41 and interaction .90 nonsignificant; within-effect and interaction tests not conflated. | PASS_2_COMPLETE |
| S046 | FokI TT .97/.32–2.88/.95 and interaction .67 nonsignificant; lower rounded event-hazard direction does not assert benefit. | PASS_2_COMPLETE |
| S047 | BsmI AA .44/.03–7.16/.56 and interaction .66 nonsignificant; broad interval contains estimate and null; C005 population link retained. | PASS_2_COMPLETE |
| S048 | BsmI AG .60/.24–1.48/.27 and interaction .50 nonsignificant; no implied treatment modification. | PASS_2_COMPLETE |
| S049 | BsmI GG .86/.52–1.41/.55 and interaction .38 nonsignificant; count/header/percentage issue remains C005. | PASS_2_COMPLETE |
| S050 | CDX2 GG .69/.34–1.38/.29 and interaction .64 nonsignificant; CDK2 label resolved through matched supplied group, no altered numeric assignment. | PASS_2_COMPLETE |
| S051 | CDX2 GA .72/.39–1.32/.28 and interaction .63 nonsignificant; reference/group matching retained. | PASS_2_COMPLETE |
| S052 | CDX2 AA 1.82/.48–6.88/.38 and interaction .19 nonsignificant; estimate above null agrees event-hazard direction. | PASS_2_COMPLETE |
| S053 | ApaI GG 1.00/.49–2.05/.99 and interaction .35 nonsignificant; rounded estimate 1 need not force P exactly 1. | PASS_2_COMPLETE |
| S054 | ApaI GT .70/.38–1.27/.24 and interaction .63 nonsignificant; no contradiction from crossing curves alone. | PASS_2_COMPLETE |
| S055 | ApaI TT .53/.15–1.84/.32 and interaction .49 nonsignificant; interval ordered and containing. | PASS_2_COMPLETE |
| S056 | TaqI TT .87/.52–1.46/.60 and interaction .35 nonsignificant; missing genotype denominators C005 do not redefine fitted effect. | PASS_2_COMPLETE |
| S057 | TaqI TC .49/.22–1.10/.08 and interaction .20 nonsignificant; near-null upper interval does not establish benefit. | PASS_2_COMPLETE |
| S058 | TaqI CC dashes/P1.00, five/four initial risk sets and sparse event curve supply no finite coefficient or test construction; absence alone not a reproduced omitted analysis. | PASS_2_COMPLETE |
| S059 | DBP1 TT .71/.42–1.22/.22 and interaction .63 nonsignificant; same subgroup identity retained. | PASS_2_COMPLETE |
| S060 | DBP1 TG 1.00/.44–2.24/.99 and interaction .49 nonsignificant; 57/59 cross-location count remains within precision; C005 separate header relation retained. | PASS_2_COMPLETE |
| S061 | DBP1 GG .65/.14–2.92/.57 and interaction .91 nonsignificant; no exact interaction reconstruction without covariance. | PASS_2_COMPLETE |
| S062 | DBP2 CC .60/.34–1.05/.07 and interaction .16 nonsignificant; endpoint order/containment coherent. | PASS_2_COMPLETE |
| S063 | DBP2 CA 1.19/.55–2.60/.66 and interaction .16 nonsignificant; higher estimate direction retained without a significant conclusion. | PASS_2_COMPLETE |
| S064 | DBP2 AA .80/.20–3.20/.75 and interaction 1 nonsignificant; rounded interaction 1 within permitted range. | PASS_2_COMPLETE |
| S065 | Men .59/.37–.97/.04 significant within-subgroup effect, interaction .13 nonsignificant; nominal P difference from rounded-center diagnostic is not a reproduced joint conflict. | PASS_2_COMPLETE |
| S066 | Women 1.18/.56–2.51/.66 and interaction .13 nonsignificant; complements men without requiring identical subgroup effects. | PASS_2_COMPLETE |
| S067 | Age ≤65 .86/.44–1.68/.65 and interaction .48 nonsignificant; post hoc status correctly supplied. | PASS_2_COMPLETE |
| S068 | Age >65 .63/.37–1.05/.07 and interaction .48 nonsignificant; allowing joint HR/CI rounding permits diagnostic P in printed range. | PASS_2_COMPLETE |
| S069 | BMI<25 .75/.49–1.16/.20 and interaction .87 nonsignificant; no participant-level denominator inferred. | PASS_2_COMPLETE |
| S070 | BMI≥25 .88/.22–3.55/.86 and interaction .87 nonsignificant; same complementary interaction test retained. | PASS_2_COMPLETE |
| S071 | Esophageal 1.01/.42–2.44/.99 and interaction .65 nonsignificant; category-specific/omnibus construction not supplied. | PASS_2_COMPLETE |
| S072 | Gastric .84/.40–1.76/.64 and interaction .88 nonsignificant; no claim establishes identical contrast to other site panels. | PASS_2_COMPLETE |
| S073 | Colorectal .69/.39–1.24/.22 and interaction .66 nonsignificant; source narrative no-interaction remains coherent. | PASS_2_COMPLETE |
| S074 | StageI .39/.14–1.13/.08 and interaction .14 nonsignificant; adjusted-stage model separately tracked, not inferred from this subgroup. | PASS_2_COMPLETE |
| S075 | StageII 1.20/.51–2.80/.68 and interaction .23 nonsignificant; differing stage interaction P alone not identical-test contradiction. | PASS_2_COMPLETE |
| S076 | StageIII .86/.51–1.46/.58 and interaction .62 nonsignificant; no omnibus coding inferred. | PASS_2_COMPLETE |
| S077 | Adenocarcinoma .70/.43–1.13/.14 and interaction .47 nonsignificant; no inferential conflict from other histology sample size. | PASS_2_COMPLETE |
| S078 | Nonadenocarcinoma 1.18/.54–2.60/.68 and interaction .47 nonsignificant; complementary contrast source matched. | PASS_2_COMPLETE |
| S079 | Individual blocks5/3:2/non-stratified randomization and final251/166 compatible with incomplete blocks; no stated cluster/stratum adjustment omitted. | PASS_2_COMPLETE |
| S080 | ITT417=251+166 efficacy population matches plan/report; cessation does not remove randomized patients; per-protocol safety populations expressly separate. | PASS_2_COMPLETE |
| S081 | Primary earliest relapse/any-cause death definition and start time align; 50/43 event composite not confused with deaths or crude five-year risk. | PASS_2_COMPLETE |
| S082 | OS time to any-cause death 37/25 distinct from cancer-specific 27/16; five-year82/81 and HR.95 different quantities, not arithmetic alternatives. | PASS_2_COMPLETE |
| S083 | Planned relapse RR versus reported post hoc subdistribution HR remains C003; coherent competing-risk model not challenged, no crude-HR equality assumed. | PASS_2_COMPLETE |
| S084 | Progressive-primary-cancer definition and counts27/16 align; 27+10=37 and16+9=25; no reassignment inferred for de novo cases. | PASS_2_COMPLETE |
| S085 | Non-primary-cancer death category including de novo examples does not demonstrate altered printed count; terminology resolves through explicit primary-cancer contrast. | PASS_2_COMPLETE |
| S086 | Safety227/147,243/160,251/166 populations are labeled separate; all printed counts/% reconcile within precision; planned RR C003 and de novo hierarchy C001 retained separately. | PASS_2_COMPLETE |
| S087 | Freedman expression using h=ln(.75)/ln(.62), .4/.6 allocation, .05two-sided/.80power/.01withdrawal yields E119.469 and N399.589→400, matching finalplan/report; no preferred formula substituted. | PASS_2_COMPLETE |
| S088 | 80/year×5=400 and2additionalyears are planning assumptions; actual417 and calendar do not contradict arithmetic sample-size rule or show stopping-threshold conflict. | PASS_2_COMPLETE |
| S089 | Annual after200/Peto<.001 and report three nonstopping interims align; no numerical interim test permits contradictory decision reproduction. | PASS_2_COMPLETE |
| S090 | Primary P.18/null-containing CI supports stated lack of significant improvement; no noninferiority/equivalence margin or claim supplied; exploratory subgroup does not reverse overall conclusion. | PASS_2_COMPLETE |
| S091 | Explicit uncorrected multiplicity plus exploratory reporting aligns; interaction.04 and men's within P.04 kept distinct; no preferred multiplicity method proposed. | PASS_2_COMPLETE |
| S092 | Final amended thresholds <20/20–40/>40 align; 173+232+5+7=417; supplied2012 prospective amendment explains prespecified status, while high-analysis omission remains C004. | PASS_2_COMPLETE |
| S093 | Five VDR/twoDBP loci finalplan and all21 panels matched; amendedDBP date is paragraph-specific2012.12.8; no separate date finding; C005 population question retained. | PASS_2_COMPLETE |
| S094 | Seven baseline missing/50normalMCMC imputations/named predictors source matched; identical printed results alone not a logical contradiction; missing pooling inputs named. | PASS_2_COMPLETE |
| S095 | Schoenfeld/stage-adjusted claims have no conflicting supplied numbers; age-adjusted S016 newly flagged independently; analyses expressly post hoc, not called prespecified. | PASS_2_COMPLETE |
| S096 | Signed-rank paired baseline/year1 and independent-arm Mann–Whitney change-ratio tests align stated data structure; no unsupported annual independence assumption introduced. | PASS_2_COMPLETE |
| S097 | Achieved-mean patient groups114+123+94+39+43=413=248+165, distinct from baseline410; AHR treatment covariate and referenceHR1 align labels, no causal-model preference applied. | PASS_2_COMPLETE |
| S098 | Planned KM versus reported Nelson–Aalen primary/key-secondary curves reproduced by exact recheck C002; survival-percentage estimator remains unspecified; no duplicate finding emitted. | PASS_2_COMPLETE |
| S099 | Final tertiary/adverse-event/safety status comparison remains C001; de novo amendment2012.12.8 corrected at registration, version/subgroup2012.12.18 distinct; P_R precedence overP_P retained. | PASS_2_COMPLETE |
| S100 | Shared Table2 HR>1/decreased direction conflicts with matched .44/lower narrative; allnine estimate directions and recheck retained under C006, not re-emitted. | PASS_2_COMPLETE |
| S101 | Full first-relapse-or-death definition resolves follow-up “or alive” shorthand; no changed event count/censoring rule observed; supplement cessation not automatic efficacy censoring. | PASS_2_COMPLETE |
| S102 | Historical1200 versus capsule1000 wording separated from documented pretrial amendment/final2000 actual regimen; no relied-on final statistical-design conflict supplied. | PASS_2_COMPLETE |
| S103 | StageI–III/individual unit/age30–90 source matched; blank-form <90 notation alone does not demonstrate changed417 analysis population or decision rule. | PASS_2_COMPLETE |
| S104 | Table1 explicit251/166 headers and22 genotype cells remain RouteA3 C005; availability-sum alternatives reconcile percentages but do not supply a printed denominator instruction; baseline-P omission separately peripheral. | PASS_2_COMPLETE |
| S105 | Duplicate assay n19/correlation.92 within bounds; no supplied interval/P/calibration statistic conflict; annual schedule coherent. | PASS_2_COMPLETE |
| S106 | Planned high>40 primary/key-secondary subgroup explicitly omitted for n5; no supplied minimum-size condition; C004 retained with disclosed small-n rationale, not re-emitted. | PASS_2_COMPLETE |

## Registered-candidate and recheck reconciliation

C001 retains P_R plus P_P, protocol_report, reproduced_after_transcription_correction, with paragraph-specific de novo date2012.12.8 and subgroup/version date2012.12.18. C002, C003 and C004 retain P_R/protocol_report/reproduced; their curve-method, RR-status and high-subgroup questions are independent. C005 and C006 retain S_W/statistical_results/reproduced: one22-cell denominator pattern and one9-estimate direction pattern. All six remain Pending Human Adjudication. No existing finding is re-emitted; no evidence-state or relationship/domain correction is proposed. Inclusion audit remains for the different fresh auditor. F-ST2-001 is not appended to the ledger by this agent and requires the separate fresh pass-2 inclusion screen.

## Audit of every initial checker excluded-observation row

NUM/XS/ST row labels below are audit locators by original table order, not finding IDs. The current union preserves each original row; this table records each independent revisit, including duplicate appearances. RouteA1 numerical-test conflicts were assessed without the .05 relative-gap exemption; other printed numeric comparisons used half-unit intervals. Only ST01 advances to the new finding. The other38 rows remain excluded; their distinct apparent observations are consolidated once in the following Excluded observations table.

| Original row | Exact original location / comparison | Independent route/precision revisit | Pass-2 outcome |
|---|---|---|---|
| NUM01 | Mainp4 pooledstageII111/417 versus26% | Recomputed[26.467,26.771]% overlaps[25.5,26.5]%; no reproduced A3 gap. | Retain ROUNDING_OR_DISPLAY_PRECISION |
| NUM02 | Mainp5 middle-baseline142/248 versus58% | [56.9416,57.5758]% overlaps[57.5,58.5]%; no A3 gap. | Retain ROUNDING_OR_DISPLAY_PRECISION |
| NUM03 | Mainp5 DBP1TG57 versus suppp23 risk59 | Half-unit gap1/reference57=.01754≤.05; distinct from C005 within-display headers. | Retain ROUNDING_OR_DISPLAY_PRECISION |
| NUM04 | Mainp5 BMI/baseline/FokI percentages versus251/166 | Cell gaps overlap or remain≤.05; above-threshold otherloci already C005, not hidden by availability assumptions. | Retain ROUNDING_OR_DISPLAY_PRECISION |
| NUM05 | Mainpp1/4 event counts versus5year77/69,82/81 | Crude full-followup counts versus censored5year estimates have different specified quantities; no asserted equality. | Retain MODEL_VERSUS_CRUDE |
| NUM06 | Mainp6 group21→41 medians versus87% change | Patient ratio summary distinct from ratio of medians; no conflicting printed identity. | Retain CONDITIONAL_OR_UNREPORTED |
| NUM07 | Supppp2–4 achievedmean413 versus mainbaseline410 | Distinct availability/time summaries; no matched-population count conflict. | Retain CONTEXT_RESOLVES |
| NUM08 | Mainp7 caption versus panelC risk rows | Pointer discrepancy does not supply an alternative printed population count or affect HR/CI/P. | Retain PERIPHERAL_COMPARISON |
| NUM09 | Initialplanpp9/12 versus finalpp25/28/45 dose | Disclosed pretrial amendment fixes actual2000; earlier unimplemented detail not a relied-on final design conflict. | Retain PERIPHERAL_COMPARISON |
| XS01 | Planpp9/12/25/28/45 dose | Same historical-dose observation; no current intervention conflict after explicit amendment. | Retain CONTEXT_RESOLVES |
| XS02 | Planp23 versusp31 high threshold comparator | FullSAP>40 and other categories identify intended comparator; no changed printed value/patient group. | Retain NOTATION_OR_TYPOGRAPHY |
| XS03 | Planpp9/24/38 versus mainp2 eligibility | Formagebound/checkbox differences show no changed417 population or decision rule. | Retain PERIPHERAL_COMPARISON |
| XS04 | Planpp9/24 versus mainp2 carcinoma wording | Same sites/exclusions resolve intended eligible condition; no reported quantity misattributed. | Retain TERMINOLOGY_OR_WORDING |
| XS05 | Planpp13/29 versus9/25 followup | Full first-relapse-or-death primary definition resolves shorthand, not a changed composite status or result. | Retain TERMINOLOGY_OR_WORDING |
| XS06 | Planpp10/25/41 versus mainpp2/7 noncancer | Primary versus non-primary distinction resolves category terminology; no observed count reassignment. | Retain TERMINOLOGY_OR_WORDING |
| XS07 | Planpp12/27/mainp3/supppp13–15 locus labels | Matched loci/genotypes/groups identify subgroup; no changed numerical outcome mapping. | Retain TERMINOLOGY_OR_WORDING |
| XS08 | Planpp17/45 version numbering | Number alone changes no statistical rule; actual supplied version identified through text/dates. | Retain PERIPHERAL_COMPARISON |
| XS09 | Planp45 versus17/18 dates | Recheck establishes paragraph-specific8 versus18; administrative date difference alone not A5 analysis conflict. | Retain PERIPHERAL_COMPARISON |
| XS10 | Planpp3/14/18/30/45 initial blank sample inputs | Complete final inputs/report400 supplied and reproduce; old blank fields do not contradict relied-on calculation. | Retain CONTEXT_RESOLVES |
| XS11 | Planpp30–31 versus mainpp3–4 calendars | Planned accrual versus observed chronology separately identified; no stopping-threshold contradiction. | Retain CONTEXT_RESOLVES |
| XS12 | Planp31 versus mainp3/eTable2 additional analyses | MI/PH/age/stage expressly post hoc; absentSAP detail not an unsupported prespecification claim. | Retain CONDITIONAL_OR_UNREPORTED |
| XS13 | Mainp7 panelC caption/risk rows | Same peripheral pointer observation; source supplies visible risk rows, no alternative values. | Retain PERIPHERAL_COMPARISON |
| XS14 | Mainp5 DBP1TG57 versus suppp23risk59 | Same half-unit1/57=.01754 precision result; no new count finding. | Retain ROUNDING_OR_DISPLAY_PRECISION |
| XS15 | Mainabstractp1 mean66 versus narrativep4 median66 | Explicitly different summaries; no matched-copy numeric conflict reproduced. | Retain NOT_REPRODUCED |
| XS16 | Suppp6MI versus mainp7available results | Numerical equality is possible; missing pooling inputs do not contradict claim. | Retain CONDITIONAL_OR_UNREPORTED |
| ST01 | Mainp6 S016 adjustedRFS interval/P | Joint Wald maximum.047315922 below printed.0475; five other complete same-page triples reproducible; missing test construction retained, not used to suppress A1. | Emit F-ST2-001 |
| ST02 | Mainpp4/6 S020 medians/change ratios | Summary-of-ratios distinct from ratio-of-summaries; no claimed identity. | Retain CONTEXT_RESOLVES |
| ST03 | Mainpp3–4/6/suppp6 MI repeated output | No individual/pooling result establishes a conflicting printed analysis. | Retain CONDITIONAL_OR_UNREPORTED |
| ST04 | Mainpp3/5 S095 PH tests | No numerical source result contradicts nonsignificance statement; missing output alone not A1. | Retain CONDITIONAL_OR_UNREPORTED |
| ST05 | Mainp6 S095 stage adjustment | No printed adjusted estimate/CI/test permits a contradicting calculation. | Retain CONDITIONAL_OR_UNREPORTED |
| ST06 | Mainpp3–4 S089 interim | Three nonstopping analyses, no interim statistic/P; no contradicted stated decision. | Retain CONDITIONAL_OR_UNREPORTED |
| ST07 | Suppp21 S058 TaqICC dashes/P1 | Sparse panel/test construction undefined; no finite estimate/CI to conflict and no demonstrated unavailable named subgroup analysis. | Retain CONDITIONAL_OR_UNREPORTED |
| ST08 | Supppp34–39 S071–S076 interaction Ps | Source does not identify identical tests; category contrasts possible; no numerical covariance-based conflict reproduced. | Retain CONDITIONAL_OR_UNREPORTED |
| ST09 | Planpp9/13/25/29 S101 followup wording | Explicit full primary endpoint resolves wording, without changed numeric or hierarchical definition. | Retain TERMINOLOGY_OR_WORDING |
| ST10 | Initialplanpp8–9/12/final25/45 S102dose | Historical statement not relied-on final2000 regimen; amendment gives actual design. | Retain CONTEXT_RESOLVES |
| ST11 | Planpp14/31 versus mainp5 baseline tests | Descriptive-test omission peripheral; no primary/key-secondary result or analysis-population change. | Retain PERIPHERAL_COMPARISON |
| ST12 | Supppp13–15 versus main/planCDX2 labels | Matching genotypes identify same panel; no altered effect value attributed. | Retain TERMINOLOGY_OR_WORDING |
| ST13 | Mainp7 caption versus risk rows | Same peripheral caption pointer; no result/count conflict supplied. | Retain PERIPHERAL_COMPARISON |
| ST14 | Mainp5 versus suppp23 DBP1TG57/59 | Same gap1/57≤.05; pooled148/150 also below threshold; C005 independently retained. | Retain ROUNDING_OR_DISPLAY_PRECISION |

## Excluded observations

Twenty-eight distinct apparent observations, each listed once with one reason code. Cross-checker repeated occurrences are consolidated here while the39-row audit above preserves every original decision. F-ST2-001 is not in this table. Reconciled routine checks are in S records, not classified as exclusions. For duplicates with differing initial codes, this independent pass retains the single most direct scope code below without altering historical checker records.

| Location | Observation | Reason code |
|---|---|---|
| Mainp4/p5 stageII |111/417 versus26% has overlapping half-unit intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| Mainp5 middle baseline vitaminD |142/248 versus58% has overlapping half-unit intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| Mainp5/suppp23 DBP1TG |57 versus59 has relative interval gap.01754; pooled148 versus150 similarly≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| Mainp5 BMI/baseline/FokI headers |Apparent percentage/header gaps overlap or≤.05; qualifying other-locus cells already in C005. | ROUNDING_OR_DISPLAY_PRECISION |
| Mainpp1/4 events versus5year survival |Whole-followup crude ratios not the censored5year quantities. | MODEL_VERSUS_CRUDE |
| Mainpp4/6 assay medians versus87% |Printed individual change-ratio distribution is distinct from ratio of group medians. | CONTEXT_RESOLVES |
| Supppp2–4 versus mainpp4–6 population |Achieved-mean413 and baseline410 have different stated availability definitions. | CONTEXT_RESOLVES |
| Mainp7 Fig3C caption/risk rows |Caption pointer does not change result or printed starting population; full rows visible. | PERIPHERAL_COMPARISON |
| Initialplanpp8–9/12/finalpp25/28/45 dose |Older1200/capsule1000 statement separated from documented pretrial2000 final regimen. | CONTEXT_RESOLVES |
| Planp23/p31 high comparator |Complete subgroup definition supplies>40; missing comparator does not change a printed patient/result value. | NOTATION_OR_TYPOGRAPHY |
| Planpp9/24/38/mainp2 eligibility |Formboundary/checkbox differences show no changed analysis population or decision rule. | PERIPHERAL_COMPARISON |
| Planpp9/24/mainp2 carcinoma labels |Same sites/exclusion examples identify intended condition. | TERMINOLOGY_OR_WORDING |
| Planpp9/13/25/29 followup |Full primary first-relapse-or-death definition resolves “or alive” shorthand. | TERMINOLOGY_OR_WORDING |
| Planpp10/25/41/mainpp2/7 noncancer |Explicit primary/non-primary distinction resolves label; no count reassignment supplied. | TERMINOLOGY_OR_WORDING |
| Planpp12/27/mainp3/supppp13–15 loci |Matched supplied locus/genotype groups resolve FokI/CDX2 naming differences without numeric reassignment. | TERMINOLOGY_OR_WORDING |
| Planpp17/45 version numbering |Version number alone does not alter relied-on statistical rule. | PERIPHERAL_COMPARISON |
| Planpp17/18/45 dates |Paragraph-specific2012.12.8 versus2012.12.18 is administrative chronology alone. | PERIPHERAL_COMPARISON |
| Planpp3/14/18/30/45 initial blank sampleSAP |Final complete calculation/report400 supplies relied-on design; initial blanks alone not conflict. | CONTEXT_RESOLVES |
| Planpp30–31/mainpp3–4 calendar |Planning assumptions versus observed accrual/followup explicitly distinguished. | CONTEXT_RESOLVES |
| Planp31/mainpp3–4 additional analyses |MI/age/stage/PH explicitly post hoc; absence from plan not a prespecification contradiction. | CONDITIONAL_OR_UNREPORTED |
| Mainabstractp1/narrativep4 age |Mean66 and median66 not copies of the same statistic. | NOT_REPRODUCED |
| Mainpp3–4/6/suppp6 MI result identity |Printed equality alone does not establish conflicting imputed or pooled output. | CONDITIONAL_OR_UNREPORTED |
| Mainpp3/5 PH claims |Nonsignificant Schoenfeld tests lack numerical output and no contradictory value supplied. | CONDITIONAL_OR_UNREPORTED |
| Mainp6 stage adjustment |No adjusted estimate/interval/statistic supplied to contradict reported nonsignificance. | CONDITIONAL_OR_UNREPORTED |
| Mainpp3–4 interim decisions |No interim P/statistic supplied to contradict nonstopping statement. | CONDITIONAL_OR_UNREPORTED |
| Suppp21 TaqICC |No finite HR/CI/test construction supplied for dashes/P1.00; sparse curve alone cannot reproduce a conflict. | CONDITIONAL_OR_UNREPORTED |
| Supppp34–39 site/stage interactions |No supplied statement identifies all category tests as one omnibus contrast. | CONDITIONAL_OR_UNREPORTED |
| Planpp14/31/mainp5 baseline hypothesis tests |Unreported descriptive comparison tests do not change primary/key-secondary result, analysis population or decision rule. | PERIPHERAL_COMPARISON |

## Limits and completion

Complete coverage:106 relationships =78 result records plus28 statistical-design/method records; all35 genotype/demographic panel records retain both within-subgroup and interaction tests, including the dash panel. The six stable IDs were revisited without deletion, renumbering, disposition or duplicate findings. New finding count1; original exclusion rows audited39, advanced1 and retained38; consolidated pass-2 excluded-observation count28. Mechanical reproduction limits remain individual event times, row-specific test/CI construction, interaction contrasts/covariance, imputation pooling variances and updated populations, numerical PH tests, stage-adjusted estimates and interim outputs. These are named definition/data limits, not coverage gaps. No inferential content supplied by references, blank forms, administrative pages or sharing statement was omitted. Pass2 is complete; the new finding requires independent fresh inclusion screening and, if included, stable-ID assignment and exact-source recheck by the coordinator's next agents.
