# Statistical pass 2 — procedure count and test shard

Runtime agent: /root/statistical_pass2_extra_d. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Exact disjoint scope: S198, S199, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S222. All 25 are DOC-003 REPORT eTable 6, physical PDF page 21, surgical and endoscopic procedures through 12 years. No other S record is owned by this shard.

The complete QUALITY_CONTROL_SCOPE.md, Workflow 1.6.2 review contract, bounded packet_06.md, and pass2_shared_context.md were read. The shared context contains the full current 14-issue ledger, every initial screening decision, every mechanical recheck, and all 53 checker exclusion rows. Source authority for each count, percentage, denominator, P value, procedure label, and footnote was visually reread in the current-run source-matched Poppler image preprocessing/stat_extra_source21.png. Current-run direct layout text preprocessing/screen_report_supp_direct.txt supplied the complete supporting method passages on pages 5–6. These derivatives were preserved; no rendering, OCR, external evidence, or custom Python was needed. Compute device: CPU; derivative engine: Poppler 26.01.0.

## Source-grounded checks and limits

[REPORT eTable 6 page 21](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21) explicitly gives n (%) and medical/lifestyle N=96 versus bariatric surgery N=166. Its footnote names chi-squared or Fisher's exact test. [REPORT page 6](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=6) states the same test family for adverse events/study outcomes. [REPORT page 5](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=5) calls secondary analyses hypothesis generating without multiple-testing adjustment. No adjusted effect model, coefficients, ORs, CIs, standard errors, or test statistics are supplied for these 25 rows.

For every row I checked both denominators, numerator bounds, percentages, event and nonevent accounting, observed direction, applicability of inferential checks, and compatibility with the stated test family. All central percentage calculations are contained in the respective one-decimal half-unit bands; consequently the full allowed input intervals also intersect those bands, with zero interval gap. Procedure rows are overlapping named categories, not an asserted mutually exclusive partition, and no sum of them is treated as a participant total. The matching denominator is the displayed full assigned group; nutritional or visit-observation denominators are not imported.

The retained pass-1 Pearson and probability-ordering Fisher calculations are explicitly diagnostics. They provide an internally compatible reconstruction for each printed P value and do not identify the authors' exact per-row test, Fisher sidedness/ordering, continuity correction, or software option. No such missing detail is assumed. All 24 numeric P bands intersect at least one diagnostic; the inequality P<.001 in S198 contains both. Thus none has a reproduced count/test discrepancy. No interval-versus-P comparison, point containment, endpoint order, coefficient sign, SE compatibility, noninferiority/equivalence margin, sample-size reproduction, interim/stopping rule, or adjusted multiplicity conclusion is applicable to these count/P-only rows. This is explicit lack of the needed printed quantity or claim, not a completed numerical reconstruction of absent quantities.

The supplied plan/report test-mapping issue is already screened under F-XS-010 and duplicate F-ST1-008. The complete recheck names the missing CMH strata, substitution rule, and test-to-row mapping, and retains the possibility that broad chi-squared denotes CMH. Reproducing ordinary 2-by-2 diagnostics does not remove that screened issue, prove an unstratified executed analysis, or create a second issue. No model-versus-crude effect comparison was made. No other screened issue changes these row inputs or authorizes importing a denominator, estimand, or software convention.

## Per-relationship pass-2 facts

MED and SURG inputs below retain the visually confirmed printed percentages; the compatible diagnostic is selected only as a check of the stated family. Every row has percentage interval gap 0, P interval gap 0, and relative discrepancy 0. S198 uses its literal inequality rather than a rounding band. The updated inventory preserves both diagnostic values and every original input.

