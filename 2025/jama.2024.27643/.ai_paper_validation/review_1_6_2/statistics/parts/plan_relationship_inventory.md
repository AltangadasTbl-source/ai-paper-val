# Statistical relationship inventory — plan shard

Runtime agent: /root/statistical_pass_1_plan. Model gpt-6.1-sol; reasoning effort high; fresh spawn. Exact disjoint scope: PLAN DOC-002 PDF pages1–229 and PLAN DOC-003 pages1–65, excluding all REPORT relationships and DOC-003 pages66–130. All assigned source units were covered via current complete mapper artifacts plus targeted direct-source confirmation. No old scientific conclusions or web sources were read. Every relationship below is PASS_1_COMPLETE; a distinct fresh pass2 agent must revisit each stable ID.

Mandatory scope/contract read completely. Mapper support-001/002/003 read completely; support-004 full summary and numeric-display section read, with exact source appendix and fresh layouts for statistical sections. All figures54,55,58,59,60 visually inspected. No OCR was required. New derivatives: bundled pdf_tools.py, user /home/juliz/venvs/stt/bin/python, PyMuPDF1.28.0, layout(sorted native reading order), CPU. Files preprocessing/statistics-1-plan/doc002-60-65.txt, doc003-8-30.txt, doc003-32-53.txt. Reused/new mapper evidence remains unchanged; source final authority.

Numbers and coefficients in the records retain supplied precision; compact repeated versions share a record. Tests that reconcile are relationship checks, not excluded observations. Relationship types/review domains apply to future findings; all compared source locations here have PLAN role. There are zero emitted findings from this disjoint PLAN-only scope. Plan/report comparisons are assigned elsewhere, and are not silently decided here. Missing virtual participant data and random seeds prevent independent stochastic replication; no sample-size contradiction is reproduced.

### S201 — Plan precedence and applicability

- **Locations and roles:** PLAN DOC-002 pp60–65; DOC-003 p8,p63.
- **Printed relationship:** Master Appendix I takes precedence over protocol statistical recommendations; R-SAP supersedes master. Master v3 explicitly applies to RSAs initiated after Feb2023; regimen C cover instead names Master v1 of24Jun2020. Version differences are prospective amendments, not automatic plan conflicts.
- **Pass 1 check:** Applicability checked before comparisons. No governing version inferred from bundle order.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S202 — Allocation and planned sample size

- **Locations and roles:** PLAN DOC-002 pp12,17–18,34,60,92,114–115,163,186,188.
- **Printed relationship:** 3:1 active/placebo;160=120+40; pooled120 active comprises60 at30mg and60 at60mg. Two-stage equal regimen then within-regimen randomization.
- **Pass 1 check:** 160×3/4=120 and120/2=60; no discrepancy. Illustrative650 screened/500 eligible are examples.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S203 — Primary endpoint and population-level effect

- **Locations and roles:** PLAN DOC-002 pp12,25,60,112,184; DOC-003 pp13,18,33–36.
- **Printed relationship:** 24-week ALSFRS-R total progression plus death/death-equivalent, Bayesian shared parameter DRR active/placebo; DRR<1 indicates slowing.
- **Pass 1 check:** Endpoint, contrast and direction agree; shared DRR is not a crude change ratio.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S204 — Death/PAV definition and observation window

- **Locations and roles:** PLAN DOC-002 pp60,64,95,166; DOC-003 p15,34–36.
- **Printed relationship:** PAV>22h/day for>7consecutive days, event first day; primary survival through week24/window or last known alive; ascertainment repeated LPLV beyond primary window.
- **Pass 1 check:** Observation extension is distinguished from primary-analysis horizon; no inferential conflict.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S205 — Shared controls and concurrency

- **Locations and roles:** PLAN DOC-002 pp61–62,137,212; DOC-003 pp17,34–35.
- **Printed relationship:** Regimen and other-regimen placebo; concurrent180days before first and after last focal randomization;180day=6month operational window. Later master allows nonconcurrent controls/RSA restrictions.
- **Pass 1 check:** Month12–24 focal example becomes6–30 controls. Eligibility subsets are conditional/prespecified; no count inferred.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S206 — FAS and ongoing participants

- **Locations and roles:** PLAN DOC-002 pp32,35,61,63; DOC-003 pp17–18,34–35.
- **Printed relationship:** As randomized, off-drug observations retained; non-ALS excluded in later master; final ongoing<24elapsed weeks excluded but interim uses ongoing data.
- **Pass 1 check:** Interim/final population distinctions explicitly supported; no observed analysis-size calculation supplied.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S207 — ECC

- **Locations and roles:** PLAN DOC-003 p17.
- **Printed relationship:** FAS subset within180day window before first and after last focal randomization, exclusive.
- **Pass 1 check:** Window supports concurrency; no reported count assigned to this plan-only record.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S208 — ERO and ECM

- **Locations and roles:** PLAN DOC-003 p17.
- **Printed relationship:** ERO=focal-only; ECM=same route of administration; Bayesian sensitivity variants Appendix I pp42–43.
- **Pass 1 check:** Population definitions complete; report implementation assigned to other checker shard.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S209 — EPP

