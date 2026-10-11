# Statistical relationship inventory — pass 1 support A

Status: PASS_1_COMPLETE. Fresh statistical reviewer: /root/statistics_one_a, fixed model gpt-6.1-sol, high effort. Agent ID recorded in the coordinator manifest: root/statistics_one_a.

Exact disjoint scope: DOC-004 REPORT eTable 1 score definitions PDF p. 2; eTables 2–5 pp. 3–15, including continuation/model footnotes and the p. 10 score-specific sample footnote; eFigures 1–2 pp. 25–26. DOC-001 REPORT Methods p. 4, Table 2 p. 5, related narrative pp. 5–8 are matched comparators/context, not a second ownership of the main-paper statistical relationships. No plan-design or eTables 6–9/eFigure 3 relationships are assigned here.

81 stable S IDs, S201–S281: 61 variable/population families with 122 separate 6-/12-month change comparisons, four score-definition families, five common method/context families, four eFigure 1 panels retaining all three visits, seven eFigure 2 proportion comparisons. Every table family preserves its baseline, both arms' change estimates and confidence intervals, between-group estimate/interval/P, exact unit/population/time and footnotes in the complete evidence appendix below. The compact table does not substitute for that transcription. Every family was read and checked at both visits; no time-cell sampling occurred.

## Evidence and check rules

Sources and pre-existing assets are preserved. Reused native layout and complete fresh semantic mapping are the locators. Retained source-matched pp. 25/26 renders were inspected in full. Native/layout transcription of main pp. 4–6 was locally regenerated with direct CPU Poppler pdftotext 26.01.0, command `pdftotext -layout -f 4 -l 6 jama_saynorea_2019_oi_190106_1635377898.43062.pdf .ai_paper_validation/review_1_6_1/preprocessing/st1-a-main-methods-p4-6.txt`. It supplies exact immediate narrative/method context. No new OCR, custom Python, GPU, web, or earlier scientific conclusions were used.

For every table family: check both arm point estimates and between-arm estimate lie within their own printed 95% CI, lower endpoint does not exceed upper endpoint, signs and I-minus-C direction reconcile with the row, and significance versus CI exclusion of zero is compatible after allowing every displayed input its half-unit rounding interval. These checks found no non-reconciling table cell in this assigned scope. A displayed SD/IQR is not treated as a standard error/CI. Difference estimates are modeled, not recomputed as crude exact subtractions. Main p. 4 establishes mixed-effects linear models, site/participant/family random intercepts, two-sided tests, P<.05, exploratory secondary analyses and no additional adjustment. Exact degrees of freedom, coefficient covariance, variance estimator, test statistic and standard errors are absent; no convention supplies them. Therefore numerical inversion of rounded CI to a unique P is unavailable and is not a finding. Rounded endpoint zero may represent a small nonzero endpoint. No NI/equivalence margin or stopping conclusion applies to these dietary displays.

In the table below, each eTable 2 family is MI, N=3272 I/3311 C; each eTable 3–5 family is completers, n=2862 I/2883 C at 6 mo and n=2833 I/2943 C at 12 mo, except the explicit er-MedDiet asterisk n=3030 I/3090 C at 6 mo and n=2971 I/3095 C at 12 mo. Food units are g/week. eTable 5 units are individually retained. Between columns use `estimate [lower,upper]; P`; the evidence appendix preserves every corresponding arm estimate/CI and baseline value. `Contained; ordered; direction compatible` applies to all three estimates at each of both time points.

## Table variable/population families

