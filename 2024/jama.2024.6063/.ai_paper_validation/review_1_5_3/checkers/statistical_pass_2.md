# Statistical Consistency Review — Pass 2

## Execution, scope, and evidence boundary

- **Stage:** `statistics_pass_2`
- **Runtime agent ID:** `/root/statistical_pass_2`
- **Model / reasoning effort:** `gpt-5.6-terra` / `high`
- **Start mode:** `FRESH_SPAWN`; distinct from `/root/statistical_pass_1`.
- **Scope completed:** `S001`, `S002`, `S003`, `S004`, `S005`, `S006`, `S007`, `S008`, `S009`, `S010`, `S011`, `S012`, `S013`, `S014`, `S015`, `S016`, `S017`, `S018`, `S019`, `S020`, `S021`, `S022`, `S023`, `S024`, `S025`, `S026`, `S027`, `S028`, `S029`, `S030`, `S031`, `S032`, `S033`, `S034`, `S035`, `S036`, `S037`, `S038`, `S039`, `S040`, `S041`, `S042`, `S043`, `S044`, `S045`, `S046`, `S047`, `S048`, `S049`, `S050`, `S051`, `S052`, `S053`, `S054`, `S055`, `S056`, `S057`, `S058`, `S059`, `S060`, `S061`, `S062`, `S063`, `S064`, `S065`, `S066`, `S067`, `S068`, `S069`, `S070`, `S071`, `S072`, `S073`, `S074`, `S075`, `S076`, `S077`, `S078`, `S079`, `S080`, `S081`, `S082`, `S083`, `S084`, `S085`, `S086`, `S087`, `S088`, `S089`, `S090`, and `S091` (91 relationships).
- **Evidence used:** canonical main/support quantitative maps; `statistics/relationship_inventory.md`; `relationships/numeric_relationship_inventory.md`; numeric and cross-source checkers; `candidate_ledger.md` (`C001` through `C016`); and `verification/evidence_recheck.md`. Direct-source locations recorded by the mechanical recheck remain the authority. No web source, old report, or old-review conclusion was used.

## Pass-2 checking rules and limitations

Every S relationship was revisited for point-estimate containment, endpoint order, sign/direction, effect measure and scale label, matching repeated locations, denominator/population implications, arithmetic and duplicate-value implications, rate/count distinctions, cross-source implications, and mechanical-recheck facts. The main article and eTable 4 supply 95% intervals, a two-sided P-value context, and a linear-mixed-model description; eTable 4 additionally specifies log-binomial regression for responder RR. They do not supply a final-model covariance structure, degrees of freedom, variance estimator, exact CI construction, cell-level estimand mapping, or a shared test-calculation rule. Thus any interval/P compatibility observation is only a labelled conventional normal-approximation diagnostic, not an exact reconstruction or a basis to infer omitted definitions.

The planned protocol/SAP analysis and power statements (S086-S089) lack the formulas and mappings required for an exact compatibility calculation. The historical external pilot statements (S090-S091) lack a compatible test/model/CI definition. These absences are recorded as limitations, not as candidates.

No assigned relationship displays `P = 0`, `p = 0.000`, or an equivalent display zero. The displayed point estimates `0`, `0.0`, and `-0.0003` are not P values. Therefore no display-zero candidate was discovered or proposed.

## Cross-lane ledger and recheck reconciliation

| Ledger/recheck input | Statistical pass-2 implication |
|---|---|
| C001 | The 21-versus-23 placebo disposition count involves undefined completion/discontinuation category mapping. It does not supply a new compatible inferential contradiction for an S record. |
| C002 and C016 | The 167/165 adherence-population and 95%-versus-cited-table observations preserve a missing denominator/population definition. They do not establish an unreported estimand or test mapping for S086 or another S relationship. |
| C003, C004, C005, C006, C007, C008 | eTable 5 count/percentage reconciliations concern category denominators, not an estimate/interval/P relationship. No new S candidate follows. |
| C009 | Recheck directly confirms the identical week-4 arm-change estimates/intervals across the weight-bearing-pain and function rows. This is the existing duplicate-value implication for S036 and S048; no second proposal is emitted. |
| C010 | Recheck directly confirms the identical complete inferential result and arm-change fields for week-4 back pain and week-12 lower-leg strength. This is the existing duplicate-value implication for S060 and S066; no second proposal is emitted. |
| C011 | Recheck directly confirms the identical hsCRP and fasting-glucose contrast/interval/P fields at week 12. This is the existing duplicate-value/label implication for S076 and S084; no second proposal is emitted. |
| C012 | Recheck confirms Key Points prints `0.30`, while the matched primary result is negative in the Abstract, Table 2, Results, and eTable 1. This is the existing sign/direction implication for S001, S021, and S029; no second proposal is emitted. |
| C013, C014, C015 | These are event-count and cross-reference observations outside an S estimate/interval/P relationship. No new S candidate follows. |

