# Current stable candidate scope

Pending Human Adjudication. Canonical ledger: ../candidate_ledger.md.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C008 | protocol_report | P_R | P_R, S_C, S_W | PLAN DOC-002 p.84 primary definition vs REPORT DOC-001 p.6 and DOC-003 p.13 primary blocks; REPORT DOC-001 p.3 sensitivity statement | reproduced_after_transcription_correction | QUESTIONED | F-ST1-008 |
| C009 | protocol_report | P_R | P_R, P_P | PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP p.91 and REPORT DOC-001 pp.3,4 | reproduced | CONFIRMED | F-XS-002, F-ST1-004 |
| C010 | protocol_report | P_R | P_R | PLAN DOC-002 SAP pp.92,93,99 vs REPORT DOC-001 pp.3,5 and DOC-003 p.12 | reproduced | CONFIRMED | F-XS-004, F-ST1-006 |
| C011 | protocol_report | P_R | P_R, P_P | PLAN DOC-002 protocol pp.48,62 vs PLAN DOC-002 pp.63,64,83 and REPORT DOC-001 p.3; PLAN DOC-002 p.77 amendment context | reproduced | CONFIRMED | F-XS-010, F-ST1-010 |
| C012 | report_internal_inconsistency | S_C | S_C, S_W | REPORT DOC-001 p.8 discussion vs REPORT DOC-001 pp.1,4,5,6 and DOC-003 p.6 | reproduced | CONFIRMED | F-NUM-001, F-XS-012 |
| C013 | statistical_results | S_W | S_W | REPORT DOC-001 p.5 prevalence pairs vs same-paragraph direction; REPORT DOC-003 p.15 corroborates and supplies severity alternative | reproduced | CONFIRMED | F-NUM-002, F-XS-013 |

## C008 — CO<6 sensitivity results appear under a primary-outcome status label

Pending Human Adjudication.

**Candidate statement:** CO<6 sensitivity results appear under a primary-outcome status label.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C, S_W

**Compared document roles:** PLAN DOC-002 p.84 primary definition vs REPORT DOC-001 p.6 and DOC-003 p.13 primary blocks; REPORT DOC-001 p.3 sensitivity statement

**Evidence state:** reproduced_after_transcription_correction

**Inclusion audit:** QUESTIONED

**Inclusion audit reason:** The printed headings and threshold descriptions reproduce, but an actual change of outcome status under Route A, category 5 is not established. Main methods explicitly call CO<6 a post hoc sensitivity performed for the primary outcome; eTable 9 explicitly identifies its entire display as post-hoc sensitivity. Grouping sensitivities of the primary construct under a primary-outcome block can reconcile the cited locations at once. The cited sources do not state that CO<6 became a prespecified primary endpoint. Thus the Route A5 premise depends on interpreting a block heading as formal endpoint hierarchy, and Route B2 is not established by these immediate contexts. This is an inclusion audit question, not a change to the original INCLUDE decision or the stable candidate's status.

**Finding IDs:** F-ST1-008

