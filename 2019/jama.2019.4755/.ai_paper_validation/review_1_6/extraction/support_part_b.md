# Support evidence mapping — shard B

Scope: DOC-002 physical PDF pp.33–62 (PLAN); DOC-004 pp.1–8 (REPORT); DOC-005 p.1 (REPORT). COMPLETE: 39/39 physical pages mapped, including 17 fresh-required protocol units. No candidate diagnosis, global relationship ID, or historical conclusion is used. Local keys B001–B071 are mapping keys only. Sources and reused derivatives were not modified. No Office/CSV source exists; workbook formulas and cached values are not applicable.

## Engines, commands, and evidence precedence

Direct tools available under tooling_record.md were used: Poppler pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0 CPU, English, psm 6. Source-linked reusable assets: review_1_5_1/preprocessing/support/DOC-002_pp1-62_layout.txt, DOC-004_pp1-3_layout.txt, DOC-005_p1_layout.txt; document_outputs/doc-b45e07a04d82/normalized_pages/page-4.txt through page-8.txt and ocr_pages/page-5.png through page-8.png. These paths are under .ai_paper_validation/. Every listed fresh unit was opened visually using its new full-page PNG. Supplement pp.5–8 were visually opened; p7 was additionally freshly rendered to resolve placement.

Fresh derivatives all reside in .ai_paper_validation/review_1_6/preprocessing/. For each N in 34,35,37,38,40,41,44,49,51,52,53,54,56,57,58,61,62, the exact command pattern was:

```bash
pdftotext -layout -f "$N" -l "$N" joi190039supp1_prod.pdf ".ai_paper_validation/review_1_6/preprocessing/support-b-protocol-$N-layout.txt"
pdftoppm -r 110 -f "$N" -l "$N" -singlefile -png joi190039supp1_prod.pdf ".ai_paper_validation/review_1_6/preprocessing/support-b-protocol-$N"
tesseract ".ai_paper_validation/review_1_6/preprocessing/support-b-protocol-$N.png" ".ai_paper_validation/review_1_6/preprocessing/support-b-protocol-$N-ocr" -l eng --psm 6
```

Output triplet: support-b-protocol-N-layout.txt, support-b-protocol-N.png, support-b-protocol-N-ocr.txt. OCR is a locator only; English semantic mapping below is based on readable source image where font encoding or German OCR is imperfect. Additional direct locators: `pdftotext -layout -f 33 -l 62 joi190039supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/support-b-protocol-33-62-layout.txt`; `pdftoppm -r 180 -f 7 -l 7 -singlefile -png joi190039supp3_prod.pdf .ai_paper_validation/review_1_6/preprocessing/support-b-results-7`; same render for protocol p61 with prefix support-b-protocol-61-detail. No fallback environment needed.

## Pagewise coverage

PDF links are relative to this extraction artifact. Physical PDF pages are authoritative; protocol physical pp.49 and 50 both print page49, and pp.51–62 print pages50–61.

