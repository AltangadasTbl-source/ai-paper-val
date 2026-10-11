# Complete checker excluded-observation union

Mechanical coordinator projection from the three current canonical checkers; every original row is retained for independent pass2 and audit review.

## Numeric checker


Only apparent discrepancies actually examined and not emitted appear below; reconciled checks are in the N inventory. Each row has exactly one scope reason code.

| Location | Observation | Reason code |
|---|---|---|
| DOC001 p.4 population narrative versus p.5 Table1 stageII | Pooled stageII111/417=26.619% versus printed26%; half-unit output [25.5,26.5] and recomputation interval [110.5/417.5×100,111.5/416.5×100]=[26.467,26.771] overlap, so discrepancy0. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC001 p.5 Table1 middle baseline25(OH)D vitamin D | 142/248=57.258% versus58%; count half-unit recomputation [141.5/248.5×100,142.5/247.5×100]=[56.9416,57.5758], printed [57.5,58.5] overlap; no qualifying numeric gap. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC001 p.5 Table1 DBP1 TG placebo versus DOC003 p.23 eFigure3Q year-zero placebo risk | 57 versus59; half-unit intervals[56.5,57.5] and[58.5,59.5], gap1/57=.01754≤.05. Locus sums148 versus150 reflect the same occurrence. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC001 p.5 Table1 BMI/baseline25(OH)D/FokI percentages versus whole-arm headers | Recomputed every displayed cell using explicit251/166 headers as well as category sums; every apparent gap remains within half-unit intervals or relative.05. The above-threshold cells in the other six loci are included inF-NUM-002 rather than excluded by available-case assumptions. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC001 pp.1,4 primary and death event counts versus five-year survival77/69 and82/81 | Whole-follow-up crude event proportions have different estimands from five-year survival in a censored survival analysis. | MODEL_VERSUS_CRUDE |
| DOC001 p.6 serum25(OH)D medians versus printed87% change ratio | (41−21)/21=95.24% is the change in printed group medians, not the participant change-ratio distribution compared by Mann–Whitney. No claim equates those quantities. | CONDITIONAL_OR_UNREPORTED |
| DOC003 pp.2–4 achieved-mean serum population413 versus DOC001 pp.4–6 baseline population410 | Trial-average values use baseline and annual samples, whereas baseline groups exclude seven missing baseline results; differing availability definitions do not establish conflicting analysis-population counts. | CONTEXT_RESOLVES |
| DOC001 p.7 Figure3 caption versus visible panelC risk table | Caption says numbers at risk for panelC not given because weighting, but panelC visibly supplies both risk rows; this figure-pointer/caption difference supplies no alternative printed count or result and is a peripheral comparison. | PERIPHERAL_COMPARISON |
| DOC002 initial pp.9,12 versus final pp.25,28,45 | Initial1200IU/day=2×600 versus initial capsule paragraph1000IU; reported trial relies on the disclosed pretrial amendment and final2000IU=2×1000. This historical plan-version inconsistency does not change the reported intervention or statistical decision rule. | PERIPHERAL_COMPARISON |


## Cross-source checker


