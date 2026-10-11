# Statistical consistency review — pass 1

Runtime task identity: `/root/statistics_pass1`. Fresh named statistical specialist, gpt-6.1-sol/high. Read completely QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md; read current tooling, source/coverage inventories and both complete quantitative maps. No legacy scientific conclusions, candidate artifacts or web evidence were used. Ownership: this artifact, statistics/relationship_inventory.md, and st1-prefixed preprocessing only.

Exact scope: all main S001–S030, all support S101–S129, and new supplementary cell groups S031–S035: 64 relationships across REPORT DOC-001 pp1–9, PLAN DOC-002 pp1–49, PLAN DOC-003 pp1–22, REPORT DOC-004 pp1–13 and administrative REPORT DOC-005 p1. The supplementary tables' entire238 paired comparisons,8 subgroup interactionP and9 graphicalP are included. All64 receive PASS_1_COMPLETE below and in the canonical inventory. One consolidated finding and18 excluded observations are recorded. No candidate IDs or adjudications are assigned.

Direct Poppler25.03.0 extraction was produced for mainpp4–7, SAPpp11–15 and protocolpp18–19. Mainp6 was directly rendered with pdftoppm25.03.0 at130dpi and visually inspected against all ten binary rows/footnote. Derivatives: preprocessing/st1-main-p4-7.txt, preprocessing/st1-sap-p11-15.txt, preprocessing/st1-protocol-p18-19.txt, preprocessing/st1-main-p6.png. Original sources/reusable assets remain unchanged.

## Finding

### F-ST1-001

