# Statistical relationship inventory — PLAN two-pass shard

Fresh statistical pass 1; run model gpt-6.1-sol, high effort; runtime task /root/statistical_pass_1_plan. Scope is every statistical/method relationship in DOC-002 pp.1–55. REPORT material supplies matched counterparts only; its independent result relationships belong to the separate REPORT statistical shard. All thirty canonical relationships below are PASS_1_COMPLETE. All thirty records were independently revisited by fresh pass-2 agent root/statistical_pass_2_plan, gpt-6.1-sol/high, and are PASS_2_COMPLETE; complete per-record checks and all checker-exclusion reassessments are in checkers/parts/statistical_pass_2_plan.md. All PLAN source links are relative to this part file. PA/PB identifiers refer to the current fresh maps, never to prior findings.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Source-linked map inputs: extraction/parts/support_plan_a.md and support_plan_b.md. Direct Poppler 25.03.0 pdftotext -layout stdout confirmation covered DOC-002 pp.12–14,19–21,31–43; DOC-001 pp.1–4,7–8; DOC-003 pp.10–14. Direct source renders of DOC-002 pp.39,43 used CPU pdftoppm -f N -l N -scale-to 1500 -singlefile -png, producing preprocessing/stat_plan_confirm/plan-39.png and plan-43.png, then visually inspected. These derivatives use direct Poppler 25.03.0, CPU, without OCR. Remaining source units were covered through the complete fresh plan maps and their source-matched reusable text/image evidence. Every direct-source unit remains mapped; no scientific gap.

## Complete relationship records

### S201 — Prospective outcome hierarchy