| S ID | REPORT exact location and variable | 6-month between-group estimate [95% CI]; P | 12-month between-group estimate [95% CI]; P | Pass 1 result |
|---|---|---|---|---|
| S201 | eTable 2 p.3 olive oil | -4 [-11,2]; .20 | -8 [-15,-2]; .02 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S202 | eTable 2 p.3 refined olive oil | -3 [-8,1]; .17 | 0 [-5,5]; .93 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S203 | eTable 2 p.3 extra-virgin olive oil | -1 [-9,6]; .71 | -8 [-16,-1]; .04 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S204 | eTable 2 p.3 nuts | 49 [41,57]; <.001 | 35 [27,43]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S205 | eTable 2 p.3 fruits | 186 [107,265]; <.001 | 197 [118,276]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S206 | eTable 2 p.3 vegetables | 188 [135,241]; <.001 | 210 [157,263]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S207 | eTable 2 p.3 cereals | -89 [-119,-60]; <.001 | -106 [-135,-77]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S208 | eTable 2 p.3 whole grains | 213 [186,240]; <.001 | 169 [142,196]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S209 | eTable 2 p.4 refined grains | -346 [-378,-314]; <.001 | -309 [-340,-277]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible; main p.6 matched |
| S210 | eTable 2 p.5 legumes | 20 [15,25]; <.001 | 21 [16,26]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S211 | eTable 2 p.5 fish | 59 [42,77]; <.001 | 75 [58,93]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S212 | eTable 2 p.5 meat | -31 [-50,-11]; .002 | -9 [-28,10]; .37 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S213 | eTable 2 p.5 red meat | -48 [-59,-36]; <.001 | -39 [-51,-28]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible; main p.6 matched |
| S214 | eTable 2 p.5 processed meat | -18 [-26,-10]; <.001 | -11 [-19,-3]; .007 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S215 | eTable 2 p.5 pastries | -60 [-69,-50]; <.001 | -49 [-59,-39]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible; main p.6 matched |
| S216 | eTable 2 p.5 dairy | 153 [84,222]; <.001 | 149 [80,218]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S217 | eTable 2 p.5 total yogurt | 110 [80,140]; <.001 | 92 [62,122]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S218 | eTable 2 p.6 fermented dairy | 102 [71,134]; <.001 | 87 [56,119]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S219 | eTable 2 p.7 low-fat dairy | 258 [193,323]; <.001 | 271 [206,336]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S220 | eTable 2 p.7 whole-fat dairy | -63 [-95,-32]; <.001 | -59 [-91,-27]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S221 | eTable 2 p.7 total alcohol | -7 [-11,-3]; .001 | -8 [-12,-3]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S222 | eTable 2 p.7 red wine | -1 [-4,1]; .36 | -1 [-4,1]; .37 | PASS_1_COMPLETE; change CIs contained/ordered; baseline median33 [IQR0,29] preserved; descriptive comparison excluded |
| S223 | eTable 3 pp.9–10 er-MedDiet | 2.3 [2.2,2.5]; <.001 | 2.3 [2.1,2.4]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible; asterisk sample applies |
| S224 | eTable 3 p.9 MDS | 0.5 [0.4,0.6]; <.001 | 0.5 [0.4,0.6]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible; C change negative at both visits |
| S225 | eTable 3 p.9 MEDAS | 1.1 [1.0,1.3]; <.001 | 1.1 [1.0,1.2]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S226 | eTable 3 p.9 PDQS | 2.4 [2.2,2.6]; <.001 | 2.3 [2.1,2.5]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S227 | eTable 4 p.10 total olive oil | -3 [-10,3]; .34 | -8 [-15,-1]; .02 | PASS_1_COMPLETE; contained, ordered, direction compatible; baseline label resolved by values/footnote |
| S228 | eTable 4 p.10 refined olive oil | -3 [-8,3]; .32 | 0 [-6,5]; .95 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S229 | eTable 4 p.10 extra virgin olive oil | 0 [-8,7]; .90 | -8 [-16,0]; .05 | PASS_1_COMPLETE; contained, ordered, direction compatible; zero endpoint/P boundary allow rounding |
| S230 | eTable 4 p.10 nuts | 50 [42,57]; <.001 | 35 [27,43]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible; line-wrapped P read as <.001 |
| S231 | eTable 4 p.10 fruits | 184 [104,265]; <.001 | 192 [113,270]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S232 | eTable 4 p.10 vegetables | 193 [139,247]; <.001 | 209 [155,263]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S233 | eTable 4 pp.10–11 cereals | -92 [-122,-61]; <.001 | -106 [-136,-75]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S234 | eTable 4 p.11 whole grains | 215 [188,242]; <.001 | 170 [143,197]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S235 | eTable 4 p.11 refined grains | -346 [-380,-311]; <.001 | -311 [-346,-277]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S236 | eTable 4 p.11 legumes | 20 [16,25]; <.001 | 21 [16,25]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S237 | eTable 4 p.11 fish | 60 [43,78]; <.001 | 73 [55,91]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S238 | eTable 4 p.11 meat | -29 [-48,-10]; .003 | -11 [-31,9]; .27 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S239 | eTable 4 p.11 red meat | -47 [-59,-35]; <.001 | -40 [-53,-28]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S240 | eTable 4 pp.11–12 processed meat | -18 [-26,-9]; <.001 | -11 [-20,-3]; .01 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S241 | eTable 4 p.12 pastries | -59 [-70,-49]; <.001 | -49 [-60,-39]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S242 | eTable 4 p.12 dairy | 159 [89,230]; <.001 | 148 [78,218]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S243 | eTable 4 p.12 total yogurt | 113 [83,143]; <.001 | 91 [61,121]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S244 | eTable 4 p.12 fermented dairy | 105 [74,137]; <.001 | 86 [55,118]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S245 | eTable 4 p.12 low-fat dairy | 265 [199,331]; <.001 | 271 [206,337]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S246 | eTable 4 p.12 whole-fat dairy | -61 [-95,-27]; .001 | -59 [-94,-25]; .001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S247 | eTable 4 pp.12–13 total alcohol | -7 [-11,-3]; <.001 | -8 [-12,-3]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S248 | eTable 4 p.13 red wine | -1 [-4,2]; .38 | -1 [-4,2]; .40 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S249 | eTable 5 p.14 energy kcal/d | -95 [-122,-68]; <.001 | -103 [-130,-75]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S250 | eTable 5 p.14 protein %E | 1.0 [0.9,1.2]; <.001 | 1.1 [1.0,1.2]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S251 | eTable 5 p.14 carbohydrate %E | -1.5 [-1.9,-1.2]; <.001 | -1.4 [-1.8,-1.1]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S252 | eTable 5 p.14 total fat %E | 0.7 [0.3,1.0]; <.001 | 0.5 [0.2,0.9]; .004 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S253 | eTable 5 p.14 SFA %E | -0.4 [-0.6,-0.3]; <.001 | -0.4 [-0.5,-0.3]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S254 | eTable 5 p.14 MUFA %E | 1.2 [0.9,1.4]; <.001 | 0.9 [0.6,1.2]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S255 | eTable 5 p.15 MUFA:SFA ratio | 0.3 [0.2,0.3]; <.001 | 0.2 [0.2,0.2]; <.001 | PASS_1_COMPLETE; contained/ordered, direction compatible; interval collapse is precision |
| S256 | eTable 5 p.15 PUFA %E | 0.5 [0.4,0.6]; <.001 | 0.4 [0.3,0.5]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S257 | eTable 5 p.15 alcohol %E | -0.2 [-0.4,0]; .02 | -0.3 [-0.4,-0.1]; .01 | PASS_1_COMPLETE; contained/ordered, direction compatible; rounded zero allows excluded zero |
| S258 | eTable 5 p.15 fiber g/week | 24 [20,27]; <.001 | 19 [16,22]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S259 | eTable 5 p.15 long-chain omega-3 g/week | 0.7 [0.5,0.8]; <.001 | 0.7 [0.5,0.9]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S260 | eTable 5 p.15 cholesterol mg/week | -53 [-93,-13]; .009 | -12 [-52,29]; .58 | PASS_1_COMPLETE; contained, ordered, direction compatible |
| S261 | eTable 5 p.15 sodium g/week | -1.2 [-1.5,-0.9]; <.001 | -1.3 [-1.7,-1.0]; <.001 | PASS_1_COMPLETE; contained, ordered, direction compatible |

## Definition and method families

| S ID | Exact REPORT location | Source-grounded relationship, check and limitations | Pass 1 |
|---|---|---|---|
| S262 | DOC-004 p.2 eTable1 er-MedDiet; DOC-001 pp.3–5 | 17-item 0–17 scale, higher adherence; nine positive components, seven negative components and alcohol condition, maximum17. All explicit serving/day/week thresholds and sex-specific alcohol conditions retained in appendix. No internal score-range contradiction. | PASS_1_COMPLETE |
| S263 | DOC-004 p.2 eTable1 MDS; DOC-001 p.5 | Six positive components >=sex-specific median, two negative components <=sex-specific median plus alcohol condition;0–9. Women5–25g/d,men10–50g/d. Score maximum agrees with components; higher better. | PASS_1_COMPLETE |
| S264 | DOC-004 p.2 eTable1 MEDAS; DOC-001 p.5 | Nine positive components, four negative plus wine >=7glasses/week;0–14. Compare its own serving/day thresholds, not er-MedDiet weekly thresholds. Internally coherent definition. | PASS_1_COMPLETE |
| S265 | DOC-004 p.2 eTable1 PDQS; DOC-001 p.5 | 13 positive and eight negative components each0/1/2points;21x2=42. Positive0–1/2–3/>=4servings/week scores0/1/2, negative reversed. No range contradiction; unreported handling of fractional serving-frequency boundaries not inferred. | PASS_1_COMPLETE |
| S266 | DOC-004 pp.4,6,7,9,11–15 footnotes; DOC-001 p.4 Methods | Changes are means95%CI from mixed-effect models accounting for site and couples random effects; main explicitly adds participant random intercept. Abbreviated footnote does not contradict full model. Couples are household allocation units; repeated-measures/random effects description coherent. No preferred model proposed. | PASS_1_COMPLETE |
| S267 | DOC-004 eTable2 pp.3–7 and eTables3–5 pp.9–15; DOC-001 pp.3–5 | MI population3272/3311 versus named completer sensitivities; time counts and score-specific asterisk preserved. er-MedDiet6mo6120=6583-463 and12mo6066=6583-517; other scores6mo5745=6583-838 and12mo5776=6583-807. No denominator imputed into figures. Main MI8 imputations/predictors recorded; detailed plan comparison belongs to main/plan shard. | PASS_1_COMPLETE |
| S268 | DOC-001 p.4 Statistical Analysis; DOC-004 pp.4,6,7,9,11–15 | Two-sided, nominal95%CI, P<.05, exploratory secondaries without additional adjustment. No test statistics,SE,DF,covariance/variance estimator printed for these results. Significance-direction compatibility checked with precision; exact P reproduction cannot use inferred model/test parameters. No superiority/NI/equivalence/multiplicity/interim stopping conclusion beyond these reported rules. | PASS_1_COMPLETE |
| S269 | DOC-004 p.9 eTable3 MCID text; DOC-001 p.5 Table2 | MDS log(.75)=-.2877; exp(-.2877/2)=.8660, rounded.87;1-.8660=.1340, rounded13%. MEDAS historical HR.90[.85,.96] and.94[.89,.99] contain points and ordered endpoints; source gives10%/6% reductions. er-MedDiet/MDS/MEDAS1point and PDQS likely2points are rationales, not NI/equivalence margins. No current-trial clinical-event effect inferred. | PASS_1_COMPLETE |
| S270 | DOC-004 pp.25–26 eFigure captions; DOC-001 pp.4,6,8 | eFigure1 P values compare group means; eFigure2 P values compare proportions. No exact figure population, numerator, denominator, proportion-CI method, or test identity printed. Main p.4 supplies general two-sided convention but does not justify choosing independent-binomial test. Main p.6 explicitly includes eFigure1 among post hoc sensitivities; graphic means compatible with eTable3 completers rather than main MI values. Main p.8 says favorable change more frequent I for most comparisons. | PASS_1_COMPLETE |

