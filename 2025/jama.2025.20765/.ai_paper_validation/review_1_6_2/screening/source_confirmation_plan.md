# Source confirmation of assigned plan pages

Runtime ID: 01a12c50-f19c-7ce1-aab5-f9cdca5b913f. Task: optional source-confirmation shard supporting the independent inclusion screen. Model: gpt-6.1-sol. Reasoning effort: high. Status: COMPLETE for the fourteen assigned pages. This handoff records source facts only. It assigns no candidate IDs, screening decisions, evidence states or human dispositions, and does not replace the later stable-candidate mechanical recheck.

Exact scope: DOC-002, `joi250093supp1_prod_1768590553.08963.pdf`, PDF pages 8, 9, 11, 13, 16, 28, 49, 51, 53, 99, 101, 103, 104 and 109. Each assigned page was opened visually. All fourteen locations are PLAN by content: prospective protocol specifications, a SAP table shell, or a prospective intervention-message schedule. Their presence in a supplement does not change that role.

The complete scope and review contract, current tooling record, direct-source inventory and relevant current checker findings were read. Current source-linked renders were used where already available; reusable page JPEGs were used for pages without a current render. These images are transcription aids for the exact supplied PDF, which remains authoritative. No OCR or new rendering was performed, no source or reused artifact was modified, and no legacy scientific conclusion or external source was used. The tooling record identifies GPU_USER_REQUESTED for approved targeted OCR elsewhere in this run and CPU rendering; neither processing operation was needed in this shard.

Direct `sha256sum` reconfirmed the supplied PLAN PDF identity as `0dcbfdf53363088fa65146d05d2f0e58b9c9f2fa001c9d60232207bbdec440a1`, matching `source_hashes_before.sha256`.

## Page and image ledger

Paths in this table are package-relative locators, not independent scientific sources. Current renders use the bundled `pdf_tools.py` with PyMuPDF 1.26.4 on the CPU; cross-source checker renders are 160 dpi. The p.13 render is 200 dpi. The numeric checker records direct-source rendering of p.16. Reusable JPEGs are the source-linked 180 dpi page images catalogued by the asset curator, with the historical rendering engine unrecorded.

| PDF page | Image opened | Assigned finding references | Source location found |
|---|---|---|---|
| 8 | `.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/page_images/page-008.jpg` | F-XS-007 | Primary endpoint, printed lines 153–164; footer 8 |
| 9 | `.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/page_images/page-009.jpg` | F-XS-009 | Secondary endpoint definitions, lines 172–187; footer 9 |
| 11 | `.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/page_images/page-011.jpg` | F-XS-008 | Participant inclusion/exclusion lists, lines 235–255; footer 11 |
| 13 | `.ai_paper_validation/review_1_6_2/preprocessing/support001_p013.png` | F-ST1-007 | Section 6, lines 304–312; footer 13 |
| 16 | `.ai_paper_validation/review_1_6_2/preprocessing/numeric_support_plan_p16.png` | F-NUM-104 | Intervention dose paragraph, lines 381–390; footer 16 |
| 28 | `.ai_paper_validation/review_1_6_2/preprocessing/cross_plan_28.png` | F-XS-001, F-XS-002, F-ST1-003, F-ST1-004 | Section 11.2.2, lines 759–764; footer 28 |
| 49 | `.ai_paper_validation/review_1_6_2/preprocessing/cross_plan_49.png` | F-XS-008 | Sections 21.3.2 and 21.4.2, lines 1375–1395; component footer 8 |
| 51 | `.ai_paper_validation/review_1_6_2/preprocessing/cross_plan_51.png` | F-ST1-007 | Section 23, lines 1445–1453; component footer 10 |
| 53 | `.ai_paper_validation/review_1_6_2/preprocessing/cross_plan_53.png` | F-NUM-104, F-XS-005 | Intervention dose paragraph, lines 1521–1532; component footer 12 |
| 99 | `.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/page_images/page-099.jpg` | F-XS-004, F-ST1-006 | Continued subgroup shell, gender rows; component footer 22 |
| 101 | `.ai_paper_validation/review_1_6_2/preprocessing/cross_plan_101.png` | F-XS-006 | SMS-log heading, enrollment block, message 6 and footnotes; component footer 1 |
| 103 | `.ai_paper_validation/review_1_6_2/preprocessing/cross_plan_103.png` | F-XS-006 | Q(-1)/Tx(+8), messages 34–38, quit-day transition; component footer 3 |
| 104 | `.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/page_images/page-104.jpg` | F-XS-006 | Continued quit-day block, messages 39–44; component footer 4 |
| 109 | `.ai_paper_validation/review_1_6_2/preprocessing/cross_plan_109.png` | F-XS-006 | Messages 129–134 and follow-up phase; component footer 9 |

