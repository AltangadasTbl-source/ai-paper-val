# Statistical Pass 1 PLAN Extension Checker

- Runtime agent ID: 01a1288b-cbda-7140-94f6-958da8f7a6b8
- Model: gpt-6.1-sol
- Reasoning effort: high
- Start mode: FRESH_SPAWN
- Task: /root/stats_pass1_plan_extension
- Exact scope: DOC-002 PLAN pp. 17-23 and 31-33 formulas, inferential rules, power and monitoring; p. 9 total-PUFA, omega-3 and omega-6 InCHIANTI tests; p. 6 Figure3 survival strata; p. 7 Figure5 curves and stars.
- Relationships: 95, S601-S695, all PASS_1_COMPLETE.
- Local candidates: 3, STAT-PE01, STAT-PE02, STAT-PE03.
- Inventory artifact: statistics/parts/pass1_plan_extension_inventory.md.
- Human status: Pending Human Adjudication.

This fresh shard is separate from primary pass 1 and all supplemental-result shards. It cannot serve as pass 2. Canonical S merge and stable C registration belong to the coordinator. Every relationship is listed individually in the inventory, including all twelve Table2 power cells and all three distinct InCHIANTI tests. No candidate-count threshold was used.

## Applied check coverage

For every record, check printed interval endpoint ordering and point containment when endpoints exist, sign/direction, scale/unit/effect measure, matchable cross-location repetition, and supplied inferential definitions. This extension has no printed numeric estimate-CI pair for the three historical InCHIANTI tests or planned coefficients. Historical survival and ACR curves were inspected visually, with graphical domain/direction checks and no reconstruction of unprinted exact coordinates or CI endpoints. Power cells were separately checked for [0,1] bounds, direction with effect magnitude, exact narrative repetitions and printed four-year units.

Exact P/CI/test/statistic/SE compatibility is unavailable when definitions are missing. Neither sidedness nor df, covariance, variance estimator or power algorithm was supplied for original ANCOVA cells; none was inferred. Addendum explicitly supplies two-sided alpha.05 but not simulation covariance and implementation. The monitoring diagnostic 2×standard-normal upper-tail(3)≈.0026998 agrees with printed P=.0027 to four decimals; it is explicitly a conditional two-sided standard-normal diagnostic, not a claim the source named sidedness. No candidate relies on a reconstructed test or normal approximation.

All locations compared below are PLAN by content. Protocol background/historical results stay PLAN. No REPORT location contributes to these three discrepancies, so each provisional relationship is P_P only; coordinator determines stable classification. No P display zero occurs; coherent display zeros would be DISPLAY_ZERO_NOT_CANDIDATE. No candidate concerns literal-zero formatting or unreported definitions alone.

## STAT-PE01 — Original eGFR outcome called dichotomous and continuous

**Linked relationship:** S617.

**Candidate statement:** The original protocol calls the same eGFR-change outcome a secondary dichotomous outcome and immediately states it is analyzed as a continuous variable. The printed variable-type label conflicts with the displayed change formula and subsequent continuous ANCOVA specification.