## Complete figure families

All geometry below is approximate visual source reading, not an exact printed estimate or digitized replacement for a table cell. Numeric annotations are printed values. Entire CI marks, axes, color legend and captions inspected. Point containment in unlabeled intervals cannot be numerically inverted. Three additional common figure relationships are S266/S268/S270 (model, nominal rule and comparison/population mapping), so all 14 assigned figure-comparison/common-model families are covered.

| S ID | REPORT exact location | Complete series and comparison; check outcome | Pass 1 |
|---|---|---|---|
| S271 | DOC-004 p.25 eFigure1 er-MedDiet upper-left | Range0–17, axis0,3,6,9,12,15,18; I purple/C gray at baseline,6,12mo. Six means/95%CI marks retained: approximately I8.5/12.5/12.7, C8.6/10.3/10.6. P baseline.13,6mo<.001,12mo<.001. Higher better; I increases more. Main MI mean differences versus graphic follow-up heights resolved by main p.6 sensitivity context/eTable3, no exact geometry asserted. | PASS_1_COMPLETE |
| S272 | DOC-004 p.25 eFigure1 MEDAS upper-right | Range0–14, axis0,3,6,9,12; six mean/95%CI marks: approximately I7.6/10/10.2,C7.6/9/9.1. BaselineP.42,6mo<.001,12mo<.001. Both improve, I more; source-sensitive mapping as S270. | PASS_1_COMPLETE |
| S273 | DOC-004 p.25 eFigure1 MDS lower-left | Range0–9, axis0,2,4,6,8; six mean/95%CI marks: approximately I4.3/4.5/4.5,C4.3/4/4. BaselineP.98,6mo<.001,12mo<.001. I rises,C falls, same directions as completer eTable3 (I+.2/C-.3 at both visits). Do not equate with main MI increases. | PASS_1_COMPLETE |
| S274 | DOC-004 p.25 eFigure1 PDQS lower-right | Range0–42, axis0,10,20,30,40; six mean/95%CI marks: approximately I21/25.5/25.5,C21/23/23. BaselineP.76,6mo<.001,12mo<.001. Both rise,I more; sensitivity context resolves MI-versus-figure values. | PASS_1_COMPLETE |
| S275 | DOC-004 p.26 eFigure2 decreased fat12mo | I purple label34%,C gray32%,P.14; plotted heights approximately I32%,C34%,CI marks near heights. First-six opposite label positions form one immediately resolvable pattern; labels match opposite heights. Exact denominator/test/CI limits absent. | PASS_1_COMPLETE |
| S276 | DOC-004 p.26 eFigure2 increased MUFA12mo | I label72%,C77%,P<.001; heights approximately I77%,C72%,allCI marks inspected. Same reversed placement pattern as S275. | PASS_1_COMPLETE |
| S277 | DOC-004 p.26 eFigure2 increased MUFA:SFA12mo | I label79%,C86%,P<.001; heights approximately I86%,C79%,allCI marks inspected. Same reversed placement pattern. | PASS_1_COMPLETE |
| S278 | DOC-004 p.26 eFigure2 increased fruit12mo | I label58%,C63%,P<.001; heights approximately I63%,C58%,allCI marks inspected. Same reversed placement pattern. | PASS_1_COMPLETE |
| S279 | DOC-004 p.26 eFigure2 increased vegetables12mo | I label56%,C64%,P<.001; heights approximately I64%,C56%,allCI marks inspected. Same reversed placement pattern. | PASS_1_COMPLETE |
| S280 | DOC-004 p.26 eFigure2 decreased meat12mo | I label60%,C62%,P.08; heights approximately I62%,C60%,allCI marks inspected. Same reversed placement pattern. | PASS_1_COMPLETE |
| S281 | DOC-004 p.26 eFigure2 decreased sugary dessert12mo | I label59%,C58%,P<.001; heights/CI centers approximately I68%,C60%. Neither original placement nor swapped labels reconcile intervention geometry: 59% or58% remains below60% axis level while intervention CI lies above60%. Exploratory secondary display; no established primary/key-secondary/population/rule exception. Excluded PERIPHERAL_COMPARISON; no P reproduction from assumed counts/test. | PASS_1_COMPLETE |

## Complete source-linked evidence appendix

The following complete transcription is preserved without normalizing printed values. Each S201–S265 family points to its exact named variable and both visit rows here. pp.1/8 are context-only cover/copyright; evidence for eTables6–9 and eFigure3 appears in the cover enumeration only and is assigned to the other shard. Links are relative to this part's directory and require one-level adjustment if merged into the canonical statistics directory.

### DOC-004 PDF p. 1 — REPORT

[Results source p. 1](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=1>)

