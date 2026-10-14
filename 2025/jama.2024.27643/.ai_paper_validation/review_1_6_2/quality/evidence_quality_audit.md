# Complete quality-control evidence audit

Runtime: /root/quality_control_auditor. Fresh qc162_quality_control_auditor, gpt-6.1-sol/high. Scope: every assigned source unit, quantitative map, numeric/statistical relationship inventory, checker finding and excluded-observation row, screening decision, stable candidate, mechanical recheck, classification and current agent-manifest row. All candidates remain **Pending Human Adjudication**.

**Audit result:** 16 inclusion audits CONFIRMED; 0 QUESTIONED; 0 new audit findings; 0 screening-decision changes. Confirmation means that the supplied observation meets the workflow inclusion threshold; it is not scientific adjudication. Every stable ID is retained. The completion-stage report, environment removal and final validation remain scheduled coordinator actions.

## Scope, coverage and provenance

QUALITY_CONTROL_SCOPE.md, the review contract, report specification, settings, tooling record and routing preflight were read. The audit inspected the closed page ledgers and relationship summaries in the main map and six support parts, the complete N001–N060 inventory, the complete 206-relationship S inventory, both canonical statistical passes and their disjoint parts, all 27 screening decisions, all 87 checker exclusion rows, the complete ledger and all 16 rechecks. Large raw text appendices were treated as source locators rather than as additional source units; the closed unit ledgers and targeted exact-source confirmations govern coverage. No old candidate list, earlier report, web source, count target or comparison with another paper entered the audit or screening. The workflow's fixed shard bounds are context limits, not finding limits.

| Source | Content role | Total | Reusable | Fresh-required | Mapped | Closure |
|---|---|---:|---:|---:|---:|---|
| DOC-001 article | REPORT | 12 | 12 | 0 | 12 | COMPLETE |
| DOC-002 protocol bundle | PLAN | 229 | 224 | 5 | 229 | COMPLETE |
| DOC-003 SAP bundle | PLAN | 130 | 125 | 5 | 130 | COMPLETE |
| DOC-004 results supplement | REPORT | 26 | 26 | 0 | 26 | COMPLETE |
| DOC-005 collaborator roster | REPORT | 6 | 6 | 0 | 6 | COMPLETE |
| DOC-006 data sharing | REPORT | 1 | 1 | 0 | 1 | COMPLETE |
| Total | Content-assigned roles | 404 | 394 | 10 | 404 | COMPLETE |

Every direct-source row satisfies reusable + fresh-required = total and mapped = total. The main 12-page scope and support scopes DOC-002 1–76/77–152/153–229, DOC-003 1–65/66–130, and DOC-004/005/006 26/6/1 pages form a disjoint complete source partition. Conservative fresh assignment of DOC-002 p137 is disclosed and does not double-count the page. All ten fresh-assigned units were inspected; image-only simulation and questionnaire material was visually mapped. There is no scientific source-coverage gap.

The coverage manifest has 35 rows, each with exactly one plain relative artifact path. All 32 completed rows resolve to existing artifacts. The audit row is completed by this artifact; the two report-generation rows are downstream tasks and must be marked COMPLETE after assembly. Candidate registration/recheck rows jointly cover all C001–C016, including the expanded C010. All statistical IDs S001–S112 and S201–S294 have explicit PASS_1_COMPLETE and PASS_2_COMPLETE records; total 112 + 94 = 206. Every numeric bundle N001–N060 records NUMERIC_CHECK_COMPLETE. The coordinator's traceability repair also incorporates the original closed per-ID records into the canonical checker artifacts, so both now explicitly name all 206 IDs without adding scientific conclusions or altering the original closed parts.

At audit time the execution manifest has 20 unique runtime rows: coordinator once and 19 fresh specialists including this auditor. Every recorded model is gpt-6.1-sol. Mandatory pass 1 root/statistical_pass_1 and pass 2 root/statistical_pass_2 are distinct fresh high-effort agents; their plan companions root/statistical_pass_1_plan and root/statistical_pass_2_plan are also distinct fresh high-effort agents. Initial root/inclusion_screener and pass-2 root/inclusion_screener_pass_2 are distinct fresh high-effort agents; both recheck agents are distinct. Ordinary mapper/checker efforts are medium. Routing preflight reports PASS, CURRENT_SESSION, INTERACTIVE_CLI and all ten presets. The fresh medium-effort report-generator row must be appended when spawned.

All six supplied-source SHA-256 checks and all 270 reused-artifact SHA-256 checks passed during this audit. Reused derivatives remain unchanged. Local PDF evidence links reviewed in the canonical ledger, screen, recheck and checkers use supplied filenames and physical #page=N anchors; anchors stay within the source's stable page count. Native text is an aid, with current-run direct-source renders supplying table/figure/glyph authority. The auditor additionally viewed DOC-003 p59's unchanged source-matched render to confirm the dash, wrapped decimal and positive matched-control figure. No fresh extraction, OCR, GPU inference, custom Python or new preprocessing artifact was needed.

## Screening audit in both directions

All 27 checker findings have exactly one canonical screening row, with no missing or orphan finding. There are 16 INCLUDE rows and 11 SCREENED_OUT rows: 10 DUPLICATE_OF_INCLUDED and 1 NOTATION_OR_TYPOGRAPHY. Each included row names a stable candidate, every duplicate names its retained candidate, and the nonduplicate exclusion names no candidate. Ledger Finding IDs match INCLUDE provenance; consolidated duplicate provenance remains in the evidence cards. No stable ID was deleted, merged after registration, ranked or suppressed.

