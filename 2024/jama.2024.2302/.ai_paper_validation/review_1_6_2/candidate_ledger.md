# Workflow 1.6.2 Candidate Ledger

**Pending Human Adjudication.** Six stable IDs were assigned after the fresh independent inclusion screen of all 11 initial findings. A different fresh pass-2 screener included F-ST2-001 as added developmental scope of C005, retaining six stable IDs across 12 findings. Discovery used complete supplied-source mapping, not legacy candidate sets. IDs follow earliest REPORT location and methods subsection order, followed by the PLAN-only issue. IDs are never removed or renumbered. Repeated observations of one issue are consolidated, preserving every finding and affected source location.

The classification table records the included finding ID for each candidate. Duplicate checker finding IDs are preserved in each card's provenance. The fresh mechanical recheck confirmed all six evidence states as reproduced and all registered role/type/domain assignments without transcription changes. Inclusion-audit fields remain pending the fresh quality audit; no AI adjudication is assigned.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main article abstract vs REPORT main article flow and surgery narrative | reproduced | CONFIRMED | F-NUM-001 |
| C002 | protocol_report | P_R | P_R, P_P | PLAN protocol vs PLAN SAP vs REPORT main article and results supplement | reproduced | CONFIRMED | F-XS-002 |
| C003 | protocol_report | P_R | P_R, P_P | PLAN protocol and PLAN SAP vs REPORT main article prior specifications | reproduced | CONFIRMED | F-XS-003 |
| C004 | protocol_report | P_R | P_R | PLAN protocol and PLAN SAP vs REPORT main article formal interim | reproduced | CONFIRMED | F-XS-004 |
| C005 | protocol_report | P_R | P_R | PLAN protocol and PLAN SAP analyses vs REPORT main article and results supplement | reproduced | CONFIRMED | F-XS-005, F-ST2-001 |
| C006 | plan_material | P_P | P_P | PLAN protocol hypothesis vs PLAN protocol power assumptions; PLAN SAP clarification | reproduced | CONFIRMED | F-NUM-002 |

## C001 — Abstract operative-repair population count

**Candidate statement:** The abstract attributes 320 infants to operative repair, while the body and participant flow give 152 early plus 129 late repairs, totaling 281.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article abstract vs REPORT main article flow and surgery narrative.
**Finding IDs:** F-NUM-001
**Checker provenance:** F-NUM-001; consolidated duplicate F-XS-001. Numeric N008, N029, N034, N065.
**Qualifying route:** Route B
**Classification rationale:** All conflicting counts are in the same REPORT article. The issue concerns an extractable operative-population count, so statistical_results applies.
**Classification ambiguity:** None; the retained population is an alternative interpretation of the abstract label, not another conflicting document role.

**Exact source locations:** REPORT [main PDF p. 1, Abstract Results](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1); [p. 3, Figure 1 repair/no-repair branches](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3); [p. 4, Patient Characteristics and Surgery Characteristics](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); [p. 5, Surgery Characteristics continuation](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5).

**Source evidence:** Abstract: 338 randomized and 320 underwent operative repair. Body: 152/163 early and 129/157 late underwent repair. Flow: early 147 before discharge plus 5 after discharge and 11 without repair; late 90 at the late threshold plus 39 before it and 28 without repair. Retained populations are 163 and 157; withdrawals total 18.
**Reported-versus-comparator:** 320 operative-repair infants versus 281 repaired retained infants; 320 instead equals 163+157 retained infants.
**Reasoning procedure:** Match counts of infants across mutually exclusive repair strategies, confirm independently using the flow branches, and preserve the possibility of a distinct abstract population/time window.
**Calculation:** 152+129=281; (147+5)+(90+39)=281; 163+157−11−28=281. Exact-count relative discrepancy is 39/320=0.121875. Conservative half-unit recomputed interval [280,282] versus abstract [319.5,320.5] leaves gap 37.5/320=0.1171875. Even all 18 withdrawals repaired gives only 299 among randomized infants; the supplied no-repair counts cannot bridge 320.
**Affected result or extracted value:** Overall number of infants undergoing repair and the population to which the abstract's accompanying demographic summary refers.
**Why context does not resolve it:** The retained population is inferable, but the abstract explicitly assigns 320 to operative repair. A data extractor cannot take both that count and the arm-specific repair counts as one coherent operative total.
**Alternative source-grounded interpretations:** The abstract may intend the retained population, or another operative population/window. No supplied statement defines a separate 320-repair population. No replacement value is proposed.
**Remaining human question:** Which population and observation window does the abstract's operative-repair statement describe, given the body and flow repair counts?

