"""Serialize manual, full-card document-role decisions; not a keyword classifier."""
import json,re
from pathlib import Path
D=Path(__file__).parent
rows=json.loads((D/'input_2025.json').read_text())
# All IDs reviewed; lists below are explicit manual overrides of within-report scope.
assign={
'jama.2024.24764':{'P_R':[6,7,8]},
'jama.2024.27643':{'S_C':[2,3,4,5,6,7]},
'jama.2025.11178':{'S_C':[34,35]},
'jama.2025.15185':{'S_C':[1,2,3,5,6,7,8]},
'jama.2025.15440':{},
'jama.2025.16450':{'P_R':[2,3,7,8],'P_O':[4,5],'P_P':[6]},
'jama.2025.19563':{'P_R':[1],'S_C':[2]},
'jama.2025.19843':{'S_C':[1]},
'jama.2025.20765':{'P_R':[13],'P_P':[3,4,5,6,7,8,9,10,11],'S_C':[2]},
'jama.2025.24175':{'P_R':[2,3,4,9],'P_P':[5],'P_B':[6,7,8,10,14]},
'jama.2025.4390':{},
'jama.2025.7583':{'P_R':[1],'P_P':[2]},
'jama.2025.7710':{'P_P':[1,2,3],'P_R':[4]},
'jama.2025.9110':{},
'jama.2025.9663':{'P_P':[3]},
}
secondary={('jama.2024.27643',6):['S_W'],('jama.2025.11178',35):['S_W'],('jama.2025.15185',2):['S_W'],('jama.2025.19563',2):['S_W'],('jama.2025.20765',13):['P_P'],('jama.2025.24175',9):['P_P'],('jama.2025.7583',1):['P_P']}
negated={'jama.2025.16450':[2,3,5,6],'jama.2025.24175':[2,3,4,14]}
notes={
('jama.2024.24764',5):'Figure mortality window is unspecified; count discrepancy may be a time-window difference. All locations are in the main article despite original cross-document category.',
('jama.2024.24764',6):'Covariance specifications differ; article silence about sandwich SE does not prove it was absent. Amendment/output unavailable.',
('jama.2024.24764',7):'UK-only comparison isolates effect measure from C008 population issue; skewness anticipated but planned median difference differs from geometric-mean ratio.',
('jama.2024.24764',8):'UK-only result remains reported; all-country result is additional and status is unclear, not proven substitution.',
('jama.2024.27643',6):'Both article-internal Figure/narrative and article/results-supp interval differences are explicitly targeted.',
('jama.2025.11178',34):'Source explicitly distinguishes self-report with EHR fallback from EHR-only sex derivation; equality is conditional.',
('jama.2025.11178',35):'Main arithmetic and main/workbook repeated percentage both directly targeted. Distinct from C005, which concerns All Observed subgroup workbook cell, not Overall narrative.',
('jama.2025.15185',2):'Internal median/IQR label-form issue and explicit matched main/supp summary comparison.',
('jama.2025.15185',3):'Results-supp unit omitted; day comparison is conditional.',
('jama.2025.15185',9):'Internal eTable total versus its own arm/category sums is target; main 146 merely corroborates arithmetic.',
('jama.2025.15185',10):'SAP defines FMMA, supporting synonym interpretation. It is a local figure abbreviation switch, not report-versus-SAP discrepancy.',
('jama.2025.16450',4):'Manual of procedures is a distinct prospective operational document, not final results or protocol/SAP. Versioned definition change possible.',
('jama.2025.16450',7):'Planned versus realized alpha-spending boundaries need not be equal; missing execution output.',
('jama.2025.16450',8):'Planned 15 versus completed 17 centers may reflect activation/milestone differences.',
('jama.2025.19563',1):'Supplement explicitly supplies global A1C failure rule. Fifteen diabetes-range participants are NOT fifteen proven changed classifications; component achievement and governing amendment missing.',
('jama.2025.19563',2):'Listed methods may be nonexhaustive; Siemens device mentioned but unlisted. Both main/supp availability and supplement-internal method/missingness arithmetic compared.',
('jama.2025.19563',3):'BMI versus weight is established by same main figure unit and main Table1; supplementary BMI usage corroborates only.',
('jama.2025.19563',4):'Different comparisons within one results supplement; main age P=.01 corroborates possible global note, not another discrepancy.',
('jama.2025.19843',1):'SAP log-rank statement supports interpretation; prose test is unnamed, so no demonstrated report-versus-plan method difference. Fixed-time versus survival tests can differ.',
('jama.2025.20765',2):'All-cause main total corroborates cause-label issue, while explicitly disaggregated TB deaths come from results supplement.',
('jama.2025.20765',13):'Explicit old-plan versus later-plan and reported 178/134 message total difference. Distinct from schedule arithmetic C003/C005; chronology unresolved.',
('jama.2025.24175',5):'Original 112 input not reproduced, repaired 117 input leaves only approximate attrition/rounding question. Retained as repaired_residual, not fully negated.',
('jama.2025.24175',9):'Original 28 corrected to24, but repaired 24/31/33 mismatch remains. Both plan internal and final-vs-plan contexts; milestone definitions missing.',
('jama.2025.7583',1):'Both protocol-versus-SAP and report-versus-SAP endpoint operator explicitly targeted. No case at exactly5 mm identified.',
('jama.2025.7583',2):'Plan and article AGREE at342 and20%; arithmetic incompatibility is within protocol/SAP full input sequence. Article does not print142. Not report-versus-plan.',
('jama.2025.7710',4):'SAP expressly Draft v1.2; final approved plan/amendment missing. No-adjustment versus planned BH remains candidate governance question.',
('jama.2025.9110',1):'Main label versus own two-endpoint displays; supplement is comparable convention, not identically matched discrepancy.',
('jama.2025.9110',3):'Main label versus own two endpoints and median-difference effect. Final supplementary methods corroborate median estimand.',
('jama.2025.9663',1):'Extraneous mmHg already contradicts own percent sign and respectively construction; eTable provides corroborating correct units. Classified local unit-placement issue.',
('jama.2025.9663',3):'Broken cross-reference in SAP, not substantive mismatch of reported result or numerical rule. May not impede rule interpretation.'
}
consult={
'jama.2024.24764':list(range(5,9)), 'jama.2025.16450':list(range(1,11)),
'jama.2025.24175':list(range(1,15)), 'jama.2025.7583':[1,2,3],
'jama.2025.20765':[6,13], 'jama.2025.7710':[4], 'jama.2025.19563':[1,2,4],
'jama.2025.19843':[1], 'jama.2025.11178':[34,35], 'jama.2025.15185':[9,10]
}
role_reasons={'S_W':'Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison.', 'S_C':'Target explicitly compares current main article and non-plan results supplement/workbook.', 'P_R':'Target compares reported current-study content with supplied protocol/SAP specification.', 'P_P':'Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator.', 'P_O':'Target compares protocol/SAP against a separate prospective operational manual, not a published-results report.', 'P_B':'Target concerns historical/background results inside the protocol, not the current trial plan or submitted main/results supplement.'}
out=[]
for r in rows:
 pkg,n=r['package'],r['number'];role='S_W'
 for label,ids in assign[pkg].items():
  if n in ids:role=label
 rel=[role]+secondary.get((pkg,n),[])
 m=re.search(r'\*\*Reported-versus-comparator:\*\*\s*(.*?)(?=\n\s*\n|\Z)',r['body'],re.S)
 comparator=m.group(1).strip() if m else r['title']
 evidence=[]
 if n in consult.get(pkg,[]):
  v='1_5_3' if pkg=='jama.2024.24764' else '1_5_1';evidence.append(f'2025/{pkg}/.ai_paper_validation/review_{v}/verification/evidence_recheck.md')
 note=notes.get((pkg,n),'')
 state='not_reproduced' if n in negated.get(pkg,[]) else 'recorded_candidate'
 if state=='not_reproduced':note='Final direct-source recheck explicitly does not reproduce registered mismatch; relationship denotes original registration only. '+note
 if pkg=='jama.2025.24175' and n in [5,9]:state='repaired_residual'
 if role=='P_B':
  note+=' Historical PROVIDE study results presented in protocol background; not current ImmunoSep observed results. Protocol footer and introduction directly inspected in stored page render.'
  evidence.extend([f'2025/{pkg}/.ai_paper_validation/review_1_5_1/extraction/support_quantitative_evidence.md',f'2025/{pkg}/.ai_paper_validation/review_1_5_1/parts/mapping/doc002_pp033_064.md',f'2025/{pkg}/.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/pp033_064/low-36.png'])
 subtype=r['title']
 out.append(dict(key=r['key'],primary=role,relations=rel,rationale=role_reasons[role]+' '+comparator,evidence_paths=evidence,ambiguity=note,duplicate_of='',subtype=subtype,evidence_state=state))
(D/'coded_2025.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
from collections import Counter
print(len(out),Counter(x['primary'] for x in out),Counter(x['evidence_state'] for x in out))
