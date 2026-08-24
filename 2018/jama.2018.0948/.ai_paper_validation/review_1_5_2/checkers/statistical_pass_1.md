# Statistical Pass 1 — Complete Source-Grounded Review

## Scope and method

Independent high-effort review of all `S001`–`S045`, using only supplied PDFs plus fresh native/layout extracts, renderings, and fresh maps. No legacy audit derivative or external source was used. Each CI was checked for endpoint order and containment. Diagnostic z/P checks use `estimate/(CI half-width/1.96)` only when the supplied CI and estimate have the same stated scale; they do not reconstruct robust/clustered GEE inference. Every record below is **PASS_1_COMPLETE**. “No candidate” is not a validity adjudication. Candidate leads are **Pending Human Adjudication**, are not stable `C` IDs, and have no disposition.

## DOC-001 main article

| S ID | Exact evidence and checks | Result |
|---|---|---|
| S001 | [p. 4](../../../jama_parshuram_2018_oi_180015.pdf#page=4) defines rate denominators (hospital/ICU discharges, ICU/eligible-unit days), clustered GEE, logit/Poisson/Gaussian and identity links. Units/scales are expressly distinct. | PASS_1_COMPLETE — no candidate; adjusted estimates not reproducible from crude counts. |
| S002 | [pp. 4–5](../../../jama_parshuram_2018_oi_180015.pdf#page=4) separates hospital and patient analyses; gives two-sided `.05` and Holm across 21 prespecified outcomes. | PASS_1_COMPLETE — no candidate; no individual inferential result in bundle. |
| S003 | [p. 4](../../../jama_parshuram_2018_oi_180015.pdf#page=4) planning `5.1/1000`, desired `1.0/1000`, detectable `.9/1000`, alpha `.05`, 80% power; [p. 8](../../../jama_parshuram_2018_oi_180015.pdf#page=8) distinguishes observed `1.69/1000`. | PASS_1_COMPLETE — no candidate; clustered-power formula inputs incomplete. |
| S004 | [p. 6 Table 2](../../../jama_parshuram_2018_oi_180015.pdf#page=6): heart rate `.58 (-.11,1.26), P=.10`; respiratory rate `.85 (.02,1.68), P=.05`. Ordered CIs contain estimates; compatible diagnostic two-sided P values are about `.10`/`.05`. Effects are adjusted difference-in-change, not raw means. | PASS_1_COMPLETE — no candidate. |
| S005 | [p. 6](../../../jama_parshuram_2018_oi_180015.pdf#page=6): systolic BP `1.12 (.59,1.65), P<.001`; saturation `1.06 (.27,1.85), P=.009`. Ordered CIs contain positive estimates; diagnostic P direction/magnitude agree. | PASS_1_COMPLETE — no candidate. |
| S006 | [p. 6](../../../jama_parshuram_2018_oi_180015.pdf#page=6): respiratory effort `4.67 (3.23,6.12), P<.001`; refill `4.65 (3.49,5.80), P<.001`. CIs ordered/containing; diagnostic z >6. | PASS_1_COMPLETE — no candidate. |
| S007 | [p. 6](../../../jama_parshuram_2018_oi_180015.pdf#page=6): oxygen `.37 (-.71,1.46), P=.50`; complete sets `38.1% (20.8%,55.4%), P<.001`. CIs/Ps compatible; raw fractions `2563/2588`, `1725/2832` match displayed percentages; binomial identity-link GEE is stated. | PASS_1_COMPLETE — no candidate. |
| S008 | [p. 7 Table 3](../../../jama_parshuram_2018_oi_180015.pdf#page=7): mortality `1.93` vs `1.56/1000`, difference `.01 (-.80,.81)`, OR `1.01 (.61,1.69), P=.96`; rates reproduce from printed counts/denominators, CIs ordered/containing, log-OR diagnostic P about `.96`. [Abstract p. 1](../../../jama_parshuram_2018_oi_180015.pdf#page=1) repeats values. | PASS_1_COMPLETE — no candidate. |
| S009 | [p. 7](../../../jama_parshuram_2018_oi_180015.pdf#page=7): no-DNR difference `.36 (-.53,1.25)`, OR `2.05 (.64,6.61), P=.23`. Same-scale CIs ordered/containing; log-OR diagnostic P agrees; no-DNR counts do not exceed deaths. | PASS_1_COMPLETE — no candidate. |
| S010 | [p. 7](../../../jama_parshuram_2018_oi_180015.pdf#page=7): SCD `-.34 (-.73,.05)/1000 days`, RR `.77 (.61,.97), P=.03`; `127/251859` and `259/307584` give `.50`/`.84`; log-RR diagnostic P about `.03`. [Abstract p. 1](../../../jama_parshuram_2018_oi_180015.pdf#page=1) matches. | PASS_1_COMPLETE — no candidate. |
| S011 | [p. 7](../../../jama_parshuram_2018_oi_180015.pdf#page=7): ICU mortality uses two explicit denominators: ICU-discharge OR `.89 (.51,1.57), P=.69`; hospital-discharge OR `.95 (.48,1.86), P=.88`. Each CI/P compatible; same events are not conflated. | PASS_1_COMPLETE — no candidate; ICU-discharge arm denominators absent. |
| S012 | [p. 7](../../../jama_parshuram_2018_oi_180015.pdf#page=7): arrest RR `1.02 (.65,1.62), P=.92`; preventable RR `.87 (.49,1.54), P=.62`. Ordered/containing CIs and log-RR diagnostic Ps agree. | PASS_1_COMPLETE — no candidate. |
| S013 | [p. 7](../../../jama_parshuram_2018_oi_180015.pdf#page=7): team-call RR `.98 (.82,1.17), P=.83`; physician-call RR `1.17 (.73,1.88), P=.52`. Log-RR CI/P checks agree. | PASS_1_COMPLETE — no candidate. |
| S014 | [pp. 7–8](../../../jama_parshuram_2018_oi_180015.pdf#page=7): consultation RR `1.05 (.85,1.30), P=.64`; urgent admission RR `.95 (.82,1.09), P=.45`. CIs/Ps agree; `828/1178` are explicitly SCD narrative admission denominators, not patient-days. | PASS_1_COMPLETE — no candidate. |
| S015 | [p. 7](../../../jama_parshuram_2018_oi_180015.pdf#page=7): ICU-readmission OR `1.11 (.77,1.61), P=.58`; hospital-readmission OR `.93 (.61,1.41), P=.74`. CI/P checks agree; rate denominators differ as footnoted. | PASS_1_COMPLETE — no candidate. |
| S016 | [p. 7 footnotes](../../../jama_parshuram_2018_oi_180015.pdf#page=7): exploratory rows Holm `P>.99`; weighted kappa `.35 (.15,.51)`. Kappa CI ordered/containing; compatible P/variance not printed. | PASS_1_COMPLETE — no candidate. |
| S017 | [p. 8](../../../jama_parshuram_2018_oi_180015.pdf#page=8): deaths `42 (6.1%)` vs `67 (6.9%)`, difference `-1.55% (-4.90,1.80), P=.36`; PIM difference `.69% (-.54,1.92), P=.27`. CIs/Ps compatible; `42+67=109`; 1653 patients is expressly not 2006 admissions. | PASS_1_COMPLETE — no candidate. |
| S018 | [p. 8 Figure 2 caption](../../../jama_parshuram_2018_oi_180015.pdf#page=8): slopes `.57` vs `.53`, difference `P=.94`. Direction is coherent; no CI, SE, df, or slope-test rule is supplied. | PASS_1_COMPLETE — no candidate; P cannot be recalculated. |

## DOC-002 protocol

| S ID | Exact evidence and checks | Result |
|---|---|---|
| S019 | [pp. 1,16](../../../joi180015supp1_prod.pdf#page=1) specifies descriptive hospital-period summaries, not an observed inferential estimate. | PASS_1_COMPLETE — no candidate; estimator/variance absent. |
| S020 | [pp. 1,16](../../../joi180015supp1_prod.pdf#page=1) specifies weighted hospital-level logit mortality model: arm, baseline logit, size stratum; reference is standard care. | PASS_1_COMPLETE — no candidate; no fitted coefficient/CI/P. |
| S021 | [p. 16](../../../joi180015supp1_prod.pdf#page=16) applies the same model to separately named ICU/DNR/readmission outcomes. | PASS_1_COMPLETE — no candidate; no observed result. |
| S022 | [pp. 1,16](../../../joi180015supp1_prod.pdf#page=1) specifies hospital Poisson models for event counts per 1000 patient-days. | PASS_1_COMPLETE — no candidate; no effect/P and no dispersion convention. |
| S023 | [p. 16](../../../joi180015supp1_prod.pdf#page=16) specifies weighted linear within-hospital means for explicitly different outcomes/units. | PASS_1_COMPLETE — no candidate; no coefficient/SE. |
| S024 | [p. 16](../../../joi180015supp1_prod.pdf#page=16) makes documentation regressions unweighted because records are equal per hospital. | PASS_1_COMPLETE — no candidate; calculated-score relationship incomplete. |
| S025 | [pp. 16–17](../../../joi180015supp1_prod.pdf#page=16) defines weighted surveys, subgroups, one outcome analysis/no interim analysis. | PASS_1_COMPLETE — no candidate; interaction/multiplicity details absent. |
| S026 | [pp. 7–9](../../../joi180015supp1_prod.pdf#page=7) defines concealed hospital allocation and `<200`/`>=200` strata. | PASS_1_COMPLETE — no candidate. |
| S027 | [pp. 7–8](../../../joi180015supp1_prod.pdf#page=7) sets competence `ICC>.90`, `<=2` score points; historical ICC `.92`/`.90` is descriptive. | PASS_1_COMPLETE — no candidate; ICC convention/CI omitted. |
| S028 | [p. 8](../../../joi180015supp1_prod.pdf#page=8) gives three distinct run-in `>80%` targets but no achieved rate/test. | PASS_1_COMPLETE — no candidate. |
| S029 | [pp. 11–12](../../../joi180015supp1_prod.pdf#page=11) specifies two blinded reviewers/pre-discussion kappa but not weighting/calculation. Scale conflict checked under P1-02/03. | PASS_1_COMPLETE — no standalone candidate. |
| S030 | [p. 20 Table 2](../../../joi180015supp1_prod.pdf#page=20) AUC CIs ordered/contain estimates (all `.87 [.85,.89]`); cases have higher medians; `772+616=1388`, `381+305=686`. `P<.0001` is threshold notation, not display-zero and not a candidate. | PASS_1_COMPLETE — no candidate; test/AUC variance not supplied. |
| S031 | [pp. 1,14](../../../joi180015supp1_prod.pdf#page=1) states 18% mortality RRR as `.9/1000`/`.09%`; [p. 29](../../../joi180015supp1_prod.pdf#page=29) calls that same 18% RRR `.9%`. With baseline `5.1/1000`, `.178×5.1=.9078/1000=.09078%`. | **Candidate lead P1-01** — direct cross-location unit/value contradiction. Human question: is p.29 `.9%` a reporting error or a distinct unstated scale? |
| S032 | [p. 29](../../../joi180015supp1_prod.pdf#page=29) gives `.178×5.1=.9078/1000` and `.199×3.2=.6368/1000`; arithmetic preserves scale. | PASS_1_COMPLETE — no additional candidate; P1-01 not duplicated. |
| S033 | [pp. 14–15,30](../../../joi180015supp1_prod.pdf#page=14): `.31×2/1000=.62/1000` as printed for SCDE planning. | PASS_1_COMPLETE — no candidate. |
| S034 | [p. 30](../../../joi180015supp1_prod.pdf#page=30): `.41×.75=.3075/1000`, compatible with `.3/1000`. | PASS_1_COMPLETE — no candidate. |
| S035 | [supplement 1 p. 30](../../../joi180015supp1_prod.pdf#page=30) states baseline stat-call rate `8.13/1000`, maximum RRR `.181`, and absolute reduction `1.45/1000`. Printed-input multiplication is `.181×8.13=1.47153/1000`, conventionally `1.47/1000` to two decimal places; the displayed-input rounding bounds do not contain `1.45`. | **Candidate lead P1-04 / appended C006** — direct printed-input arithmetic contradiction. Alternative explanation: undisplayed, more precise source inputs may have been used, but they are not supplied. Human question: what precise inputs/calculation produce the printed `1.45/1000`? |

## DOC-003 analysis plan

| S ID | Exact evidence and checks | Result |
|---|---|---|
| S036 | [p. 1](../../../joi180015supp2_prod.pdf#page=1) separates hospital-period binary `x/n` from count `x/patient-days` and declares exchangeable GEE. | PASS_1_COMPLETE — no candidate; plan only. |
| S037 | [pp. 1–2](../../../joi180015supp2_prod.pdf#page=1) provides distinct logit/identity binomial GEE risk/odds models and baseline transforms. | PASS_1_COMPLETE — no candidate; no fitted result. |
| S038 | [pp. 2–3](../../../joi180015supp2_prod.pdf#page=2) provides log-Poisson rate-ratio and identity-Poisson rate-difference models with time at risk. | PASS_1_COMPLETE — no candidate; no coefficient/CI/test. |
| S039 | [p. 3](../../../joi180015supp2_prod.pdf#page=3) prose says days are log-link offset and intervention/baseline predictors; printed code visually puts `Intervention + logBaseline` inside `offset(log(N)+...)` and has unmatched parentheses. Without executable output/provenance or an observed estimate, this does not establish a reporting contradiction. | PASS_1_COMPLETE — no candidate; diagnostic lead only: verify intended code against original analysis code. |
| S040 | [p. 4](../../../joi180015supp2_prod.pdf#page=4) defines Gaussian GEE continuous-outcome model with baseline mean/clustering. | PASS_1_COMPLETE — no candidate; no observed effect. |
| S041 | [pp. 4–5](../../../joi180015supp2_prod.pdf#page=4) lists separate GEE/GLMER, interaction, weighted and quasi-family sensitivity methods, without claiming numerical equality. | PASS_1_COMPLETE — no candidate. |
| S042 | [p. 5](../../../joi180015supp2_prod.pdf#page=5) lists identity-link probability/rate sensitivity analyses with distinct weights/variance structures. | PASS_1_COMPLETE — no candidate; fitted variance absent. |
| S043 | [p. 6](../../../joi180015supp2_prod.pdf#page=6) defines service-presence subgroups and treatment×subgroup GEE interaction. | PASS_1_COMPLETE — no candidate; no interaction result. |
| S044 | [p. 7](../../../joi180015supp2_prod.pdf#page=7) defines patient selection and first/sum/mean/any-day ICU aggregation rules. | PASS_1_COMPLETE — no candidate; no results. |

## DOC-004 supplementary results

| S ID | Exact evidence and checks | Result |
|---|---|---|
| S045 | [pp. 12–13 eTable 4](../../../joi180015supp3_prod.pdf#page=12) denominators `393,686,531,967`; percentages agree (e.g., `42/686=6.12%`, `67/967=6.93%`). Every adjusted-difference CI is ordered/contains estimate. Stated identity-binomial/Gaussian GEE makes CI/P direction compatible: mortality `-1.55 (-4.90,1.80), P=.36`; PIM `.69 (-.54,1.92), P=.27`; HFOV `-1.17 (-2.52,.19), P=.09`. Adjusted effects need not equal crude difference-in-changes. | PASS_1_COMPLETE — no candidate. |

## Additional cross-location candidate leads

### P1-02 — cardiac-arrest scale-label contradiction

- **Evidence:** [supplement 1 p. 11](../../../joi180015supp1_prod.pdf#page=11) defines cardiac arrest as scale `6 or 7`; [p. 24 Table 5](../../../joi180015supp1_prod.pdf#page=24) puts CPR/death at `6/7`; [p. 27 Table 6 legend](../../../joi180015supp1_prod.pdf#page=27) calls events including cardiac arrest “scale rating `4 or 5`.”
- **Comparator/rule:** same protocol seven-category scale; no different scale is identified.
- **Reasoning:** direct label contradiction, not an inferential approximation.
- **Human question:** Does p.27 intend another scale, or are `4 or 5` wrong?

### P1-03 — preventability-threshold contradiction

- **Evidence:** [p. 11](../../../joi180015supp1_prod.pdf#page=11) says rating `>4` but immediately includes `4,5,6`; [p. 28 Table 7](../../../joi180015supp1_prod.pdf#page=28) says `>=4`.
- **Comparator/rule:** the protocol’s own six-point threshold definition.
- **Reasoning:** direct textual/label contradiction; no unstated convention inferred.
- **Human question:** Is the operative threshold `>=4` or `>4`?

### P1-04 / appended C006 — stat-call planning arithmetic

- **Evidence:** [supplement 1 p. 30](../../../joi180015supp1_prod.pdf#page=30) prints baseline `8.13/1000 patient-days`, maximum relative risk reduction `.181`, and “absolute risk reduction of `1.45/1000` events per thousand patient days.”
- **Comparator/rule:** multiplication of the two displayed inputs on the printed rate scale: `8.13×.181=1.47153`, conventionally `1.47/1000` to two decimal places. The ranges from the displayed decimal precision do not include `1.45`.
- **Reasoning:** direct arithmetic from supplied printed inputs. An undisplayed more-precise baseline or RRR could explain the result, but no such input is supplied.
- **Human question:** What precise inputs or calculation produce the printed `1.45/1000`?

## Counts and limitations

- Complete records: **45/45 S IDs**; no sampling or count cap.
- Candidate leads: **4** (`P1-01`–`P1-04`, with P1-04 recorded as appended `C006`); diagnostic non-candidate lead: DOC-003 code/prose formula.
- No `P=0`, `p=.000`, or equivalent display-zero result supported a candidate. `P<.0001` was treated as a threshold display.
- Limitations: often absent are GEE covariance/df, exact test construction, multiplicity mechanics, raw model inputs, and estimand mappings. No P value was called inconsistent solely from a crude approximation and no adjusted effect was compared with an unmatched crude contrast.
