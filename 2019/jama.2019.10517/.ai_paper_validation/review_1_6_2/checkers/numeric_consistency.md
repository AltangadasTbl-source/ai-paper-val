# Main-paper numeric consistency review

Complete assigned scope: DOC-001 REPORT, N001–N079 and Table4 numeric portions S017–S032, all10 PDF pages reviewed through current source-linked map and direct source extractions/rendered displays. Authority: supplied PDF, not derivative conclusions. Full calculations and outcomes are in `relationships/parts/numeric_main.md`. No qualifying F-NUM finding was identified after complete assigned coverage. Relationship totals:79 stable N relationships,16 Table4 cross-references,0 findings,8 excluded observations. No candidate IDs or adjudications assigned.

## Findings

None in this bounded numeric shard. Participant-flow arithmetic, primary counts, all table percentages, safety fractions, Table5 absolute risk differences and effect identities were checked. The supplied adjusted Cox and mixed-model estimates are not crude count ratios or raw mean subtractions.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 REPORT PDF p.5 Table1 hyperlipidemia, N045 | O18/64=28.125% versus29.0%; P19/62=30.6452% versus29.7%. Half-unit input intervals yield[27.1318,29.1339]% and[29.6,31.7073]%, overlapping the printed intervals[28.95,29.05]% and[29.65,29.75]%. Gap0,relative discrepancy0 for both. Even fixed-integer percentage residuals divided by printed value are below.05. No row-specific denominator is imputed. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 REPORT PDF p.5 Table1 placebo living arrangements, N032–N034 | Printed49+10+1=60 versus column n62. Sum half-unit interval[58.5,61.5] and denominator interval[61.5,62.5] touch; gap0. With exact counts2/62=.03226 also below.05. Row percentages individually reconcile with62. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 REPORT PDF p.5 Table1 race, N023–N025 | Olanzapine printed84.4+9.4+6.3=100.1%; individually rounded categories reconcile with54+6+4=64. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 REPORT PDF p.6 Table2 DKEFS color row/footnotes, N057 | Superscript i points to Barnes scale while footnote h explicitly defines both DKEFS measures. Row name and footnote h identify the intended scaled score1–19; no printed value changes. | NOTATION_OR_TYPOGRAPHY |
| DOC-001 REPORT PDF pp.4,6 SAS/AIMS definitions, N017 | SAS0–40 versus explicitly head-dropping-excluded0–36 is different score totals; AIMS item-level0–5 versus overall severity0–4 is different scoring quantities. No matched quantity conflict established. | NOT_REPRODUCED |
| DOC-001 REPORT PDF p.4 UKU adverse-effect definition, N017 | Items stated0–3 and threshold says score3 or4, or2-point increase. Out-of-range4 is a redundant alternative beside attainable3; it does not change the immediately usable threshold or any printed adverse-effect percentage. | CONTEXT_RESOLVES |
| DOC-001 REPORT PDF pp.7–8 NNT, N069 | NNT2.8 attributed to HR; crude inverse RD from13/64 and34/62 is2.89635. Even before count-input rounding, gap from printed[2.75,2.85] is.04635/2.8=.01655≤.05. No stated time-specific survival calculation is contradicted by this difference. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 REPORT PDF pp.7–8 Table4, N075; S017–S032 | Several changes differ from subtraction of marginal baseline/termination means or medians. Footnote explicitly says difference may not equal subtraction because missing data; median of changes also need not equal difference of medians. Printed n permit different observation sets; equal marginal n do not establish paired identity. | CONTEXT_RESOLVES |

## Source evidence and limitations

