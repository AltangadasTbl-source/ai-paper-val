# Cross-source consistency review — Workflow 1.6

Complete scope: five supplied PDFs, 102 physical pages, main map M001–M120 and support map U001–U064 including all subrows, with both page-delimited PLAN and REPORT transcription parts. Document roles by content: DOC-001, DOC-004, DOC-005 are REPORT; DOC-002 and DOC-003 are PLAN. There are 49 matched semantic groups and 18 local candidate observations. No stable C IDs or AI adjudications are assigned; all observations are Pending Human Adjudication.

Engine: direct Poppler pdftotext 26.01.0 and the source-linked native/layout assets recorded by the mappers. Additional direct read commands were `pdftotext -layout -f 4 -l 4 jama_bot_2019_oi_190007.pdf -`, `pdftotext -layout -f 12 -l 12 joi190007supp3_prod.pdf -`, and `pdftotext -layout -f 5 -l 5 joi190007supp3_prod.pdf -`. No new extraction derivative, OCR, rendering, Python, web, GPU, legacy conclusion, or parallel checker output was used. Sources and reused assets were preserved. Direct source pages remain the authority for mechanical recheck.

## Complete matched-key coverage

The rows cover every mapped value and definition, with compound rows retaining all their subrows. Groups remain below the 120-relationship bound. No candidate count limit or sampling was applied.

