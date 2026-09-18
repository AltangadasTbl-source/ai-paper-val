import {fileURLToPath} from 'node:url';
import fs from 'node:fs/promises';
import {chromium} from 'playwright';
const root=process.env.ADJ_ROOT || fileURLToPath(new URL('../',import.meta.url)).replace(/\/$/,'');
const pages=[
 ['一次只做一小步','今天只需要打开 Excel。全程不需要终端、脚本或安装依赖。',[
 ['先找你的角色','初审人：从第 2 页开始。<br>交接人：看第 6–7 页。<br>复核人：从第 8 页开始。'],
 ['整个流程','初审 → 保存初审备份 → 另存复核副本 → 固定初审快照 → 复核与讨论 → 保存最终文件。'],
 ['给自己一个小目标','先看 1 条候选。做完后，允许自己休息。<br>不要一次读完整张表。'],
 ['记住三个词','<b>no</b>：还在做。<br><b>primary_done</b>：初审做完。<br><b>checker_done</b>：复核做完。'],
 ['提示','表里的判断用英文选项。本文用中文解释。<br>AI 提出的候选 ≠ 已经确认的问题。']
 ]],
 ['开始：选对文件','目标：建立自己的工作副本。',[
 ['□ 1　选年份','打开对应年度的 .xlsx 文件：2018、2019、2024 或 2025。不要把 examples 测试文件用于正式研究。'],
 ['□ 2　另存为','Excel → 文件（File）→ 另存为（Save As）。<br>例如：<b>2019_primary_work.xlsx</b>。'],
 ['□ 3　填身份','打开 <b>Setup</b>。在 B2 的 primaryReviewerId 填稳定的个人 ID。B3 可填姓名。<br>B6 的 stage 保持 <b>primary</b>。B4、B5 先留空。'],
 ['□ 4　找到第一条','打开 <b>Papers</b>，找到对应的 <b>C_论文编号</b> 工作表。一次只看一行。'],
 ['完成标志','你有自己的工作副本，而且 Setup B6 = primary。<br>此时 M 列 Primary assessment 应显示空白。']
 ]],
 ['看证据，再做决定','目标：先理解这一条候选。',[
 ['□ 1　认准编号','看 A 列 Candidate key。它是这条候选的唯一编号。不要改这个编号。'],
 ['□ 2　读内容','读 B 列 Candidate title 和 C 列 Source location。<br>去 <b>Candidates</b>、<b>Evidence</b>，按同一个 key 筛选。需要时打开共享年份／论文文件夹中的原文。'],
 ['□ 3　选 Disposition（D）','<b>retain</b>：保留这条发现。<br><b>exclude</b>：看过了，不保留。<br><b>discuss</b>：看过了，需要一起讨论。'],
 ['□ 4　确认 Review domain（E）','这里可能有 AI 建议。你必须检查它是否合适。<br>统计／数值问题 → statistical_results。<br>报告内部不一致 → report_internal_inconsistency。<br>计划材料之间不一致 → plan_material。<br>计划与最终报告的差异 → protocol_report。'],
 ['停一下','空白表示还没有答案。discuss 表示已经看过但需要讨论。它们不一样。']
 ]],
 ['只填当前需要的判断','目标：按 E 列的领域，填写适用的 H–L 列。',[
 ['D = retain 时','<b>statistical_results</b>：H（是否有统计／数值报告问题）和 I（是否实质性）必填；J 可选。<br><br><b>report_internal_inconsistency / plan_material</b>：K 必填。<br><br><b>protocol_report</b>：L 可选，没有额外必填判断。不要求额外寻找变更说明或理由。'],
 ['D = exclude 或 discuss 时','H–L 不需要领域判断。保持空白或 not_applicable。'],
 ['□ 改过领域？再看一遍','已选的旧答案不会自行消失。G 若显示 <b>CLEAR INACTIVE VALUES</b>，删除不适用的旧答案，或选 not_applicable。重新启用的必填项要补答。'],
 ['三个不同意思','空白：还没填，或可选项未评估。<br>indeterminate / unknown：适用，但目前不能确定。<br>not_applicable：这个判断不适用于当前分支。'],
 ['拿不准选项的意思','打开 <b>Codebook</b>，按字段名查解释。不要把不确定直接当成“没有问题”。']
 ]],
 ['初审：完成一行就保存','目标：看到 PRIMARY READY。',[
 ['□ 1　检查这一行','证据看过了；D 和 E 已确认；必填判断已填好。R 列 Notes 可写英文备注。'],
 ['□ 2　标记初审完成','F 列 Complete 选 <b>primary_done</b>。<br>初审阶段 N–Q 四列保持空白。'],
 ['□ 3　看 G 列','<b>PRIMARY READY</b>：这一行初审条件已满足。<br><b>CHECK FIELDS</b>：检查 D、E 和适用判断。<br><b>CHECK REVIEWER IDs</b>：检查 Setup 的身份。'],
 ['□ 4　保存或休息','Windows：Ctrl+S。Mac：Command+S。<br>记下“文件名 + 工作表名 + Candidate key”，下次从这里继续。'],
 ['改过已完成的答案？','先把 F 改为 <b>no</b>。改完后重新核对，再选 primary_done。系统不会自动重置完成标记。'],
 ['准备交接','所有行完成后，去 <b>Checks</b>。B7 必须显示 <b>PRIMARY READY</b>，才进入下一页。']
 ]],
 ['交接第 1 步：留好备份','目标：原始初审有一份独立存档。',[
 ['□ 1　看总状态','Checks 的 B7 = <b>PRIMARY READY</b>。这只检查填写和完成状态；证据判断仍由人负责。'],
 ['□ 2　保存初审备份','保存为例如 <b>2019_primary_complete.xlsx</b>，然后关闭文件。把它作为初审存档保留。'],
 ['□ 3　建立复核副本','重新打开初审备份，马上 File → Save As。<br>另存为例如 <b>2019_checking.xlsx</b>。'],
 ['□ 4　看窗口顶部的文件名','现在必须是 <b>2019_checking.xlsx</b>。<br>后面的操作都在复核副本里做。'],
 ['此时不要改 stage','Setup B6 暂时仍是 <b>primary</b>。<br>下一页先固定初审快照，再切到 checker。'],
 ['交给复核人的东西','复核工作副本 + 初审备份 + 共享原文文件夹的位置。<br>约定谁正在编辑复核副本，避免同时改出多个版本。']
 ]],
 ['交接第 2 步：固定快照','目标：复核改答案时，初审记录不会跟着变。',[
 ['□ 1　打开 Primary_snapshot','确认 Setup B6 仍为 <b>primary</b>。<br>在工作表左上方的名称框（Name Box），输入本年度范围，然后按 Enter：'],
 ['要选的范围','2018：<b>A1:L120</b>　　2019：<b>A1:L72</b><br>2024：<b>A1:L92</b>　　 2025：<b>A1:L132</b>'],
 ['□ 2　复制，并贴回原处','复制选中区域。不要换到别处。<br>Home → Paste → Paste Special → <b>Values（值）</b>。<br>意思是：把计算结果贴回同一块区域，变成固定记录。<br>不要选普通粘贴或 Formulas。然后保存。'],
 ['□ 3　切换阶段','到 Setup：B6 改成 <b>checker</b>；B4 填复核人的 ID。复核人必须与初审人不同。B5 可填姓名。'],
 ['□ 4　检查交接成功','回 C_ 表：M 列显示初审摘要，D/E/H–L/R 保留现有答案。<br>如果出现 <b>FREEZE SNAPSHOT</b> 或 <b>CHECK KEY / SNAPSHOT</b>，先不要复核。'],
 ['顺序错了怎么办？','尚未开始复核：从初审备份另存一个新副本，重做本页。<br>已经开始复核：先另存当前文件保留修改；再从初审备份取回正确快照。不要用复核后的答案冒充初审。']
 ]],
 ['复核：同意就做两件事','目标：核对原文和初审答案，再记录复核结论。',[
 ['□ 1　看 M，再看原文','M 是初审快照摘要。D/E/H–L/R 是当前可编辑答案。<br>先核对候选和证据，再决定是否同意。'],
 ['□ 2　完全同意且不修改','N 列 Checker result 选 <b>agree</b>。<br>F 列 Complete 选 <b>checker_done</b>。'],
 ['□ 3　看 G 列','G 应显示 <b>FINAL READY</b>。<br>F 留在 primary_done 时，复核还不算完成。'],
 ['需要补充说明？','N 选 <b>agree_clarification</b>，O 写英文说明。需要修改的答案，直接在 D/E/H–L/R 改。再核对并选 checker_done。'],
 ['空白现在就是空白','不再有“空白继承初审”。想删掉可选答案，直接清空该格。不要输入旧版的 <clear>。必填项不能清空后当成完成。'],
 ['先休息也可以','保存文件，记下工作表和 Candidate key。修改已完成行时，先把 F 设为 no；核对后再选 checker_done。']
 ]],
 ['有分歧：一起讨论','目标：把最终共识写清楚。',[
 ['□ 1　选择复核结果','不同意：N = <b>disagree</b>。<br>暂时无法判断：N = <b>unable</b>。'],
 ['□ 2　写下原因','O 列 Checker comment 用英文写：哪里不同意，或缺什么信息。直接填写建议的答案。'],
 ['□ 3　一起讨论','disagree、unable，或者初审 D = discuss，都需要讨论。不要只把 Complete 改成完成就结束。'],
 ['□ 4　记录共识','P 列 Discussion resolution = <b>resolved</b>。<br>Q 列 Resolution note 写参与人及共同结论。<br>把 D/E/H–L/R 更新为最终答案；D 不能仍是 discuss。'],
 ['□ 5　重新核对','F = <b>checker_done</b>，G = <b>FINAL READY</b>。<br>若尚未讨论完，保存草稿；不要当成最终结果交付。'],
 ['出现 AGREE BUT CHANGED','你选择 agree，但答案和初审快照不同。<br>若修改是有意的，请选合适的非 agree 结果并补说明；若是误改，恢复原答案。']
 ]],
 ['完成：直接交付 Excel','目标：所有候选都完成，再交最终文件。',[
 ['□ 1　看 Checks','B7 = <b>FINAL READY</b>。<br>否则打开 Decisions，筛选 status，找到待处理的 key，再回对应 C_ 表修改。'],
 ['□ 2　看内置结果','<b>Decisions</b>：初审、最终判断、复核记录与结果分类。<br><b>Paper_counts</b>：每篇论文的计数；该论文未全部完成时，最终计数留空。<br><b>Protocol_plan_table</b>：协议／计划材料的描述性结果。'],
 ['□ 3　保存最终版','File → Save As，例如 <b>2019_final.xlsx</b>。<br>把最终版与原始初审备份一起交给管理者。整个流程不需要另跑校验或导出命令。'],
 ['管理者汇总四年时','每年只收一份权威 final 文件。建立新的汇总工作簿，按相同列名依次复制四年的结果行，用 <b>Paste Special → Values</b> 粘贴。表头只保留一遍；不要混入 TEST 文件。'],
 ['核对数量','正式候选：2018＝119；2019＝71；2024＝91；2025＝131。四年合计 <b>412</b> 条、<b>45</b> 篇论文。'],
 ['结果怎么理解','协议／计划差异只作描述，不自动等于确认的问题。<br>“初审答案可见”的复核不能当作盲法一致性评估。']
 ]],
 ['没有锁，也不用解锁','目标：知道新版能改什么，以及出错后怎么恢复。',[
 ['为什么旧版有锁图标？','旧版曾给工作表、部分单元格和工作簿结构加保护，主要为了防止误改来源或公式。锁图标通常是在提示这种保护。'],
 ['v.2.1.5.4 已全部取消','新版工作表、单元格、工作簿结构均不加锁。<br>不设密码，不需要“解除工作表保护”。'],
 ['哪些地方是日常输入？','Setup 的身份与 stage；C_ 表的 D、E、F、H–L、N–R。<br>A–C、G、M 和结果表是来源／计算区域：虽然能改，日常审阅保留原样。'],
 ['误改了公式或编号？','马上撤销：Windows Ctrl+Z；Mac Command+Z。<br>若已经保存并关闭，使用自己的备份恢复。恢复前先另存当前文件，保留已有工作。'],
 ['若仍看见锁或无法编辑','先核对文件路径和名称：是不是打开了旧版或初审备份？再看 Excel 的 Review 菜单。若显示 Protect Sheet，说明当前工作表没有启用保护。<br>下载提示、只读文件权限或别人占用文件，是另一类问题；请先另存自己的工作副本。'],
 ['最后记住','一次一行。看证据 → 填答案 → 看 G → 保存。<br>初审用 primary_done；复核用 checker_done。']
 ]]
];
const html=`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>人工复核分步指南 v.2.1.5.4</title><style>
@font-face{font-family:CN;src:url('file:///System/Library/Fonts/Supplemental/Arial%20Unicode.ttf')}
@page{size:A4;margin:0}*{box-sizing:border-box}body{margin:0;color:#173f57;font-family:CN,Arial,sans-serif;font-size:12pt;line-height:1.55}.page{width:210mm;height:297mm;padding:13mm 16mm 18mm;page-break-after:always;position:relative}.top{color:#176b75;font-size:9pt;border-bottom:1px solid #cad7df;padding-bottom:4mm;display:flex;justify-content:space-between}h1{font-size:24pt;line-height:1.2;margin:8mm 0 4mm;font-weight:normal}.task{color:#52606d;margin:0 0 6mm}section{margin-bottom:4mm}h2{font-weight:normal;color:#176b75;font-size:15pt;margin:0 0 1.5mm}p{margin:0}section:last-of-type{background:#f0f5f8;border-left:3px solid #176b75;padding:3mm 4mm}b{font-family:Arial,CN,sans-serif;font-weight:bold}.footer{position:absolute;bottom:10mm;left:16mm;right:16mm;border-top:1px solid #cad7df;padding-top:3mm;color:#52606d;font-size:9pt}.page:last-child{page-break-after:auto}
</style>${pages.map(([title,task,sections],i)=>`<article class="page"><div class="top"><span>人工复核分步指南　/　v.2.1.5.4　/　全程 Excel</span><span>${i+1} / ${pages.length}</span></div><h1>${title}</h1><p class="task">${task}</p>${sections.map(([h,t])=>`<section><h2>${h}</h2><p>${t.replaceAll('<clear>','&lt;clear&gt;')}</p></section>`).join('')}<div class="footer">${i===pages.length-1?'一次一行。完成后保存。':`完成这一页，再翻到第 ${i+2} 页。`}</div></article>`).join('')}</html>`;
await fs.mkdir('/tmp/adjudication-excel-only',{recursive:true});await fs.writeFile('/tmp/adjudication-excel-only/guide.html',html);
const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
const page=await browser.newPage();await page.goto('file:///tmp/adjudication-excel-only/guide.html');await page.evaluate(()=>document.fonts.ready);
const metrics=await page.locator('.page').evaluateAll(nodes=>nodes.map((p,i)=>({page:i+1,bottom:p.querySelector('section:last-of-type').getBoundingClientRect().bottom-p.getBoundingClientRect().top,footer:p.querySelector('.footer').getBoundingClientRect().top-p.getBoundingClientRect().top})));
if(metrics.some(m=>m.bottom>m.footer-12))throw Error(JSON.stringify(metrics));
await page.pdf({path:`${root}/human_adjudication_v_2_1_5_4_step_by_step_CN.pdf`,printBackground:true,preferCSSPageSize:true});
console.log(JSON.stringify(metrics));await browser.close();
