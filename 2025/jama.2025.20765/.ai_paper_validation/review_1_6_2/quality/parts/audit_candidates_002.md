# Quality audit part: C008–C013

Runtime ID: `01a12c70-9043-7552-8bc3-bac08204fa08`. Fresh quality-control audit specialist; model `gpt-6.1-sol`; reasoning effort `high`. Assigned stable IDs: C008, C009, C010, C011, C012, C013. All remain Pending Human Adjudication. Scope complete: six of six assigned cards, eleven mapped initial finding decisions, and their relevant checker exclusions and statistical-pass-2 facts. Inclusion audit: five CONFIRMED, one QUESTIONED. No newly qualifying unregistered finding is emitted. No stable ID is deleted, merged, suppressed, ranked, or assigned a scientific disposition.

Read the complete QUALITY_CONTROL_SCOPE.md; current candidate part candidates_002.md; exact-source recheck part recheck_002.md; inclusion_screen.md; source_confirmation_plan.md; statistical_pass_2b.md and statistical_pass_2c.md; relevant original numeric, cross-source and statistical-pass-1 findings/exclusions; and the card requirements in report_spec.md. Current-run source confirmations, rather than earlier scientific conclusions, supplied evidence. Discovery and inclusion were assessed from the cited supplied-source relationships without a finding-count target. No web, raw-data assumptions, or custom Python were used.

Sixteen distinct existing source-page renders were visually revisited: DOC-001 PDF pp. 3, 5, 6, 8; DOC-002 pp. 28, 48, 62, 63, 83, 91, 92, 93; DOC-003 pp. 6, 12, 13, 15. Existing current-source confirmations cover other cited pages. Image locators are preprocessing/cross_main_{3,5,8}.png; st1-main-006.png; cross_plan_{28,48,62,63,83,91,92,93}.png; cross_supp_{6,12}.png; numeric_support_p013.png; and recheck002_supp_015.png, relative to review_1_6_2. No fresh render or OCR was generated. The source PDFs remain authoritative. These PDF links use four parent directories from this part; the coordinator must rebase them when merging the canonical quality artifact.

## C008 — CO<6 sensitivity results in primary-outcome blocks

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C, S_W

**Compared document roles:** PLAN DOC-002 p.84 primary definition vs REPORT DOC-001 p.6 and DOC-003 p.13 primary blocks; REPORT DOC-001 p.3 sensitivity statement

**Evidence state:** reproduced_after_transcription_correction

**Inclusion audit:** QUESTIONED

The printed headings and threshold descriptions reproduce, but an actual change of outcome status under Route A, category 5 is not established. Main methods explicitly call CO<6 a post hoc sensitivity performed for the primary outcome; eTable 9 explicitly identifies its entire display as post-hoc sensitivity. Grouping sensitivities of the primary construct under a primary-outcome block can reconcile the cited locations at once. The cited sources do not state that CO<6 became a prespecified primary endpoint. Thus the Route A5 premise depends on interpreting a block heading as formal endpoint hierarchy, and Route B2 is not established by these immediate contexts. This is an inclusion audit question, not a change to the original INCLUDE decision or the stable candidate's status.

**Finding IDs:** F-ST1-008

**Qualifying route:** Route A, category 5

This is the registered route; its status-change premise is questioned above.