- **Locations and roles:** PLAN DOC-002 pp122,196; DOC-003 p17.
- **Printed relationship:** Initiated treatment; regimen protocol adherence80–120%; as treated; event-dependent truncation per R-SAP, placebo borrowing adherence handled separately.
- **Pass 1 check:** No preference imposed. Missing regimen details explicitly deferred to governing R-SAP.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S210 — Safety population STF/STN/SRO

- **Locations and roles:** PLAN DOC-002 pp64–65; DOC-003 pp17–18.
- **Printed relationship:** Initiators as treated; STF eligible shared placebo, STN same mode, SRO focal-only; off-drug safety follow-up retained.
- **Pass 1 check:** Safety denominator differs by defined population, not by unexplained relabeling.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S211 — Repeat participants

- **Locations and roles:** PLAN DOC-002 pp43,63.
- **Printed relationship:** New randomization/new baseline and observation set; cross-regimen sets conditionally independent given baseline including prebaseline ALSFRS slope; washout max30days/5half-lives.
- **Pass 1 check:** Choice stated coherently; no raw participant audit or preferred model proposed.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S212 — Pooled doses and dose-specific support

- **Locations and roles:** PLAN DOC-002 pp63,92,163; DOC-003 p33.
- **Printed relationship:** Primary pooled active doses versus shared controls; dose-specific secondary/supportive analyses prescribed by R-SAP.
- **Pass 1 check:** No multiplicity rule inferred for dose-specific tests from convention.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S213 — Interim eligibility and schedule

- **Locations and roles:** PLAN DOC-002 pp27,61,63,92,137,163,212; DOC-003 pp19,40–41.
- **Printed relationship:** 40 randomized with24-week opportunity;30active10control by3:1; first eligible platform regimen then approximately12week global intervals; final after all focal opportunity24weeks.
- **Pass 1 check:** 40×.75=30 and×.25=10; schedule matches recommended design.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S214 — Success rule

- **Locations and roles:** PLAN DOC-002 pp63,137,212; DOC-003 pp19,41.
- **Printed relationship:** Default no early-success interim; final P(DRR<1)>.979, calibrated one-sided typeI .025; regimen appendix explicitly no early success.
- **Pass 1 check:** Success distinguished from95%credible interval exclusion. Calibration exception slower focal progression explicitly disclosed.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S215 — Futility rule

- **Locations and roles:** PLAN DOC-002 p64; DOC-003 p41.
- **Printed relationship:** P(DRR<.9)<.05;<.9 corresponds at least10%slowing; nonbinding in protocol.
- **Pass 1 check:** Direction and margin coherent; estimatedDRR is not itself an automatic boundary.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S216 — Secondary multiplicity

- **Locations and roles:** PLAN DOC-003 pp12,19.
- **Printed relationship:** Gate on significant primary; upperHHD+grip→SVC→lowerHHD→death/PAV default, two-sidedP<.05; no lower significance after first failure; nominalP also reported.
- **Pass 1 check:** Sequential rule explicitly stated. No unsupported familywise/global-null critique.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S217 — Missing data

- **Locations and roles:** PLAN DOC-002 pp62,64; DOC-003 pp12–13,18,43.
- **Printed relationship:** Baseline last pre-treatment observation; covariate mean after transform; substitute nearest missing visit maintaining sequence; MAR otherwise; mortality via joint model; no primary imputation.
- **Pass 1 check:** Death handling distinguished from MAR nonmortality. Sensitivities do not contradict primary no-imputation rule.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S218 — ALSFRS-R scale and prebaseline slope

- **Locations and roles:** PLAN DOC-002 pp51,73–75; DOC-003 pp13–14.
- **Printed relationship:** 12×0–4=0–48; higher better; four3item domains0–12; deltaFRS=(48−baseline)/monthssinceweakness withdays×12/365.25.
- **Pass 1 check:** Alternate5a/5b is oneitem; score totals and change directions reconcile.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S219 — SVC transformation

- **Locations and roles:** PLAN DOC-002 pp41,52; DOC-003 p14.
- **Printed relationship:** Maximum3–5attempts (master SAP allows minimum2 or singlelab slow/forced); percent predicted GLI sex/age/height/ethnicity; higherbetter.
- **Pass 1 check:** Operational protocol vs SAP measurement details not turned into population-specific numeric conflict absent reliance.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S220 — HHD and grip scale

- **Locations and roles:** PLAN DOC-002 p52; DOC-003 pp14–15,24.
- **Printed relationship:** 11bilateral muscles plus bilateralgrip=24; average percentchange among initially nonzero; upper/lower/global; HHD0/0[2] composites with death-equivalent.
- **Pass 1 check:** 24=2×12. Zero handling and interval censoring stated; no crude/model comparison.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S221 — Endpoint hierarchy within plan

- **Locations and roles:** PLAN DOC-002 pp112–113,184–185; DOC-003 p13.
- **Printed relationship:** Primary function/survival; secondary SVC,HHD/grip,survival; safetyTEAE,labs,ECG,suicidality; exploratory voice,≥6pointdecline,biomarkers,PRO/homeFVC.
- **Pass 1 check:** Repeated protocol versions preserve endpoint statuses; within assigned plan no conflicting clinical result.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S222 — PK/PD interim and separate plans

