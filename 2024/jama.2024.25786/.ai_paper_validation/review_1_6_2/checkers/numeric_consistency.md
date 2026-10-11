# Numeric consistency check — main report

Status: COMPLETE. Fresh runtime task /root/numeric_main; numeric_consistency_reviewer, gpt-6.1-sol, medium. Assigned scope: DOC-001, REPORT, all 11 source pages, MAIN-N001–MAIN-N066 mapped as N001–N066. All 96 printed numerator/denominator/percentage pairs, every Figure 1 branch and exclusion reason, every Figure 3 event/at-risk array, every Figure 4 subgroup total, and matched main-report count occurrences were reviewed. Supplement displays belong to the support numeric shard; cross-document matching and inferential test logic belong to their separate reviewers.

QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Current main mapping was read; direct supplied-source layout text was obtained using Poppler 26.01.0 pdftotext, streamed without creating derivatives. Source-matched full-page render p.8 was inspected for Figure 4 values and caption alignment. No earlier candidate/report conclusions or external evidence were read. All compared locations below have document role REPORT. Scientific coverage gaps: none. See relationships/numeric_relationship_inventory.md for complete printed inputs and reconciliation records.

Self-screened totals:66 stable main numeric relationships;2 findings;9 excluded observations. No candidate IDs, adjudications or grades are assigned here.

## Findings

### F-NUM-001

**Title:** Counts from completed and primary-analysis populations are described as randomized population counts.

**Exact source locations and document roles:** REPORT DOC-001 [p.1 Abstract, Interventions and Results](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=1); REPORT DOC-001 [p.2 Key Points, Findings](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=2); REPORT DOC-001 [p.3 Figure 1 randomized and group-allocation boxes](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3); REPORT DOC-001 [p.5 Trial Population](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5). Related inventory: N002, N004, N007, N011, N012.

**Printed inputs:** Abstract Interventions says patients were randomly assigned 1:1 and gives restrictive n=733, liberal n=724. Key Points says “Among 1508 randomized adult trauma patients.” Abstract Results and Trial Population say 1979 were randomized and 1508 completed. Figure 1 gives 983 randomized to restrictive and 994 randomized to liberal after 2 envelopes were lost;750/758 received strategies;733/724 entered primary analysis. Trial Population gives 1457 primary-outcome participants,733/724.

**Rule and calculation:** Randomized counts should refer to allocation before reported postrandomization exclusions, rather than received-intervention/completed or primary-analysis counts. Counts 1979−1508=471,983−733=250 and 994−724=270 identify the population differences. For printed copies at integer precision:1979 interval[1978.5,1979.5] versus 1508 interval[1507.5,1508.5], gap 470, relative 470/1979=0.237494. Restrictive 983 interval[982.5,983.5] versus 733 interval[732.5,733.5], gap 249, relative 249/983=0.253306. Liberal 994 interval[993.5,994.5] versus 724 interval[723.5,724.5], gap 269, relative 269/994=0.270624. Each exceeds 0.05. The source supplies the population identities; no allocation mechanism is inferred.

**Focus area:** A, counts and denominators.

**Proposed review domain:** statistical_results. Proposed relationship: S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** Total randomized sample size and arm-level randomized denominators accompanying the primary result. Extraction from the Key Points/Abstract intervention description yields 1508 and 733/724; Figure 1 gives 1979 and 983/994 with 2 unallocated-envelope cases.

**Why context does not resolve it:** B1: randomized/completed/analyzed participant totals are in focus. B2: the named randomized quantities have two different printed count sets; although other locations identify completed and analyzed sets, the Abstract intervention description and Key Points do not explicitly say that their numbers describe these later populations. B3: the choice changes randomized sample-size extraction by approximately 24%–27%. This is a quantity-to-population attribution discrepancy, rather than a synonym for the same analysis set.

**Alternatives and missing definition:** The shorter sections may intentionally describe randomized participants retained for intervention or primary analysis, using “randomized” to describe trial membership rather than the allocation-stage count. The body and flow diagram make that possible interpretation available. A human reviewer should determine whether these sections intend an allocation-stage count or a retained/analysis count and whether the population qualification should be made explicit. The 2 lost envelopes are separately accounted for and are not an additional finding.