| Finding ID | Audited screen | Candidate | Independent audit reason |
|---|---|---|---|
| F-NUM-001 | INCLUDE / MEETS_THRESHOLD | C007 | C007: matched primary-model rates; 28.57%/33.33% precision gaps, Route B. |
| F-NUM-002 | INCLUDE / MEETS_THRESHOLD | C008 | C008: repeated monthly versus 24-week quantity identity, Route B. |
| F-NUM-003 | INCLUDE / MEETS_THRESHOLD | C009 | C009: exclusion-derived denominator interval gap 6.10%, Route B. |
| F-NUM-004 | INCLUDE / MEETS_THRESHOLD | C013 | C013: plasma-reproducing method leaves >20% serum gaps, Route A4. |
| F-XS-001 | SCREENED_OUT / DUPLICATE_OF_INCLUDED | C007 | Same mortality component pattern; every affected source remains in C007. |
| F-XS-002 | SCREENED_OUT / DUPLICATE_OF_INCLUDED | C008 | Same SVC quantity identity; all dose and sensitivity context retained in C008. |
| F-XS-003 | SCREENED_OUT / DUPLICATE_OF_INCLUDED | C009 | Same regimen-placebo exclusions/denominator; all three table comparisons retained in C009. |
| F-XS-004 | INCLUDE / MEETS_THRESHOLD | C006 | C006: explicit five/six covariate sets, report-only Route B; no unsupported PLAN conflict. |
| F-XS-005 | INCLUDE / MEETS_THRESHOLD | C004 | C004: planned adjusted primary CAFS versus named Wilcoxon, Route A5; version ambiguity retained. |
| F-XS-006 | INCLUDE / MEETS_THRESHOLD | C005 | C005: named planned primary logrank lacks identifiable result, Route A5. |
| F-XS-007 | INCLUDE / MEETS_THRESHOLD | C003 | C003: complete supplied-output search for named primary/key-secondary analyses, Route A5. |
| F-XS-008 | INCLUDE / MEETS_THRESHOLD | C001 | C001: secondary to exploratory status transition, Route A5; hierarchy explains governance only. |
| F-XS-009 | INCLUDE / MEETS_THRESHOLD | C010 | C010: prospective three-group delta-FRS versus claimed prespecified median split, Route A5. |
| F-XS-010 | INCLUDE / MEETS_THRESHOLD | C002 | C002: direct prespecified/post-hoc report conflict and bounded supplied-plan absence; Route B/A5. |
| F-XS-011 | INCLUDE / MEETS_THRESHOLD | C011 | C011: added death/PAV components and endpoint form, Route A5 inside PLAN. |
| F-ST1-001 | INCLUDE / MEETS_THRESHOLD | C012 | C012: all three printed CI/P conflicts retained, Route A1 exempt from precision screening. |
| F-ST1-002 | SCREENED_OUT / DUPLICATE_OF_INCLUDED | C004 | Same CAFS method identity; revision-history and earlier version evidence retained in C004. |
| F-ST1-003 | SCREENED_OUT / DUPLICATE_OF_INCLUDED | C003 | Same named-output omission pattern; union retained in C003 with reported week-24 PAV/death excluded. |
| F-ST1-004 | SCREENED_OUT / DUPLICATE_OF_INCLUDED | C008 | Same monthly/24-week SVC identity; separate model definitions retained in C008. |
| F-ST1-005 | SCREENED_OUT / DUPLICATE_OF_INCLUDED | C002 | Same plasma-status issue; separate unavailable PD plan remains explicit in C002. |
| F-ST1-006 | SCREENED_OUT / DUPLICATE_OF_INCLUDED | C013 | Same serum contrast-scale pattern; alternative log/original-scale evidence retained in C013. |
| F-ST1-007 | SCREENED_OUT / NOTATION_OR_TYPOGRAPHY | — | The source's quoted one-sided code label accompanies an upper bound; explicit same-page two-tailed gate and no contradictory printed test/output. A test-sidedness conflict is not reproduced. |
| F-ST1-008 | SCREENED_OUT / DUPLICATE_OF_INCLUDED | C007 | Same matched primary-model mortality rates; both mean and median copies retained in C007. |
| F-ST2-001 | INCLUDE / MEETS_THRESHOLD | C016 | C016: explicit LOQ/LOD replacement target difference for the same serum condition, Route B. |
| F-ST2-002 | SCREENED_OUT / DUPLICATE_OF_INCLUDED | C010 | Same prospective-subgroup/display identity pattern as C010; both weight and delta-FRS occurrences independently rechecked. |
| F-ST2-201 | INCLUDE / MEETS_THRESHOLD | C014 | C014: HR1.3 simulated DRR direction reversal exceeds 5%, Route A2; later-version relevance bounded. |
| F-ST2-202 | INCLUDE / MEETS_THRESHOLD | C015 | C015: visible dash immediately before wrapped decimal permits reversed numerical sign, Route A2; punctuation alternative retained. |

## Every checker exclusion audited

Ordinal labels identify the original rows in source order, without creating finding IDs. All 57 pass-1/numeric/cross-source exclusions and all 30 pass-2 exclusions are covered separately, including repeated observations. Historical exclusions repaired through existing candidates are explicitly identified rather than silently endorsed. Every ROUNDING_OR_DISPLAY_PRECISION row was checked against half-unit intervals and the 0.05 relative rule; none is used to remove a reproduced interval-versus-P/test conflict. No display-zero P value alone supports a stable candidate.

