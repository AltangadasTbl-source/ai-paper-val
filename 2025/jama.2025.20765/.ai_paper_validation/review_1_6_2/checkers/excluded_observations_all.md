# Complete initial checker excluded-observation handoff

All 45 observations copied verbatim from current-run checkers, with provenance. No screening decisions are replaced.

## Provenance: checkers/numeric_consistency.md

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| [REPORT PDF p. 4](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4), Figure1 excluded-patient reasons | Reasons sum above8152, but note b expressly permits more than one exclusion reason per participant; an exclusive partition was an apparent assumption, not a displayed requirement. | CONTEXT_RESOLVES |
| [REPORT PDF p. 5](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5), Table1 low-addiction row | 514(75.7%) and212(65.0%) appear inconsistent if divided by the full720/360; the cigarette-user population679/326 reproduces them and identifies the appropriate HSI population in context. | NOT_REPRODUCED |
| [REPORT PDF p. 5](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5), Table1 TB-stage rows | Independently rounded stage percentages sum100.1% in each arm; row percentages pass half-unit checks, and all stage counts total720/360. | ROUNDING_OR_DISPLAY_PRECISION |
| [REPORT PDF p. 4](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4), Participants; [REPORT PDF p. 5](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5), Table1 tobacco use/day | Narrative calls5/7 cigarettes and8/15 bidis an average while Table1 labels the summaries median; all numbers agree and field reading resolves the summary wording immediately. | TERMINOLOGY_OR_WORDING |
| [REPORT PDF p. 3](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3), mixed-effects analysis; [REPORT PDF p. 6](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6), Table2 crude RR column | Aggregate event-risk ratios differ from some crude-labeled RRs, for example primary300/720 divided by55/360=2.7273 versus3.0. The methods and table notes identify clustered mixed-effects estimates; “crude” does not assert an aggregate participant ratio without cluster modeling. This comparison alone cannot diagnose a numerical inconsistency. | MODEL_VERSUS_CRUDE |
| [REPORT PDF p. 3](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3), logistic model; [REPORT PDF p. 6](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6), RR headers | Logistic-model wording invites an assumption that an exponentiated coefficient is reported as RR, but an aggregate OR does not reproduce these rows and no printed transformation identifies that computation. The numeric checker cannot establish effect-measure identity from this assumption; the independent statistical lane reviews the stated-method logic. | CONDITIONAL_OR_UNREPORTED |
| [REPORT PDF p. 6](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6), treatment failure usual-care percentage; [REPORT PDF p. 1](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1) and [REPORT PDF p. 5](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5) repeated result | 2/360×100=.555556% versus printed.5%. Half-unit count inputs give100×[1.5/360.5,2.5/359.5]=[.416089,.695410]%, overlapping printed[.45,.55]%; relative discrepancy0 under the required rule. | ROUNDING_OR_DISPLAY_PRECISION |
| [REPORT PDF p. 5](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5), Secondary Outcomes; [REPORT PDF p. 6](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6), TB outcome rows | Success+death+default+failure total691 M and344 U versus720/360; these main-report rows are not declared an exhaustive outcome partition, so requiring equality would depend on an unstated category assumption. | CONDITIONAL_OR_UNREPORTED |


## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-003 REPORT p3, eTable 1 | Ineligibility reason counts total 13856, above 8146 ineligible participants; reasons are not stated to be mutually exclusive and can occur together. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 REPORT p4, eTable 2 | Site 2012 appears in later site tables but has no prior-quit-attempt row here; no printed total or analysis-population size is contradicted by this descriptive table omission. | PERIPHERAL_COMPARISON |
| DOC-003 REPORT p5, eTable 3 | Monthly mean sums174.19/177.7 differ from printed total174.3/178.0; the printed input and total half-unit intervals overlap. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 REPORT pp6,8,15–16, eTables 4,5,10 | Small percentage deviations, including overall heart-attack8/52 with15.2%, recruitment40/527 with7.5%, and symptom percentages rounded to whole or one-decimal units, fit input intervals or have remaining relative discrepancy≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 REPORT pp3,8, eTables 1,5 | Site recruitment-screening denominators sum9240 versus screening total9232; half-unit output gap7 and relative7/9232=.000758 are below0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 REPORT pp15–16, eTable 10 | Epigastric-pain category count sum698 mHealth versus699 implied by other symptoms; no explicit same-table denominator is printed and percentages fit both totals; even a one-person total difference is below0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 REPORT pp13–14, eTable 9 | Crude RR values differ from unclustered risk ratios, including300/695 versus55/333 yielding2.6135 rather than2.9. Crude and adjusted cluster ICCs and the mixed-model context do not establish that this column is the simple unclustered ratio. | MODEL_VERSUS_CRUDE |
| DOC-002 PLAN pp63–64, lines1894–1907 and1936–1943 | Printed attrition/product results704,1036,1080,1620 differ from arithmetic704.4,1036.8,1056,1616.16; half-unit input intervals overlap or remaining relative discrepancy≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-002 PLAN p62, lines1866–1868 and pilot diagram | “In each site n=16” differs from diagram total16 across4 sites; the immediately adjoining figure and first16 pilot statement show the aggregate reading. The observation depends on site-level wording. | TERMINOLOGY_OR_WORDING |
| DOC-002 PLAN p64, line1948 | A phase-4 diagram box says “Phase 3 (Superiority trial)” while its surrounding title, arm labels, 36 sites and1620 participants consistently identify phase4; the numeric values themselves are unchanged. | TERMINOLOGY_OR_WORDING |
| DOC-002 PLAN p85, MPSS description | Five domains and a5-point scale are described with total5–35; the scale description is a wording/terminology observation without a reported numeric result that can be reconstructed from printed participant values. | TERMINOLOGY_OR_WORDING |
| DOC-002 PLAN pp54–55, TAM table | Process-substudy table says30% while prose and country counts use20%; this does not determine a reported primary/key-secondary result, analysis-population size or statistical decision rule. | PERIPHERAL_COMPARISON |


## Provenance: checkers/cross_source_consistency.md

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p 3/p 6; PLAN SAP pp 91–92 | Main table calls the available-outcome sensitivity PP, while methods/SAP call it complete case; denominators 667/318 and the stated exclusion rule identify the same set immediately. | TERMINOLOGY_OR_WORDING |
| REPORT main pp 3/6; REPORT supplement p 13 | CO<6 post hoc sensitivity rows appear under a primary-outcomes heading; immediate report methods identify them as sensitivity analyses of the same primary endpoint, not a newly declared co-primary outcome. | TERMINOLOGY_OR_WORDING |
| PLAN pp 27/65; PLAN pp 8/47/84 | Economic cost-per-additional-quitter wording calls quitting secondary; the economic passage does not identify a different continuous-abstinence analysis, and the primary endpoint remains explicit. | TERMINOLOGY_OR_WORDING |
| PLAN pp 47/84; REPORT main p 3 | Strict CO<10 verification and CO>10 override leave exactly 10 unstated in the override sentence; positive endpoint criterion<10 already defines inclusion, with no observed 10 ppmresult in conflict. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp 13/51; REPORT main p 2 | Planned minimization balances country/monthly TBvolume; report describes country stratification. This does not establish that monthly-volume minimization was absent; no incompatible algorithm or fitted adjustment statement is printed. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp 11/49; REPORT main p 2 | Retreatment exclusion is omitted from shortened report wording; no enrolled retreatment population or analysis count conflicts. | CONDITIONAL_OR_UNREPORTED |
| PLAN p 55 | TAM30% tableversus 20% text and country target rows concerns an unreported process substudy; it does not change a primary/key-secondary result, reported analysis-population size, or statistical decision rule. | PERIPHERAL_COMPARISON |
| PLAN pp 51/63/77/83 | Phase 3 target 1096 including 16 pilotversus 1080; printed-count intervals [1095.5, 1096.5]/[1079.5, 1080.5] gap 15/1080=.0139≤.05. Combined 2716 versus 2700 likewisegap 15/2700=.0056. No separate change of the ITT inclusion criterion is demonstrated. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p 7 Figure 2; REPORT supplement p 8 eTable 5 | Lowest usual-care observed graphical point appears slightly abovezero while one site table prints 0/35; figure's sequential cluster IDs have no exact supplied site-ID crosswalk, and no exact numerical plotted value is printed. A unique source-matched numeric discrepancy is not reproduced. | NOT_REPRODUCED |
| PLAN pp 85/92/97; complete REPORT sources | Clinical TBscore, sputumconversion, relapse, EQ-5 D, MPSS/SUTS, economic/process results are not supplied. None is in the abstract or explicitly designated key secondary; absence alone is outside the route A5 planned-primary/key-secondary nonreporting category. No reported contrary status/composite is identified. | CONDITIONAL_OR_UNREPORTED |
| PLAN p 91; REPORT main p 6 | SAP promises primary-model Pvalue; table provides RR/CIand narrative significance but no Pvalue. This is an unreported statistic, with no conflicting printed Pvalue, test, or replacement analysis. | CONDITIONAL_OR_UNREPORTED |