| Location | Observation | Reason code |
|---|---|---|
| PLAN pp. 9/12/25/28/45 | Initial intervention 2×600 IU differs from initial capsule paragraph 1000 IU; the reviewed final dose and report agree at 2×1000=2000 and amendment explicitly records pretrial increase | CONTEXT_RESOLVES |
| PLAN p. 23 versus p. 31 | High group's design parenthesis prints 40 ng/mL without a comparator; complete low/middle categories and SAP's >40 define the intended boundary immediately | NOTATION_OR_TYPOGRAPHY |
| PLAN pp. 9/24/38 and REPORT p. 2 | Registration form age30≤<90 versus narrative age30–90, additional consent/surgeon-judgment checkboxes versus numbered criteria; no demonstrated change to randomized or analyzed population | PERIPHERAL_COMPARISON |
| PLAN pp. 9/24 and REPORT p. 2 | Epidermal versus epithelial carcinoma labels, with identical anatomical sites and exclusion examples | TERMINOLOGY_OR_WORDING |
| PLAN pp. 13/29 versus pp. 9/25 | Follow-up paragraph says relapse-free “or alive,” whereas explicit primary definition requires no relapse and alive; clear primary definition resolves intended composite censoring wording | TERMINOLOGY_OR_WORDING |
| PLAN pp. 10/25/41 and REPORT pp. 2/7 | “Non-cancer” plan examples include de novo cancer progression; report says noncancer death while plan explicitly distinguishes primary from non-primary cancer deaths; no source result/count demonstrates reallocation | TERMINOLOGY_OR_WORDING |
| PLAN pp. 12/27 and REPORT p. 3; REPORT supplement pp. 13–15 | FokI rs10735810 versus rs2228570 and CDX2 versus CDK2 labels; matching locus/genotype/sample groups identify intended subgroup, with no different numeric outcome assignment demonstrated | TERMINOLOGY_OR_WORDING |
| PLAN pp. 17/45 | Final cover printed version1 versus amendment-history version3; dates establish supplied final version and no analysis rule differs solely because of version numbering | PERIPHERAL_COMPARISON |
| PLAN pp. 45 and 17/18 | DBP/de novo amendment dates2012.12.8 versus final-version/subgroup date2012.12.18; calendar detail does not establish a changed decision rule or result | PERIPHERAL_COMPARISON |
| PLAN pp. 3/14/18/30/45 | Initial blank sample-size SAP versus initial synopsis400; final amended400 is supplied and report relies on final calculation, so initial-document residual does not alter reported plan assumptions | CONTEXT_RESOLVES |
| PLAN pp. 30–31 and REPORT pp. 3–4 | Planned80/year×5 accrual and7-year total versus actual enrollment January2010–April2016 and follow-up2018; the former are explicitly planning assumptions, latter observed calendar | CONTEXT_RESOLVES |
| PLAN p. 31 and REPORT p. 3/supplement eTable2 | Missing-data exclusion/MI, age/stage adjustment and PH checks absent from SAP; report explicitly labels these analyses post hoc, so absence alone creates no prespecification conflict | CONDITIONAL_OR_UNREPORTED |
| REPORT p. 7 Figure3C caption and risk table | Caption says panelC risk numbers not given because weighting; displayed risk numbers are present, but the pointer/text does not change a primary/key-secondary estimate or starting analysis-population count | PERIPHERAL_COMPARISON |
| REPORT p. 5 DBP1 TG and supplement p. 23 | Placebo genotype count57 versus starting risk count59: half-unit intervals[56.5,57.5] and[58.5,59.5], gap1; reference57 gives relative discrepancy1/57=.01754≤.05 | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT abstract p. 1 and narrative p. 4 | Age66 is explicitly mean in abstract and median in narrative; these are separate summaries and the package does not establish either value as the other's copy | NOT_REPRODUCED |
| REPORT supplement p. 6 versus main p. 7 | MI subgroup estimates/CI/P equal complete-case printed results at displayed precision; equality alone does not establish a conflict with the imputation claim | CONDITIONAL_OR_UNREPORTED |


## Statistical pass1 checker