| Original checker row | Original reason code | Independent audit result |
|---|---|---|
| NUM-EX01 | ROUNDING_OR_DISPLAY_PRECISION | Age copies: .60/58.4=1.0274% after half-unit intervals; ≤5%. |
| NUM-EX02 | ROUNDING_OR_DISPLAY_PRECISION | Fatigue 12/13 count intervals touch; 12/120 versus 10.8% leaves 2.6829%; ≤5%. |
| NUM-EX03 | ROUNDING_OR_DISPLAY_PRECISION | Figure 1 reasons 2+1+1+1 give [3,7], overlapping total 6's [5.5,6.5]. Source death count is 1. |
| NUM-EX04 | ROUNDING_OR_DISPLAY_PRECISION | Completion 137/164 versus 85%: corrected interval [82.978723%,84.097859%]; relative gap 0.4731067%; ≤5%. |
| NUM-EX05 | ROUNDING_OR_DISPLAY_PRECISION | Unknown race 164−160 permits [3,5], overlapping printed 3's [2.5,3.5]. |
| NUM-EX06 | ROUNDING_OR_DISPLAY_PRECISION | Discussion 13 versus 5+9: [12.5,13.5] overlaps [13,15]. |
| NUM-EX07 | ROUNDING_OR_DISPLAY_PRECISION | Moderate TEAE 44 versus 22+24: gap .5/44=1.1364%; ≤5%. |
| NUM-EX08 | ROUNDING_OR_DISPLAY_PRECISION | Severity total 884 versus 889: gap 3/889=.3375%; ≤5%. |
| NUM-EX09 | ROUNDING_OR_DISPLAY_PRECISION | Functional bound gaps .3401%, .1121%, .7806%, 1.1655%; all ≤5%. Plasma −.4/−.5 intervals touch. Independent CI/P pattern remains C012. |
| NUM-EX10 | PERIPHERAL_COMPARISON | Observed-visit and mortality-excluded contributors are differently defined; no changed FAS size. |
| NUM-EX11 | PERIPHERAL_COMPARISON | Exploratory serum numerical crosscopies are peripheral; within-display reproducing-method issue remains C013. |
| NUM-EX12 | MODEL_VERSUS_CRUDE | Adjusted profile-likelihood Cox HR is not a stated crude risk ratio; no reproducible same-estimand conflict. |
| NUM-EX13 | PERIPHERAL_COMPARISON | Particle concentrations are historical/preclinical rationale, with no supplied primary-design/decision reliance. |
| NUM-EX14 | CONDITIONAL_OR_UNREPORTED | Ventilation percentages allow outcome-specific risk sets after prevalent-event exclusions; no printed shared denominator to contradict. |
| XS-EX01 | NOT_REPRODUCED | Mapper's death 3 was a transcription; exact Figure 1 shows 1. No supplied-source finding. |
| XS-EX02 | TERMINOLOGY_OR_WORDING | Paired El Escorial labels give an immediate complementary interpretation; wording alone changes no printed value. |
| XS-EX03 | CONDITIONAL_OR_UNREPORTED | Historical exclusion repaired through F-ST2-002 and C010: claimed prespecified <56 kg label differs from two prospective low-weight groups. Empty <43 kg is an alternative. |
| XS-EX04 | ROUNDING_OR_DISPLAY_PRECISION | Age copy interval gap 1.0274%; ≤5%. |
| XS-EX05 | ROUNDING_OR_DISPLAY_PRECISION | Fatigue count intervals touch; percentage gap 2.6829%; ≤5%. |
| XS-EX06 | ROUNDING_OR_DISPLAY_PRECISION | 13 versus 5+9 sum/copy intervals overlap. |
| XS-EX07 | ROUNDING_OR_DISPLAY_PRECISION | Four functional credible-bound gaps remain ≤5%; not an interval/P pair. |
| XS-EX08 | PERIPHERAL_COMPARISON | Peripheral exploratory serum copies; C013 independently retains the within-display method comparison. |
| XS-EX09 | ROUNDING_OR_DISPLAY_PRECISION | Sensitivity P=.05/.051 intervals overlap; reversal of contrast order reverses both estimate and bounds, with both intervals containing zero. |
| XS-EX10 | PERIPHERAL_COMPARISON | Peripheral plasma crosscopies do not suppress the within-row CI/P conflicts in C012. |
| XS-EX11 | PERIPHERAL_COMPARISON | Baseline copies and per-visit contributors are peripheral; mortality-related exclusions distinguish contributor definitions. |
| XS-EX12 | ROUNDING_OR_DISPLAY_PRECISION | Power 80/77 integer half-unit gap 2/80=2.5%; ≤5%. |
| XS-EX13 | CONTEXT_RESOLVES | Later Master third-drug/28-week defaults have different applicability and RSA overrides; no matched governing mismatch. |
| XS-EX14 | PERIPHERAL_COMPARISON | OLE schedule/amendment differences concern extensions, with no demonstrated primary/key-secondary decision change. |
| XS-EX15 | TERMINOLOGY_OR_WORDING | 40 randomized is immediately defined as 30 drug + 10 placebo; no changed allocation. |
| XS-EX16 | MODEL_VERSUS_CRUDE | Adjusted Cox results are explicitly model-based; crude risks are different quantities. |
| XS-EX17 | PERIPHERAL_COMPARISON | Simulated PLAN and observed REPORT outputs are different quantities; internal supplied-design direction is separately C014. |
| XS-EX18 | CONDITIONAL_OR_UNREPORTED | Absent earlier Master version alone does not create a contrary printed result; governing-version limits retained. |
| XS-EX19 | NOTATION_OR_TYPOGRAPHY | Random intercept/slope and covariance meanings are explicit; index letters alone do not establish a changed result. |
| ST1R-EX01 | ROUNDING_OR_DISPLAY_PRECISION | Functional credible-bound copy gaps remain ≤5%; no interval/P pair. |
| ST1R-EX02 | ROUNDING_OR_DISPLAY_PRECISION | Plasma −.5/−.4 upper-bound intervals meet at −.45. |
| ST1R-EX03 | ROUNDING_OR_DISPLAY_PRECISION | Serum sensitivity P=.05/.051 ranges overlap; both matched intervals contain zero after contrast reversal. |
| ST1R-EX04 | MODEL_VERSUS_CRUDE | Explicitly adjusted Cox/profile-likelihood estimates are not crude risk ratios. |
| ST1R-EX05 | CONDITIONAL_OR_UNREPORTED | Serious TEAE P=.31 has no specified independent-arm test/output identity; a nested 2×4 reconstruction would invent structure. |
| ST1R-EX06 | NOTATION_OR_TYPOGRAPHY | Treat/trtrnd code-template names identify the intended treatment contrast; no printed numerical change. C004 separately retains primary CAFS model identity. |
| ST1R-EX07 | NOTATION_OR_TYPOGRAPHY | Post template identifier is absent from the displayed model, but coefficients and prose specify the week-24 contrast; no printed output contradiction. |
| ST1R-EX08 | CONTEXT_RESOLVES | Explicit revision/equation/code include treatment main effect; residual shared-baseline words alone do not replace a result. |
| ST1R-EX09 | NOTATION_OR_TYPOGRAPHY | Monthly delta-FRS formula resolves unit wording; independent three-group/median issue remains C010. |
| ST1R-EX10 | TERMINOLOGY_OR_WORDING | 40 is immediately decomposed into 30 drug + 10 placebo. |
| ST1R-EX11 | CONTEXT_RESOLVES | Historical exclusion does not suppress the independently screened/rechecked five/six covariate conflict already retained as C006. |
| ST1R-EX12 | NOT_REPRODUCED | DRR credible interval and CAFS P=.0026 belong to separate explicitly named estimands/analyses. |
| ST1R-EX13 | CONTEXT_RESOLVES | Serum regimen-only rerun is expressly post hoc with same-plate rationale; exploratory status is unchanged. Separate replacement-target issue is C016. |
| ST1P-EX01 | PERIPHERAL_COMPARISON | Later Master treatment-main code/prose difference has no established reliance by this regimen's reported analysis; governing regimen equation/code includes treatment main effect. |
| ST1P-EX02 | CONTEXT_RESOLVES | Slope equation, contrast and month units immediately identify the estimand despite residual 24-week prose. |
| ST1P-EX03 | TERMINOLOGY_OR_WORDING | Explicit hazard equation and DRR definition identify rate; time wording alone is not a printed numerical reversal. |
| ST1P-EX04 | CONTEXT_RESOLVES | Six/eight refers to a scenario-parameter enumeration, not participant counts or a changed decision rule; all eight parameters are named. |
| ST1P-EX05 | ROUNDING_OR_DISPLAY_PRECISION | Early-futility .01 permits [.005,.015], overlapping values below .01. |
| ST1P-EX06 | ROUNDING_OR_DISPLAY_PRECISION | Posterior .979 permits [.9785,.9795], including >.979; no independently contrary same-result interval/test is printed. |
| ST1P-EX07 | NOT_REPRODUCED | Shared-parameter DRR and fixed-sharing CAFS are explicitly separate outcomes/analyses, not a same-result CI/P pair. |
| ST1P-EX08 | CONTEXT_RESOLVES | Historical context exclusion repaired by F-ST2-201/C014: HR1.3 direction reversal has 11.1111% precision gap, Route A2. |
| ST1P-EX09 | CONTEXT_RESOLVES | Protocol explicitly gives Appendix I precedence; exact contributor rule is disclosed and identifies mortality exclusions. |
| ST1P-EX10 | CONTEXT_RESOLVES | Master permits RSA override; both regimen versions specify 24 weeks. |
| ST1P-EX11 | CONDITIONAL_OR_UNREPORTED | Log-weeks offset can be rescaled to participant-years; no printed rate establishes omitted conversion. |
| ST2R-EX01 | ROUNDING_OR_DISPLAY_PRECISION | Age gap 1.0274%; ≤5%. |
| ST2R-EX02 | ROUNDING_OR_DISPLAY_PRECISION | Fatigue count intervals touch; percentage gap 2.6829%; ≤5%. |
| ST2R-EX03 | ROUNDING_OR_DISPLAY_PRECISION | Reasons/race/event-count intervals overlap; moderate TEAE gap 1.1364%, severity gap .3375%; all ≤5%. |
| ST2R-EX04 | ROUNDING_OR_DISPLAY_PRECISION | Completion interval correction gives .4731067% relative gap; ≤5%, with no changed screening conclusion. |
| ST2R-EX05 | ROUNDING_OR_DISPLAY_PRECISION | Functional credible-bound gaps remain ≤5%; no same-result interval/P conflict. |
| ST2R-EX06 | ROUNDING_OR_DISPLAY_PRECISION | Plasma −.4/−.5 ranges touch. |
| ST2R-EX07 | ROUNDING_OR_DISPLAY_PRECISION | Sensitivity estimates and intervals reverse consistently; .05/.051 precision ranges overlap and both intervals contain zero. |
| ST2R-EX08 | MODEL_VERSUS_CRUDE | Adjusted profile-likelihood HR is not a crude risk ratio. |
| ST2R-EX09 | CONDITIONAL_OR_UNREPORTED | Prevalent-event exclusions yield outcome-specific risk sets; unknown denominators are not replaced by randomized totals. |
| ST2R-EX10 | CONDITIONAL_OR_UNREPORTED | Serious TEAE P=.31 lacks a stated test-to-output identity; a contrary proportion test is not source-established. |
| ST2R-EX11 | PERIPHERAL_COMPARISON | Exploratory crosscopies are peripheral; independent within-row C012/C013 are retained. |
| ST2R-EX12 | PERIPHERAL_COMPARISON | Visit contributors have explicit mortality exclusions; no changed FAS size. |
| ST2R-EX13 | NOTATION_OR_TYPOGRAPHY | Template Treat/trtrnd/post identifiers identify their contrasts through prose/coefficients; no changed number. |
| ST2R-EX14 | CONTEXT_RESOLVES | Amendment, equation and code explicitly retain treatment main effect; residual shared-baseline words do not establish contrary output. |
| ST2R-EX15 | NOTATION_OR_TYPOGRAPHY | Monthly delta-FRS formula resolves unit text; actual partition difference remains C010. |
| ST2R-EX16 | TERMINOLOGY_OR_WORDING | Immediate 30+10 parenthetical resolves 40 randomized. |
| ST2R-EX17 | TERMINOLOGY_OR_WORDING | Paired El Escorial complement wording is immediately identifiable; no changed result attribution established. |
| ST2R-EX18 | CONTEXT_RESOLVES | Post-hoc same-plate serum rerun is disclosed and leaves exploratory status unchanged; C016 concerns a separate explicit substitution rule. |
| ST2R-EX19 | ROUNDING_OR_DISPLAY_PRECISION | Approximate power gap 2/80=2.5%; ≤5%. |
| ST2R-EX20 | CONTEXT_RESOLVES | Later Master default applicability/overrides distinguish versions; no matched regimen design contradiction. |
| ST2P-EX01 | PERIPHERAL_COMPARISON | Later-default treatment-main omission has no established regimen-C reliance; governing regimen model contains it. |
| ST2P-EX02 | CONTEXT_RESOLVES | Explicit slope/month equation and contrast resolve residual 24-week estimand wording. |
| ST2P-EX03 | TERMINOLOGY_OR_WORDING | Hazard equation and DRR definition resolve time/rate terminology without a changed printed number. |
| ST2P-EX04 | CONTEXT_RESOLVES | Six/eight scenario parameters are explicitly enumerated; no participant denominator or decision rule changes. |
| ST2P-EX05 | ROUNDING_OR_DISPLAY_PRECISION | .01 interval [.005,.015] overlaps early-futility probabilities below 1%. |
| ST2P-EX06 | ROUNDING_OR_DISPLAY_PRECISION | .979 interval [.9785,.9795] admits values >.979; no independent same-result interval/test conflict. |
| ST2P-EX07 | NOT_REPRODUCED | DRR credible interval and CAFS P are explicitly different named analyses. |
| ST2P-EX08 | CONTEXT_RESOLVES | Appendix I contributor definition has explicit prospective precedence. |
| ST2P-EX09 | CONTEXT_RESOLVES | RSA override distinguishes 24-week regimen from 28-week default. |
| ST2P-EX10 | CONDITIONAL_OR_UNREPORTED | Unit conversion can reconcile weeks and participant-years; no printed rate establishes omitted conversion. |