| Group | Map keys and identity | Compared scope | Comparison result |
|---|---|---|---|
| XG01 | M001,M004,U001,U007: design and allocation | Main pp1–3,5–6; protocol pp8,15 | 2×2 and four countries agree. Planned1000/250 versus actual1025/257,256,256,256 is prospective versus actual, no candidate. |
| XG02 | M001,U008: recruitment dates | Main pp1–2; protocol p16 | Planned July2015–June2016 versus observed July2015–October2016 is an extension, not a falsely identical numerical result. |
| XG03 | M002,M018,M021,U005,U008,U021,U044: BMI screen | Main pp2–3; results supplement p3; protocol pp13,16,29 | Figure exclusion<15 versus online eligibility25–40: XC01. Strict>25 versus inclusive25 alone has no supplied boundary cases. |
| XG04 | M002,M019,U001,U008,U021,U023,U025,U044: other eligibility | Main pp1–3; results supplement p3; protocol pp8,16,29,31,33 | Age18–75,PHQ≥5 and six-month MDD window agree. Mailing18–65 is a recruitment subset. Psychiatric wording has no identified quantitative consequence. |
| XG05 | M003,U001,U011,U016–U018,U045: supplement doses | Main pp1–2; results supplement p4; protocol pp8,18,23–25 | 1.0g versus1.412g EPA+DHA: XC02. Micronutrient30/400/20/100 fits planned25–55/400–600/20/100–200. Two pills/day and one year agree. |
| XG06 | U013,U045,U046: laboratory composition | Results supplement pp4–5; protocol p20 | Shared-FAME EPA:DHA ratio4.65 versus declared3:1: XC03. No total daily mass reconstructed from FAME percentages. Laboratory67.9/14.6 meets planned minima65/10. |
| XG07 | U013,U045: placebo composition | Protocol p20; results supplement p4 | “Sunflower oil78(40%)” lacks an identifiable constituent/basis;57%linoleic/30%oleic is not a supported identical comparator. |
| XG08 | M006,U001,U002,U012,U047,U050: therapy schedule | Main p4; results supplement pp6,9; protocol pp8–9,19 | 21=15individual+6group,30/60minutes,one year agree. Single/double meetings do not imply a different session count. |
| XG09 | M009,M072,M113,U042,U049,U051,U055.a–i,U063: adherence | Main pp4,6,9; results supplement pp8–9,12,16,22; SAPp4 | ≥8/21 agrees;71.9/70.7 average71.3% supports71%. ≥70% versus >70%: XC04.515/666=77.33% supports77% multinutrient adherence; omega512/652=78.53% is distinct. Medians14 and0 agree. |
| XG10 | U019,U022: packages | Protocol pp26,30 | 13weeks versus initial4months recorded as an operational difference. No observed adherence denominator is tied to initial quantity, so no candidate under result-focused scope. |
| XG11 | M007,U001,U008,U020,U025,U026,U040: MDD endpoint | Main pp1,4; protocol pp8,16,28,33–34; SAPp2 | Cumulative12months and3/6/12 assessments agree; DSM-IV/DSM-5 labels: XC05. MINI5.0/5.01 alone could be patch notation. |
| XG12 | M008,U002,U020,U032,U040: IDS class | Protocol pp9,28,43; SAPp2; main pp4,8 | IDS primary versus secondary framing of numeric effects: XC06. Other outcomes reserved for later reports do not create omission candidates. |
| XG13 | M010,U009,U010: power calculation | Main p4; protocol pp16–17 | Planning inputs differ: XC07. PLAN25% versus30→15%: XC08. REPORT392 versus196×4: XC09. |
| XG14 | M005,M011,U021,U041,U043: randomized analysis | Main pp2,4; protocol p29; SAPpp2–5 | Site/history strata, ITT, effect coding, two-sided.05, MI100/MAR/Rubin agree. Protocol not specifying block8–12 is no conflict. |
| XG15 | M012,U032,U041,U042: logistic/Cox | Main p4/Table2; protocol p43; SAPpp3–4 | Logistic primary agrees with SAP. Cox primary/secondary/post hoc labels differ: XC10. |
| XG16 | M013–M015,U032,U033,U041–U043,U057–U063: model variants | Main pp4,6,8; results supplement pp18–22; protocol pp43–44; SAPpp3–5 | GEE versus robust T12, MI versus nonMI, CACE and modifier models distinguished. R satisfies planned SAS-or-R; STATA CACE is separate. No general-method candidate. |
| XG17 | M008,M066,U027,U048: symptom scales | Main pp4–5; results supplement p7; protocol p35 | PHQ0–27/cutoffs5,10;IDS0–84/cutoffs14,26;GAD0–21/cutoffs5,10 agree. Treatment MCIDs2–3/4–6 are not prevention effect estimates. |
| XG18 | M008,M067,U040,U048,U056,U059–U062: utility | Main pp4–5,7–8; results supplement pp7,17,20–21; SAPp2 | Higher is better; supplied positive graph data does not contradict printed0–1 scale. No external tariff critique. |
| XG19 | M008,U020,U027: TFEQ instrument | Main p4; protocol pp28,35 | Identifier18 versus item count21: XC11, conditional on scored versus administered questions. |
| XG20 | M068–M069,U027,U047,U051,U055.l: diet instrument | Main p5; results supplement pp6,12,16; protocol p35 | GA2LEN264 versus250 items: XC12. Ten groups versus eleven listed: XC13. Range0–77/eleven score components agrees. Advice targets differ legitimately from baseline medians. |
| XG21 | U002,U028,U029: blood volumes | Protocol pp9,36–37 | Summary35ml versus detail37ml: XC14; detailed sum37ml agrees. Excluding conditional DNA would yield31ml. |
| XG22 | U051,U055.o–r: blood availability | Results supplement pp12,16 | Subset upper331 versus paired335: XC15; lower211/1025=20.59% versus22%: XC16. Analyte/time/site populations need confirmation. |
| XG23 | U051,U055 footnote: kappa labels | Results supplement pp4,12,16 | .73/.70 component assignments reversed: XC17. |
| XG24 | M016,U003,U014,U037–U039: background | Main pp2,9; protocol pp10,21,52,56; SAPp1 | Overall17% versus sex-specific ranges differ in population; YLD second versus total burden third differ in metric/date. Historical6362/146538/54 is not trial N. |
| XG25 | M017–M023,U023,U025: participant flow | Main Figure1/p6; protocol recruitment diagram | 5965/2235/1773/1250/1025 agree; differences3730/462/523/225 reconcile. Exclusion reasons may overlap; exclusivity not assumed. PLAN diagram has no observed trial counts. |
| XG26 | M024–M036,M070,M074–M083: completion/dropout | Main pp1,3,6 | Available831/771/779 implies missing194/254/246.779/1025=76%. Loss246 versus dropout239 without preceding MDD has an explicit different definition. Per-arm reason sums agree. |
| XG27 | M037–M064,M109–M110: baseline repeats | Main abstract/Table1/p8 | Women772 agrees; weighted age46.5/BMI31.4 and PHQ7.3/7.5,GAD5.8/5.8 agree. Baseline PHQ below screening threshold is a different assessment. |
| XG28 | M038–M069: baseline labels | Main Table1/Methods | Sex/site/education totals, history subset, count/percentage units, activity h/day, BMI, drinks/week and diet-frequency labels checked. Repeated alcohol quartiles have no supplied contradictory observations. |
| XG29 | M073–M078,M085: MDD counts | Main pp1–2,6–7 | 25+26+32+22=105; marginals51/54/57/48 and percentages reconcile. Repeated wrong therapy arm for22 in footnoted: XC18. |
| XG30 | M079–M084: person-time/rates | Main Table2/p7 | 4656+4488=4503+4641=9144; rates51/4656,54/4488,57/4503,48/4641 per100months round1.1/1.2/1.3/1.0. Risk%, event count and rate distinguished. |
| XG31 | M075,M077,M078,M085: OR repeats | Main abstract/Table2/narrative | OR1.06/.93/.93 and all CI/P repeats agree. Reference labels and effect-code scale checked; transformations are unreported, so no candidate solely from that missing detail. Crude OR not substituted for adjusted MI results. |
| XG32 | M080,M082,M083,M085: HR repeats | Main Table2/narrative | HR1.05/.91/.91 and all CI/P repeats agree. Reference labels and effect-code scale checked; transformations are unreported, so no candidate solely from that missing detail. |
| XG33 | M086–M090,M071,U056: graphs | Main Figure2/narrative; results supplement p17 | Every outcome N vector agrees with missingness ranges29–32,206–211,275–278,268. Available data versus imputed analysis distinguished. Median/IQR/1.5IQR/dots/mean diamonds agree. Tick9 is not an assessment. |
| XG34 | M091,M100,U062: interaction range | Main pp7–8; results supplement p21 | Imputed P.41–.98 versus nonimputed.42–.96 are different analyses, no conflict. Graphs do not estimate adjusted interaction tests. |
| XG35 | M092,M102,M105,M108: PHQ supplement | Main Table3/p8 | Doubled displayed coefficients/intervals versus narrative .65(.25,1.06),.56(.11,1.01) reconcile using unrounded-value intervals. No false rounding candidate. |
| XG36 | M094,M102,M106: IDS supplement | Main Table3/p8 | .60(.15,1.05) doubled versus1.20(.29,2.10) is compatible with rounding. |
| XG37 | M096,M102,M107: GAD supplement | Main Table3/p8 | .25(.08,.42)×2=.50(.16,.84);same P.004. |
| XG38 | M097,M102,M104: GAD therapy | Main Table3/p8 | −.24(−.42,−.06)×2=−.48(−.84,−.12);same P.01. |
| XG39 | M093,M095,M098,M099,M103,M109,M110: remaining secondary | Main Table3/text/Figure2 | No repeated numerical conflict. Cohen D uses baseline/12month changes and pooled SD, distinct from adjusted ANCOVA; no forced conversion or near-zero IDS sign claim. |
| XG40 | M092–M101,U062.a–l: sensitivity variants | Main Table3; results supplement p21 | All16MI and24nonMI results checked. Imputation and interaction model differ; B/CI/SE/P differences are sensitivity variants. “Comparable” does not mean identical. |
| XG41 | M111,U057.a–i: PHQ modifier | Main p8; results supplement p18 | F-BA×baseline−.064CI−.118,−.01/P.020 supports direction/T12 label. Conditional main.288 is not the unmoderated−.17 estimand. Every covariate row checked. |
| XG42 | M111,U058.a–i: GAD modifier | Main p8; results supplement p19 | Supplements×baseline+.062CI.009,.115/P.022 supports direction/overall label. Conditional main−.107 differs legitimately from unmoderated+.25. Baseline GAD P0:DISPLAY_ZERO_NOT_CANDIDATE. |
| XG43 | M111,U059.a–m,U060.a–d,U061.a–d: utility modifier | Main p8; results supplement p20 | UK interaction+.017CI.001,.033/P.041;UK+.013 versus NL−.007 supports narrative. Conditional NL−.006 differs legitimately from pooled+.004. All21 result rows checked. |
| XG44 | M112,U053,U054,U063.a–h: CACE | Main p8; results supplement pp14–15,22 | Therapy OR.78(.64,.95) agrees; all eight result cells and stars matched. Generic ratio formula does not specify logistic scale; changed SEM versus logistic and unknown transformation preclude assuming1.06/compliance must equal.84. No candidate solely from missing details. |
| XG45 | M114,M115,U031,U052,U055.j–k: adverse events | Main pp1,8; results supplement pp13,16; protocol p40 | 24+24+26+24=98 hospitalized persons, one death in supplement+therapy agree. Persons differ from episodes; no rate/count confusion. General SAE definition does not prove other unreported events. |
| XG46 | M116,M117,U052,U064.a–c: concealment | Main p8; results supplement pp13,23 | 8.2/10.4/25.5/43.7% agree; N195/193/188/183 sums759;unknown307/759=40.45% rounds40.4%. P<.001 agrees; unspecified test not guessed. |
| XG47 | U026–U028,M007,M013: times | Protocol pp34–36; main pp4,7; results supplement pp12,17 | 3/6/12 outcome assessments agree;9month adherence/optional physical visit is distinct.24month online follow-up is outside reported12month window. |
| XG48 | M118–M120,U030,U034–U038: remaining context | Main pp9–11; protocol pp39,45–60 | Conclusions match one-year results;246/1025≈quarter lost. References, insurance and safety deadlines are not matching trial findings. All administrative/reference units inspected via maps/transcripts. |
| XG49 | DOC-005 complete page | Data-sharing p1; main p10 pointer | Administrative conditional access statement; no supplied structured dataset or quantitative outcome to compare. Complete no-applicable-result unit. |

