# Statistical Consistency Review — Pass 1

## Completion record

- **Pass:** 1 of 2.
- **Exact scope:** all 80 statistical relationships S001-S080 in `statistics/relationship_inventory.md`, reconstructed from complete canonical main and support evidence maps (DOC-001 pp. 1-11; DOC-002 pp. 1-25; DOC-003 pp. 1-167).
- **Status:** PASS_1_COMPLETE for every S ID.
- **Checks performed:** point-estimate containment; interval endpoint ordering; sign/direction; effect-measure and scale labels; matching abstract/narrative/table/figure/support repetitions; and test/P/CI/SE/statistic checks only where compatible definitions were explicitly supplied.
- **Stable S IDs:** 80.
- **Candidate proposals:** 5 (SP-01 through SP-05), without C IDs or disposition.
- **Display-zero records:** 0; no displayed finite-precision P zero was found.

## Evidence-check summary

All main-paper HRs and generalized ORs have positive ordered CIs containing their printed estimates, except the separately printed *incidence difference* in S013/SP-01. The main primary result is identical across abstract, narrative, Table 2, Figure 2 overall, Figure 3, and conclusion. Secondary and post-hoc repetitions are compatible after retaining outcome/time-window/population labels. The Figure 2 interaction P values were kept distinct from subgroup effect P values; source does not supply interaction test statistics or degrees of freedom.

Exact inferential compatibility was not assumed where Table 2 provides a log-rank P for the primary outcome but Cox HR CIs, or where row-level P-test labels are absent. Three log-scale CI-to-tail comparisons were retained only as explicitly labelled diagnostics in the inventory; none created a proposal. The support protocol/SAP is versioned prospective material; its historical and revised assumptions were not compared as if they were observed results.

## Candidate proposals for coordinator registration

| Proposal | S IDs | Exact source location(s) | Direct contradiction requiring human adjudication |
|---|---|---|---|
| SP-01 | S013 | DOC-001 Table 2, PDF p. 8 | Incidence difference -0.4% is outside its reported 95% CI (-2.4% to -1.7%). |
| SP-02 | S033 | DOC-002 Table S6, PDF p. 19 | BA header n=249 is incompatible with 9 (3.9): 9/249 rounds to 3.6%, not 3.9%. |
| SP-03 | S034 | DOC-002 Table S7, PDF p. 20; DOC-001 Figure 1, p. 5; DOC-002 Table S10, p. 23 | Header group total 471 conflicts with displayed site patient total 501 without a stated population distinction. |
| SP-04 | S035-S038 | DOC-002 Table S8, PDF p. 21; DOC-001 Figure 1, p. 5; DOC-002 Table S10, p. 23 | PPS headers 249/252 conflict with primary-row n(%) and supplied PPS denominators 233/238. |
| SP-05 | S039-S042 | DOC-002 Table S9, PDF p. 22; DOC-002 Table S10, p. 23 | ATS headers 249/252 conflict with primary-row n(%) and supplied ATS denominators 247/254. |

Each proposal is a candidate consistency observation only and remains pending human adjudication. No severity, validity, acceptance, rejection, or correction is assigned.

## Missing definitions retained for pass 2

- Cox coefficients, standard errors, variance estimator, covariate coding, and covariance structures.
- Exact statistic/df for Schoenfeld and subgroup interaction tests.
- Row-level selected P test for most main Table 2 outcomes, and selected EQ-5D test.
- Landmark-analysis specification, censoring details, and final subgroup-model specification.
- Event-level versus person-level basis for the SAP’s safety Fisher comparison.

## Display-zero policy record

No `P = 0`, `p = 0.000`, or equivalent appears in this assigned scope. No tail probability was derived to criticize zero display notation, and no display-zero candidate was generated.

## Pass-2 handoff

**Explicit pass-1 relationship register:** S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080.

Pass 2 must revisit S001-S080 with the complete candidate ledger and mechanical evidence-recheck facts, and append any genuinely new candidate proposals without changing these S IDs. It must record `PASS_2_COMPLETE` for every S record in the canonical inventory.
