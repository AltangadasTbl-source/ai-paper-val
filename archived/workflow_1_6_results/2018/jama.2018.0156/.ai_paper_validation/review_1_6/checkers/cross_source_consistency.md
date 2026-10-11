# Cross-source consistency review

Scope: every canonical main/support mapping group covering all 146 supplied PDF pages: DOC-001 pp 1–9 REPORT; DOC-002 pp 1–134 PLAN; DOC-003 pp 1–3 REPORT. Read all canonical maps and source inventory; no old candidate, adjudication, or report record used. No outside evidence. Current provider retained. This artifact owns draft keys XS01–XS15 only; these are not stable candidate IDs or adjudications. All remain pending human adjudication.

Tools: direct Poppler 25.03.0 `pdftotext -layout` confirmation of main pp 1–4, 6–7; results supplement pp 2–3; protocol pp 12, 65–66, 112–113. Other exact plan transcriptions use source-linked complete fresh maps and their documented visual confirmations, including image-only SAP p 130. Source maps and assets are unchanged. No Python, package installation, OCR execution or GPU used. Mandatory recheck must visually reconfirm every resulting stable ID against supplied PDF.

Matching checks distinguish patients versus procedures; randomized/ITT/PP/safety sets; assignment versus actual treatment; day 28 versus admission/ROSC; unadjusted versus center random-effects; risk difference versus OR; count versus seconds; one-decimal versus two-decimal displays. Absolute differences are percentage points even when printed with %. A corroborating location is not a further discrepancy relationship.

## Complete matched-family coverage

There are 47 matched relationship families below. A family may include many paired cells or repeated plan versions; counts do not impose a finding cap. Canonical maps retain every individual quantitative cell, so rows summarize complete checked groups, rather than sample cells.