**Evidence:** PLAN [p.7](../../../../joi180136supp1_prod.pdf#page=7), [p.13](../../../../joi180136supp1_prod.pdf#page=13), [p.31 §7.1](../../../../joi180136supp1_prod.pdf#page=31); PA-S001, PA-S007, PA-S014. Primary is mean daily-call stiffness; secondary IVR pain/weakness/fatigue, clinical myotonia, quantitative grip, INQoL, SF36, plasma mexiletine, biceps force, needle EMG, remaining-week/washout IVR. Other parameters: “Not applicable.” REPORT DOC-001 pp.2–4,7–8 lists stiffness as primary and other outcomes as secondary, while cautioning they should be interpreted as exploratory. Checked status separately from inferential caveat: the report still explicitly identifies secondary outcomes. Additional Timed Up&Go is disclosed as secondary but is not described as prespecified. Omission of non-key biceps/washout results is tracked as excluded observation, without equating absence with a printed status change. No emitted finding for this relationship.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S202 — Primary IVR acquisition/window

**Evidence:** PLAN [p.8](../../../../joi180136supp1_prod.pdf#page=8), [p.14](../../../../joi180136supp1_prod.pdf#page=14), [pp.15–17 Table1](../../../../joi180136supp1_prod.pdf#page=15), [p.31](../../../../joi180136supp1_prod.pdf#page=31); PA-S003, PA-S008, PA-S014 primary component. Weekly calls first two weeks and daily calls last two; exact primary weeks 3,4,8,9,14,15,19,20,25,26,30,31,36,37,41,42. REPORT DOC-001 p.3 frequentist period means use last two weeks. Primary window agrees; 31 analyzed sets ×28 expected calls=868 matches report p.4, confirming fourteen scheduled daily calls per arm/pair. PLAN assumed ten available observations per arm for simulation, not fourteen complete observations; these are different quantities. No finding.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S203 — Methodological objective and conventional-trial comparison

**Evidence:** PLAN [pp.10–11](../../../../joi180136supp1_prod.pdf#page=10); PA-S004. Primary methodological objective and secondary clinical objective differ from endpoint hierarchy, which independently identifies stiffness. REPORT DOC-001 pp.1–4 addresses effectiveness and comparison with previous RCT using frequentist reanalysis. Objective wording is not a different primary quantitative endpoint; no numerical conflict. No finding.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S204 — N-of-1 analysis unit and repeated design

**Evidence:** PLAN [p.7](../../../../joi180136supp1_prod.pdf#page=7); PA-S002. Adult genetically confirmed NDM, double-blind randomized within-patient placebo crossover, aggregated Bayesian analysis. REPORT DOC-001 pp.2–3 has the same within-patient unit. Dependent secondary tests and patient-level aggregation do not contradict the repeated design merely because they differ from the planned model; planned specification differences are separately tracked in S223/S225/S226. No independent finding.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S205 — Prespecified informative/noninformative robustness comparison

**Evidence:** PLAN [p.12](../../../../joi180136supp1_prod.pdf#page=12), [p.41](../../../../joi180136supp1_prod.pdf#page=41); PA-S005 robustness component and S-PB11. Both explicitly promise comparison/replacement of elicited clinical priors with noninformative priors. REPORT primary Bayesian code uses noninformative priors; supplied report results have no alternate clinical-prior analysis or comparison. The protocol simulation's clinical/noninformative performance table is planning evidence, not a sensitivity result on observed data. Finding F-ST1-202, Route A category5, primary sensitivity analysis not reported. Primary prior specification itself is separately F-ST1-201.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S206 — Treatment-order randomization

**Evidence:** PLAN [p.12](../../../../joi180136supp1_prod.pdf#page=12), [p.31](../../../../joi180136supp1_prod.pdf#page=31); PA-S006. Computer-generated order of active/placebo within each set, pharmacy kits. REPORT DOC-001 p.2 specifies block randomization by set. No contradiction in unit or order; unspecified block size alone supplies no finding. Random invitation sampling (S229) is distinct.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S207 — Eligibility and prebaseline washout

**Evidence:** PLAN [pp.18–19](../../../../joi180136supp1_prod.pdf#page=18), [p.13](../../../../joi180136supp1_prod.pdf#page=13), [p.22](../../../../joi180136supp1_prod.pdf#page=22); PA-S009. Age≥18, genetically confirmed chloride/sodium NDM; listed neurological/cardiac/other exclusions. Prior-drug minimum washouts five, three, or two days by drug. REPORT DOC-001 p.2 uses a two-week prebaseline washout. A longer washout satisfies the printed protocol minima; source is not an exact two-/three-/five-day maximum. eTable1 has additional criteria disclosed; no demonstrated change to an analysis denominator from eligibility definitions. No finding; no clinical-design preference applied.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S208 — Simulation design and observation count

**Evidence:** PLAN [p.19](../../../../joi180136supp1_prod.pdf#page=19); PA-S010. 1000 realizations; 30 patients; two arms ×10 observations/arm/pair ×2 or3 pairs=40 or60 observations/person, 1200 or1800 overall. Simulation random intercept, slope and common residual; no formula-based sample-size claim. Observation arithmetic reproduces. Report's later simulation expressly post hoc and includes response-dependent stopping; its 69% power does not purport to be this design-prior expected probability. No finding.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S209 — Simulation priors, parameter inputs and truncation

**Evidence:** PLAN [pp.19–20](../../../../joi180136supp1_prod.pdf#page=19), [p.41](../../../../joi180136supp1_prod.pdf#page=41); PA-S011, PA-N007/008. Placebo4.62; intercept SD2.19; slope SD1.77; residual SD0.827; clinical mean-effect normal mean1.75, SD0.89 (p.41 resolves p.20 notation). Values truncated to1–9. Clinical difference0.75/2.19=0.3425, reproducing printed effect size0.34. Design prior draws mean effect, analysis prior can differ; fixed effects expressly omitted in simulation because reference estimates lacked subgroup/center distinctions. No internally contradicted simulation method. Full output cannot be regenerated without code/random-number sequence, not a finding absent a printed conflicting result.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S210 — Four planning outputs, missing-data scenario and evidence cutoff

**Evidence:** PLAN [p.21](../../../../joi180136supp1_prod.pdf#page=21); PA-S012, PA-N009. Clinical-prior expected probabilities0.817/0.821 and vague-prior0.782/0.784 for two/three completed pairs; two priors ×two counts=4 scenarios. Vague analysis prior N(1.75,10) leaves design prior unchanged. These are expectations of Pr(mean effect>0.75), not frequentist power nor individual probabilities. Two/three pairs anticipate incomplete data while1–4 actual pairs allowed. “Similar” to0.8 is not a stated requirement each planning output≥0.8. Table's “treatment periods” versus repeated prose “pairs” is a resolvable label inconsistency tracked in excluded table. No finding.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S211 — Compliance measurement

**Evidence:** PLAN [pp.30–31](../../../../joi180136supp1_prod.pdf#page=30); PA-S013. Pill counting and drug accountability, no adherence-based primary analysis exclusion specified. REPORT DOC-001 p.8 gives mean adherence94% and two patients<75%; the disclosed adherence measure does not itself contradict the analysis population. No invented per-protocol cutoff. No finding.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S212 — Blinding/decoding and sequential advice

**Evidence:** PLAN [p.31](../../../../joi180136supp1_prod.pdf#page=31), [p.41](../../../../joi180136supp1_prod.pdf#page=41); PA-S015. Individual trial blind; code after all completion except SAE; treatment-blinded statistician interim advice. REPORT DOC-001 pp.2–3 describes blinded staff and ongoing interim advice. Individual decision based on posterior effect while trial blind is not alone a contradiction: code labels can preserve anonymity of named treatments. No finding on an assumed decoding procedure; missing implementation detail precisely listed in excluded observations.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S213 — IVR severity/frequency, scale and effect direction

**Evidence:** PLAN [p.31](../../../../joi180136supp1_prod.pdf#page=31); PA-S016. Severity ordinal1–9 and frequency hours for stiffness/pain/weakness/fatigue. REPORT DOC-001 p.3 uses severity1–9 with9 worst, positive placebo-minus-mexiletine reduction. Mean primary severity and normal model are explicitly stated; no general critique of normal treatment of ordinal data. Frequency not reported is non-key outcome omission without a conflicting value. No finding.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S214 — Quality-of-life instruments

**Evidence:** PLAN [p.32](../../../../joi180136supp1_prod.pdf#page=32); PA-S017 instrument component. Disease-specific INQoL and Dutch SF36. REPORT DOC-001 pp.3,7–8 uses these instruments. The plan supplies no conflicting numeric composite-score aggregation or component scaling; unprovided scoring formula is not independently a finding. Report-only scale/range checks remain in REPORT shard.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S215 — Clinical action myotonia measurement definition

**Evidence:** PLAN [p.32](../../../../joi180136supp1_prod.pdf#page=32); PA-N018 and PA-S017 boundary. Eye closure and fist contraction three seconds, five attempts, relaxation time seconds; percussion two sites. REPORT DOC-001 p.3 and p.8 Table2 footnote h specify forceful contractions five seconds for eye/hand relaxation. Three versus five seconds is a printed measurement-definition change, not an effect-size rounding comparison. Combined with S216 as F-ST1-204, repeated pattern of changed quantitative myotonia definitions. Percussion outcome omission is non-key, excluded separately from definition mismatch.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S216 — Quantitative handgrip relaxation/warm-up definition

**Evidence:** PLAN [pp.32–33](../../../../joi180136supp1_prod.pdf#page=32); PA-S017 continuation, S-PB01. Three-second MVIC, five contractions with ten-second rest, three sets with ten-minute rest. Relaxation cutoffs90→10%,90→50%,90→75%, first/final for warm-up. REPORT DOC-001 pp.3,7–8 specifies90→5% relaxation, first/fifth/mean of five trials. Endpoint lower cutoff5% is not one of the three prespecified cutoffs; F-ST1-204 with S215. No invented covariance, extra-set aggregation or scaling assumptions.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S217 — Biceps force secondary endpoint

**Evidence:** PLAN [p.34](../../../../joi180136supp1_prod.pdf#page=34); S-PB02 biceps component. Peak of three MVCs defines maximum; isometric contractions60%MVC≥30seconds and ten-minute rest. Report handgrip peak/transient paresis is a different disclosed construct and is not explicitly asserted to be the biceps assay. The biceps endpoint is prespecified secondary, not key secondary by this package's hierarchy/abstract; no reported biceps result. Excluded non-key omission; no finding that treats handgrip as a misattributed biceps result.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S218 — Needle EMG ascertainment/grade

**Evidence:** PLAN [p.34](../../../../joi180136supp1_prod.pdf#page=34); S-PB02 EMG component. Rectus femoris; discharges≥500ms in≥3 nonendplate areas;1+/2+/3+ thresholds. REPORT DOC-001 pp.3,8 describes ten insertions,30seconds each and0–3 grading with3 every insertion. Zero provides no-discharge category;1+/2+/3+ wording is compatible with report's abbreviated criteria reference. No numeric threshold explicitly contradicted by addition of insertion details. No finding.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S219 — Primary analysis population and withdrawal data

**Evidence:** PLAN [p.35 §7.5](../../../../joi180136supp1_prod.pdf#page=35); S-PB03. Intent-to-treat includes all pretermination data unless consent withdrawn. REPORT DOC-001 p.3 limits aggregation to≥1 completed treatment period; p.4 analyzes27 completers of30 randomized and excludes3 withdrawals. Primary eligibility rules differ as printed; data availability/consent for withdrawn patients is not defined in supplied evidence. Finding F-ST1-203, Route B, records specification difference without asserting unavailable raw data or benefit bias. No imputation rule is demanded beyond sources.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S220 — Whole-study versus individual stopping

**Evidence:** PLAN [p.35 §7.7](../../../../joi180136supp1_prod.pdf#page=35), [p.43](../../../../joi180136supp1_prod.pdf#page=43); S-PB04. Whole study can stop for objectives/safety/DSMB; no combined-trial efficacy interim decision. Individual posterior analyses advisory. REPORT DOC-001 p.4 retrospectively notes>95% benefit after first11 patients; no assertion that recruitment stopped at11, and30 enrolled. Retrospective sequential plot is not a contradiction of no whole-study efficacy stopping. No finding.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S221 — Adverse events and full safety population

**Evidence:** PLAN [pp.36–38](../../../../joi180136supp1_prod.pdf#page=36); S-PB05. All spontaneous/observed events irrespective of relatedness, SAE categories, AR/SUSAR definitions; complete research population safety analysis. REPORT DOC-001 p.8 and DOC-003 p.6 uses30 for safety including the withdrawn SAE patient; agrees with complete randomized research population despite27 efficacy patients. Administrative seven/eight/fifteen-day reporting schedules are not efficacy windows. No finding.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S222 — DSMB safety decision triggers

**Evidence:** PLAN [p.38](../../../../joi180136supp1_prod.pdf#page=38), [p.39 Figure3](../../../../joi180136supp1_prod.pdf#page=39); S-PB06. Source-render confirmed text requires study-related SAEs≥10%(three patients) or≥2 same cardiac events; figure requires cardiac AE/SAEs>10%(three patients) or≥2 same cardiac events. ForN30,3/30=10% and4/30=13.33%; event class and inequality differ. F-ST1-206, Route B, planned safety decision rule. Individual ECG/drug triggers and unblinding retained: QT>500ms,QRS>150ms, serious conduction changes, serum>2µg/mL or0–0.25µg/mL. No reported false stop/continue assertion inferred from one SAE or subtherapeutic drug values.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S223 — Planned primary hierarchical model/covariates

**Evidence:** PLAN [p.40 §9.1](../../../../joi180136supp1_prod.pdf#page=40); S-PB07. Patient random intercept/slope; common within-person residual; subgroup chloride versus sodium types1/2 and center fixed effects. REPORT DOC-001 p.3 and DOC-003 pp.11–14 specify arm-specific patient means, total group and binary-genotype hierarchical code, common within-person variance. Random intercept/slope and arm-specific patient means may be alternate parameterizations; no unknown covariance equivalence imposed. Clear documented prior changes are F-ST1-201 with S226; planned separate sodium subtypes versus binary reported grouping is F-ST1-208. Center omission in a reported single-center study has directly disclosed context rather than an independent finding.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S224 — Treatment-pair/order interactions

**Evidence:** PLAN [p.40](../../../../joi180136supp1_prod.pdf#page=40); S-PB08. Will investigate interactions of treatment effect with pair and order. REPORT DOC-001 pp.3–4 describes candidate randomization-order and period covariates excluded atP≥.10, resultsP=.85/.22, without a treatment-by-order/pair term shown. Planned primary interaction analyses not identifiable in supplied reported specification; F-ST1-207. Human question is whether reportedP values are interaction or main-effect terms; no assumption of term identity from names alone.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S225 — Planned secondary Bayesian analyses

**Evidence:** PLAN [p.40](../../../../joi180136supp1_prod.pdf#page=40); S-PB09. “The secondary endpoints will be analyzed in the same way.” REPORT DOC-003 p.8 displays Bayesian posterior symptoms pain/weakness/tiredness; DOC-001 pp.3–4 and Table2 additionally disclose frequentist reanalysis (mixed effects for IVR, dependent t for other measures). Primary conventional-trial comparison is expressly planned (S203), so additional frequentist comparisons are not automatically a contradicted primary method. No non-IVR Bayesian results supplied, but these are not key secondary outcomes here; excluded observation records their omission exactly. No independently emitted finding.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S226 — Primary priors and sequential updating

**Evidence:** PLAN [pp.40–41](../../../../joi180136supp1_prod.pdf#page=40); S-PB10. Clinical priors for individual/overall effects, near-noninformative remaining parameters; mean parameters normal largeSD (placebo example mean5,SD10); variance inverse gamma shape=scale0.001; mean-effect clinical prior mean1.75,SD0.89; elicited individual2.5th/97.5th percentiles. Posterior after earlier pair becomes next prior. REPORT DOC-003 pp.10–14 uses normal mean priors precision0.001 (SD31.6228; total means centered4) and uniform0.01–10 SD priors, no elicited mean-effect prior. F-ST1-201 concerns the explicit variance-prior family difference only; individual interim noninformative mean priors agree with PLANp.42. Primary clinical/noninformative robustness result omission is separately S205/F-ST1-202. Normal/inverse-gamma conjugacy does not, without full implementation, establish a conflicting reported number, so no generic conjugacy critique emitted.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S227 — Clinically relevant threshold and individual stopping boundaries

**Evidence:** PLAN [pp.41–43](../../../../joi180136supp1_prod.pdf#page=41), [p.48](../../../../joi180136supp1_prod.pdf#page=48); S-PB12. q=Pr(individual effect>0.75); stop adviceq≥.80 orq≤.20, otherwise continue, after pairs1–3; patient/physician discretion and no whole-study efficacy interim. REPORT DOC-001 p.3 says>.80/<.20, remaining continue; no observed individual exactly on.80/.20, so equality-wording alone changes no reproduced decision. Margin0.75 agrees; reported clinical effect size0.43 uses different explicitly reported natural-historySD1.75, rather than planningSD2.19. No finding on this context-resolved standardization. Individual exception rules/results independently checked in REPORT shard.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S228 — Interim noninformative-only text versus informative-prior arrows

**Evidence:** PLAN [p.42](../../../../joi180136supp1_prod.pdf#page=42), [p.43 Figure4](../../../../joi180136supp1_prod.pdf#page=43); S-PB13. Text expressly limits interim analyses to noninformative priors only; directly rendered Figure4 has “+informative priors” arrows into first discontinuation and second effectiveness decision paths. This concerns stopping computation itself, not just LR terminology. F-ST1-205, Route B, P_P/plan_material. No numeric LR interpretation or named prior parameter inferred from diagram.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S229 — Sample size, genotype strata and centers

**Evidence:** PLAN [pp.44–46](../../../../joi180136supp1_prod.pdf#page=44), [p.12](../../../../joi180136supp1_prod.pdf#page=12), [pp.19–21](../../../../joi180136supp1_prod.pdf#page=19); S-PB14. Target30=20Nijmegen+10Maastricht; strata15chloride+7PMC+8SCM=30. Nijmegen invitations15+10+10=35, distinct from enrollment. Two ten-patient cohorts onp.12 correspond to Nijmegen20 before later Maastricht10; p.45 specifies this sequencing. REPORT30 single-center, actual genotype19/11, not the designed allocation15/15. No reported claim of random equal genotype allocation; invitation strata not treatment arms. Center/calendar differences do not change30 target or a reproduced decision. Excluded apparent cohort/sample and subtype label observations; no primary model finding solely for absent center in a one-center report.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

### S230 — Randomized intervention, sets and assessment timing

**Evidence:** PLAN [pp.7–8](../../../../joi180136supp1_prod.pdf#page=7), [pp.12–17](../../../../joi180136supp1_prod.pdf#page=12), [p.22](../../../../joi180136supp1_prod.pdf#page=22), [p.30](../../../../joi180136supp1_prod.pdf#page=30); PA-N001–006,PA-N010/017. One–four sets, each4+1+4+2=11weeks, minimum11maximum44;200mg1×day1,2×day2,3×remaining days, maintenance600mg/day. REPORT same4-week arms,washout1week,11-week sets and200mgTID. Abbreviated maintenance dose does not assert absent titration. Clinical visits at starts/ends of arms per plan table; report's4-week “set” wording is context-resolved to period by its11-week set definition. Follow-up planned3months versus extended reported18–31months is not a primary/keysecondary endpoint change. No finding.

**Pass 1:** PASS_1_COMPLETE. **Pass 2:** PASS_2_COMPLETE. Fresh independent PLAN pass 2 revisited count/denominator, estimate/test, method, cross-source and mechanical-recheck implications; see the explicit S-ID row in checkers/parts/statistical_pass_2_plan.md. No new finding.

## Partition and completeness

PA-S001/007/014 hierarchy consolidate inS201; PA-S003/008 primary acquisition inS202; PA-S004→S203; PA-S002→S204; PA-S005 robustness plusPB11→S205 (RCT comparison inS203); PA-S006→S206; PA-S009→S207; PA-S010→S208; PA-S011→S209; PA-S012→S210; PA-S013→S211; PA-S015→S212; PA-S016→S213; PA-S017 instrument/measurement boundary→S214–S216. PB01→S216; PB02 splits biceps/EMG→S217/S218; PB03→S219; PB04→S220; PB05→S221; PB06→S222; PB07→S223; PB08→S224; PB09→S225; PB10→S226; PB12→S227; PB13→S228; PB14→S229. Numeric design/dose/timing definitions that govern statistical relationships are retained inS230. Administrative/background PLAN pages are covered by the maps but do not instantiate current-trial inferential results. Historical OR/CI/P examples onp.29 reconcile null/significance directions and have no operative trial statistical design relation; no candidate discovery used external literature.

Thirty relationships; eight findingsF-ST1-201–F-ST1-208; every relationship explicitly checked. No scientific coverage limitation. Source-level raw patient measurements, analysis execution logs and prior-elicitation forms are not supplied; missing definitions are named where relevant, without assuming them.
