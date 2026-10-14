# Statistical pass 1 — plan shard

Runtime agent: /root/statistical_pass_1_plan. Fresh gpt-6.1-sol/high agent. Exact assigned scope: PLAN DOC-002 pages1–229 and PLAN DOC-003 pages1–65. REPORT evidence and DOC-003 pages66–130 are excluded from this disjoint shard. These294pages were covered through the current support001/002/003 complete maps, support004 complete summary/numeric displays and targeted authoritative source sections. Stable statistical relationships: S201–S294,94total, each explicit PASS_1_COMPLETE in statistics/parts/plan_relationship_inventory.md.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Checks cover allocation/sample-size arithmetic; endpoint/analysis hierarchy; pooled doses; shared-control populations; mortality/function coupling; covariance and random/fixed effects; every Bayesian prior; MCMC and posterior summaries; 10% futility/.979 superiority rules; secondary gatekeeping; missingness/imputation; supportive model/contrast/code; all primary sensitivity families; simulation assumptions; all operating-characteristic rows;24 illustrative simulation rows and8 interval displays. No raw-data, preferred-method, clinical, novelty or broad study-design audit was performed.

Direct confirmation used the supplied PDF and bundled pdf_tools.py layout helper via /home/juliz/venvs/stt/bin/python (PyMuPDF1.28.0), at preprocessing/statistics-1-plan/doc002-60-65.txt, doc003-8-30.txt, doc003-32-53.txt. Fresh source renders from support004 for DOC-00354,55,58,59,60 were visually inspected, including all estimates, interval endpoints, posterior probabilities and CAFS labels. No OCR or GPU inference was necessary. All sources, prior artifacts and reused assets are preserved.

## Pass 1 findings

No finding met the inclusion threshold within this PLAN-only scope. Count:0. Apparent discrepancies are listed once below. A zero finding count here does not decide cross-source REPORT/PLAN comparisons assigned to the other fresh statistical agent and cross-source reviewer.

## Reconciliation rules and missing definitions

- Sample allocation160×3/4=120,160×1/4=40,120/2=60. Interim40×3/4=30 and40×1/4=10.
- DRR.75 means25%slowing and.25 means75%; null1; posterior futilityP(DRR<.9)<.05 uses10%slowing. FinalsuccessP(DRR<1)>.979 differs from95%credible interval exclusion.
- Gamma(shape.01,rate1) baseline mortality prior mean=.01 andSD=sqrt(.01)=.1, matching the source. Variance hyperprior Gamma(shape1,rate.05²) concerns precision1/sigma_eta², not standard deviation.
- Every figure estimate falls inside ordered bounds. Bayesian common-DRR intervals are matched to the common-DRR posterior. Separate functional and mortality intervals and CAFS one-sided joint-rank P values are not aligned to the same named estimand.
- Numerical operating characteristics are simulations, not simple fixed two-group calculations. Virtual PRO-ACT sampling data, random seeds and MCMC outputs are not supplied. Independent stochastic reproduction is unavailable; no contradictory printed sample-size output is established. Diagnostic closed-form power calculations were not substituted.
- Current M-SAP v3 governs later regimens; regimen-C cover names Master v1. A later-default code/prose conflict therefore cannot establish that the reported regimen-C method relies on that specification. The other statistical agent confirms its assigned governing R-SAP3p122 includes treatment main effect in both equation andcode, while earlier Master v1 intentionally imposed shared baseline. This message is a scope/applicability handoff, not imported old conclusions.
- No noninferiority or equivalence margin/conclusion appears in this assigned trial design. No supplied standard error/test statistic accompanies the illustrative DRR intervals; normal approximations were not imposed on Bayesian bounds or on CAFS.

## Excluded observations