**Qualifying route:** Route A, category 5

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), primaryCO<10 and posthocCO<6 sensitivity; REPORT.
- [DOC-001 — PDF p. 6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2 Primary outcome block, both CO<6 ITT and PP rows; REPORT.
- [DOC-002 — PDF p. 84](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=84>), lines2653–2669 primary endpoint; PLAN.
- [DOC-003 — PDF p. 13](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9 Primary outcomes CO<6row; REPORT.

**Source evidence:** SAP defines primary verification as CO<10 ppm. Main p.3 explicitly calls CO<6 post hoc sensitivity. Main p.6 nevertheless places both CO<6 rows in Primary outcome: ITT264/720 vs38/360, RR3.7[2.4,5.8], adjusted3.9[2.4,6.9]; PP264/667 vs39/318, RR3.6[2.14,6.87], adjusted3.8[2.3,7.7]. eTable9, titled Post-hoc sensitivity analysis after excluding deaths, also places CO<6 under Primary outcomes:264/695 vs38/333, RR3.6[2.4,5.4], adjusted3.8[2.4,6.2]. The status convention remains an explicit alternative; promotion to a prespecified endpoint is not inferred.

**Calculation:** Compare categorical outcome status for the same biochemical threshold. The primary-status block contains an alternative post hoc threshold alongside the prespecified primary threshold; numeric rounding does not apply.

**Affected result or extracted value:** Outcome-status extraction accompanying both main CO<6 ITT and PP rows and the supplementary excluding-deaths CO<6 row.

**Why context does not resolve it:** Route A category 5 applies to a reproduced planned-outcome status difference; the post hoc table title supplies a possible display convention without removing its printed Primary outcomes block.

**Alternative source-grounded interpretations:** The block may organize analyses of the primary construct, including sensitivities, rather than declare additional primary endpoints. That convention is not explicitly distinguished.

**Exact remaining human question:** Do all three CO<6 rows retain post hoc sensitivity status despite placement in primary blocks, and what outcome-status metadata accompanies their estimates?

**Classification rationale:** Roles follow content: prospective SAP is PLAN, trial tables/methods are REPORT. The registered status comparison generates P_R, S_C and S_W, with P_R taking precedence and protocol_report following that type. Preserve these registered fields while carrying the ambiguity below; the underlying formal-status interpretation is not independently confirmed by this audit. The recheck's p.6 location correction and addition of S_W are supported, so its evidence state remains reproduced_after_transcription_correction.

**Classification ambiguity:** If primary blocks merely group analyses of the primary construct, the plan corroborates the CO<10 endpoint rather than providing a conflicting status statement. P_R and the cross-report status comparison therefore depend on the same unestablished formal-hierarchy reading. No hierarchy promotion, prespecification claim, or implemented threshold change is inferred.

**Checker provenance:** F-ST1-008; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.



## C009 — Primary missing-outcome handling differs between protocol and SAP/report

Pending Human Adjudication.

**Candidate statement:** Primary missing-outcome handling differs between protocol and SAP/report.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP p.91 and REPORT DOC-001 pp.3,4

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: missing-outcome handling for the primary ITT is focus D. B2: the separately headed protocol outcomes paragraph says MAR, while SAP/report assign missing primary outcomes nonabstinent status, without an outcome-specific mapping or replacement hierarchy. Adjacent economic text is a plausible restriction but does not expressly restrict the paragraph. B3: the missingness assumptions attached to primary ITT 300/720 versus 55/360 and RR 3.0 [2.0,4.9] could differ in extraction or interpretation. The observation is a printed specification contrast, not merely an absent imputation detail.

**Finding IDs:** F-XS-002, F-ST1-004

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), missing-primary-outcome paragraph; REPORT.
- [DOC-001 — PDF p. 4](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure1 attrition and analysis totals; REPORT.
- [DOC-002 — PDF p. 28](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=28>), lines759–764 separately headed Statistical analysis; PLAN.
- [DOC-002 — PDF p. 66](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=66>), lines2012–2016 separately headed Statistical analysis; PLAN.
- [DOC-002 — PDF p. 91](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=91>), lines2890–2892 ITT and Russell Standard; PLAN.

**Source evidence:** Protocol says outcomes primarily analyzed in a missing-at-random architecture. SAP regards dropout/incomplete data as continuing smokers. Report treats missing primary outcomes as negative/not abstinent: 53/720 and 42/360, total 95, are missing; primary ITT retains 720/360 and complete-case sensitivity discards missing.

**Calculation:** MAR is a stated missingness architecture; assigning all missing primary outcomes nonabstinent is a deterministic classification. No supplied passage maps them to a combined or separately identified primary analysis. No bias or alternative efficacy result is calculated.

**Affected result or extracted value:** Missing-outcome assumptions attached to ITT 300/720 versus 55/360 and RR 3.0 [2.0,4.9].

**Why context does not resolve it:** The MAR paragraph has its own Statistical analysis heading; adjacency to economic imputation does not restrict it explicitly to costs/QALYs/covariates. Complete-case sensitivity is separately stated.

**Alternative source-grounded interpretations:** MAR may concern another imputation/covariate/economic model, or SAP may supersede the protocol. Neither restriction nor replacement mapping is supplied.

**Exact remaining human question:** Which primary missing-data architecture applied, and how do MAR and missing-as-smoking map to identified analyses or amendments?

**Classification rationale:** Prospective protocol and SAP passages are PLAN; article methods/flow are REPORT. Protocol versus report yields P_R; protocol versus SAP yields P_P. P_R precedes P_P and fixes protocol_report. The flow only corroborates retained denominators; it creates no additional relationship. Evidence state reproduced is supported by the direct-source recheck.

**Classification ambiguity:** MAR and deterministic smoking status can apply to distinct analyses; the source does not map their scope. Economic adjacency and possible SAP supersession are retained alternatives, rather than inferred chronology.

**Checker provenance:** F-XS-002, F-ST1-004; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.



## C010 — Prespecified gender-specific primary analyses are not reported

Pending Human Adjudication.

**Candidate statement:** Prespecified gender-specific primary analyses are not reported.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SAP pp.92,93,99 vs REPORT DOC-001 pp.3,5 and DOC-003 p.12

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route A, category 5: an explicitly planned subgroup analysis of the primary treatment effect is not reported in the complete supplied subgroup results or matched main narrative. This is distinct from omission of ancillary non-key secondary outcomes. The SAP anticipates disclosure of unavailable confidence intervals, so sparse enrollment does not supply an observed removal or nonestimation explanation.

**Finding IDs:** F-XS-004, F-ST1-006

**Qualifying route:** Route A, category 5

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), prespecified subgroup list; REPORT.
- [DOC-001 — PDF p. 5](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), subgroup consistency narrative; REPORT.
- [DOC-002 — PDF p. 92](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2936–2939 subgroup analysis introduction; PLAN.
- [DOC-002 — PDF p. 93](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=93>), lines2940–2952, gender and interval disclosure; PLAN.
- [DOC-002 — PDF p. 99](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=99>), Gender Male/Female table shell; PLAN.
- [DOC-003 — PDF p. 12](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=12>), complete eTable8; REPORT.

**Source evidence:** SAP specifies primary treatment-effect sensitivity models by age, education, occupation, gender male/female, and smoking duration, each with RR and 95% CI and disclosure of missing CIs. eTable 8 and main subgroup narrative contain age, education, occupation, smoking duration, reading SMS, without gender rows/results or nonestimability explanation. Male baseline counts are 698/720 and 345/360.

**Calculation:** Match each planned subgroup to the complete supplied subgroup display and narrative. Gender has no reported counterpart; the blank Male/Female SAP shell corroborates the planned prose and is not a result.

**Affected result or extracted value:** Planned male/female primary RRs/CIs and the robustness scope of the primary abstinence analysis.

**Why context does not resolve it:** Route A category 5 applies to an unreported planned primary analysis. Sparse female observations may explain nonestimation, but the SAP expressly anticipates unavailable-interval disclosure.

**Alternative source-grounded interpretations:** The analysis may have been infeasible, performed but omitted, or removed by amendment. No explanation or result is supplied.

**Exact remaining human question:** Where are the planned male/female primary results or the disclosed reason estimates/CIs were unavailable or removed?

**Classification rationale:** PLAN SAP versus REPORT methods/results gives P_R and protocol_report. Main/supplement omissions agree; there is no S_C discrepancy. The recheck establishes cited plan wording and absence at complete report displays, supporting reproduced. One issue contains both male/female planned rows and both checker findings.

**Classification ambiguity:** Absence is bounded to the complete supplied report package; it does not establish that an analysis was never performed.

**Checker provenance:** F-XS-004, F-ST1-006; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.



## C011 — Current primary-data attrition assumptions differ

Pending Human Adjudication.

**Candidate statement:** Current primary-data attrition assumptions differ.

**Source-order key:** DOC-001 PDF p. 3.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.48,62 vs PLAN DOC-002 pp.63,64,83 and REPORT DOC-001 p.3; PLAN DOC-002 p.77 amendment context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: attrition allowance is focus D and is attached to the reported primary sample-size/power rationale. B2: 10% appears in combined-plan overview and statistics introduction, while both phase-specific calculations and the SAP combined overview use 20%; no explicit differing definition or surviving-input hierarchy reconciles them. B3: a reader could extract 10% or 20% as the attrition assumption supporting the 1080-participant, 90%-power primary design. Amendment context changes sample sizes but does not expressly reconcile these percentages.

**Finding IDs:** F-XS-010, F-ST1-010

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), sample-size20%attrition; REPORT.
- [DOC-002 — PDF p. 48](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=48>), lines1344–1347 primary-data10%; PLAN.
- [DOC-002 — PDF p. 62](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=62>), lines1861–1863 primary-data10%; PLAN.
- [DOC-002 — PDF p. 63](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=63>), lines1894–1898 Phase3 20%calculation; PLAN.
- [DOC-002 — PDF p. 64](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=64>), lines1936–1938 Phase4 contextual20%calculation; PLAN.
- [DOC-002 — PDF p. 77](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>), sample-sizeamendment; PLAN.
- [DOC-002 — PDF p. 83](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=83>), lines2624–2638 SAP20%; PLAN.

**Source evidence:** Current protocol overview/statistics introduction uses 10% missing primary outcome data. Detailed Phase 3 calculation uses 20%, 587+(587×.2)=704, then 1080. SAP and report also use 20%; Phase 4 20% is contextual rather than an additional reported result.

**Calculation:** Printed input copies 10±0.5% and 20±0.5% give gap 9 percentage points and relative gap 9/10=0.90. The expressly stated additive inflation formula is not challenged; no alternative power result is asserted.

**Affected result or extracted value:** Attrition assumption attached to reported 90% power and 1080-participant primary design.

**Why context does not resolve it:** Current passages refer to the same primary-data assumption without distinguishing phase or missingness type; the amendment does not map surviving 10% statements to a superseded input.

**Alternative source-grounded interpretations:** Overview/introduction may retain a previous assumption while detail/SAP/report use 20%. A final hierarchy or dated calculation is absent.

**Exact remaining human question:** Which primary-data attrition assumption governed Phase 3, and how do the surviving 10% and 20% specifications relate?

**Classification rationale:** Protocol versus SAP/detail inputs yields P_P; 10% protocol versus 20% report yields P_R. P_R takes precedence and fixes protocol_report. The amendment is PLAN context; it is not a separate conflicting relationship. The exact-source recheck supports reproduced.

**Classification ambiguity:** Combined-study missingness could have a separate definition, or 10% could be a retained overview input. No final hierarchy is inferred solely from bundle order, labels, or surviving prose. Describe these as supplied-plan passages rather than claim an undisclosed chronological precedence.

**Checker provenance:** F-XS-010, F-ST1-010; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.



## C012 — All-cause mortality percentage is attributed to TB-specific mortality

Pending Human Adjudication.

**Candidate statement:** All-cause mortality percentage is attributed to TB-specific mortality.

**Source-order key:** DOC-001 PDF p. 5.

**Review domain:** report_internal_inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT DOC-001 p.8 discussion vs REPORT DOC-001 pp.1,4,5,6 and DOC-003 p.6

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: this is an explicitly in-scope misattributed result; cause-specific versus all-cause mortality changes which outcome receives a printed risk. B2: the report distinguishes 32 TB deaths and 52 total deaths but describes 4.8% of participants as dying of TB; the immediate discussion supplies no alternate numerator or cause definition. B3: six-month TB-specific mortality could be extracted as 4.8% or 32/1080≈3.0%. The outcome-attribution domain is appropriate, rather than a separate claim that the death totals fail.

**Finding IDs:** F-NUM-001, F-XS-012

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 1](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>), 1080randomized,corroboratingdenominator; REPORT.
- [DOC-001 — PDF p. 4](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure1 death25/27 and1080enrolled; REPORT.
- [DOC-001 — PDF p. 5](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), TBcause32/52; REPORT.
- [DOC-001 — PDF p. 6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2 deaths25/720and27/360; REPORT.
- [DOC-001 — PDF p. 8](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8>), discussion4.8%diedofTB; REPORT.
- [DOC-003 — PDF p. 6](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=6>), eTable4 total52 andTB32; REPORT.

**Source evidence:** Discussion says 4.8% of trial participants died of TB within six months. Main results say TB caused 61.5% [32/52] of deaths. Figure 1/Table 2 show 25+27=52 deaths among 1080 participants. eTable 4 separately identifies 32 TB and 20 other-cause deaths.

**Calculation:** 32/1080×100=2.962963% versus 52/1080×100=4.814815%. TB rounded-input range is 100×[31.5/1080.5,32.5/1079.5]=[2.915317,3.010653]%, disjoint from printed 4.8±.05=[4.75,4.85]%; gap 1.739347/4.8=.362364. The all-cause ratio overlaps 4.8%.

**Affected result or extracted value:** Six-month TB-specific mortality risk, extractable as 4.8% or 32/1080≈3.0%.

**Why context does not resolve it:** The cause label changes which outcome receives the number; the report explicitly distinguishes TB from other causes and supplies no alternate cause population.

**Alternative source-grounded interpretations:** The discussion may intend all-cause mortality among participants with TB; another cause classification or denominator might underlie 4.8%, but none is stated.

**Exact remaining human question:** Does 4.8% mean all-cause mortality among participants with TB or TB-attributed deaths, and which numerator/denominator defines the latter?

**Classification rationale:** Main discussion versus main cause report yields S_W; discussion versus supplementary cause report yields S_C. S_C takes precedence; both sources are REPORT by result content. The inconsistency concerns outcome attribution and fixes report_internal_inconsistency. Denominator/death summaries corroborate the arithmetic. No prospective plan relationship is added. Recheck supports reproduced.

**Classification ambiguity:** The discussion may mean all-cause mortality among trial participants with TB rather than TB-attributed deaths; that interpretation explains 52/1080 but is not its literal cause label.

**Checker provenance:** F-NUM-001, F-XS-012; checkers/numeric_consistency.md; checkers/cross_source_consistency.md; independent decision in screening/inclusion_screen.md.



## C013 — Adverse-event narrative reverses two any-symptom arm directions

Pending Human Adjudication.

**Candidate statement:** Adverse-event narrative reverses two any-symptom arm directions.

**Source-order key:** DOC-001 PDF p. 5.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.5 prevalence pairs vs same-paragraph direction; REPORT DOC-003 p.15 corroborates and supplies severity alternative

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route A, category 2: the arm-direction statement reverses the adjacent any-symptom percentages for two symptoms, with relative precision gaps above 0.05. Immediate recoverability of the numeric direction does not remove an always-register direction conflict. Preserve the distinct moderate/severe interpretation as a source-grounded alternative.

**Finding IDs:** F-NUM-002, F-XS-013

**Qualifying route:** Route A, category 2

**Exact source locations:**

- [DOC-001 — PDF p. 5](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), Adverse Events ordered percentages and summarysentence; REPORT.
- [DOC-003 — PDF p. 15](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=15>), eTable10 irritability/anxiety severity rows; REPORT.

**Source evidence:** Main Adverse Events fixes arm order mHealth versus usual care, prints irritability 40.5% versus 43.4% and anxiety 33.3% versus 36.8%, then says both were more common in mHealth. eTable 10 None percentages 59.5/56.6 and 66.7/63.2 corroborate those prevalences; moderate/severe frequencies are higher in mHealth.

**Calculation:** mHealth-minus-usual-care rounded prevalence differences are [−3.00,−2.80] and [−3.60,−3.40] percentage points. Gap/control-reference ratios are 2.80/43.4=.064516 and 3.40/36.8=.092391. Both directions remain lower mHealth. Dry mouth 62.7 versus 55.7 agrees and is contextual.

**Affected result or extracted value:** Any-irritability and any-anxiety frequency directions by randomized arm.

**Why context does not resolve it:** Route A category 2 applies to a printed direction reversing the values, even when the intended direction may be reconstructed immediately.

**Alternative source-grounded interpretations:** The sentence may refer instead to moderate/severe symptoms; eTable 10 supports that distinct quantity, but the sentence names no switch.

**Exact remaining human question:** Does more common refer to any irritability/anxiety or moderate/severe burden, and which quantity and arm direction should be extracted?

**Classification rationale:** Competing percentages and direction are within a single REPORT paragraph, giving S_W/statistical_results. Supplementary severity/prevalence rows corroborate the printed percentages and supply an alternative quantity; they are not a conflicting report and add no S_C. Recheck supports reproduced. No plan is a comparator.

**Classification ambiguity:** The paragraph might switch from any symptom to moderate/severe burden without stating that switch; severity and prevalence are separate quantities.

**Checker provenance:** F-NUM-002, F-XS-013; checkers/numeric_consistency.md; checkers/cross_source_consistency.md; independent decision in screening/inclusion_screen.md.