**Exact human question:** Do the Abstract Interventions n=733/n=724 and Key Points 1508 denote allocated patients, completed-intervention patients, or primary-analysis patients, and which randomized sample sizes should be extracted from these sections?

### F-NUM-002

**Title:** The liberal-group TBI subgroup denominators do not sum to the all-patient denominator in Figure 4.

**Exact source locations and document roles:** REPORT DOC-001 [p.8 Figure 4, All patients, Moderate or severe TBI, and footnote a](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8). Related inventory: N046, N062. Values were checked against exact supplied-source layout text and the source-matched full-page render.

**Printed inputs:** Liberal All patients 121/724 (16.7%). Liberal AIS score<3:48/473 (10.1%); AIS score≥3:73/202 (36.1%). Restrictive corresponding rows 118/733,45/500 and 73/233. Footnote a states AIS range 0–6, defines<3 and≥3, and says only AIS codes for isolated brain injury were selected, excluding neck injuries.

**Rule and calculation:** The two printed score categories<3 and≥3 exhaust a numeric AIS score. Within the same figure, denominators 473+202=675 differ from all 724 by 49, while numerators 48+73=121 reproduce the all-patient event count. Restrictive denominators 500+233=733 and events 45+73=118 reconcile. Conservative half-unit input intervals give liberal subgroup-denominator sum[472.5+201.5,473.5+202.5]=[674,676]; all-patient interval[723.5,724.5]. The gap is 723.5−676=47.5; relative discrepancy 47.5/724=0.065608>0.05. Each individual printed percentage reconciles with its own numerator/denominator; the finding concerns the subgroup total.

**Focus area:** A, subgroup totals and analysis denominators.

**Proposed review domain:** statistical_results. Proposed relationship: S_W.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** Liberal primary-outcome denominator for the AIS<3 subgroup, denominator completeness for TBI subgroup analysis, and whether 49 all-patient participants are omitted from the subgroup distribution.

**Why context does not resolve it:** Route A category 3 applies to counts within one display. The caption does not state a missing/unknown-score subgroup or identify 49 excluded observations. Footnote selection of isolated brain-injury codes may explain a subgroup population restriction, but it does not quantify that restriction or explain why the two categories retain all 121 events while omitting 49 denominator observations.

**Alternatives and missing definition:** The smaller denominator may be intentional because AIS classification is unavailable or because neck-only injuries are excluded from this subgroup analysis. Alternatively, one printed subgroup denominator may refer to a different patient subset. The footnote concerns selection of injury codes and does not specify whether it excludes patients, codes, or unclassified records. No replacement denominator or preferred analysis is proposed.

**Exact human question:** Why do liberal AIS<3 and AIS≥3 denominators sum to 675 rather than 724 in Figure 4, and do the 49 omitted patients have missing/excluded AIS classifications or does one displayed denominator represent a different subgroup population?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p.4 Table, liberal site-of-inclusion percentages |451/758 gives 59.499% rather than 59.4%, and 307/758 gives 40.501% rather than 40.6%. Half-unit input intervals overlap both printed percentage intervals; relative gap zero. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p.4 Table, restrictive transport categories |78.0+18.7+3.2=99.9%, while category counts sum 747; independent one-decimal rounding accounts for the 0.1-point total. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p.8 Figure 4, ICU/lung-disease/ISS subgroup totals versus all-patient row |The subgroup event and denominator sums differ slightly from all patients. All half-unit gaps divided by respective all-patient values are≤0.05: ICU denominators 729/719, events 116/118; lung denominators 726/712, events 116/119; ISS denominators 732/718, events 117/119. TBI denominator discrepancy is separately emitted. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p.6 Figure 2 and p.8 Figure 4 effect estimates |Adjusted logistic ORs and displayed risk differences differ from crude odds ratios, risk ratios or differences computed from displayed counts. The stated regression/stratification/weighting framework does not require identity with crude quantities, and a crude reproducing method does not reproduce the rows. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 p.7 Figure 3 panel A versus panel B death events |Composite panel death-event totals 53/43 differ from standalone death totals 63/53. Composite first-event counting can retain respiratory-first patients only once;10 overlapping events per arm from the composite/components accounts for the totals, so these labels need not represent the same count. | CONTEXT_RESOLVES |
| REPORT DOC-001 p.7 Figure 3 panelsA/C risk arrays and p.6 Figure 2 denominators |Risk-array baselines 748/756 differ from complete binary-outcome denominators 733/724; risk counts differ across outcome panels at individual times. The figure is explicitly Kaplan–Meier, and individual time contributor comparisons do not establish a primary-result discrepancy without missingness/censoring definitions. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p.4 Table abbreviation versus p.1/p.5 ISS name |“Injury Severity Scale” versus “Injury Severity Score” denotes the same ISS quantity in immediate context and changes no displayed value. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 p.8 Discussion versus p.4 Table oxygen-duration summaries |“One-quarter of patients” above 50 minutes uses a quantile consistent with the observed duration summaries; applying it to every randomized/treated patient would require an unstated denominator assumption. No count for that proposition is printed. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p.6 major-protocol-violation sentence |Liberal 102 (13.7%) versus 102/758=13.456% assumes the received-strategy total is the adherence denominator, although the sentence does not print a denominator. Even that assumed comparison is within 0.05 relative discrepancy. | CONDITIONAL_OR_UNREPORTED |