Only apparent issues considered but not emitted appear here. Successful checks are in S records. Each row has exactly one scope reason code. None of these rows establishes a null-significance contradiction or a reproducing source-stated test conflict; pass2 must independently revisit every row under RouteA and the display-precision rule.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p.6 age-adjusted RFS;S016 | HR.66,CI.43–.99,P.048: symmetric log-Wald diagnostic joint rounded HR/CI permits P≈.042745–.047316, whereas displayed P interval is[.0475,.0485). Residual gap≈.000184/.048≈.00384. Source does not identify this P as a Wald rather than score/likelihood-ratio test; CI excludes1 and P<.05 agree. No exact stated-test contradiction reproduced. Exclusion rests on absent construction, not on treating a RouteA1 conflict as rounding. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp.4/6 lab25(OH)D;S020 | Group medians21→41 imply95.24% centered crude change, whereas reported individual change-ratio summary87%; source defines change-ratio comparison across patients rather than ratio of group medians. Summary-of-ratios is distinct from ratio-of-summaries. | CONTEXT_RESOLVES |
| REPORT main pp.3–4/6 and supplement p.6;S094/S040–S043 | All imputed HR/CI/P rows repeat available-case values to displayed precision; source provides neither individual imputed values nor pooled variances/post-imputation counts to establish that any row conflicts. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp.3/5 PH checks;S095 | Schoenfeld tests called nonsignificant without numerical statistics/P; no supplied contradictory PH-test result. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p.6 stageI-adjusted model;S095 | StageI-adjusted analyses described as nonsignificant without estimates/intervals; no printed adjusted number conflicts. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp.3–4 interim;S089 | Three interims did not meetPetoP<.001, but numerical interim test outputs absent; cannot reconstruct a contradictory stopping decision. | CONDITIONAL_OR_UNREPORTED |
| REPORT supplement p.21 eFig3O;S058 | TaqICC HR/CI/interaction shown as dashes with P1.00 and one event in vitaminD/none visible in placebo; no finite coefficient,SE or exact test specified. Sparse Cox fitting may not yield a finite HR, and the displayed test cannot be independently reconstructed from curves. | CONDITIONAL_OR_UNREPORTED |
| REPORT supplement pp.34–39 site/stage interactions;S071–S076 | Category-specific panels print different interaction Ps; exact contrasts/omnibus coding not identified. Different contrasts are possible and no source says these are identical tests. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp.9/13 and25/29;S101 | Relapse-free “or alive” wording in follow-up collection paragraph versus full primary earliest-relapse-or-death definition; full endpoint definition resolves intended reading, without a printed event-count conflict. | TERMINOLOGY_OR_WORDING |
| PLAN initial pp.8–9/12,finalp.25/amendmentp.45;S102 | Initial1200IU regimen versus1000IU/capsule paragraph, while finalplan/report explicitly2000IU after pretrial dose amendment. The actual randomized intervention is identified by final specification/amendment; the older unimplemented detail does not change the relied-on reported analysis. | CONTEXT_RESOLVES |
| PLAN pp.14/31 baseline tests versus REPORT mainTable1 p.5;S104 | Planned descriptive baseline t/Mann–Whitney/chi-square comparisons are not printed as baseline P values; no primary/key-secondary statistical result or population size is changed by that descriptive-display omission. | PERIPHERAL_COMPARISON |
| REPORT supplement pp.13–15 eFig3 labels versus REPORT main/PLAN CDX2 definition;S050–S052/S093 | Supplement says CDK2 while genotype block and supplied SNP definition identify CDX2; the intended same genotype grouping is immediately identifiable and no printed effect value is changed. | TERMINOLOGY_OR_WORDING |
| REPORT main p.7 Fig3 caption;M095 | Caption says panelC risk numbers not given due weighting, although numbers appear under panelC. This figure pointer does not change the printed HR/CI/P or identify a conflicting analysis; full risk rows are visible. | PERIPHERAL_COMPARISON |
| REPORT main p.5 Table1DBP1TG and supplementp.23 risk0;S060/S093 | Placebo57 versus59: half-unit intervals[56.5,57.5] versus[58.5,59.5] givegap1/57≈.01754≤.05; pooled locus148 versus150 similarly stays within display-precision threshold. Do not infer a genotype reclassification from this supplied difference alone. | ROUNDING_OR_DISPLAY_PRECISION |

## Cross-lane source-confirmed relationship coverage

S104 also covers the Table1 genotype count/percentage/denominator relationship reported by the current numeric checker as F-NUM-002 (N033–N038/N095). I independently viewed exact main p.5 source-linked image, confirmed explicit251/166 headers and absence of a genotype-denominator footnote, and recomputed all22 above-.05 cells using count/header half-unit intervals and percentage±.5. All22 calculations match current numeric provenance. Locus category-sum denominators are source-grounded alternatives, not explicit display context. This Route A category3 count relationship is covered for both statistical-pass scope and extraction/population implications without emitting a duplicate statistical finding. Linked inferential records S093/S044–S064 preserve the genetic analyses; S104 names the complete count relationship. The other current numeric finding F-NUM-001 is the same source pattern as F-ST1-001/S100. The two scientific checker artifacts retain independent provenance.

