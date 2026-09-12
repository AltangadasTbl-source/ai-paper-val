"""Validate exhaustive manual coding and reproduce all descriptive totals."""
from pathlib import Path
from collections import Counter
import json,csv,hashlib,html,re
D=Path(__file__).resolve().parent
ROOT=D.parents[1]
YEARS=['2018','2019','2024','2025']
ROLES=['P_R','P_P','P_O','P_B','S_C','S_W']
LABELS={'P_R':'论文/结果补充材料 vs protocol/SAP','P_P':'protocol/SAP 内部或计划版本之间','P_O':'protocol/SAP vs 独立操作手册','P_B':'protocol 中的历史背景数据内部','S_C':'main vs 普通 supplement / 普通 supplement 之间','S_W':'单个 main / 普通 supplement 内部'}
source=json.loads((D/'all_candidates.json').read_text());bykey={r['key']:r for r in source};assert len(source)==len(bykey)==412
rows=[]
for y in YEARS:
 coded=json.loads((D/f'coded_{y}.json').read_text()); expected={k for k in bykey if k.startswith(y+'::')}
 assert len(coded)==len(expected)==len({r['key'] for r in coded})
 assert {r['key'] for r in coded}==expected
 for r in coded:
  assert r['primary'] in ROLES and r['primary'] in r['relations']
  assert set(r['relations'])<=set(ROLES) and len(r['relations'])==len(set(r['relations']))
  assert r['rationale'] and not r.get('duplicate_of'), 'Review duplicates before counting'
  for p in r['evidence_paths']:assert (ROOT/p).exists(),p
  rows.append({**bykey[r['key']],**r})
assert len({r['package'] for r in rows})==45
# Manually identified mechanism axis for P_R only; independent from original category.
mechanisms={
'analysis_specification':{'jama.2017.21906':[4,6],'jama.2019.0556':[7],'jama.2019.12618':[3],'jama.2019.14231':[1],'jama.2019.17380':[7],'jama.2024.2302':[3,4],'jama.2024.23898':[4,7],'jama.2024.24764':[6,7],'jama.2025.16450':[7],'jama.2025.7710':[4]},
'intervention_delivery':{'jama.2018.9128':[12],'jama.2024.11057':[1],'jama.2025.16450':[3],'jama.2025.20765':[13],'jama.2025.24175':[2]},
'population_recruitment_sites':{'jama.2018.14280':[23],'jama.2018.8802':[2],'jama.2024.24764':[8],'jama.2025.16450':[2,8],'jama.2025.24175':[4,9]},
}
for r in rows:
 if r['primary']=='P_R':
  r['plan_discrepancy_mechanism']='endpoint_definition_window_hierarchy'
  for m,mp in mechanisms.items():
   if r['number'] in mp.get(r['package'],[]):r['plan_discrepancy_mechanism']=m
 else:r['plan_discrepancy_mechanism']=''
 r.setdefault('evidence_state','recorded_candidate')
 r['additional_sensitivity_exclude']=r['evidence_state']=='record_input_error' or r['key']=='2019::jama.2019.2210::C008'
 r['broad_plan_involved']=any(x.startswith('P_') for x in r['relations'])
 r['submission_involved']=any(x.startswith('S_') for x in r['relations'])
 r['current_report_cross_document']=bool(set(r['relations'])&{'P_R','S_C'})
 r['original_cross_document']=r['category']=='Cross-document numeric inconsistency'
rows.sort(key=lambda r:(r['year'],r['package'],r['number']))
def cnt(a):return {p:sum(r['primary']==p for r in a) for p in ROLES}
def describe(a):
 return {'n':len(a),'papers':len({r['package'] for r in a}),'primary':cnt(a),'inclusive':{p:sum(p in r['relations'] for r in a) for p in ROLES},'primary_papers':{p:len({r['package'] for r in a if r['primary']==p}) for p in ROLES},'broad_plan_n':sum(r['broad_plan_involved'] for r in a),'broad_plan_papers':len({r['package'] for r in a if r['broad_plan_involved']}),'submission_n':sum(r['submission_involved'] for r in a),'submission_papers':len({r['package'] for r in a if r['submission_involved']}),'current_report_cross_document_n':sum(r['current_report_cross_document'] for r in a),'PR_mechanisms':dict(Counter(r['plan_discrepancy_mechanism'] for r in a if r['primary']=='P_R'))}