| S ID | Procedure | Printed MED n (%) /96 | Printed SURG n (%) /166 | Printed P | Compatible diagnostic P | SURG observed direction versus MED | Pass 2 |
|---|---|---|---|---|---|---|---|
| S198 | Crossovers, conversions, and revisions | 24 (25.0) | 15 (9.0) | <.001 | Pearson .000469225; Fisher .000959658 | Lower | PASS_2_COMPLETE |
| S199 | Cholecystectomy | 2 (2.1) | 7 (4.2) | .49 | Fisher .493005380 | Higher | PASS_2_COMPLETE |
| S200 | Lysis of adhesions | 0 (0.0) | 2 (1.2) | .53 | Fisher .533912433 | Higher | PASS_2_COMPLETE |
| S201 | Hernia repair | 0 (0.0) | 2 (1.2) | .53 | Fisher .533912433 | Higher | PASS_2_COMPLETE |
| S202 | Exploratory laparoscopy | 0 (0.0) | 2 (1.2) | .53 | Fisher .533912433 | Higher | PASS_2_COMPLETE |
| S203 | Exploratory laparotomy | 0 (0.0) | 1 (0.6) | 1.00 | Fisher 1.000000000 | Higher | PASS_2_COMPLETE |
| S204 | Appendectomy | 0 (0.0) | 2 (1.2) | .53 | Fisher .533912433 | Higher | PASS_2_COMPLETE |
| S205 | Colon resection | 0 (0.0) | 2 (1.2) | .53 | Fisher .533912433 | Higher | PASS_2_COMPLETE |
| S206 | Hysterectomy | 0 (0.0) | 2 (1.2) | .53 | Fisher .533912433 | Higher | PASS_2_COMPLETE |
| S207 | Other abdominal surgery | 2 (2.1) | 5 (3.0) | 1.00 | Fisher 1.000000000 | Higher | PASS_2_COMPLETE |
| S208 | Endoscopic treatment of leak | 0 (0.0) | 1 (0.6) | 1.00 | Fisher 1.000000000 | Higher | PASS_2_COMPLETE |
| S209 | Endoscopic treatment of dilated GJ stoma | 0 (0.0) | 2 (1.2) | .53 | Fisher .533912433 | Higher | PASS_2_COMPLETE |
| S210 | Endoscopic treatment of GI bleeding | 1 (1.0) | 0 (0.0) | .37 | Fisher .366412214 | Lower | PASS_2_COMPLETE |
| S211 | Other therapeutic endoscopy | 2 (2.1) | 5 (3.0) | 1.00 | Fisher 1.000000000 | Higher | PASS_2_COMPLETE |
| S212 | Other endoscopy | 3 (3.1) | 14 (8.4) | .09 | Pearson .092795850 | Higher | PASS_2_COMPLETE |
| S213 | Joint injection | 9 (9.4) | 6 (3.6) | .053 | Pearson .053138680 | Lower | PASS_2_COMPLETE |
| S214 | Procedures for fractures | 1 (1.0) | 3 (1.8) | 1.00 | Fisher 1.000000000 | Higher | PASS_2_COMPLETE |
| S215 | Joint replacement | 5 (5.2) | 3 (1.8) | .12 | Pearson .123147800 | Lower | PASS_2_COMPLETE |
| S216 | Amputation | 0 (0.0) | 1 (0.6) | 1.00 | Fisher 1.000000000 | Higher | PASS_2_COMPLETE |
| S217 | Other orthopedic surgery | 13 (13.5) | 33 (19.9) | .19 | Pearson .193874867 | Higher | PASS_2_COMPLETE |
| S218 | Cataract surgery | 8 (8.3) | 13 (7.8) | .89 | Pearson .885351006 | Lower | PASS_2_COMPLETE |
| S219 | Other eye surgery | 4 (4.2) | 6 (3.6) | .82 | Pearson .822156259 | Lower | PASS_2_COMPLETE |
| S220 | Vitrectomy | 2 (2.1) | 1 (0.6) | .56 | Fisher .556320489 | Lower | PASS_2_COMPLETE |
| S221 | Panniculectomy or abdominoplasty | 0 (0.0) | 5 (3.0) | .16 | Fisher .161712951 | Higher | PASS_2_COMPLETE |
| S222 | Other plastic surgery | 2 (2.1) | 1 (0.6) | .56 | Fisher .556320489 | Lower | PASS_2_COMPLETE |

## Findings

No new finding meets the inclusion threshold in S198–S222. Every assigned relationship was revisited; none was omitted to limit findings. Already-screened observations were not re-emitted.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|

No new apparent issue was excluded in this shard. Reconciled checks appear above and in the inventory, not as exclusion rows. All 53 original exclusion rows were read against route A categories 1–5 and the display-precision rule. None concerns a new qualifying discrepancy in the assigned S198–S222 scope; global exclusion rereading and any global findings remain with the primary pass-2 agent, so no duplicate global exclusion decision is added here.

## Completion

25/25 assigned relationships have PASS_2_COMPLETE; all 25 retain PASS_1_COMPLETE. New findings: 0. New excluded observations: 0. Scientific coverage gaps: none. Limits: per-row test selection and Fisher sidedness/probability ordering/software details are absent; there are no effect intervals or test statistics to check. Preserved source-linked diagnostics establish compatibility without filling these definitions. Updated records: statistics/parts/pass2_06_inventory.md.