## Limitations

No raw censoring times, event-bin boundary definition, pooled age distribution, or main-report denominators for adherence/guess/atelectasis percentages are supplied in this scope. These limit mechanical reconstruction but leave no assigned direct-source page unmapped. Source-role assignment is REPORT for all locations. Independent inclusion screening and evidence recheck remain subsequent stages.
# Numeric consistency supporting shard

Runtime agent: /root/numeric_support; named numeric role extension; run model gpt-6.1-sol; reasoning medium; FRESH_SPAWN. Status: COMPLETE. Exact disjoint scope: DOC-003 REPORT eFigure p.13 and all eTables1–11 pp.14–25. Scope comprises13 pages, one three-panel figure,11 tables on12 pages,42 stable relationship groups N201–N242,200 numerator/denominator/percentage cells, all continuous descriptive n/medians/IQR and all92 model estimate/interval sets for effect-measure identity. Inferential compatibility is assigned to the statistical reviewers; main-paper internal and cross-document relationships are separate. Six findings; seven excluded observations. No scientific-coverage limitation in the assigned numeric scope. Graphical curve readings are approximate and cannot establish unseen exact values.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Reused evidence is the current source-linked support map and hashed source renders, without old conclusions. All affected percentages were confirmed against direct source text and full-page render readings pp.14,15,20,24. eTable5 source p.18 was confirmed by fresh direct Poppler layout extraction. REPORT eMethods pp.9–12 were inspected directly for ICU and missing-data/model definitions. CPU, Poppler26.01.0; source extraction command and complete cells are recorded in relationships/numeric_support_inventory.md. Source and reused assets unchanged.

All findings use S_W and proposed domain statistical_results; there are no PLAN locations in this shard. Interval arithmetic permits±.5 for every printed integer count/denominator,±.05 for one-decimal percentages,±.5 for integer percentages and truncates negative numerator bounds at zero. No displayed result is replaced by a final correction.

### F-NUM-101

Receiving-center percentages in the Bern row do not reconcile with the printed pairs.

