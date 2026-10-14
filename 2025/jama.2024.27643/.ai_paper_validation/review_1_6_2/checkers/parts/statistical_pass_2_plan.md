# Statistical pass 2 — independent PLAN shard

Runtime agent: /root/statistical_pass_2_plan. Model: gpt-6.1-sol. Reasoning effort: high. Start: FRESH_SPAWN, distinct from both pass1 statistical agents. Exact scope: S201–S294, all94 stable inferential relationships; PLAN DOC-002 PDF pp.1–229 and DOC-003 pp.1–65. REPORT and regimen-plan/report relationships S001–S112 are owned by a separate fresh pass2 agent. This file is a bounded part for coordinator canonical merge.

QUALITY_CONTROL_SCOPE.md, the complete1.6.2 review contract, settings and tooling record were read. The complete C001–C013 ledger, inclusion screen, every mechanical recheck fact and every57 excluded-observation row from the numeric, cross-source and both pass1 statistical shards were read. Current support001/002/003 maps and the complete support004 relationship/numeric summary were read, with authoritative source retrieval for statistical sections. No earlier-run scientific conclusions were consulted.

## Pass 2 finding

### F-ST2-201 — Estimated DRR direction in planned operating characteristics

**Locations and document roles:** PLAN [DOC-003 physical PDF p.50, §6.2 prose and Table6.2.1](../../../../joi240158supp2_prod_1742927563.7711.pdf#page=50), within the Master SAP AppendixI prospective primary-design/simulation report. Both sides are PLAN in the same supplied document. Plan connection: [DOC-002 p.65](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=65) expressly uses AppendixI operating characteristics for the recommended sample-size/primary-design justification; [regimen protocol p.137](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=137) and [p.212](../../../../joi240158supp1_prod_1742927563.7611.pdf#page=212) reference that default statistical design. These links corroborate relevance rather than add a distinct conflict relationship.

**Printed statements and values:** In the null/worse mortality scenarios with functional DRR=.70, the paragraph says power and estimated DRR decrease as mortality increases. Table6.2.1 shows the mean estimated DRR for mortality HR1.3 as .72, .75, .81 at5%,10%,20% baseline mortality, respectively. The corresponding power values .68,.57,.35 decrease. For mortality HR1.0, mean estimated DRR is .71,.72,.75 and power .72,.67,.56. Thus the DRR direction is increasing while the prose assigns decreasing to both quantities. The subsequent sentence explicitly prints .75 and .81 and describes decreasing functional treatment effect, preserving a possible intended distinction between DRR and benefit.

**Rule and calculation:** A direction statement that reverses a displayed estimate is RouteA category2 when its reading changes direction/magnitude beyond the numeric precision threshold. Two-decimal DRRs have half-unit intervals ±.005. For mortality HR1.3,5% mortality DRR.72 permits[.715,.725], and20% mortality DRR.81 permits[.805,.815]. Every admissible20%-minus5% difference is positive,[.080,.100], with nonoverlap gap .080/reference.72=.111111 (11.11%). For10%→20%, intervals[.745,.755] and[.805,.815] have gap .050/.75=.066667 (6.67%). Both exceed.05 and directly oppose the printed decreasing-direction statement. HR1.0 .71→.75 permits[.705,.715] and[.745,.755], gap .030/.71=.042254 (4.23%), so that magnitude comparison alone would be screened by precision; it is retained only as another location of the same prose direction pattern. Central DRR changes .72→.81 and implied benefit1-DRR28%→19% are illustrative identities, not fitted trial estimates.

**Focus area:** B and D, direction agreement for primary-design operating-characteristic estimates.

**Proposed review domain:** plan_material.

**Proposed relationship type:** P_P; **All relationships:** P_P.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** The direction of the average simulated primary DRR response to increased baseline mortality under the specified functional benefit/mortality-harm scenario, used to explain the prospective shared-parameter design. This is a PLAN operating-characteristic result, not the observed CNM-Au8 trial DRR.

**Why context does not resolve it:** RouteA category2 always registers a reproduced direction reversal. The later numeric explanation supports a likely intended benefit reading, but it does not make the printed estimated-DRR decreasing statement agree with its own table. The prior CONTEXT_RESOLVES exclusion therefore does not apply to this reproduced always-register observation.

**Alternatives and missing definitions:** The prose may intend that treatment benefit1-DRR, rather than DRR itself, decreases; the numerical table and subsequent explanation support that alternative. An older AppendixI version may establish the operative wording for regimenC. The supplied later Master SAP's [p.8 applicability statement](../../../../joi240158supp2_prod_1742927563.7711.pdf#page=8) distinguishes later RSAs, and [regimen cover p.63](../../../../joi240158supp2_prod_1742927563.7711.pdf#page=63) names Master SAPv1.0. No claim is made that these illustrative values are observed trial outcomes or that this wording changed a conducted analysis. The inconsistency is within the supplied prospective primary-design explanation, whose general relevance is explicitly cited above; definitive governing-version attribution remains a limitation for human review.

**Exact human question:** In this prospective primary-design operating-characteristic explanation, does the decreasing statement concern DRR or1-DRR benefit, and what governing AppendixI version and direction should a reader record for the .72,.75,.81 scenario?

**Source confirmation:** p50 was freshly rendered at200dpi with the bundled helper and visually inspected. Prose, row/column identity, decimal values and signs match native source text. No OCR/source disagreement was observed. Linked source PDFs remain unchanged. No C ID is assigned before independent screening.

### F-ST2-202 — Signed CAFS P value in illustrative PLAN prose

**Locations and document roles:** PLAN [DOC-003 physical PDF p.59, top continuation paragraph and adjacent Figure6.3.2 matched-regimen-only lower row](../../../../joi240158supp2_prod_1742927563.7711.pdf#page=59). Both are PLAN illustrative operating-characteristic results in the supplied prospective primary-analysis/simulation appendix, not observed trial outcomes. [Preceding p.58](../../../../joi240158supp2_prod_1742927563.7711.pdf#page=58) names the example and contrasts Bayesian primary with joint-rank CAFS inference.

**Printed statements and values:** The top paragraph describing matched-regimen-only controls prints CAFS p-value of - .3675, with the dash separated by a space and line break before the decimal. The adjacent figure's matched-only CAFS P-value is0.3675. The same paragraph's treatment estimate1.0 and posterior probability.51 agree with the lower figure, establishing the matched result identity.

**Rule and calculation:** A P value is a probability and cannot be negative. Taking the printed dash literally as a minus sign gives -.3675, while the figure supplies +.3675. Four-decimal half-unit intervals are[-.36755,-.36745] and[.36745,.36755], respectively; their gap is.73490 and the reference absolute figure value.3675 gives relative discrepancy1.9997279 (199.97%). The sign changes the numerical P reading; this is not a display-zero P observation. The source explicitly names the same matched-control CAFS result in both locations, so no alternate estimator or population is silently aligned.

**Focus area:** B, test-value identity and permitted P range.

**Proposed review domain:** plan_material.

**Proposed relationship type:** P_P; **All relationships:** P_P.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** The signed printed CAFS P value for the matched-control illustrative sensitivity analysis used to explain the prospective shared-control primary-design diagnostics.

**Why context does not resolve it:** The strict printed-number doubt rule requires a finding where a visible sign may change a P reading. The positive figure makes a punctuation explanation likely, but a reproduced numerical sign reading cannot be excluded solely because its intended positive value is inferable. Independent screening must determine whether this dash is merely punctuation or a signed numerical reading under the inclusion rule.

**Alternatives and missing definitions:** The dash may be a stray punctuation separator rather than an intended negative sign; the positive figure and both analyses' null description support that alternative. No actual negative test output, changed primary decision, misconduct or conducted-analysis consequence is asserted. The later Master SAP version and earlier regimen-C governing cover at[p.63](../../../../joi240158supp2_prod_1742927563.7711.pdf#page=63) limit attribution to a specific operative regimen plan, as in F-ST2-201. This is bounded to the supplied PLAN display, not a comparison with an unprovided source.

**Exact human question:** Should the dash in the prose be read as punctuation or as a sign attached to the numerical P, and what signed value should be recorded for this matched-control CAFS result?

**Source confirmation:** The exact source-matched current render preprocessing/support-004/p059.png was viewed. The dash and line-break position are visible, and native source retrieval agrees; the adjacent lower figure explicitly prints0.3675. This is a direct print observation; the inferred punctuation mechanism is separated from it. No C ID is assigned before independent screening.


## All prior checker exclusions revisited

This table records every57 prior row once, in its original checker order. It is a routeA/precision audit, not a second register of findings. REPORT-specific mechanical conclusions/emissions remain assigned to the companion fresh pass2 agent; no observation already in the screening log is re-emitted. Checks that reconcile are in the S record table below.

| Prior row | Source observation reread | Pass2 routeA and precision decision |
|---|---|---|
| NUM01 | Abstract/body age58.4/57.7 | Half-unit gap.60/58.4=1.03%, below.05; precision exclusion remains. |
| NUM02 | Fatigue12/120 versus10.8% and12/13 copies | Count intervals touch; percentage gap2.683% is below.05. No reproduced RouteA3. |
| NUM03 | Figure1 regimen-placebo6 versus2+1+1+1 | Sum[3,7] overlaps[5.5,6.5], so no reproduced RouteA3 under required integer precision. |
| NUM04 | Completion137/164 versus85% | Remaining relative gap1.40%, below.05. |
| NUM05 | Unknown-race3 versus164-160=4 | [3,5] and[2.5,3.5] overlap; no reproduced count discrepancy. |
| NUM06 |13 events versus5+9=14 | Sum[13,15] intersects[12.5,13.5]; no reproduced RouteA3. |
| NUM07 | Moderate44 versus22+24=46 | Precision gap.5/44=1.136%, below.05. |
| NUM08 | Severity884 versus889 | Precision gap3/889=.337%, below.05. |
| NUM09 | Functional bounds; plasma-.4/-.5 copies | Functional relative gaps<.05; plasma half-unit intervals meet. This is not the same-display CI/P conflict, already C012. |
| NUM10 | Functional contributor/risk counts | Explicit mortality-related contributor definition separates quantities; per-time-point copies are peripheral without a changed randomized population. |
| NUM11 | Exploratory serum numerical copies | No independent RouteA1 pair or category2 reversed number; peripheral cross-copy. Within-table scale method is already C013. |
| NUM12 | Adjusted Cox HR versus crude risks | Model-based estimand is explicitly adjusted; no source claims crude identity, so no reproduced RouteA4. |
| NUM13 | PLAN particle quantities per mL/per60mL | Preclinical rationale does not define trial primary/key-secondary inference or a planned decision. It is outside the relied-on PLAN design remit. |
| NUM14 | Assisted-ventilation16(18%)/9(31%) | Outcome-specific prevalent-event exclusions make denominators unavailable; no stated common denominator establishes a reproduced count conflict. |
| XS01 | Mapper Figure1 death transcription | Exact source shows1, not derivative3; NOT_REPRODUCED. |
| XS02 | ElEscorial complementary label | Paired subgroup counterpart resolves wording; no membership count or altered partition is established by the truncated label alone. Companion owns REPORT verification. |
| XS03 | Weight<56 combines planned lower strata | Read against RouteA5, not merely missing participant-count logic; visible group pooling deserves independent companion REPORT/PLAN reconsideration. No PLAN-only emission here. |
| XS04 | Age copies | Precision1.03% remains below.05. |
| XS05 | Fatigue copies | Touching integer intervals and percentage gapbelow.05 remain precision-compatible. |
| XS06 | Total events | Half-unit sum/copy intervals overlap. |
| XS07 | Functional credible-bound copies | Each remaining relative gap is below.05; no CI/P test conflict. |
| XS08 | Exploratory serum copies | Peripheral cross-copy alone; C013 retains reproduced within-table method identity. |
| XS09 | Serum sensitivityP=.05/.051 and signs | P intervals overlap; contrast ordering explains opposite signs. No reproduced same-analysis CI/P contradiction. |
| XS10 | Plasma endpoint copies across displays | Cross-copy is distinct from same-row interval/P issue already C012. No repeated finding. |
| XS11 | Baseline/per-visit contributor copies | Peripheral copies with defined mortality exclusions; no common trial-analysis-size discrepancy. |
| XS12 |80% versus77% planned power | Gap2/80=2.5% after integer half units; precision exclusion. |
| XS13 | Later Master third drug/28weeks versus regimen | Applicability and explicit RSA overrides distinguish prospective versions. No reproduced altered governing regimen element. |
| XS14 | OLE windows/duration | Extension amendments and administrative windows are separate from randomized primary/key-secondary rules. |
| XS15 |40 active versus30drug+10placebo | Immediate parenthetical resolves40 randomized meaning; no conflicting numeric allocation. |
| XS16 | Cox versus crude | Explicitly adjusted estimand; no crude-result claim. |
| XS17 | Simulated figures versus actual trial | Distinct PLAN simulated and REPORT observed quantities cannot be matched. The p50 direction finding instead compares its own same-page prose/table. |
| XS18 | Absent earlier Master SAP | Missing document alone has no conflicting printed result; C004/C006 retain governing-version limits. |
| XS19 | Equation indexes/covariance letters | Named participant/regimen intercept-slope prose identifies symbol roles; no altered printed result/test. |
| ST1R01 | Functional credible-bound copies | Remaining gaps<.05, not CI/P comparison; precision exclusion. |
| ST1R02 | Plasma upper-.4 versus-.5 | Half-unit ranges touch. |
| ST1R03 | SensitivityP=.05/.051 | Overlapping P precision and both corresponding intervals contain0 after contrast reversal. |
| ST1R04 | Adjusted Cox versus crude | Source explicitly labels adjustment and profile-likelihood inference; no reproduced crude identity. |
| ST1R05 | SeriousTEAEP=.31 reconstruction | Test/population for a nested2x4 recomputation is unspecified; no valid same-result reproduction is established. |
| ST1R06 | CAFS codevariable name | Intended treatment comparison explicit; variable naming alone changes no printed number or stated decision. |
| ST1R07 | Repeated-measures post identifier | Coefficient blocks and baseline-to24week prose state the intended contrast; identifier ambiguity alone supplies no result contradiction. |
| ST1R08 | Shared-baseline phrase after amendment | Explicit governing treatment main effect and revision distinguish model choice; no reproduced changed result supplied by the residual phrase. |
| ST1R09 | delta-FRS unit | Explicit monthly formula resolves points/year wording. Actual three-group/median partition discrepancy is already C010 and not re-emitted. |
| ST1R10 |40 active parenthetical |30+10=40; meaning is explicit. |
| ST1R11 | Sex covariate lists | Existing C006 includes this report adjustment-set issue after independent screening/recheck; duplicate, not re-emitted. |
| ST1R12 | DRR.64-1.29 versus CAFSP.0026 | Exact figures/prose name separate Bayesian DRR and fixed-sharing joint-rank CAFS analyses. No same-result interval/P pair exists. |
| ST1R13 | Serum plate-related regimen-only rerun | Disclosed exploratory analysis change retains status and has no missing primary/key-secondary output; no changed status/composite or supplied-plan-presence claim reproduced. |
| ST1P01 | Later Master treatment main effect/code | No regimen reliance on this later default; explicit governing regimen model retains treatment main effect. Not a printed result or prespecified/report replacement. |
| ST1P02 | Slope section repeats24week estimand | Immediate slope equation, contrast, month unit and slope interpretation identify quantity; no relied-on observed value is misattributed here. |
| ST1P03 | Slowing time wording versus rate | Explicit hazard and DRR definition establish rate identity; wording alone is not a numerical direction reversal. |
| ST1P04 | Six versus eight scenario parameters | Named table parameters and their sensitivity rows are available; parameter-list wording is not a participant count or changed analysis decision. |
| ST1P05 |<1% versus.01 early futility | [ .005,.015 ] admits valuesbelow.01; no reproduced interval/test conflict. |
| ST1P06 | Posterior.979 significance asterisk | [.9785,.9795] admits>.979; no interval or same-DRR test contradicts it, so ordinary display precision applies. |
| ST1P07 | Shared DRR versus CAFS | Separate named estimands/tests; NOT_REPRODUCED as a same-result pair. |
| ST1P08 | DRR decreases prose versus table | Reproduced RouteA2 direction reversal with HR1.3 gap11.11%; emitted as F-ST2-201. Immediate explanation does not authorize CONTEXT_RESOLVES. |
| ST1P09 | Protocol all-function versus AppendixI contributor exclusion | Explicit protocol precedence identifies exact primary contributor rule; no undisclosed replaced analysis asserted. |
| ST1P10 | Master28weeks versus regimen24 | Master explicitly permits RSA override; both regimen versions consistently24weeks. |
| ST1P11 | Poisson weeks versus years | Unit conversion is possible; absent printed rate leaves no reproduced conversion contradiction. |

## Excluded observations

Only apparent observations that this PLAN pass2 decided not to emit are listed; no qualifying routeA observation is excluded. F-ST2-201 is omitted from this table because it is emitted above. Existing candidate references are not additional excluded observations.

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC-003 pp21–22, applicabilityp8 and governingp63 | Later-default prose/equation treatment main effect differs from code, but no reported regimen-C result is demonstrated to rely on that later specification. | PERIPHERAL_COMPARISON |
| PLAN DOC-003 p22 | The slope section repeats24-week-change estimand prose; explicit slope equation/contrast/month units identify its meaning without a reported quantity conflict in this assigned scope. | CONTEXT_RESOLVES |
| PLAN DOC-003 pp18,36–37 | Time-to-mortality slowing terminology is clarified by explicit monthly-hazard equation and DRR definition. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-003 pp46–47 | Six-parameter prose versus eight named scenario parameters does not change a participant count, primary/key-secondary result or decision rule. | CONTEXT_RESOLVES |
| PLAN DOC-002 p65; DOC-003 pp48–49 | Less-than1% early futility and printed.01 share admissible half-unit values[.005,.015]. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-003 pp52–53, Trial2deaths11 | Posterior.979 with asterisk permits[.9785,.9795], including values>.979; no independent interval/test conflict exists. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-003 pp58–59 | DRR interval and CAFSP.0026 are explicitly separate named analyses, rather than a same-result CI/P pair. | NOT_REPRODUCED |
| PLAN DOC-002 pp61–62; DOC-003 pp35–36 | AppendixI contributor definition takes explicit precedence over protocol recommendations, identifying the operational rule. | CONTEXT_RESOLVES |
| PLAN DOC-003 p9; DOC-002 pp92,163 | Master28-week maximum explicitly permits RSAoverride; regimenC24weeks is consistently stated. | CONTEXT_RESOLVES |
| PLAN DOC-003 p27 | Logweeks offset can be rescaled to per100 participant-years; no printed rate demonstrates absence of conversion. | CONDITIONAL_OR_UNREPORTED |

## Independent status for every assigned S ID

All94 relationships have explicit PASS_2_COMPLETE. Detailed retained printed values, exact PLAN locations and both pass statuses are in statistics/parts/plan_relationship_inventory_pass_2.md. The table below states the independent pass2 check for every ID; no range shorthand substitutes for a relationship record.

| Relationship ID | Pass2 status | Independent check |
|---|---|---|
| S201 | PASS_2_COMPLETE | Prospective precedence is explicit at protocol p60 and SAP p8; regimen-C cover p63 specifies an earlier Master version. Versions are not silently aligned. This limits later-default model comparisons; C001/C011 preserve observed status/composite differences without inventing governance. |
| S202 | PASS_2_COMPLETE | Allocation reconciles: 160*3/4=120, 160/4=40, 120/2=60. Shared controls add participants by a defined pooling rule; the randomized target is not a promised final pooled-control count. |
| S203 | PASS_2_COMPLETE | Primary function/mortality shared DRR, baseline-through-week24 horizon and active/placebo direction agree. Null=1 and benefit=DRR<1 are expressly stated; no crude functional ratio is substituted. |
| S204 | PASS_2_COMPLETE | PAV criteria >22 hours/day and >7 consecutive days are consistent; later vital-status ascertainment is distinguished from the primary week24 censoring horizon. |
| S205 | PASS_2_COMPLETE | Concurrent 180-day extensions and nonconcurrent-control options are explicit; the focal month12-24 example gives month6-30. No undocumented participant denominator is inferred. |
| S206 | PASS_2_COMPLETE | Interim includes ongoing participants; final requires an opportunity to complete 24 weeks. As-randomized and post-discontinuation retention are explicit; no count contradiction is supplied. |
| S207 | PASS_2_COMPLETE | ECC is an explicitly defined FAS subset with an exclusive 180-day eligibility window. No actual ECC result/count is printed in this PLAN shard. |
| S208 | PASS_2_COMPLETE | ERO and ECM population identities differ by regimen and administration route. Governing regimen analysis omissions are already captured in C003, with no separate PLAN-only discrepancy. |
| S209 | PASS_2_COMPLETE | Per-protocol adherence restrictions are deferred to R-SAP while protocols name 80%-120%. As-treated and event-dependent truncation are explicit, with no participant count to refit. |
| S210 | PASS_2_COMPLETE | STF/STN/SRO are treated populations by defined shared/route/regimen eligibility, distinct from randomized efficacy sets; no unexplained population arithmetic is reproduced. |
| S211 | PASS_2_COMPLETE | Repeat observation sets are conditionally independent given a new baseline and stated covariates after washout. This is a stated coherent choice; no preferred alternative or raw-data audit is proposed. |
| S212 | PASS_2_COMPLETE | Primary pooling of both doses and supportive dose-specific analyses are explicit. The source does not turn exploratory nominal dose-specific P values into confirmatory declarations. |
| S213 | PASS_2_COMPLETE | 40 randomized comprises 30 active and 10 placebo under 3:1; eligibility requires week24 opportunity. Global approximately12-week intervals and final-analysis timing are internally coherent. |
| S214 | PASS_2_COMPLETE | Final posterior Pr(DRR<1)>.979 is distinguished from mere exclusion of1 by a95% credible interval. No early-success default applies, and the slower-focal calibration exception is expressly disclosed. |
| S215 | PASS_2_COMPLETE | DRR<.9 means at least10% slowing and interim posterior probability below.05 defines futility. The point estimate alone is not the stopping boundary. |
| S216 | PASS_2_COMPLETE | Default secondary gate requires primary success and a sequential two-tailed P<.05 rule; nominal results are still reported. Regimen-specific hierarchy can supersede the default. |
| S217 | PASS_2_COMPLETE | Baseline substitution/mean imputation, nonmortality MAR and mortality handling are distinct explicit steps. AppendixI precedence supplies the functional mortality-contribution definition. |
| S218 | PASS_2_COMPLETE | 12 items*4=48 and four domains*12=48 reconcile. Alternative cutting-food items are mutually exclusive. Delta-FRS explicitly divides by months since weakness onset. |
| S219 | PASS_2_COMPLETE | Maximum maneuver selection and GLI prediction covariates are named. Protocol/SAP operational differences do not establish a reported key-secondary value or decision conflict. |
| S220 | PASS_2_COMPLETE | 11 bilateral muscles plus bilateral grip give24 measures. Zero-handling and first/second-zero interval-censored composite rules are explicit; existing outcome-status C001 is retained. |
| S221 | PASS_2_COMPLETE | Protocol endpoint statuses are read directly. The complete ledger's C001 and C011 capture changed HHD status and six-point composite elsewhere; no duplicate finding is emitted here. |
| S222 | PASS_2_COMPLETE | First40 riluzole users reachingweek8 is a PK review, distinct from40/24-week efficacy interim eligibility. Biomarker test details are delegated to separate plans, with C002's unavailable-plan caveat retained. |
| S223 | PASS_2_COMPLETE | Repeated-measures prose and code include treatment, visit, treatment*visit and six covariate/interactions with unstructured within-participant covariance; fixed versus random regimen conditions are explicit. |
| S224 | PASS_2_COMPLETE | Contrast coefficients give (active24-active0)-(placebo24-placebo0) under the printed group/visit order. The estimate is a24-week change difference and has95% Wald bounds. |
| S225 | PASS_2_COMPLETE | Later Master prose/equation include a treatment main effect while code lacks it; exact source confirms the difference, but regimen-C reliance on this later default is unestablished and its governing regimen slope specification includes the main effect. Excluded as PERIPHERAL_COMPARISON; no reproduced RouteA result or decision conflict. |
| S226 | PASS_2_COMPLETE | Plan separates logrank from unadjusted/adjusted Cox with profile-likelihood bounds. These are distinct analyses, so no Wald/CI/P identity is inferred; C005 retains the governing planned/report logrank comparison. |
| S227 | PASS_2_COMPLETE | Pairwise joint ranks, survival priority and shared follow-up function comparison are defined. Adjusted rank and unadjusted Wilcoxon are separate alternatives; C004 preserves the governing regimen primary-analysis difference. |
| S228 | PASS_2_COMPLETE | First/second loss-of-strength times are interval-censored by visits, matched to explicitly named interval-censored methods. No independent-sample or exact-event assumption is invented. |
| S229 | PASS_2_COMPLETE | 50 placebo-reference imputations use earlier-visit regressions and named covariates, with endpoint ranges explicit. No imputation count or unspecified covariance is substituted for data. |
| S230 | PASS_2_COMPLETE | 95% normal efficiency is a robust tuning definition, not a confidence level. Exponential-tilting sensitivity states its endpoint/weight remit; absent grid values alone are not a contradiction. |
| S231 | PASS_2_COMPLETE | Default subgroup interactions and F tests for >2levels are specified. Regimen-C partition conflict C010 and named output omissions C003 remain distinct; later Master median split alone cannot redefine their governing plan. |
| S232 | PASS_2_COMPLETE | Across-regimen placebo slope/survival comparisons are control-heterogeneity diagnostics with specified adjustment. They are not active-treatment efficacy comparisons. |
| S233 | PASS_2_COMPLETE | Poisson offset is logweeks but output unit can be converted to per100 participant-years; no numeric rate establishes omitted conversion. Event counts and affected-participant proportions remain distinct. |
| S234 | PASS_2_COMPLETE | Exposure is inclusive of endpoints with defined interruption handling; blinding exact tests are named. Internal replication tolerance .1% is not this review's display-precision threshold. |
| S235 | PASS_2_COMPLETE | Functional rate is multiplied by exp(theta), and the minus sign makes positive slopes declines. DRR.75 maps to25% slowing; survivor-only functional contributors are explicit rather than inferred. |
| S236 | PASS_2_COMPLETE | Monthly hazard lambda0*exp(theta) shares DRR with function; Uniform(0,2) allocates half its mass below1. Time/rate prose is clarified by the explicit hazard equation and is not a new direction-value reversal. |
| S237 | PASS_2_COMPLETE | Overall intercept Normal(38,10^2), participant intercept Normal(0,sigma_gamma^2) and sigma_gamma Uniform(0,10) are coherent; SD and variance are kept distinct. |
| S238 | PASS_2_COMPLETE | Slope mean Normal(1,1^2) and arm-specific SD Uniform(0,2) are explicit. Normal individual slopes need not be restricted to decline; that choice is not questioned. |
| S239 | PASS_2_COMPLETE | Regimen precision prior is Gamma(shape1,rate.05^2), not a Gamma prior on SD. Time effects are conditionally centered at the preceding effect with a Uniform SD; reference effects are0. |
| S240 | PASS_2_COMPLETE | Baseline centering and post-transformation mean imputation are explicit. No variance scaling is inferred from the term standardized; Normal(0,1^2) is a coefficient prior. |
| S241 | PASS_2_COMPLETE | Gamma(shape.01,rate1) gives mean.01/1=.01 and SD sqrt(.01)/1=.1 exactly, matching print. Residual SD Uniform(0,4) is not a variance declaration. |
| S242 | PASS_2_COMPLETE | At least500000 posterior samples with thinning10 and convergence/effective-size selection are specified. Equal-tail versus highest-density intervals and retained draw count are not invented. |
| S243 | PASS_2_COMPLETE | Residual/mean-change/KM fit diagnostics are explicit. Visual curves are not digitized into exact estimates or used for a broad model-fit critique. |
| S244 | PASS_2_COMPLETE | ECC/ECM/ERO primary sensitivity populations and ERO removal of regimen effects are defined. Governing unreported ECM/EPP outputs are already retained in C003; no duplicate PLAN finding. |
| S245 | PASS_2_COMPLETE | Four nonmortality imputation rules are named: LOCF,0,worst combined,worst arm. Death contribution remains a separate defined component; no preferred method is substituted. |
| S246 | PASS_2_COMPLETE | Piecewise sensitivity explicitly moves the subject slope into an exponential parameterization and has six4-week intervals. It is a different named model, not an internally conflicting copy of the primary beta term. |
| S247 | PASS_2_COMPLETE | The eight fixed borrowing variances and death-alone sensitivity are named. Finite grid endpoints are descriptive limits, not claims of an exact asymptotic identity. |
| S248 | PASS_2_COMPLETE | Bootstrap virtual data, additive treatment shift and residual variation are stated. Mean slope -1.03 with30% slowing gives additive +.309; raw PROACT subset/seed unavailable prevents independent stochastic power reproduction. |
| S249 | PASS_2_COMPLETE | Table enumerates eight scenario parameters despite six-parameter prose; all assumptions/results remain specifically listed. This count is not a participant count, endpoint result or changed planned decision rule; retained CONTEXT_RESOLVES. |
| S250 | PASS_2_COMPLETE | 160=120+40 and approximate accrual/interim/final durations refer to simulated schedules. No deterministic closed-form sample-size claim or complete stochastic inputs are supplied. |
| S251 | PASS_2_COMPLETE | Null operating probability .024 and early futility .28 are distinct. Mean estimated DRR1.05 under stopping selection is not required to equal the generating null exactly; no standalone contradiction. |
| S252 | PASS_2_COMPLETE | Common25% slowing power.61, early futility.01 and meanDRR.75 match the stated scenario. Printed.01 allows[.005,.015], overlapping probabilities below1%. |
| S253 | PASS_2_COMPLETE | Common30% slowing power.77, early futility.00 and meanDRR.69 match source; display-zero probability is not treated as an impossible event. |
| S254 | PASS_2_COMPLETE | Common35% slowing power.88, early futility.00 and meanDRR.64 are internally ordered with increasing benefit; no unsupported simulation recalculation. |
| S255 | PASS_2_COMPLETE | 30% function slowing with mortalityHR1 has power.72 and meanDRR.71, distinct from common-benefit power.77. No trial posterior or primary significance is inferred. |
| S256 | PASS_2_COMPLETE | 30% function slowing with mortalityHR1.3 has power.68 and meanDRR.72, consistent with the adverse-mortality scenario; early futility.01 remains precision-compatible with<1% prose. |
| S257 | PASS_2_COMPLETE | Table6.2.1 at5% mortality has meanDRR.71/.72 for HR1/1.3. Reversed estimated-DRR direction prose on the same page is emitted once as F-ST2-201. |
| S258 | PASS_2_COMPLETE | At10% mortality meanDRR.72/.75 for HR1/1.3 rises from the5% scenario. F-ST2-201 retains the repeated direction pattern; no separate candidate or stochastic power refit. |
| S259 | PASS_2_COMPLETE | At20% mortality meanDRR.75/.81 for HR1/1.3 rises rather than decreases. HR1.3 end-to-end gap .08/.72=11.11% after half-unit intervals qualifies RouteA2; F-ST2-201. |
| S260 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S261 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S262 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S263 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S264 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S265 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S266 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S267 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S268 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S269 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S270 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S271 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S272 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S273 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S274 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S275 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S276 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S277 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S278 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S279 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S280 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S281 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S282 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S283 | PASS_2_COMPLETE | This specific illustrative row was reread in Table6.2.2 or6.2.3: active deaths, separate mortality/function estimates, common DRR, CAFS one-sided P and posterior probability remain different named outputs. Asterisks follow CAFS P<.025 and posterior>.979; the .979 boundary is precision-compatible with [.9785,.9795]. No interval/test statistic or standard error supplies an independent same-result conflict. No normal approximation is imposed. |
| S284 | PASS_2_COMPLETE | Direct figurep54: .73[.54,.97],1.04[.54,1.82],.76[.6,.98] have ordered bounds and contain their estimates. Posterior.982>.979 and CAFS.013<.025 each match its separate rule. |
| S285 | PASS_2_COMPLETE | Direct figurep55: .73[.54,.97],1.27[.69,1.93],.79[.63,1.01] contain estimates. Posterior.972<=.979 and CAFS.028>=.025 are coherent for distinct named analyses. |
| S286 | PASS_2_COMPLETE | Direct figurep58 shared .73[.58,.95] is contained, posterior.99>.979 and CAFS.0063<.025. Shared controls and matched-only results have distinct precision/populations. |
| S287 | PASS_2_COMPLETE | Direct figurep58 matched-only .91[.65,1.36],posterior.683 and CAFS.5525 imply no success under their separate criteria; interval contains1 and the estimate. |
| S288 | PASS_2_COMPLETE | Direct figurep59 shared .9[.64,1.29] and posterior.714 are paired Bayesian outputs; CAFS.0026 is explicitly a different fixed-sharing joint-rank test. NOT_REPRODUCED as an interval/P conflict. |
| S289 | PASS_2_COMPLETE | Direct figurep59 matched-only1[.73,1.4],posterior.51 and CAFS.3675 are coherent; top prose has a separated dash before.3675. Its possible signed-P reading is emitted as F-ST2-202, with punctuation retained as an alternative. |
| S290 | PASS_2_COMPLETE | Direct figurep60 shared .67[.5,.87],posterior.998 and CAFS.0088 are contained and individually significant under their named criteria. |
| S291 | PASS_2_COMPLETE | Direct figurep60 matched-only .73[.51,1.13],posterior.931 and CAFS.1102 are not significant under the separate criteria. Similar point effects with wider intervals are not equivalent significance claims. |
| S292 | PASS_2_COMPLETE | Five across-regimen rows are bounded probabilities with valid DRRs. Focal-slower typeI.060 versus nominal.025 is expressly excepted in the calibration paragraph, so no stated decision is contradicted. |
| S293 | PASS_2_COMPLETE | All eleven operating-characteristic rows are checked by scenario. TypeI values .020-.025 obey printed calibration, and reduced borrowing/dropout change power as separately simulated; virtual inputs unavailable. |
| S294 | PASS_2_COMPLETE | Historical HR.3730/BreslowP.0302 has no accompanying HR interval or same-test statistic; preclinical plots supply mean/SEM and named tests without incompatible printed pairs. No raw-data or preferred-analysis critique. |

## Direct authority, limitations and handoff

New source derivatives: preprocessing/statistics-2-plan/sap8-61.txt, protocol60-65.txt and sap50.png. Commands used /home/juliz/venvs/stt/bin/python workflow_1_6_2/scripts/pdf_tools.py text SOURCE --first8 --last61 OUT --layout for DOC-003, --first60 --last65 for DOC-002, and render DOC-003 --page50 OUT. Engine: PyMuPDF1.28.0, native sorted reading order; CPU200dpi rendering. All five current source-matched support004 figures p054.png,p055.png,p058.png,p059.png,p060.png were viewed independently, including ordered intervals, point containment, posterior/CAFS identities, cumulative events and risk-set counts. No new OCR or GPU inference was needed. Current and legacy evidence assets remain unchanged.

Individual participant/virtualPROACT data, simulation random seeds, posterior draws, credible-interval construction and separate earlier Master/PD plans are unavailable. Statistical inference cannot be independently refitted from the supplied summary values alone; no sidedness, degrees of freedom, interval construction or covariance is imposed beyond explicit source rules. The operating-characteristic direction finding is arithmetic/textual, not a stochastic refit. All13 stable candidate facts remain Pending Human Adjudication; C003's clarified week24PAV/death presence and C013's corrected exponential diagnostic were retained.

Completed scope:94 relationships;2 new findings;10 current PLAN excluded observations;57 prior checker rows reread; zero assigned scientific coverage gaps. No candidate count is targeted or candidate adjudication assigned. Coordinator must merge the bounded parts, screen F-ST2-201 and F-ST2-202 with a fresh independent screener, and append/recheck only if included. Runtime ID: /root/statistical_pass_2_plan.