- **Locations and roles:** PLAN DOC-002 pp135–136,210–211.
- **Printed relationship:** First40riluzole users reachingweek8 reviewed usingweek4/8active/placeboPK; AuPK/PD separateplans.
- **Pass 1 check:** Not efficacy interim40/24weeks; no threshold/test supplied. Distinct purpose resolves apparent timing conflict.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S223 — Repeated-measures model

- **Locations and roles:** PLAN DOC-003 pp19–21.
- **Printed relationship:** Visit,treatment,treatment×visit plus6covariates andcovariate×visit; unstructured withinparticipant;>3regimens randomintercept,≤3fixed; REML.
- **Pass 1 check:** Model terms/prose/code agree apart from equation's compressed intercept notation; SAS includes intercept.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S224 — Week24 repeated-measures contrast

- **Locations and roles:** PLAN DOC-003 p20.
- **Printed relationship:** Visitorder0,8,16,24; controlfirstactive last; estimate coefficients1,0,0,−1,−1,0,0,1;95%Wald.
- **Pass 1 check:** Contrast=(active24−active0)−(placebo24−placebo0); positive favors higher-retention outcomes.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S225 — Random-slopes model

- **Locations and roles:** PLAN DOC-003 pp21–23.
- **Printed relationship:** Participant/regimen randomintercept+slope unstructured;6covariates plus×month;>3regimensrandomelsefixed;days×12/365.25;95%Wald slopedifference.
- **Pass 1 check:** Currentmaster p22 code omits treatmentmain whileprose/equationinclude. Not tied to report's governing master v1; excluded PERIPHERAL_COMPARISON, not a preference.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S226 — Survival tests and HR intervals

- **Locations and roles:** PLAN DOC-003 p23.
- **Printed relationship:** KM andlog-rank;≥1eventeacharm Cox;profilelikelihood bounds,adjusted age+6covariates;gammafrailty dropped≤3regimens/nonconvergence.
- **Pass 1 check:** Different log-rank/Cox adjustments acknowledged. No common-estimand interval/P conflict in these plan instructions.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S227 — CAFS joint rank

- **Locations and roles:** PLAN DOC-002 p64; DOC-003 pp23–24,42.
- **Printed relationship:** Pairwise survivalwhenorderknownelse functionatmaxcommon followup;−1/0/+1;Wilcoxon t oradjustedmixed;death/PAVvsdeathalone×4function measures.
- **Pass 1 check:** Ordinal joint-rank estimand distinguished from rateDRR. Full2×4×2variant family mapped; source-coherent.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S228 — Interval-censored HHD0 and0[2]

- **Locations and roles:** PLAN DOC-003 p24.
- **Printed relationship:** NPMLE andCox acrossfive efficacysets;6covariates;all24bilateralmeasurements vs4mostfrequentlyzero groups(up to8).
- **Pass 1 check:** Discrete visit observation intervals support stated method; no independence/continuous-event assumption imposed.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S229 — Placebo multiple imputation

- **Locations and roles:** PLAN DOC-003 pp24–25.
- **Printed relationship:** FAS/ERO;ALSFRS/HHDupper/SVC/HHDlower;50imputations fromearliervisit placebo regressions adjusted6covariates;0–48ALSFRS,other≥0.
- **Pass 1 check:** SAScode/priorvisits/regression source match;4measure×2model×2population family mapped. No claim that50reproduces raw results.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S230 — Robust and exponential-tilting sensitivities

- **Locations and roles:** PLAN DOC-003 p25.
- **Printed relationship:** FAS randomslopes samefixed/random;smoothedHuber95%normal asymptoticefficiency;death+24weekALSFRS composite exponentialtilting benefit/harm weights.
- **Pass 1 check:** 95%efficiency is not a confidence level. Missing weight grid not a finding without printed conflict.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S231 — Subgroup interactions

- **Locations and roles:** PLAN DOC-003 pp25–26.
- **Printed relationship:** Age65,sex,race>5%,ethnicity,3drugs,BMI25/30,CKD90/60,median deltaFRS/NfL,onset18,ElEscorial/onset,severity≥2,earlySVC≥80/onset24,bulbar,site≥5perarm.
- **Pass 1 check:** Subgroup×time/subgroup×treatment×time, differences/difference-of-differences/F for>2levels; other>5% applicability retained. No omitted subgroup inferred here.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S232 — Across-control diagnostics

- **Locations and roles:** PLAN DOC-003 p26.
- **Printed relationship:** PlaceboFAS regimen×time mixedslopes+6covariates×time;adjusted slopes/referencefocal andoverallF;KM/logrank/Cox survival.
- **Pass 1 check:** Control contrasts are diagnostic control heterogeneity, not active efficacy estimands.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S233 — TEAE rates, safety windows andlab/ECG

- **Locations and roles:** PLAN DOC-003 pp27–28.
- **Printed relationship:** TEAE firstdose→safety/death/lastcontact/ATE;Poisson loglink offsetlogweeks;rateper100participantyears anddelta95%CI;MedDRA≥5%;CTCAE5.0shifts.
- **Pass 1 check:** Weekoffset can be converted foryearunit; no numericprinted rate implies an unperformed conversion. Counts ofevents vsaffectedparticipants distinct.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S234 — Other analyses andvalidation