## Stable-candidate inclusion and classification audit

The ledger and source-confirmed recheck provide the substantive evidence needed for each final card. All 16 review domains, primary/all relationships, content-assigned roles and evidence states agree. The report is assembled after this audit; its exact classification-field equality and complete required-label presence are mandatory coordinator release checks, not claims of an already inspected report.

## C001 — Muscle-strength outcome status

**Inclusion audit:** CONFIRMED

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN regimen protocols vs PLAN regimen SAPs and REPORT article/results supplement

**Evidence state:** reproduced

**Qualifying route:** Route A, category 5

**Concrete inclusion reason:** Protocol secondary HHD/grip status versus exploratory SAP/report status is reproduced at protocol pp112/184, SAP pp76–78/109–112 and article p3/results pp5–6. Outcome-status changes always register. SAP precedence is a governance alternative, not a removal of the printed transition. The named muscle-strength endpoint status can be extracted differently; no absent numerical grip effect is invented.

**Classification and precedence audit:** Both PLAN-to-REPORT and PLAN-to-PLAN comparisons occur. P_R takes precedence over P_P; protocol_report is appropriate.

**Evidence-card completeness and bounded impact:** Dated amendment and exact grip-output mapping remain missing. Preserve secondary/exploratory status wording and the authority-table alternative.