```text
                                              Supplementary Online Content

Sayón-Orea C, Razquin C, Bulló M, et al. Effect of a nutritional and behavioral intervention on energy-reduced Mediterranean diet
adherence among patients with metabolic syndrome [published October 15, 2019]. JAMA. doi:10.1001/jama.2019.14630

Supplement 3. eTable 1. Definitions of scores capturing the four dietary patterns.
eTable 2. Baseline dietary variables and their changes by randomized treatment group: Foods and foods groups.
eTable 3. Sensitivity analysis. Baseline, 6-month and 12-month changes in quality dietary scores by randomized treatment group:
completers only.
eTable 4. Sensitivity analysis. Baseline, 6-month and 12-month changes in food items by randomized treatment group: completers
only.
eTable 5. Sensitivity analysis. Baseline values, 6-month and 12-month changes in nutrient intake by randomized treatment group:
completers only
eTable 6. Sensitivity analysis. Baseline and 6- and 12- month changes in quality dietary scores by randomized treatment group: All
randomized participants. Replacing all missing values with baseline value.
eTable 7. Sensitivity analysis. Baseline values, 6-month and 12- month changes in food items by randomized treatment group: all
randomized participants. Replacing all missing values with baseline value
eTable 8. Sensitivity analysis. Baseline values, 6-month and 12-month changes in nutrient intake by randomized treatment group:
all randomized participants. Replacing all missing values with baseline value.
eTable 9. Baseline and 12- month change (95% confidence intervals) in risk factors, by treatment group: all randomized 245
participants (multiple imputation [MI]) and completers only.
eFigure 1. Mean values (95% CI) of scores capturing the 4 quality dietary patterns at baseline, at 6 months and at 12 months
according to the randomized treatment group.
eFigure 2. Percentage of participants complying with the intended dietary changes by randomized treatment group
eFigure 3 Changes in nutritional variables (expressed in common units of baseline standard deviations) after 6 and 12 months in
the control and in the intervention group.

This supplementary material has been provided by the authors to give readers additional information about their work.




                                      © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 2 — REPORT

[Results source p. 2](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=2>)

```text
Supplemental eTable 1. Definitions of scores capturing the four dietary patterns.

                         17-item Energy-reduced Mediterranean Diet              Mediterranean           Mediterranean Diet Adherence            Prime Diet Quality Score
                         (er-MedDiet, 0-17 points)                              Diet Score (MDS,        Screener (MEDAS, 0-14 points)           (PDQS, 0-42 points)
                                                                                0 to 9 points),
                                                                                Trichopoulou
 Positively weighted     Olive oil as main culinary fat                         MUFA:SFAa               Olive oil as main culinary fat          Dark leafy green vegetablesc
 components              ≥ 2 servings/d vegetables                              Vegetablesa             ≥ 4 tbs/d olive oil                     Cruciferous vegetablesc
                         ≥ 3 servings/d fruits                                  Fruits and nutsa        ≥ 2 servings/d vegetables               Carrotsc
                         ≥ 3 servings/wk legumes                                Legumesa                ≥ 3 servings/d fruits                   Other vegetablesc
                         ≥ 3 servings/wk fish                                   Fish a                  ≥ 3 servings/wk legumes                 Whole citrus fruitsc
                         ≥ 3 servings/wk nuts                                   Cerealsa                ≥ 3 servings/wk fish                    Other whole fruitsc
                         Preference of poultry (chicken, turkey, or rabbit)                             ≥ 3 servings/wk nuts                    Legumesc
                           over red meats (beef, pork, lamb, hamburgers,                                Preference of poultry (chicken,         Nutsc
                           or sausages)                                                                 turkey, or rabbit) > red meats (beef,   Poultryc
                                                                                                                                                Fishc
                         ≥ 2 servings/wk olive oil sauce with tomato,                                   pork, hamburgers, or sausages)
                                                                                                                                                Eggsc
                           garlic, onion, or leek (sofrito)                                             ≥ 2 servings/wk olive oil sauce
                                                                                                                                                Whole grainsc
                         ≥5 servings/wk of whole grain cereals                                          with tomato, garlic, onion, or leek
                                                                                                                                                Liquid vegetable oilsc
                                                                                                        (sofrito)
 Negatively weighted       <1 servings/wk red or processed meats               Meat and meat                                              Red meatd
                                                                                                        <1 serving/d red or processed meats
                                                                                       b
 components                <1 servings/wk butter or margarine or cream         products                                                   Potatoesd
                                                                                                        <1 serving/d butter or margarine or
                                                                                             b
                           <1 servings/wk carbonated sugar-sweetened           Dairy products      cream                                  Processed meatd
                           beverages                                                               <1 serving/d carbonated sugar-         Whole fat dairyd
                           <3 servings/wk commercial bakery, cakes,                                sweetened beverages                    Refined grains & baked goodsd
                           biscuits, or pastries                                                   <2 servings/wk commercial bakery,      Sugar sweetened beveragesd
                           Avoidance of any added sugar to beverages                               cakes, biscuits, or pastries           Fried foods obtained away
                           ≤ 1 serving/d of white bread                                                                                   from homed
                           < 3 servings/wk of refined grain, pasta or white                                                               Sugary desserts and ice creamd
                           rice
  Alcohol                   2-3 glasses/d for men                              5-25 g/d (women)     ≥7 glasses/wk of wine
                            1-2 glasses/d for women                            10-50 g/d (men)
a
  One point if the consumption was ≥ the sex specific median
b
  One point if the consumption was ≤ the sex specific median
c
  0 points if the consumption was between 0–1 serving/wk; 1 point if the consumption was between 2–3 servings/wk and 2 points if the consumption was ≥4 servings/week.
d
  0 points if the consumption was ≥4 servings/week; 1 point if the consumption was between 2–3 servings/wk and 2 points if the consumption was between 0–1 serving/week.




                                                            © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 3 — REPORT

[Results source p. 3](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=3>)