| Family | Complete matched scope | Cross-source outcome |
|---|---|---|
| F01 | Main abstract/Key Points/flow:2043=1020+1023 | Agree |
| F02 | Main completed/ITT 2040=1018+1022, 3 ineligible exclusions; 99.8% | Agree after analysis-set match; 3 exclusions are explicitly identified |
| F03 | Randomized abstract female 665 versus ITT Table 1 female 664 | Different populations; no contradiction; one excluded woman is possible |
| F04 | Randomized mean age 64.7 versus Table 1 ITT means 65.7/63.8 | Weighted and rounded means align; no contradiction |
| F05 | Eligibility age 18+, all-randomized ITT wording versus excluded 2 nonarrest/1 minor | Defined eligibility exceptions, not a quantitative candidate from wording alone |
| F06 | Main 20 centers versus results eTable 1 full 21 rows | XS01 |
| F07 | Main 15 France/5 Belgium versus enrolled IDs 16, 17, 18, 20 Belgian and 17 other IDs | Same mismatch family XS01; mapping of final IDs is explicit in supplied roster/amendment |
| F08 | Main center 5 Saint Pierre versus plan 5 Beaujon/17 Saint Pierre | XS02 |
| F09 | Original 20-center plan versus amendment 25 | Disclosed change 20−1+6=25; no discrepancy solely from old/new versions |
| F10 | Later consolidated protocol 20 versus amendment 25 | XS15; both final bundle locations retained; ambiguity explicit |
| F11 | Planned 2000 versus realized 2043; 24 months versus 22 months | Target versus realized value; no candidate |
| F12 | Recruitment 100/center, 5/center/month, 24 months | XS13 |
| F13 | Enrollment Jan 2/end follow-up Jan 26, day 28 window | 24-day last-enrollment gap is not sufficient: last patient may have died before day 28; no supplied surviving-last-patient evidence |
| F14 | Day 28 primary and 28–35 day ascertainment across all sources | Agree; window is ascertainment timing, not later efficacy horizon |
| F15 | CPC≤2 and Table 2 primary counts 44/43, PP 43/40 | Agree; CPC 1+2 reconstructs primary numerators |
| F16 | Amended baseline-disability primary qualification versus report CPC≤2 | No supplied counted patient outside CPC≤2 or numerical reclassification; no candidate merely for omitted qualification |
| F17 | Primary orientation BMV−TI/ETI and margin−0.01/−1% | Agree across report/protocol/SAP |
| F18 | Original/later/SAP alternative hypotheses | XS06; positive versus negative alternative threshold |
| F19 | 95% two-sided planned versus 97.5% one-sided displayed lower CI | Equivalent lower-tail coverage; no candidate merely for sidedness labels |
| F20 | Primary ITT 44/1018, 43/1022, .11 pp, −1.64%, P=.11 across abstract/results | Agree; narrative inequality separately XS07 |
| F21 | Primary PP 43/995, 40/943, 4.3%/4.2%, .08 pp, −1.74%, P=.12 | Rounded primary difference and percentages agree |
| F22 | Hierarchical primary .05 pp/−1.70% versus unadjusted .11 pp/−1.64% | Explicit different model; no discrepancy |
| F23 | Power 956/group, .8, alpha.025, 5000 simulations, 2000 target, 3%/2% assumptions | All plan/report occurrences agree; target buffer 2000−1912=88 not arithmetic error |
| F24 | Hasegawa registry 649359 versus 650000; BMV 2.9% versus 3% | Explicit rounded assumption; agree at displayed precision |
| F25 | Same Hasegawa historical ETI 1.1% REPORT versus 1.0% PLAN | XS03; PLAN background retains PLAN role |
| F26 | Gueugniaud 2% and putative-placebo preservation 50% | Agree; 2% minus 1 pp=1% preserves 50% |
| F27 | Original interim 50%/75% versus SAP cancelled/no adjustment | Disclosed cancellation; no candidate |
| F28 | SAS 9.2 earlier plan versus 9.4 SAP/report | Updated software version; no inferential result conflict supplied |
| F29 | Table 1 complete baseline counts/continuous rows versus definitions | Population/unit/quantile labels align; no cross-document results table duplicate |
| F30 | Main ITT survival 55/54, 5.4%/5.3%, .1 pp, CI −1.8 to 2.1 repeated abstract/text/Table 2 | Agree |
| F31 | Main ITT admission 294/333, 28.9%/32.6%, −3.7 pp, CI −7.7 to .3 repeated | Agree |
| F32 | Main ITT ROSC 348/397, 34.2%/38.9%, −4.7 pp, CI −8.8 to −.5, P=.03 repeated | Agree; PP ETI % separately XS09 |
| F33 | Table 2 PP survival 54/995, 51/943, 5.4%/5.4%, printed .1 pp | XS11; wide CI not diagnosed without inference method |
| F34 | Table 2 PP CPC distribution versus 943 denominator and primary narrative | XS10 for 34(3.5); rest counts/sums and primary 4.2% agree |
| F35 | Table 2 PP admission 289/995, 312/943, 29.1%/33.1%, −4.0 pp, P=.055 | Counts/proportions/direction agree; no cross-source second inferential report |
| F36 | Table 2 PP ROSC 342/995, 377/943, 34.4%/30.0%, −5.6 pp | XS09 |
| F37 | Table 2 CPC block P=.68/.76 and CPC 3 alignment | P belongs whole block, not single CPC 3 row; no candidate from text alignment |
| F38 | Table 3/abstract/adverse narrative difficulty 186/1027, 134/996, 4.7 pp, CI 1.5–7.9, P=.004 | Exact repeated agreement |
| F39 | Table 3/abstract/adverse narrative failure 69/1028, 21/996, 4.6 pp, CI 2.8–6.4, P<.001 | Exact repeated agreement; different procedure-event denominator than ITT |
| F40 | Table 3/abstract/adverse narrative regurgitation 156/1027, 75/999, 7.7 pp, CI 4.9–10.4, P<.001 | Exact repeated agreement |
| F41 | VAS 20(5–55)mm, IDS 1(0–4), VAS 0–100, IDS>5, Han>2 across appendices and report | Units/bounds/thresholds agree; neurological-purpose statement XS14 |
| F42 | IDS/VAS collection from CRF day 28 versus measured prehospital | Collection/data abstraction can follow measurement; no numeric timing candidate without conflation evidence |
| F43 | Plan composite technique failure includes death/regurgitation versus reported procedural failure 6.7%/2.1% | Different named components/composite; not identical estimand; no candidate solely because composite omitted |
| F44 | All rate terms in secondary/safety tables and plans | Numerator/denominator explicitly patient proportions; no person-time or incidence-rate confusion |
| F45 | Center 5 CPR115=56+59, CCF 86%/87%, −1 pp, pauses 27/16, difference 11 seconds | CCF and subgroup totals agree; pause-unit XS08; 115 need not equal all center 5 patients 156 |
| F46 | Posthoc ECMO/donation exclusion 91 versus eTable denominators 971+978=1949 | 2040−1949=91; baseline 35+12+23+21=91; numerator decrease 87→82 possible; no cross-source mismatch |
| F47 | Posthoc 155 before ROSC reassignment, eTable 863/1174, 41/45 versus baseline 1018/1022, 44/43 | XS04 denominator, XS05 numerator; exclusion wording addressed as alternative; effect .9 pp agrees exact fractions |