**Reproducible evidence locator:** [protocol p112](../../../joi240158supp1_prod_1742927563.7611.pdf#page=112). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C002 — Plasma NfL prespecification

**Inclusion audit:** CONFIRMED

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C

**Compared document roles:** PLAN regimen SAP versus REPORT article and REPORT results supplement

**Evidence state:** reproduced

**Qualifying route:** Route A, category 5

**Concrete inclusion reason:** The article calls plasma NfL prespecified, while results pp6/11 expressly call it post hoc for this manuscript. The supplied regimen plan specifies serum/CSF NfL and delegates other PD analyses; it contains no named plasma contrast. Route A5 supports bounded supplied-plan absence; the direct REPORT status conflict independently meets Route B for pooled −9.5%, P=.04.

**Classification and precedence audit:** P_R takes precedence over S_C. Both conflicting report statements and the supplied-plan scope support protocol_report; the absent external PD plan must not be described as proof of a change outside the package.

**Evidence-card completeness and bounded impact:** Keep the unavailable external plan, prospective sample-collection context and UCH-L1/multiplex assay explanation. Impact is limited to analysis-status/specification extraction.

**Reproducible evidence locator:** [article p3](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=3). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C003 — Unreported named planned primary/key-secondary analyses

**Inclusion audit:** CONFIRMED

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN regimen SAP versus complete REPORT article/results supplement

**Evidence state:** reproduced

**Qualifying route:** Route A, category 5

**Concrete inclusion reason:** Named planned primary/key-secondary sensitivity, supportive, population, missingness, endpoint/follow-up and subgroup outputs lack identifiable results in the complete supplied REPORT set. The item-wise recheck preserves every retained family and distinguishes reported counterparts. This always-register omission pattern concerns supplied reporting, not whether analyses were performed.

**Classification and precedence audit:** Sole P_R gives protocol_report. Repeated omissions are one stable pattern. Primary CAFS, primary logrank and changed subgroup partitions remain separately defined rules.

**Evidence-card completeness and bounded impact:** The week-24 PAV/death output IS reported and is explicitly excluded from this omission claim. Use the complete recheck item table and individually anchored source pages; no numerical consequence or absence of conduct is established.

**Reproducible evidence locator:** [SAP p119](../../../joi240158supp2_prod_1742927563.7711.pdf#page=119). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C004 — Adjusted planned CAFS versus reported Wilcoxon

**Inclusion audit:** CONFIRMED

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN regimen SAP versus REPORT article/results supplement

**Evidence state:** reproduced

**Qualifying route:** Route A, category 5

**Concrete inclusion reason:** Latest supplied regimen SAP pp118–119 specifies primary covariate-adjusted CAFS rank regression, while article pp3–4 names Wilcoxon and P=.51. A different baseline-NfL sensitivity P=.88 is not the specified adjusted primary output. A named primary key-secondary analysis difference always registers.

**Classification and precedence audit:** Sole P_R gives protocol_report. Earlier Wilcoxon SAP and July 22, 2022 adjustment revision are version alternatives rather than additional conflict relationships.

**Evidence-card completeness and bounded impact:** Keep earlier SAP p84 and revision p97, their dates and governing-version uncertainty. Do not infer a replacement adjusted P or a conducted analysis change.

**Reproducible evidence locator:** [SAP p118](../../../joi240158supp2_prod_1742927563.7711.pdf#page=118). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C005 — Planned survival logrank result

**Inclusion audit:** CONFIRMED

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN regimen SAP versus REPORT article/results supplement

**Evidence state:** reproduced

**Qualifying route:** Route A, category 5

**Concrete inclusion reason:** Both regimen versions expressly plan primary key-secondary survival logrank; supplied article pp3–4/7 and results p10 provide adjusted Cox and KM curves without an identifiable logrank result. KM plotting and adjusted Cox P=.22 do not identify the planned test. The nominal-secondary reporting rule remains relevant despite failed primary hierarchy.

**Classification and precedence audit:** Sole P_R gives protocol_report; the named primary test is distinct from supportive-output omission C003.

**Evidence-card completeness and bounded impact:** Only supplied-output absence is established. Event times, logrank statistic/P, unprovided output and mapping/amendment remain absent; no hypothetical logrank result is calculated.

**Reproducible evidence locator:** [SAP p121](../../../joi240158supp2_prod_1742927563.7711.pdf#page=121). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C006 — Survival covariate-set descriptions

**Inclusion audit:** CONFIRMED

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT article methods/Table 2 versus REPORT results supplement

**Evidence state:** reproduced

**Qualifying route:** Route B

**Concrete inclusion reason:** Source-confirmed methods lists in article p3 and results p10 name five Cox covariates; article Table 2 p7 adds sex. No distinct fitted analysis is identified. B1 statistical model specification, B2 unresolved complete-set descriptions, and B3 which adjustment produced six reported survival HRs all hold.

**Classification and precedence audit:** S_C outranks S_W; statistical_results fits model logic. Governing older Master SAP is not supplied, so SAP context supplies no additional P_R relationship.

**Evidence-card completeness and bounded impact:** The result-specific footnote or abbreviated method prose may identify the intended fit; keep that alternative. Do not infer that any actual fit excluded sex.

**Reproducible evidence locator:** [article Table 2 p7](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C007 — Mortality component estimates

**Inclusion audit:** CONFIRMED

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT article versus REPORT results supplement

**Evidence state:** reproduced

**Qualifying route:** Route B

**Concrete inclusion reason:** Article p4's matched primary-model monthly mortality rates .007/.006 differ from results p15's .010/.009 in both mean and median columns. Half-unit gaps .002/.007=.285714 and .002/.006=.333333 reproduce. B1 primary statistical estimates, B2 unspecified fit/summary identity, B3 which monthly component pair to extract all hold.

**Classification and precedence audit:** Separate REPORT PDFs give S_C/statistical_results. No PLAN comparator is needed; crude event ratios are not substituted.

**Evidence-card completeness and bounded impact:** Conditional/marginal summaries or separate fits are bounded alternatives without printed identifiers. Downstream impact is limited to copying one primary component pair.

**Reproducible evidence locator:** [results p15](../../../joi240158supp3_prod_1742927563.7911.pdf#page=15). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C008 — SVC change versus monthly rate

**Inclusion audit:** CONFIRMED

**Review domain:** report_internal_inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT article versus REPORT results supplement; REPORT article internal comparison

**Evidence state:** reproduced

**Qualifying route:** Route B

**Concrete inclusion reason:** Article p4 repeatedly assigns monthly PPN labels to −9.32/−8.53 and dose-specific values that results p16 identifies as 24-week changes; the same article supplies separate monthly sensitivity magnitudes. B1 key-secondary quantity, B2 two explicitly available analysis types, B3 time-scale/quantity extraction all hold. Equal numeric copies have zero precision gap; this is a quantity identity comparison.

**Classification and precedence audit:** S_C outranks S_W; report_internal_inconsistency is appropriate because outcome horizon/model attribution changes the extractable quantity. PLAN definitions only corroborate distinct models.

**Evidence-card completeness and bounded impact:** 168×12/365.25=5.519507 months and the diagnostic conversion interval reproduce; they are not fitted replacement estimates. Preserve the possibility that the table is intended and monthly wording was carried over.

**Reproducible evidence locator:** [results p16](../../../joi240158supp3_prod_1742927563.7911.pdf#page=16). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C009 — Survival regimen-placebo exclusions and denominator

**Inclusion audit:** CONFIRMED

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT article survival paragraph versus REPORT article Table 2

**Evidence state:** reproduced

**Qualifying route:** Route B

**Concrete inclusion reason:** Article p4 explicitly describes four of 41 regimen-placebo participants as excluded, while Table 2 p7 retains 41 in all three regimen-placebo rows. [40.5,41.5]−[3.5,4.5]=[36,38], versus [40.5,41.5], gap 2.5/41=.060976. B1 analysis denominator, B2 unreconciled exclusion predicate, B3 key-secondary risk population all hold.

**Classification and precedence audit:** Both conflicting locations are one REPORT, S_W/statistical_results. The shared-placebo 164−2=162 comparison reconciles and is not a separate issue.

**Evidence-card completeness and bounded impact:** Four may refer to events; the table and later narrative support this alternative. The diagnostic 4/37 versus 4/41 does not establish actual participant identities or recompute an adjusted HR.

**Reproducible evidence locator:** [article p4](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C010 — Prespecified subgroup partitions

**Inclusion audit:** CONFIRMED

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN regimen SAP versus REPORT article/results supplement

**Evidence state:** reproduced

**Qualifying route:** Route A, category 5

**Concrete inclusion reason:** Both SAP versions specify three fixed delta-FRS strata, versus a report-claimed prespecified two-group median split. They also specify <43/43–<56 kg separately, versus claimed prespecified <56 kg. The fresh pass-2 recheck preserves both occurrences. This repeated prospective subgroup-to-display identity difference always registers; participant membership is not invented.

**Classification and precedence audit:** Sole P_R gives protocol_report. Agreeing PLAN versions do not create P_P, and corroborating article/subgroup displays do not create S_C. Consolidation occurred by pattern without deleting a stable ID.

**Evidence-card completeness and bounded impact:** Keep the empty <43 kg alternative, potential pooling/amendment, and absence of ≥150 kg alone as nonqualifying. Retain both .06/−.01 delta-FRS results and −.25 [−1.11,.60] low-weight result as locators, without claiming their numeric estimates conflict.

**Reproducible evidence locator:** [results p19](../../../joi240158supp3_prod_1742927563.7911.pdf#page=19). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C011 — Six-point functional-decline composite inside PLAN

**Inclusion audit:** CONFIRMED

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN regimen protocols versus PLAN regimen SAPs

**Evidence state:** reproduced

**Qualifying route:** Route A, category 5

**Concrete inclusion reason:** Protocol pp112/184 uses week-24 proportions with ≥6-point decline; SAP pp78/111 uses first-event decline or death/death-equivalent. Added death/PAV components reproduce a changed prospective composite, independent of numerical precision.

**Classification and precedence audit:** All conflicting material is PLAN, so sole P_P gives plan_material. Article p3's brief time-to-event reference only corroborates relevance and does not define a separate contrary REPORT composite.

**Evidence-card completeness and bounded impact:** Keep SAP-precedence/amendment alternatives and avoid claiming a separate unprovided numerical six-point result.

**Reproducible evidence locator:** [SAP p111](../../../joi240158supp2_prod_1742927563.7711.pdf#page=111). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C012 — NfL interval versus P display pattern

**Inclusion audit:** CONFIRMED

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 3B interval versus P rows

**Evidence state:** reproduced

**Qualifying route:** Route A, category 1

**Concrete inclusion reason:** All three eTable 3B p17 rows reproduce: pooled plasma [−18,0]/P=.04, 60-mg plasma [−20,0]/P=.04, and 60-mg serum [−45.1,−.7]/P=.05. The first two printed intervals contain zero despite P<.05; the last excludes zero although the stated rule is strict P<.05. Route A1 is expressly exempt from the precision screen.

**Classification and precedence audit:** All conflicting CI/P pairs are one REPORT table, S_W/statistical_results. More precise article bounds corroborate a rounding alternative rather than an independent S_C comparison.

**Evidence-card completeness and bounded impact:** Unrounded bounds/P, different inferential constructions and test/interval identities remain alternatives. Do not apply a Wald approximation or let possible hidden precision remove these printed conflicts.

**Reproducible evidence locator:** [results p17](../../../joi240158supp3_prod_1742927563.7911.pdf#page=17). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C013 — Serum NfL contrast scale

**Inclusion audit:** CONFIRMED

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 3B modeled changes versus contrasts

**Evidence state:** reproduced

**Qualifying route:** Route A, category 4

**Concrete inclusion reason:** The table's stated log/exponentiated-scale method q(a,b)=100[(1+a/100)/(1+b/100)−1] reproduces all three plasma contrasts. Serum input half-unit intervals give [−20.890816,−20.749507], [−20.102483,−19.960552], [−21.600315,−21.459566]; gaps relative to printed serum contrasts are .206787/.209707/.209843. Category 4 applies to a method reproducing the other rows, without assuming crude participant ratios.

**Classification and precedence audit:** Within one REPORT display, sole S_W/statistical_results. Exploratory article crosscopies only support an alternative scale interpretation and do not add S_C.

**Evidence-card completeness and bounded impact:** Keep the possible log/original-scale distinction, arithmetic-difference alternative, missing contrast covariance and interval scale. The exponential diagnostic is 30.734714% and −23.202646%; no production mechanism or replacement correction is asserted.

**Reproducible evidence locator:** [results p17](../../../joi240158supp3_prod_1742927563.7911.pdf#page=17). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C014 — Estimated DRR direction in planned operating characteristics

**Inclusion audit:** CONFIRMED

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN Master SAP Appendix I prose versus PLAN same-page Table 6.2.1

**Evidence state:** reproduced

**Qualifying route:** Route A, category 2

**Concrete inclusion reason:** Supplied Master SAP p50 says estimated DRR decreases as mortality rises, but the matched HR1.3 mean sequence .72/.75/.81 increases. [.715,.725] versus [.805,.815] yields positive change [.080,.100] and relative gap .080/.72=.111111; .75→.81 also exceeds 5%. A reversed named numerical direction beyond precision always registers.

**Classification and precedence audit:** Same prospective PLAN explanation/table gives P_P/plan_material. Protocol Appendix I references corroborate primary-design relevance and add no P_R. General design relevance does not prove this later appendix governed regimen C.

**Evidence-card completeness and bounded impact:** Keep the benefit 1−DRR alternative, later Master applicability limitation and absent earlier governing version. HR1.0 .71→.75 gap 4.225% does not independently qualify. No observed trial estimate or conducted decision is implicated.

**Reproducible evidence locator:** [SAP p50](../../../joi240158supp2_prod_1742927563.7711.pdf#page=50). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C015 — Signed CAFS P value in illustrative PLAN prose

**Inclusion audit:** CONFIRMED

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN Master SAP illustrative prose versus PLAN same-page Figure 6.3.2

**Evidence state:** reproduced

**Qualifying route:** Route A, category 2

**Concrete inclusion reason:** Independent visual inspection confirms a short dash after 'CAFS p-value of' and immediately before the wrapped .3675, while the matched-control figure prints +.3675 with matching estimate 1.0/posterior .51. Literal −.3675 versus +.3675 intervals leave gap .73490/.3675=1.999728. A potentially numerical reversed sign is preserved under the printed-number doubt rule, with punctuation ambiguity explicit.

**Classification and precedence audit:** Both prospective illustrative PLAN locations give P_P/plan_material; no REPORT result conflicts. The primary-design/key-secondary illustration is distinct from actual CNM-Au8 outcome inference.

**Evidence-card completeness and bounded impact:** The dash may be punctuation and the adjacent positive figure supports that intended reading. Do not assert an actual negative P computation or clinical significance effect. Keep later/earlier governing-version ambiguity and the exact visible glyph context.

**Reproducible evidence locator:** [SAP p59](../../../joi240158supp2_prod_1742927563.7711.pdf#page=59). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## C016 — Serum NfL below-quantitation substitution rule

**Inclusion audit:** CONFIRMED

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN regimen SAP biomarker imputation versus REPORT results supplement serum methods

**Evidence state:** reproduced

**Qualifying route:** Route B

**Concrete inclusion reason:** Regimen SAP p112 explicitly replaces below-LOQ serum values with LOQ; results p11 explicitly uses assay LOD for the same condition. B1 planned/reported statistical preprocessing, B2 neither instruction equates limits or states a target amendment, B3 the imputation specification underlying the named log/MMRM serum analysis all hold. This is an explicit categorical instruction conflict, not a conjecture about an omitted detail.

**Classification and precedence audit:** Sole P_R gives protocol_report. Article p8 and results p17 locate the serum results but do not add a conflicting S_C relationship. Distinct from plasma prespecification and serum contrast scale.

**Evidence-card completeness and bounded impact:** Numerical LOQ/LOD, equality of limits, substituted sample counts and an operative post-hoc rerun specification are unavailable. Do not claim any participant was substituted or that the −23.2%, P=.03 result would change; impact is limited to reproducibility/specification extraction.

**Reproducible evidence locator:** [results p11](../../../joi240158supp3_prod_1742927563.7911.pdf#page=11). Every additional affected page remains individually identified in the canonical source recheck and must appear in the final evidence card.

## Repairs and release requirements

| Record | Supportable repair or required completion | Reason and status |
|---|---|---|
| Current-run Figure 1 mapping | Regimen-placebo death transcription was corrected from 3 to source 1 before registration; original reused assets were preserved. | Exact source resolves the derivative-only observation; no stable candidate arose from it. |
| C003 omission scope | Week-24 PAV/death is expressly retained as reported; only death-alone and later-follow-up outputs remain in that part of the missing-output pattern. | Prevents overstatement; repaired in ledger/recheck and required in the report. |
| C006 classification | REPORT five/six-covariate discrepancy retained; supplied PLAN context does not create an unsupported P_R comparison. | Earlier governing Master covariate specification is absent; source-confirmed S_C with S_W is retained. |
| C010 repeated pattern | Weight occurrence added to the existing delta-FRS partition candidate with every affected source and empty-category alternative. | Same prospective-subgroup/display identity rule; all locations retained without deleting any stable ID. |
| C013 exponential diagnostic | 100(exp(.268)−1)=30.734714%; 100(exp(−.264)−1)=−23.202646%. | Supporting arithmetic reproduced; no supplied printed value is altered. |
| Completion exclusions NUM-EX04/ST2R-EX04 | Correct approximate repeated 1.40% to 0.4731067% under the mandated full half-unit rule: [82.978723%,84.097859%] versus [84.5%,85.5%], gap .402141 percentage points divided by 85. | Repaired audit arithmetic; still ≤5%, with unchanged exclusion. Original checker artifacts/parts remain preserved. |
| Ledger/recheck scope introductions | Coordinator removed stale appended-entry-awaiting-recheck wording and qualified 13 as the initial recheck scope. | All 16 are now independently source-rechecked; repaired during audit. |
| Both canonical statistical checker records | Coordinator incorporated original closed per-ID inventories into canonical checker artifacts, with links rebased and original parts retained. | All 206 IDs now occur explicitly in both checker records; traceability repair adds no scientific conclusion. |
| Ledger inclusion-audit column | Coordinator must copy CONFIRMED for C001–C016 from this artifact. | The audit makes these 16 threshold decisions; no candidate state or disposition is changed. |
| Final report cards | Fresh generator must provide every required report-spec label; copy domain/type/all relationships/roles/evidence/audit/finding fields exactly; individually anchor every affected physical source page. | Report assembly follows this audit. Range shorthand in the ledger must not omit locations already individually supplied in the recheck. |
| Report impact and ambiguity | Preserve every candidate's bounded alternative and name only the affected value/specification; avoid claims of realized meta-analysis harm, actual changed fit, conducted omission or corrected result. | Missing plans, unrounded values, sample memberships and assay inputs limit inference, not source coverage. |
| Final run controls | Add fresh medium report-generator runtime; complete report coverage rows; finalize performance fields; recompute after-hashes; render HTML; remove fallback environment; finalize tooling; run validator to PASS. | Scheduled downstream operations; the current audit does not claim final report/HTML/cleanup/validation already exists. |

## Classification closure and limitations

All 16 evidence states are reproduced and supported by a determining source-confirmation fact. None rests on a display-zero P value. Domain totals reconcile: protocol_report 7, statistical_results 5, report_internal_inconsistency 1, plan_material 3. Primary relationships reconcile: P_R 7, S_C 3, S_W 3, P_P 3. Every primary type is present in its all-relationships list and follows P_R > P_P > S_C > S_W. PLAN/REPORT roles are assigned from content, including prospective bundles supplied as supplements, and corroborating-only documents do not create conflict relationships.

The threshold audit confirms 16 and questions 0. The 27 screening decisions remain 16 included and 11 screened out; historical checker exclusions already repaired in pass 2 are explicitly accounted for. No additional qualifying observation was found in either direction, so no F-QA finding or new screening row is required. No count target governed this result.

Missing earlier governing Master/PD plans, dated amendments, unrounded output, posterior/model data, exact fitted covariate identity, subgroup membership and assay limits/counts remain bounded limitations. No raw-data, broad design, clinical, novelty or conduct audit was attempted. C014/C015 concern supplied primary-design illustrations, with later-version applicability explicitly limited, rather than observed CNM-Au8 outcomes. C015 confirms a possible source-printed numerical sign reading with punctuation intent unresolved, not an actual negative computed probability. C016 confirms replacement-target wording with numerical impact unknown.

Neutral vocabulary checks found no prohibited issue terms in the canonical ledger, screen and recheck outside permitted established statistical terms. Source/page identity, calculation rules, direct observations and inferred explanations remain separate. Final release requires the scheduled report classification equality, link checks, cleanup and validator PASS; this completed scientific audit supplies every stable ID without suppressing an assigned candidate.