```text
Supplemental eTable 2. Baseline dietary variables and their changes by
randomized treatment group: Foods and foods groups.

                                    MULTIPLE IMPUTATION: ALL RANDOMIZED
                                                PARTICIPANTS
 Food and food groups           Intervention group            Intervention                  Between-group
                                                                 group                        difference
                                      N=3,272                   N=3,311                                  p value
 Olive oil (g/week)
  Baseline, median (IQR)           350 (175, 350)            350 (175, 350)
  6-month change                    28 (23 to 33)             32 (28 to 37)             -4 (-11 to 2)     0.20
  12-month change                   36 (31 to 41)             44 (39 to 49)             -8 (-15 to -2)    0.02
 Refined olive oil (g/week)
  Baseline, median (IQR)              0 (0, 70)                 0 (0, 70)
  6-month change                   -38 (-41 to -34)         -34 (-38 to -31)             -3 (-8 to 1)     0.17
  12-month change                  -39 (-42 to -35)         -39 (-42 to -35)             0 (-5 to 5)      0.93
 Extra-virgin olive oil
 (g/week)
   Baseline, median (IQR)           175 (70, 350)            175 (70, 350)
  6-month change                    65 (59 to 70)             66 (61 to 71)              -1 (-9 to 6)     0.71
  12-month change                   75 (69 to 80)             83 (77 to 88)             -8 (-16 to -1)    0.04
 Nuts (g/week)
  Baseline, median (IQR)            60 (28, 165)              60 (14, 165)
  6-month change                  120 (114 to 126)            72 (66 to 77)             49 (41 to 57)    <0.001
  12-month change                 117 (111 to 123)            82 (76 to 87)             35 (27 to 43)    <0.001
 Fruits (g/week)
  Baseline, median (IQR)        2,287 (1,523, 3,200)      2,287 (1,494,
                                                          3,281)
  6-month change                  344 (287 to 401)         158 (104 to 213)             186 (107 to      <0.001
                                                                                           265)
  12-month change                 430 (370 to 491)          233 (177 to 289)            197 (118 to      <0.001
                                                                                           276)
 Vegetables (g/week)
  Baseline, median (IQR)        2,168 (1,621, 2,814)      2,130 (1,596,
                                                          2,863)
  6-month change                  330 (292 to 368)         142 (106 to 178)             188 (135 to      <0.001
                                                                                           241)
  12-month change                 347 (306 to 389)          137 (100 to 175)            210 (157 to      <0.001
                                                                                           263)
 Cereals (g/week)
  Baseline, median (IQR)          877 (627, 1432)           870 (645, 1432)
  6-month change                 -165 (-186 to -143)        -75 (-95 to -55)         -89 (-119 to -      <0.001
                                                                                          60)
  12-month change                -205 (-227 to -183)        -99 (-120 to -79)       -106 (-135 to -      <0.001
                                                                                          77)
 Whole grains (g/week)
  Baseline, median (IQR)            109 (0, 525)               98 (0, 525)
  6-month change                  274 (254 to 293)            61 (42 to 79)             213 (186 to      <0.001
                                                                                           240)
  12-month change                 228 (207 to 248)            59 (40 to 78)             169 (142 to      <0.001
                                                                                           196)




                            © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 4 — REPORT

[Results source p. 4](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=4>)

```text
 Refined grains (g/week)
   Baseline, median (IQR)         779 (425, 1475)           779 (412, 1474)
   6-month change                -538 (-562 to -515)      -192 (-214 to -170)       -346 (-378 to -   <0.001
                                                                                         314)
   12-month change               -535 (-559 to -510)      -226 (-249 to -203)       -309 (-340 to -   <0.001
                                                                                         277)

IQR, Interquartile range, Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                            © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 5 — REPORT

[Results source p. 5](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=5>)

```text
Supplemental eTable 2 (cont). Baseline dietary variables and their changes by
randomized treatment group. Foods and food groups.

                                MULTIPLE IMPUTATION: ALL RANDOMIZED
                                            PARTICIPANTS
 Food and food groups          Intervention           Control group           Between-group difference
                                  group
                                 N=3,272                  N=3,311                               p value
 Legumes (g/week)
   Baseline, median            120 (88, 180)           120 (88, 176)
 (IQR)
   6-month change              37 (34 to 41)            17 (14 to 21)         20 (15 to 25)     <0.001
  12-month change              39 (36 to 43)            18 (15 to 22)         21 (16 to 26)     <0.001
 Fish (g/week)
   Baseline, median           673 (472, 918)           682 (475, 918)
 (IQR)
   6-month change             101 (88 to 114)           41 (29 to 53)         59 (42 to 77)     <0.001
  12-month change             105 (91 to 119)           29 (17 to 42)         75 (58 to 93)     <0.001
 Meat (g/week)
   Baseline, median          993 (760, 1263)          994 (776, 1271)
 (IQR)
   6-month change           -109 (-123 to -95)        -78 (-92 to -65)       -31 (-50 to -11)   0.002
  12-month change           -116 (-130 to -101)      -107 (-120 to -93)       -9 (-28 to 10)     0.37
 Red meat (g/week)
   Baseline, median           290 (150, 497)           300 (150, 520)
 (IQR)
   6-month change           -115 (-123 to -106)       -67 (-75 to -59)       -48 (-59 to -36)   <0.001
  12-month change           -120 (-129 to -111)       -81 (-89 to -72)       -39 (-51 to -28)   <0.001
 Processed meat
 (g/week)
   Baseline, median           227 (143, 317)           227 (143, 322)
 (IQR)
   6-month change             -63 (-68 to -57)        -45 (-50 to -39)       -18 (-26 to -10)   <0.001
  12-month change             -63 (-69 to -57)        -52 (-57 to -46)        -11 (-19 to -3)   0.007
 Pastries (g/week)
   Baseline, median            121 (42, 275)           114 (42, 261)
 (IQR)
   6-month change           -109 (-116 to -102)       -49 (-56 to -42)       -60 (-69 to -50)   <0.001
  12-month change           -109 (-116 to -102)       -60 (-67 to -53)       -49 (-59 to -39)   <0.001
 Dairy (g/week)
   Baseline, median         2100 (1532, 2959)        2200 (1548, 3597)
 (IQR)
   6-month change              16 (-34 to 66)        -137 (-184 to -90)      153 (84 to 222)    <0.001
  12-month change             -41 (-95 to 12)          -190 (-239 to -       149 (80 to 218)    <0.001
                                                            141)
 Total yogurt (g/week)
   Baseline, median            375 (58, 875)           375 (58, 875)
 (IQR)
   6-month change             119 (97 to 141)           9 (-11 to 30)        110 (80 to 140)    <0.001
  12-month change             88 (64 to 111)            -4 (-25 to 17)        92 (62 to 122)    <0.001




                         © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 6 — REPORT

[Results source p. 6](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=6>)

```text
 Fermented dairy
 (g/week)
   Baseline, median           550 (300, 975)          575 (300, 1025)
 (IQR)
   6-month change             97 (74 to 120)            -5 (-27 to 16)       102 (71 to 134)   <0.001
   12-month change             72 (47 to 96)            -16 (-38 to 7)        87 (56 to 119)   <0.001

IQR, Interquartile range. Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                         © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 7 — REPORT

[Results source p. 7](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=7>)

```text
Supplemental eTable 2 (cont). Baseline dietary variables and their changes by
randomized treatment group. Foods and food groups.

                                 MULTIPLE IMPUTATION: ALL RANDOMIZED
                                             PARTICIPANTS
 Food and food groups      Intervention             Control group             Between-group difference
                           group
                                N=3,272                  N=3,311                               p value
 Low-fat dairy (g/week)
   Baseline, median           658 (0, 1,775)          687 (0, 1,775)
 (IQR)
   6-month change            326 (279 to 373)         68 (23 to 113)       258 (193 to 323)      <0.001
   12-month change           267 (217 to 318)          -4 (-50 to 42)      271 (206 to 336)      <0.001
 Whole-fat dairy
 (g/week)
   Baseline, median              0 (0, 375)              0 (0, 375)
 (IQR)
   6-month change           -174 (-196 to -151)     -110 (-132 to -88)      -63 (-95 to -32)     <0.001
   12-month change          -160 (-184 to -135)     -101 (-123 to -78)      -59 (-91 to -27)     <0.001
 Total alcohol intake
 (g/week)
   Baseline, median              32 (5, 98)             36 (5, 103)
 (IQR)
   6-month change             -13 (-16 to -10)          -6 (-9 to -3)         -7 (-11 to -3)      0.001
   12-month change            -12 (-15 to -9)           -4 (-7 to -1)         -8 (-12 to -3)     <0.001
 Red wine (g/week)
   Baseline, median              33 (0, 29)              4 (0, 29)
 (IQR)
   6-month change                1 (-1 to 3)             2 (0 to 4)            -1 (-4 to 1)       0.36
   12-month change               2 (0 to 4)              3 (1 to 5)            -1 (-4 to 1)       0.37

IQR, Interquartile range
Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                          © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 8 — REPORT

[Results source p. 8](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=8>)

```text
© 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 9 — REPORT

