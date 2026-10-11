# Statistical relationship inventory — pass 1

Runtime agent: `/root/statistical_pass_1`; fresh `qc161_statistical_consistency_reviewer`, `gpt-6.1-sol`, reasoning `high`. Exact scope is the disjoint union of the three current evidence maps across six supplied PDFs, 100/100 mapped physical pages. This inventory contains 111 stable grouped relationships. A group retains every component row/time point/model in its full vector; grouping does not sample nonsignificant or exploratory outputs.

Read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md. No old candidate/report scientific conclusions or external sources were used. REPORT: DOC-001 main, DOC-005 results supplement, DOC-006 administrative data sharing. PLAN: DOC-002 protocol, DOC-003 approved changes, DOC-004 SAP. DOC-006 and administrative/reference pages have no inferential result. Source definitions, not source filenames, set roles.

Shared vector key: H=higher PEEP12cmH2O+recruitment; L=lower PEEP4cmH2O without routine recruitment. Main and non-PP supplement analysis989/987; PP917/912. Main Table2 vectorHsummary;Lsummary;H−Labsolute difference95%CI;P. Table3 vectorHevents%;Levents%;difference95%CI percentage points;printedRR95%CI;P. Exceptions: hospital-free days mean difference/t-test, five-day mortality HR/Cox. All source-supplied sidedness is two-sided; primary finalalpha.044, secondarynominal.05, exploratory componentsBonferroni99.58%CI. No noninferiority/equivalence margin or claim is supplied. No numeric standard error or test statistic is reported. Unprinted item is unreported, never zero.

Every S record below has PASS_1_COMPLETE; pass 2 is PASS_2_COMPLETE for all 111 records under distinct fresh runtime agent `/root/statistical_pass_2`. All direct comparisons apply half-unit precision. Normal approximations and graph coordinates are diagnostic only. Final candidate confirmation uses supplied PDFs; direct streamed Poppler extraction and source-matched rendered images were used to confirm pass-1 finding locations.

### S001