## Relationship completion record

The complete individual pass-2 record is appended to `statistics/relationship_inventory.md`. All 91 records retain `PASS_1_COMPLETE` and now have explicit `PASS_2_COMPLETE` entries. Their pass-2 outcomes are summarized without using a candidate-count stop rule:

| Relationship set | Revisited checks and result |
|---|---|
| S001, S021, S029 | The primary result is contained in its interval, endpoints are ordered, VAS direction/scale is retained, and matched negative values round consistently. The independently printed Key Points positive sign remains the existing C012 implication. |
| S002-S020, excluding no IDs | Main Table 2 effects and ICC: containment, endpoint order, effect/scale labels, time point, and repeated-location checks complete. The separate C001, C002, C013-C016 population/count/cross-reference facts do not create an additional compatible inferential contradiction. |
| S022, S023 | eTable 1 sensitivity estimates: containment/order, negative direction, analysis labels, and diagnostic CI/P compatibility complete; no cross-lane contradiction. |
| S024, S025, S026, S027, S028 | Serial knee-pain VAS through 20 weeks: containment/order, direction and 0-100 scale checks complete. |
| S030, S031, S032, S033, S034, S035 | WOMAC total pain: containment/order, direction and 0-500 scale checks complete; S035 matches S003. |
| S036, S048 | C009 is the mechanically confirmed duplicated arm-change/interval pattern; between-group results are otherwise separately checked. |
| S037, S038, S039, S040, S041 | WOMAC weight-bearing pain: containment/order, direction and 0-300 scale checks complete. S038/S039 finite-precision zero estimates are not display-zero P values. |
| S042, S043, S044, S045, S046, S047 | WOMAC non-weight-bearing pain: containment/order, direction and 0-200 scale checks complete. |
| S049, S050, S051, S052, S053 | WOMAC function: containment/order, direction and 0-1700 scale checks complete. |
| S054, S055, S056, S057, S058, S059 | Hand-pain VAS: containment/order, direction and 0-100 scale checks complete. |
| S060, S066 | C010 is the mechanically confirmed complete duplicate across different endpoint/time labels and scales; the copied-field pattern, rather than raw subtraction, is the source-grounded implication. |
| S061, S062, S063, S064, S065 | Other back-pain VAS results: containment/order, direction and 0-100 scale checks complete. |
| S067 | Lower-leg strength, 24 weeks: containment/order, N unit and direction checks complete; matches S009. |
| S068, S069 | AQoL-6D: containment/order and -0.04-to-1 scale checks complete; no display-zero issue. |
| S070, S071, S072, S073, S074, S075 | OMERACT-OARSI RR: positive scale, log-binomial label, interval relation to 1, and repeated 24-week location checks complete. |
| S076, S084 | C011 is the mechanically confirmed duplicate contrast/interval/P pattern across hsCRP and fasting glucose; no cell-level model mapping is supplied to prescribe a correction. |
| S077 | hsCRP, 24 weeks: metric/interval/order and Table 2 match complete. |
| S078, S079 | Triglycerides: 12-week narrative match and distinct 24-week result retained. |
| S080, S081 | HDL: containment/order, sign, scale and 24-week match complete. |
| S082, S083 | LDL: containment/order and diagnostic CI/P compatibility complete; S082's upper bound `0.005` and P `.06` do not independently contradict under finite precision. |
| S085 | Fasting glucose, 24 weeks: containment/order and Table 2 match complete. |
| S086, S087, S088, S089 | Planned/final definition and power records revisited; missing compatible calculation definitions are named in the inventory. No convention-based reconstruction attempted. |
| S090, S091 | Historical external pilot records revisited; test/model/CI definitions remain absent, so no compatibility calculation is attempted. |

## Pass-2 candidate implications and handoff

- **Existing stable candidates implicated by statistical pass 2:** C009, C010, C011, and C012 only, with the S-record mappings above. Their inclusion here does not assign severity, validity, correction, acceptance, rejection, or disposition; all remain Pending Human Adjudication in the stable ledger.
- **New candidate proposals:** 0. No new C ID is requested, and no existing C ID is renumbered, merged, removed, or adjudicated.
- **Relationships completed:** 91 of 91, each explicitly marked `PASS_2_COMPLETE` in `statistics/relationship_inventory.md`.
- **Primary limitations:** unreported contrast orientation for displayed between-group changes; final-model covariance, degrees of freedom, variance estimator, CI/P construction, and cell-level estimand mapping; incomplete adherence denominators; and absent exact formulas for protocol power/historical pilot calculations.
- **Durable artifacts:** `statistics/relationship_inventory.md`; `checkers/statistical_pass_2.md`.

## Explicit pass-2 relationship register

PASS_2_COMPLETE for every relationship: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091.