Other PLAN-only mapped groups, including complete scales, blank forms and administrative-only units, were inspected through canonical complete maps. Bibliographic years/pages, document versions, contact numerals and administrative deadlines do not enter observed-trial matched-result claims. Historical 40/120=33%, 69/573=12%, N 10455=8487+1968 match. Main historical 91.8%/9.2% generates XS12 below. No supplied structured data or Office units exist. No display-zero P value was encountered in matched result families.

## Draft candidates

### XS01 — Twenty trial centers versus twenty-one contributing centers

Category: Cross-document numeric inconsistency. Compared locations: [main Methods p 2](../../../jama_jabre_2018_oi_180004.pdf#page=2), REPORT: 20 centers, 15 France and 5 Belgium; [eTable 1 p 2](../../../joi180004supp2_prod.pdf#page=2), REPORT: 21 distinct rows, IDs 1, 24, 5, 9, 12, 17, 13, 8, 3, 14, 22, 11, 15, 23, 16, 18, 20, 25, 7, 6, 2. Every row contributes at least one patient; ID 2 contributes 0 BMV and 3 ETI. All rows sum to 1018/1022, the main ITT totals. Rule: number of distinct contributing center IDs is 21, not 20; integer tolerance zero. Roster identifies four contributing Belgian IDs 16, 17, 18, 20 and seventeen other French IDs. Relationship: S_C only. The PLAN amendment's 25 authorized centers is contextual, because authorized and actually enrolling totals can differ. Alternative: administrative subcenters may count separately or main count may be stale. Human question: identify the final contributing-site roster and any center-ID aggregation.

### XS02 — Numeric center identifier 5 assigned inconsistent site

Category: Measure, label, or scale inconsistency. [Main Outcomes p 3](../../../jama_jabre_2018_oi_180004.pdf#page=3), REPORT, calls the monitored CPR site “Center No. 5: Saint Pierre”; [original roster p 47](../../../joi180004supp1_prod.pdf#page=47), PLAN, assigns 05 to Beaujon/Clichy; [roster p 49](../../../joi180004supp1_prod.pdf#page=49), PLAN, assigns 17 to Saint-Pierre/Brussels. This concerns the identity of the 115-patient numerical CPR subset. Rule: one trial center identifier cannot denote both sites without renumbering. Relationship: P_R. The disclosed amendment changes center 11's PI, adds 21–26, and removes 19; it does not disclose a 5/17 reassignment. Alternative: a separate monitoring-study numbering system. Human question: which site produced the 56 BMV/59 ETI CPR observations, and which numbering system does “5” denote?

### XS03 — Historical ETI favorable neurological survival 1.1% versus 1.0%

Category: Cross-document numeric inconsistency. [Main Discussion p 7](../../../jama_jabre_2018_oi_180004.pdf#page=7), REPORT: Hasegawa's Japanese registry of 649359 patients, ETI 1.1% versus BMV 2.9%. [Original background p 12](../../../joi180004supp1_prod.pdf#page=12), PLAN: same registry, 30-day favorable neurological survival BMV 2.9% among 367837 and ETI 1.0% among 41972. [Later background p 67](../../../joi180004supp1_prod.pdf#page=67), PLAN, repeats 1.0%. Main p 3 corroborates 1.1%, REPORT. Rule: same cited registry, airway strategies, favorable neurological endpoint and BMV 2.9% identify the background result; standard rounding to one decimal cannot turn one value into both 1.0 and 1.1. Relationship: P_R only; repeated PLAN agreement adds no P_P. Alignment limitation: main does not print the 41972 denominator or the 30-day horizon in this sentence. Alternative: another airway subgroup, adjustment, or horizon. Human question: which numerator, denominator, analysis and endpoint horizon underlie each value? No external source was accessed.

### XS04 — Before-ROSC reassignment does not conserve participants

Category: Denominator, proportion, or total inconsistency. [Main primary/flow p 4](../../../jama_jabre_2018_oi_180004.pdf#page=4), REPORT: ITT 1018/1022. [Main Methods pp 3–4](../../../jama_jabre_2018_oi_180004.pdf#page=3), REPORT: consider intubated-after-BMV/before-ROSC patients in ETI. [Posthoc narrative p 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), REPORT: 155 such patients. [eTable 2 p 3](../../../joi180004supp2_prod.pdf#page=3), REPORT: reassignment denominators 863/1174. Rule: transferring 155 predicts 1018−155=863 and 1022+155=1177, preserving 2040; printed 863+1174=2037. Relationship: S_C only. Main baseline totals and 155 establish the transfer expectation; they do not themselves form an additional discrepant within-main pair. Alternative: three exclusions, a changed starting population, or a denominator transcription. Main wording “after exclusion ... considered in the ETI group” is ambiguous, but identifies no three additional exclusions; the eTable says considered in ETI. Human question: supply complete starting, transferred and excluded participant counts, particularly the missing three. No correction presumed.

### XS05 — Before-ROSC reassignment does not conserve favorable survivors

Category: Numeric or arithmetic inconsistency. [Main primary p 4](../../../jama_jabre_2018_oi_180004.pdf#page=4), REPORT: 44/43 favorable survivors. [eTable 2 second row p 3](../../../joi180004supp2_prod.pdf#page=3), REPORT: 41/45 after reassignment. Rule: reclassification alone preserves 44+43=87, whereas 41+45=86; BMV loses three successes but ETI gains two. Relationship: S_C. Alternative: one favorable survivor excluded or recoded, or numerator transcription. This may share an accounting cause with XS04, but compares distinct printed numerator values. Human question: identify the missing favorable survivor and exact outcome/exclusion rule, confirming the same day 28 CPC≤2 endpoint. Integer tolerance zero.

### XS06 — SAP alternative threshold positive 0.01 versus negative 0.01

Category: Statistical reporting inconsistency. [SAP p 130](../../../joi180004supp1_prod.pdf#page=130), PLAN: H0 is πBVM−πTI≤−0.01 and H1 is πBVM−πTI≥0.01. [SAP p 133](../../../joi180004supp1_prod.pdf#page=133), PLAN: conclude noninferiority if lower CI >−0.01. [Earlier SAP p 121](../../../joi180004supp1_prod.pdf#page=121) and original/later protocol pp 36/90, PLAN: H1≥−0.01. Rule: +0.01 and −0.01 differ by 2 percentage points and define different alternatives for the identical contrast. Relationship: P_P only; main −1% merely corroborates. Inclusive boundary wording is preserved without a separate candidate. Alternative: omitted minus sign or an intended superiority alternative, neither disclosed. Human question: inspect signed SAP equation and intended hypothesis/decision rule. The mapper visually read p 130; mandatory recheck must repeat sign inspection.

### XS07 — Lower-limit comparison wording contradicts primary numbers

Category: Statistical reporting inconsistency. [Main Results p 4](../../../jama_jabre_2018_oi_180004.pdf#page=4), REPORT: lower bound −1.64%; “was greater than the threshold of noninferiority, thus noninferiority was not demonstrated.” [Main Methods p 3](../../../jama_jabre_2018_oi_180004.pdf#page=3), REPORT: threshold −1%, and acceptance requires a higher lower bound. Rule: −1.64<−1, not greater. Relationship: S_W only; PLAN agreement adds no P_R. Alternative: “greater” refers to deficit magnitude, which the signed criterion does not say. Human question: verify the intended signed relational word. The printed conclusion that noninferiority was not demonstrated agrees with the numbers.

### XS08 — Difference in count of pauses labeled seconds

Category: Measure, label, or scale inconsistency. [Main Outcomes p 3](../../../jama_jabre_2018_oi_180004.pdf#page=3), REPORT: number of pauses lasting >2 seconds. [Posthoc p 4](../../../jama_jabre_2018_oi_180004.pdf#page=4), REPORT: BMV 27 versus ETI 16 pauses; “difference, 11 seconds [95% CI, 7 to 15]”. Rule: 27−16=11 pauses; seconds is the event-duration threshold, not a count-difference unit. Relationship: S_W. PLAN duration endpoints are different from this explicitly posthoc count endpoint and add no P_R. Alternative: 27/16 are duration summaries, or the 11-second difference belongs to another result. Human question: confirm outcome, summary measure and CI units against the monitor-derived analysis.

### XS09 — PP ETI ROSC 30.0% does not match 377/943 or −5.6 percentage points

Category: Denominator, proportion, or total inconsistency. [Main Table 2 p 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), REPORT: PP ETI denominator 943, ROSC 377(30.0); BMV 342/995(34.4); difference −5.6. Rule: 100×377/943=39.9788%, rounding to 40.0%; exact arm difference −5.60693 points matches −5.6, while displayed 34.4−30.0=+4.4 reverses direction. Relationship: S_W only; ITT 38.9% is a different population. Alternative: different ETI denominator or percentage transcription; the percentage implies a denominator near 1257, not 943. Human question: verify numerator, denominator and intended percentage/population.

### XS10 — PP ETI CPC 1 percentage 3.5% versus 34/943

Category: Denominator, proportion, or total inconsistency. [Main Table 2 p 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), REPORT: PP ETI n 943, CPC 1=34(3.5%). Rule: 100×34/943=3.6055%, rounding to 3.6%, outside the printed 3.5 rounding interval [3.45, 3.55). CPC cells 34+6+7+4+892 sum to 943; primary 40/943 rounds 4.2%, agreeing with narrative. Relationship: S_W. Alternative: a distinct neurologically assessed denominator, not stated in this block. Human question: confirm denominator and percentage cell.

### XS11 — PP survival difference 0.1 points versus exact fraction difference

Category: Numeric or arithmetic inconsistency. [Main Table 2 p 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), REPORT: PP 54/995(5.4%) and 51/943(5.4%), difference 0.1 percentage points. Rule: 100×(54/995−51/943)=0.0188642 points, rounding to 0.0, not 0.1. Using displayed 5.4−5.4 also gives 0.0. Relationship: S_W. Alternative: an adjusted contrast or different denominator, not labeled in the table. Human question: verify unrounded effect, denominators and possible copying from ITT. Printed wide CI −10 to 9.7 remains for independent statistical assessment; this card relies only on arithmetic.

### XS12 — Historical 91.8% success implies 8.2%, not 9.2% complement

Category: Numeric or arithmetic inconsistency. [Main Discussion p 7](../../../jama_jabre_2018_oi_180004.pdf#page=7), REPORT: US historical trial 1941 participants, 1272 in cardiac arrest, success 91.8% after fewer than 3 attempts; “incidence of difficult intubation thus being 9.2%”. Rule: if difficulty is the complement implied by “thus, ” 100−91.8=8.2%; rounding cannot bridge the 1-point gap. Relationship: S_W. Alternative: difficulty includes another criterion or has another denominator, so is not the complement. Human question: confirm operational definition, population and denominator for both values from supplied evidence. No historical external article consulted.

### XS13 — PLAN recruitment 100 per center versus 5 per month for 24 months

Category: Numeric or arithmetic inconsistency. [Original summary p 10](../../../joi180004supp1_prod.pdf#page=10), [table p 24](../../../joi180004supp1_prod.pdf#page=24), [later summary pp 65–66](../../../joi180004supp1_prod.pdf#page=65), [table p 79](../../../joi180004supp1_prod.pdf#page=79), all PLAN: expected total 2000, 20 centers, 24 months, 100 per center, 5 per month per center. Rule under the labeled constant average: 5×24=120 per center and 5×24×20=2400, whereas 100/24=4.167 per month. Relationship: P_P only; realized enrollment is a different quantity. Alternative: 5 denotes capacity or only 20 active months, with 4 months of activation; no such active-period definition printed. Human question: confirm rate interpretation and active months. Conditional arithmetic question, not recruitment-feasibility judgment.

### XS14 — PLAN IDS/VAS described as neurological-function scales

Category: Measure, label, or scale inconsistency. [Original p 25](../../../joi180004supp1_prod.pdf#page=25) and [later p 80](../../../joi180004supp1_prod.pdf#page=80), PLAN, say IDS, VAS, mRS, CPC are used to assess neurological function at day 28. [Original p 24](../../../joi180004supp1_prod.pdf#page=24), [IDS appendix p 52](../../../joi180004supp1_prod.pdf#page=52), [VAS appendix p 53](../../../joi180004supp1_prod.pdf#page=53), PLAN, define IDS as intubation difficulty based on seven airway parameters and VAS 0–100 as mask-ventilation difficulty. Rule: explicit quantitative scale labels conflict with the collective neurological-purpose statement. Relationship: P_P only. Main Table 3 correctly labels median VAS 20 mm/IDS 1 as airway difficulty, merely corroborating. Alternative: the collective sentence intends neurological purpose only for mRS/CPC. Human question: verify the intended grammatical scope and outcome-scale labels; no claim actual airway scores were measured as neurological outcomes.

### XS15 — Later consolidated protocol retains 20 centers after amendment to 25

Category: Cross-document numeric inconsistency. [Later protocol p 65](../../../joi180004supp1_prod.pdf#page=65) and [p 72](../../../joi180004supp1_prod.pdf#page=72), PLAN, combined version V1.4 dated 22 September 2015/V2 dated 22 January 2016: 20 centers, 15 France/5 Belgium. [MS1 comparison p 112](../../../joi180004supp1_prod.pdf#page=112), PLAN, explicitly changes 20 to 25, removes Belgian 19 and adds French 21–26, yielding 21 France/4 Belgium authorized. Rule: contemporaneous later-version participating-center statements do not reflect the disclosed 20−1+6=25 amendment. Relationship: P_P only. Actual 21 enrolling centers need not equal 25 authorized, adding no S_C/P_R. Classification ambiguity: amendment separates roster from protocol to avoid future version changes; body 20 may be historical context. Human question: are later body counts current or historical, and which roster governs V1.4/V2? Candidate concerns printed numeric framing, not proof of a plan violation.

## Completion and limitations

All 146 source pages are covered through complete canonical maps; 47 matched families and all additional applicable PLAN internal definitions were checked. Fifteen draft observations emitted without stable IDs or AI judgments. Missing alignment definitions are named individually; exact visual source recheck remains mandatory. No CI engine, patient-level accounting or site renumbering was invented. Independent statistical review covers inferential compatibility beyond repeated-result identity. No supplied Office/structured-data source or scientific coverage gap is known. Source and reused assets remain unchanged.