- **Semantic key:** Statistical Analysis p.3 original power; map key MAIN033.
- **Locations and roles:** REPORT DOC-001 [source page 3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Control40%,dropout 5%,RR.75,power 80%,two-sidedα.05,total 748;target primary 5-day PPC
- **Analysis keys / checks / missing definitions:** Diagnostic fixed-design normal approximation gives 355.943 per arm, reproducing the stated 356. Multiplying 712 by 1.05 gives 747.6, consistent with the printed 748 total under an additive allowance arithmetic interpretation; the source does not specify that algorithm; the protocol also discloses the later replacement. No sample-size observation survives context.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Original 40%/30%, RR .75, .05/80% power inputs: diagnostic 355.943 per arm and additive allowance reproduce 748; no unique dropout convention is imposed.

### S002

- **Semantic key:** Statistical Analysis p.4 revised power; map key MAIN034.
- **Locations and roles:** REPORT DOC-001 [source page 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Blinded review of 618 patients;pooled PPC≈20%;control assumed 20%,dropout 5%,RR.75,power 80%,two-sidedα.05,total 2013;nonbinding interim at 50/75/100%for efficacy/harm/futility;committee recommended continuation
- **Analysis keys / checks / missing definitions:** Revised design includes group-sequential efficacy/futility spending; a fixed-design diagnostic is 905.366 per arm and is not a replacement for East 6.0. 1912/.95=2012.632, rounded up to 2013. Actual interim vectors are unreported; no observed stopping statistic is inferred. Final continuation and primary P=.23 are consistent with the final nonbinding rule.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Revised 20%/15% sequential design and 618-person blinded review retained; 1912/.95 rounds to 2013. Actual interim statistics absent; no stopping decision manufactured.

### S003

- **Semantic key:** p.4 primary decision rule; map key MAIN035.
- **Locations and roles:** REPORT DOC-001 [source page 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Two-sided primaryα.044 accounts for interims;other testsα.05;generic hypothesis tests were two-sided;secondary unadjusted for multiple comparisons/exploratory
- **Analysis keys / checks / missing definitions:** Primary P=.23 exceeds .044; exploratory secondary alpha=.05 and explicit absence of multiplicity adjustment are coherent. The component Bonferroni figure is a separately prespecified sensitivity family, not a contradiction.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Primary .23>.044 supports no detected superiority; secondary nominal .05 and component Bonferroni family are distinct disclosed rules. No NI/equivalence margin or claim supplied.

### S004

- **Semantic key:** p.4 analysis populations/missingness; map key MAIN036.
- **Locations and roles:** REPORT DOC-001 [source page 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** ITT by randomization among eligible surgery/general anesthesia;primary no missing data stated;complete cases for all outcomes;consent withdrawal data censored at withdrawal;PP exclusion as MAIN024
- **Analysis keys / checks / missing definitions:** Matched flow 2013−29−8=1976; analyzed 989+987; PP917+912=1829. Eight postoperative losses and complete cases are disclosed. 'No missing data' is read in the analyzed complete-case set, not as an assertion of follow-up for all randomized people. SAP exclusion/missingness specifications are retained in S087.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Flow 2013−29−8=1976=989+987; PP 917+912=1829. Complete-case and withdrawal descriptions explain analyzed-set missingness; no alternate denominator inferred.

### S005

- **Semantic key:** p.4 primary binary model; map key MAIN037.
- **Locations and roles:** REPORT DOC-001 [source page 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Counts/percentages;RR95%CI Wald likelihood ratio approximation;chi-square hypothesis test;effect H relative toL labeled by results
- **Analysis keys / checks / missing definitions:** The source names incidence RR, 95% Wald-style interval and chi-square testing, without supplying a covariate-adjusted primary model. Effect identity is reviewed in F-ST1-001; a specific orientation is diagnostic rather than asserted as the authors' computation.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Primary incidence RR/95% interval/chi-square labels revisited with C001 recheck. Unspecified estimator and orientation remain the existing identity issue.

### S006

- **Semantic key:** p.4 primary time-to-event; map key MAIN038.
- **Locations and roles:** REPORT DOC-001 [source page 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Kaplan–Meier time toPPC;HR95%CI Cox;Schoenfeld residuals vs transformed time forPH assumption
- **Analysis keys / checks / missing definitions:** Cox HR, Kaplan–Meier occurrence proportions and binomial RR are separate estimands; S106 preserves the full primary HR vector. Source supplies no numeric test statistic, standard error, covariance or event times for independent Cox reconstruction.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Cox HR/95% CI, Kaplan–Meier and PH assessment are distinct from incidence RR; event times and variance unavailable for independent reconstruction.

### S007

- **Semantic key:** p.4 primary sensitivity; map key MAIN039.
- **Locations and roles:** REPORT DOC-001 [source page 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Generalized linear mixed effects with study-site random effect;additional composite-outcome sensitivities;results pp.10–11 unchanged by adjustment/similar assumptions;Supplement4eTable9/eFigure12 pointers
- **Analysis keys / checks / missing definitions:** Mixed site-random effect and composite sensitivity methods map to S098/S110; all are kept distinct from the main reported RR and from PP. The report describes agreement of conclusions rather than equality of coefficients.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Site-random-effect and composite sensitivities map to S098/S110 on their own scales; unchanged conclusions do not require equal coefficients.

### S008

- **Semantic key:** p.4 other binary results; map key MAIN040.
- **Locations and roles:** REPORT DOC-001 [source page 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** RR95%CI Wald likelihood ratio approximation andchi-square hypothesis test;Table 3 notes corroborate
- **Analysis keys / checks / missing definitions:** All binary secondary/post hoc rows below are checked for containment/order/direction and named-measure identity; Wald-style intervals and chi-square P are distinct procedures. No unreported variance or continuity option is assumed.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All other binary estimates retain source interval/test distinction and explicit exceptions; shared identity issue remains C001, with no assumed chi-square option.

### S009

- **Semantic key:** p.4 hospital-free days; map key MAIN041.
- **Locations and roles:** REPORT DOC-001 [source page 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** day90;t-test;mean difference;Table3footnoteh;MAIN098 result
- **Analysis keys / checks / missing definitions:** Reported mean difference−.77 has ordered95%CI−2.16,.61 and t-testP=.27. Diagnostic SE≈.707 and |t|≈1.09 gives P≈.28; printed vector reconciles under precision. SAP supplementary zero-inflated beta model is not supplied as a numeric result.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Hospital-free-day mean difference −.77, CI −2.16,.61 and t-test .27 reconcile within summary precision; diagnostic SE approximately .707 only.

### S010

- **Semantic key:** p.4 five-day mortality; map key MAIN042.
- **Locations and roles:** REPORT DOC-001 [source page 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Kaplan–Meier/Cox without covariates;HR95%CI;SchoenfeldPH assessment;Table3footnotel;MAIN105 result
- **Analysis keys / checks / missing definitions:** Post hoc mortality CoxHR1.67(.40,6.97),P=.48 matches exact supplement1.67(.40,6.97),P=.484; confidence limits ordered and direction aligned. No event-time or Cox covariance reconstruction is possible.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Five-day Cox mortality 1.67(.40,6.97), .48 matches supplementary .484 within precision; absent event times prevent exact model recreation.

### S011

- **Semantic key:** p.4 subgroup model; map key MAIN043.
- **Locations and roles:** REPORT DOC-001 [source page 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** BinomialGLM with treatment×subgroupinteraction;5prespecified binary partitions:type surgery,BMI40,SpO2 96%,incision,waist-to-hip1.0
- **Analysis keys / checks / missing definitions:** All five interaction tests are separate from stratum effect tests; no interaction covariance inferred from subgroup CIs. Prespecified boundaries match SAP; allocation blocks/risk balancing are recorded separately S080.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Five treatment-by-subgroup interaction tests remain distinct from stratum effects; missing link/covariance is not supplied from separate intervals.

### S012

- **Semantic key:** pp.4,10–12 matched analytical claims; map key MAIN044.
- **Locations and roles:** REPORT DOC-001 [source page 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** R3.4.1;PP vsITTdid not significantly differ;randomization-factor adjustment unaffected;different assumptions similar;abdominalvisceral open/laparoscopic interaction not significant;no numeric sensitivity/interaction vector printed here
- **Analysis keys / checks / missing definitions:** Every referenced sensitivity/subgroup conclusion is matched by its own population/model. The absence of numeric interims and some prospective confirmation analyses does not by itself identify a contradictory reported value.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. PP, adjustment, composite and surgical-interaction claims checked against their own vectors/populations; no equality of different fitted coefficients required.

### S013

- **Semantic key:** Table 2 p.7 tidal volume; map key MAIN045.
- **Locations and roles:** REPORT DOC-001 [source page 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** All 3 time-point H/Lmean (SD),absolute-difference95%CI,P;7.2(1.4)/7.1(.7),0(0,.2),.15;7.2(1.5)/7.1(.4),.1(0,.2),.007;7.3(1.6)/7.1(.6),.1(0,.2),.008;mL/kgpredicted weight;PBW formula in Table 2 p.8
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All three tidal-volume vectors: containment, ordered limits and H−L direction checked; rounded zero endpoints and means can reconcile; exact row test/contributors absent.

### S014

- **Semantic key:** Table 2 p.7 PEEP; map key MAIN046.
- **Locations and roles:** REPORT DOC-001 [source page 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** All 3 time-point vectors11.5(2.0)/4.0(.7),7.5(7.4,7.6);12.0(1.1)/4.0(.5),7.9(7.9,8.0);12.1(1.1)/4.1(.7),8.0(7.9,8.1);all P<.001;cm H2O;narrativepp.4,6matchesfirst-hourmean
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All three PEEP vectors: positive differences and intervals match H>L and narrative; 7.9 versus rounded 12.0−4.0 reconciles at half-unit precision.

### S015

- **Semantic key:** Table 2 p.7 recruitment; map key MAIN047.
- **Locations and roles:** REPORT DOC-001 [source page 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Any972(98.3%)/11(1.1%),97.1(96.1,98.2),P<.001;Hafter968(97.9%),first951(96.2%),last968(97.9%);numbermedian4(IQR3–5);narrativepp.6,8matches;L11rescue
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Recruitment 972/989 versus 11/987 and 97.1 interval retain coherent direction; timing counts are overlapping procedure occasions, not partition totals.

### S016

- **Semantic key:** Table 2 p.7 peak pressure; map key MAIN048.
- **Locations and roles:** REPORT DOC-001 [source page 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** All3H/Lmean (SD)/differenceCI/P;cm H2O;26.0(5.0)/23.4(5.6),2.6(2.1,3.1);27.9(5.1)/26.5(5.6),1.4(1.0,1.9);27.5(5.2)/26.1(5.7),1.4(.9,1.9);all P<.001;pp.8,11direction
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All three peak-pressure vectors contained and ordered; positive H−L differences match arm summaries and narrative.

### S017

- **Semantic key:** Table 2 p.7 driving pressure; map key MAIN049.
- **Locations and roles:** REPORT DOC-001 [source page 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Defined as plateau−PEEP;all 3 vectors11.3(4.6)/15.4(5.1),−4.1(−4.5,−3.6);12.2(4.5)/17.9(5.4),−5.7(−6.1,−5.2);11.8(4.6)/17.4(5.4),−5.6(−6.0,−5.1);all P<.001;cm H2O;pp.8,11direction
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All three driving-pressure vectors contained and ordered with negative H−L differences; source defines plateau−PEEP, separate from peak pressure.

### S018

- **Semantic key:** Table 2 p.7 respiratory rate; map key MAIN050.
- **Locations and roles:** REPORT DOC-001 [source page 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** All 3 vectors14.0(2.9)/14.4(2.6),−.4(−.7,−.2),P<.001;16.0(3.3)/16.2(3.2),−.2(−.5,0),.09;17.0(3.9)/17.4(3.8),−.4(−.7,0),.02;breaths/min
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All three respiratory-rate vectors checked; rounded upper zero with .02 and negative estimate allows a subzero underlying endpoint; test details not inferred.

### S019

- **Semantic key:** Table 2 p.7 FIO2; map key MAIN051.
- **Locations and roles:** REPORT DOC-001 [source page 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** All 3 vectors.57(.21)/.56(.20),.01(0,.02),.27;.45(.09)/.48(.11),−.02(−.03,−.01),<.001;.46(.11)/.49(.13),−.03(−.05,−.02),<.001;fraction;pp.8direction
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All three fractional FiO2 vectors checked with display precision; first small positive and subsequent negative differences agree with direction.

### S020

- **Semantic key:** Table 2 p.7 SpO2; map key MAIN052.
- **Locations and roles:** REPORT DOC-001 [source page 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** All 3 vectors98.2(2.0)/97.4(2.5),.7(.5,.9);97.9(1.9)/96.6(2.3),1.3(1.1,1.5);98.3(2.1)/97.1(2.4),1.2(1.0,1.4);all P<.001;%;p.8direction
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All three SpO2 vectors contained and ordered, with H>L; .7 versus displayed .8 first difference reconciles under rounded summaries.

### S021

- **Semantic key:** Table 2 p.7 end-tidal CO2; map key MAIN053.
- **Locations and roles:** REPORT DOC-001 [source page 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** All 3 vectors38.4(4.8)/38.0(4.5),.3(0,.8),.09;40.4(4.5)/39.9(4.5),.5(.1,.9),.01;41.3(5.4)/40.6(5.1),.7(.2,1.1),.004;mmHg
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All three end-tidal CO2 vectors checked; zero rounded endpoint/.09 does not establish incompatibility; subsequent positive effects and P values coherent at available precision.

### S022

- **Semantic key:** Table 2 p.7 printed Heat rate; map key MAIN054.
- **Locations and roles:** REPORT DOC-001 [source page 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** All 3 vectors76.5(15.8)/76.0(14.3),.6(−.7,1.9),.38;72.6(13.4)/73.1(14.0),−.6(−1.8,.6),.36;73.5(13.0)/74.9(13.8),−1.4(−2.6,−.2),.02;beats/min
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All three heart-rate vectors checked; sign and intervals follow summaries, including final negative difference. Printed name is locally clear.

### S023

- **Semantic key:** Table 2 p.7 mean arterial pressure; map key MAIN055.
- **Locations and roles:** REPORT DOC-001 [source page 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** All 3 vectors84.3(19.3)/82.4(17.5),1.8(.2,3.4),.03;82.0(14.9)/81.9(14.5),.1(−1.2,1.4),.87;81.0(13.9)/81.1(13.8),−.1(−1.4,1.1),.81;mmHg
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All three mean-arterial-pressure vectors checked; contained estimates and ordered endpoints; rounded summary differences and near-null P values do not add a finding.

### S024

- **Semantic key:** Table 2 p.7 head elevation; map key MAIN056.
- **Locations and roles:** REPORT DOC-001 [source page 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 0–15°473(47.8%)/464(47.0%);>15°516(52.2%)/523(53.0%);shared P.70;difference and CI blank
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Head-elevation binary categories sum to 989/987, percentages reconcile; .70 is one category comparison, with no invented per-category effect/CI.

### S025

- **Semantic key:** Table 2 p.7 noninvasive ventilation; map key MAIN057.
- **Locations and roles:** REPORT DOC-001 [source page 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 274(27.7%)/264(26.8%);.9(−3.0,4.9);P.64
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Noninvasive ventilation counts/percentages, .9(−3.0,4.9), .64: contained and ordered with coherent near-null direction.

### S026

- **Semantic key:** Table 2 p.8 anesthesia; map key MAIN058.
- **Locations and roles:** REPORT DOC-001 [source page 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Totalintravenous104(10.5%)/95(9.6%);balanced885(89.5%)/892(90.4%);shared P.51
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Intravenous/balanced anesthesia categories sum to 989/987 and reconcile with percentages; global .51 is not duplicated as two separate tests.

### S027

- **Semantic key:** Table 2 p.8 epidural and location; map key MAIN059.
- **Locations and roles:** REPORT DOC-001 [source page 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Any80(8.1%)/81(8.2%),−.1(−2.5,2.3),.92;thoracic64/80(80.0%)/66/81(81.5%);lumbar16/80(20.0%)/15/81(18.5%);shared location P.81
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Any epidural uses full-arm denominators; thoracic/lumbar use 80/81 and sum accordingly. Global location .81 is separate from any-use .92.

### S028

- **Semantic key:** Table 2 p.8 neuromuscular blockade; map key MAIN060.
- **Locations and roles:** REPORT DOC-001 [source page 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 974(98.5%)/961(97.4%);1.1(−.1,2.4);.08
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Blockade 974/961, 1.1(−.1,2.4), .08 retains coherent direction, containment and percentages; parent counts contextualize existing F-NUM-002 only.

### S029

- **Semantic key:** Table 2 p.8 neuromuscular monitoring; map key MAIN061.
- **Locations and roles:** REPORT DOC-001 [source page 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 632/982(64.9%)/651/984(67.7%);−1.8(−6.0,2.4);.40;includes any monitoring, e.g., train of 4
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Monitoring denominators/percentages and difference remain covered by screened F-NUM-002, PERIPHERAL_COMPARISON; no trial-population reinterpretation or re-emission.

### S030

- **Semantic key:** Table 2 p.8 reversal; map key MAIN062.
- **Locations and roles:** REPORT DOC-001 [source page 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 724/982(74.3%)/723/984(75.2%);.2(−3.6,4.1);.90
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Reversal denominators/percentages and difference remain covered by screened F-NUM-002, PERIPHERAL_COMPARISON; no new issue registered.

### S031

- **Semantic key:** Table 2 p.8 total fluids/crystalloids; map key MAIN063.
- **Locations and roles:** REPORT DOC-001 [source page 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Median (IQR),L:total1.5(1.0,2.5)/1.6(1.0,2.5),.02(−.11,.14),.79;crystalloid1.5(1.0,2.5)/1.5(1.0,2.5),0(−.12,.11),.97
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Both total-fluid/crystalloid medians and difference intervals reviewed; displayed median subtraction is not a source-defined estimator for the reported difference.

### S032

- **Semantic key:** Table 2 p.8 colloids; map key MAIN064.
- **Locations and roles:** REPORT DOC-001 [source page 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Median (IQR),L:.5(.5–.7)/.5(.5–.5),.05(−.09,.19),.50;any74(7.5%)/56(5.7%),1.8(−.3,4.0),.09
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Colloid amount and any-use vectors checked separately; amount estimate lies within CI, and binary 1.8(−.3,4.0), .09 direction is coherent.

### S033

- **Semantic key:** Table 2 p.8 urine; map key MAIN065.
- **Locations and roles:** REPORT DOC-001 [source page 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Median (IQR),L:.14(0,.30)/.15(0,.30);−.02(−.05,.01);.16
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Urine median/IQR and −.02(−.05,.01), .16 checked; no exact median-difference algorithm or underlying data is supplied.

### S034

- **Semantic key:** Table 2 p.8 transfusion; map key MAIN066.
- **Locations and roles:** REPORT DOC-001 [source page 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** RBC19(1.9%)/29(2.9%),−1.0(−2.3,.3),.14;plasma14(1.4%)/17(1.7%),−.3(−1.4,.7),.58;platelets2(.2%)/2(.2%),0(−.3,.3),>.99;albumin19(1.9%)/11(1.1%),.8(−.2,1.8),.14
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All four RBC/plasma/platelet/albumin count, percentage, difference, CI and P vectors checked; contained and ordered, with coherent signs.

### S035

- **Semantic key:** Table 2 p.8 blood loss; map key MAIN067.
- **Locations and roles:** REPORT DOC-001 [source page 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Mean (SD)187(412)/182(382)mL;5.2(−30.3,40.8);.77
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Blood-loss 187/182 means and 5.2(−30.3,40.8), .77: interval contains estimate and rounded summaries allow the difference; row-specific test not assumed.

### S036

- **Semantic key:** Table 2 p.8 temperature; map key MAIN068.
- **Locations and roles:** REPORT DOC-001 [source page 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Mean (SD)36.3(.7)/36.2(.7)°C;0(0,.1);.12
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Temperature 36.3/36.2, rounded 0(0,.1), .12 permits an underlying near-zero difference and endpoint; no precision-level finding.

### S037

- **Semantic key:** Table 2 p.8 durations; map key MAIN069.
- **Locations and roles:** REPORT DOC-001 [source page 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Median (IQR),h:surgery2.5(2.0,3.3)/2.5(2.0,3.3),0(−.1,.1),.62;anesthesia3.2(2.5,4.2)/3.2(2.5,4.2),0(−.1,.2),.94;PBWmen50+.91(height−152.4),women45.5+.91(height−152.4)
- **Analysis keys / checks / missing definitions:** All component time-point/row vectors reviewed: point containment, endpoint order and H−L direction. The source does not individually establish test/variance/contributor count for every displayed continuous or categorical comparison; no method or denominator is supplied by convention. All rounded means/differences and zero CI endpoints allow half-unit display precision. Row-specific exceptions and exclusions are recorded in the checker.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Both duration vectors contained/ordered with near-null tests; PBW formulas match plan/report and retain sex/height units.

### S038

- **Semantic key:** Table 3 p.9 primary PPC;pp.1,2,8,10–12; map key MAIN070.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 211(21.3%)/233(23.6%);−2.3(−5.9,1.4);RR.93(.83,1.04);P.23;abstract,narrative,KeyPoints,Figure2all-patients match;not significantly reduced
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure. Primary .23>.044 supports no detected superiority; abstract, Key Points, text and all-patient forest vector match.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Full primary 211/989 versus 233/987, RD/RR/CI/P and matched occurrences revisited; C001 absorbs quantity identity, while .23>.044 conclusion is coherent.

### S039

- **Semantic key:** Table 3 p.9 mild respiratory; p.8; map key MAIN071.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 135(13.7%)/154(15.6%);−1.9(−5.1,1.2);RR.92(.80,1.05);.22;most common component
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Mild-failure 135/154, RD/RR/CI/.22 contained and ordered; C001 quantity identity and C002 operational definition already registered.

### S040

- **Semantic key:** Table 3 p.9 moderate respiratory; map key MAIN072.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 42(4.2%)/58(5.9%);−1.6(−3.6,.3);RR.83(.65,1.05);.10
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Moderate-failure 42/58, RD/RR/CI/.10 contained and ordered; both existing candidate implications retained without asserting actual recoding.

### S041

- **Semantic key:** Table 3 p.9 severe respiratory; map key MAIN073.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 30(3.0%)/36(3.6%);−.6(−2.2,1.0);RR.90(.69,1.18);.45
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Severe-failure 30/36, RD/RR/CI/.45 contained/ordered and directionally coherent; existing C001 covers identity.

### S042

- **Semantic key:** Table 3 p.9 atelectasis; map key MAIN074.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 44(4.4%)/55(5.6%);−1.1(−3.0,.8);RR.88(.70,1.10);.25
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Atelectasis 44/55 full vector checked; estimate containment, endpoint order and negative direction hold; identity pattern already C001.

### S043

- **Semantic key:** Table 3 p.9 pleural effusion;pp.8,11; map key MAIN075.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 43(4.3%)/21(2.1%);2.2(.7,3.8);RR1.35(1.14,1.62);.005;narrative: higher in H
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure. Higher H effusion matches positive difference and ratio>1; nominal .005 is exploratory. Bonferroni component99.58%CI1.05–1.76 is retained separately.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Effusion 43/21, positive RD, ratio>1 and .005 match higher-H narrative; Bonferroni 99.58% interval also excludes 1; C001 covers identity.

### S044

- **Semantic key:** Table 3 p.9 new infiltrates; map key MAIN076.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 14(1.4%)/18(1.8%);−.4(−1.5,.7);RR.87(.59,1.29);.47
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Infiltrates 14/18 full vector checked, with ordered containing intervals and negative direction; identity issue already C001.

### S045

- **Semantic key:** Table 3 p.9 cardiopulmonary edema; map key MAIN077.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 17(1.7%)/9(.9%);.8(−.2,1.8);RR1.31(.99,1.74);.12
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Cardiopulmonary edema 17/9 full vector checked; ordered containing intervals and positive direction; no same-procedure interval/P inversion imposed.

### S046

- **Semantic key:** Table 3 p.9 bronchospasm; map key MAIN078.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 12(1.2%)/10(1.0%);.2(−.7,1.1);RR1.09(.74,1.60);.67
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Bronchospasm 12/10 full vector checked; conservative count-bound overlap is not an independent contradiction; existing common-block occurrence retained.

### S047

- **Semantic key:** Table 3 p.9 pulmonary infection; map key MAIN079.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 10(1.0%)/10(1.0%);0(−.9,.9);RR.99(.64,1.55);>.99
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Infection 10/10 full vector checked; equal events plus unequal arm totals and display precision are not a separate identity finding.

### S048

- **Semantic key:** Table 3 p.9 aspiration; map key MAIN080.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 2(.2%)/1(.1%);.1(−.2,.4);RR1.33(.60,2.97);>.99
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Aspiration 2/1 full vector checked; rare-cell interval/test options absent, so >.99 is not independently reconstructed from a specified option.

### S049

- **Semantic key:** Table 3 p.9 ARDS; map key MAIN081.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 3(.3%)/1(.1%);.2(−.2,.6);RR1.50(.85,2.64);.62
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. ARDS 3/1, 1.50(.85,2.64), .62 contained/ordered and directionally coherent; declared-measure disparity is within existing C001.

### S050

- **Semantic key:** Table 3 p.9 pneumothorax; map key MAIN082.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 1(.1%)/3(.3%);−.2(−.6,.2);RR.50(.09,2.72);.37
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Pneumothorax 1/3 full vector checked; ordered containing CI and negative direction; rare-cell method options not inferred.

### S051

- **Semantic key:** Table 3 p.9 severe PPC composite; map key MAIN083.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 116(11.7%)/134(13.6%);−1.8(−4.8,1.1);RR.91(.80,1.05);.22;pp.8–10not significantly different
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Severe PPC 116/134 full vector checked; C001 scale and C002 mild-exclusion definition retained separately; no membership consequence asserted.

### S052

- **Semantic key:** Table 3 p.9 extrapulmonary composite; map key MAIN084.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 167(16.9%)/150(15.2%);1.7(−1.5,4.9);RR1.06(.95,1.19);.31
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Extrapulmonary 167/150 full vector checked; contained/ordered and positive direction; separate time-to-event result is a different estimand.

### S053

- **Semantic key:** Table 3 p.9 SIRS; map key MAIN085.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 93(9.4%)/83(8.4%);1.0(−1.5,3.5);RR1.06(.91,1.22);.44
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. SIRS 93/83 full vector checked; estimate containment/order and positive direction hold; existing identity issue not re-emitted.

### S054

- **Semantic key:** Table 3 p.9 sepsis; map key MAIN086.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 18(1.8%)/15(1.5%);.3(−.8,1.4);RR1.09(.79,1.49);.60
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Sepsis 18/15 full vector checked; intervals contain estimates, endpoints ordered and signs match; sparse test options remain unspecified.

### S055

- **Semantic key:** Table 3 p.9 severe sepsis; map key MAIN087.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 7(.7%)/10(1.0%);−.3(−1.1,.5);RR.82(.46,1.45);.46
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Severe sepsis 7/10 full vector checked; contained/ordered, negative direction; identity pattern already C001.

### S056

- **Semantic key:** Table 3 p.9 septic shock; map key MAIN088.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 7(.7%)/8(.8%);−.1(−.9,.7);RR.93(.54,1.60);.79
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Septic shock 7/8 full vector checked; conservative bounds overlap and rare-cell options absent; no additional contradiction asserted.

### S057

- **Semantic key:** Table 3 p.9 GI failure and grades; map key MAIN089.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Any65(6.6%)/56(5.7%),.9(−1.2,3.0),RR1.07(.90,1.28),.40;grade1:34/49(69.4%)/26/46(56.5%);2:11/49(22.4%)/16/46(34.8%);3:3/49(6.1%)/2/46(4.3%);4:1/49(2.0%)/2/46(4.3%);shared grade P.64;no gradeRR/difference printed
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure. Grade P=.64 is one four-category comparison; grade denominator49/46 is explicit and not presumed to be the any-event denominator65/56.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. GI-any 65/56 and all four graded vectors revisited; grades total explicit 49/46, shared .64 is a distribution test, not four row tests.

### S058

- **Semantic key:** Table 3 p.9 kidney failure and grades; map key MAIN090.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Any31(3.1%)/32(3.2%),−.1(−1.6,1.4),RR.98(.76,1.26),.89;risk13/31(41.9%)/15/32(46.9%);injury9/31(29.0%)/10/32(31.2%);failure7/31(22.5%)/5/32(15.6%);loss2/31(6.4%)/2/32(6.2%);shared grade P.97
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure. Grade P=.97 is one four-category comparison, not four per-grade P values; counts total31/32.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Kidney-any 31/32 and all four graded vectors revisited; grade counts sum to 31/32 and .97 is global; nested grade percentages do not change exact event counts or a primary/key secondary result.

### S059

- **Semantic key:** Table 3 p.9 extrapulmonary infection; map key MAIN091.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 29(2.9%)/23(2.3%);.6(−.8,2.0);RR1.11(.87,1.42);.40
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Extrapulmonary infection 29/23 full vector checked; containment/order/direction hold; shared identity pattern already C001.

### S060

- **Semantic key:** Table 3 p.9 hepatic failure; map key MAIN092.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 9(.9%)/9(.9%);0(−.8,.8);RR.99(.63,1.59);>.99
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Hepatic failure 9/9 full vector checked; equal-count, rounded near-one effect does not independently establish the registered pattern.

### S061

- **Semantic key:** Table 3 p.9 coma; map key MAIN093.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 2(.2%)/2(.2%);0(−.4,.4);RR.99(.37,2.66);>.99
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Coma 2/2 full vector checked; equal counts, ordered containing CI and >.99 do not add a distinct observation.

### S062

- **Semantic key:** Table 3 p.9 disseminated intravascular coagulation; map key MAIN094.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 1(.1%)/0; .1(−.1,.3);RR2.00(1.91,2.09);>.99
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure. CI1.91–2.09 excludes1 while P>.99 and differenceCI−.1,.3 spans0. This merits inspection, but a direct CI/test equivalence claim depends on an unspecified sparse-cell variance/test option; excluded under CONDITIONAL_OR_UNREPORTED.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. DIC 1/0, finite ratio/CI and >.99 revisited; C001 covers undefined empirical contrast. A separate CI/P incompatibility depends on missing sparse-cell interval/test options.

### S063

- **Semantic key:** Table 3 p.9 acute myocardial infarction; map key MAIN095.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** H0/L0;difference, CI, RR and P blank
- **Analysis keys / checks / missing definitions:** Both event counts zero; no effect/CI/P printed. Blank is preserved as unreported, not zero; no undefined RR is manufactured.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. MI 0/0 retains blank effect/CI/P; no undefined ratio, precision interval or test value manufactured.

### S064

- **Semantic key:** Table 3 p.9 impaired wound; map key MAIN096.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 22(2.2%)/26(2.6%);−.4(−1.8,.9);RR.91(.66,1.24);.55
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Wound healing 22/26 full vector checked; contained/ordered and negative direction; existing C001 includes the common block.

### S065

- **Semantic key:** Table 3 p.9 unexpected ICU; map key MAIN097.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 41(4.1%)/32(3.2%);.9(−.8,2.6);RR1.12(.91,1.38);.29
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Unexpected ICU 41/32 full vector checked; contained/ordered and positive direction; explicit endpoint window retained.

### S066

- **Semantic key:** Table 3 p.9 hospital-free days90; map key MAIN098.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Mean (SD)81.2(16.5)/82.0(14.5);median (IQR)86(84,87)/86(84,87);difference−.77(−2.16,.61),repeated under the effect column with footnote h identifying the mean difference;P.27;t-test
- **Analysis keys / checks / missing definitions:** Reported mean difference−.77 has ordered95%CI−2.16,.61 and t-testP=.27. Diagnostic SE≈.707 and |t|≈1.09 gives P≈.28; printed vector reconciles under precision. SAP supplementary zero-inflated beta model is not supplied as a numeric result.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Both hospital-free-day mean/SD and median/IQR summaries retained; footnote identifies mean difference −.77 and t-test .27, compatible within precision.

### S067

- **Semantic key:** Table 3 p.9 hypoxemia;pp.1,3,10–11; map key MAIN099.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 49(5.0%)/134(13.6%);−8.6(−11.1,−6.1);RR.51(.40,.65);<.001;abstractprints differenceCI−11.1% to6.1%;both occurrences retained exactly;direction: fewer in H
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure. Abstract upper bound+6.1 is an evident missing minus glyph: lower bound−11.1, point−8.6 and same-tableupper−6.1 make intended sign immediately clear. Excluded NOTATION_OR_TYPOGRAPHY.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Hypoxemia 49/134 full vector and abstract occurrence checked; missing abstract upper-bound minus is immediately resolved by point/lower bound/main table, not a new finding.

### S068

- **Semantic key:** Table 3 p.9 hypotension;pp.3,10–11; map key MAIN100.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 313(31.6%)/170(17.2%);14.4(10.7,18.2);RR1.43(1.31,1.56);<.001;direction: more in H
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Hypotension 313/170 positive difference/ratio, <.001 and narrative agree; C001 concerns magnitude/scale rather than a direction reversal.

### S069

- **Semantic key:** Table 3 p.9 bradycardia;pp.3,10–11; map key MAIN101.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 98(9.9%)/59(6.0%);3.9(1.5,6.3);RR1.27(1.11,1.45);.001;direction: more in H
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Bradycardia 98/59 positive difference/ratio and .001 match narrative; ordered containing intervals; existing C001 absorbs identity.

### S070

- **Semantic key:** Table 3 p.9 in-hospital mortality; map key MAIN102.
- **Locations and roles:** REPORT DOC-001 [source page 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 12(1.2%)/5(.5%);.7(−.1,1.5);RR1.41(.95,1.81);.09;pp.8–10not significantly different
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure. In-hospitalmortality differs in window from five-day Cox mortality, so the estimates are not matched as the same outcome.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. In-hospital death 12/5 full vector checked; contained/ordered and nonsignificant .09. Its window differs from five-day Cox death; interval algorithm absent.

### S071

- **Semantic key:** Table 3 p.10 rescue;pp.11; map key MAIN103.
- **Locations and roles:** REPORT DOC-001 [source page 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 59(6.0%)/166(16.8%);−10.8(−13.6,−8.1);RR.49(.39,.62);<.001;post hoc;direction: fewer in H
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Rescue 59/166 negative difference/ratio, <.001 and fewer-H narrative agree; post hoc status retained; identity issue already C001.

### S072

- **Semantic key:** Table 3 p.10 vasoactive;pp.11; map key MAIN104.
- **Locations and roles:** REPORT DOC-001 [source page 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 491(49.6%)/439(44.5%);5.2(.8,9.6);RR1.10(1.01,1.21);.02;post hoc;direction: fewer in L
- **Analysis keys / checks / missing definitions:** Full event/reference-denominator, differenceCI, ratioCI and P vector reviewed. Printed estimates lie within ordered intervals; direction agrees with H versus L and the narrative. Incidence-measure identity belongs to consolidated F-ST1-001. Intervals and chi-square P are not presumed to be inversions of one procedure.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Vasoactive 491/439, positive difference/ratio and .02 agree with fewer-L narrative and supplementary any-use; identity already C001.

### S073

- **Semantic key:** Table 3 p.10 mortality5days;pp.11; map key MAIN105.
- **Locations and roles:** REPORT DOC-001 [source page 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 5(.5%)/3(.3%);.2(−.3,.8);HR1.67(.40,6.97);.48;post hoc Cox;not significantly different
- **Analysis keys / checks / missing definitions:** Post hoc mortality CoxHR1.67(.40,6.97),P=.48 matches exact supplement1.67(.40,6.97),P=.484; confidence limits ordered and direction aligned. No event-time or Cox covariance reconstruction is possible.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Five-day mortality 5/3 with Cox exception, 1.67(.40,6.97), .48 agrees with supplementary .484; no incidence-RR substitution.

### S074

- **Semantic key:** Figure 2 p.10 type surgery; map key MAIN106.
- **Locations and roles:** REPORT DOC-001 [source page 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Nonlaparoscopic79/240vs74/253,RR1.09(.90,1.32);laparoscopic130/740vs156/727,RR.88(.77,1.01);interaction P.08;method: binomial GLM
- **Analysis keys / checks / missing definitions:** All two-stratum counts, ratio95%CIs and interactionP reviewed; containment/order/direction hold. Every reported interactionP>.05 and no subgroup heterogeneity conclusion is asserted. Test depends on fitted binomial GLM and shared covariance, not obtainable from separate CIs; no link or covariance is inferred. Estimand identity joins F-ST1-001.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Both surgical strata and .08 interaction checked; subgroup contributors do not imply full-arm counts; interaction covariance/link not inferred from CIs.

### S075

- **Semantic key:** Figure 2 p.10 BMI; map key MAIN107.
- **Locations and roles:** REPORT DOC-001 [source page 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** <40:76/336vs94/376,RR.93(.77,1.13);≥40:135/653vs139/611,RR.94(.82,1.08);interaction P.97;BMI kg/m² footnote
- **Analysis keys / checks / missing definitions:** All two-stratum counts, ratio95%CIs and interactionP reviewed; containment/order/direction hold. Every reported interactionP>.05 and no subgroup heterogeneity conclusion is asserted. Test depends on fitted binomial GLM and shared covariance, not obtainable from separate CIs; no link or covariance is inferred. Estimand identity joins F-ST1-001.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Both BMI strata sum to full arms and .97 interaction supports no detected interaction; C001 handles displayed quantity identity.

### S076

- **Semantic key:** Figure 2 p.10 baseline saturation; map key MAIN108.
- **Locations and roles:** REPORT DOC-001 [source page 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** <96%88/317vs112/342,RR.88(.74,1.06);≥96%123/672vs121/645,RR.99(.86,1.13);interaction P.35
- **Analysis keys / checks / missing definitions:** All two-stratum counts, ratio95%CIs and interactionP reviewed; containment/order/direction hold. Every reported interactionP>.05 and no subgroup heterogeneity conclusion is asserted. Test depends on fitted binomial GLM and shared covariance, not obtainable from separate CIs; no link or covariance is inferred. Estimand identity joins F-ST1-001.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Both SpO2 strata sum to full arms, directions/intervals hold and .35 interaction is separate from stratum estimates.

### S077

- **Semantic key:** Figure 2 p.10 incision; map key MAIN109.
- **Locations and roles:** REPORT DOC-001 [source page 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Peripheral32/126vs25/126,RR1.16(.89,1.53);upperabdominal179/863vs208/861,RR.90(.80,1.02);interaction P.11
- **Analysis keys / checks / missing definitions:** All two-stratum counts, ratio95%CIs and interactionP reviewed; containment/order/direction hold. Every reported interactionP>.05 and no subgroup heterogeneity conclusion is asserted. Test depends on fitted binomial GLM and shared covariance, not obtainable from separate CIs; no link or covariance is inferred. Estimand identity joins F-ST1-001.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Both incision strata sum to full arms and .11 interaction agrees with narrative; no independent interaction reconstruction from marginal CIs.

### S078

- **Semantic key:** Figure 2 p.10 waist-to-hip; map key MAIN110.
- **Locations and roles:** REPORT DOC-001 [source page 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** Printed label: cm;<1.0:97/467vs100/457,RR.97(.83,1.13);≥1.0:98/447vs112/449,RR.92(.78,1.08);interaction P.65
- **Analysis keys / checks / missing definitions:** All two-stratum counts, ratio95%CIs and interactionP reviewed; containment/order/direction hold. Every reported interactionP>.05 and no subgroup heterogeneity conclusion is asserted. Test depends on fitted binomial GLM and shared covariance, not obtainable from separate CIs; no link or covariance is inferred. Estimand identity joins F-ST1-001.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Both waist-to-hip strata and .65 interaction checked; incomplete measurement contributors retained, ratio-unit glyph immediately clear; C001 not re-emitted.

### S079

- **Semantic key:** Figure 2 p.10 allpatients/axes and matched subgroup claim; map key MAIN111.
- **Locations and roles:** REPORT DOC-001 [source page 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10); other exact matched pages remain in the semantic key.
- **Full printed vector / specification:** 211/989vs233/987;RR.93(.83,1.04);marker sizes proportional to numbers entering the analysis;axisRR95%CI ticks.7,1,2;left favors H; right favors L;pp.8,12claim: consistent effects; no significant interaction
- **Analysis keys / checks / missing definitions:** All-patient forest vector equals main primaryvector. Left/right favorable labels agree with ratio direction. Marker sizes represent analyzed sample, and no significant interaction claim follows the five reported interactionP values; repeated occurrences remain in S038/S074–S078 evidence matching.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All-patient 211/989 versus 233/987 vector matches primary; favorable axes and no-significant-interaction claim agree with all five interaction P values.

### S080

- **Semantic key:** Trial design, eligibility, allocation unit/stratification, intervention dose/timing and rescue.
- **Additional design / intervention / measurement specifications:**
  - PLAN010: PLAN DOC-002 [p.13](../../../joi190055supp1_prod_16092.pdf#page=13): Lower PEEP 4 cmH2O/no recruitment versus higher 12 cmH2O/recruitment. Volume controlled, FiO2 minimum .4 and lowest to maintain saturation ≥93%; I:E 1:2; rate for end-tidal CO2 35–45 mmHg; tidal volume 7 ml/kg IBW. Male IBW=50+.91×(height cm−152.4), female=45.5+.91×(height cm−152.4). Tidal volume actual inspired ventilator-circuit volume.
  - PLAN011: PLAN DOC-002 [pp.13–14](../../../joi190055supp1_prod_16092.pdf#page=13): Recruitment after induction, every disconnection, every hour and before surgery end when stable. Peak limit 55 cmH2O; start tidal volume 7 ml/kg IBW, rate ≥6/min, PEEP12 (or higher rescue), I:E1:1; tidal-volume increments 4 ml/kg to plateau40–50; if max volume with plateau<40 increase PEEP≤20; maintain 3 breaths plateau40–50; restore prior settings retaining PEEP12/rescue.
  - PLAN012: PLAN DOC-002 [p.14](../../../joi190055supp1_prod_16092.pdf#page=14), [p.19](../../../joi190055supp1_prod_16092.pdf#page=19): Deviations allowed for safety/surgeon request; PEEP modification with systolic<90 >3 min unresponsive fluids/vasoactive drugs, refractory arrhythmia, vasoactive tolerance limit, massive transfusion or life-threatening surgery. Massive transfusion >100% blood volume/24 h or >50%/4 h; approximate adult blood volume70 ml/kg; target Hct>21%, Hb>7 mg/dl as printed. p.19 adherence list uses >50%/4 h.
  - PLAN013: PLAN DOC-002 [pp.14–15](../../../joi190055supp1_prod_16092.pdf#page=14): Lower-arm rescue after excluding airway/auto-PEEP/hemodynamic/ventilator causes: desaturation≤92%; nine FiO2/PEEP steps .5/4, .6/4, .7/4, .8/4, .9/4,1.0/4,1.0/5,1.0/6,1.0/7(optional RM); FiO2 fraction, PEEP cmH2O. p.13 trigger specifies >1 min.
  - PLAN014: PLAN DOC-002 [p.15](../../../joi190055supp1_prod_16092.pdf#page=15): Higher-arm rescue after excluding same causes: .4/14(RM optional), .4/16(RM optional), .4/18(RM optional), .5/18,.6/18,.7/18,.8/18,.9/18,1.0/18,1.0/20(RM optional). If saturation worsens despite stable hemodynamics consider PEEP10 then8 at any step. Surgery starts incision/trocar insertion and ends wound closure.
  - PLAN016: PLAN DOC-002 [p.17](../../../joi190055supp1_prod_16092.pdf#page=17): Baseline SpO2 after10 min room air beach-chair; added supine10min measurement if beach-chair SpO2≥92%; FVC/FEV1 optional; dyspnea and thoracic/abdominal rest/incident pain VAS10 cm.
  - PLAN017: PLAN DOC-002 [pp.18–19](../../../joi190055supp1_prod_16092.pdf#page=18): Intraoperative measurements after induction, hourly and immediately before/after recruitment; anesthesia intubation→extubation/OR exit and surgery incision→closure in minutes; peak/plateau/PEEP cmH2O, tidal volume ml, respiratory rate, I:E, inspired fraction %, SpO2%, end-tidal CO2 mmHg, systolic/diastolic/mean pressure mmHg; dose/fluids/transfusion, blood loss and urine ml whole surgery.
  - PLAN033: PLAN DOC-003 [p.1](../../../joi190055supp2_prod_16092.pdf#page=1): Approved 2.4.1 June2014 vs2.4 November2013: open/laparoscopic inclusion changed to all surgery under general anesthesia; hepatic definition replaced bilirubin>2mg/dL plus transaminase/LDH>2×normal with ratios and90day definition recorded PLAN031.
  - PLAN037: PLAN DOC-003 [p.3](../../../joi190055supp2_prod_16092.pdf#page=3): 2.6 October2016 vs2.5 adds supine10min room-air SpO2 measurement when beach-chair≥92%.
- **Matched reported intervention:** REPORT DOC-001 pp.1–3 and DOC-005 pp.18–20: high PEEP12cmH2O with recruitment versus low PEEP4cmH2O without routine recruitment, volume-controlled tidal volume7mL/kg predicted weight, recruitment after intubation/hourly/after disconnection/before surgery end or extubation, plateau40–50cmH2O, peak limit55cmH2O, three breaths at target, rescue for SpO2≤92%. The supplied PBW formulas are50+.91×(height−152.4) for men and45.5+.91×(height−152.4) for women. Definitions of surgical exposure, safety deviations and arm-specific rescue dose schedules are retained above; intervention implementation is not audited clinically.
- **Full printed specifications and exact roles/locations:**
  - PLAN001: PLAN DOC-002 [p.5](../../../joi190055supp1_prod_16092.pdf#page=5), [p.8](../../../joi190055supp1_prod_16092.pdf#page=8): International multicenter randomized trial; hypothesis that higher PEEP with recruitment prevents PPC in intermediate/high-risk obese patients ventilated with lower tidal volumes. Summary primary endpoint is proportion of patients with PPC.
  - PLAN003: PLAN DOC-002 [pp.5–6](../../../joi190055supp1_prod_16092.pdf#page=5), [p.9](../../../joi190055supp1_prod_16092.pdf#page=9), [p.10](../../../joi190055supp1_prod_16092.pdf#page=10): BMI ≥35 kg/m2; ARISCAT ≥26; surgery under general anesthesia expected ≥2 h. Adults through exclusion age <18. ARISCAT intermediate/high threshold repeated p.29.
  - PLAN004: PLAN DOC-002 [p.10](../../../joi190055supp1_prod_16092.pdf#page=10): Recruit 2013; expected 90 centers, at least 24 randomized per center; consecutive screening over 2 years, registry all screened regardless of eligibility.
  - PLAN005: PLAN DOC-002 [pp.10–11](../../../joi190055supp1_prod_16092.pdf#page=10): Exclusions: previous lung surgery, unstable hemodynamics/intractable shock, severe COPD home NIV/oxygen or repeated systemic corticosteroid exacerbation treatment, chemotherapy/radiation ≤2 months before surgery, NYHA III/IV/acute coronary syndrome/persistent ventricular tachyarrhythmia, invasive ventilation >30 min in last 30 days, pregnancy, prevalent ARDS requiring prolonged ventilation, pulmonary systolic pressure >40 mmHg, intracranial injury/tumor, neuromuscular disease, prone/lateral position, one-lung ventilation, cardiac/neurosurgery, planned reintubation, other interventional study/refusal consent.
  - PLAN009: PLAN DOC-002 [pp.12–13](../../../joi190055supp1_prod_16092.pdf#page=12): Dedicated central website, balanced per center and ARISCAT intermediate/high risk; permuted blocks length 6; 1:1 allocation before surgery. One intervention-aware intraoperative collector and a blinded postoperative outcome assessor at each site.
- **Checks / missing definitions:** Main randomization (p2) states site strata and blocks4,6,8; protocol states fixed block6 and ARISCATbalance. Plan does not label ARISCAT as an analysis random effect; site adjustment remains distinct. A risk-balancing instruction versus a condensed report description does not establish a changed primary estimator. Exact block difference is retained as plan/report context, without inferring a clinical effect or unreported stratum.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All plan/report design, intervention/rescue, measurement and amendment specifications revisited. Reported dose/formulas match; allocation-block wording does not establish a changed primary estimator or decision rule.

### S081

- **Semantic key:** Primary collapsed PPC definition, component hierarchy and measurement.
- **Full printed specifications and exact roles/locations:**
  - PLAN021: PLAN DOC-002 [p.22](../../../joi190055supp1_prod_16092.pdf#page=22): Primary collapsed composite in first five days: aspiration pneumonitis, bronchospasm, mild/moderate/severe respiratory failure, ARDS, infection, atelectasis, cardiac-failure pulmonary edema, effusion, pneumothorax, new infiltrates; ≥1 meets endpoint.
  - PLAN029: PLAN DOC-002 [p.31](../../../joi190055supp1_prod_16092.pdf#page=31): Complete PPC definitions in table below.
  - PLAN038: PLAN DOC-004 [p.1](../../../joi190055supp3_prod_16092.pdf#page=1): Updated SAP finalized January20,2018; steering endorsement before last inclusion, database lock and analysis. Primary first-five-day collapsed PPC ≥1, same component list.
  - Detailed PLAN DOC-002p31 component thresholds: aspiration respiratoryfailure after inhaledgastriccontent; bronchospasm newlywheezing treatedbronchodilators; mildRF PaO2<60mmHg orSpO2<90% after≥10minroomair respondsoxygen; moderateRF same thresholds despiteoxygen; severeRF requiresNIV/invasiveventilation; ARDS Berlin; infectionnew/progressiveinfiltrate+≥2ofantibiotic,temperature>38°C,WBC<4000/>12000 and/orpurulence; atelectasisopacity+ipsilateralshift+adjacentoverinflation; edemaclinicalcongestion+Xrayvascular/diffuseinfiltrates; effusioncostophrenic/hemidiaphragm/displacement/supinehazecriteria; pneumothoraxpleuralairwithoutvascularbed; newinfiltrateswithoutothersigns. REPORT DOC-005pp20–21 supplies mild≤2L/min,moderate>2L/min andsevereventilation classifications; the source '=2' glyph is interpreted with main Table3definition≤2, rather than redefining endpoint.
- **Checks / missing definitions:** ≥1of12 first-five-day components matches report. Component-specific respiratory severity wording differs between protocol oxygen-response criteria and report≤2/>2L definitions; later SAP adopts same component list without newly defining oxygen strata. This preserves a direct endpoint-definition comparison for cross-source checking; neither raw recoding nor changed primary composite size is inferred.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Full component/window hierarchy revisited with C002: protocol moderate omits room-air/ten-minute qualifiers; oxygen-response/flow distinction remains existing P_R issue, without actual recoding inference.

### S082

- **Semantic key:** Secondary endpoints, safety/event windows and severe PPC.
- **Full printed specifications and exact roles/locations:**
  - PLAN002: PLAN DOC-002 [p.5](../../../joi190055supp1_prod_16092.pdf#page=5), [p.12](../../../joi190055supp1_prod_16092.pdf#page=12): Secondary list: intraoperative complications, postoperative invasive/noninvasive support, unexpected ICU admission or readmission within 30 days, hospital readmission within 30 days, hospital-free days at day 90, mortality at day 90, extrapulmonary complications, wound healing. Desaturation SpO2 ≤92% >1 min; hypotension during recruitment systolic pressure <90 mmHg >2 min.
  - PLAN018: PLAN DOC-002 [p.19](../../../joi190055supp1_prod_16092.pdf#page=19): Recruitment-related events: new systolic<90 mmHg or drop>10 mmHg if already<90; new HR<50 bpm or drop>20% if already<50; new SpO2≤92% or drop>5% if already<92%; other events recorded.
  - PLAN019: PLAN DOC-002 [pp.19–20](../../../joi190055supp1_prod_16092.pdf#page=19): Assess daily first through fifth postoperative day and last day before discharge; score pulmonary/extrapulmonary complications with date onset; postoperative ventilation indication/duration hours, new CPAP/NPPV/invasive support, ICU stay/readmission, impaired wound recovery, bowel/mobility, postoperative fluids/transfusion since last assessment; SpO2 room-air beach-chair, vital/laboratory/optional imaging/spirometry; discharge date.
  - PLAN030: PLAN DOC-002 [p.32](../../../joi190055supp1_prod_16092.pdf#page=32): Complete extrapulmonary definitions below.
  - PLAN031: PLAN DOC-002 [p.33](../../../joi190055supp1_prod_16092.pdf#page=33): DIC/GI/hepatic definitions below.
  - PLAN039: PLAN DOC-004 [p.1](../../../joi190055supp3_prod_16092.pdf#page=1): Secondary collapsed severe PPC excludes mild respiratory failure; extrapulmonary events, intraoperative events per original protocol, unexpected ICU, wound healing, in-hospital mortality, hospital-free days day90. REDCap/randomization and25% source-file checks; lock after resolving data or exhausted efforts.
  - Exact PLANdefinitionsDOC-002pp32–33: SIRS≥2temperature<36/>38°C,HR>90,RR>20/PaCO2<32mmHg,WBC<4000/>12000/>10%bands; sepsisinfectiousSIRS; severesepsisorgan dysfunction/hypoperfusion/hypotension; septicshockrefractoryhypotensiondespitefluids (lactate>4mmol/dL printed); comaGlasgow<8withoutsedation; MIcardiacmarkerrise/fall≥1above99thpercentile+ischemia evidence; renalriskCr×1.5/GFRdrop>25%/urine<.5ml/kg/h×6h,injury×2/>50%/<.5×12h,failure×3/>75%/<.3×24h/anuria12h,loss>4weeks; DICplatelets<50:2/<100:1,DDimer>4:2/>.39:1,PT>20.5:2/>17.5:1,total≥5; GI0normal,1feed<50%/none3days,2intoleranceORhypertension,3both,4compartmentsyndrome; hepaticday5/day1bilirubin>1.7andINR>1.0,ornewencephalopathyandINR>1.5within8weekswithoutchronichepaticdisease. These thresholds are preserved for matching endpoint identity, not clinical audit.
- **Checks / missing definitions:** SeverePPC excludes mildRF consistently. Protocolday90mortality was replaced in finalSAP with in-hospitalmortality before last inclusion; amendment/SAP context resolves old/latest endpoint hierarchy. Posthocfive-day mortality remains separate. Recruitment-event thresholds and overall intraoperative-event labels are read with reportdefinitions, without asserting different denominators.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All secondary/severe/safety windows and definitions revisited; final SAP identifies in-hospital mortality and mild exclusion, resolving historical endpoint list context.

### S083

- **Semantic key:** Original power and retained historical enrollment.
- **Full printed specifications and exact roles/locations:**
  - PLAN006: PLAN DOC-002 [p.11](../../../joi190055supp1_prod_16092.pdf#page=11): Initial calculation: 356 per group; two-sided α=.05, power 80%, higher PEEP event rate 30%, lower 40%, RR .75; 5% dropout, 748 total/374 per group.
  - PLAN008: PLAN DOC-002 [p.12](../../../joi190055supp1_prod_16092.pdf#page=12): Procedure section explicitly retains total 748; primary parameter PPC; systemic inflammation/lung/distal-organ injury markers other parameters.
- **Checks / missing definitions:** Normal diagnostic356perarm;712×1.05=747.6→748. Retained748 procedure statement is historical beside explicit revised2013 and approvedversion2.5sample-size change; immediate context identifies current target.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Original 356-per-arm/748 planning text is historical alongside explicit revised target and approved change; normal diagnostic and additive allowance reconcile.

### S084

- **Semantic key:** Adaptive sample-size assumptions and disclosed version change.
- **Full printed specifications and exact roles/locations:**
  - PLAN007: PLAN DOC-002 [p.11](../../../joi190055supp1_prod_16092.pdf#page=11): Re-estimated after first 618 patients on DSMB recommendation, lower collapsed-composite incidence; control .20, RR .75, overall α=.05, power 80%, maximum 1912 with interim efficacy/futility adjustment; 5% dropout, 2013 included; East 6.0.
  - PLAN035: PLAN DOC-003 [p.2](../../../joi190055supp2_prod_16092.pdf#page=2): 2.5 February2016 vs2.4.2: centers60→90, minimum patients12–13→24; original power text kept/slightly modified; revised618-patient observation/control.20/RR.75/power80%/overall.05/max1912/5% dropout2013/East6.0 added.
- **Checks / missing definitions:** Revisedmaximum1912includes sequential monitoring;1912/.95=2012.632→2013. Fixed-design normal diagnostic1810.732total cannot establish discrepancy for stated sequentialEastdesign. No raw eventrate beyond blindedpooled≈20% is inferred.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All revised power inputs/version change retained; sequential maximum 1912 and 5% allowance yield 2013. Fixed-design calculation is only a diagnostic.

### S085

- **Semantic key:** Interim/stopping boundaries, alpha/beta spending and version chronology.
- **Full printed specifications and exact roles/locations:**
  - PLAN022: PLAN DOC-002 [p.22](../../../joi190055supp1_prod_16092.pdf#page=22): Nonbinding sequential efficacy/futility looks50%,75%,100% (N956,1434,1912); gamma spending−4 for α and β; P efficacy≤.006,≤.015,≤.044; futility>.82,>.35,>.044 respectively.
  - PLAN023: PLAN DOC-002 [p.22](../../../joi190055supp1_prod_16092.pdf#page=22): Table power.80, α.05, gamma−4,p1=.20,p2=.15. Look1 fraction.5/N956/cumulative α.006/β.024/Zeff≥2.75/Zfut<.225/H1 crossing efficacy.234/futility.024. Look2 .75/1434/.018/.071/≥2.432/<.929/.296/.047. Look3 1/1912/.05/.2/≥2.012/<2.012/.271/.129.
  - PLAN024: PLAN DOC-002 [p.23](../../../joi190055supp1_prod_16092.pdf#page=23): Figure axes enrollment956,1434,1912 and Effect Size(Z)−4 to4; upper blue Harm at approximately +2.75,+2.432,+2.012; lower blue Efficacy at negatives; central pink Futility expands from ±.225 to±.929 to±2.012. Boundaries mirror table absolute magnitudes; figure direction preserved.
  - PLAN034: PLAN DOC-003 [pp.1–2](../../../joi190055supp2_prod_16092.pdf#page=1): 2.4.2 October2014 vs2.4.1 heading says June2013: delete previous interim at50% (n374 randomized/treated), early termination RR<.5 or>2.0 (examples higher<20% or>80% against lower40%), DSMB decision, undisclosed absent early stop; explicitly no interim analyses. Primary endpoint/analysis section updated; AE appendix added; postoperative day2/4 visits added to sheet but already in prior text; DSMB4.
  - PLAN036: PLAN DOC-003 [pp.2–3](../../../joi190055supp2_prod_16092.pdf#page=2): Version2.5 adds sequential looks N956,1434,1912 at50/75/100%; nonbinding gamma−4 α/β, efficacy nominalP≤.006,.015,.044 and futility>.82,.35,.044; table/figure added; DSMB5.
- **Checks / missing definitions:** EfficacyZ2.75/2.432/2.012 correspond two-sidednominalP≈.006/.015/.044. Cumulativealpha.006/.018/.05 is not nominalP at a look. H1efficacycrossing.234+.296+.271=.801 andfutility.024+.047+.129=.200 match power.80 within rounding. The approved removal and later reinstatement of interim monitoring is explicit. Actual interimZ/P are absent; continuation cannot be independently replayed.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All three alpha/beta/Z/crossing-probability vectors and version chronology checked. Nominal .006/.015/.044 differs coherently from cumulative alpha; crossings sum .801/.200 within precision.

### S086

- **Semantic key:** Protocol preliminary measure names/models and definitive SAP.
- **Full printed specifications and exact roles/locations:**
  - PLAN025: PLAN DOC-002 [p.23](../../../joi190055supp1_prod_16092.pdf#page=23): Exact source prose: “odds ratio relative risks” with “95% confidence levels interval” using logistic regression for primary group comparison. No deleted text/strikeout apparent in rendered source; both measure names coexist in print.
  - PLAN026: PLAN DOC-002 [p.23](../../../joi190055supp1_prod_16092.pdf#page=23): Remaining normal variables mean/SD and Student t; nonnormal median/IQR and Mann–Whitney U; categorical n(%) and χ²/Fisher or relative risks; time-dependent data proportional hazard model adjusted for possible baseline imbalances.
  - PLAN027: PLAN DOC-002 [p.23](../../../joi190055supp1_prod_16092.pdf#page=23): SAP finalized before data collection end; only primary confirmatory, all others exploratory; intention-to-treat; blinded statistical expert; significance p=.05; uncertainty95%; software SPSS.
- **Checks / missing definitions:** Protocol phrase 'odds ratio relative risks' and logistic model is ambiguous in isolation, but prospective finalSAP expressly replaces with incidenceRR/chi-square. The current reportfollowsSAP statedlabel; the unresolved reportedmeasure identity is F-ST1-001, rather than a separate preliminary terminology issue. t/MWU/chi-square/Fisher choices are stated coherently for respective data.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Preliminary OR/RR/logistic wording is superseded by explicit final SAP incidence specification; t/MWU/chi-square/Fisher choices coherent; no preferred method proposed.

### S087

- **Semantic key:** SAP missingness, population, sidedness and multiplicity.
- **Full printed specifications and exact roles/locations:**
  - PLAN040: PLAN DOC-004 [p.2](../../../joi190055supp3_prod_16092.pdf#page=2): Complete-case all outcomes excluding missing outcome; if >1% primary missing, multiple-imputation and estimating-equation sensitivity; minimal/no losses anticipated.
  - PLAN041: PLAN DOC-004 [p.2](../../../joi190055supp3_prod_16092.pdf#page=2): Modified ITT in assigned group; exclude loss due withdrawal consent or surgery cancellation; statement no major preliminary-plan adjustments.
  - PLAN042: PLAN DOC-004 [p.2](../../../joi190055supp3_prod_16092.pdf#page=2): Histograms plus D’Agostino–Pearson normality; baseline counts/%/meanSD/medianIQR; two-sided tests5% except primary interim correction; no multiplicity P adjustment; R2016.
- **Checks / missing definitions:** Completecases primary missingtrigger>1%;8postoperativelosses/1984eligible=.403%, so sensitivitytrigger not reached. 29postsurgeryeligibility/nonconsent exclusions and8losses are disclosed. mITT/ITT naming does not alter989/987. Normalitytests and Ryear/version differences do not identify contradictory reported test.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Complete-case/mITT rules, >1% trigger, sidedness and multiplicity revisited; 8/1984=.403% does not reach trigger, 989/987 population unchanged by names.

### S088

- **Semantic key:** SAP primary/binary/time-to-event and hospital-free-day methods.
- **Full printed specifications and exact roles/locations:**
  - PLAN044: PLAN DOC-004 [p.2](../../../joi190055supp3_prod_16092.pdf#page=2): Primary incidence numbers/% and RR95% CI via “Wald’s likelihood ratio approximation test”; χ² hypothesis test; two-sided α=.044; Kaplan–Meier time to PPC with log-rank.
  - PLAN045: PLAN DOC-004 [p.2](../../../joi190055supp3_prod_16092.pdf#page=2): Binary secondary numbers/%/RR95% CI same Wald wording and χ²; day90 hospital-free mean difference/Student t; confirmation mean ratio generalized additive model zero-inflated beta.
- **Checks / missing definitions:** PrimaryRR/95%CI/chi-square/finalalpha.044 matches reportmethod labels, with F-ST1-001 covering identity. SAPlog-rank planned, reportCoxHR given; exact log-rank statistic/test notprinted, so no equivalence is imposed. Hospital-free-dayzero-inflatedbetameanratio confirmation is not supplied numerically; absence alone does not contradict displayedmean difference.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Final primary/binary/t-test models match report labels; log-rank and additional hospital-free-day confirmation outputs are not supplied, without establishing replacement of reported analysis.

### S089

- **Semantic key:** SAP subgroup partitions, interaction and site random-effect sensitivity.
- **Full printed specifications and exact roles/locations:**
  - PLAN046: PLAN DOC-004 [pp.2–3](../../../joi190055supp3_prod_16092.pdf#page=2): PPC subgroups nonlaparoscopic/laparoscopic; BMI<40/≥40 kg/m2; baselineSpO2<96/≥96%; peripheral/upper abdominal (incision cranial umbilicus); waist:hip<1/≥1. Treatment-by-subgroup interactions generalized linear models and forest plot.
  - PLAN047: PLAN DOC-004 [p.3](../../../joi190055supp3_prod_16092.pdf#page=3): Primary sensitivity generalized linear mixed-effect model center random effects (stratification variable).
- **Checks / missing definitions:** Allfivepartitions match mainFigure2; siteGLMM result .86(.68,1.08),P.19 retainedS098. No model link/covariance inferred; binomialinteraction and siteadjustment account for stated participant/design units.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All five SAP partitions, interaction and site-random sensitivity match reported counterparts; no GLM link or covariance supplied from convention.

### S090

- **Semantic key:** SAP component count and individual component multiplicity.
- **Full printed specifications and exact roles/locations:**
  - PLAN048: PLAN DOC-004 [p.3](../../../joi190055supp3_prod_16092.pdf#page=3): Count of positive composite components; Mann–Whitney group comparison and proportional-odds logistic OR95% CI.
  - PLAN049: PLAN DOC-004 [p.3](../../../joi190055supp3_prod_16092.pdf#page=3): Each component generalized linear model with Bonferroni;99.58% CI, printed 1−.05/12=.9958.
- **Checks / missing definitions:** CountproportionaloddsCI andMann–WhitneyP are explicitly separate, so test inversion is not imposed.1−.05/12=.9958333→99.58% printed componentCI. All12eFigure12point intervals ordered and contain estimates; pleuraleffusion excludes1 even atcorrectedlevel.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Count OR/Wilcoxon distinction and 12-component correction retained: 1−.05/12=.9958333, displayed 99.58%; no common test inversion imposed.

### S091

- **Semantic key:** SAP common/average/heterogeneous/severity-weighted GEE.
- **Full printed specifications and exact roles/locations:**
  - PLAN050: PLAN DOC-004 [p.3](../../../joi190055supp3_prod_16092.pdf#page=3): Multivariate GEE multiple outcomes/subject; common-effect OR across components; distinct-effect GEE separate component effects; average relative effect averages those treatment effects and tests average=0.
  - PLAN051: PLAN DOC-004 [p.3](../../../joi190055supp3_prod_16092.pdf#page=3): Treatment-by-component interaction in distinct-effects GEE tests heterogeneity.
  - PLAN052: PLAN DOC-004 [p.3](../../../joi190055supp3_prod_16092.pdf#page=3): Clinical severity weights determined a posteriori; multivariate GEE common-effect OR with weights.
- **Checks / missing definitions:** Multipleoutcomes perparticipant are explicitly recognized by GEE. CommonsingleeffectOR, distinctcomponentcoefficients, averageeffecttestzero, interactionheterogeneity andaposterioriweights are retained. Covariance/varianceestimator, transformation of averageeffect and numericseverityweights notsupplied; no specificGEEtest is inferred. Potential Wald re-expression ofaverageOR .99CI.94–1.05P.98 is conditional, excluded. Weightednumericresultnotprinted; missing output alone does not support changed primary inference.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All common/distinct/average/heterogeneous/severity-weighted GEE steps retained; transformation, covariance and severity weights absent. Average CI/P Wald diagnostic remains conditional.

### S092

- **Semantic key:** Intraoperative IV fluids; SUP012.
- **Locations and roles:** REPORT DOC-005 [page 24](../../../joi190055supp4_prod_16092.pdf#page=24).
- **Checks / missing definitions:** Every displayed row/count/percentage/meanSD/dose/P is retained below. Independent-arm comparisons respect participant randomization; where table-level exact test choice/contributor denominator is absent, it remains unreported. Categorical global P values and withinparticipant day/time records are not reinterpreted as row-specific or independent repeated-measures tests. No matched peripheral comparison is promoted.
- **Full printed vector (source-mapped layout):**

### Physical PDF page 24

eTable 3. Types of intraoperative IV fluids

___________________________________________________________________________
                                    High PEEP             Low PEEP             P value
                                    n=989                 n=987


Total fluids – mL, mean (SD)        1898 (1401)           1882 (1352)          0.79
       Crystalloids, No. (%)        920 (93.0)            928 (94.0)           0.37
                                    1838 (1306)           1841 (1298)          0.97
       Synthetic colloids, No. (%) 74 (7.5)               56 (5.7)             0.10
                                    50 (211)              35 (171)             0.09
              HES, No. (%)          45 (4.6)              32 (3.2)             0.13
                                    32 (178)              21 (139)             0.15
              Gelatines, No. (%)    31 (3.1)              24 (2.4)             0.34
                                    17 (104)              13 (102)             0.38
              Dextran, No. (%)      1 (0.1)               0 (0.0)              0.99
                                    1 (15.9)              0 (0)                0.32
___________________________________________________________________________
PEEP, positive end-expiratory pressure; HES, hydroxyl-ethyl -starch containing solution.




© 2019 American Medical Association. All rights reserved.

- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Every fluid type count/percentage, mean/SD and P checked; types can overlap, dose summaries need not equal medians in main; exact row test choice absent.

### S093

- **Semantic key:** Vasoactive/inotropic drug requirements and doses; SUP013.
- **Locations and roles:** REPORT DOC-005 [page 25](../../../joi190055supp4_prod_16092.pdf#page=25).
- **Checks / missing definitions:** Every displayed row/count/percentage/meanSD/dose/P is retained below. Independent-arm comparisons respect participant randomization; where table-level exact test choice/contributor denominator is absent, it remains unreported. Categorical global P values and withinparticipant day/time records are not reinterpreted as row-specific or independent repeated-measures tests. No matched peripheral comparison is promoted.
- **Full printed vector (source-mapped layout):**

### Physical PDF page 25

eTable 4. Types of intraoperative vasoactive drugs

___________________________________________________________________________
                             High PEEP         Low PEEP          P value
                                    n=989             n=987
___________________________________________________________________________


Need for vasoactive drugs           491 (49.6)        439 (44.5)   0.02
       Dopamine, No. (%)            0 (0.0)           2 (0.2)      1.00
       (mg)                         0.0 (0.0)         0.0 (1.5)    0.16
       Norepinephrine, No. (%)      164 (16.6)        154 (15.6)   0.55
       (mg)                         0.3 (1.2)         0.2 (1.2)    0.36
       Phenylephrine, No. (%)       232 (23.5)        190 (19.3)   0.02
       (mg)                         0.7 (5.5)         0.5 (4.4)    0.26
       Epinephrine, No. (%)         14 (1.4)          15 (1.5)     0.85
       (mg)                         0.0 (0.7)         0.0 (0.7)    0.37


Use of inotropic drug
       Dobutamine, No. (%)          1 (0.1)           1 (0.1)      1.00
       (mg)                         0.0 (0.9)         0.0 (0.0)    0.32


_________________________________________________________________________
PEEP, positive end-expiratory pressure.




© 2019 American Medical Association. All rights reserved.

- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Every vasoactive/inotropic count/dose/P checked; multiple drugs can occur per participant and doses round to zero; any-use matches main, not a sum of drug counts.

### S094

- **Semantic key:** Anesthetic, analgesic, paralytic and reversal agent comparisons; SUP014.
- **Locations and roles:** REPORT DOC-005 [page 26](../../../joi190055supp4_prod_16092.pdf#page=26).
- **Checks / missing definitions:** Every displayed row/count/percentage/meanSD/dose/P is retained below. Independent-arm comparisons respect participant randomization; where table-level exact test choice/contributor denominator is absent, it remains unreported. Categorical global P values and withinparticipant day/time records are not reinterpreted as row-specific or independent repeated-measures tests. No matched peripheral comparison is promoted.
- **Full printed vector (source-mapped layout):**

### Physical PDF page 26

eTable 5. Types of anesthetic, muscle paralyzing and reversal agents

___________________________________________________________________________
                             High PEEP         Low PEEP          P value
                             n=989             n=987
___________________________________________________________________________

Volatile anesthetics, No.(%)
       Desflurane                   469 (47.4)         468 (47.4)      1.00
       Sevoflurane                  401 (40.5)         411 (41.6)      0.62
       Isoflurane                   40 (4.0)           37 (3.7)        0.73

Intravenous anesthetics, No.(%)
       Propofol                     927 (93.7)         911 (92.3)      0.21
       Midazolam                    278 (28.1)         287 (29.1)      0.63
       Thiopental                   37 (3.7)           40 (4.1)        0.72
       Ketamine                     144 (14.6)         136 (13.8)      0.62
       Etomidate                    7 (0.7)            7 (0.7)         1.00
       Dexmedetomidine              78 (7.9)           79 (8.0)        0.92
       Others                       38 (3.8)           31 (3.1)        0.40

Analgesics, No.(%)
      Morphine                      160 (16.2)         158 (16.0)      0.92
      Alfentanil                    7 (0.7)            8 (0.8)         0.79
      Fentanyl                      539 (54.5)         570 (57.8)      0.15
      Sufentanil                    239 (24.2)         208 (21.1)      0.10
      Remifentanil                  331 (33.5)         339 (34.3)      0.68
      Lidocaine                     320 (32.4)         313 (31.7)      0.76
      Procaine                      2 (0.2)            0 (0.0)         0.48
      NSAIDS                        236 (23.9)         239 (24.2)      0.85
      Others                        308 (31.1)         280 (28.4)      0.18

Muscle paralyzing agents, No.(%)
      Atracurium                    27 (2.7)           24 (2.4)        0.68
      Cis-atracurium                66 (6.7)           51 (5.2)        0.16
      Mivacurium                    1 (0.1)            2 (0.2)         1.00
      Pancuronium                   5 (0.5)            2 (0.2)         0.45
      Vecuronium                    47 (4.8)           48 (4.9)        0.91
      Rocuronium                    847 (85.6)         848 (85.9)      0.86
      Succnylcholine                240 (24.3)         234 (23.7)      0.77
      Others                        4 (0.4)            3 (0.3)         0.71

Reversal of muscle paralysis agents, No.(%)
      Sugammadex                     438 (44.3)        434 (44.0)      0.89
      Cholinesterase inhibitors      290 (29.3)        295 (29.9)      0.78

___________________________________________________________________________
PEEP, positive end-expiratory pressure.



© 2019 American Medical Association. All rights reserved.

- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Every anesthetic/analgesic/paralytic/reversal count, percentage and P checked; overlapping agents are not exclusive partitions, exact sparse test option absent.

### S095

- **Semantic key:** Surgical categories/global tests and laparoscopy pressure; SUP015.
- **Locations and roles:** REPORT DOC-005 [page 27](../../../joi190055supp4_prod_16092.pdf#page=27).
- **Checks / missing definitions:** Every displayed row/count/percentage/meanSD/dose/P is retained below. Independent-arm comparisons respect participant randomization; where table-level exact test choice/contributor denominator is absent, it remains unreported. Categorical global P values and withinparticipant day/time records are not reinterpreted as row-specific or independent repeated-measures tests. No matched peripheral comparison is promoted.
- **Full printed vector (source-mapped layout):**

### Physical PDF page 27

eTable 6. Further characteristics of surgery

___________________________________________________________________________
                             High PEEP         Low PEEP          P value
                             n=989             n=987
___________________________________________________________________________

Priority of surgery, No.(%)
        Elective                   962 (97.8)         958 (97.6)
        Emergency                  13 (1.3)           11 (1.1)     0.64
        Urgent                     9 (0.9)            13 (1.3)

Positioning during surgery, No.(%)
       Supine                      357 (36.2)         367 (37.2)
       Trendelenburg               86 (8.7)           69 (7.0)
       Reverse Trendelenburg       486 (49.3)         491 (49.8)   0.69
       Lithotomy                   17 (1.7)           16 (1.6)
       Seated                      39 (4.0)           43 (4.4)

Surgical wound classification, No.(%)

       Clean                       514 (52.1)         525 (53.2)
       Clean-contaminated          461 (46.8)         450 (45.6)   0.46
       Contaminated                10 (1.0)           7 (0.7)
       Dirty                       1 (0.1)            4 (0.4)

Intra-abdominal pressure during
laparoscopy - (mmHg), mean (SD)
                                    14.7 (3.6) 14.5 (2.1)        0.17
___________________________________________________________________________
PEEP, positive end-expiratory pressure.




© 2019 American Medical Association. All rights reserved.

- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Every surgery-priority/position/wound category and laparoscopy-pressure vector checked; contributor counts are table-specific, category P values are global, not row-wise.

### S096

- **Semantic key:** Postoperative VAS dyspnea/thoracic/abdominalrest/incidentpain across days1–5; SUP016.
- **Locations and roles:** REPORT DOC-005 [page 28](../../../joi190055supp4_prod_16092.pdf#page=28).
- **Checks / missing definitions:** Every displayed row/count/percentage/meanSD/dose/P is retained below. Independent-arm comparisons respect participant randomization; where table-level exact test choice/contributor denominator is absent, it remains unreported. Categorical global P values and withinparticipant day/time records are not reinterpreted as row-specific or independent repeated-measures tests. No matched peripheral comparison is promoted.
- **Full printed vector (source-mapped layout):**

### Physical PDF page 28

eTable 7. Assessment of postoperative pain and dyspnea

___________________________________________________________________________
                        High PEEP        Low PEEP          P value
                        n=989            n=987
___________________________________________________________________________

VAS dyspnea – cm, mean (SD), No.

      Day 1                1.8 (1.5), 912      1.8 (1.4), 917   0.53
      Day 2                1.4 (1.0), 840      1.5 (1.0), 844   0.57
      Day 3                1.4 (0.9), 619      1.3 (0.8), 617   0.68
      Day 4                1.3 (0.9), 461      1.3 (0.8), 459   0.79
      Day 5                1.2 (0.9), 336      1.2 (0.8), 330   0.78

VAS thoracic – cm, mean (SD), No.

      Day 1                1.6 (1.3), 914      1.7 (1.4), 913   0.52
      Day 2                1.3 (0.8), 838      1.4 (3.9), 841   0.34
      Day 3                1.2 (0.6), 620      1.2 (0.6), 617   0.94
      Day 4                1.1 (0.5), 461      1.2 (0.5), 459   0.20
      Day 5                1.1 (0.4), 336      1.1 (0.5), 330   0.16

VAS abdominal rest pain – cm, mean (SD), No.

      Day 1                2.7 (1.8), 950      2.9 (1.9), 958   0.10
      Day 2                2.1 (1.5), 881      2.1 (1.4), 889   0.31
      Day 3                1.8 (1.3), 647      1.8 (1.2), 650   0.94
      Day 4                1.6 (1.2), 469      1.6 (1.0), 475   0.75
      Day 5                1.5 (1.0), 346      1.5 (1.0), 337   0.83

VAS abdominal incident pain – cm, mean (SD), No.

      Day 1                 3.7 (2.4), 916        3.7 (2.3), 929    0.52
      Day 2                 2.8 (2.0), 837        2.9 (1.9), 857    0.51
      Day 3                 2.4 (1.7), 615        2.4 (1.7), 627    0.55
      Day 4                 2.0 (1.5), 458        2.1 (1.5), 459    0.69
      Day 5                 1.9 (1.4), 339        1.9 (1.5), 333    0.58
___________________________________________________________________________
PEEP, positive end-expiratory pressure; VAS, visual analogue scale.




© 2019 American Medical Association. All rights reserved.

- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All 20 day-by-outcome mean/SD/contributor/P vectors revisited; no exact row test is named, rounded summaries do not identify a unique t statistic or repeated-measures covariance.

### S097

- **Semantic key:** Per-protocol primary PPC and all twelve components; SUP017.
- **Locations and roles:** REPORT DOC-005 [page 29](../../../joi190055supp4_prod_16092.pdf#page=29).
- **Checks / missing definitions:** PP is917/912, separate fromITT989/987. All13vectors checked for containment/order/direction. PrimaryP=.17 andCIspan1 support same qualitative inference asITT. EffusionCIexcludes1/P=.01directionconsistent. CardioedemaCI1.02–1.82andP=.09 are from different specified interval/testprocedures; no testvarianceoption inferred. Identitypattern F-ST1-001.
- **Full printed vector (source-mapped layout):**

### Physical PDF page 29

eTable 8. Per-protocol analysis

_______________________________________________________________________________________________________________________
                                                          High PEEP            Low PEEP               Effect Estimate    P value
                                                          n=917                n=912                  95% CI
_______________________________________________________________________________________________________________________
Primary outcome
      Postoperative pulmonary complications               186 / 917 (20.3)     209 / 912 (22.9)       0.92 (0.82 – 1.04) 0.17
              Mild respiratory failure                    119 / 917 (13.0)     140 / 912 (15.4)       0.90 (0.78 – 1.04) 0.15
              Moderate respiratory failure                38 / 917 (4.1)       51 / 912 (5.6)         0.84 (0.66 – 1.07) 0.15
              Severe respiratory failure                  25 / 917 (2.7)       35 / 912 (3.8)         0.83 (0.61 – 1.11) 0.18
              ARDS                                        3 / 917 (0.3)        1 / 912 (0.1)          1.50 (0.84 – 2.64) 0.62
              Bronchospasm                                11 / 917 (1.2)       10 / 912 (1.1)         1.04 (0.69 – 1.57) 0.84
              New pulmonary infiltrates                   14 / 917 (1.5)       14 / 912 (1.5)         0.99 (0.68 – 1.44) 0.99
              Pulmonary infection                         10 / 917 (1.1)       9 / 912 (1.0)          1.05 (0.68 – 1.61) 0.83
              Aspiration pneumonitis                      2 / 917 (0.2)        1 / 912 (0.1)          1.33 (0.59 – 2.96) 1.00
              Pleural effusion                            38 / 917 (4.1)       18 / 912 (2.0)         1.37 (1.14 – 1.65) 0.01
              Atelectasis                                 38 / 917 (4.1)       50 / 912 (5.5)         0.85 (0.67 – 1.09) 0.18
              Cardiopulmonary edema                       15 / 917 (1.6)       7 / 912 (0.8)          1.36 (1.02 – 1.82) 0.09
              Pneumothorax                                1 / 917 (0.1)        2 / 912 (0.2)          0.66 (0.13 – 3.29) 0.62
_______________________________________________________________________________________________________________________
PEEP, positive end-expiratory pressure; CI, confidence interval; ARDS, acute respiratory distress syndrome.




© 2019 American Medical Association. All rights reserved.

- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All 13 PP event/estimate/CI/P vectors checked on 917/912; generic effect label retained. .17 null result agrees qualitatively with ITT; cardiopulmonary interval/P pair not assumed to share a test.

### S098

- **Semantic key:** Primary-outcome random-effect, count, common/average/interaction GEE sensitivity; SUP018.
- **Locations and roles:** REPORT DOC-005 [page 30](../../../joi190055supp4_prod_16092.pdf#page=30).
- **Checks / missing definitions:** Allfive sensitivity comparisons, summary dispersion and complete footnotes retained. Site-randomeffect .86(.68,1.08),P.19; proportionalodds .88(.72,1.09) withWilcoxonP.25; commonGEE .93(.80,1.08),P.37; heterogeneityP.11; averagedGEE .99(.94,1.05),P.98. Different countCI/Pmethods expressly disclosed. Averageeffect transformation and interval/test covariance notdefined, so Wald diagnostic is not asserted as contradiction.
- **Full printed vector (source-mapped layout):**

### Physical PDF page 30

eTable 9. Sensitivity analysis for the primary outcome

_______________________________________________________________________________________________________________________
                                               High PEEP         Low PEEP          Odds ratio             P value
                                               n=989             n=987             95% CI

Random-effect model                                                 —                         —                         0.86 (0.68 – 1.08)*       0.19
Count events                                                        0.35 (0.88)               0.38 (0.86)
   Median (IQR)                                                     0 (0 – 0)                 0 (0 – 0)                 0.88 (0.72 – 1.09)£       0.25
Common effect GEE                                                   —                         —                         0.93 (0.80 – 1.08)¥       0.37
Treatment-component interaction GEE                                 —                         —                         —                         0.11**
Average relative effect GEE                                         —                         —                         0.99 (0.94 – 1.05)££      0.98
PEEP: positive end expiratory pressure; IQR: interquartile range; GEE: generalized estimating equations
* 95% confidence intervals and p values calculated in a mixed-effect model with study sites as random-effects
£ 95% confidence intervals calculated with proportional odds logistic regression and p values calculated Wilcoxon rank-sum test
¥ 95% confidence intervals and p values calculated in a common effect GEE model (estimating a single treatment effect across all 12 components)
** p value calculated in a GEE model (test whether the treatment effect differs across the 12 components)
££ p value calculated in a GEE model (estimating, then averaging, the 12 distinct treatment effects)




© 2019 American Medical Association. All rights reserved.

- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All five sensitivity comparisons, count summaries and footnotes revisited; site/GEE model estimates not forced to crude ratios. Average .99(.94,1.05), .98 lacks specified common test construction.

### S099

- **Semantic key:** Observed display of sequential monitoring design; same plannedruleS085.
- **Locations and roles:** REPORT DOC-005 [page31](../../../joi190055supp4_prod_16092.pdf#page=31); PLAN DOC-002p22–23;PLAN DOC-003p2–3.
- **Full printed and graphical vector:**

### SUP019 — eFigure1, physical page31

X: Enrollment956,1434,1912; numbers exclude dropouts. Y: Effect Size(Z), ticks−4 through4 by1. Blue upper region “Harm”, blue lower “Efficacy”, central pink “Futility”. Plotted harm thresholds approximately2.75,2.4,2.0; efficacy thresholds approximately−2.75,−2.4,−2.0; futility limits approximately±0.2,±0.9,±2.0 at the three respective enrollment points. These are graph-position estimates (roughly±0.1Z); no exact numeric boundary table is printed on this page. Graph displays boundaries, not a separate observed trial Z trajectory.


- **Checks / missing definitions:** Graph is design boundaries, not observedZtrajectory. Exact protocol magnitudesZ2.75,2.432,2.012 andfutility.225,.929,2.012 match plottedapproximately±.1Z. Harmabove0/efficacybelow0 followsH−Lsign. No observed lookdecision is derived from plottedboundarylines.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All plotted monitoring boundaries agree with exact planned magnitudes within graph precision; plot is design, not observed Z trajectory.

### S100

- **Semantic key:** Tidal volume five-timegroupinteraction; SUP20.
- **Locations and roles:** REPORT DOC-005 [page32](../../../joi190055supp4_prod_16092.pdf#page=32); matching MAIN45vector atmainp7 retained above.
- **Full vector:** | SUP020/p32 | Tidal Volume(ml/kg PBW),6–10 by1 | 0.081 | H7.23,7.24,7.20,7.15,7.30; L7.13,7.10,7.12,7.13,7.15 | H0.09,0.08,0.08,0.07,0.10; L0.04,0.03,0.04,0.04,0.05 |
- **Keys/checks/missing definitions:** Open/dashedLow,filled/solidHigh; orderedtimesAfterIntubation,1st,2nd,3th,LastHour; pointsmean,bars95%CI. DisplayedP tests time×group in mixed-effectlinearmodel, not separatetimepointarmcontrast. Graphicalmeans/halfwidths are diagnostics at resolutions~.05mL/kg, .2/.3cmH2O,.1%SpO2,.5%FiO2. Allbarorder/pointcontainment/direction visually inspected; exactcoordinates/contributors/covariance notprinted. Differences frommainpointtestsorfractionalFiO2do not identify inconsistentanalysis. Drivingpressure=plateau−PEEP;peakpressure is separatelymeasured.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All five tidal-volume time means/bars and .081 time-by-group P revisited; bar containment/order and unit/reference conventions coherent, not single-time-point tests.

### S101

- **Semantic key:** PEEP five-timegroupinteraction; SUP21.
- **Locations and roles:** REPORT DOC-005 [page33](../../../joi190055supp4_prod_16092.pdf#page=33); matching MAIN46vector atmainp7 retained above.
- **Full vector:** | SUP021/p33 | PEEP(cmH2O),0,5,10,15 | <0.001 | H11.5,12.0,12.05,12.05,12.1; L4.0,4.05,4.05,4.10,4.10 | H0.2,0.1,0.1,0.1,0.1; Labout0.05–0.1 each |
- **Keys/checks/missing definitions:** Open/dashedLow,filled/solidHigh; orderedtimesAfterIntubation,1st,2nd,3th,LastHour; pointsmean,bars95%CI. DisplayedP tests time×group in mixed-effectlinearmodel, not separatetimepointarmcontrast. Graphicalmeans/halfwidths are diagnostics at resolutions~.05mL/kg, .2/.3cmH2O,.1%SpO2,.5%FiO2. Allbarorder/pointcontainment/direction visually inspected; exactcoordinates/contributors/covariance notprinted. Differences frommainpointtestsorfractionalFiO2do not identify inconsistentanalysis. Drivingpressure=plateau−PEEP;peakpressure is separatelymeasured.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All five PEEP means/bars and <.001 interaction checked; higher-arm direction and graph precision coherent with corresponding main values.

### S102

- **Semantic key:** Peak pressure five-timegroupinteraction; SUP22.
- **Locations and roles:** REPORT DOC-005 [page34](../../../joi190055supp4_prod_16092.pdf#page=34); matching MAIN48vector atmainp7 retained above.
- **Full vector:** | SUP022/p34 | Peak Pressure(cmH2O),15–35 by5 | <0.001 | H26.0,28.0,28.2,28.3,27.5; L23.3,26.4,26.8,27.2,26.1 | H0.3,0.3,0.3,0.5,0.3; L0.3,0.3,0.4,0.5,0.4 |
- **Keys/checks/missing definitions:** Open/dashedLow,filled/solidHigh; orderedtimesAfterIntubation,1st,2nd,3th,LastHour; pointsmean,bars95%CI. DisplayedP tests time×group in mixed-effectlinearmodel, not separatetimepointarmcontrast. Graphicalmeans/halfwidths are diagnostics at resolutions~.05mL/kg, .2/.3cmH2O,.1%SpO2,.5%FiO2. Allbarorder/pointcontainment/direction visually inspected; exactcoordinates/contributors/covariance notprinted. Differences frommainpointtestsorfractionalFiO2do not identify inconsistentanalysis. Drivingpressure=plateau−PEEP;peakpressure is separatelymeasured.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All five peak-pressure means/bars and <.001 interaction checked; no covariance reconstructed or peak substituted for plateau in driving pressure.

### S103

- **Semantic key:** SpO2 five-timegroupinteraction; SUP23.
- **Locations and roles:** REPORT DOC-005 [page35](../../../joi190055supp4_prod_16092.pdf#page=35); matching MAIN52vector atmainp7 retained above.
- **Full vector:** | SUP023/p35 | SpO2(%),90–100 by1 | <0.001 | H98.2,97.9,98.1,98.3,98.3; L97.5,96.6,96.9,97.1,97.1 | H0.1,0.1,0.1,0.15,0.15; L0.15,0.15,0.15,0.2,0.2 |
- **Keys/checks/missing definitions:** Open/dashedLow,filled/solidHigh; orderedtimesAfterIntubation,1st,2nd,3th,LastHour; pointsmean,bars95%CI. DisplayedP tests time×group in mixed-effectlinearmodel, not separatetimepointarmcontrast. Graphicalmeans/halfwidths are diagnostics at resolutions~.05mL/kg, .2/.3cmH2O,.1%SpO2,.5%FiO2. Allbarorder/pointcontainment/direction visually inspected; exactcoordinates/contributors/covariance notprinted. Differences frommainpointtestsorfractionalFiO2do not identify inconsistentanalysis. Drivingpressure=plateau−PEEP;peakpressure is separatelymeasured.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All five SpO2 means/bars and <.001 interaction checked; higher-arm direction coherent; exact graph coordinates/contributors unprinted.

### S104

- **Semantic key:** Driving pressure five-timegroupinteraction; SUP24.
- **Locations and roles:** REPORT DOC-005 [page36](../../../joi190055supp4_prod_16092.pdf#page=36); matching MAIN49vector atmainp7 retained above.
- **Full vector:** | SUP024/p36 | Driving Pressure(cmH2O),5,10,15,20 | <0.001 | H11.3,12.2,12.3,12.2,11.8; L15.4,17.9,18.0,18.0,17.4 | H0.3,0.3,0.3,0.4,0.3; L0.3,0.35,0.35,0.5,0.35 |
- **Keys/checks/missing definitions:** Open/dashedLow,filled/solidHigh; orderedtimesAfterIntubation,1st,2nd,3th,LastHour; pointsmean,bars95%CI. DisplayedP tests time×group in mixed-effectlinearmodel, not separatetimepointarmcontrast. Graphicalmeans/halfwidths are diagnostics at resolutions~.05mL/kg, .2/.3cmH2O,.1%SpO2,.5%FiO2. Allbarorder/pointcontainment/direction visually inspected; exactcoordinates/contributors/covariance notprinted. Differences frommainpointtestsorfractionalFiO2do not identify inconsistentanalysis. Drivingpressure=plateau−PEEP;peakpressure is separatelymeasured.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All five driving-pressure means/bars and <.001 interaction checked; lower-H direction consistent with plateau−PEEP definition and main.

### S105

- **Semantic key:** FiO2 five-timegroupinteraction; SUP25.
- **Locations and roles:** REPORT DOC-005 [page37](../../../joi190055supp4_prod_16092.pdf#page=37); matching MAIN51vector atmainp7 retained above.
- **Full vector:** | SUP025/p37 | FiO2(%),30–70 by10 | <0.001 | H57.8,45.7,45.5,45.5,46.3; L56.8,48.6,49.1,49.5,50.0 | H1.4,0.6,0.6,0.8,0.7; L1.3,0.7,0.8,1.0,0.8 |
- **Keys/checks/missing definitions:** Open/dashedLow,filled/solidHigh; orderedtimesAfterIntubation,1st,2nd,3th,LastHour; pointsmean,bars95%CI. DisplayedP tests time×group in mixed-effectlinearmodel, not separatetimepointarmcontrast. Graphicalmeans/halfwidths are diagnostics at resolutions~.05mL/kg, .2/.3cmH2O,.1%SpO2,.5%FiO2. Allbarorder/pointcontainment/direction visually inspected; exactcoordinates/contributors/covariance notprinted. Differences frommainpointtestsorfractionalFiO2do not identify inconsistentanalysis. Drivingpressure=plateau−PEEP;peakpressure is separatelymeasured.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All five FiO2 percent means/bars and <.001 interaction checked; percent/fraction conversion retained, graphical diagnostic precision and time-model distinction respected.

### S106

- **Semantic key:** Primary PPC time-to-event; SUP26.
- **Locations and roles:** REPORT DOC-005 [page38](../../../joi190055supp4_prod_16092.pdf#page=38); Coxspecification mainp4.
- **Full vector:** | SUP026/p38 | Proportion of Patients with Postoperative Pulmonary Complications;0–0.25 by0.05 | 21.3%;23.6% | 0.88(0.73–1.06),0.190 | 0.05 | L987,987,791,767,760,756; H989,989,827,797,788,785 |
- **Keys/checks/missing definitions:** BlueLow/redHigh; time0–5days; highrelative tolowHR95%CI; medianfollow-up4(2–5). Containment,endpointorder,HRandcurvedirection reviewed. HRnotincidenceRR; namedPHdiagnostic is not an effectP. Risk-tablecounts are preserved exactly and are not used to invent censoring/eventtimes. SchoenfeldP=.05doesnotstatePHrejectionandroundingcanstraddlethreshold; nogeneraldesigncritique. Confidence/test compatibility beyond printed method cannot be mechanically reconstructed without eventtimes/variance; no Waldtest inferred.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Primary HR .88(.73,1.06), .190, occurrence curves and full risk table checked; PH .05 is separately named, rounded threshold does not establish a contradicted decision.

### S107

- **Semantic key:** Severe PPC time-to-event; SUP27.
- **Locations and roles:** REPORT DOC-005 [page39](../../../joi190055supp4_prod_16092.pdf#page=39); Coxspecification mainp4.
- **Full vector:** | SUP027/p39 | Proportion of Patients with Severe Postoperative Pulmonary Complications;0–0.15 by0.05 | 11.7%;13.6% | 0.85(0.66–1.09),0.197 | 0.28 | L987,987,791,767,760,756; H989,989,827,797,788,785 |
- **Keys/checks/missing definitions:** BlueLow/redHigh; time0–5days; highrelative tolowHR95%CI; medianfollow-up4(2–5). Containment,endpointorder,HRandcurvedirection reviewed. HRnotincidenceRR; namedPHdiagnostic is not an effectP. Risk-tablecounts are preserved exactly and are not used to invent censoring/eventtimes.  Confidence/test compatibility beyond printed method cannot be mechanically reconstructed without eventtimes/variance; no Waldtest inferred.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Severe PPC HR .85(.66,1.09), .197, occurrence proportions, full risk table and PH .28 checked; no incidence-RR or event-time equivalence imposed.

### S108

- **Semantic key:** Extrapulmonary complications time-to-event; SUP28.
- **Locations and roles:** REPORT DOC-005 [page40](../../../joi190055supp4_prod_16092.pdf#page=40); Coxspecification mainp4.
- **Full vector:** | SUP028/p40 | Proportion of Patients with Postoperative Extra-Pulmonary Complications;0–0.20 by0.05 | 16.9%;15.2% | 1.12(0.89–1.39),0.314 | 0.67 | L987,987,898,873,852,845; H989,989,896,861,834,828 |
- **Keys/checks/missing definitions:** BlueLow/redHigh; time0–5days; highrelative tolowHR95%CI; medianfollow-up4(2–5). Containment,endpointorder,HRandcurvedirection reviewed. HRnotincidenceRR; namedPHdiagnostic is not an effectP. Risk-tablecounts are preserved exactly and are not used to invent censoring/eventtimes.  Confidence/test compatibility beyond printed method cannot be mechanically reconstructed without eventtimes/variance; no Waldtest inferred.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Extrapulmonary HR 1.12(.89,1.39), .314, proportions, full risk table and PH .67 checked; direction coherent on its distinct time-to-event scale.

### S109

- **Semantic key:** Five-day mortality time-to-event; SUP29.
- **Locations and roles:** REPORT DOC-005 [page41](../../../joi190055supp4_prod_16092.pdf#page=41); Coxspecification mainp4.
- **Full vector:** | SUP029/p41 | 5-Day Mortality;0–0.005 by0.001 | 0.5%;0.3% | 1.67(0.40–6.97),0.484 | 0.14 | L987,987,987,987,986,986; H989,989,988,987,985,985 |
- **Keys/checks/missing definitions:** BlueLow/redHigh; time0–5days; highrelative tolowHR95%CI; medianfollow-up4(2–5). Containment,endpointorder,HRandcurvedirection reviewed. HRnotincidenceRR; namedPHdiagnostic is not an effectP. Risk-tablecounts are preserved exactly and are not used to invent censoring/eventtimes. Probabilityofdeath/5-DayMortalityaxes,HRcaption,events5/3andmortality mainvector resolve literalcaption'extra-pulmonarycomplications' at once; terminology excluded. Confidence/test compatibility beyond printed method cannot be mechanically reconstructed without eventtimes/variance; no Waldtest inferred.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Mortality HR 1.67(.40,6.97), .484, 5/3 events, full risk table and PH .14 checked; mortality axes/event vector resolve isolated extra-pulmonary caption wording.

### S110

- **Semantic key:** All twelve individualcomponentBonferroniGLMintervals andallfourglobal95%effectintervals; SUP030.
- **Locations and roles:** REPORT DOC-005 [page42](../../../joi190055supp4_prod_16092.pdf#page=42); PLAN DOC-004p3; REPORT mainTable3pp9–10.
- **Full printed vector:**

### SUP030 — eFigure12, physical page42

[Forest plot](../../../joi190055supp4_prod_16092.pdf#page=42). Header “Postoperative Pulmonary Complications”; component header “Risk Ratio(99.58%CI)”. Exact printed vector:

| Component | Risk ratio | 99.58%CI |
|---|---:|---|
| Mild Respiratory Failure | 0.92 | 0.76–1.12 |
| Moderate Respiratory Failure | 0.83 | 0.59–1.17 |
| Severe Respiratory Failure | 0.91 | 0.61–1.34 |
| Aspiration | 1.33 | 0.41–4.30 |
| Bronchospasm | 1.09 | 0.62–1.91 |
| ARDS | 1.50 | 0.65–3.44 |
| Pulmonary Infection | 1.00 | 0.52–1.90 |
| Atelectasis | 0.88 | 0.64–1.23 |
| Cardiopulmonary Edema | 1.31 | 0.87–1.98 |
| Pleural Effusion | 1.36 | 1.05–1.76 |
| Pneumothorax | 0.50 | 0.04–5.96 |
| Pulmonary Infiltrates | 0.87 | 0.49–1.55 |

Separate “Global Tests” block header “Odds Ratio(95%CI)”:

| Analysis label | Displayed odds ratio | 95%CI |
|---|---:|---|
| Collapsed Composite | 0.93 | 0.83–1.04 |
| Count(Proportional Odds) | 0.88 | 0.72–1.09 |
| Common Effect GEE | 0.93 | 0.80–1.08 |
| Average Relative Effect GEE | 0.99 | 0.94–1.05 |

No P values or contributor counts appear on this forest plot. X ticks0.50,1.00,1.50,2.00,2.50,3.00, intermediate minor ticks; dotted reference at1.00. Left Favours High PEEP/right Favours Low PEEP. Aspiration and pneumothorax CIs use off-scale arrowheads at the right; pneumothorax also extends below the left plotting limit. Component squares and global diamonds represent displayed estimates/intervals. Caption expands CI,ARDS,GEE,PEEP. The forest plot confidence levels are distinct for components and global tests; they are retained explicitly.


- **Checks / missing definitions:** All16estimatescontainedinorderedintervals;favorableaxes consistent withreferenceH/L. Aspiration/pneumothoraxoffscaleextensionsretaintrueprintedlimits. Confidencelevel99.58%for12components distinct from95%globalanalyses, matchingSAPBonferroni1−.05/12. No Pprinted. Componentpointdifferences .90vs.91, .99vs1.00,1.35vs1.36are differentGLM/intervalprocedures; no forcedequality. Collapsedcomposite .93(.83,1.04) matches mainRRvector but sits underOddsRatioheader: F-ST1-002. OtherglobalORlabels correspond theirnamedGEE/proportionaloddsmodels; no generic'relative effect' estimator supplied byconvention.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. All 12 Bonferroni component and four global intervals checked for containment/order/direction. Global collapsed-composite OR label remains C001; separate GLM component estimates not forced to crude ratios.

### S111

- **Semantic key:** Historical ARISCAT derivation used to define trial eligibility; all bivariate/multivariate ORs, coefficients and scores.
- **Locations and roles:** PLAN DOC-002 [Appendix i, page29](../../../joi190055supp1_prod_16092.pdf#page=29); REPORT DOC-005 [eTable1, page22](../../../joi190055supp4_prod_16092.pdf#page=22). These are historical derivation results, not PROBESE randomized effects. Bivariate n1627; multivariate n1624; eligibility threshold ARISCAT≥26.
- **Full vector:** Multivariate vectors below are repeated in the report supplement; baseline categories have reference1 and no displayed coefficient/score.

| Predictor | Bivariate OR (95% CI) | Multivariate OR (95% CI) | β | Score |
|---|---|---|---:|---:|
| Age≤50 y | 1 | 1 | not printed | not printed |
| Age51–80 y | 3.1(1.5–6.7) | 1.4(.6–3.3) | .331 | 3 |
| Age>80 y | 8.8(3.8–20.3) | 5.1(1.9–13.3) | 1.619 | 16 |
| SpO2≥96% | 1 | 1 | not printed | not printed |
| SpO2 91–95% | 3.1(1.8–5.3) | 2.2(1.2–4.2) | .802 | 8 |
| SpO2≤90% | 15.2(7.2–32.5) | 10.7(4.1–28.1) | 2.375 | 24 |
| Respiratory infection last month | 6.1(3.4–11.1) | 5.5(2.6–11.5) | 1.698 | 17 |
| Preop anemia≤10g/dL | 4.4(2.4–8.01) | 3.0(1.4–6.5) | 1.105 | 11 |
| Peripheral incision | 1 | 1 | not printed | not printed |
| Upper abdominal | 6.9(4.0–11.9) | 4.4(2.3–8.5) | 1.480 | 15 |
| Intrathoracic | 16.9(8.4–34.1) | 11.4(4.9–26.0) | 2.431 | 24 |
| Duration≤2h | 1 | 1 | not printed | not printed |
| Duration>2–3h | 6.1(3.2–11.3) | 4.9(2.4–10.1) | 1.593 | 16 |
| Duration>3h | 11.2(6.3–20.1) | 9.7(4.7–19.9) | 2.268 | 23 |
| Emergency | 2.1(1.2–3.7) | 2.2(1.04–4.5) | .768 | 8 |

- **Checks / missing definitions:** Every nonreference point is contained in its ordered95% interval. Coefficients reconcile with log odds ratios within displayed precision. The report score rule is ten times the coefficient, rounded to an integer; all displayed scores follow that rule. Protocol and report multivariate vectors match. Individual-model P values/test statistics/variance are not supplied. Historical analysis is not used to infer the randomized intervention effect or evaluate a preferred risk model.
- **Pass 1:** PASS_1_COMPLETE.
- **Pass 2:** PASS_2_COMPLETE; fresh runtime `/root/statistical_pass_2`. Every historical bivariate/multivariate OR, CI, coefficient and score revisited; ordered containment, exp-coefficient/display precision and ten-times-coefficient integer scores reconcile.