- **Locations and roles:** PLAN DOC-003 pp28–30.
- **Printed relationship:** Weight repeated/slopes efficacysets;suicidalityproportions;screens finalexperience;exposureinclusive/interruptions;blindingFisher+exacttrend;independent keyanalyses integerexact,floating0.1%commonmean.
- **Pass 1 check:** Disposition/exposure reference periods stated; validation0.1% rule not substituted for review precision.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S235 — Bayesian functional model

- **Locations and roles:** PLAN DOC-003 pp35–38.
- **Printed relationship:** Survivorsonly Y=(alphaRT+gammai)−betai exp(thetaT+deltaXi+rho_d+eta_r)j×12/52+normalnoise; placebo theta0=0,activeexp(theta1)DRR.
- **Pass 1 check:** Positive beta declines function via minus sign;DRR.75→25%slowing,.25→75%;actualweeks conversion coherent.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S236 — Bayesian mortality andDRRprior

- **Locations and roles:** PLAN DOC-003 pp36–37,40.
- **Printed relationship:** Monthly exponentiallambda0exp(thetaT),constantcontrolhazard,nocovariate/regimen/timeeffects;DRRUniform(0,2).
- **Pass 1 check:** P(DRR<1)=P(DRR>1)=.5 inprior; hazardspecified scale. Slows mean time phrase treated as context-resolved rate terminology.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S237 — Intercept priors

- **Locations and roles:** PLAN DOC-003 pp37–38.
- **Printed relationship:** alphaRT Normal(38,10²);gammai Normal(0,sigma_gamma²),sigma_gamma U(0,10).
- **Pass 1 check:** Variances/SDlabels retained, no contradiction; priorsnot judged aspreferredinformativeness.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S238 — Slope priors

- **Locations and roles:** PLAN DOC-003 p38.
- **Printed relationship:** betai Normal(mu_beta,sigma_beta,T²);mu_beta Normal(1,1²);sigma_beta,T U(0,2).
- **Pass 1 check:** Arm-specificvariance stated. Negative individualslopes possible underNormal not itself a reporting issue.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S239 — Regimen/time priors

- **Locations and roles:** PLAN DOC-003 p39.
- **Printed relationship:** eta1=0;eta_r Normal(0,sigma_eta²);1/sigma_eta² Gamma(shape1,rate.05²);rho0=0;rho_d Normal(rho_d−1,sigma_rho²),sigma_rho U(0,2).
- **Pass 1 check:** Gamma is shape-rate, variancehyperprior not SD. Timeindexconcurrent0andearlier6monthbins coherent.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S240 — Covariate prior andcentering

- **Locations and roles:** PLAN DOC-003 p39.
- **Printed relationship:** Onset,deltaFRS,logserumNfL,riluzole,edaravone,phenylbutyrate/taurursodiol;mean-center applicablecombineddataset,meanimputetransformed;delta_c iidNormal(0,1²).
- **Pass 1 check:** NoSDrescaling inferred from standardizedword; explicit subtractmean supplies definition.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S241 — Residual/mortality priors

- **Locations and roles:** PLAN DOC-003 p40.
- **Printed relationship:** sigmaRT U(0,4);lambda0 Gamma(shape.01,rate1) monthly,printedmean.01SD.1.
- **Pass 1 check:** Gamma mean=.01/1=.01;SD=sqrt(.01)/1=.1, exact reconciliation.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S242 — Posterior MCMC summaries

- **Locations and roles:** PLAN DOC-003 p40.
- **Printed relationship:** Atleast500000samples,thinning10,convergence/effective sampleadequacy;DRRmean95%credibleinterval,P(DRR<1),P(DRR<.9).
- **Pass 1 check:** No unspecified equal-tail/HPD or retainedcount inferred; no printed contradictory result requires it.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S243 — Primary model fit

- **Locations and roles:** PLAN DOC-003 pp41–42.
- **Printed relationship:** Residualvsfitby4weeks/treatment,meanSDchangevsfitted,KMvsexponential,functionalnoncontributionbymortality/other.
- **Pass 1 check:** Diagnostics mapped; no genericfitcritique based only onimages.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S244 — Primary population sensitivity family

- **Locations and roles:** PLAN DOC-003 pp42–43.
- **Printed relationship:** Bayesian primary repeated inECC,ECM,ERO;CAFS alsoprimary/sensitivitypopulations;EROremovesregimeneffects.
- **Pass 1 check:** Inherited specification mapped for governing-source comparison by otherchecker; noREPORTomission determined inthisshard.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S245 — Primary nonmortality imputation sensitivity

- **Locations and roles:** PLAN DOC-003 p43.
- **Printed relationship:** LOCF,zero botharms,worstcombined,worstwithinarm ALSFRS;survivorsfunctionalcomponent.
- **Pass 1 check:** Fourdistinctprespecifiedhandlingrules mapped, no preferred method assigned.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S246 — Primary functional/time effect sensitivity