## C002 — Planned and reported primary and hospital-day analysis specifications

**Candidate statement:** The protocol, SAP and report describe different primary and hospital-day models; the report explicitly replaces the SAP's frequentist primary mixed model with GEE after nonconvergence.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R, P_P
**Compared document roles:** PLAN protocol vs PLAN SAP vs REPORT main article and results supplement.
**Finding IDs:** F-XS-002
**Checker provenance:** F-XS-002; consolidated duplicate F-ST1-001. Statistical S027, S028, S029.
**Qualifying route:** Route A, category 5
**Classification rationale:** REPORT analyses differ from PLAN specifications, and the supplied protocol/SAP also differ in model family/link. P_R takes precedence over P_P. The two REPORT locations corroborate the actual implementation and do not add S_C.
**Classification ambiguity:** The later SAP may intentionally supersede the protocol families; the report expressly explains its GEE fallback. Both disclosures remain attached to the candidate.

**Exact source locations:** PLAN [protocol PDF p. 13, lines 471–488, primary/hospital analysis paragraphs](../../joi240020supp1_prod_1710443209.74911.pdf#page=13); PLAN [SAP p. 7, lines 263–266](../../joi240020supp2_prod_1710443209.75411.pdf#page=7), [p. 8, lines 267–271](../../joi240020supp2_prod_1710443209.75411.pdf#page=8); REPORT [main p. 4, Statistical Analysis](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4), [p. 6, Table 2](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6); REPORT [results supplement p. 5, eTable 2 and model footnote](../../joi240020supp3_prod_1710443209.75411.pdf#page=5).

**Source evidence:** Protocol primary binomial GLMM with log link; hospital days lognormal with absolute differences. SAP binary logistic and count negative-binomial models, site random intercept and gestational-age group, same model for frequentist/Bayesian analyses. Report logistic mixed primary, negative-binomial hospital model, but frequentist primary GEE logistic with exchangeable site correlation because the mixed model did not converge.
**Reported-versus-comparator:** Protocol log-link/lognormal specifications versus SAP/report logistic/negative-binomial; SAP shared primary mixed model versus reported frequentist GEE replacement.
**Reasoning procedure:** Match outcome, 10-month time window and model-dependent reported quantities; compare family, link, center structure and effect measure without preferring an analysis.
**Calculation:** Qualitative model-specification comparison; display-precision intervals do not apply to differing model families/links. Affected printed effects include primary Bayesian RR 0.68/RD −7.9%, frequentist RR 0.65/RD −9.0%, and hospital-day RR 0.91.
**Affected result or extracted value:** Model attributed to the primary SAE and key-secondary hospital-day effects and their uncertainty intervals.
**Why context does not resolve it:** Route A category 5 retains replacement of a planned primary/key-secondary analysis. The GEE explanation is disclosed, but the originally planned frequentist mixed-model output is not reported.
**Alternative source-grounded interpretations:** The later SAP may supersede protocol families; GEE is a disclosed convergence-driven substitute. No preference among the coherent methods is proposed.
**Remaining human question:** Which dated specifications governed the final models, and which planned primary or hospital-day analyses were replaced or retained?

## C003 — Bayesian intervention and subgroup main-effect prior specifications

**Candidate statement:** The SAP and report give intervention-prior ranges that do not reconcile under display precision, and the protocol/SAP give different subgroup main-effect prior specifications.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R, P_P
**Compared document roles:** PLAN protocol and PLAN SAP vs REPORT main article prior specifications.
**Finding IDs:** F-XS-003
**Checker provenance:** F-XS-003; consolidated duplicate F-ST1-002. Statistical S030, S031, S032.
**Qualifying route:** Route B
**Classification rationale:** The intervention endpoints conflict between SAP PLAN and article REPORT. Distinct protocol/SAP subgroup main-effect distributions additionally involve P_P; P_R takes precedence. The protocol's general intervention range merely corroborates the article and does not itself create another report/plan conflict.
**Classification ambiguity:** The final implemented parameter-specific priors and the second-parameter convention of protocol N(0,1000) are not supplied. No convention or posterior change is inferred.

**Exact source locations:** PLAN [protocol p. 13, lines 486–498](../../joi240020supp1_prod_1710443209.74911.pdf#page=13); PLAN [SAP p. 8, lines 283–290](../../joi240020supp2_prod_1710443209.75411.pdf#page=8), [p. 9, lines 327–332](../../joi240020supp2_prod_1710443209.75411.pdf#page=9); REPORT [main p. 4, priors/modifier paragraphs](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4); affected REPORT results [main p. 6, Table 2/Figure 2](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6), [p. 8, Figure 3](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8).

**Source evidence:** SAP categorical intervention OR prior 0.2–4, Normal(0, SD 0.7) on log OR; count RR prior 0.33–3.3. Report categorical/count OR/RR prior 0.33–3.0. Protocol general final range 0.33–3.0; subgroup main effects N(0,1000), SD parameters Uniform(0,1000). SAP subgroup main effects reuse its primary priors, including specified GA/site distributions.
**Reported-versus-comparator:** Report 0.33–3.0 versus SAP categorical 0.2–4/count 0.33–3.3; subgroup main-effect prior families/scales differ between supplied plans.
**Reasoning procedure:** Compare priors for the same named outcomes and parameters, allow half-unit rounding of endpoints, and distinguish these source-copy discrepancies from within-SAP Normal-range diagnostics or interaction-prior rounding.
**Calculation:** Categorical lower intervals [0.15,0.25] versus [0.325,0.335]: gap 0.075/0.2=0.375. Categorical upper [3.5,4.5] versus [2.95,3.05]: gap 0.45/4=0.1125. Count upper [3.25,3.35] versus [2.95,3.05]: gap 0.20/3.3=0.060606. All exceed 0.05. Distinct subgroup distribution families are qualitative comparisons.
**Affected result or extracted value:** Primary Bayesian RR/RD and 97% benefit probability, hospital-day RR 0.91 and 82% benefit probability, subgroup posterior effects/probabilities.
**Why context does not resolve it:** Neutrality identifies the prior center without reconciling the spread or distribution. No supplied statement identifies which conflicting parameter-specific prior generated the reported posterior results.
**Alternative source-grounded interpretations:** The article may summarize protocol-level priors; the SAP may supersede subgroup priors; parameter scales may differ. No source establishes the actual implementation. The SAP internal Normal SD 0.7 and interaction SD 0.6 display comparisons were screened out and are not part of this candidate.
**Remaining human question:** Which parameter-specific intervention and subgroup main-effect priors were actually used, and how do the supplied ranges/distributions describe that implementation?

## C004 — Formal interim analysis information milestone

**Candidate statement:** The supplied amended plans specify a formal interim with approximately 200, or 200, infants' 10-month data; the article reports data for 309 infants at the formal interim.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol and PLAN SAP vs REPORT main article formal interim.
**Finding IDs:** F-XS-004
**Checker provenance:** F-XS-004; consolidated duplicate F-ST1-003. Statistical S040.
**Qualifying route:** Route B
**Classification rationale:** This is a REPORT-versus-PLAN statistical stopping-design comparison. Agreement between the two plans and between report stopping descriptions does not add another relationship.
**Classification ambiguity:** Protocol uses approximately; SAP specifies 200. Operational delay or an unsupplied amendment may explain the reported information size, but neither is established in the supplied evidence.

**Exact source locations:** PLAN [protocol p. 14, lines 519–530](../../joi240020supp1_prod_1710443209.74911.pdf#page=14), [p. 25, version 7 history, lines 979–982](../../joi240020supp1_prod_1710443209.74911.pdf#page=25); PLAN [SAP p. 4, lines 119–127](../../joi240020supp2_prod_1710443209.75411.pdf#page=4); REPORT [main p. 4, formal interim paragraph](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4), [p. 8, early-stopping limitation](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8).

**Source evidence:** Protocol one amended safety/efficacy review at approximately 200 10-month outcomes; SAP one formal review when 200 randomized infants' 10-month data available; report formal interim with data available for 309 in February 2021, 97% benefit probability exceeding the 95% threshold.
**Reported-versus-comparator:** Interim information count 309 versus planned 200; the reported efficacy probability crosses the stated threshold and is not itself a discrepancy.
**Reasoning procedure:** Compare the formal decision-point information population, preserving the approximate qualifier and separating it from recruitment calendars and final 308-outcome population.
**Calculation:** [199.5,200.5] versus [308.5,309.5] leaves gap 108/200=0.54. These counts do not reconcile under display precision; 97%>95% reconciles.
**Affected result or extracted value:** Information population underlying the primary benefit probability and early enrollment termination.
**Why context does not resolve it:** The stopping threshold is coherent, but no supplied amendment or operational account explains the changed formal information milestone. This concerns a planned decision rule, rather than a peripheral calendar.
**Alternative source-grounded interpretations:** Delayed analysis, a different meaning of available data, or an unsupplied amendment could explain 309. None is asserted as fact, and interim 309 is not forced to equal final 308.
**Remaining human question:** How was the planned 200-infant milestone implemented or amended, and what exact population generated the reported interim 97% probability?

## C005 — Planned primary and key-secondary analyses without supplied reported counterparts

**Candidate statement:** Several explicitly planned primary or key-secondary analyses have no result counterpart in the complete supplied article and results supplement.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol and PLAN SAP analyses vs REPORT main article and results supplement.
**Finding IDs:** F-XS-005, F-ST2-001
**Checker provenance:** F-XS-005 and independently included extension F-ST2-001; consolidated duplicate F-ST1-004. Statistical S046, S047, S048, S049, S050, S051, with S039 linked to developmental effect-size assumptions.
**Qualifying route:** Route A, category 5
**Classification rationale:** Explicit PLAN analysis specifications are compared with a completed REPORT search. Two agreeing REPORT documents do not create S_C; the planned primary/key-secondary nonreporting pattern is consolidated in one P_R candidate.
**Classification ambiguity:** The SAP permits future manuscripts as deemed necessary. Later publications are not supplied. Exploratory modifiers analyze the primary endpoint; hospital days are abstract-reported secondary, and death and BSIDIII are prespecified important secondary. The article explicitly says developmental assessment is ongoing; no completed developmental result or due date is inferred.

**Exact source locations:** PLAN [SAP p. 4, lines 133–149, modeled death](../../joi240020supp2_prod_1710443209.75411.pdf#page=4), [p. 5, lines 163–166, PP population](../../joi240020supp2_prod_1710443209.75411.pdf#page=5), [p. 8, lines 269–276, ≥3%/≥5% benefit](../../joi240020supp2_prod_1710443209.75411.pdf#page=8), [p. 9, lines 315–347, PP/modifiers/continuous GA](../../joi240020supp2_prod_1710443209.75411.pdf#page=9); PLAN [protocol p. 13, lines 490–500, modifiers](../../joi240020supp1_prod_1710443209.74911.pdf#page=13); alternative publication scope [SAP p. 2, lines 28–37](../../joi240020supp2_prod_1710443209.75411.pdf#page=2). REPORT counterparts/search: [main p. 4, methods and developmental deferral](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4), [p. 6, primary/hospital results](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6), [p. 7, Table 3 and heterogeneity](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7), [p. 8, Figure 3](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8); [results supplement p. 1, contents](../../joi240020supp3_prod_1710443209.75411.pdf#page=1), [p. 5, eTable 2](../../joi240020supp3_prod_1710443209.75411.pdf#page=5). Complete absence search covers main physical pp. 1–10 and results-supplement pp. 1–8, including all other flow/baseline/center/reference/acknowledgment pages.

**Source evidence:** Unconditional planned analyses: primary PP in addition to mITT; probabilities of at least 3% and 5% SAE reduction; primary maternal education ≤12, prenatal care, difficult-to-reduce hernia, sex, race/ethnicity and distance modifiers; hospital-day modifiers; continuous-GA primary association/interaction; modeled important-secondary death with frequentist/Bayesian uncertainty and probabilities; important-secondary BSIDIII overall and modifier effect estimates, intervals and probabilities. Reports show primary 159/149 ascertained-outcome infants, any-benefit 97%, GA/BPD/approach subgroups, overall hospital-day effects, and descriptive death 2 (1.3%) versus 3 (2.0%) only. Main p. 4 explicitly states that the 2-year neurocognitive assessment is ongoing and supplies no developmental effect; this known ongoing status is retained prominently.
**Reported-versus-comparator:** No supplied result for each named planned analysis, despite complete inspection of both REPORT sources. Available raw death counts, other subgroup effects and any-benefit probability are distinct outputs.
**Reasoning procedure:** Match each explicit analysis specification to every supplied REPORT page/display, distinguish unconditional specifications from conditional imbalance sensitivity, and preserve explicit developmental deferral. Pass 2 applied Route A category 5 without a disclosed-deferral exception; the new independent screen retained the developmental output absence as the same nonreporting pattern rather than a separate candidate.
**Calculation:** Qualitative absence comparison; no rounding calculation applies. All listed absences share the planned primary/key-secondary nonreporting pattern and form one candidate.
**Affected result or extracted value:** Primary robustness in PP, clinically important benefit probabilities, primary/hospital heterogeneity evidence, modeled key-secondary death inference, and reported status/result location of developmental overall/modifier inference. No unavailable cognitive effect is assigned a numerical value.
**Why context does not resolve it:** Route A category 5 retains planned primary/key-secondary analyses not reported and permits no CONTEXT_RESOLVES exclusion for a reproduced absence. Publication discretion and explicitly ongoing developmental assessment explain possible deferral but do not supply the planned quantitative outputs. Conditional imbalance sensitivity remains outside the pattern.
**Alternative source-grounded interpretations:** Developmental assessment is explicitly ongoing, directly supporting deferred reporting. Other analyses may appear in unsupplied future manuscripts, remain unperformed, have been replaced or omitted from publication; their status is not assumed. No conclusion that developmental results should already be available, and no preferred analysis, is proposed.
**Remaining human question:** Where are the planned primary/hospital/death outputs reported, or which were deferred, replaced or not conducted; given ongoing developmental assessment, what is the later status/result location of the planned BSIDIII overall and modifier inference?

**Pass-2 added affected locations:** PLAN [SAP p. 4, lines 129–149, developmental follow-up and important-secondary inference](../../joi240020supp2_prod_1710443209.75411.pdf#page=4), [p. 8, lines 267–276, continuous-outcome effects and intervals](../../joi240020supp2_prod_1710443209.75411.pdf#page=8), [p. 9, lines 318–332, developmental modifier inference](../../joi240020supp2_prod_1710443209.75411.pdf#page=9); PLAN [protocol p. 12, developmental assessment/sample-size paragraphs](../../joi240020supp1_prod_1710443209.74911.pdf#page=12), [p. 13, lines 481–484 and 490–500, linear model/modifiers](../../joi240020supp1_prod_1710443209.74911.pdf#page=13); REPORT [main p. 1, abstract result coverage](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1), [p. 4, Outcomes ongoing-assessment statement](../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4), main pp. 6–8 and results-supplement pp. 1/5 linked above. The completed absence search covers all 18 REPORT pages. The distinct fresh extension recheck reproduced these added facts without transcription or classification changes; ongoing assessment is expressly preserved.

## C006 — Protocol hospital-day median assumptions

**Candidate statement:** The protocol hypothesis prints expected early/late medians 18/15 days, while its power section gives 8/5 days; the SAP explicitly clarifies the intended medians as 8/5.

**Review domain:** plan_material
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN protocol hypothesis vs PLAN protocol power assumptions; PLAN SAP clarification.
**Finding IDs:** F-NUM-002
**Checker provenance:** F-NUM-002. Numeric N112, N114, N119. The cross/statistical checker context exclusions are reviewed again in pass 2 and audit, without creating duplicate IDs.
**Qualifying route:** Route A, category 2
**Classification rationale:** Conflicting arm-specific median assumptions are solely within PLAN material and concern sample-size/power assumptions. The SAP corroborates the power-section medians and discloses a clarification; it is not a REPORT comparator.
**Classification ambiguity:** None for document roles; the explicit SAP clarification is a source-grounded resolution of intended inputs retained for human review.

**Exact source locations:** PLAN [protocol p. 3, lines 105–109, specific aim](../../joi240020supp1_prod_1710443209.74911.pdf#page=3), [p. 12, lines 460–462, power assumptions](../../joi240020supp1_prod_1710443209.74911.pdf#page=12); corroborating PLAN [SAP p. 3, lines 73–80, clarification](../../joi240020supp2_prod_1710443209.75411.pdf#page=3); related power outputs [protocol p. 13, Table 4](../../joi240020supp1_prod_1710443209.74911.pdf#page=13), [SAP p. 4, lines 114–115](../../joi240020supp2_prod_1710443209.75411.pdf#page=4).

**Source evidence:** Expected median hospital days 18 early/15 late versus 8 early/5 late; power section separately gives means 18/13, lognormal distribution and 98% power. SAP explicitly clarifies medians as 8/5.
**Reported-versus-comparator:** Differing magnitude of arm-specific planned medians within the protocol; both pairs imply a three-day contrast.
**Reasoning procedure:** Match the same hospital-day median assumptions, distinguish mean/median labels and apply printed-copy half-unit intervals.
**Calculation:** Early [17.5,18.5] versus [7.5,8.5]: gap 9/18=0.5. Late [14.5,15.5] versus [4.5,5.5]: gap 9/15=0.6. Both exceed 0.05. Equal three-day contrasts do not reconcile the arm-specific magnitudes. No independent conflict in the power algorithm is inferred.
**Affected result or extracted value:** Planned arm-specific medians supporting the hospital-day hypothesis and power assumptions.
**Why context does not resolve it:** Route A category 2 retains a magnitude-changing printed value even when another supplied statement reconstructs the intended input. The SAP clarification remains explicit in this candidate.
**Alternative source-grounded interpretations:** The supplied SAP establishes intended medians 8/5; human review may consider that sufficient for extraction. The protocol's 18/15 median pair is not its 18/13 mean pair. No final correction is proposed.
**Remaining human question:** How should the printed protocol median assumptions and the SAP's explicit clarification be represented for extraction of the planned hospital-day inputs?