| Source/page | Basis | Mapped content | Status |
|---|---|---|---|
| DOC-002 33 | Reusable | SUSAR deadlines, follow-up windows, unblinding and sampling burden; B001 | COMPLETE |
| DOC-002 34 | Fresh layout/render/OCR + visual | Three-month colonoscopy window and reinclusion, optional biomarkers; B002 | COMPLETE |
| DOC-002 35 | Fresh layout/render/OCR + visual | Administrative deadlines; B003; no study result | COMPLETE |
| DOC-002 36 | Reusable | Ten-year retention; B004; no study result | COMPLETE |
| DOC-002 37 | Fresh layout/render/OCR + visual | eCRF medication history two weeks, dropout three weeks; B005 | COMPLETE |
| DOC-002 38 | Fresh layout/render/OCR + visual | Diary dates, ten-year participant-list retention; B006 | COMPLETE |
| DOC-002 39 | Reusable | Funding points to Appendix4; no applicable result or displayed quantity | COMPLETE |
| DOC-002 40 | Fresh layout/render/OCR + visual | Double entry, four monitoring visits/year and first after ~20 patients; B007 | COMPLETE |
| DOC-002 41 | Fresh layout/render/OCR + visual | Monitoring/steering/publication policy; no applicable inferential result; contextual one meeting before start | COMPLETE |
| DOC-002 42 | Reusable | 300mg, day1 administration, storage, platelet/PK quantities; B008 | COMPLETE |
| DOC-002 43 | Reusable | PK half-lives and packaging; B009 | COMPLETE |
| DOC-002 44 | Fresh layout/render/OCR + visual | Storage below25°C and accountability; B010 | COMPLETE |
| DOC-002 45 | Reusable | References1–16 only; no applicable extracted results | COMPLETE |
| DOC-002 46 | Reusable | References17–34 only; no applicable extracted results | COMPLETE |
| DOC-002 47 | Reusable | References35–51 only; numeric study-title context1657 cases,10-year study, aspirin300/75/300mg; no supplied result | COMPLETE |
| DOC-002 48 | Reusable | Reference52 only; no applicable result | COMPLETE |
| DOC-002 49 | Fresh render/OCR + visual | Scanned signed approval page, not blank; dates only; no applicable result | COMPLETE |
| DOC-002 50 | Reusable | Unsigned duplicate signature form; no applicable quantitative result | COMPLETE |
| DOC-002 51 | Fresh layout/render/OCR + visual | AE/SAE/expectedness definitions; B011 | COMPLETE |
| DOC-002 52 | Fresh layout/render/OCR + visual | SUSAR, intensity and causality definitions; B012 | COMPLETE |
| DOC-002 53 | Fresh layout/render/OCR + visual | Reporting24h,3 working days/72h,7+8days,15days; B013 | COMPLETE |
| DOC-002 54 | Fresh layout/render/OCR + visual | AE outcome/action categories and fatal-event counting rule; B014 | COMPLETE |
| DOC-002 55 | Reusable | Appendix1 references3–4 only; no applicable result | COMPLETE |
| DOC-002 56 | Fresh layout/render/OCR + visual | Optional blood volumes/timing/storage; B015 | COMPLETE |
| DOC-002 57 | Fresh layout/render/OCR + visual | Laboratory contacts only; no applicable result | COMPLETE |
| DOC-002 58 | Fresh layout/render/OCR + visual | Investigator signature form only; no applicable result | COMPLETE |
| DOC-002 59 | Reusable | Financial table rows1–4; B016 | COMPLETE |
| DOC-002 60 | Reusable | Financial table rows5–12; B017 | COMPLETE |
| DOC-002 61 | Fresh layout/render/OCR + visual | Financial rows13–16,total and footnotes1–12; B018 | COMPLETE |
| DOC-002 62 | Fresh layout/render/OCR + visual | Financial footnotes13–18; B019 | COMPLETE |
| DOC-004 1 | Reusable | Contents eTables1–6; no independent result | COMPLETE |
| DOC-004 2 | Reusable | Eligibility and thresholds; B020 | COMPLETE |
| DOC-004 3 | Reusable | Eligibility continuation; B021 | COMPLETE |
| DOC-004 4 | Reusable | eTable2:20 rows,all counts/footnotes; B022–B041 | COMPLETE |
| DOC-004 5 | Reusable + visual | eTable3:9 rows,all counts/percentages/CIs; B042–B050 | COMPLETE |
| DOC-004 6 | Reusable + visual | eTable4:9 rows,all counts/percentages/CIs; B051–B059 | COMPLETE |
| DOC-004 7 | Reusable + fresh render/visual | eTable5:9 rows,all values/CIs and header placement; B060–B068 | COMPLETE |
| DOC-004 8 | Reusable + visual | eTable6:9 rows,18SD/P pairs; B069 | COMPLETE |
| DOC-005 1 | Reusable | Protocol/code/data availability; B070 | COMPLETE |

## PLAN relationships: operational, historical and contextual content