- **Locations and roles:** PLAN DOC-003 pp43–44.
- **Printed relationship:** Piecewiselinear6×4week intervals;sum mu_beta,k exp(beta_i+theta+deltaXi+rho+eta)Eijk12/52;muNormal1,1²;betaNormal0,armvariance;otherpriorssame. Separatetime-treatment anddistinctfunction/mortalityvariants.
- **Pass 1 check:** Subjectbeta movesinsideexp byexplicitalternateparameterization;nointerchange withprimarybetaoutsideexp.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S247 — Borrowing/survival sensitivity

- **Locations and roles:** PLAN DOC-003 p44.
- **Printed relationship:** Regimenvariancefixed .001²,.01²,.05²,.1²,.5²,1²,5²,10²;deathaloneinsteadcomposite.
- **Pass 1 check:** Endpoints andvariancegrid explicit;zero vsinfiniteborrowinglimitnotassumedexact atfinitegrid.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S248 — Simulation design andpower reproduction

- **Locations and roles:** PLAN DOC-003 pp45–47; DOC-002 p65.
- **Printed relationship:** PROACT≥3measurementsspan≥24weeks,onset<3years,VC>50,N2175;mean slope−1.03SD.76,residualSE1.77;bootstrap,additive treatmentpreservesslopevariance;3regimens,10000trials/scenario.
- **Pass 1 check:** Functioneffect theta=−slope×slowing e.g.30% gives+.309;simulation vsanalysis multiplicative difference explicit. Seed/rawvirtualpatients unavailable, not standalone finding.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S249 — Simulation nuisance/effect scenarios

- **Locations and roles:** PLAN DOC-003 pp46–47.
- **Printed relationship:** Accrual40/20/60,dropout2/4/6%monthly,start1/3/6months;all-regimen/function/residual±10%,focal±10%;mortality5/10/20%;effectnull/25/30/35%,nomortalitybenefit,andHR1.3harm.
- **Pass 1 check:** Table lists8parameters whileprose6;displayed tables operationallyenumerate scenarioinputs; countwording alone not primarydecision discrepancy.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S250 — Planned sample/power implementation

- **Locations and roles:** PLAN DOC-002 pp92,137,163,212; DOC-003 pp48–49.
- **Printed relationship:** 160/regimen=120active40matchedcontrol;sharedcontrolsfromotherregimens;simulated earlyfutility/nonbinding successrule;firstinterim~7months,then10/13,final~16;meanduration14–15.
- **Pass 1 check:** Approximateaccrualcompletion andglobaltiming not exactclosed-form sampleformula; distributionsforreproduction not supplied. No sample mismatch reproduced.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S251 — Base operating characteristics 0% function slowing /mortalityHR1

- **Locations and roles:** PLAN DOC-003 pp48–49; DOC-002 p65.
- **Printed relationship:** Meanmonths14,success0.024,earlyfutility0.28,meanDRR1.05;10000simulations withfutility.
- **Pass 1 check:** Narrative/tablesmatch. MeanDRRnotforcedequaltrueDRR understopselection. Probability0.28 printed.01allows[.005,.015]; less-than1%narrative remainscompatible withrounding.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S252 — Base operating characteristics 25% function slowing /mortalityHR0.75

- **Locations and roles:** PLAN DOC-003 pp48–49; DOC-002 p65.
- **Printed relationship:** Meanmonths15,success0.61,earlyfutility0.01,meanDRR0.75;10000simulations withfutility.
- **Pass 1 check:** Narrative/tablesmatch. MeanDRRnotforcedequaltrueDRR understopselection. Probability0.01 printed.01allows[.005,.015]; less-than1%narrative remainscompatible withrounding.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S253 — Base operating characteristics 30% function slowing /mortalityHR0.7

- **Locations and roles:** PLAN DOC-003 pp48–49; DOC-002 p65.
- **Printed relationship:** Meanmonths15,success0.77,earlyfutility0,meanDRR0.69;10000simulations withfutility.
- **Pass 1 check:** Narrative/tablesmatch. MeanDRRnotforcedequaltrueDRR understopselection. Probability0 printed.01allows[.005,.015]; less-than1%narrative remainscompatible withrounding.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S254 — Base operating characteristics 35% function slowing /mortalityHR0.65

- **Locations and roles:** PLAN DOC-003 pp48–49; DOC-002 p65.
- **Printed relationship:** Meanmonths15,success0.88,earlyfutility0,meanDRR0.64;10000simulations withfutility.
- **Pass 1 check:** Narrative/tablesmatch. MeanDRRnotforcedequaltrueDRR understopselection. Probability0 printed.01allows[.005,.015]; less-than1%narrative remainscompatible withrounding.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S255 — Base operating characteristics 30% function slowing /mortalityHR1

- **Locations and roles:** PLAN DOC-003 pp48–49; DOC-002 p65.
- **Printed relationship:** Meanmonths15,success0.72,earlyfutility0,meanDRR0.71;10000simulations withfutility.
- **Pass 1 check:** Narrative/tablesmatch. MeanDRRnotforcedequaltrueDRR understopselection. Probability0 printed.01allows[.005,.015]; less-than1%narrative remainscompatible withrounding.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S256 — Base operating characteristics 30% function slowing /mortalityHR1.3

