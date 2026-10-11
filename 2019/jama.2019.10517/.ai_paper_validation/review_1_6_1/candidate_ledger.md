# Stable Candidate Ledger

Pending Human Adjudication. Independent initial screening produced two distinct included issues, registered in main-report source order. Stable IDs are never deleted. No candidate count target was applied. Mechanical recheck confirms reproduced evidence states for both IDs. The final auditor confirms inclusion for both IDs under all four threshold criteria.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | PLAN protocol p.12 vs REPORT main article p.4 | reproduced | CONFIRMED | F-XS-001 |
| C002 | protocol_report | P_R | P_R | PLAN protocol p.14 vs REPORT main article pp.5,7 | reproduced | CONFIRMED | F-XS-002 |

## C001 — Additional HDRS change condition in the primary relapse definition

**Candidate statement:** The planned HDRS component of the primary relapse endpoint requires a score of at least 18 and an additional five-point rise from randomized baseline; the reported component specifies the absolute score threshold alone. Allowed near-remission entry scores make these definitions nonequivalent.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol p.12 vs REPORT main article p.4
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-001
**Checker provenance:** Included F-XS-001 from the cross-source checker, independently corroborated by statistical pass 1 F-ST1-001, screened out as DUPLICATE_OF_INCLUDED and mapped to C001. All locations from both findings are retained.
**Classification rationale:** A positive prospective primary-endpoint specification in PLAN is compared with the reported endpoint definition in REPORT. Supporting eligibility/result passages establish relevance and do not add independent relationships. P_R implies protocol_report.
**Classification ambiguity:** No content-role ambiguity. The package does not identify whether the shorter reported definition abbreviates an operationally retained condition or reflects an amendment.