[Results source p. 9](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=9>)

```text
Supplemental eTable 3. Sensitivity analysis. Baseline, 6-month and 12-month
changes in quality dietary scores by randomized treatment group: completers
only.

                                                               COMPLETERS ONLY
 Variable                                 Intervention            Control group               Between-group
                                          group                                                 difference
                                            n=2,862 (6 mo)         n=2,883 (6 mo)                         p value
                                           n=2,833 (12 mo)          n=2,943 (12
                                                                        mo)
 17-item er-MedDiet (0 to 17)*
    Baseline, mean (SD)                         8.5 (2.6)              8.6 (2.7)
    6-month change                          4.1 (4.0 to 4.2)       1.8 (1.7 to 1.9)       2.3 (2.2 to 2.5)   <0.001
    12-month change                         4.3 (4.2 to 4.4)       2.0 (1.9 to 2.1)       2.3 (2.1 to 2.4)   <0.001
 MDS (Trichopolou 0 to 9)
    Baseline, mean (SD)                         4.3 (1.7)              4.3 (1.6)
    6-month change                          0.2 (0.1 to 0.2)        -0.3 (-0.4 to -       0.5 (0.4 to 0.6)   <0.001
                                                                         0.3)
    12-month change                         0.2 (0.1 to 0.2)        -0.3 (-0.4 to -       0.5 (0.4 to 0.6)   <0.001
                                                                         0.3)
 MEDAS (0 to 14)
    Baseline, mean (SD)                         7.6 (1.9)              7.6 (1.9)
    6-month change                          2.5 (2.5 to 2.6)       1.4 (1.3 to 1.5)       1.1 (1.0 to 1.3)   <0.001
    12-month change                         2.7 (2.7 to 2.8)       1.6 (1.6 to 1.7)       1.1 (1.0 to 1.2)   <0.001
 PDQS (0 to 42)
    Baseline, mean (SD)                        21.0 (3.7)             21.0 (3.7)
    6-month change                          4.6 (4.5 to 4.8)       2.3 (2.1 to 2.4)       2.4 (2.2 to 2.6)   <0.001
    12-month change                         4.7 (4.5 to 4.8)       2.4 (2.3 to 2.5)       2.3 (2.1 to 2.5)   <0.001

Baseline data are means (SD). 6-month and 12-month change are means (95% CI) calculated using mixed effect
models incorporating site and intra-cluster correlations (couples) as random factors.
er-MedDiet, Energy reduced Mediterranean Diet; MDS, Mediterranean Diet Score, MEDAS, Mediterranean Diet
Adherence Screener; PDQS, Prime Diet Quality Score. The direction of all 4 food patterns is the same: a higher score
means a higher quality of the overall dietary pattern. The possible ranges were 0-17 for er-MedDiet, 0-9 for the MDS,
0-14 for MEDAS, and 0-42 for PDQS.

The minimum clinically important difference (MCID) can be considered 1 point for the MDS, because a 2 point
increment (roughly corresponding to one standard deviation) was associated in the fully adjusted model with a 25%
relative reduction in all-cause mortality (Trichopoulou et al. N Engl J Med 2003;348:2599-608, Table 4), coefficient
= log(0.75) = -0.2877. Therefore, 1 point in the MDS (corresponding to 0.5 SD) will lead to a 13% relative risk
reduction corresponding to a hazard ratio of 0.87, namely exp(-0.2877/2) = 0.87, which can be considered higher than
a minimal clinically significant effect from the subjective point of view of a patient.

For the MEDAS, in the PREDIMED trial, assessed as an observational study, and controlling for potential
confounding, 1-point increment was associated with a 10% reduction in the risk of the composite primary
cardiovascular end-point (multivariable-adjusted hazard ratio= 0.90, 95% CI, 0.85-0.96) and with a 6% reduction in
total mortality (multivariable-adjusted hazard ratio= 0.94, 95% CI, 0.89-0.99) (unpublished data). Therefore, 1 point
should represent a sufficiently important difference for an individual patient.

The 17-item er-MedDiet score basically captures the 14-items of MEDAS with some additions (sufficiently explained
in our main manuscript) that have been repeatedly associated with benefits in previous observational studies with
good control for confounding. Therefore, a 1-point difference can be also accepted as a minimum clinically important
difference.

For the PDQS (range 0 to 42, SD=3.7), the minimum clinically important difference will represent probably a 2-point
increment, given its wider range.




                              © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 10 — REPORT

[Results source p. 10](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=10>)

```text
*The number of participants included in this analysis was: for the intervention group at 6 months n=3,030 and at 12
months n=2,971 and for the control group at 6 months n=3,090 and at 12 months n=3,095




Supplemental eTable 4. Sensitivity analysis. Baseline, 6-month and 12-month
changes in food items by randomized treatment group: completers only.


                                                         COMPLETERS ONLY
 Variable                       Intervention group          Control group           Between-group difference
                                  n=2,862 (6 mo)           n=2,883 (6 mo)                                     p
                                  n=2,833 (12 mo)          n=2,943 (12 mo)                                  value
 Total olive oil (g/week)
   Baseline, mean (SD)             350 (175, 350)            350 (175, 350)
   6-month change                   26 (22 to 31)             29 (25 to 34)               -3 (-10 to 3)      0.34
   12-month change                  34 (30 to 39)             42 (38 to 47)               -8 (-15 to -1)     0.02
 Refined olive oil
 (g/week)
   Baseline, median                   0 (0, 70)                 0 (0, 70)
   (IQR)
   6-month change                  -37 (-41 to -33)         -34 (-38 to -31)               -3 (-8 to 3)      0.32
   12-month change                 -39 (-43 to -35)         -39 (-43 to -35)               0 (-6 to 5)       0.95
 Extra virgin olive oil
 (g/week)
   Baseline, median                 175 (70, 350)            175 (70, 350)
   (IQR)
   6-month change                   63 (57 to 68)             63 (58 to 69)                0 (-8 to 7)       0.90
   12-month change                  73 (68 to 79)             81 (76 to 87)               -8 (-16 to 0)      0.05
 Nuts (g/week)
   Baseline, median                 60 (28, 165)              60 (14, 165)
   (IQR)
   6-month change                 120 (115 to 126)            71 (65 to 76)               50 (42 to 57)     <0.00
                                                                                                              1
   12-month change                117 (111 to 123)            82 (77 to 88)               35 (27 to 43)     <0.00
                                                                                                              1
 Fruits (g/week)
   Baseline, median              2287 (1523, 3200)        2287 (1494, 3281)
   (IQR)
   6-month change                 349 (292 to 406)         165 (108 to 222)          184 (104 to 265)       <0.00
                                                                                                              1
   12-month change                435 (379 to 491)         244 (188 to 299)          192 (113 to 270)       <0.00
                                                                                                              1
 Vegetables (g/week)
   Baseline, median              2173 (1640, 2811)        2135 (1607, 2886)
   (IQR)
   6-month change                 330 (291 to 368)          136 (98 to 174)          193 (139 to 247)       <0.00
                                                                                                              1
   12-month change                350 (311 to 388)         141 (103 to 179)          209 (155 to 263)       <0.00
                                                                                                              1
 Cereals (g/week)
   Baseline, median               885 (641, 1432)           877 (645, 1432)
   (IQR)




                              © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 11 — REPORT