- **Locations and roles:** PLAN DOC-003 pp48–49; DOC-002 p65.
- **Printed relationship:** Meanmonths15,success0.68,earlyfutility0.01,meanDRR0.72;10000simulations withfutility.
- **Pass 1 check:** Narrative/tablesmatch. MeanDRRnotforcedequaltrueDRR understopselection. Probability0.01 printed.01allows[.005,.015]; less-than1%narrative remainscompatible withrounding.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S257 — Mortality sensitivity5%

- **Locations and roles:** PLAN DOC-003 p50.
- **Printed relationship:** NulltypeI0.024,meanDRR1.01;functionDRR.70,mortalityHR.70power/mean0.77/0.69,HR10.72/0.71,HR1.30.68/0.72;nofutility.
- **Pass 1 check:** Allprobabilities[0,1];common benefitpower.77through5/10/20%,nullbelow.025. Harm/noeffectshiftsDRRup toward1asexpected. Numerical operating characteristicsnot independently simulated withoutvirtualdata.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S258 — Mortality sensitivity10%

- **Locations and roles:** PLAN DOC-003 p50.
- **Printed relationship:** NulltypeI0.023,meanDRR1.01;functionDRR.70,mortalityHR.70power/mean0.77/0.69,HR10.67/0.72,HR1.30.57/0.75;nofutility.
- **Pass 1 check:** Allprobabilities[0,1];common benefitpower.77through5/10/20%,nullbelow.025. Harm/noeffectshiftsDRRup toward1asexpected. Numerical operating characteristicsnot independently simulated withoutvirtualdata.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S259 — Mortality sensitivity20%

- **Locations and roles:** PLAN DOC-003 p50.
- **Printed relationship:** NulltypeI0.024,meanDRR1.01;functionDRR.70,mortalityHR.70power/mean0.77/0.69,HR10.56/0.75,HR1.30.35/0.81;nofutility.
- **Pass 1 check:** Allprobabilities[0,1];common benefitpower.77through5/10/20%,nullbelow.025. Harm/noeffectshiftsDRRup toward1asexpected. Numerical operating characteristicsnot independently simulated withoutvirtualdata.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S260 — Illustrative Trial1,active deaths11

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths18;separatemortalityHR0.68,functionDRR0.73,sharedDRR0.73,CAFSone-sidedP0.002,posteriorP(DRR<1)0.994.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S261 — Illustrative Trial1,active deaths13

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths18;separatemortalityHR0.81,functionDRR0.72,sharedDRR0.73,CAFSone-sidedP0.003,posteriorP(DRR<1)0.991.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S262 — Illustrative Trial1,active deaths14

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths18;separatemortalityHR0.87,functionDRR0.73,sharedDRR0.74,CAFSone-sidedP0.005,posteriorP(DRR<1)0.988.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S263 — Illustrative Trial1,active deaths17

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths18;separatemortalityHR1.04,functionDRR0.73,sharedDRR0.76,CAFSone-sidedP0.013,posteriorP(DRR<1)0.982.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S264 — Illustrative Trial1,active deaths18

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths18;separatemortalityHR1.1,functionDRR0.73,sharedDRR0.77,CAFSone-sidedP0.015,posteriorP(DRR<1)0.975.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S265 — Illustrative Trial1,active deaths19

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths18;separatemortalityHR1.15,functionDRR0.73,sharedDRR0.78,CAFSone-sidedP0.022,posteriorP(DRR<1)0.973.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S266 — Illustrative Trial1,active deaths21

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths18;separatemortalityHR1.27,functionDRR0.73,sharedDRR0.79,CAFSone-sidedP0.028,posteriorP(DRR<1)0.972.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S267 — Illustrative Trial1,active deaths23

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths18;separatemortalityHR1.36,functionDRR0.71,sharedDRR0.8,CAFSone-sidedP0.035,posteriorP(DRR<1)0.956.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S268 — Illustrative Trial1,active deaths24

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths18;separatemortalityHR1.41,functionDRR0.71,sharedDRR0.81,CAFSone-sidedP0.056,posteriorP(DRR<1)0.95.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S269 — Illustrative Trial1,active deaths26

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths18;separatemortalityHR1.48,functionDRR0.71,sharedDRR0.82,CAFSone-sidedP0.091,posteriorP(DRR<1)0.948.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S270 — Illustrative Trial1,active deaths27

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths18;separatemortalityHR1.52,functionDRR0.71,sharedDRR0.84,CAFSone-sidedP0.135,posteriorP(DRR<1)0.908.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S271 — Illustrative Trial1,active deaths29

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths18;separatemortalityHR1.58,functionDRR0.73,sharedDRR0.88,CAFSone-sidedP0.233,posteriorP(DRR<1)0.853.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S272 — Illustrative Trial2,active deaths6

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths11;separatemortalityHR0.66,functionDRR0.72,sharedDRR0.71,CAFSone-sidedP0.001,posteriorP(DRR<1)0.998.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S273 — Illustrative Trial2,active deaths7

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths11;separatemortalityHR0.77,functionDRR0.72,sharedDRR0.73,CAFSone-sidedP0.003,posteriorP(DRR<1)0.993.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S274 — Illustrative Trial2,active deaths8

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths11;separatemortalityHR0.87,functionDRR0.74,sharedDRR0.74,CAFSone-sidedP0.004,posteriorP(DRR<1)0.992.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S275 — Illustrative Trial2,active deaths9

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths11;separatemortalityHR0.96,functionDRR0.74,sharedDRR0.75,CAFSone-sidedP0.006,posteriorP(DRR<1)0.988.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S276 — Illustrative Trial2,active deaths10

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths11;separatemortalityHR1.06,functionDRR0.73,sharedDRR0.75,CAFSone-sidedP0.009,posteriorP(DRR<1)0.982.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S277 — Illustrative Trial2,active deaths11

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths11;separatemortalityHR1.13,functionDRR0.74,sharedDRR0.78,CAFSone-sidedP0.013,posteriorP(DRR<1)0.979.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S278 — Illustrative Trial2,active deaths12

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths11;separatemortalityHR1.21,functionDRR0.74,sharedDRR0.78,CAFSone-sidedP0.014,posteriorP(DRR<1)0.976.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S279 — Illustrative Trial2,active deaths13

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths11;separatemortalityHR1.27,functionDRR0.73,sharedDRR0.78,CAFSone-sidedP0.017,posteriorP(DRR<1)0.975.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S280 — Illustrative Trial2,active deaths14

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths11;separatemortalityHR1.33,functionDRR0.74,sharedDRR0.8,CAFSone-sidedP0.028,posteriorP(DRR<1)0.961.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S281 — Illustrative Trial2,active deaths16

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths11;separatemortalityHR1.45,functionDRR0.73,sharedDRR0.8,CAFSone-sidedP0.036,posteriorP(DRR<1)0.959.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S282 — Illustrative Trial2,active deaths17

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths11;separatemortalityHR1.49,functionDRR0.74,sharedDRR0.82,CAFSone-sidedP0.058,posteriorP(DRR<1)0.939.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S283 — Illustrative Trial2,active deaths19