Only apparent issues decided not to emit are listed. Checks that reconcile appear in the S records.

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC-003 pp21–22 §6.5.3; governing p8,p63 | Later M-SAP3 random-slopes prose and equation include treatment-group main effect; its SAS code has month and treatment×month but omits treatment main effect. The supplied regimen-C governing cover identifies Master v1, and no reported result is shown to rely on this later default. This plan-only observation lacks the required relied-on statistical design relationship. | PERIPHERAL_COMPARISON |
| PLAN DOC-003 p22 §6.5.3 | Following the slope contrast, an estimand paragraph repeats repeated-measures/24-week change language. The same section explicitly names slope, month units, slope contrast and positive-slope interpretation, so intended slope quantity is immediately identifiable; no assigned reported value is misattributed. | CONTEXT_RESOLVES |
| PLAN DOC-003 pp18,36–37 | Text speaks of slowing mean time to death/time to mortality alongside a rate ratio. Explicit mortality hazard equation, DRR examples and rate-of-progression definition identify the rate parameter immediately. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-003 pp46–47 §5.2 | Prose calls the scenario set6parameters while the table numbers8. The displayed table names all assumptions and later tables show each scenario; this prose count does not change any participant denominator, reported result or planned decision rule. | CONTEXT_RESOLVES |
| PLAN DOC-002 p65; PLAN DOC-003 pp48–49 Table6.1.1 | Less-than1% early-futility narrative vs printed.01 operating probability: half-unit interval[.005,.015] admits probabilities below.01. No nonoverlapping precision interval. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-003 pp52–53 Table6.2.3 active deaths11 | Posterior.979 receives significance asterisk while final rule is>.979. Printed.979 admits[.9785,.9795], including values above.979; no independent contradictory interval or test for that same DRR is printed. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-003 pp58–59 Figure6.3.2 shared-control row | DRR.9(.64,1.29),posterior.714 alongside CAFS P.0026 appears divergent only if CAFS is misaligned to the commonDRR. Source explicitly distinguishes dynamic-sharing Bayesian DRR from fixed-sharing joint-rank estimand and demonstrates their different sensitivity; no P value is printed for the commonDRR. | NOT_REPRODUCED |
| PLAN DOC-003 p50 Table6.2.1 and adjacent prose | Prose says power and estimatedDRR decrease as mortality increases; tableDRR increases. Immediate next sentences giveDRR.75/.81 and explain that functional benefit decreases, so direction of the intended benefit statement is identifiable and not an independent decision or extracted trial result. | CONTEXT_RESOLVES |
| PLAN DOC-002 pp61–62 and PLAN DOC-003 pp35–36 | Protocol general all-longitudinal-data wording contrasts with explicit later AppendixI exclusion of functional data for participants reaching mortality. Protocol explicitly assigns precedence to AppendixI; the latter supplies the exact contributor definition. | CONTEXT_RESOLVES |
| PLAN DOC-003 p9 vs PLAN DOC-002 pp92,163 | Master maximum up-to28weeks versus regimen-C24weeks. Same master sentence allows RSA override; both supplied regimen-C appendices consistently specify24weeks. | CONTEXT_RESOLVES |
| PLAN DOC-003 p27 §6.6.1 | Poisson offset is logweeks while output rate unit is per100participant-years. A unit conversion can reconcile these; no printed rate from this plan demonstrates an omitted conversion. | CONDITIONAL_OR_UNREPORTED |

## Limitations and handoff

94relationships,0findings,11excluded observations. All294assignedpages mapped; zero scientific coverage gaps. Historical derivation engines are unspecified in some reused assets; current targeted layout/helper engine is recorded. Simulation example estimates lack raw inputs for independent posterior/operating-characteristic replication, and credible-interval construction is not named; no unsupported tail/model convention was inferred. Background preclinical/historical figures were mapped and retained as rationale rather than clinical-result evidence.

Primary durable artifact: checkers/parts/statistical_pass_1_plan.md. Relationship artifact: statistics/parts/plan_relationship_inventory.md. Coordinator must merge these94distinct S IDs into the canonical inventory; every S requires later distinct-agent PASS_2_COMPLETE. Runtime ID for execution manifest: /root/statistical_pass_1_plan.