**Exact source locations:** PLAN [protocol p.12, section 3.9.8, especially lines 556–557](../../joi190079supp1_prod.pdf#page=12); PLAN [protocol p.7, remission/near-remission eligibility](../../joi190079supp1_prod.pdf#page=7); REPORT [main p.4, Primary Outcome: Relapse](../../jama_flint_2019_oi_190079.pdf#page=4); REPORT [main p.3, near-remission/randomization eligibility](../../jama_flint_2019_oi_190079.pdf#page=3); REPORT [main p.1, abstract primary result](../../jama_flint_2019_oi_190079.pdf#page=1); REPORT [main p.6, primary Cox result](../../jama_flint_2019_oi_190079.pdf#page=6); REPORT [main p.7, continued Cox result and Table 3 events](../../jama_flint_2019_oi_190079.pdf#page=7).

**Source evidence:** Protocol prints HAM-D ≥18 and a “mean absolute increase of 5 points” relative to RCT entry. Report prints 17-item HDRS score of 18 or higher. HDRS/HAM-D names identify the same instrument. The report permits entry scores 11–15 for near-remission.
**Reported-versus-comparator:** Report score ≥18 versus plan score ≥18 with the additional five-point baseline-change condition.
**Reasoning procedure:** Read both positive definitions and establish whether the change condition follows necessarily from eligible entry scores. No observed event change is assumed.
**Calculation:** A logical illustration only: entry 15 and later 18 implies a three-point increase. It satisfies the reported score component but not a five-point change requirement; entry 14 implies four points. Integer score criteria have no display-precision reconciliation.
**Affected result or extracted value:** Operational primary composite-relapse definition attached to 13/64 versus 34/62 events and adjusted HR 0.25 (95% CI 0.13–0.48), P<.001.
**Why context does not resolve it:** The reported requirements and supplied prospective conjunction differ; near-remission entry prevents treating the extra condition as universally redundant. The immediate context does not establish the final algorithm used for the events.
**Alternative source-grounded interpretations:** The report may abbreviate a retained operational condition, or the score component may have been revised to the absolute threshold alone. Other composite components may qualify events independently. No participant-level baseline/event scores or final endpoint amendment are supplied; no count or conclusion change is inferred.
**Human verification steps:** Confirm the printed conjunction and report component, identify the approved final relapse algorithm and any amendment, and establish which criterion generated the primary events.
**Remaining human question:** Was the five-point increase condition retained for the score-based primary relapse component, or prospectively amended before generating the reported primary result?

## C002 — Planned metabolic observation exclusion appears as a post hoc sensitivity

**Candidate statement:** The prospective H2 specification excludes pertinent metabolic observations after new or changed hyperlipidemia treatment. The report describes this operation as a post hoc sensitivity beside analyses including all participants, leaving the relation of the headline estimates to the prospective rule unclear.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol p.14 vs REPORT main article pp.5,7
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-002
**Checker provenance:** Included F-XS-002 from the cross-source checker, independently corroborated by statistical pass 1 F-ST1-002, screened out as DUPLICATE_OF_INCLUDED and mapped to C002. All affected locations from both are retained.
**Classification rationale:** A prospective observation-inclusion specification in PLAN is compared with the reported main-versus-sensitivity implementation in REPORT for H2 key secondary outcomes. Multiple report passages form one plan/report issue; no distinct report-internal conflict is asserted. P_R implies protocol_report.
**Classification ambiguity:** No content-role ambiguity. A later supplied-source amendment or exact sensitivity coefficients are unavailable; the issue does not establish which individual observations changed an estimate.

**Exact source locations:** PLAN [protocol p.14, H2, lines 660–679, especially 673–675](../../joi190079supp1_prod.pdf#page=14); REPORT [main p.5, Statistical Analyses continuation](../../jama_flint_2019_oi_190079.pdf#page=5); REPORT [main p.7, Secondary Outcomes and medication-change sensitivity](../../jama_flint_2019_oi_190079.pdf#page=7); REPORT [main p.1, abstract cholesterol/triglyceride results](../../jama_flint_2019_oi_190079.pdf#page=1).

**Source evidence:** Plan says relevant metabolic data after new or changed hyperlipidemia treatment “will be excluded from the mixed model.” Report describes post hoc analyses excluding pertinent post-change data after statin or hypoglycemic treatment; 12 statin changes occurred, six per arm, and three hypoglycemic changes occurred, two/one. It states sensitivity results were qualitatively similar to analyses including all participants.
**Reported-versus-comparator:** Prospective exclusion in the H2 model versus reported post hoc sensitivity exclusion alongside main reported metabolic analyses. The hypoglycemic extension is context; the conflicting prospective rule concerns hyperlipidemia treatment.
**Reasoning procedure:** Match prospective H2 outcome and mixed-model data handling with reported sensitivity and headline results. Distinguish observation exclusion from complete participant removal; no medication-based reassignment is inferred.
**Calculation:** Six plus six equals 12 statin starts/changes, establishing applicability. The operation concerns observation-inclusion logic, not rounded numerical inputs. Exact coefficients after exclusion cannot be recalculated from the supplied aggregate data.
**Affected result or extracted value:** Relation of the printed total-cholesterol daily coefficient 0.29 mg/dL (95% CI 0.13–0.45; adjusted P=.003) and triglyceride coefficient −0.153 mg/dL (95% CI −0.306 to 0.004; adjusted P=.25) to the prospectively specified medication-censored H2 analysis.
**Why context does not resolve it:** Qualitative similarity supplies neither exact planned-analysis estimates nor an amendment reconciling the main-versus-sensitivity hierarchy. The positive analysis descriptions remain different despite the report identifying what sensitivity was performed.
**Alternative source-grounded interpretations:** The all-observation analysis may have become principal after a prospective amendment; the planned exclusion may have been implemented only as sensitivity; or the report may call a prespecified procedure post hoc. No later plan, analyte-specific excluded observations/dates, or exact censored coefficients are supplied. No numerical or significance change is asserted and no preferred analysis is proposed.
**Human verification steps:** Identify the final approved H2 data-inclusion rule and any amendment, establish which observations generated headline coefficients, and compare exact all-observation and medication-censored outputs.
**Remaining human question:** Which medication-change observation-inclusion rule generated the headline H2 estimates, and how was the reported main-versus-sensitivity hierarchy reconciled with the prospective plan?

**Mechanical recheck bound for C002:** The phrase “including all participants” does not prove that every post-change observation entered the headline models: participants may remain represented by earlier measurements after observation censoring. The reproduced issue concerns the positive prospective exclusion instruction and reported main-versus-sensitivity hierarchy, leaving the exact headline observation set unresolved. Triglycerides are explicitly pattern-mixture averaged; their precise medication-censoring interaction and exact sensitivity outputs are not supplied. No participant removal, coefficient change, significance change or absence of an amendment is inferred.