- **Exact source locations and roles:** REPORT DOC-003, source p.14, eTable1, Receiving trauma center, University Hospital Bern row, restrictive and liberal columns; both numerator/denominator and percentage are in that same row. [Source p.14](../../../joi240147supp2_prod_1738701765.29201.pdf#page=14).
- **Relationships:** N206; S_W.
- **Printed inputs:** restrictive50/750(7.2); liberal47/758(6.7). Column headers N750 and N758. Receiving-center counts sum750 and758, corroborating the displayed denominators.
- **Rule and calculation:** percentage=100×numerator/denominator. Restrictive point recomputation6.666667%, half-unit recomputed interval[6.595603,6.737825] versus printed[7.15,7.25]; gap.412175 percentage points, relative.0572465. Liberal point recomputation6.200528%, interval[6.130521,6.270627] versus printed[6.65,6.75]; gap.379373, relative.0566228. Both exceed.05. One finding consolidates the same receiving-center row pattern in both columns.
- **Focus area:** A, counts and denominators.
- **Proposed review domain:** statistical_results.
- **Qualifying route:** Route A, category 3.
- **Affected result or extracted value:** the percentage of each allocation group received at University Hospital Bern,7.2% and6.7%.
- **Why context does not resolve it:** this is the always-register category of count/denominator/percentage inconsistency within one display. The count-derived alternative does not remove the printed percentages a reader may extract.
- **Alternatives:** the percentages may use a different numerator/denominator, or one or more printed values may be displaced. No alternate denominator or population is disclosed for this row.
- **Exact human question:** Which Bern receiving-center numerator, denominator and percentage should be used for each allocation group, and what denominator generated the printed7.2% and6.7%?

### F-NUM-102

Liberal walk-in transport percentage differs substantially from its printed count pair.

- **Exact source locations and roles:** REPORT DOC-003, p.15, eTable2, Type of transport to the trauma center, Walk-in row, liberal column, both count pair and percentage. [Source p.15](../../../joi240147supp2_prod_1738701765.29201.pdf#page=15).
- **Relationships:** N209; S_W.
- **Printed inputs:**4/743(5.3), header liberal N758. The six liberal transport numerators sum743.
- **Rule and calculation:**100×4/743=.538358%; half-unit input interval[.470746,.606061] versus printed percentage[5.25,5.35]. Gap4.643939 percentage points; relative4.643939/5.3=.876215>.05.
- **Focus area:** A.
- **Proposed review domain:** statistical_results.
- **Qualifying route:** Route A, category 3.
- **Affected result or extracted value:** liberal walk-in transport prevalence, printed5.3%.
- **Why context does not resolve it:** route A category3 applies; reconstructing a count-derived percentage does not remove the displayed5.3% reading.
- **Alternatives:** a decimal may have been displaced in the percentage, or the numerator/denominator may represent another population. The immediate row and transport total disclose no such population.
- **Exact human question:** What liberal walk-in count, transport denominator and percentage should be extracted, and how was the printed5.3% obtained?

### F-NUM-103

The liberal vascular-surgery percentage is positive while the printed numerator is zero.

- **Exact source locations and roles:** REPORT DOC-003, p.15, eTable2, Surgery performed in the trauma resuscitation room, Vascular surgery row, liberal column. [Source p.15](../../../joi240147supp2_prod_1738701765.29201.pdf#page=15).
- **Relationships:** N212; S_W.
- **Printed inputs:**0/747(1.1).
- **Rule and calculation:**100×0/747=0%; permitting numerator[0,.5], denominator[746.5,747.5] produces[0,.066979]%. Printed1.1 gives[1.05,1.15]. Gap.983021 percentage points; relative.893655>.05.
- **Focus area:** A.
- **Proposed review domain:** statistical_results.
- **Qualifying route:** Route A, category 3.
- **Affected result or extracted value:** liberal vascular surgery count/prevalence, zero events versus printed1.1%.
- **Why context does not resolve it:** route A category3 applies even though zero-count arithmetic is evident; the printed positive percentage remains a different extracted quantity.
- **Alternatives:** the percentage may belong to another surgery row, or the count may not be the numerator used. The table supplies no alternate count or denominator.
- **Exact human question:** Was there any liberal-group vascular surgery during resuscitation, and which numerator/denominator/percentage is intended in this row?

### F-NUM-104

The liberal AIS<3 subgroup percentage does not reproduce from the printed numerator and denominator.

- **Exact source locations and roles:** REPORT DOC-003, p.20, eTable7, Moderate or severe traumatic brain injury, AIS<3 row, liberal column. [Source p.20](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20).
- **Relationships:** N228; S_W.
- **Printed inputs:**48/473(9.2). Adjacent liberal AIS≥3 is73/202(36.1); all-patient row121/724(16.7), retained as context without assuming no missing subgroup data.
- **Rule and calculation:**100×48/473=10.147992%; half-unit recomputed interval[10.031679,10.264550] versus printed[9.15,9.25]. Gap.781679 percentage points; relative.0849651>.05.
- **Focus area:** A.
- **Proposed review domain:** statistical_results.
- **Qualifying route:** Route A, category 3.
- **Affected result or extracted value:** primary-outcome event frequency in the liberal AIS<3 subgroup, printed9.2% versus count-derived approximately10.15%.
- **Why context does not resolve it:** route A category3 applies. The subgroup-total deficit does not supply a disclosed replacement denominator for this specific row.
- **Alternatives:** the denominator may be a displaced value, or the percentage may use another AIS population. A denominator near522 would yield approximately9.2%, but that is an alternative rather than a source-established correction.
- **Exact human question:** What numerator, denominator and percentage generated the liberal AIS<3 primary-outcome subgroup result?

### F-NUM-105

Both exclusion rows print allocation-population denominators beside percentages evidently computed across excluded patients.

- **Exact source locations and roles:** REPORT DOC-003, p.24, eTable10, Exclusion after randomization and Secondary exclusion rows, restrictive and liberal columns; compare each printed count pair with its adjacent percentage. [Source p.24](../../../joi240147supp2_prod_1738701765.29201.pdf#page=24).
- **Relationships:** N236,N237; S_W. This is one repeated denominator pattern across all four cells.
- **Printed inputs:** exclusion after randomization55/750(45),67/758(55), stated N130; secondary exclusion174/750(51),165/758(49), stated N341. Footnote states two secondary exclusions had missing allocation.
- **Rule and calculation:** using each displayed denominator:
  | Pair | Point recomputed percentage | Half-unit recomputed interval | Printed interval | Gap | Relative gap |
  |---|---:|---|---|---:|---:|
  |55/750(45)|7.333333|[7.261825,7.404937]|[44.5,45.5]|37.095063|.824335|
  |67/758(55)|8.839050|[8.767304,8.910891]|[54.5,55.5]|45.589109|.828893|
  |174/750(51)|23.200000|[23.117921,23.282188]|[50.5,51.5]|27.217812|.533683|
  |165/758(49)|21.767810|[21.687541,21.848185]|[48.5,49.5]|26.651815|.543915|
  All exceed.05. Alternative across-row arithmetic yields55/122=45.081967%,67/122=54.918033%,174/339=51.327434%,165/339=48.672566%, consistent with displayed integer percentages. This identifies an evident denominator pattern without selecting a replacement.
- **Focus area:** A.
- **Proposed review domain:** statistical_results.
- **Qualifying route:** Route A, category 3.
- **Affected result or extracted value:** excluded-patient frequencies: percentages of allocation populations versus allocation distribution among excluded patients, different quantities for extraction.
- **Why context does not resolve it:** route A category3 applies; title and across-row percentages suggest distribution, while the printed no./total no. pairs explicitly use750/758. The display supplies contradictory quantities even if the intended distribution is inferable.
- **Alternatives:** counts may be reported against the full allocation populations while percentages describe a separate distribution denominator, or the denominators may have been carried over from allocation headers. No dual-denominator convention is disclosed.
- **Exact human question:** Do the four percentages represent percentages within allocation populations or the restrictive/liberal distribution among exclusions, and what denominator belongs beside each count?

### F-NUM-106

The ICU-admission subgroup population cannot contain the displayed ICU-admission outcome counts under the reported allocation totals.

- **Exact source locations and roles:** REPORT DOC-003 p.18 eTable5 ICU admission row, restrictive and liberal count pairs; REPORT same document p.20 eTable7 ICU admission Yes and No rows and all-patient row; REPORT same document pp.9–10 exploratory definition elaborations do not disclose a distinct ICU admission time window for the subgroup. [Outcome source p.18](../../../joi240147supp2_prod_1738701765.29201.pdf#page=18), [Subgroup source p.20](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20).
- **Relationships:** N221,N227; S_W.
- **Printed inputs:** eTable5 ICU admission374/738(50.7),359/736(48.8). eTable7 ICU Yes denominators271 and238, No denominators458 and481; totals729 and719. Allocation totals750 and758. Subgroup primary events are74/271 and68/238.
- **Rule and calculation:** for two sets in the same allocation universe, ICU-admitted participants among subgroup-classified participants must be at least admitted count plus classified total minus allocation total. Restrictive point lower bound374+729−750=353, exceeding271 by82; liberal359+719−758=320, exceeding238 by82. Permitting all printed integer half-unit intervals, restrictive lower bound is at least373.5+(457.5+270.5)−750.5=351 versus displayed Yes interval[270.5,271.5], gap at least79.5, relative79.5/271=.293358. Liberal lower bound358.5+(480.5+237.5)−758.5=318 versus[237.5,238.5], gap at least79.5, relative79.5/238=.334034. Thus outcome/subgroup missingness alone cannot reconcile the populations. No crude/model comparison is involved.
- **Focus area:** A, same participant count/analysis population across report locations.
- **Proposed review domain:** statistical_results.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** primary-outcome subgroup analysis for patients admitted to ICU, specifically event frequencies74/271(27.3) and68/238(28.6) and the population to which the ICU subgroup OR applies.
- **Why context does not resolve it:** identical ICU-admission labels provide no distinguishing time window or eligibility criterion. Even assigning every participant absent from subgroup totals to ICU admissions leaves too many ICU-admitted participants for the printed Yes denominators. A reader cannot identify the intended ICU subgroup population or the denominator for subgroup extraction.
- **Alternatives:** eTable7 may define a narrower ICU exposure or time point not disclosed beside the result; one or more Yes/No counts may belong to another grouping; eTable5 or eTable7 may contain a displaced count. The report elaboration of ICU duration does not state a distinguishing admission criterion.
- **Exact human question:** Which ICU-admission definition and eligibility/time window generated eTable7, and how do its271/238 admitted-patient denominators reconcile with the374/359 ICU admissions and729/719 classified subgroup totals?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-003 p.14 eTable1 receiving Rigshospitalet and Odense, both allocation columns |335/750(44.4),348/758(45.7),173/750(22.9),177/758(23.2) leave half-unit interval gaps.120286,.064107,.034677,.019611 percentage points; relative gaps.002709,.001403,.001514,.000845, all at most.05. Consolidated one small display-discrepancy pattern. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p.15 eTable2 mechanism restrictive firearm denominator724 versus742 in other mechanism rows | Printed denominator intervals[723.5,724.5] and[741.5,742.5] leave gap17; relative17/742=.022911 at most.05. Percentage8/724(1.1) itself reconciles. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p.20 eTable7 liberal AIS subgroup denominator sum473+202=675 versus all-patient724 | The table does not assert complete AIS ascertainment; an apparent partition deficit alone depends on assuming no missing subgroup classification. The independently inconsistent48/473(9.2) pair is emitted as F-NUM-104. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-003 pp.17–18,20–22,25 eTables4–5,7–8,11 OR columns versus crude count ORs | Some printed ORs differ from crude count ratios; report p.12 describes inverse-probability weighting and GEE variance, and table labels do not state a crude estimate. No observed OR/RR identity substitution is established. Example primary crude OR(118×603)/(615×121)=.9562 versus first-model1.01. | MODEL_VERSUS_CRUDE |
| REPORT DOC-003 p.19 eTable6 median allocation summaries versus mean-difference columns | Initial surgery medians114−113=1 differ from MD10.3; source explicitly distinguishes median/IQR allocation summaries from mean-difference estimates, allowing different quantities. | CONTEXT_RESOLVES |
| REPORT DOC-003 p.24 eTable10 exclusion-after-randomization N130 versus55+67=122 | Count-sum interval[121,123] and printed total[129.5,130.5] give gap6.5;6.5/130=.05 exactly, screened by the required precision threshold. Secondary total174+165+2=341 reconciles and is not an excluded observation. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p.25 eTable11 missing-counted primary restrictive135//750(18.0) | Duplicated slash leaves numerator135,denominator750 and percentage18.0 unchanged. | NOTATION_OR_TYPOGRAPHY |

Counts:13 assigned pages;42 relationship groups;200 printed count/denominator/percentage cells checked;6 findings;7 excluded-observation rows. All observed inferential estimates retain source model labels; inferential tests are handed to the statistical lanes. No C IDs, dispositions, severity or validity labels assigned. Artifacts: relationships/numeric_support_inventory.md; checkers/numeric_support_part.md.