- **Locations and roles:** PLAN DOC-003 pp51–53.
- **Printed relationship:** Placebodeaths11;separatemortalityHR1.57,functionDRR0.75,sharedDRR0.85,CAFSone-sidedP0.085,posteriorP(DRR<1)0.917.
- **Pass 1 check:** SeparateDRR components/sharedDRR/CAFS distinctionsmaintained. Stars agreewithCAFS P<.025 andposterior>.979;Trial2posterior.979*isdisplayprecisionboundary[.9785,.9795],notreproducedcontradiction. NoCIorteststatistic supplied;Pcannotberecomputedfrompointestimatealone.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S284 — Trial1,17active/18placebodeaths

- **Locations and roles:** PLAN DOC-003 p54 Figure6.2.
- **Printed relationship:** Function .73(.54,.97);mortality1.04(.54,1.82);shared.76(.6,.98);posterior.982,CAFSP.013
- **Pass 1 check:** Allpointestimateswithinorderedintervals;sharedcredibleexcludes1andposterior>.979. CAFSsignificantone-sided.025. Function/mortalityownintervalshavenoownPprinted. Visuallyconfirmedexactsourceimage; KM event/risksetsincludeattrition;functionalNexcludesmortalitybyexplicitmodeldefinition.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S285 — Trial1,21active/18placebodeaths

- **Locations and roles:** PLAN DOC-003 p55 Figure6.2.
- **Printed relationship:** Function.73(.54,.97);mortality1.27(.69,1.93);shared.79(.63,1.01);posterior.972,CAFSP.028
- **Pass 1 check:** Allpointestimatescontained;sharedincludes1andposteriorbelow.979;CAFSP>.025. SeparatefunctionCIcannotbecomparedtoCAFSjoint-rankP. Visuallyconfirmedexactsourceimage; KM event/risksetsincludeattrition;functionalNexcludesmortalitybyexplicitmodeldefinition.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S286 — Trial3,sharedcontrol

- **Locations and roles:** PLAN DOC-003 p58 Figure6.3.
- **Printed relationship:** SharedDRR.73(.58,.95),posterior.99,CAFS.0063
- **Pass 1 check:** Containment/ordercoherent;credibleintervalbelow1,posteriorabove.979andCAFSP<.025. Visuallyconfirmedexactsourceimage; KM event/risksetsincludeattrition;functionalNexcludesmortalitybyexplicitmodeldefinition.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S287 — Trial3,matched-only

- **Locations and roles:** PLAN DOC-003 p58 Figure6.3.
- **Printed relationship:** SharedDRR.91(.65,1.36),posterior.683,CAFS.5525
- **Pass 1 check:** Containment/ordercoherent;intervalincludes1,posteriorbelowthreshold;CAFSP>.025. Visuallyconfirmedexactsourceimage; KM event/risksetsincludeattrition;functionalNexcludesmortalitybyexplicitmodeldefinition.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S288 — Trial4,sharedcontrol