[Results source p. 11](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=11>)

```text
   6-month change           -172 (-194 to -151)       -80 (-102 to -59)         -92 (-122 to -61)    <0.00
                                                                                                       1
   12-month change          -212 (-233 to -190)       -106 (-127 to -84)       -106 (-136 to -75)    <0.00
                                                                                                       1

IQR, Interquartile range
Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




Supplemental eTable 4 cont. Sensitivity analysis. Baseline, 6-month and 12-month
changes in food items by randomized treatment group: completers only.

                                                         COMPLETERS ONLY
 Variable                  Intervention group          Control group                   Between-group difference
                             n=2,862 (6 mo)           n=2,883 (6 mo)                                     p value
                             n=2,833 (12 mo)          n=2,943 (12 mo)
 Whole grains (g/week)
   Baseline, median            109 (0, 525)              98 (0, 525)
   (IQR)
   6-month change            277 (257 to 296)           61 (42 to 81)           215 (188 to 242)         <0.001
   12-month change           231 (211 to 250)           61 (42 to 80)           170 (143 to 197)         <0.001
 Refined grains
 (g/week)
   Baseline, median          779 (425, 1475)           779 (412, 1474)
   (IQR)
   6-month change           -544 (-568 to -519)      -198 (-222 to -174)      -346 (-380 to -311)        <0.001
   12-month change          -539 (-563 to -514)      -227 (-252 to -203)      -311 (-346 to -277)        <0.001
 Legumes (g/week)
   Baseline, median           120 (88, 180)             120 (88, 176)
   (IQR)
   6-month change              38 (35 to 42)            18 (14 to 21)                20 (16 to 25)       <0.001
   12-month change             40 (37 to 43)            19 (16 to 23)                21 (16 to 25)       <0.001
 Fish (g/week)
   Baseline, median           673 (472, 918)           682 (475, 918)
   (IQR)
   6-month change            101 (88 to 113)            40 (28 to 53)                60 (43 to 78)       <0.001
   12-month change           104 (91 to 117)            31 (18 to 44)                73 (55 to 91)       <0.001
 Meat (g/week)
   Baseline, median          993 (760, 1263)           994 (776, 1271)
   (IQR)
   6-month change           -110 (-123 to -96)         -81 (-94 to -67)         -29 (-48 to -10)          0.003
   12-month change          -118 (-133 to -104)       -107 (-121 to -93)         -11 (-31 to 9)              0.27
 Red meat (g/week)
   Baseline, median           290 (150, 497)           300 (150, 520)
   (IQR)
   6-month change           -114 (-122 to -106)        -67 (-75 to -59)         -47 (-59 to -35)         <0.001
   12-month change          -120 (-129 to -112)        -80 (-89 to -71)         -40 (-53 to -28)         <0.001
 Processed meat
 (g/week)



                         © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 12 — REPORT

[Results source p. 12](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=12>)

```text
   Baseline, median              227 (143, 317)           227 (143, 322)
   (IQR)
   6-month change               -63 (-69 to -57)          -45 (-51 to -39)          -18 (-26 to -9)          <0.001
   12-month change              -64 (-70 to -58)          -52 (-58 to -46)          -11 (-20 to -3)           0.01
 Pastries (g/week)
   Baseline, median              121 (42, 275)             114 (42, 261)
   (IQR)
   6-month change             -109 (-116 to -101)         -49 (-57 to -42)         -59 (-70 to -49)          <0.001
   12-month change            -109 (-116 to -101)         -60 (-67 to -52)         -49 (-60 to -39)          <0.001

IQR, Interquartile range
Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.



Supplemental eTable 4 cont. Sensitivity analysis. Baseline and 6- and 12- month
changes in food items by randomized treatment group: completers only.

                                                             COMPLETERS ONLY
 Variable                        Intervention              Control group                   Between-group difference
                                     group
                                n=2,862 (6 mo)            n=2,883 (6 mo)                                    p value
                                n=2,833 (12 mo)           n=2,943 (12 mo)
 Dairy (g/week)
   Baseline, median (IQR)         2,100 (1,532,         2,200 (1,548, 3,597)
                                      2,959)
   6-month change                 17 (-33 to 67)          -143 (-192 to -93)        159 (89 to 230)          <0.001
   12-month change                -39 (-88 to 11)        -186 (-235 to -137)        148 (78 to 218)          <0.001
 Total yogurt (g/week)
   Baseline, median (IQR)         375 (58, 875)             375 (58, 875)
   6-month change                119 (98 to 140)             6 (-15 to 27)          113 (83 to 143)          <0.001
   12-month change                87 (66 to 109)            -4 (-25 to 17)              91 (61 to 121)       <0.001
 Fermented dairy
 (g/week)
   Baseline, median (IQR)        550 (300, 975)           575 (300, 1,025)
   6-month change                 97 (75 to 119)            -9 (-31 to 14)          105 (74 to 137)          <0.001
   12-month change                72 (49 to 94)             -15 (-37 to 7)              86 (55 to 118)       <0.001
 Low-fat dairy (g/week)
   Baseline, median (IQR)         658 (0, 1,775)            687 (0, 1,775)
   6-month change               327 (280 to 373)            62 (15 to 108)          265 (199 to 331)         <0.001
   12-month change              270 (223 to 317)            -1 (-47 to 45)          271 (206 to 337)         <0.001
 Whole-fat dairy
 (g/week)
   Baseline, median (IQR)           0 (0, 375)                0 (0, 375)
   6-month change              -173 (-197 to -149)        -111 (-135 to -87)        -61 (-95 to -27)         0.001
   12-month change             -159 (-183 to -134)        -99 (-124 to -75)         -59 (-94 to -25)         0.001
 Total alcohol intake
 (g/week)
   Baseline, median (IQR)           32 (5, 98)               36 (5, 103)




                            © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 13 — REPORT

[Results source p. 13](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=13>)