Exact source authority for all apparent issues: `jama_flint_2019_oi_190079.pdf#page=4`, `#page=5`, `#page=6`, `#page=7`, `#page=8`. Supplied source role is REPORT at every compared location. Source-linked relative links from this shard directory: [Table1](../../../jama_flint_2019_oi_190079.pdf#page=5), [Table2](../../../jama_flint_2019_oi_190079.pdf#page=6), [NNT](../../../jama_flint_2019_oi_190079.pdf#page=7), [Table4](../../../jama_flint_2019_oi_190079.pdf#page=8), [Safety definitions](../../../jama_flint_2019_oi_190079.pdf#page=4). Direct Poppler text and main-mapping CPU images confirmed the printed values; no OCR discrepancy was observed. Limits: paired individual data, exact underlying Cox/survival output and blank Table4 baseline n cells are absent. All assigned relationships are checked; there is no scientific coverage gap.
# Numeric consistency review: support shard

Completed scope: N111–N132 and N211–N236, 48 numeric relationships. DOC-002 PLAN core/appendix; DOC-003 REPORT plot numeric applicability; DOC-004 REPORT applicability. Inventory: `relationships/parts/numeric_support.md`. Two findings and five excluded observations. Primary inferential reproduction remains assigned to the statistical reviewer. No previous candidate/report conclusions, external literature or web sources were used.

### F-NUM-101

Planned acute recruitment size differs inside the plan supporting the randomized target.

- **Locations and roles:** [DOC-002 p.21 section4.2.1 lines995–997](../../../joi190079supp1_prod.pdf#page=21), PLAN; [DOC-002 p.7 section3.9.1/Figure1](../../../joi190079supp1_prod.pdf#page=7), PLAN; [DOC-002 p.8 lines373–381](../../../joi190079supp1_prod.pdf#page=8), PLAN; [DOC-002 p.17 Table4](../../../joi190079supp1_prod.pdf#page=17), PLAN. [DOC-002 p.15 sample-size paragraph](../../../joi190079supp1_prod.pdf#page=15), PLAN, establishes relevance of176RCTtarget.
- **Relationship IDs:** N118,N119,N126,N129,N132.
- **Printed inputs:** p.21 four sites each 82 patients; p.17 each site 98 acutely ill and 44 randomized; p.7 total 392 acute, 196 stabilization, 176 RCT; p.8 conservative 50% remission and approximately 10% stabilization attrition; p.15 176 total / 88 per arm.
- **Rule and calculation:** Equal contributions across the same four sites require one common acute recruitment target.4×82=328 versus4×98=392. Under stated conservative flow,328×.50×.90=147.6 versus392×.50×.90=176.4. The latter supports the printed176target; the former does not.
- **Display precision:** Treat the four-site identity as an exact enumerated structure.82 interval[81.5,82.5] gives four-site total[326,330];98 interval[97.5,98.5] gives[390,394]; total392 interval[391.5,392.5]. Per-site interval gap15; relative discrepancy15/98=.153061. Four-site reconstruction versus392 gap61.5; relative discrepancy61.5/392=.156888. Both exceed.05. The conservative-flow comparison is relevance evidence rather than a separately asserted exact forecast.
- **Focus area:** D, planned sample size/population inputs.
- **Proposed review domain:** `plan_material`.
- **Proposed relationship type / all relationships:** `P_P` / `P_P`.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Planned acute recruitment size underpinning the 176-participant primary relapse-power design; extraction 328 versus 392 changes the available planned randomized pool.
- **Why context does not resolve it:** Both passages describe recruitment for the proposed study at the same four sites. No distinct subset, amended target, or phase-specific explanation accompanies 82. Reading 98 as more plausible does not explain what 82 was intended to represent.
- **Alternatives:** Section 4.2.1 may reflect a different unreconciled recruitment target, or 82 may represent an unlabelled subset; neither explanation is supplied. No inference about an undisclosed amendment is made.
- **Exact human question:** Which acute recruitment target applies—82 or 98 participants per site—and how is the 82-per-site statement reconciled with the 392 acute / 176 randomized sample-size plan?
- **Source authority:** Direct Poppler page text confirmed all numbers; reusable source-matched `review_1_5_1/preprocessing/support_001/visual_p21.png` and `visual_p17.png` were visually opened and confirm82and98/44respectively. Source PDFs remain final authority for mechanical recheck.

### F-NUM-102

The historical35% used for primary relapse-power planning has different printed denominators within the plan.

- **Locations and roles:** [DOC-002 p.4 section3.4 lines175–177](../../../joi190079supp1_prod.pdf#page=4), PLAN; [DOC-002 p.15 section3.10.4 lines725–737 and Table2](../../../joi190079supp1_prod.pdf#page=15), PLAN.
- **Relationship IDs:** N112,N126.
- **Printed inputs:** p.4 says Aronson found approximately 35% of relapses occurred following discontinuation of antipsychotic medication in persons continuing antidepressants. p.15 adopts 35% relapse in the sertraline+placebo group versus 15% continued olanzapine, then says 35% relapse following discontinuation is the same as the rate reported by Aronson. Table 2 uses 35% placebo relapse with 15% olanzapine relapse and 10% attrition to obtain power .84.
- **Rule and calculation:** Let A be relapses after discontinuation,Rall relapses in the described historical population,Dpersons discontinuing. The p.4 printed reading is100A/R≈35%; the power-input reading is100A/D=35%. A/R does not establish A/D withoutR/D. The supplied package does not printA,R,Dor a conversion explaining why these rates can be equated. The20-percentage-pointcontrast35−15andNNT5do reconcile; the issue is the quantity used as the historical input.
- **Display precision:** Both displayed percentages have nominal intervals[34.5%,35.5%]; their numerical gap iszero. This is a denominator/quantity-identity conflict, not a reproduced numeric difference between copies of the same quantity, so a relative discrepancy is not computable without historical denominators. Rounding cannot convert a share of relapses into a participant relapse risk. No numeric threshold is asserted for an unavailable conversion.
- **Focus area:** D, sample-size/power assumption; C, identity of the quantity underlying the stated assumption.
- **Proposed review domain:** `plan_material`.
- **Proposed relationship type / all relationships:** `P_P` / `P_P`.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** The 35% placebo participant-relapse assumption supporting the stated .84 power for the 176-participant primary relapse design and the historical justification extracted for that assumption.
- **Why context does not resolve it:** The power paragraph explicitly identifies the historical rate as the same quantity, while the earlier description conditions the 35% on relapses. These denominators correspond to different risks; neither location supplies counts or a clarifying definition. This historical comparison is directly tied to a primary power input, rather than peripheral background alone.
- **Alternatives:** The p.4 wording may have intended a relapse risk among discontinuers; alternatively35%may have been deliberately chosen independently for power despite a differently defined historical proportion. The supplied text does not identify either interpretation. No external historical study was consulted.
- **Exact human question:** Does the cited 35% mean relapse risk among persons discontinuing antipsychotic medication, or the proportion of relapses occurring after discontinuation, and what supplied denominator or clarification supports using it as the 35% placebo relapse input?
- **Source authority:** Both exact PDF pages were read by direct Poppler layout extraction. The registered observation rests on their explicit wording and denominator definitions; final visual page recheck remains required.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-002 p.6, N114 | Historical longitudinal remission OR 1.28 differs from crude ratio 41.9/23.9; the text assigns OR to remission over the trial and percentages to last assessment. | MODEL_VERSUS_CRUDE |
| DOC-002 Table 5 p.29, N225 | Week 6 percentages imply integer completion totals 194 by race and 193 by ethnicity. With exact participant denominators and percentage half-unit intervals, reconstruction gives race [193.9455,194.2045], ethnicity [192.8725,193.1315], gap .8140/194.075≈.00419; even integer 1/194≈.00515≤.05. Allowing half-unit count intervals only widens these ranges. Week 12 partitions both imply 142. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-002 pp.39–40, N230/N232 | General minimum olanzapine 5 mg versus EPSE-specific reduction minimum 10 mg concerns distinct permitted maneuvers; general 5 mg minimum is explicitly retained for intolerance/stabilization. | CONTEXT_RESOLVES |
| DOC-002 pp.7,41, N118/N234 | Standard maximum 20 weeks pre-RCT versus possible 22 weeks with two additional stabilization visits: the extension is explicitly conditional and approved on p.7, qualifying ordinary 8-week stabilization. | CONTEXT_RESOLVES |
| DOC-002 p.21, N132 | Map/layout transcription >2 DAS and >21 HAM-D differs from source-matched visual ≥2 and ≥21. This apparent source inconsistency is derivative-only; source glyphs take precedence. | NOT_REPRODUCED |

## Durable source-glyph correction and limitations

At package-relative `.ai_paper_validation/review_1_5_1/preprocessing/support_001/visual_p21.png`, visually inspected line1014 prints **≥2** for DAS conviction and line1017 prints **≥21** for HAM-D. At numeric-checker handoff, direct native/layout text and the pre-correction core map transcribed **>2/>21**. Use the visually confirmed source reading for eligibility comparisons. No mapper file was edited by this shard. Coordinator subsequently annotated the map with ≥2/≥21; the literal extracted and reused text remains preserved.

No assigned numeric gap remains. Historical data are distinguished from current-trial results. DOC-003 lacks exact numeric plot labels, event counts, denominators and crude-effect definitions, so no precision arithmetic is inferred from pixels. DOC-004 supplies no applicable quantitative relationship. Full primary inferential and simulation reproduction is statistical-owned. No source/reused asset was changed.