## Provenance: checkers/statistical_pass_1.md

## Excluded observations

Only apparent issues not emitted are listed. Relationships that reconcile without an apparent issue are recorded in the inventory, not counted here. Every row has exactly one reason code.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p6 Table2; DOC-003 pp11–14 eTables7–9 | Model-based RRs differ from count-based risk ratios. Mixed-effects/adjusted estimates are not crude participant-level ratios even when a column saysCrude; no source states the displayed modelRR equals the simple ratio. | MODEL_VERSUS_CRUDE |
| PLAN DOC-002 pp63–64; REPORT DOC-001 p3 | Initial n587 and n864 do not equal one normal-approximation calculation from displayed power/rates. The precise initial sample-size test, continuity adjustment/equation and software are not supplied; diagnostic≈540/969 is not a reproducing source method and does not establish a contradiction. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp63–64 attrition calculations | Additive20% allowance versus dividing by.8 would produce≈734 rather than704 and1080 rather than1036. Even the point-level gap relative to704/1036 isabout4.2–4.3%; allowing input/output half-units makes the relative discrepancy no larger. The explicit additive rule itself reproduces. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 pp63–64,83; REPORT DOC-001 p3 | 704×1.50=1056 versus≈1080;1036×1.56=1616.16 versus1620;1.50versus1.56 Phase4DE. For704±.5 and1.50±.005 product[1051.7325,1060.2725],printed1080±.5 gap19.2275/1080=.0178; Phase4gap<.003; DEgap(.050)/1.50=.0333. Rounded cluster capacities and display rule screen the apparent arithmetic differences. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p6 Table2 and DOC-003 p12 eTable8 | Other log-symmetric reconstruction departures do not cross.05: Table2 primaryITT crude.01622,adjusted.04562;CO10PPcrude.03983;CO6ITTadjusted.03053. eTable8 age<40 .000571,no formal .043561,smoking≥24 .012204,readingYes .017970. These are excluded once; rows above.05 are all retained inF-ST1-001. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp6,8 | Narrative observedICC.19 versus primaryITTtable.18. Printed ranges[.185,.195] and[.175,.185] touch,gap0;complete-caseICC.19 also supplies context. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp3,6 | PP label versus complete-case description. The methods define omission of missingprimary outcomes and Table2 denominators667/318 exactly implement it; terminology does not obscure which numbers apply. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 p5;DOC-003 p11 eTable7 | Narrative says shorter smoking duration and higher education modified theprimary outcome, whereas table supplies prognostic covariateRRs rather than interactions. Immediate outcome-predictor context allows the wording, and no specific interaction statistic is claimed. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 pp3,7 Figure2 | Bayesian prior,MCMC and exact numerical CrI endpoints are not supplied. No printed probability/statement conflicts with a stated prior or method; graphical values remain approximate. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp85–86,91–92,97;allREPORT results | Additional planned non-key secondary EQ5D,clinicalTB score,sputum conversion,relapse,MPSS/SUTS and anyAE/SAE analyses are not displayed. These are not designatedkey secondary or primaryanalyses and no status-changing replacement is stated; omission alone is peripheral under the tiered scope. The planned genderprimary subgroup is separately emitted. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 pp64–65,83 | Phase4 cluster allocations18/18 versus20/20 concern the separately unreported noninferiority phase; no reportedPhase3 decision or population depends on those counts. Phase3allocation discrepancy is separately emitted. | PERIPHERAL_COMPARISON |
| REPORT DOC-003 pp15–16 eTable10 | Pearson diagnostics give drymouth31.842versus31.2;headache2.787versus2.7;insomnia6.991versus6.9. Even treating integer counts as exact,printedhalf-units yield maximum relativegaps.01898,.01386,.00590,all≤.05. Exact-marked rows retain their distinct test and are not judged by an assumeddf. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 p84;REPORT DOC-001 p3 | Planned urine-striplevel<3 versus report negativecassette naming does not supply a numerical contradictory threshold or observedclassification. Missing assaymapping alone is not a result conflict. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp8,47,84;REPORT DOC-001 p3 | CO<10 verification andCO>10 supersession sentences leave an unstated operational sentence for exact10. No observedexact10 result or claimed classification conflicts; the<10 endpoint itself is definite. | CONDITIONAL_OR_UNREPORTED |