residual=[r for r in rows if r['evidence_state']!='not_reproduced'];strong=[r for r in residual if not r['additional_sensitivity_exclude']]
summary={'all':describe(rows),'by_year':{y:describe([r for r in rows if r['year']==y]) for y in YEARS},'without_nine_explicit_nonreproductions':describe(residual),'additional_two_record_sensitivities':describe(strong),'original_cross_document_reclassification':cnt([r for r in rows if r['original_cross_document']]),'original_category_crosstab':{c:cnt([r for r in rows if r['category']==c]) for c in sorted({r['category'] for r in rows})},'additional_evidence_files':len({p for r in rows for p in r['evidence_paths']}),'candidates_with_deeper_record_reads':sum(bool(r['evidence_paths']) for r in rows),'mixed_candidates':sum(len(r['relations'])>1 for r in rows)}
(D/'summary.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
(D/'reclassified_candidates.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
fields=['key','year','package','id','title','category','primary','relations','evidence_state','plan_discrepancy_mechanism','broad_plan_involved','submission_involved','current_report_cross_document','additional_sensitivity_exclude','rationale','ambiguity','duplicate_of','reportPath','line','evidence_paths']
with (D/'reclassified_candidates.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for r in rows:w.writerow({k:json.dumps(r[k],ensure_ascii=False) if isinstance(r[k],list) else r[k] for k in fields})
packages=[]
for y in YEARS:
 for pkg in sorted({r['package'] for r in rows if r['year']==y}):
  a=[r for r in rows if r['year']==y and r['package']==pkg]
  packages.append({'year':y,'package':pkg,'n':len(a),**cnt(a),'PR_ids':','.join(r['id'] for r in a if r['primary']=='P_R'),'broad_plan_n':sum(r['broad_plan_involved'] for r in a)})
with (D/'paper_counts.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(packages[0]));w.writeheader();w.writerows(packages)
manifest=[]
for p in sorted({r['reportPath'] for r in rows}):
 t=(ROOT/p).read_bytes();manifest.append({'path':p,'sha256':hashlib.sha256(t).hexdigest(),'candidates':sum(r['reportPath']==p for r in rows)})
(D/'source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
# Source-linked full manual ledger, scientific text remains in authoritative final reports.
md=['# 412条候选记录的文档角色重新分类','', '所有412条均已逐卡阅读；每个原始候选ID保留一次。下列分类不是已确认错误的裁决。primary互斥，relations保留实质混合关系。','']
for r in rows:
 md.extend([f"## {r['key']} — {r['title']}",'',f"- 主分类：{r['primary']}（{LABELS[r['primary']]}）；全部关系：{', '.join(r['relations'])}",f"- 原分类：{r['category']}；记录状态：{r['evidence_state']}",f"- 原始候选卡：[{r['reportPath']}:{r['line']}]({ROOT/r['reportPath']}:{r['line']})",f"- 重新编码理由：{r['rationale']}"])
 if r['ambiguity']:md.append(f"- 边界/局限：{r['ambiguity']}")
 for p in r['evidence_paths']:md.append(f'- 额外核对：[{p}]({ROOT/p})')
 md.append('')
(D/'candidate_ledger.md').write_text('\n'.join(md))
pr=['# 论文与protocol/SAP对照的45条候选','', '其中5条原始差异明确未复现。2018.0156 C008的验证记录存在输入语义错误，2019.2210 C008为已说明等同的时间起点措辞；敏感性计算另列。','', '| 年份 | Paper | ID | 原分类 | 问题 | 记录状态 |','|---|---|---|---|---|---|']
for r in rows:
 if r['primary']=='P_R':pr.append(f"| {r['year']} | {r['package']} | [{r['id']}]({ROOT/r['reportPath']}:{r['line']}) | {r['category']} | {r['title'].replace('|','/')} | {r['evidence_state']} |")
(D/'protocol_sap_candidates.md').write_text('\n'.join(pr)+'\n')
print(json.dumps(summary,indent=2,ensure_ascii=False))
pct=lambda n,d:f'{100*n/d:.1f}%'
lines=['# 45篇文章、412条验证候选的重新分类汇总','',
'本次统计对象为2018、2019、2024、2025四个年份目录中的45个paper packages。每篇仅取`.ai_paper_validation`目录下当前最高版本的`final_report_*.md`；不重复累计历史版本、candidate ledger、checker和复核记录。按文件夹年份归属，不按DOI中的年份重新分组。', '',
f"已逐条阅读412张完整候选卡；{summary['candidates_with_deeper_record_reads']}条在编码中记录了额外回查路径，共{summary['additional_evidence_files']}份不同的详细验证、提取、源页或图像记录。2018、2019、2024由三个分年审阅代理完成，主审完成2025；主审统一边界，另由另一位分年审阅代理对2025的46条进行独立二次分类核对。这不是412条的双人独立裁决，也未计算审阅者一致率。", '',
'**核心结果：论文/结果supp与protocol/SAP对照的候选为45/412（10.9%），涉及24/45篇（53.3%）。排除9条在复核中明确未复现的原始差异后，40/403（9.9%）仍归入该关系；进一步排除一条验证记录输入语义错误和一条原文明示等同的措辞案例，为38/401（9.5%）。这些都不是已确认的protocol违背率。**','',
'**一、文档关系重新分类**','',
'协议和SAP本来也是提交材料的一部分。本分析为回答问题，操作性地将其与main及其他supp分开。文件名supp1/supp2不能决定角色；检查了文件内容和精确比较对象。', '',
'主分类互斥；混合条目优先归入论文—计划关系，再归入其他计划关系，再归入跨普通报告文件关系。各行条目数可相加，涉及文章数不可相加。','',
'| 重新分类 | 条数 | 占412条 | 涉及文章/45 |','|---|---:|---:|---:|']
for p in ROLES:lines.append(f"| {LABELS[p]} | {summary['all']['primary'][p]} | {pct(summary['all']['primary'][p],412)} | {summary['all']['primary_papers'][p]}/45 |")
lines+=['', '**广义protocol/SAP材料相关为95/412（23.1%），涉及30/45篇（66.7%）。** 其中只有45条属于论文—计划比较；其余50条是41条计划内部、2条与独立操作手册比较、7条历史背景数据问题。将95条全部解释为论文偏离protocol/SAP会混淆关系。','',
'**仅归于main+普通supp内部的主分类共317/412（76.9%）**，其中65条为跨文件，252条为单文件内部。另有7条论文—计划候选同时具有提交报告内部的实质矛盾，所以非互斥口径下涉及main+普通supp内部关系共324条、44篇。跨普通报告文件关系非互斥合计71条，单文件内部284条；这些交叠计数不能直接相加。','',
'**二、分年计数**','', '| 年份 | 篇数 | 候选总数 | 论文—计划 | 其他计划材料相关 | main—普通supp | 单文件报告内部 | 论文—计划/当年候选 |','|---|---:|---:|---:|---:|---:|---:|---:|']
for y in YEARS:
 s=summary['by_year'][y];c=s['primary'];lines.append(f"| {y} | {s['papers']} | {s['n']} | {c['P_R']} | {c['P_P']+c['P_O']+c['P_B']} | {c['S_C']} | {c['S_W']} | {pct(c['P_R'],s['n'])} |")
lines+=['| 合计 | 45 | 412 | 45 | 50 | 65 | 252 | 10.9% |','',
'论文—计划候选分别涉及2018年7/10篇、2019年6/10篇、2024年4/10篇、2025年7/15篇。年份构成、报告工作流和单篇候选粒度不同，不能把以上差异当成年度质量变化。','',
'**三、原cross-document标签为何不能直接用于回答**','',
'原Cross-document numeric inconsistency只有85条。重新阅读后的互斥归属如下：','',
'| 85条原cross-document候选的实际关系 | 数量 | 占85条 |','|---|---:|---:|']
for p in ['P_R','S_C','S_W','P_P','P_B']:
 n=summary['original_cross_document_reclassification'][p];lines.append(f'| {LABELS[p]} | {n} | {pct(n,85)} |')
lines+=['', '**45条论文—计划候选中，只有19条带原cross-document标签；另26条（57.8%）藏在其他指标里：21条measure/label/scale、3条statistical reporting、2条analysis-unit/population。** 同时，原cross-document中18条实际只发生在单个main或普通supp内部。','',
'限定分母为“涉及当前论文/结果报告的跨文件比较”，即P_R或S_C，共110条独立候选；其中45条涉及论文—计划，45/110=40.9%。71条涉及普通报告之间比较，其中6条与P_R重叠；不能用45+71作为独立分母。排除明确未复现记录后，分母105、论文—计划40，占38.1%。此分母不含仅在计划之间比较的条目。','',
'原指标与新关系为两个轴，不再互相竞争。完整交叉表：','',
'| 原指标 | 论文—计划 | 计划内部 | 计划—手册 | 计划背景 | 普通报告跨文件 | 普通报告单文件 | 总数 |','|---|---:|---:|---:|---:|---:|---:|---:|']
for c,ct in summary['original_category_crosstab'].items():lines.append('| '+c+' | '+' | '.join(str(ct[p]) for p in ROLES)+' | '+str(sum(ct.values()))+' |')
lines+=['', '**四、论文—计划的具体差异机制**','',
'机制为本次对P_R的另一个互斥编码维度；不会将同一个ID按统计、标签和跨文档重复计数。','',
'| 机制 | 原45条 | 排除9条明确未复现记录后，P_R剩40条 |','|---|---:|---:|']
for m,label in [('endpoint_definition_window_hierarchy','终点定义、阈值、观察窗口或终点层级'),('analysis_specification','统计模型、先验、插补、匹配/随机化、亚组或预设分析声明'),('population_recruitment_sites','研究/分析人群、入组日期或中心数量'),('intervention_delivery','干预剂量、消息数或干预时长')]:lines.append(f"| {label} | {summary['all']['PR_mechanisms'][m]} | {summary['without_nine_explicit_nonreproductions']['PR_mechanisms'][m]} |")
lines+=['', '**五、证据状态与敏感性计算**','',
'| 口径 | 总候选分母 | 论文—计划 | 比例 | 广义计划材料相关 | 比例 |','|---|---:|---:|---:|---:|---:|']
for label,s in [('保留所有原始候选ID',summary['all']),('排除9条原始差异明确未复现',summary['without_nine_explicit_nonreproductions']),('再排除输入语义错误1条和明确等同措辞1条',summary['additional_two_record_sensitivities'])]:lines.append(f"| {label} | {s['n']} | {s['primary']['P_R']} | {pct(s['primary']['P_R'],s['n'])} | {s['broad_plan_n']} | {pct(s['broad_plan_n'],s['n'])} |")
lines+=['', '明确未复现的9条：','']
for r in rows:
 if r['evidence_state']=='not_reproduced':lines.append(f"- [{r['key']}]({ROOT/r['reportPath']}:{r['line']})：{r['title']}（原关系{r['primary']}）。")
lines+=['', '进一步敏感性检查：','',
'- 2018/jama.2018.0156 C008：最终候选卡和recheck把54/1022标作死亡，当前来源提取文本实际为day-28存活。论文与计划终点口径的条件性问题仍可保留，但原定量论证不能照抄。编码标记record_input_error。',
'- 2019/jama.2019.2210 C008：randomization与supplementation start名称不同，但文章明确为同一访视/等同起点，不支持实际日期差异。',
'- 2025/jama.2025.24175 C005和C009虽写Original comparator not reproduced，纠正输入后分别还剩近似失访率/取整问题和24/31/33中心数的里程碑问题。编码repaired_residual，未按关键词一律删除。','',
'其余条目仍可能是简称、四舍五入/截尾、不同统计分析、已披露计划变更、研究阶段差别或格式问题。这次没有对全部条目作科学真实性裁决，9条排除并不意味着其余403条已确证。','',
'**六、影响分类的重点案例**','',
'- jama.2025.7710 C004：论文无多重性调整，而protocol及Draft SAP计划Benjamini–Hochberg调整；计P_R。草案状态与正式最终版本缺失必须保留，不能称已确认违规。',
'- jama.2025.19563 C001：protocol的三条件OR规则与supp明确的A1C全局失败条件不同；计P_R。15名糖尿病范围A1C参与者不等于15名终点被改变者，缺各人其他成功条件。',
'- jama.2025.7583 C002：论文、protocol、SAP都给342及20%；问题是计划材料中142/组与失访膨胀算式不匹配。计P_P，不计论文—计划差异。',
'- jama.2025.15185 C010：SAP给出FMMA定义并支持同义解释，记录针对的是结果图FMA/FMMA局部称谓。计S_W，不因引用SAP就计P_R。',
'- jama.2025.19843 C001：main的P=.78与结果图log-rank P=.56；SAP提供计划语境，但main未标出该P的检验，不能推定它违反SAP。计S_C。',
'- jama.2025.16450 C004：独立操作手册GMFCS 3–5与SAP 4–5；计P_O，不等同最终论文与计划差异。相反jama.2019.12618的文件封面明示原始/最终protocol，主体采用Manual of Operations形式，按实际protocol角色编码。',
'- jama.2025.24175 C006/C007/C008/C010/C014来自protocol中对PROVIDE既往试验的背景叙述和表图；源页有Protocol页脚。计P_B，其中C014未复现，不算当前试验main/supp内部问题。','',
'**七、45篇逐篇计数与追溯文件**','',
'| 年份 | Paper | 总数 | P_R | P_P | P_O | P_B | S_C | S_W | P_R IDs |','|---|---|---:|---:|---:|---:|---:|---:|---:|---|']
for p in packages:lines.append('| '+p['year']+' | '+p['package']+' | '+str(p['n'])+' | '+' | '.join(str(p[k]) for k in ROLES)+' | '+(p['PR_ids'] or '—')+' |')
lines+=['', '保留每个源候选ID一次，未发现可以确定为同一问题而必须合并的重复ID。相关单元格、不同访视或行列交换仍可能共享同一产生原因，本统计单位是候选ID，不是独立错误机制。例如jama.2025.11178一篇贡献37条（全部412条的9.0%），仅Table3即有26条SMD/CI结构候选。因此同时报告文章比例，并不把412条当成412个独立样本。','',
'- [412条完整编码与依据](candidate_ledger.md)', '- [412条CSV](reclassified_candidates.csv)', '- [45条论文—计划候选索引](protocol_sap_candidates.md)', '- [45篇逐篇CSV](paper_counts.csv)', '- [计数JSON](summary.json)', '- [编码规则](CODING_RULES.md)', '- [可复算聚合脚本](aggregate.py)', '- [45份最终MD及SHA256](source_manifest.json)', '',
'所有源论文、PDF、原始验证MD和历史记录均未改写。以上输出仅为本次事后重新分类。']
(D/'SUMMARY_ZH.md').write_text('\n'.join(lines)+'\n')
