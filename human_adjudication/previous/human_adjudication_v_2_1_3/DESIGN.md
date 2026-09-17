# Human adjudication v.2.1.3 设计说明

本版按照用户要求，将原来的四份年度混合工作簿拆为四份 Primary 和四份 Checker，并统一两类文件的每篇论文一张表的呈现方式。统计判断范围沿用 v.2.1.2。

## 文件与呈现

八份人工审阅 XLSX 放在版本目录顶层；冻结来源放在 resources 子目录。每份文件均包含 Start、Setup、Papers、Candidates、Evidence、Codebook；Primary 的论文表以 P_ 开头，Checker 以 C_ 开头。

共有 45 篇论文，因此两轮合计 90 张可见论文审阅表；候选仍为 412 个唯一 key，在不同阶段出现不表示新增候选。两类表共用前 14 列的顺序、宽度、表头颜色、行高和冻结位置。Checker 追加其四个复核/讨论字段以及一个只读初审摘要，不再将所有论文放在单张年度 Checker 表中。

## 独立文件之间的交接

Checker 的空白布局可以预先发布，但不能预填尚未发生的人工初审。发布模板因此明确标注 AWAITING PRIMARY HANDOFF。prepare-checker 只接受全部完成且通过校验的 Primary 文件，生成相同布局的独立 Checker 副本；记录初审人身份、原文件 SHA256 和逐 key 的初审快照。

快照保存在隐藏的 _Primary 表，并在每张 C_ 论文表同一候选行显示只读摘要。快照与摘要均校验完整性；原 Primary 文件保持不变。Checker 不依赖外部工作簿引用，可独立共享；初审后续修改不会偷偷同步到已交接的复核。

本次文件拆分需要一次管理者交接命令，取代旧版同一文件内直接转交的方式。普通审阅者仍使用 Excel 填写，无需逐条复制或手工维护跨文件引用。已有输出文件不覆盖，避免误丢复核工作。

## 判断与继承

五个领域判断列继续保留条件默认值。适用项空白、不适用项 N/A；默认不算人工答案。Checker 依据本行修改和嵌入的初审领域/disposition 计算适用性，按候选 key 继承，正确重排完整行不改变对应关系。

statistical_results 必填错误状态和实质性，下游影响可选；internal_nonstatistical 和 plan_material 共用一个判断，但前者是递交材料内部的非统计不一致，后者是 protocol/SAP 等计划材料之间的不一致。protocol_report 为计划与最终报告差异，可选描述；Documentation 和 Justification 继续删除。

切换领域后，原先不适用的初审字段不自动成为新判断。手动选择覆盖默认公式的限制、红色旧值提示、可选恢复默认值和完成标记人工重新确认规则均延续 v.2.1.2。

## 校验与统计

schema 更新为 xlsx-adjudication-5，明确区分 primary、checker_template 和 checker 三个文件阶段。Primary 完成状态为 primary_complete，只代表初审已完成，不能作为最终统计结果；模板不能在没有交接的情况下接受复核作答或进入导出。

校验逐篇核对工作表候选集合、Papers 清单、源证据、只读摘要和快照，并验证命名范围和已知默认公式。Primary 不要求复核字段；已准备的 Checker 必须保持完整初审快照和原文件来源记录。默认公式只按已知规则解释，不执行任意输入公式，不信任缓存。

最终导出仅接受已准备的 Checker 文件，每年一份。初审和复核均完成、讨论解决后才有确定类别；未完成不是零。P_R/P_P 仅作描述，不进入时间比较；S_C/S_W 的统计错误和内部非统计不一致延续既有实质性条件。

全部 XLSX 内容为英文；Codebook 的字段名来自与表头相同的 LABELS，并增加新只读摘要的解释。文档中明确区分自动化结构/语义验证与未实测的桌面 Excel 交互。验证见 [VALIDATION.md](VALIDATION.md)。