**Compared locations and roles:**
- PLAN [DOC-002 PDF p.17, VI.c opening sentence](../../../../joi190122supp1_prod.pdf#page=17): “As a secondary dichotomous outcome” followed by change in eGFR from baseline to year4, “analyzed as a continuous variable.”
- PLAN [DOC-002 PDF p.17, VI.c change definition](../../../../joi190122supp1_prod.pdf#page=17): eGFR4−eGFR0, without a binary threshold for this continuous outcome.
- PLAN [DOC-002 PDF p.18, VI.e and Equation4](../../../../joi190122supp1_prod.pdf#page=18): ACR and eGFR changes “are continuous variables” tested using ANCOVA; eGFR4 is modeled on baseline eGFR and treatment assignment.

**Printed versus comparator:** “dichotomous” versus “continuous,” for the same baseline-to-year4 eGFR change. The separate binary composite endpoint on p17 is a different outcome and is not used as a comparator.

**Rule and calculation:** A single specified analysis variable cannot simultaneously carry mutually different dichotomous and continuous type labels under the same stated definition. The formula eGFR4−eGFR0 carries no threshold-based two-category coding, and Equation4 has continuous eGFR outcome. This is a direct label identity comparison, not a reconstruction of fitted data. Rounding tolerance: not applicable.

**Direct observation versus inference:** Both labels and the unthresholded formula are directly printed and visually confirmed. A copied word from the next composite paragraph is a possible explanation only; no production mechanism is asserted.

**Missing definition:** No additional mathematical input is required for the wording conflict. Whether the word “dichotomous” was intended to refer to another secondary outcome requires author clarification.

**Alternative supplied-source interpretation:** The following composite paragraph is dichotomous and could be the intended referent; the opening sentence explicitly names eGFR change and continuous analysis, leaving a local wording question.

**Human question:** Which outcome does “secondary dichotomous” modify, and what variable-type label was intended for the eGFR4−eGFR0 ANCOVA outcome?

**Provisional classification:** Measure, label, or scale inconsistency; P_P; all relationships P_P; compared PLAN versus PLAN; derived review domain plan_material. No evidence-state or disposition assignment made by this checker.

**Source confirmation:** Exact p17/p18 source-matched rendered pages visually inspected. Native/layout transcription agrees.

**Bounded relevance:** A data extractor could copy an incorrect continuous/binary endpoint label from protocol metadata; no effect on paper conclusions is inferred.

## STAT-PE02 — Table2 co-primary label differs from original endpoint hierarchy

**Linked relationship:** S618; corroborating power values S643-S654 and repeated narrative S655.

**Candidate statement:** Table2 titles urine ACR and eGFR as co-primary outcomes, while the same original protocol explicitly labels ACR primary and eGFR secondary.

**Compared locations and roles:**
- PLAN [DOC-002 PDF p.17, VI.b](../../../../joi190122supp1_prod.pdf#page=17): primary outcome is baseline-to-year4 urine ACR change.
- PLAN [DOC-002 PDF p.17, VI.c](../../../../joi190122supp1_prod.pdf#page=17): eGFR change from baseline to year4 is in secondary study outcomes.
- PLAN [DOC-002 PDF p.19, Table2 title and VI.h narrative](../../../../joi190122supp1_prod.pdf#page=19): “Study power for co-primary study outcomes, by effect size”; columns urine ACR and estimated GFR. Nearby prose also calls them co-primary continuous outcomes.

**Printed versus comparator:** The same original four-year ACR/eGFR pair has primary/secondary hierarchy in VI.b/VI.c, versus co-primary hierarchy in the power table and prose. Numerical90% entries17% ACR and2.6eGFR agree between table and narrative; the candidate is the inferential endpoint label, not a numeric power mismatch.

**Rule and calculation:** Match same plan version, baseline-to-year4 time and continuous outcomes. “Co-primary” places both outcomes in the primary tier; “primary ACR/secondary eGFR” places eGFR in a different tier. Direct label comparison; no numerical calculation or rounding tolerance needed.

**Direct observation versus inference:** Hierarchy words are directly observed on p17/p19 and visually confirmed. No multiplicity violation or actual analysis departure is inferred. The explicit p31-33 amendment changes hierarchy/time later and does not resolve differing labels within the original plan.

**Missing definition:** Whether “co-primary” was a generic power-table descriptor, an intended original hierarchy, or an unreconciled wording carryover is not specified. Original alpha.05 without correction is printed but does not adjudicate the labeling question.

**Alternative supplied-source interpretation:** Power was calculated for both continuous outcomes; “co-primary” might have been used informally to group their calculations. VI.b/VI.c remain formally different labels.

**Human question:** Which endpoint hierarchy should be extracted for the June28,2010 original protocol, and was the p19 co-primary label intended to supersede p17?

**Provisional classification:** Measure, label, or scale inconsistency; P_P; all relationships P_P; PLAN versus PLAN; derived review domain plan_material. No evidence state or suggested disposition assigned here.

**Source confirmation:** Original p17 and p19 source-matched rendered pages visually inspected; exact title and text match current extraction.

**Bounded relevance:** Protocol-based extraction could classify eGFR as primary or secondary depending on which supplied section is copied. No protocol-violation or conclusion-impact judgment made.

## STAT-PE03 — Exponentiated ACR coefficient labeled as relative contrast of percent changes

**Linked relationship:** S623; same parallel omega3 interpretation tracked S625.

**Candidate statement:** The original plan defines percent change as (ACR4−ACR0)/ACR0, then states that exp(beta2)−1 from an ANCOVA of log(ACR4) represents the relative difference in that percent change. At a common baseline, the supplied equation identifies an exponentiated follow-up ratio; the relative difference between the defined changes is generally a different quantity.

**Compared locations and roles:**
- PLAN [DOC-002 PDF p.17, VI.b](../../../../joi190122supp1_prod.pdf#page=17): percent change is summarized as (ACR4−ACR0)/ACR0.
- PLAN [DOC-002 PDF p.18, VI.e Equation3 and following coefficient definition](../../../../joi190122supp1_prod.pdf#page=18): log(ACR4)=beta0+beta1log(ACR0)+beta2(vitamin D)+e; log is explicitly natural log in the prior equation. “[exp(beta2)−1] represents the relative difference in percent change in albuminuria” comparing active vitaminD to placebo; accompanying95%CI/P assess treatment effect.
- PLAN [DOC-002 PDF p.18, parallel equations statement](../../../../joi190122supp1_prod.pdf#page=18): same form is proposed for omega3. This is shared provenance, not another distinct candidate.

**Rule and calculation:** Hold the supplied baseline and the fitted equation's non-treatment components fixed. Let B be the common positive baseline ACR; P and A the exponentiated modeled log-follow-up values for placebo and active treatment. Equation3 gives q=A/P=exp(beta2). Defined changes are cP=(P−B)/B and cA=(A−B)/B. For cP nonzero, their relative difference is (cA−cP)/cP=(A−P)/(P−B)=(q−1)×P/(P−B), which is generally different from q−1. Multiplying both c values by100 to report percentage units does not remove the difference. No covariance or inferential convention is needed for this algebraic scale distinction. Tolerance: exact algebra, no rounding.

**Labeled diagnostic example:** Hypothetical values B=100, P=200, A=100 give q=.5 and exp(beta2)−1=−.5, while defined change is1 (100%) for placebo and0 for active; relative difference in changes is−1 (−100%). These are demonstration inputs, not observed study data and not a reconstructed treatment estimate.

**Direct observation versus inference:** Both the change formula and coefficient label are directly printed and visually confirmed. The derivation is a deterministic identity using the supplied equation at common baseline. It does not assume beta1=1, fit a model, infer an SE or prescribe a new estimate.

**Missing definition:** The protocol does not define whether “relative difference in percent change” is informal shorthand for a baseline-adjusted geometric follow-up ratio, a ratio of fold changes, or the literal relative difference of the VI.b defined changes. Link-function prediction versus arithmetic means, retransformation and exact estimand mapping are unreported; the demonstration concerns exponentiated fitted log values, not arithmetic-mean predictions.

**Alternative supplied-source interpretation:** If the phrase informally refers to the ratio of follow-up/baseline fold changes, q−1 can express a proportional contrast at common baseline. That requires distinguishing fold change ACR4/ACR0 from the printed fractional increment (ACR4−ACR0)/ACR0.

**Human question:** Was exp(beta2)−1 intended as a baseline-adjusted proportional follow-up difference or ratio-of-fold-changes contrast, and how should its label distinguish it from a literal relative difference between VI.b defined percent changes?

**Provisional classification:** Measure, label, or scale inconsistency; P_P; all relationships P_P; PLAN versus PLAN; derived review domain plan_material. No evidence-state or disposition assignment made.

**Source confirmation:** Exact p17 formula and p18 Equation3/label visually confirmed in source-matched renders; current native/layout transcription agrees.

**Bounded relevance:** An extractor could treat the coefficient as a relative contrast of percentage increments instead of the modeled multiplicative ACR contrast. No actual numerical treatment estimate or paper conclusion is adjudicated.

## Non-candidate records and precise limitations

- S601-S603: three independent bounded P<.0001 tests have coherent direction but no coefficients, CIs or exact test definitions; no contradiction inferred.
- S604-S615: Figure3 survival [0,1] domain and Figure5 positive ACR/direction are coherent. N691 is total historical sample, not a risk-set denominator. Star thresholds, groups, error-bar type, CI levels and curve coordinates are unprinted.
- S640-S666: Original power domain, monotonicity, time units and exact table/narrative values reconcile. Original ANCOVA sidedness, df, power algorithm and percent-effect orientation are absent. No assumption that composite incidence equals sum of overlapping component incidences.
- S656: Dilution arithmetic17/.8=21.25 and2.6/.8=3.25 is diagnostic; published21%/3.2 may reflect rounding or imperfectly specified dilution, and no supplied rounding rule establishes a contradiction.
- S667-S668: Z3/P.0027 agrees with an explicitly conditional two-sided standard-normal diagnostic; repeated-look exact familywise alpha cannot be calculated from the supplied schedule/variance information.
- S669: Plan10 imputations is retained literally. Report comparison belongs to matched cross-source checking, rather than an independent emitted record here.
- S670: Equation1 omits a separately printed common time term while Equation2 prints one. Missing intended coding/constraints/error definitions create an implementation limitation, not a candidate solely from an omitted model term.
- S671-S676: Categorical times0,2,5, interaction threshold.05,95%CI and year5-only inference are retained literally; no scalar/joint interaction test or unprinted year2 P inferred.
- S678-S684: Original versus amended subgroup directions are version-keyed; an explicitly disclosed amendment is not automatically a same-result contradiction.
- S688-S691:2000replications,1058(80%) and80%power at2.3 are coherent with graphic direction. Inverse1058/.8=1322.5 is only a diagnostic treating rounded80% exact; no printed denominator in this section creates an impossible sample. Simulation covariance/algorithm and exact curve points absent.
- S692-S695: Four safety incidence comparisons are prospective rules, with no observed counts/rates/person-time/P/CI or test. Neither incidence-rate nor proportion interpretation is forced.

All95 relationship records are PASS_1_COMPLETE. Fresh pass2 must revisit S601-S695 using the complete cross-lane ledger and mechanical recheck, including the three local candidates after stable registration. Candidate discovery remains uncapped; there are no severity/validity/adjudication labels.