## PDF page 8: primary endpoint and cotinine criterion

[Supplied PDF page 8](../../../joi250093supp1_prod_1768590553.08963.pdf#page=8). PLAN protocol, section 2.2.1, printed lines 153–164. A running header explicitly reads `QUIT4TB Trial` and `V6.0 07.03.25`. This header is a direct observation even though the checker describes this passage as an earlier protocol occurrence.

Lines 154–157 state: “The primary endpoint will be biochemically verified continuous abstinence at 6 months post randomisation.” They continue: “Abstinence is defined as self-report of not having used more than 5 cigarettes, bidis, water pipe sessions since the quit date, verified biochemically by a breath carbon monoxide (CO) reading of less than 10 ppm at month 6.”

Lines 158–161 state: “In case of concomitant smokeless tobacco use, biochemical verification will be carried out using Accutest® NicAlertTM strips to detect cotinine (a nicotine metabolite) level in urine samples. Reading of the strip will indicate a cotinine level (0-6), where level <3 (i.e., equivalent to 100-200ng/mL cotinine) will be considered tobacco abstinence.”

Lines 162–164 state that elevated CO “>10ppm” and cotinine indicating active tobacco use supersede self-reported abstinence and define the patient as a tobacco user. The same page begins the secondary-endpoint list, including seven-day point abstinence assessed at week 9 and month 6 and TB treatment adherence from treatment support cards.

F-XS-007 transcription facts: named strip assay, 0–6 scale, level <3 and the printed 100–200 ng/mL expression are all visible. The spacing and trademark glyphs differ from the checker's normalized wording, but the numerical criterion is as transcribed. The page supplies no cassette concentration crosswalk, assay substitution statement or amendment disclosure. No passage is clipped here. Determining equivalence to the reported cassette requires the separately assigned report and later plan passages; this shard supplies no assay-equivalence inference.

## PDF page 9: treatment-failure definition and trial phases

[Supplied PDF page 9](../../../joi250093supp1_prod_1768590553.08963.pdf#page=9). PLAN protocol, continued section 2.2.2, printed lines 172–187; component footer 9. There is no version header on this page itself.

Lines 172–174 state that treatment success includes cured and completed treatment, and that treatment success, treatment failure, default and death will be recorded from TB register TB03 at month 6. Lines 179–180 define: “Treatment failure: ‘A patient who was initially smear-positive and who remained smear-positive at month 5 or later during treatment’”.

Immediate neighboring definitions are cure with a negative smear at month 6 and at least one previous occasion; completed treatment at month 6 without meeting cure or failure criteria; default as interruption for two consecutive months or more; death from any cause during treatment; and relapse after previous cure or completion.

Section 3, lines 189–197, describes four phases: Phase 1 PPI consultation, Phase 2 pilot, Phase 3 superiority comparing mTB-Tobacco with usual care, and Phase 4 noninferiority comparing mTB-Tobacco with face-to-face behavioral support. Phase 3 and Phase 4 each have six months of recruitment plus six months of follow-up.

F-XS-009 transcription fact: “month 5 or later” is printed, and the checker matches that passage. This page contains no amendment disclosure or statement that it supersedes another definition. The amendment and SAP comparison require the other assigned review scopes. All relevant lines are readable without clipping.

## PDF page 11: full participant eligibility lists

[Supplied PDF page 11](../../../joi250093supp1_prod_1768590553.08963.pdf#page=11). PLAN protocol, sections 4.3.2 and 4.4.2, printed lines 235–255; component footer 11. No version header appears on this page itself.

The introduction says patients must fulfill all inclusion criteria and none of the exclusion criteria. The six inclusion bullets are:

- “Age at least 15 years (counted as adult TB patients in Bangladesh and Pakistan)”;
- “Willing and able to provide written informed consent”;
- “Diagnosed with drug sensitive PTB (smear positive or negative) in the last four weeks”;
- “Currently smokes tobacco on a daily basis or have only stopped or reduced smoking (less than daily) since diagnosed with TB”;
- “Willing to quit tobacco use”;
- “Access to personal mobile phone”.

The four participant exclusion bullets are age below 15; retreatment TB, MDR TB, miliary or extrapulmonary TB; current pharmacotherapy for tobacco dependence; and unwillingness or inability to provide written informed consent. The paragraph preceding those bullets says people anticipated to have adverse effects from study treatment or research burden will be excluded. Above the participant list, facility conditions cover a nominated focal person, adequate staff/facilities, and administrative participation.

F-XS-008 transcription facts: the recent cessation/reduction exception and personal-phone requirement are present. Neither a patient/household SMS-reader criterion nor a ≥25 smoking-days criterion appears anywhere in the full lists on this page. This is a statement about the visible lists, not proof about every operational eligibility document. The page supplies no explicit eligibility amendment. The lists are fully visible and not clipped.

## PDF page 13: allocation procedure, source clipping and version header

[Supplied PDF page 13](../../../joi250093supp1_prod_1768590553.08963.pdf#page=13). PLAN protocol, section 6, printed lines 304–312; footer 13. Running header: `QUIT4TB Trial`, `V6.0 07.03.25`.

Lines 305–310 state that interventions are delivered at group level, health facilities are clusters, and facilities “would be randomised 2:2:1 to mTB-Tobacco (intervention A), face-to-face (intervention B), or standard care (intervention C).” An independent University of Edinburgh statistician blinded to centres will use computer-generated random-number lists. Lines 310–312 state: “The allocation will be based on using minimisation to ensure balance across the groups on the average number of TB patients seen per month and geographical location (Bangladesh and Pakistan).”

Immediate preceding content covers participant withdrawal, retaining already collected data/samples, and placeholder text for early stopping/discontinuation procedures. Below the allocation paragraph, the figure prints total Phases 2–4 recruitment of 2,384 at 37 patients/site and Phase 3 total 24 sites, with 888 + 16 pilot = 904 patients.

F-ST1-007 transcription facts: both monthly TB-volume and geographical-location factors are present, and the checker matches them. The allocation paragraph also explicitly names three arms in a 2:2:1 ratio, rather than solely the two-arm Phase 3 contrast. The immediate context must retain that distinction when matching this passage to the report. There is no explicit amendment disclosure in this paragraph.

The lower recruitment diagram is visibly cut by the bottom edge of the source page; the current direct-source render confirms that clipping. The affected allocation text is completely visible. No hidden diagram values were reconstructed. The header-version fact is retained independently of the bundle's earlier/later component descriptors.

## PDF page 16: 178 messages and dose schedule

[Supplied PDF page 16](../../../joi250093supp1_prod_1768590553.08963.pdf#page=16). PLAN intervention specification, printed lines 378–400; footer 16. No version header appears on this page itself.

Lines 378–380 say that after piloting and before continuing to the superiority trial the programme will undergo a refinement process/study pause and make intervention adjustments if needed. Lines 381–386 describe a set of translated messages, a transmission schedule, an automated digital platform, a supervision team and storage only of a unique trial ID.

Lines 386–390 state: “Each participant in the intervention group will receive a total of 178 SMS messages over a period of 6 months. In the first two months, the frequency of messages would be 4 to 5 messages per day, in next two month the frequency would reduce to 2 to 3 messages per day and in the last two months there will be 1 to 2 messages sent per week.”

The following paragraph describes REDCap screening, consent, recording phone contacts, sending messages “as per the schedule”, and no SMS in the control arm. A separate vendor/data-handling paragraph and the face-to-face intervention heading follow.

F-NUM-104 transcription facts: total 178, total duration six months, three consecutive two-month segments, 4–5/day, 2–3/day and 1–2/week all match the visible source. This page does not define 178 as unique templates rather than participant transmissions; the sentence specifically begins “Each participant ... will receive”. The preceding paragraph explicitly allows refinement after piloting, but this page does not give a revised total or schedule or reconcile them. Calendar-month duration and a detailed send log are not defined here. All quoted dose text is visible without clipping. No arithmetic result or inclusion decision is assigned by this shard.

## PDF page 28: statistical model and missingness architecture

[Supplied PDF page 28](../../../joi250093supp1_prod_1768590553.08963.pdf#page=28). PLAN protocol, section 11.2.2, printed lines 759–764; footer 28. Running header: `QUIT4TB Trial`, `V6.0 07.03.25`.

The complete paragraph states: “Outcomes will be primarily analysed in a missing-at-random architecture by fitting generalised linear mixed models using a log link and assuming an underlying Poisson distribution with clusters treated as a random effect. All analyses will account for clustering through the random intercept model. The crude and adjusted relative risks (RRs) and corresponding 95% CIs will be estimated.”

Immediate preceding lines 751–758 concern the economic analysis: cost per QALY ICER, complete cases with complete costs/QALYs at all time points, and pattern-mixture sensitivity analyses for multiple imputation. The quoted paragraph has its own “Statistical analysis” heading. The next section covers urine collection and nicotine dipstick testing among participants using other tobacco forms; the page then begins translation procedures.

F-XS-001/F-ST1-003 source facts: log link, Poisson distribution, cluster random effect, random intercept and crude/adjusted RRs with 95% CIs are printed. F-XS-002/F-ST1-004 source facts: “Outcomes will be primarily analysed in a missing-at-random architecture” is printed. All these transcriptions match the cited lines. The statement does not explicitly restrict MAR to costs, QALYs or covariates, and does not name a dropout=smoker rule in this paragraph. Its adjacency to economic text and separate section heading are both direct contextual facts; which analysis the authors intended is a separate interpretive question. No model amendment or supersession statement appears here, and nothing is clipped.

## PDF page 49: later-component eligibility lists

[Supplied PDF page 49](../../../joi250093supp1_prod_1768590553.08963.pdf#page=49). PLAN protocol, sections 21.3.2 and 21.4.2, printed lines 1375–1395; the printed component footer is 8, not PDF page 49. There is no running version header on this page itself.

The six participant inclusion bullets read as on PDF page 11: at least 15 years, written consent, drug-sensitive PTB diagnosed in the last four weeks, daily smoking or stopping/reducing below daily since diagnosis, willingness to quit, and personal mobile phone access. Lines 1382–1383 specifically state: “Currently smokes tobacco on a daily basis or have only stopped or reduced smoking (less than daily) since diagnosed with TB”. Line 1385 states: “Access to personal mobile phone”.

The four exclusion bullets, lines 1392–1395, are age below 15; retreatment TB, MDR TB, miliary or extrapulmonary TB; current tobacco-dependence pharmacotherapy; and unwillingness/inability to provide written informed consent. The introductory exclusion paragraph refers to anticipated adverse effects from treatment or research burden. The top of the page contains facility eligibility, including at least 50 new TB patients/month, approved functioning centres, focal staff and facilities.

F-XS-008 transcription facts: the full list matches the checker's clinical items, including the recent-stop/reduction exception. No ≥25 smoking-days or SMS-reading-access condition appears on this page. The page has no explicit eligibility-change disclosure. Lists are fully readable, including the final exclusion bullet near the lower margin.

## PDF page 51: later allocation statement and adjacent flow diagram

[Supplied PDF page 51](../../../joi250093supp1_prod_1768590553.08963.pdf#page=51). PLAN protocol, section 23, printed lines 1445–1453; component footer 10. No version header appears on this page itself.

Lines 1446–1451 describe clustered facilities “randomised 2:2:1 to mTB-Tobacco (intervention A), face-to-face (intervention B), or standard care (Control)”, with an independent University of Edinburgh statistician blinded to centres and computer-generated random-number lists. Lines 1451–1453 state: “The allocation will be based on using minimisation to ensure balance across the groups on the average number of TB patients seen per month and geographical location (Bangladesh and Pakistan).”

F-ST1-007 transcription facts: monthly TB-volume and country factors match the finding. The same paragraph retains the broader three-arm 2:2:1 statement. Immediately below it, however, the Phase 3 superiority diagram shows 27 sites, 1080 + 16 pilot = 1096 participants, mHealth 10 Bangladesh + 8 Pakistan sites and control 5 Bangladesh + 4 Pakistan sites, with 40 participants/site. Thus the diagram specifies 18:9 Phase 3 sites. A later box shows Phase 4 noninferiority with 36 sites and 1620 participants. These are contextual printed facts, not a separate observation selected by this shard.

The top diagram box prints 2,716 patients across Phases 2–4. Lower country boxes are cut at the bottom source-page edge; the allocation paragraph, Phase 3 arm boxes and Phase 4 total box are visible. The page has no explicit minimization-change or omission disclosure. Whether a shorter report description includes the planned factor is not established by this plan page alone.

## PDF page 53: 134 messages, revised frequencies and pilot refinement

[Supplied PDF page 53](../../../joi250093supp1_prod_1768590553.08963.pdf#page=53). PLAN intervention specification, printed lines 1506–1542; component footer 12. No version header appears on this page itself.

Lines 1506–1517 describe a 16-patient pilot, eight per country, testing message clarity, quantity, timing/frequency and users' engagement. The pilot is embedded in the superiority trial, with pilot data treated under the same processes and governance as main-trial data. Lines 1518–1520 explicitly say the programme will undergo refinement/study pause after piloting and before continuing to the superiority trial, with intervention adjustments if needed.

Lines 1521–1526 describe the translated message set, transmission schedule, automated platform, supervision team and unique-ID storage. Lines 1526–1530 state: “Each participant in the intervention group will receive a total of 134 SMS messages over a period of 6 months. In the first two months, the frequency of messages would be 4 to 5 messages per day, in next two month the frequency would reduce to 1 to 2 messages per day and in the last two months there will be 1 message sent per week.” Lines 1530–1532 add Phase 3 education leaflets from TB health professionals. The following paragraph describes REDCap, sending messages “as per the schedule” and no SMS for controls.

F-NUM-104/F-XS-005 transcription facts: 134, six months, first two months 4–5/day, next two months 1–2/day and final two months one/week are printed exactly as summarized. The paragraph labels the total as what each participant receives and does not define it as unique templates. Immediate pilot-refinement language is explicit; it does not state on this page which revised numeric schedule supersedes the printed one. No calendar-month convention, branch-selection rule or actual send log is supplied here. The dose paragraph is completely visible without clipping. This shard makes no inclusion or arithmetic conclusion.

## PDF page 99: gender subgroup shell

[Supplied PDF page 99](../../../joi250093supp1_prod_1768590553.08963.pdf#page=99). PLAN SAP table continuation; component footer 22. The page has no version/date header and no repeated table title or column header.

The visible shell contains the final education row “More than Primary (classes >6)”, occupation rows “Active in Job/Business” and “Dependents and retired”, a “Gender” block with “Male” and “Female” rows, and a “Smoking Duration” block with “<24 Years” and “>24 Years” rows. All numerical cells are blank. Printed lines 3016–3017 lie below the table.

F-XS-004/F-ST1-006 transcription facts: the gender male/female shell exists, as claimed. No subgroup result, estimate, CI, P value or nonestimability explanation is printed here. Identification as a primary-outcome analysis and its method comes from the SAP prose/table title on separately assigned pages; this continuation alone cannot establish those descriptors. There is no amendment or removal disclosure here. The table is fully visible; it is a continuation rather than a clipped display.

## PDF page 101: enrollment anchor, message 6 and definitions

[Supplied PDF page 101](../../../joi250093supp1_prod_1768590553.08963.pdf#page=101). PLAN prospective operational material headed “mTB-Tobacco Intervention SMS log”, printed lines 3019–3020; component footer 1. No version or date is printed on this page.

The table columns include “Day Received”, “Message” and “Character Count”, with generic/for-all branch labels. The enrollment-day cell prints “Day Reruited” followed by `Q (-8)` and `Tx (+1)` with footnote markers. Message 1 is the welcome message and is timed “At time/day of enrolment”. Messages 2 and 3 follow in this block; message 3 says “You will get up to 5 text messages every day”.

The next block is `Q (-7)` / `Tx (+2)`. Message 6 states: “The best way to quit tobacco use is to stop completely. To help you quit, we have set a date for you, 7-days from today, to stop using tobacco completely.” Its time is 5:00 pm. The two footnotes state: “This is number of days to the quit date” and “Tx is used for TB treatment and +1 means the first day of treatment”.

F-XS-006 transcription facts: enrollment Q(-8)/Tx(+1), the enrollment timing, and the subsequent seven-days-from-today statement are all visible. The log directly supplies two different anchors: quit-relative days and treatment days. Those anchors should be retained rather than normalized into an assumed enrollment/treatment equivalence beyond the table's own pairing. The page supplies no five-day alternative, revision history, or crosswalk to the report. The bottom of message 11 continues to the next page; every cited enrollment/message-6 element and both footnotes are fully visible.

## PDF page 103: day before quit and transition

[Supplied PDF page 103](../../../joi250093supp1_prod_1768590553.08963.pdf#page=103). PLAN SMS-log continuation; component footer 3. No version/date appears.

The page shows `Q (-2)` / `Tx (+7)` for messages 29–33, then `Q (-1)` / `Tx (+8)` for messages 34–38. Message 38 states: “Ready for quitting tomorrow! Hope you have removed all tobacco products, matches, lighters, ashtrays, paan dans, and waterpipe around you. If not do so right away!” It is timed 7:00 pm. The following left-hand cell begins “QUIT” and message 39 begins on the lower edge, continuing to PDF page 104.

F-XS-006 transcription fact: Q(-1)/Tx(+8) followed by the quit-day transition matches the finding. The source-page break divides the quit-day cell and message 39; it does not conceal the preceding anchor or “tomorrow” instruction. No schedule amendment is printed. The ordinal quit-day wording is supplied on the next assigned page, not reconstructed from this partial cell.

## PDF page 104: ordinal quit-day statement

[Supplied PDF page 104](../../../joi250093supp1_prod_1768590553.08963.pdf#page=104). PLAN SMS-log continuation; component footer 4. No version/date appears.

The continued left-hand cell explicitly reads “DATE (Q) This is the 8th day since joining mTB-Tobacco”. Together with the preceding page's “QUIT”, it is a quit-date label. Messages 39–44 occupy that block. Message 40 states: “Today is your QUIT DATE! Remove all tobacco products around you. You can do it!” at 12:00 pm. The other quit-day times are 9:00 am, 2:00 pm, 5:00 pm, 7:00 pm and 9:00 pm.

The next block is `Q (+1)` / `Tx (+10)` for messages 45–47, followed by `Q (+2)` / `Tx (+11)` and `Q (+3)` / `Tx (+12)`. Message 45 begins “24 hours tobacco free”.

F-XS-006 source nuance: the direct wording is an ordinal “8th day since joining”, while the finding paraphrases the log as “8 days after enrollment”. Whether enrollment day is counted as day one, and whether “joining”, enrollment and the treatment anchor refer to the same clock, are not explicitly reconciled on these pages. The separately printed Q(-8)/Tx(+1) and Q(-1)/Tx(+8) labels remain direct facts. This handoff does not silently convert the ordinal phrase into an elapsed-day count. No five-day rule or revision disclosure appears here. The continued quit-day label and all relevant times are readable.

## PDF page 109: final daily-phase messages and three follow-up reminders

[Supplied PDF page 109](../../../joi250093supp1_prod_1768590553.08963.pdf#page=109). PLAN SMS-log continuation; component footer 9. No version/date appears.

Messages 129, 130 and 131 share `Q (+41)` / `Tx (+50)` and are timed 9:00 am, 2:00 pm and 5:00 pm. The next band reads “mTB-Tobacco Follow-up phase!” and contains:

- Message 132, `Q (+52)` / `Tx (+61)`, time 12:00 pm: “Well done! You have successfully completed first 2 months of your TB treatment. Now it’s time to visit your provider for sputum test and collect more medicine!”;
- Message 133, `Q (+112)` / `Tx (+121)`, time 12:00 pm: “Well done! You have successfully completed 4 months of your TB treatment. Now it’s time to visit your provider for sputum test and collect more medicine!”;
- Message 134, `Q (+180)` / `Tx (+189)`, time 12:00 pm: “Well done! You have successfully completed 6 months of your TB treatment. Now it’s time to visit your provider for the final sputum test.”

Message 133 also contains a non-English rendering, which is not reproduced in this English-only handoff. The English text and numeric date cells are completely visible. Printed line 3021 follows the table.

F-XS-006 transcription facts: daily-phase ending Q(+41)/Tx(+50), three follow-up reminder IDs 132–134 and the three quoted Q/Tx dates match the finding. The reminders explicitly mention TB treatment months 2, 4 and 6; their time origin is therefore treatment, not an unstated conversion into enrollment months. The final day cell Tx(+189) is retained alongside its six-month wording without replacing either. The log lists three reminder rows; it supplies no amendment or fourth monthly reminder on this page. The final table closes fully, with no hidden continuation after message 134.

## Handoff limits and remaining source questions

All fourteen assigned pages were inspected and their requested printed statements found. No assigned unit has unreadable relevant text. Source clipping on p.13 and p.51 affects lower diagram branches, and page breaks divide the SMS table on pp.103–104; the finding-linked prose/date cells are visible. There is no new extraction derivative to inventory.

The page-specific statements above establish source facts, not screening conclusions. Remaining interpretation requires the independently assigned report/SAP/amendment locations: protocol component precedence despite V6.0 headers on earlier-described pages; the relation of economic context to the separately headed MAR/model paragraph; what intervention refinements were adopted; whether ordinal quit-day wording and Q/Tx anchors use the same clock as enrollment; whether the prospective log was the delivered revision; the assay-threshold crosswalk; and whether a shortened report allocation description includes the listed minimization factor. No answer to those questions is invented here.