**Exact locations and document roles:** REPORT [main article p6, Table2](../../../jama_simonis_2018_oi_180108.pdf#page=6), all ten RR rows and footnotec; REPORT [p4, Statistical Analysis](../../../jama_simonis_2018_oi_180108.pdf#page=4), secondary binary risk-ratio specification; REPORT [p1, abstract secondary results](../../../jama_simonis_2018_oi_180108.pdf#page=1), repeated pulmonary-complicationRRs. PLAN [SAPp13, Secondary outcomes](../../../joi180108supp2_prod.pdf#page=13) corroborates the treatment effect on binary outcomes as RR and the Wald approximation/chi-square specification; it is not a conflicting side. Table2 directly shows event counts within randomized strategy columns. Mainp6 render was visually checked.

**Relationship IDs:** S009,S015,S016,S019,S020,S021,S022,S023,S024,S120,S121. **Focus area:** B,C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. The PLAN text only corroborates the stated quantity and therefore does not add P_R.

**Printed values:**

| Outcome | Low event/total | Intermediate event/total | Printed RR (95%CI) | PrintedP | Event risk ratio from columns | Diagnostic reverse-conditioned ratio |
|---|---:|---:|---|---:|---:|---:|
| ICU mortality | 132/450 | 115/458 | 1.11(.96–1.27) | .15 | 1.16823 | 1.11084 |
| Hospital mortality | 151/477 | 140/484 | 1.06(.93–1.22) | .35 | 1.09440 | 1.06645 |
| ARDS | 17/448 | 23/462 | .86(.59–1.24) | .38 | .76223 | .85789 |
| Pneumonia | 19/450 | 17/462 | 1.07(.78–1.47) | .67 | 1.14745 | 1.07270 |
| Pneumothorax | 8/448 | 6/462 | 1.16(.73–1.84) | .55 | 1.37500 | 1.16364 |
| Atelectasis | 51/449 | 52/464 | 1.00(.81–1.23) | .94 | 1.01353 | 1.00771 |
| Extrapulmonary infection | 20/448 | 28/463 | .84(.60–1.18) | .28 | .73820 | .84015 |
| Extrapulmonary sepsis | 12/448 | 16/463 | .87(.56–1.33) | .50 | .77511 | .86796 |
| Delirium | 149/343 | 132/361 | 1.15(.99–1.34) | .06 | 1.18802 | 1.15616 |
| Need for tracheostomy | 54/477 | 52/484 | 1.03(.84–1.26) | .78 | 1.05370 | 1.02971 |

**Rule and calculation:** The stated effect of the intervention on an event risk compares P(event|low) with P(event|intermediate). For source counts a/n versus b/m this is (a/n)/(b/m). The complete printed pattern instead tracks q=[a/(a+b)]/[(n−a)/(n+m−a−b)], comparing P(low|event) with P(low|noevent). For ARDS, source column risk ratio=(17/448)/(23/462)=.76223, outside the printedRR.86 rounding interval[.855,.865); reverse-conditioned q=(17/40)/(431/870)=.85789. For pneumothorax, source column risk ratio=(8/448)/(6/462)=1.375, outside[1.155,1.165); reverse-conditioned q=(8/14)/(440/896)=1.16364. Integer source counts supply exact arithmetic; varying rounded printed percentages cannot bridge these differences.

Diagnostic only: the ordinary log-Wald interval for q uses SE²=1/a−1/(a+b)+1/(n−a)−1/(n+m−a−b). It yields ARDS[.59456,1.23784], matching printed[.59,1.24] at two decimal places, and pneumothorax[.73568,1.84055], close to printed[.73,1.84]. Across the ten rows this reverse conditioning also tracks the entire displayed interval pattern; some point/endpoints differ at the last displayed digit, so this is not asserted to reconstruct the exact pipeline or numerical formatting. No test statistic, covariate adjustment or coding mechanism is inferred. A chi-square test of association is invariant to table transpose, so the printedP values cannot determine which conditioning generated the reportedRRs. The finding concerns effect-measure identity rather than a claim thatP andCI must use the same approximation.

**Affected result or extracted value:** Treatment risk ratios and95%CIs for ICU/hospital mortality, ARDS, pneumonia, pneumothorax, atelectasis, extrapulmonary infection/sepsis, delirium and tracheostomy; the pulmonary-complicationRRs also occur in the abstract. For example, extracting.86 as the ARDS event-risk ratio differs from the column-count quantity.76223. The issue changes the effect quantity and interval an evidence extractor would use, while the stated nonsignificant secondary conclusions remain compatible with their printedP values.

**Why context does not resolve it:** Table2 footnotec and the methods explicitly call these intervention effects risk ratios and give no alternate conditioning, adjustment, link, covariate set, standardized risks, or other model specification that explains this repeated numerical pattern. The abstract repeats the effects without clarifying their estimand. The supplied SAP corroborates the same label. The source does not state that these are adjusted/model-basedRRs; the finding is supported by a consistent alternate conditional quantity and its interval pattern across the complete family, rather than by an isolated crude-versus-model comparison. Immediate context cannot select between the stated event-risk contrast and the alternate conditional contrast.

**Source-grounded alternatives and missing definition:** The printed values may describe an undocumented model-based treatmentRR; the analysis model, adjustments and marginalization would then need specification. Alternatively, the conditioning of the displayedRRs may be the reverse conditional risk identified above; the actual pipeline is not supplied. Neither explanation is asserted. Missing definition: which random variable is treated as the outcome, which groups form the risk denominators and reference category, and whether an additional binary model supplies these estimates. A preferred analysis is not proposed.

**Exact human question:** What outcome, denominator conditioning, reference group and any model adjustment generated the ten Table2RRs and95%CIs, and which estimates represent the stated risk of each event under low versus intermediate tidal-volume ventilation for extraction?

## Excluded observations

Each observation appears once with exactly one scope reason code. Repeated manifestations are consolidated.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 pp4–6,S011 | Rounded primary means15.2/15.5 give−.3 while displayedMD−.27; SD/n-derived diagnosticSE.74433 gives near.717P. Half-unit intervals permit reportedMD/CI/P. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p6,S013–S014; p7,S027–S028 | Mean-difference/GLM results differ from time-to-dischargeHRs; explicit distinct model/effect labels identify which applies. | CONTEXT_RESOLVES |
| REPORT DOC-001 pp1,6–7,S017–S018 | CoxHRs need not equal count-basedRRs; death timing is not supplied. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 pp3–7; PLAN DOC-003 pp11–12,S005,S115 | ITT wording with955complete cases versus961randomized:6missing,complete-case explicit and missing fraction.624% below1%trigger. | CONTEXT_RESOLVES |
| PLAN DOC-002 pp18–19; DOC-003 p11; REPORT DOC-001 p4,S004,S107 | Diagnostic normal approximation392.44/arm versus397; exact t implementation/sample-size software unstated. Protocol explicitly397×1.20=476.4 rounded476 explains952 target and inflation. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 p33; DOC-003 pp12–13,21,S111,S119 | OriginalCox primary changed to t; laterSAP and amendment table explicitly identify the reportedprimaryanalysis. | CONTEXT_RESOLVES |
| PLAN DOC-003 pp14–15,21; REPORT DOC-001 pp4,6,S128 | AdjustedGLM sensitivity not reported; modification table expressly says so, separateGLMMreportedP.72 is identifiable; no alternate adjusted effect printed. | CONTEXT_RESOLVES |
| PLAN DOC-003 pp13–14,22; REPORT DOC-001 pp4–7,S113,S122 | Perprotocol analysis not described, expressly disclosed in modification table; complete-case assigned-group primary remains identifiable. | CONTEXT_RESOLVES |
| PLAN DOC-003 pp14,21–22; REPORT DOC-001 pp4,6; DOC-004 p9,S123 | Gaussian subgroup distribution replaces zero-inflated plan; explicit amendment identifies reportedmodel, not an unresolved model choice. | CONTEXT_RESOLVES |
| PLAN DOC-003 p14; REPORT DOC-004 p9,S123 | Planned exploratory respiratory-rate subgroup lacks a printed result; no missing primary/keysecondaryresult or alternate extractedvalue demonstrated. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-003 p12; REPORT DOC-004 pp5–7,S118 | Day7 planned ventilatory displays versus first3days reported; exploratory per-time-point scope does not change primary/keysecondaryresult or decisionrule. | PERIPHERAL_COMPARISON |
| REPORT DOC-001 pp4–5; DOC-004 pp5–8,S006,S031–S034 | Individual day/modeP differs from general longitudinal narrative; exact supplemental per-cell tests/model contrasts are not supplied, and separate time/mode comparisons do not establish global-model contradiction. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-004 p6,S032 | Other-mode post-titrationPEEP8(5–1) obvious incomplete/reversed upperquantile; nearbyvalues/unit identify a typographic interval presentation rather than an inferentialCI. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-004 pp5–7,S031–S033 | Aggregate post-titrationpH upperIQR7.54 exceeds mode-level upperquantiles7.36/7.40/7.42; exploratory per-time-point descriptive comparison does not alter primary/keysecondaryresult,analysisn or decisionrule. | PERIPHERAL_COMPARISON |
| REPORT DOC-001 p6; DOC-004 p9,S029 | Main subgroup interval labeledIQR while eTable5explicitlylabels95%CI and prints identical limits; intendedinterval identifiable immediately. Empty mean()footer similarly resolves from±format. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-004 pp6,12,S035 | PSVVTday2P.03 versus graphicalP.027 is displayed precision. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 p35; DOC-003 p11,S115,S126 | 10%cost imputation trigger versus1%primary trigger refer to distinct analyses. | CONTEXT_RESOLVES |
| PLAN DOC-002 pp31–32,42; DOC-003 pp10–11; REPORT DOC-001 p2,S110 | Safety reviews and continuation do not imply numerical efficacyinterimanalysis; no quantitative stopping threshold supplied. | CONTEXT_RESOLVES |

## Complete pass-1 relationship record

| S ID | Record |
|---|---|
| S001 | PASS_1_COMPLETE |
| S002 | PASS_1_COMPLETE |
| S003 | PASS_1_COMPLETE |
| S004 | PASS_1_COMPLETE |
| S005 | PASS_1_COMPLETE |
| S006 | PASS_1_COMPLETE |
| S007 | PASS_1_COMPLETE |
| S008 | PASS_1_COMPLETE |
| S009 | PASS_1_COMPLETE |
| S010 | PASS_1_COMPLETE |
| S011 | PASS_1_COMPLETE |
| S012 | PASS_1_COMPLETE |
| S013 | PASS_1_COMPLETE |
| S014 | PASS_1_COMPLETE |
| S015 | PASS_1_COMPLETE |
| S016 | PASS_1_COMPLETE |
| S017 | PASS_1_COMPLETE |
| S018 | PASS_1_COMPLETE |
| S019 | PASS_1_COMPLETE |
| S020 | PASS_1_COMPLETE |
| S021 | PASS_1_COMPLETE |
| S022 | PASS_1_COMPLETE |
| S023 | PASS_1_COMPLETE |
| S024 | PASS_1_COMPLETE |
| S025 | PASS_1_COMPLETE |
| S026 | PASS_1_COMPLETE |
| S027 | PASS_1_COMPLETE |
| S028 | PASS_1_COMPLETE |
| S029 | PASS_1_COMPLETE |
| S030 | PASS_1_COMPLETE |
| S031 | PASS_1_COMPLETE |
| S032 | PASS_1_COMPLETE |
| S033 | PASS_1_COMPLETE |
| S034 | PASS_1_COMPLETE |
| S035 | PASS_1_COMPLETE |
| S101 | PASS_1_COMPLETE |
| S102 | PASS_1_COMPLETE |
| S103 | PASS_1_COMPLETE |
| S104 | PASS_1_COMPLETE |
| S105 | PASS_1_COMPLETE |
| S106 | PASS_1_COMPLETE |
| S107 | PASS_1_COMPLETE |
| S108 | PASS_1_COMPLETE |
| S109 | PASS_1_COMPLETE |
| S110 | PASS_1_COMPLETE |
| S111 | PASS_1_COMPLETE |
| S112 | PASS_1_COMPLETE |
| S113 | PASS_1_COMPLETE |
| S114 | PASS_1_COMPLETE |
| S115 | PASS_1_COMPLETE |
| S116 | PASS_1_COMPLETE |
| S117 | PASS_1_COMPLETE |
| S118 | PASS_1_COMPLETE |
| S119 | PASS_1_COMPLETE |
| S120 | PASS_1_COMPLETE |
| S121 | PASS_1_COMPLETE |
| S122 | PASS_1_COMPLETE |
| S123 | PASS_1_COMPLETE |
| S124 | PASS_1_COMPLETE |
| S125 | PASS_1_COMPLETE |
| S126 | PASS_1_COMPLETE |
| S127 | PASS_1_COMPLETE |
| S128 | PASS_1_COMPLETE |
| S129 | PASS_1_COMPLETE |

## Limitations

No source-unit coverage gap remains. Exact continuous and longitudinal test reproduction is limited by source-unstated statistics, variance choices, model links/covariance, survivor/subgroup sample sizes, individual outcome/event times and supplemental per-cell test mappings. Every limit is recorded with the affected relationships in statistics/relationship_inventory.md. No sidedness, test variant, covariance, variance estimator, degrees of freedom, denominator or model is inferred from convention. Sidedness/two-sided5% and95%intervals are supplied for the main formal analyses; absent details constrain exact reproduction rather than authorizing a preferred method. Noninferiority,equivalence and numerical stopping boundaries are not applicable. Costs/mediation have no reported quantitative estimate in this package.