- **Locations and roles:** PLAN DOC-003 p59 Figure6.3.
- **Printed relationship:** SharedDRR.9(.64,1.29),posterior.714,CAFS.0026
- **Pass 1 check:** Containment/ordercoherent;DRRcredibleintervalincludes1andposteriorbelowthreshold. CAFSsignificanceexplicitlycontrastedasdifferentjoint-rankanalysis/estimand,not PfortheDRR. Visuallyconfirmedexactsourceimage; KM event/risksetsincludeattrition;functionalNexcludesmortalitybyexplicitmodeldefinition.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S289 — Trial4,matched-only

- **Locations and roles:** PLAN DOC-003 p59 Figure6.3.
- **Printed relationship:** SharedDRR1(.73,1.4),posterior.51,CAFS.3675
- **Pass 1 check:** Containment/ordercoherent;sharedintervalincludes1,posteriornear.5,CAFSnonsignificant. Visuallyconfirmedexactsourceimage; KM event/risksetsincludeattrition;functionalNexcludesmortalitybyexplicitmodeldefinition.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S290 — Trial5,sharedcontrol

- **Locations and roles:** PLAN DOC-003 p60 Figure6.3.
- **Printed relationship:** SharedDRR.67(.5,.87),posterior.998,CAFS.0088
- **Pass 1 check:** Containment/ordercoherent;sharedintervalbelow1,posteriorabove.979andCAFSP<.025. Visuallyconfirmedexactsourceimage; KM event/risksetsincludeattrition;functionalNexcludesmortalitybyexplicitmodeldefinition.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S291 — Trial5,matched-only

- **Locations and roles:** PLAN DOC-003 p60 Figure6.3.
- **Printed relationship:** SharedDRR.73(.51,1.13),posterior.931,CAFS.1102
- **Pass 1 check:** Containment/ordercoherent;intervalincludes1,posteriorbelow.979,CAFSnonsignificant. Similarpointestimateswithlargeruncertaintyarenotidenticalsignificance. Visuallyconfirmedexactsourceimage; KM event/risksetsincludeattrition;functionalNexcludesmortalitybyexplicitmodeldefinition.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S292 — Across-regimen heterogeneity operating characteristics

- **Locations and roles:** PLAN DOC-003 p56.
- **Printed relationship:** No-futility:typeI/meanNullDRR/power/meanAltDRR base.024/1.01/.77/.69;focalslower.060/.96/.85/.66;focalfaster.010/1.05/.67/.72;lowerresidual.024/1.01/.79/.69;higher.023/1.01/.75/.69.
- **Pass 1 check:** Slowerfocalexception to.025calibrationstatedp41. Not a contradictionnorunrevealeddecisiondeviation. Same-null simulatedsignificanceexpected asoperatingcharacteristics.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S293 — Additional sensitivity operating characteristics

- **Locations and roles:** PLAN DOC-003 p61.
- **Printed relationship:** NulltypeI/nullDRR/power/altDRR:base.024/1.01/.77/.69;slowaccrual.025/1.01/.77/.69;fast.020/1.01/.76/.69;dropout4%.024/1.01/.74/.69;6%.024/1.01/.71/.69;start3mo.023/1.02/.67/.70;6mo.021/1.03/.56/.71;slopeslow.023/1.01/.75/.69;fast.023/1.01/.78/.69;residuallow.023/1.01/.79/.69;high.023/1.01/.75/.69.
- **Pass 1 check:** Full11rowsmapped;probabilities inbounds,typeI≤.025atprintedprecision;increasingdropoutandstartgap reducepower. Differentfutilitysettingskeptdistinct.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

### S294 — Background inferential displays and exposure tables

- **Locations and roles:** PLAN DOC-002 pp100–111,119–121,172–183,194–195.
- **Printed relationship:** Historical cell/mouseclinical-rationale Pvalues,HR.3730/BreslowP.0302;SEMfigurebars;NOAEL/AUCratios. Mappinginventoryexplicitlyretains allfigures/tables/axes/tests.
- **Pass 1 check:** No observedCNM-Au8clinicalresult or plannedprimarydecisionderivesnumericallyfromthesedisplays. Nointerval/P/testconflict reproduced;generic preferenceorgraphheightdigitizationexcluded.
- **Pass 1 status:** PASS_1_COMPLETE.
- **Pass 2 status:** Pending distinct-agent pass 2.

## Stable IDs and coverage

S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S222, S223, S224, S225, S226, S227, S228, S229, S230, S231, S232, S233, S234, S235, S236, S237, S238, S239, S240, S241, S242, S243, S244, S245, S246, S247, S248, S249, S250, S251, S252, S253, S254, S255, S256, S257, S258, S259, S260, S261, S262, S263, S264, S265, S266, S267, S268, S269, S270, S271, S272, S273, S274, S275, S276, S277, S278, S279, S280, S281, S282, S283, S284, S285, S286, S287, S288, S289, S290, S291, S292, S293, S294.

Count: 94 relationships;0 findings. DOC-002229/229 and DOC-00365/65 assigned pages are mapped in the current support artifacts. No uninspected scientific source unit. Background rationale, blank scales, bibliographies and administrative pages carry no further trial inferential relationship. Governing-version and method-definition limitations named within the relevant records.