## Candidate observations

### XC01 — Online BMI exclusion threshold

**Compared locations and roles:** [REPORT main Figure1 p3](../../../jama_bot_2019_oi_190007.pdf#page=3),1451 excluded for “BMI <15 or >40”; [REPORT results supplement p3](../../../joi190007supp3_prod.pdf#page=3),online eligibility BMI25–40. Main p2/protocol p16 corroborate25–40 without adding discrepancy edges. **Edge:** S_C between the two REPORT locations.

The same online screen carries lower thresholds15 and25, a10kg/m² label difference attached to1451 excluded persons. Actual screening code/count correctness is unknown. A broader first screen followed by telephone25 threshold is possible (Figure1 also lists18 BMI<25 exclusions), or the label could be a typo. **Human check:** compare the source figure and online eligibility paragraph; establish whether the online rule used15 or25 and whether1451 needs any change. Do not infer that ineligible persons were enrolled.

### XC02 — EPA+DHA daily dose

**Locations/roles:** [PLAN protocol p23](../../../joi190007supp1_prod.pdf#page=23),“EPA+DHA=1.0g per day”; [REPORT main p2](../../../jama_bot_2019_oi_190007.pdf#page=2) and [REPORT supplement p4](../../../joi190007supp3_prod.pdf#page=4),1412mg per day. PLAN pp8/18 describe one1000mg capsule. **Edges:** P_R from PLAN p23 to each REPORT; the reports agree.

1.0g=1000mg;1412−1000=412mg,41.2% above the stated dose. This is the same intended trial dose in a final-amendment protocol, not a planned-versus-actual participant quantity. A later formulation amendment or different capsule-content basis could explain it; p23 explicitly names EPA+DHA. **Human check:** establish the approved and delivered daily dose and amendment basis; clarify the differing descriptions without assuming a protocol violation.

### XC03 — EPA:DHA ratio versus laboratory composition

**Locations/roles:** [REPORT supplement p4](../../../joi190007supp3_prod.pdf#page=4),3:1; [REPORT supplement p5](../../../joi190007supp3_prod.pdf#page=5),EPA67.9 and DHA14.6g/100gFAME, described as contents tested and confirmed; [REPORT main p2](../../../jama_bot_2019_oi_190007.pdf#page=2),3:1. **Edges:** S_W supplement pp4/5; S_C main p2 versus supplement p5. PLAN minima are not contradictory.

Common-denominator ratio67.9/14.6=4.6507, not3. Absolute FAME-to-daily-dose conversion is unnecessary for this ratio, but the relation between FAME composition and declared parent-fatty-acid mass ratio needs confirmation. Nominal versus assay ratio, assay conversion, distinct lots, or a printed value may explain the difference. **Human check:** confirm analyte/basis/lot identity and compare ratios on a compatible mass basis. No total daily mass is inferred from percentages.

### XC04 — Adherence ≥70% versus more than70%

**Locations/roles:** [REPORT main methods p4](../../../jama_bot_2019_oi_190007.pdf#page=4),≥70%; [REPORT main results p6](../../../jama_bot_2019_oi_190007.pdf#page=6),77% took “more than70%”; [REPORT supplement pp12,16](../../../joi190007supp3_prod.pdf#page=16),≥70%; [PLAN SAPp4](../../../joi190007supp2_prod.pdf#page=4),at least70%. **Edges:** main strict> versus main≥ S_W; main strict> versus supplement≥ S_C; main strict> versus SAP≥ P_R. All ≥ locations agree with each other.

Exactly70% is included under≥ and excluded under>. Thus77% carries a different printed classification rule. Loose prose or no exact-boundary observations could leave the count unchanged. **Human check:** establish the implemented threshold and exact-boundary cases for77%; do not infer a count change without them.

### XC05 — MDD diagnostic criterion label

**Locations/roles:** [PLAN protocol endpoint p28](../../../joi190007supp1_prod.pdf#page=28),DSM-5/MINIV5.01; [PLAN summary p8](../../../joi190007supp1_prod.pdf#page=8) and [PLAN measurement table p34](../../../joi190007supp1_prod.pdf#page=34),DSM-IV; [REPORT main primary outcome p4](../../../jama_bot_2019_oi_190007.pdf#page=4),DSM-IV/MINI5.0 underlying105 onsets. **Edges:** P_P endpoint versus PLAN summary/table; P_R endpoint versus REPORT. Supplement screening p3 is context, not a separate endpoint edge.

The same12month endpoint has different diagnostic criterion labels. This is a measure-definition question for105 events, not evidence of changed diagnoses. A typo, retained older instrument label, or amendment may explain it. **Human check:** determine the actual diagnostic version used for105 events and authoritative endpoint definition; no clinical consequence is assumed.

### XC06 — IDS primary versus secondary

**Locations/roles:** [PLAN protocol pp9,28](../../../joi190007supp1_prod.pdf#page=28),IDS under main endpoints; [PLAN primary analysis p43](../../../joi190007supp1_prod.pdf#page=43),MDD/IDS; [PLAN SAPp2](../../../joi190007supp2_prod.pdf#page=2),IDS secondary; [REPORT main pp4,8](../../../jama_bot_2019_oi_190007.pdf#page=8),secondary/exploratory IDS results, including overall supplementB.60(.15–1.05),P.01. **Edges:** protocol primary versus SAP secondary P_P; protocol primary versus REPORT secondary P_R. SAP/REPORT agree.

The label changes the printed inferential framing of the same numeric IDS results. The SAP may have superseded the protocol hierarchy. **Human check:** establish the authoritative hierarchy/amendment and whether the primary/secondary and exploratory labels accurately describe IDS. No omitted outcome or broad study-design candidate is alleged.

### XC07 — Power-calculation inputs

**Locations/roles:** [PLAN protocol pp16–17](../../../joi190007supp1_prod.pdf#page=16),control30%,intervention15%,180/group,power90%,α.05,dropout20%,250/arm; [REPORT main p4](../../../jama_bot_2019_oi_190007.pdf#page=4),control30%,intervention20%,33% relative/10% absolute difference,392/196,power90%,α.05,attrition22%,250/combination. **Edge:** P_R.

The stated planning calculation differs in event probability15/20%,attrition20/22%,required size180/196. This does not compare expected with observed incidence or planned with recruited N. Different additive-interaction versus main-effect calculations, recalculation, or amendment may explain it. No unprovided power formula was reconstructed. **Human check:** identify the calculation and contrast actually used and which version each paragraph describes.

### XC08 — PLAN25% versus30→15%

**Location/role:** [PLAN protocol p16](../../../joi190007supp1_prod.pdf#page=16),“difference of25%”,control30%,intervention15%. **Edge:** P_P within this paragraph.

30−15=15percentage points and (30−15)/30=50% relative reduction; neither common meaning yields25%. “Difference” could refer to another factorial contrast. **Human check:** identify the denominator/contrast for25%; no replacement value is prescribed without that definition.

### XC09 — REPORT392 versus196 in each of four combinations

**Location/role:** [REPORT main p4](../../../jama_bot_2019_oi_190007.pdf#page=4),“392participants (196 in each of the4 possible intervention combinations)”. **Edge:** S_W. PLAN four-cell design only corroborates cell identity.

196×4=784, not392;392/4=98.392 could mean each main-effect condition aggregating two cells, or the parenthesis could be incorrect. **Human check:** identify the unit of392 and196 and the intended power target, distinct from actual1025 randomized.

### XC10 — Cox planned versus post hoc label

**Locations/roles:** [REPORT main p4](../../../jama_bot_2019_oi_190007.pdf#page=4),post hoc Cox analysis underlying Table2 HR1.05/.91/.91; [PLAN SAPp4](../../../joi190007supp2_prod.pdf#page=4),planned secondary time-to-MDD Cox/HR95%CI/P; [PLAN protocol p43](../../../joi190007supp1_prod.pdf#page=43),Cox under primary. **Edges:** REPORT post hoc versus each PLAN P_R; protocol primary versus SAP secondary P_P.

The same numeric HR analysis carries incompatible prespecification/priority labels. “Post hoc” could refer only to a particular censoring/model implementation; SAP timing and amendments matter. **Human check:** establish SAP date and exact planned/post hoc implementation, then clarify the framing. No inference that HR numbers themselves differ.

### XC11 — TFEQ-18 item count21

**Locations/roles:** [PLAN protocol p35](../../../joi190007supp1_prod.pdf#page=35),TFEQ-18 with item-count21; [PLAN endpoint list p28](../../../joi190007supp1_prod.pdf#page=28),TFEQ-18; [REPORT main p4](../../../jama_bot_2019_oi_190007.pdf#page=4),revised TEFQ-R18 with three0–100 factors. **Edges:** PLAN count21 versus identifier18 P_P; PLAN count/version versus REPORT measure identity P_R, conditional on18 denoting scored item count.

The instrument identifier and explicit item-count field differ, potentially affecting the reported factor-scale label.18 scored plus3 additional questions, expanded instrument, or typo could explain this. **Human check:** distinguish administered from scored items and specify any expanded version. No TFEQ effect estimate was invented; the residual question concerns the printed0–100 measure identity.

### XC12 — GA2LEN264 versus250 items

**Locations/roles:** [PLAN protocol p35](../../../joi190007supp1_prod.pdf#page=35),FFQ-GA2LEN264items; [REPORT supplement p12](../../../joi190007supp3_prod.pdf#page=12),250item GA2LEN deriving eleven-component0–77 diet score, with numeric baseline and change results. **Edge:** P_R.

The same named instrument has a14item count difference. Adapted questionnaire, food items versus all questions, or amendment could explain it. **Human check:** identify administered/scored version and count basis; no claim that the diet score is numerically wrong.

### XC13 — Ten diet groups versus eleven

**Locations/roles:** [REPORT supplement p6](../../../joi190007supp3_prod.pdf#page=6),“ten different food groups” followed by vegetables,fruit,fish,meat,pulses,whole grains,dairy,olive oil,processed food,soft drinks,alcohol; [REPORT supplement p12](../../../joi190007supp3_prod.pdf#page=12) and [REPORT main Table1 footnote p5](../../../jama_bot_2019_oi_190007.pdf#page=5),eleven components,0–77score. **Edges:** ten versus same-paragraph enumeration S_W; ten versus supplement eleven S_W; ten versus main eleven S_C, conditional on identical grouping.

Eleven separate groups are enumerated. Advice could combine processed food/soft drinks or group beverages differently from scoring. **Human check:** establish the grouping rule for advice versus score. Do not change0–77 scoring without its construction rule.

### XC14 — Blood summary35ml versus37ml

**Locations/roles:** [PLAN protocol p9](../../../joi190007supp1_prod.pdf#page=9),3×6ml+2×8.5ml; [PLAN schedule pp36–37](../../../joi190007supp1_prod.pdf#page=37),17+6+2+6+6=37ml at baseline6/12. **Edge:** P_P.

Summary18+17=35ml; detail37ml differs by2ml, matching hematology. Conditional DNA omission would give31ml, not35ml. A summary omission or different collection scope/site could explain it. **Human check:** identify collection scope and which hematology/DNA tubes apply. Actual collection amounts are unknown.

### XC15 — Blood upperN331 versus paired changeN335

**Locations/roles:** [REPORT supplement p12](../../../joi190007supp3_prod.pdf#page=12),baseline/12month subset n211–331 for selenium/folate/25OHvitaminD; [REPORT eAppendix8 p16](../../../joi190007supp3_prod.pdf#page=16),T12−T0 changes for those three analytes N335. **Edge:** S_W.

Paired changes needing both waves cannot exceed331 participants in either wave under the same stated subset;335>331 by4. A site-specific range, imputed changes, unpaired record count, or description error could explain it. **Human check:** establish analyte-specific baseline/T12/paired/imputed Ns and population; EPA334 is a distinct analyte and not assumed to share this assay population.

### XC16 — Blood211 versus22%

**Locations/roles:** [REPORT supplement p12](../../../joi190007supp3_prod.pdf#page=12),“n=211to331,22–32%”; [REPORT main pp1,3](../../../jama_bot_2019_oi_190007.pdf#page=3),randomized1025. **Edges:** S_C conditional on full randomized denominator; S_W within the printed numerator/percentage pair once denominator is identified.

211/1025×100=20.585%,round21%,not22%;331/1025=32.293%,round32%. A subgroup denominator or nonmatching range endpoints could explain it. **Human check:** specify denominator and endpoint mapping for22–32%; no definitive percentage correction without these inputs.

### XC17 — Kappa component assignments

**Locations/roles:** [REPORT supplement p4](../../../joi190007supp3_prod.pdf#page=4),supplement1=omega3/supplement2=micronutrient; [REPORT methods p12](../../../joi190007supp3_prod.pdf#page=12),kappa.73/.70 for1/2,respectively; [REPORT table footnote p16](../../../joi190007supp3_prod.pdf#page=16),multinutrient=.73/omega=.70. **Edge:** S_W pp12/16; p4 corroborates identity.

Methods imply omega=.73 and micronutrient=.70, opposite the footnote assignments. “Multinutrient” might mean combined pills instead of the micronutrient pill, or labels/“respectively” could be reversed. **Human check:** verify the two contingency-table kappas and component labels.

### XC18 — Twenty-two events mislabeled in Table2 footnote

**Locations/roles:** [REPORT main Table2 footnoted p6](../../../jama_bot_2019_oi_190007.pdf#page=6),32/256(12.5%) without therapy and22/256(8.6%) “without therapy”; [REPORT abstract p1](../../../jama_bot_2019_oi_190007.pdf#page=1) and [REPORT footnotef p6](../../../jama_bot_2019_oi_190007.pdf#page=6),22 with therapy. **Edges:** S_W; no PLAN discrepancy.

The same256-person arm cannot represent both separately reported32 and22 counts in the four-arm decomposition. An arm-label transcription defect may explain it. **Human check:** inspect footnoted and the arm-event listing; confirm intended with-therapy label without assuming changed event counts.

## Limits and noncandidate rules

No supplied individual-level/structured results file exists. OR and HR may already represent full contrasts despite effect coding; the package does not establish an unrescaled exponentiation rule. No candidate was emitted solely from unknown expβ versus exp2β transformation. Exact model transformations, boundary cases, blood-pair populations, amendments and questionnaire adaptations need human clarification where named; these limitations do not represent omitted source coverage. Boxplots lack printed numeric point values, so population/time/summary type was matched without inventing precision or inferring significance.

Actual versus planned N and recruitment duration; expected versus observed incidence; MI versus nonMI sensitivity results; conditional versus marginal coefficients; baseline versus screening PHQ; and other unreported analyses were not registered as inconsistencies. The generic CACE ratio explanation does not alone justify a logistic OR discrepancy without its link-scale/model/reference definition. Missing RERI or standardized-effect CI/P fields were not omission candidates. The GAD baseline P=0 is DISPLAY_ZERO_NOT_CANDIDATE.

Every compared location in the candidate cards has its content role and an exact local PDF link. Conditional comparisons preserve the unresolved definition and supported alternative instead of inferring a violation. All18 observations remain Pending Human Adjudication.