```text
   6-month change                -13 (-16 to -10)            -6 (-9 to -3)              -7 (-11 to -3)   <0.001
   12-month change                -12 (-15 to -9)            -4 (-7 to -1)              -8 (-12 to -3)   <0.001
 Red wine (g/week)
   Baseline, median (IQR)            4 (0, 29)                 4 (0, 29)
   6-month change                   1 (-1 to 3)               2 (0 to 4)                 -1 (-4 to 2)     0.38
   12-month change                  2 (0 to 4)                3 (1 to 5)                 -1 (-4 to 2)     0.40


IQR, Interquartile range
Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                            © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 14 — REPORT

[Results source p. 14](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=14>)

```text
Supplemental eTable 5. Sensitivity analysis. Baseline values, 6-month and 12-
month changes in nutrient intake by randomized treatment group: completers
only.

                                                            COMPLETERS ONLY
 Variable                      Intervention group         Control group                 Between-group difference
                                 n=2,862 (6 mo)          n=2,883 (6 mo)                                  p value
                                 n=2,833 (12 mo)         n=2,943 (12 mo)
 Total energy Intake
 (kcal/d)
   Baseline, mean (SD)              2,355 (544)             2,369 (555)
   6-month change               -173 (-192 to -154)       -78 (-97 to -59)       -95 (-122 to -68)        <0.001
   12-month change              -176 (-196 to -157)        -74(-93to -54)       -103 (-130to -75)         <0.001
 Total protein (%E)
   Baseline, mean (SD)               16.8 (2.8)              16.8 (2.8)
   6-month change                 1.2 (1.1 to 1.3)         0.2 (0.1 to 0.3)          1.0 (0.9 to 1.2)     <0.001
   12-month change                1.1 (1.0 to 1.2)           0 (-.1 to .1)           1.1 (1.0 to 1.2)     <0.001
 Total carbohydrate (%E)
   Baseline, mean (SD)               40.7 (6.8)              40.4 (6.9)
   6-month change                -3.3 (-3.6 to -3.1)     -1.8 (-2.1 to -1.6)    -1.5 (-1.9 to -1.2)       <0.001
   12-month change               -3.7 (-3.9 to -3.4)     -2.3 (-2.5 to -2.0)    -1.4 (-1.8 to -1.1)       <0.001
 Total fat (%E)
   Baseline, mean (SD)               39.5 (6.6)              39.7 (6.5)
   6-month change                 2.5 (2.2 to 2.7)         1.8 (1.5 to 2.0)          0.7 (0.3 to 1.0)     <0.001
   12-month change                2.9 (2.6 to 3.1)         2.3 (2.1 to 2.6)          0.5 (0.2 to 0.9)     0.004
 SFA (%E)
   Baseline, mean (SD)                9.9 (2.0)              10.0 (2.0)
   6-month change                -1.0 (-1.1 to -0.9)     -0.6 (-0.6 to -0.5)    -0.4 (-0.6 to -0.3)       <0.001
   12-month change               -0.9 (-1.0 to -0.9)     -0.6 (-0.7 to -0.5)    -0.4 (-0.5 to -0.3)       <0.001
 MUFA (%E)
   Baseline, mean (SD)               20.5 (4.7)              20.6 (4.6)
   6-month change                 3.5 (3.3 to 3.7)         2.3 (2.1 to 2.5)          1.2 (0.9 to 1.4)     <0.001
   12-month change                3.9 (3.7 to 4.1)         3.0 (2.8 to 3.2)          0.9 (0.6 to 1.2)     <0.001

Baseline data are means (SD)
E, energy; SFA, saturated fatty acids; MUFA, monounsaturated fatty acids
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                         © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 15 — REPORT

[Results source p. 15](<../../../../joi190106supp3_prod_1635377898.49725.pdf#page=15>)

```text
Supplemental eTable 5 cont. Sensitivity analysis. Baseline values, 6-month and 12-
month changes in nutrient intake by randomized treatment group: completers
only.

                                                               COMPLETERS ONLY
 Variable                              Intervention            Control group               Between-group difference
                                           group
                                      n=2,862 (6 mo)          n=2,883 (6 mo)                                p value
                                      n=2,833 (12 mo)         n=2,943 (12 mo)
 Ratio MUFA:SFA
   Baseline, mean (SD)                     2.1 (0.5)               2.1 (0.5)
   6-month change                      0.6 (0.6 to 0.7)        0.4 (0.4 to 0.4)         0.3 (0.2 to 0.3)    <0.001
   12-month change                     0.7 (0.6 to 0.7)        0.5 (0.4 to 0.5)         0.2 (0.2 to 0.2)    <0.001
 PUFA (%E)
   Baseline, mean (SD)                     6.4 (1.9)               6.4 (1.8)
   6-month change                      1.3 (1.2 to 1.4)        0.8 (0.7 to 0.8)         0.5 (0.4 to 0.6)    <0.001
   12-month change                     1.3 (1.2 to 1.3)        0.8 (0.8 to 0.9)         0.4 (0.3 to 0.5)    <0.001
 Total alcohol (%E)
   Baseline, median (IQR)                   1 (0, 4)               2 (0, 4)
   6-month change                     -0.3 (-0.4 to -0.2)      -0.1 (-0.2 to 0)         -0.2 (-0.4 to 0)     0.02
   12-month change                    -0.3 (-0.4 to -0.1)       0 (-0.1 to 0.1)          -0.3 (-0.4 to -     0.01
                                                                                              0.1)
 Fiber (g/week)
   Baseline, mean (SD)                     184 (63)                182 (60)
   6-month change                       40 (37 to 42)           16 (14 to 19)            24 (20 to 27)      <0.001
   12-month change                      37 (35 to 40)           18 (16 to 21)            19 (16 to 22)      <0.001
 Long chain w-3 fatty acids
 (g/week)
   Baseline, median (IQR)                   5 (4, 9)               5 (4, 9)
   6-month change                      1.1 (0.9 to 1.2)        0.4 (0.3 to 0.6)         0.7 (0.5 to 0.8)    <0.001
   12-month change                     1.1 (1.0 to 1.2)        0.4 (0.3 to 0.6)         0.7 (0.5 to 0.9)    <0.001
 Cholesterol (mg/week)
   Baseline, mean (SD)                   2,651 (793)             2,682 (794)
   6-month change                    -222 (-250 to -194)       -169 (-197 to -          -53 (-93 to -13)    0.009
                                                                    141)
   12-month change                   -218 (-247 to -189)       -206 (-235 to -          -12 (-52 to 29)      0.58
                                                                    178)
 Sodium (g/week)
   Baseline, median (IQR)             22.2 (17.9, 27.1)        22.2 (17.9, 27.4)
   6-month change                     -3.1 (-3.3 to -2.8)     -1.9 (-2.1 to -1.6)        -1.2 (-1.5 to -    <0.001
                                                                                              0.9)
   12-month change                    -3.2 (-3.5 to -3.0)     -1.9 (-2.1 to -1.6)        -1.3 (-1.7 to -    <0.001
                                                                                              1.0)

Baseline data are means (SD) or median (IQR)
E, energy; SFA, saturated fatty acids; MUFA, monounsaturated fatty acids; PUFA, polyunsaturated fatty
acids;
w-3, omega-3
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.



                            © 2019 American Medical Association. All rights reserved.

```