**Exact source locations:** [REPORT DOC-001 PDF p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Trial Outcomes and Statistical Analysis; [REPORT DOC-001 PDF p.6](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table 2, both CO<6 ITT and PP rows within the Primary outcome block; [PLAN DOC-002 PDF p.84](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=84>), primary definition, lines 2653–2669; [REPORT DOC-003 PDF p.13](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable 9 title and Primary outcomes block.

**Source evidence:** The plan primary endpoint uses CO<10 ppm. Main methods specify post hoc CO<6 sensitivity for the primary outcome. Main Table 2 includes CO<6 ITT 264/720 versus 38/360 and CO<6 PP 264/667 versus 39/318 in its primary block. The PP usual-care count is literally 39/318, with printed 11.9%; preserve both. eTable 9 is titled Post-hoc sensitivity analysis (intention to treat) after excluding deaths, and prints CO<6 264/695 versus 38/333 under Primary outcomes. All three affected CO<6 rows belong in the existing pattern; none is independently re-emitted.

**Calculation:** Categorical status labels have no rounding calculation. The nearby PP count/percentage does not independently qualify: 100×39/318=12.264151%; half-unit input range 100×[38.5/318.5,39.5/317.5]=[12.087912,12.440945]%, versus printed [11.85,11.95]%; gap 0.137912/11.9=0.011589≤0.05. ITT 38 and PP 39 numerator half-unit intervals touch at 38.5; no positive precision gap or participant reclassification is established.

**Classification rationale:** Roles follow content: prospective SAP is PLAN, trial tables/methods are REPORT. The registered status comparison generates P_R, S_C and S_W, with P_R taking precedence and protocol_report following that type. Preserve these registered fields while carrying the ambiguity below; the underlying formal-status interpretation is not independently confirmed by this audit. The recheck's p.6 location correction and addition of S_W are supported, so its evidence state remains reproduced_after_transcription_correction.

**Classification ambiguity:** If primary blocks merely group analyses of the primary construct, the plan corroborates the CO<10 endpoint rather than providing a conflicting status statement. P_R and the cross-report status comparison therefore depend on the same unestablished formal-hierarchy reading. No hierarchy promotion, prespecification claim, or implemented threshold change is inferred.

**Affected result or extracted value:** Outcome-status metadata accompanying the two main CO<6 rows and the supplementary death-excluded CO<6 row. This audit establishes no consequence for their numerical estimates or the primary CO<10 efficacy conclusion.

**Missing inputs and alternatives:** The intended block convention is not defined explicitly; the source-grounded primary-construct grouping explanation is immediate and material. Preserve it fully. Required repair: retain printed PP 11.9% alongside 39/318 and expand the inclusion/classification audit reason. No source-based correction to any printed cell is proposed.

**Potential downstream evidence impact:** If the formal status discrepancy is confirmed, a data extractor could attach primary rather than post hoc sensitivity metadata to these three rows. This is a conditional metadata implication; no propagation or conclusion change is established.

## C009 — Protocol MAR wording versus SAP/report missing-as-smoking

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP p.91 and REPORT DOC-001 pp.3,4

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

Reproduced and qualifying by Route B. B1: missing-outcome handling for the primary ITT is focus D. B2: the separately headed protocol outcomes paragraph says MAR, while SAP/report assign missing primary outcomes nonabstinent status, without an outcome-specific mapping or replacement hierarchy. Adjacent economic text is a plausible restriction but does not expressly restrict the paragraph. B3: the missingness assumptions attached to primary ITT 300/720 versus 55/360 and RR 3.0 [2.0,4.9] could differ in extraction or interpretation. The observation is a printed specification contrast, not merely an absent imputation detail.

**Finding IDs:** F-XS-002, F-ST1-004

**Qualifying route:** Route B

**Exact source locations:** [PLAN DOC-002 PDF p.28](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=28>), lines 759–764, separately headed Statistical analysis; [PLAN p.66](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=66>), lines 2011–2016, corresponding paragraph; [PLAN SAP p.91](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=91>), lines 2890–2892; [REPORT DOC-001 PDF p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), missing-primary handling; [REPORT p.4](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure 1 denominators.

**Source evidence:** Both protocol passages use missing-at-random architecture for outcomes; SAP regards dropout or incomplete primary data as continuing smokers; the report treats missing primary outcome data as negative/not abstinent and discards them in a separate complete-case analysis. Repeated protocol statements form one candidate. Source p.28 carries a V6.0 header; physical bundle order alone supplies no applicable-plan hierarchy.

**Calculation:** No numeric mismatch is asserted. 720−53=667, 360−42=318, 53+42=95 and 720+360=1080 reproduce the reported primary/complete-case population relationship. Rounding does not govern the categorical missing-data specification.

**Classification rationale:** Prospective protocol and SAP passages are PLAN; article methods/flow are REPORT. Protocol versus report yields P_R; protocol versus SAP yields P_P. P_R precedes P_P and fixes protocol_report. The flow only corroborates retained denominators; it creates no additional relationship. Evidence state reproduced is supported by the direct-source recheck.

**Classification ambiguity:** MAR and deterministic smoking status can apply to distinct analyses; the source does not map their scope. Economic adjacency and possible SAP supersession are retained alternatives, rather than inferred chronology.

**Affected result or extracted value:** Missing-outcome architecture accompanying the primary ITT RR 3.0 [2.0,4.9]. No changed numerical RR, bias direction, or efficacy conclusion is calculated.

**Missing inputs and alternatives:** Outcome-specific MAR applicability, any relevant imputation model/variables, and a disclosed applicable-plan replacement mapping are absent. Economic-only MAR or SAP replacement could explain the contrast. Current evidence-card core fields are complete; preserve these bounds in the report's reasoning and mechanical-recheck fields.

**Potential downstream evidence impact:** If confirmed, an extractor could record MAR-based handling or missing-as-smoking handling for the primary ITT. No model result under an alternative handling rule is available.

## C010 — Planned male/female primary treatment-effect analyses

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SAP pp.92,93,99 vs REPORT DOC-001 pp.3,5 and DOC-003 p.12

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

Reproduced and qualifying by Route A, category 5: an explicitly planned subgroup analysis of the primary treatment effect is not reported in the complete supplied subgroup results or matched main narrative. This is distinct from omission of ancillary non-key secondary outcomes. The SAP anticipates disclosure of unavailable confidence intervals, so sparse enrollment does not supply an observed removal or nonestimation explanation.

**Finding IDs:** F-XS-004, F-ST1-006

**Qualifying route:** Route A, category 5

**Exact source locations:** [PLAN DOC-002 PDF p.92](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines 2936–2939; [PLAN p.93](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=93>), gender/model/disclosure lines 2940–2952; [PLAN p.99](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=99>), blank Gender Male/Female shell; [REPORT DOC-001 PDF p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), planned subgroup list; [REPORT p.5](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), results narrative/baseline; [REPORT DOC-003 PDF p.12](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=12>), complete eTable 8.

**Source evidence:** SAP specifies primary-treatment sensitivity models by gender male/female, each with site random intercept, RR/95% CI and disclosure of missing CIs. The complete report subgroup display contains age, education, occupation, smoking duration and reading SMS, without gender. Baseline males 698/720 and 345/360 imply females 22 and 15. The blank SAP shell corroborates planning; it is PLAN rather than a report with missing results. The sex covariate RR 0.83 [0.34,2.02] in eTable 7 is a predictor association, not the planned male/female treatment contrasts.

**Calculation:** Match planned subgroup analyses to reported treatment-effect rows, preserving their estimand distinction from a covariate association. No numeric discrepancy or rounding calculation concerns absence of the planned analyses.

**Classification rationale:** PLAN SAP versus REPORT methods/results gives P_R and protocol_report. Main/supplement omissions agree; there is no S_C discrepancy. The recheck establishes cited plan wording and absence at complete report displays, supporting reproduced. One issue contains both male/female planned rows and both checker findings.

**Classification ambiguity:** Absence is bounded to the complete supplied report package; it does not establish that an analysis was never performed.

**Affected result or extracted value:** Planned sex-specific primary treatment RRs/CIs and the reported scope of primary-effect stability checks.

**Missing inputs and alternatives:** Sex-specific abstinence counts and treatment-model outputs, estimability information, and an omission/removal explanation are unavailable. Sparse female observations could impede estimation; completed-but-omitted analysis or an amendment are possible, unobserved explanations. No direction of a missing estimate or change to the overall effect is inferred.

**Potential downstream evidence impact:** If confirmed, an extractor could describe the planned sex-specific sensitivity as unavailable or omit it from the recorded primary robustness scope. No supplied sex-specific treatment estimate is imputed.

## C011 — Ten versus twenty percent primary-data attrition inputs

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.48,62 vs PLAN DOC-002 pp.63,64,83 and REPORT DOC-001 p.3; PLAN DOC-002 p.77 amendment context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

Reproduced and qualifying by Route B. B1: attrition allowance is focus D and is attached to the reported primary sample-size/power rationale. B2: 10% appears in combined-plan overview and statistics introduction, while both phase-specific calculations and the SAP combined overview use 20%; no explicit differing definition or surviving-input hierarchy reconciles them. B3: a reader could extract 10% or 20% as the attrition assumption supporting the 1080-participant, 90%-power primary design. Amendment context changes sample sizes but does not expressly reconcile these percentages.

**Finding IDs:** F-XS-010, F-ST1-010

**Qualifying route:** Route B

**Exact source locations:** [PLAN DOC-002 PDF p.48](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=48>), lines 1344–1347; [PLAN p.62](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=62>), lines 1861–1863; [PLAN p.63](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=63>), Phase 3 lines 1894–1898; [PLAN p.64](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=64>), Phase 4 lines 1936–1938; [PLAN p.77](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>), sample-size amendment context; [PLAN SAP p.83](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=83>), lines 2624–2638; [REPORT DOC-001 PDF p.3](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), sample-size paragraph.

**Source evidence:** Protocol combined total 2716 states 10% without primary outcome data; Phase 3 and Phase 4 state 20%, with expressly additive calculations 587+(587×0.2)=704 and 864+(864×0.2)=1036. SAP combined overview and Phase 3 explanation use 20%; report says anticipated 20% attrition in deriving 1080 participants. Amendment changes Phase 3 888→1080 and Phase 4 1480→1620. Repeated passages form one input-assumption candidate; the separate phase is supporting context, not an enlarged efficacy claim.

**Calculation:** Printed percentage intervals [9.5,10.5]% and [19.5,20.5]% have gap 9 percentage points; gap/reference 9/10=0.90>0.05. The specified additive rule is coherent and is not challenged. Distinct nearby product departures remain within precision: 704±0.5 times 1.50±0.005 gives [1051.7325,1060.2725], versus 1080±0.5, gap 19.2275/1080=0.017804. 1036±0.5 times 1.56±0.005 gives [1610.2025,1622.1225], overlapping 1620±0.5. The printed Phase 4 DE copies 1.50±0.005 and 1.56±0.005 give gap 0.05/1.50=0.033333. These exclusions do not remove the distinct 10%/20% input comparison.

**Classification rationale:** Protocol versus SAP/detail inputs yields P_P; 10% protocol versus 20% report yields P_R. P_R takes precedence and fixes protocol_report. The amendment is PLAN context; it is not a separate conflicting relationship. The exact-source recheck supports reproduced.

**Classification ambiguity:** Combined-study missingness could have a separate definition, or 10% could be a retained overview input. No final hierarchy is inferred solely from bundle order, labels, or surviving prose. Describe these as supplied-plan passages rather than claim an undisclosed chronological precedence.

**Affected result or extracted value:** Attrition input attached to the reported 1080-participant primary design and 90% power; no alternative achieved power or numerical primary effect is calculated.

**Missing inputs and alternatives:** Applicable dated input hierarchy and any definition distinguishing combined-study from phase-specific missingness are absent. Preserve both alternatives. Core source-card fields and repeated locations are complete; report wording must avoid implying a final applicable percentage has been determined.

**Potential downstream evidence impact:** If confirmed, a design extractor could copy the 10% or 20% assumption for the primary sample-size rationale. No recalculated power or clinical conclusion is available from this audit.

## C012 — Cause attribution of the printed 4.8% mortality

Pending Human Adjudication.

**Review domain:** report_internal_inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT DOC-001 p.8 discussion vs REPORT DOC-001 pp.1,4,5,6 and DOC-003 p.6

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

Reproduced and qualifying by Route B. B1: this is an explicitly in-scope misattributed result; cause-specific versus all-cause mortality changes which outcome receives a printed risk. B2: the report distinguishes 32 TB deaths and 52 total deaths but describes 4.8% of participants as dying of TB; the immediate discussion supplies no alternate numerator or cause definition. B3: six-month TB-specific mortality could be extracted as 4.8% or 32/1080≈3.0%. The outcome-attribution domain is appropriate, rather than a separate claim that the death totals fail.

**Finding IDs:** F-NUM-001, F-XS-012

**Qualifying route:** Route B

**Exact source locations:** [REPORT DOC-001 PDF p.8](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8>), discussion paragraph attributing 4.8% to TB deaths; [REPORT p.5](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), TB 61.5% [32/52] of deaths; [REPORT p.1](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>), randomized denominator; [REPORT p.4](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure 1 death counts; [REPORT p.6](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table 2 death numerator/denominator pairs; [REPORT DOC-003 PDF p.6](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=6>), complete eTable 4 causes.

**Source evidence:** Discussion prints 4.8% dying of TB within six months. Main results and eTable 4 distinguish 32 TB-attributed deaths from 52 total deaths; arm totals are 25 and 27 among 720 and 360 participants. Two initial findings describe one cause-attribution issue and are consolidated without lost locations.

**Calculation:** 100×32/1080=2.962963%; 100×52/1080=4.814815%. Required conservative count-input intervals give TB [2.915317,3.010653]% and all-cause [4.766312,4.863363]%. Printed 4.8±0.05 gives [4.75,4.85]%. The TB gap is 4.75−3.010653=1.739347 percentage points, relative 1.739347/4.8=0.362364>0.05; all-cause overlaps. The cause table's separate one-count percentage pattern belongs to existing C017, not this issue.

**Classification rationale:** Main discussion versus main cause report yields S_W; discussion versus supplementary cause report yields S_C. S_C takes precedence; both sources are REPORT by result content. The inconsistency concerns outcome attribution and fixes report_internal_inconsistency. Denominator/death summaries corroborate the arithmetic. No prospective plan relationship is added. Recheck supports reproduced.

**Classification ambiguity:** The discussion may mean all-cause mortality among trial participants with TB rather than TB-attributed deaths; that interpretation explains 52/1080 but is not its literal cause label.

**Affected result or extracted value:** Six-month TB-attributed mortality risk and its numerator/denominator. No change to the reported Cox all-cause HR 0.4 [0.2,0.9] is inferred.

**Missing inputs and alternatives:** No alternate TB-attribution rule, cause population or denominator yielding 4.8% is supplied. The all-cause-among-people-with-TB interpretation is source-grounded. Core card fields, arithmetic and true PDF pagination are complete.

**Potential downstream evidence impact:** If confirmed, a cause-specific mortality extractor could copy 4.8% instead of 32/1080≈3.0%, or label an all-cause risk as TB-attributed. No actual downstream propagation is established.

## C013 — Any-irritability and any-anxiety direction statement

Pending Human Adjudication.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.5 prevalence pairs vs same-paragraph direction; REPORT DOC-003 p.15 corroborates and supplies severity alternative

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

Reproduced and qualifying by Route A, category 2: the arm-direction statement reverses the adjacent any-symptom percentages for two symptoms, with relative precision gaps above 0.05. Immediate recoverability of the numeric direction does not remove an always-register direction conflict. Preserve the distinct moderate/severe interpretation as a source-grounded alternative.

**Finding IDs:** F-NUM-002, F-XS-013

**Qualifying route:** Route A, category 2

**Exact source locations:** [REPORT DOC-001 PDF p.5](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), complete Adverse Events paragraph and ordered arm percentages; [REPORT DOC-003 PDF p.15](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=15>), eTable 10 none/mild/moderate/severe rows for irritability and anxiety.

**Source evidence:** Main percentages in mHealth/usual-care order are irritability 40.5%/43.4% and anxiety 33.3%/36.8%, then both are described as more common in mHealth. Supplementary None percentages 59.5/56.6 and 66.7/63.2 have complementary any-symptom frequencies matching the main pairs. Moderate+severe frequencies are higher in mHealth: irritability 11.2+4.3=15.5% versus 7.2+1.2=8.4%; anxiety 6.9+2.4=9.3% versus 3.6+0.3=3.9%. One repeated direction pattern contains both symptoms and both checker findings.

**Calculation:** mHealth minus usual care equals −2.9 and −3.5 percentage points; printed half-unit ranges give [−3.00,−2.80] and [−3.60,−3.40], both strictly negative. Relative gaps using the usual-care reference are 2.80/43.4=0.064516 and 3.40/36.8=0.092391>0.05. Dry mouth 62.7%/55.7% agrees with its stated direction and is context only. Neither the severity chi-square tests nor the reported P<.001 statements contradict these different prevalence quantities.

**Classification rationale:** Competing percentages and direction are within a single REPORT paragraph, giving S_W/statistical_results. Supplementary severity/prevalence rows corroborate the printed percentages and supply an alternative quantity; they are not a conflicting report and add no S_C. Recheck supports reproduced. No plan is a comparator.

**Classification ambiguity:** The paragraph might switch from any symptom to moderate/severe burden without stating that switch; severity and prevalence are separate quantities.

**Affected result or extracted value:** Randomized-arm direction for any irritability and any anxiety. No aggregate safety conclusion, causal harm claim, or primary abstinence conclusion is inferred.

**Missing inputs and alternatives:** The intended quantity for more common is not explicitly stated. Moderate/severe counts are available and support the alternative; patient-level adverse-event overlap and any-event aggregation are unavailable and unnecessary for the registered direction issue. Core card fields and all repeated locations are complete.

**Potential downstream evidence impact:** If confirmed, an adverse-event extractor could take the sentence as indicating higher any-irritability/any-anxiety prevalence in mHealth despite the adjacent lower percentages. No pooled safety estimate or actual propagation is established.

## Screening audit in both directions within this shard

The eleven mapped finding IDs each have exactly one INCLUDE/MEETS_THRESHOLD row and the named stable ID. No duplicate decision or lost provenance is present in this assigned subset. The audit reviews both included findings and relevant excluded observations; package-wide decision/exclusion completeness is reserved to the primary audit shard.

| Finding IDs | Stable ID | Existing decision | Independent audit |
|---|---|---|---|
| F-ST1-008 | C008 | INCLUDE | QUESTIONED for the source/context reason above; preserve decision provenance and stable ID. |
| F-XS-002, F-ST1-004 | C009 | INCLUDE for each | CONFIRMED, Route B. |
| F-XS-004, F-ST1-006 | C010 | INCLUDE for each | CONFIRMED, Route A5; eTable 7 sex covariate is not the planned subgroup contrast. |
| F-XS-010, F-ST1-010 | C011 | INCLUDE for each | CONFIRMED, Route B; retained one attrition-input pattern. |
| F-NUM-001, F-XS-012 | C012 | INCLUDE for each | CONFIRMED, Route B; cause attribution affects named mortality extraction. |
| F-NUM-002, F-XS-013 | C013 | INCLUDE for each | CONFIRMED, Route A2; retained one repeated direction pattern. |

Relevant cross-source exclusion row 2 describes the same C008 grouping observation as TERMINOLOGY_OR_WORDING. Statistical pass 2 identifies it as DUPLICATE_OF_INCLUDED because C008 is already registered. This audit agrees it is not a new issue and questions the formal-status-change premise for the existing stable ID; there is no new candidate registration or duplicate finding. Relevant PP/complete-case wording exclusions are supported by 720−53=667 and 360−42=318 and do not change which reported population applies. Planned ancillary non-key secondary omissions remain distinct from the explicitly primary gender analyses in C010. No omitted primary gender result is hidden in the eTable 7 covariate row.

Relevant numeric/statistical precision exclusions were checked against the 0.05 rule, including CO<6 PP 39/318 with printed 11.9%, the sample-size intermediate products and Phase 4 DE copy comparison given above, the target copies 1096 versus 1080 (half-unit gap 15/1080=0.013889) and 2716 versus 2700 (15/2700=0.005556), and dry-mouth/headache/insomnia Pearson diagnostics (relative gaps 0.018980, 0.013857, 0.005903). None crosses 0.05; the additive attrition formula is explicit rather than an omitted retention formula. These precision observations do not contain interval-versus-P/test conflicts requiring Route A1. An unspecified exact test is not replaced by a Pearson convention. No assigned candidate has display-zero P as its basis.

No qualifying screened-out or checker-excluded observation absent from the current ledger was found in this candidate-related subset. No F-QA-101 or later new-finding ID is emitted. The sole opposing-direction inclusion finding is the C008 audit question; it changes neither the stable set nor the original screening decision.

## Repair register and coordinator handoff

| Repair reference | ID | Action and reason | State |
|---|---|---|---|
| QA2-001 | C008 | Replace PENDING_AUDIT with QUESTIONED and carry the complete status-grouping reason into the ledger table and report card; the direct sources establish sensitivity status and grouping but not formal outcome promotion. | Requested through coordinator; no canonical file written here. |
| QA2-002 | C008 | Preserve registered P_R/P_R,S_C,S_W/protocol_report and reproduced_after_transcription_correction fields while expanding Classification ambiguity to state that their formal-status reading is conditional; a corroborating-only plan cannot by itself create P_R. | Requested through coordinator. |
| QA2-003 | C008 | Include literally printed usual-care PP 39/318 and 11.9% in the report evidence; retain all three CO<6 affected rows and the primary-construct grouping alternative. The ledger currently lists 39/318 but omits this printed percentage from its source-evidence paragraph. | Supportable omission documented for coordinator repair. |
| QA2-004 | C009–C013 | Replace PENDING_AUDIT with CONFIRMED and preserve the route-specific reasons, missing inputs, bounded interpretations and evidence states recorded above in the ledger table/report cards. | Requested through coordinator. |

No arithmetic correction, pagination correction or additional pattern consolidation is required for C009–C013. The C008 recheck correction is already present in the current ledger part. All citations use physical PDF pages; component footers are not substituted for PDF pagination. Each classification field above matches the supplied current candidate table, apart from the assigned inclusion-audit update. Report cards are not yet assembled at this shard's handoff, so final ledger/report equality and rendered-link resolution require coordinator validation after merge. Required report-only fields—Reported-versus-comparator, Reasoning procedure, Mechanical evidence recheck and Potential downstream evidence impact—must be supplied in assembly using these bounded facts; their absence from the registration part alone is not a source-evidence gap.

Assigned stable-ID inclusion coverage is complete. Package-wide source rows, relationship inventory closure, routing/execution-manifest freshness, other stable IDs and all checker exclusion totals are outside this disjoint shard and are handled by separate audit parts. Limits are the explicit block-status convention for C008, outcome-specific MAR mapping for C009, unreported sex-specific model outputs for C010, applicable attrition-input hierarchy for C011, alternate cause mapping for C012 and prevalence-versus-severity linkage for C013. These limits constrain interpretation, not the completed review of assigned evidence.