B001 [protocol p33](../../../joi190039supp1_prod.pdf#page=33): SUSAR reporting within15days,7days if deadly/life-threatening; DSUR once/year or request. Participant missing colonoscopy contacted within3weeks after medication; new appointment within3months of randomization. Unblinding envelopes: one set each at study centers,KKS,DKFZ. Stool collection device one/day. These are planned windows/counts, not observed outcomes.

B002 [protocol p34](../../../joi190039supp1_prod.pdf#page=34): colonoscopy gold standard; FIT results usually not returned. If colonoscopy absent within3months after randomization, agreed positive stool result sent to gastroenterologist; patients undergoing colonoscopy after more than3months can be reincluded. Biomarkers optional and research-only; no specified analysis time or result.

B003 [protocol p35](../../../joi190039supp1_prod.pdf#page=35): planned study end notified within90days; premature end within15days; clinical report within1year. Framework versions2008/2006/2004 are administrative context. B004 [p36](../../../joi190039supp1_prod.pdf#page=36): participant identification lists and all documentation retained at least10years. B005 [p37](../../../joi190039supp1_prod.pdf#page=37): eCRF includes medication within2weeks before start and date/reason of dropout within3weeks. B006 [p38](../../../joi190039supp1_prod.pdf#page=38): diary records whether/when medication/stool collection occurred; participant list includes randomized number only available after randomization, screening failures logged; list retained10years after study. Drug accountability records kept for years without precise duration here.

B007 [p40](../../../joi190039supp1_prod.pdf#page=40): diary/histology/colonoscopy entered by two independent blinded reviewers; planned monitoring4visits/center/year excluding initiation/close-out, two KKS and two DKFZ; first KKS after around20patients/center, variable with quality. B008 [p42](../../../joi190039supp1_prod.pdf#page=42): oral aspirin300mg/tablet, study day1 one glass water; storage not above25°C protected from humidity; placebo not above25°C. Background platelet replacement10–15%/day, aggregatory normalization4–6days because50%functioning platelets suffice. Tmax0.5–2hours; volume distribution0.16L/kg; plasma binding>90%. B009 [p43](../../../joi190039supp1_prod.pdf#page=43): unmetabolized ASA urine1%total intake; half-life ASA15–20min, salicylic acid2–3hours. RITA software version1.24; primary blister1tablet/unit. B010 [p44](../../../joi190039supp1_prod.pdf#page=44): medication below25°C protected from humidity. No trial efficacy statistics on these pages.

B011 [p51](../../../joi190039supp1_prod.pdf#page=51): AE is temporally associated untoward medical occurrence without necessary causality; pre-existing condition counts only if worsened; surgery itself not AE, underlying condition may be; planned surgery and pre-existing indication excluded. SAE criteria death,life-threatening,hospitalization/prolongation,persistent/significant disability/incapacity,congenital anomaly. Unexpected nature/severity inconsistent with product information or new specificity/severity/frequency information. B012 [p52](../../../joi190039supp1_prod.pdf#page=52): SUSAR requires suspected drug relationship plus unexpectedness plus seriousness. Intensity mild/moderate/severe based on everyday-activity interference; causality certain,probable,possible,unlikely,not assessable,not related. These classify safety counts, not statistical estimates.

B013 [p53](../../../joi190039supp1_prod.pdf#page=53): SAE report within24hours or next working day; independent second assessor within next3working days(72hours as printed). Fatal/life-threatening SUSAR notice within7calendar days,follow-up additional8calendar days; other SUSAR/safety within15calendar days. B014 [p54](../../../joi190039supp1_prod.pdf#page=54): each SUSAR single case; outcome categories recovered,resolving,unresolved,recovered with sequel,fatal,unknown. If multiple AEs only event leading to death(possibly related) classified fatal. IMP actions unknown,not applicable,none,drug treatment,other.

B015 [p56](../../../joi190039supp1_prod.pdf#page=56): first appointmentday0 optional blood4extra tubes9–10mL each(2EDTA,2serum). Specified serum8.5–9mL: Sarstedt9mL type02.1388 or Vacutainer8.5mL type367953. EDTA9–10mL: Sarstedt9mL type06.1664.001(K3) or Vacutainer10mL type367525(K2). Serum room-temperature30min,max60min; centrifuge10min2500–3500RPM. EDTA invert8–10times. Store4–8°C,pickup2–3days; laboratory centrifugation2500–3500RPM/aliquot same day; aliquots−20°C. No biomarker outcomes supplied.

### Financial plan table and formulas (all EUR)

B016 [p59](../../../joi190039supp1_prod.pdf#page=59): printed rows and component values, translated into English.

| Row | Total | Components in displayed order |
|---|---:|---|
|1 KKS project management|13,383|Protocol4,424; patient information1,580; insurance632; ethics application3,476; authority application2,528; local authority395; closure348|
|2 Internal project management|153,000|No itemized cells on this page|
|3 Clinical pharmacology management|30,950|Protocol8,000; information2,000; ethics/authority400; site/physician qualification650; SAE/SUSAR assessment10,000; amendments800; monitoring reports/DSUR3,200; steering300; final report5,600|
|4 Monitoring quality control|24,790|Investigator folder1,776; manual1,184; training1,184; initiation2,131; regular monitoring14,208; close-out1,421; site support2,886 continues p60|

B017 [p60](../../../joi190039supp1_prod.pdf#page=60):

|Row|Total|Components|
|---|---:|---|
|5 Monitoring travel|3,000|No itemized amount|
|6 Pharmacovigilance|28,922|Safety protocol884; manual2,272; SAE/SUSAR capture/report15,600; safety reports8,616; SAE listings1.704(as printed); structures1,548|
|7 Data management including eCRF|40,642|Plan504; database7,288; adverse-event coding nz; status189; queries15,309; database closure1,008; transfer1,008; MACRO license10,800; support4,536|
|8 General KKS project costs|12,731|Meetings2,592; central folder5,573; coordination4,566; audits nz|
|9 Practice compensation|60,000|Footnote6|
|10 Medication/blistering|3,400|No itemized amount|
|11 Investigator/GCP training|2,430|Footnote7|
|12 Laboratory|24,881|Courier1,440; supplies2,388; materials6,107; shipping546; measurements14,400(last3 p61)|

B018 [p61](../../../joi190039supp1_prod.pdf#page=61): row13 other meetings500; row14 ethics/BfArM fees6,800; row15 insurance67,116; row16 general costs35,060(itemized printing3,000; shipping31,080; meeting/hotel980). Study budget505,570. Overhead,tax,total including overhead/tax,contract funds,own funds,total available funds blank. Double-asterisk means total cost of subsequent items. Budget content is PLAN administrative numeric evidence, not reported clinical results.

Footnotes1–12, visually read and translated preserving printed operations: (1) ethics registration2,528 plus other ethics948; (2) TV-L E13 salary50% for3years30,000×3 plus E9 salary50% for3years21,000×3; (3) monitoring per ICH E6/SOP; (4) KKS2visits/year×3years, train80 plus53/hour plus possible hotel80, printed1,596; Benscheid/Zaineddin2visits/year×3years,80/person train, printed480; minimum total2,076; (5) assumes1/20participants SAE,100×150, and1/1000 SUSAR,2×300; (6)30/completed case,printed30×2000; (7)3physicians training650×3=1,950,hotel80×3=240,train80×3=240,total2,430; (8)blood pickup0.3/sample×2samples×2400=1,440; (9)2plasma+2serum tubes/person,100plasma tubes27.7,100serum tubes26.6 **as visually printed** (reusable text says26.9, source wins); (10)8protective tubes/person,2400participants,500tubes133,plus1,000stool collection aids; (11)3.5/delivery to DKFZ weekly52weeks×3years=546; (12)1.5/FOBGold TubeScreen measurement×4samples/person×2400=14,400.

B019 [p62](../../../joi190039supp1_prod.pdf#page=62): (13) travel/food no number; (14)BfArM study registration1,700,annual report1,000,amendment700,assume3amendments; (15)23.50/person×2400; (16)5000flyers350–500,3000questionnairesaverage1,045beforetax,all study document printing3,500,additional color costs possible; (17)postage1.45×2400=3,480,stool shipping2.25×4×2400=21,600,practice document shipping2400×2.50=6,000,total31,080; (18)1study meeting/year,4meetings total,hotel80,travelUlm/Heidelberg80 for3persons=480,additional possible500.

## REPORT definitions and matching keys

B020 [results p2](../../../joi190039supp3_prod.pdf#page=2): eligibility age40–80both sexes; postmenopause no bleeding≥12months or surgical sterilization; premenopause negative pregnancy test; planned screening/diagnostic colonoscopy. Excluded anticoagulants/antiplatelets within2weeks,ASA within1week,NSAIDs/COX2 within3days; severe kidney/liver disease GFR<30mL/min. B021 [p3](../../../joi190039supp3_prod.pdf#page=3): cardiac exclusions MI past6months; planned methotrexate≥15mg/week; other clinical/administrative exclusions without numeric result.

Matching main-paper keys: eTable2 connects returned/valid tests and planned versus actual sampling day to main participant flow/analysis populations. eTable3 connects multi-sample detection sensitivity/specificity to main secondary outcomes. eTables4–5 connect day2 per-protocol detection/predictive values to main day2 intention-to-screen Tables2–3 after explicit population matching. eTable6 connects site random-effects sensitivity analysis to main Results and statistical definitions. These are matching keys, not equality claims across differing populations.

### eTable2 complete cells

[DOC-004 p4](../../../joi190039supp3_prod.pdf#page=4). Intervention N1075; control N1059. Columns below: scheduled day; returned; valid; actual-day bins Missing,<0,0,1,2,3,4,>4. All cells N(count), never percentages. Scheduled day relative tablet intake. Valid requires valid result and sample before colonoscopy(or information unavailable). Actual day2 samples used per-protocol. “Any” aggregates sample records across scheduled occasions, not necessarily unique persons.

|Key|Group/test|Scheduled|Returned|Valid|Missing|<0|0|1|2|3|4|>4|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|B022|Intervention quantitative|≤0|1044|1026|82|152|781|9|1|0|0|1|
|B023|Intervention quantitative|2|1045|1030|77|2|11|126|758|48|5|3|
|B024|Intervention quantitative|3|989|975|77|1|0|9|105|700|65|18|
|B025|Intervention quantitative|4|955|944|64|1|0|0|7|93|677|102|
|B026|Intervention quantitative|Any|4033|3975|300|156|792|144|871|841|747|124|
|B027|Intervention qualitative|≤0|1037|970|78|149|733|8|1|0|0|1|
|B028|Intervention qualitative|2|1040|974|75|2|9|121|719|42|4|2|
|B029|Intervention qualitative|3|979|922|71|1|0|9|97|663|65|16|
|B030|Intervention qualitative|4|955|887|60|1|0|0|7|88|638|93|
|B031|Intervention qualitative|Any|4011|3753|284|153|742|138|824|793|707|112|
|B032|Control quantitative|≤0|1016|1000|80|159|753|5|2|0|0|1|
|B033|Control quantitative|2|1024|1012|78|2|4|136|747|38|4|3|
|B034|Control quantitative|3|987|979|75|1|1|5|114|706|58|19|
|B035|Control quantitative|4|959|947|72|1|0|1|1|104|656|112|
|B036|Control quantitative|Any|3986|3938|305|163|758|147|864|848|718|135|
|B037|Control qualitative|≤0|1026|968|76|149|735|5|2|0|0|1|
|B038|Control qualitative|2|1024|969|72|2|4|126|720|39|3|3|
|B039|Control qualitative|3|979|934|73|1|1|5|108|677|51|18|
|B040|Control qualitative|4|956|905|66|1|0|1|1|103|627|106|
|B041|Control qualitative|Any|3985|3776|287|153|740|137|831|819|681|128|

### eTable3 complete cells

[DOC-004 p5](../../../joi190039supp3_prod.pdf#page=5). Advanced neoplasms=CRC or advanced adenoma; one300mg aspirin/placebo; at least one positive among up to3samples scheduled days2,3,4. Cutoff µgHb/g. A=aspirin,P=placebo tuples each ordered TP,FN,TN,FP,Se%,Sp%; differences percentage points A−P with95%CI. TP/FN disease-positive; TN/FP disease-negative. Sensitivity=TP/(TP+FN),specificity=TN/(TN+FP) are reconstruction identities; interval method not stated on this page. No P values.

|Key|Sex/test/cutoff|A tuple|P tuple|Se difference [CI]|Sp difference [CI]|
|---|---|---|---|---|---|
|B042|All quantitative10.2|63,50,685,261,55.8,72.4|49,58,774,161,45.8,82.8|10.0[-3.3,22.8]|-10.4[-14.1,-6.6]|
|B043|All quantitative17.0|44,69,816,130,38.9,86.3|35,72,852,83,32.7,91.1|6.2[-6.4,18.7]|-4.9[-7.7,-2.0]|
|B044|All qualitative10.2|53,58,714,222,47.7,76.3|35,73,779,146,32.4,84.2|15.3[2.3,27.8]|-7.9[-11.5,-4.3]|
|B045|Men quantitative10.2|46,31,311,148,59.7,67.8|28,30,362,102,48.3,78.0|11.5[-5.5,27.8]|-10.3[-15.9,-4.5]|
|B046|Men quantitative17.0|34,43,384,75,44.2,83.7|22,36,408,56,37.9,87.9|6.2[-10.5,22.4]|-4.3[-8.8,0.3]|
|B047|Men qualitative10.2|41,34,343,111,54.7,75.6|19,40,372,89,32.2,80.7|22.5[5.6,38.0]|-5.1[-10.5,0.2]|
|B048|Women quantitative10.2|17,19,374,113,47.2,76.8|21,28,412,59,42.9,87.5|4.4[-16.7,25.1]|-10.7[-15.4,-5.8]|
|B049|Women quantitative17.0|10,26,432,55,27.8,88.7|13,36,444,27,26.5,94.3|1.2[-17.4,20.4]|-5.6[-9.1,-2.0]|
|B050|Women qualitative10.2|12,24,371,111,33.3,77.0|16,33,407,57,32.7,87.7|0.7[-19.0,20.7]|-10.7[-15.5,-5.9]|

### eTable4 complete cells

[DOC-004 p6](../../../joi190039supp3_prod.pdf#page=6). Same definitions/order as eTable3; day2 per-protocol rather than combined samples. All arm count cells and Se/Sp percentages preserved, all differences95%CI.

|Key|Sex/test/cutoff|A tuple|P tuple|Se difference [CI]|Sp difference [CI]|
|---|---|---|---|---|---|
|B051|All quantitative10.2|42,56,635,136,42.9,82.4|25,61,691,85,29.1,89.0|13.8[-0.1,27.1]|-6.7[-10.1,-3.2]|
|B052|All quantitative17.0|29,69,704,67,29.6,91.3|18,68,735,41,20.9,94.7|8.7[-4.0,20.8]|-3.4[-5.9,-0.8]|
|B053|All qualitative10.2|30,56,617,119,34.9,83.8|19,65,683,62,22.6,91.7|12.3[-1.4,25.4]|-7.8[-11.2,-4.5]|
|B054|Men quantitative10.2|31,34,310,78,47.7,79.9|11,34,344,58,24.4,85.6|23.2[5.0,39.5]|-5.7[-10.9,-0.4]|
|B055|Men quantitative17.0|23,42,350,38,35.4,90.2|9,36,373,29,20.0,92.8|15.4[-1.8,30.9]|-2.6[-6.5,1.4]|
|B056|Men qualitative10.2|24,33,311,63,42.1,83.2|9,37,353,40,19.6,89.8|22.5[4.5,38.6]|-6.7[-11.5,-1.8]|
|B057|Women quantitative10.2|11,22,325,58,33.3,84.9|14,27,347,27,34.1,92.8|-0.8[-21.8,20.6]|-7.9[-12.3,-3.4]|
|B058|Women quantitative17.0|6,27,354,29,18.2,92.4|9,32,362,12,22.0,96.8|-3.8[-21.6,15.0]|-4.4[-7.6,-1.1]|
|B059|Women qualitative10.2|6,23,306,56,20.7,84.5|10,28,330,22,26.3,93.8|-5.6[-25.1,15.3]|-9.2[-13.7,-4.6]|

### eTable5 complete cells and source/extraction placement facts

[DOC-004 p7](../../../joi190039supp3_prod.pdf#page=7). Caption day2,one300mg aspirin/placebo,advanced neoplasms,per-protocol. PPV/NPV in%; tuples A/P=(PPV,NPV),differences percentage points95%CI. Reconstruction identities PPV=TP/(TP+FP),NPV=TN/(TN+FN); counts from matched eTable4 rows, but equality is not assumed without checking. Printed cutoff header visibly reads `[µg` without visible `Hb/g]`, while native extraction supplies `[µg Hb/g]` in displaced order. Preserve display and text separately. Women difference cells visibly show a minus glyph alone in fresh Poppler180dpi render; extracted number fragments18.2,25.7,21.6 are displaced across lines. Mapping below records minus-only display and corresponding native-text fragments; no correction is assigned.

|Key|Sex/test/cutoff|A PPV,NPV|P PPV,NPV|PPV difference [CI]|NPV difference [CI]|
|---|---|---|---|---|---|
|B060|All quantitative10.2|23.6,91.9|22.7,91.9|0.9[-9.3,10.7]|0.0[-2.8,2.8]|
|B061|All quantitative17.0|30.2,91.1|30.5,91.5|-0.3[-15.3,14.2]|-0.5[-3.3,2.3]|
|B062|All qualitative10.2|20.1,91.7|23.5,91.3|-3.3[-14.8,7.7]|0.4[-2.6,3.3]|
|B063|Men quantitative10.2|28.4,90.1|15.9,91.0|12.5[-0.2,24.1]|-0.9[-5.2,3.4]|
|B064|Men quantitative17.0|37.7,89.3|23.7,91.2|14.0[-4.9,31.1]|-1.9[-6.1,2.2]|
|B065|Men qualitative10.2|27.6,90.4|18.4,90.5|9.2[-5.9,22.8]|-0.1[-4.4,4.2]|
|B066|Women quantitative10.2|15.9,93.7|34.1,92.8|minus-only display; native18.2[-34.7,-1.3]|0.9[-2.9,4.6]|
|B067|Women quantitative17.0|17.1,92.9|42.9,91.9|minus-only display; native25.7[-48.4,-0.7]|1.0[-2.7,4.8]|
|B068|Women qualitative10.2|9.7,93.0|31.2,92.2|minus-only display; native21.6[-38.9,-3.9]|0.8[-3.2,4.8]|

Abbreviations: CI confidence interval,FIT fecal immunochemical test,g gram,Hb hemoglobin,NPV negative predictive value,PPV positive predictive value. No P values supplied. Source display placement versus extracted hidden/misaligned text is a derivative limitation, fully mapped for review.

### eTable6 complete cells

B069 [DOC-004 p8](../../../joi190039supp3_prod.pdf#page=8): site-effect sensitivity analysis. GLMM random-intercept standard deviations with corresponding likelihood-ratio P values. Null SD=0,alternativeSD>0. Successful outcome is agreement between test and colonoscopy for advanced neoplasms at day2 after single300mg aspirin/placebo; intention-to-screen. Cutoff µgHb/g. No arm-specific SDs,counts,confidence intervals or LRT statistics supplied.

|Sex/test/cutoff|Sensitivity SD|Sensitivity P|Specificity SD|Specificity P|
|---|---:|---:|---:|---:|
|All quantitative10.2|0.00E+00|0.50|5.49E-03|0.38|
|All quantitative17.0|1.97E-01|0.16|0.00E+00|0.50|
|All qualitative10.2|0.00E+00|0.50|9.23E-03|0.30|
|Men quantitative10.2|0.00E+00|0.50|1.00E-14|0.50|
|Men quantitative17.0|0.00E+00|0.50|1.47E-02|0.40|
|Men qualitative10.2|0.00E+00|0.50|1.13E-02|0.35|
|Women quantitative10.2|0.00E+00|0.50|1.79E-12|0.50|
|Women quantitative17.0|1.67E-01|0.40|0.00E+00|0.50|
|Women qualitative10.2|4.35E-16|0.50|0.00E+00|0.50|

B070 [DOC-005 p1](../../../joi190039supp4_prod.pdf#page=1): retrospective availability statement says protocol published2018;18(1):914; statistical code available from Silvia Calderazzo; dataset not available. No supplied data/code contents or quantitative trial result. REPORT role by content, not a prospective PLAN.

B071 cross-table definition inventory: eTables3–4 counts N,Se/Sp%,eTable5 predictive values%,effect differences percentage points with95%CI; comparator aspirin minus placebo inferred from displayed signed arm contrasts and requires same sex,test,cutoff,time,population. eTable2 sample-level totals require valid/before-colonoscopy rule and actual-day bins. eTable6 SDs are model parameters, not diagnostic percentages or standard errors. Neither effect OR/RR/HR nor person-time rates occur in this scope.

## Completion and limitations

39unique pages complete;17fresh-required protocol pages rendered,OCR-located and visually inspected;22reusable-backed pages covered. eTables2–6 contain56 individually reconstructed rows:20sample-count,9combined-detection,9per-protocol detection,9predictive-value,9site-effect. All18site SD/P pairs and54difference/CI pairs in eTables3–5 retained. Pages45–48,50,55,57,58 and results cover/availability were explicitly opened from reusable content; no applicable trial results recorded. Protocol p49 signed approval scan was visually confirmed as nonblank. No scientific coverage gap remains. Derivative font corruption, low-quality German OCR and eTable5 hidden/displaced numeric text remain recorded transcription/display limitations; final recheck must use supplied PDFs. No source/reused asset changed; no web,GPU,arbitrary Python or old scientific disposition used.
