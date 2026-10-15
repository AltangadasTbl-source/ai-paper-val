# AI-validation-project：Mentor 观点、目标、实践方法与历次更新

## 材料范围与说明

本文基于本地目录中全部 5 份非 Markdown 会议材料整理：

- `June-12/MeetingWithDrLin-06-12-2026_原文 (1).txt`
- `June-30/MeetingWithDrLin-06-30-2026_原文.txt`
- `June-30/MeetingNote_MeetWithDrLin-06-30-2026.txt`
- `July-24/MeetingWithDrLin-07-24-2026_Transcript.txt`
- `July-24/Meeting With Dr Lin Note 0724.txt`

自动转录存在较多中英文同音误识别。本文结合上下文与两份人工会议记录交叉校正，并注意区分 Mentor 的明确意见、学生提出的方案，以及尚未确定的讨论方向。

综合三次会议，Mentor 所说的 **AI-validation-project** 更准确地讲，是：

> 用现成的大语言模型对医学论文正文、表格、流程图和 supplementary materials 做系统化的内部一致性审计，识别可验证的数值、报告及版本不一致；再由人工核实这些 AI flags，评估这种工具是否值得成为投稿、审稿或发表前的常规 safeguard。

它不是要证明一篇论文的科学结论“绝对正确”，也不是主要做模型排行榜、微调新模型或识别学术造假。

## 一、Mentor 的出发点

### 1. 直接来源是 Mentor 自己的审稿经验

Mentor 在审阅 applied、clinical、systematic review/meta-analysis 类论文时，开始用不将输入用于训练的 business AI 检查正文和 supplement。至少有两次，AI 找到了人工审稿时很难注意到的错误，例如：

- point estimate 不在其 confidence interval 内；
- 不同 outcome 的 CI 完全相同，疑似复制粘贴后漏改；
- p-value 与 CI 是否跨越 null value 相互矛盾；
- 正文更新过，但 supplement 仍然是旧结果；
- 流程图人数加减不一致，或与正文中的数字对不上；
- 图片中的数字与正文不一致。

这些不是抽象假设，而是 Mentor 在真实审稿或合作稿件中遇到、并向作者确认过的情况。参见 [6 月 12 日 transcript：项目起点](June-12/MeetingWithDrLin-06-12-2026_原文%20%281%29.txt#L708)。

### 2. 人工审稿无法稳定完成逐项核查

Mentor 认为普通审稿人往往只花一两个小时看一篇论文，且没有足够激励逐表、逐行核对正文和 supplement。数字表面上通常“看起来合理”，但局部不一致很容易漏过。

AI 的优势不是替代专业判断，而是：

- 能快速扫描长文档；
- 能跨正文、表格、附录和图片找对应关系；
- 对重复 CI、算术不平、版本漂移等模式非常敏感；
- 可以把人工注意力引向值得进一步核实的位置。

### 3. 大量问题可能只是 typo，但仍然具有研究与实践价值

Mentor 多次强调，AI 发现的问题不必等同于真正的分析错误，更不能直接等同于造假。很多可能来自：

- 复制粘贴漏改；
- 排版错误；
- 正文改了但 supplement 未同步；
- 分析版本更新后图表未更新；
- participant flow 中遗漏了解释；
- table 总数与 subgroup 加总不一致。

但即使只是 typo，也会影响论文的可信度和可复核性。AI 因而可以作为额外的 quality-control safeguard。

对于明显异常、重复数字或难以解释的模式，它也可能提示更严重的数据完整性问题，但 Mentor 没有把“检测造假”定为项目的核心 endpoint。

### 4. 更广泛的思想背景：AI 时代的核心能力是判断与核实

7 月 24 日前半段，Mentor 反复表达：AI 已经能够快速搭论文框架、写代码和做 simulation，但输出仍需具备专业知识的人核查、纠偏和重新组织。学生不能把 AI 输出 take for granted，而应训练判断、质疑和引导 AI 的能力。参见 [7 月 24 日 transcript：AI 与人工判断](July-24/MeetingWithDrLin-07-24-2026_Transcript.txt#L79)。

这和 validation project 的逻辑一致：

- AI 检查人写的论文；
- 人再检查 AI 提出的 flags；
- 最终是 human–AI audit workflow，而不是把判断完全交给模型。

## 二、Mentor 想达成的点

### 1. 证明 AI 具有“常规审计价值”

Mentor 最关心的问题不是模型的 benchmark accuracy，而是：

- AI 是否能在真实论文中经常提供有用、可核实的 flags？
- 有多少论文至少存在一项被人工确认的问题？
- 问题主要出现在哪些位置、属于哪些类型？
- 这种检查是否值得作者、审稿人或期刊 routinely 使用？

换句话说，核心是展示 practical potential 和 workflow value。

### 2. 给出一个可执行的论文质量保障方案

Mentor 希望最终能支持这样的实践建议：

> 在投稿、审稿或发表前，把每篇稿件的正文和 supplement 交给 AI 按统一清单检查一次，再由人核实 AI 报告的问题。

AI 不能保证结果正确，但能减少本可避免的错误。

### 3. 即使在高水平期刊中发现少量问题，也足以有意义

Mentor 的判断是：

- 如果审计 JAMA 级别的 RCT，哪怕约 10% 的文章发现可验证问题，也是重要 finding；
- 如果高水平期刊完全找不到问题，项目的卖点会减弱；
- PLOS ONE 之类的一般性 multidisciplinary journal 更可能发现问题，Mentor 当时粗略猜测可能接近 50%，但其学术冲击力会较弱；
- 因此可以考虑高水平期刊与一般期刊对比。

人工 note 对这一点记录得非常直接：“unsupervised is enough”“JAMA: 10% fault is enough”“PLOS ONE…50% problematic”。参见 [6 月 30 日 note](June-30/MeetingNote_MeetWithDrLin-06-30-2026.txt#L23)。

其中 10% 和 50% 是讨论中的经验性预期/说明，不是预先确定的统计标准。

### 4. 形成一篇快速、较小、偏应用的 AI paper

Mentor 不希望该项目过多占用学生做统计方法研究的时间。定位是：

- 一个相对小、可以快速完成的项目；
- AI-related applied paper；
- 不以开发全新统计方法为主；
- 可以投 BMJ Open 一类 open-access applied journal；
- AI 模型更新太快，因此一旦完成分析，应尽快写完并投稿。

### 5. 展示低成本模型也能产生价值

Mentor 后来进一步提出：最强、最贵模型当然可能更好，但若相对便宜、一般研究人员可以获得的 thinking model 也能识别错误，反而更能支持项目的现实价值。

因此“cost-effective、accessible audit”可能成为一个卖点，但尚未被确定为正式的模型比较研究。

## 三、讨论过的实践方法

### A. 研究设计：以自然发表论文做 unsupervised audit

6 月 30 日，学生提出过：

- 人工模拟有错误的 tables；
- 刻意篡改已有项目结果；
- 把任务做成 supervised evaluation；
- 或先人工标注 100 篇，再微调小模型。

Mentor 的明确意见是：当前项目不需要先找出 100 篇已知有错的文章，也不需要把 supervised learning 作为主线。

建议的主流程是：

1. 收集真实发表的论文；
2. AI 自由识别潜在问题；
3. 要求 AI 清楚解释“哪里不一致、为什么是问题”；
4. 人工回到论文核实每一个 flag；
5. 统计论文中问题的出现情况、类型和可用性。

AI 可能漏掉问题，因此这种设计不能直接估计完整 sensitivity；但 AI 已提出的问题通常可以由算术、上下文或跨文档对照直接核实。参见 [6 月 30 日 transcript：unsupervised 设计](June-30/MeetingWithDrLin-06-30-2026_原文.txt#L420)。

### B. 审计对象

Mentor 更倾向于：

- individual original clinical studies；
- 优先考虑 RCT；
- 不以 meta-analysis 为主要样本，因为 meta-analysis 是对原始结果的再汇总，原始 study 出错会继续传递；
- 每篇同时纳入 main manuscript 和 supplementary materials；
- 流程图和其他图片也不一定排除，因为 Mentor 的经验是当前模型能读取其中数字并与正文比较。

### C. AI 的检查清单

会议中提到的具体 audit targets 包括：

- point estimate 是否落在 CI 内；
- p-value 与 CI 是否一致；
- CI 是否跨越 null value；
- OR 等变换尺度下的 CI 与 point estimate 是否合理；
- 同一 table 中是否出现可疑的重复 CI；
- 正文、表格和 supplement 的数值是否一致；
- 是否存在新旧分析版本混杂；
- flow chart 人数能否正确加减；
- randomized、excluded、dropout 与 analyzed 人数是否闭合；
- subgroup 加总是否等于总数；
- baseline table 中男女或其他类别加总是否等于 N；
- 图片数字与正文描述是否一致。

6 月 12 日所说的 “training” 更像是用 prompt/checklist 引导模型集中检查这些内容，不等于一定要 fine-tune 模型。

### D. Prompt 与运行方式

Mentor 的建议包括：

- 使用固定 prompt，保证每篇论文尽量同样处理；
- 要求模型不仅报告问题，还必须解释依据和待核实位置；
- 一篇一篇运行，而不是一次把 100 篇塞进去；
- subscription 界面处理过长输入时可能“偷懒”或省略内容；
- API 可能更适合批量任务，但成本和配置需再研究；
- 每篇通常一两分钟即可完成初次 audit；
- 把 AI 当筛查工具，最终仍需人工审核。

### E. 抽样与期刊方案

先后讨论过：

1. 随机抽取约 100 篇；
2. 选 JAMA 或 BMJ 等 top journal；
3. 只选 JAMA 正刊，不混入 JAMA 子刊；
4. JAMA RCT；
5. PLOS ONE 中的 RCT 或限定某个领域；
6. JAMA 与 PLOS ONE 做高水平/一般期刊对比；
7. 若期刊一年文章过多，可限一个月或几个月；
8. 可以使用 random sample，也可以用 convenience sample，但必须写清楚；
9. 实际数量不必机械达到 100，样本来源和合理性更重要。

### F. 时间/纵向比较

这个想法经历了明显变化：

- 6 月 12 日：考虑 2019 年等 AI 普及前论文，避免样本本身已由 AI 协助；
- 6 月 30 日：提出比较 2019 年与 2024/2025 年，观察 AI 普及前后错误率是否变化；
- 7 月 24 日：发现近一年 JAMA RCT 很少，若做到约 100 篇可能要回溯至 2019/2020 年；Mentor 开始质疑纵向比较是否会让项目变复杂；
- COVID 时期构成潜在 confounder：公共卫生紧急状态下研究和发表速度快，可能天然更容易出错；
- 最后立场是纵向比较可以做也可以不做，但必须解释时间范围：
  - 若纳入 COVID 年份，要讨论其特殊性；
  - 若从 2022/2023 年开始，要解释排除 COVID 高峰期；
  - 更简单的核心问题仍是：在已有 AI 工具的近期，发表的论文是否仍有可避免的问题。

7 月人工 note 也只留下了两个关键词：“AI-training”“longitudinal comparison”，说明该方向仍未最终定案。参见 [7 月 24 日 note](July-24/Meeting%20With%20Dr%20Lin%20Note%200724.txt#L31)。

### G. 数据收集自动化

Mentor 建议让 AI 或脚本：

- 遍历 JAMA 各 issue；
- 根据 title/abstract 判断是否符合 RCT inclusion criteria；
- 自动列出 eligible articles 和 DOI；
- 提高效率及 reproducibility。

但受版权墙和学校图书馆登录限制，PDF 与 supplement 未必能完全自动下载，可能仍需人工处理。

### H. 结果整理与人工审计

建议建立：

- 每篇文章的完整 AI 输出记录；
- 一张大的 summary table；
- 每一行对应论文及其问题；
- 问题类型、原始位置、AI 解释、人工核实结果；
- 详细逐条记录放 supplement；
- 主文汇总论文层面和问题类别层面的发现。

必须区分：

- candidate flag；
- 人工确认的问题；
- minor typo/reporting inconsistency；
- 可能影响结果解释的 substantive issue。

### I. 资源、隐私和合规

Mentor 重视以下问题：

- 审稿材料应使用不会拿输入训练模型的 business/team 版本，避免 data leakage；
- 曾考虑团队订阅、API 或短期 $200 Pro；
- Pro 账号不能多人共享，否则违反账号规则并可能被封；
- 学生个人订阅可能通过研究经费报销，但流程需向 Kevin/学校确认；
- Mentor 有一项包含 AI 工作的 funding proposal 在等待结果；如果未下来，也可能先从其他 account 支出；
- 预计建立 group plan，让参与项目的学生合法使用。

对于 2024 年中以后文章出现的 “all rights reserved，包括 text/data mining、AI training” 条款，Mentor 的初步判断是：非商业的学术审计可能类似 systematic review 中对论文数据的使用，不等于拿论文训练商业模型。但这只是会议中的初步理解，不是正式法律结论，仍需进一步核对。

## 四、全部 updates：时间线

### 6 月 12 日：项目首次成形

- Mentor 从真实审稿经验提出 AI result/data verification idea。
- 确立核心价值：发现人工容易漏掉的内部不一致。
- 初步审计范围包括正文、tables、supplement 和图片。
- 初步样本设想为约 100 篇临床研究/RCT。
- 考虑 JAMA、BMJ 等顶级期刊，以及 2019 年等 AI 普及前样本。
- 认为不必主要做模型比较；重点是展示 potential。
- 希望免费或低成本模型也能工作。
- 提醒项目应快速完成，因为模型更新很快。
- 让学生先写 plan，不必立即大规模运行。
- 承诺可提供 AI 经费与必要的下载帮手。
- 希望暑期推进，但优先级仍低于已有的主要 manuscript/methodology 项目。

### 6 月 30 日：研究问题与设计被收窄

- 学生查阅了 Mentor 以前参与的相似文章，并考虑 supervised/simulated-error 设计。
- Mentor 明确：unsupervised 就够，不必先建立 100 篇已知错误的 ground truth。
- 核心变成：AI 在自然发表论文中能否频繁产生可验证、实用的 flags。
- JAMA RCT：哪怕约 10% 有问题也具有价值，但零发现风险较高。
- PLOS ONE：更可能发现问题，但论文影响力和故事力度相对一般。
- 出现三个候选设计：
  - JAMA；
  - PLOS ONE；
  - 好期刊与一般期刊对比。
- 出现纵向比较设想：2019 versus 2024/2025。
- 计划样本约 100，但可按月份、年份、领域或随机抽样缩小。
- 让学生先写 protocol/collection/search plan。
- 确定文章为 applied paper，可用 Word 写作。
- 建议由 AI 初筛 eligible RCT、输出 DOI，再人工下载正文和 supplement。
- 定位为“顺手推进的小项目”，避免妨碍主要统计方法研究。

### 7 月 24 日：已经进入 pilot

- 项目已处理/收集约 20 篇文章。
- 当前设置为每篇最多报告 10 个问题。
- 20 篇共得到 111 条 candidate flags。
- 学生抽查了其中两篇、约十余条 flags，报告称基本都成立。
- 已看到的明确问题包括：
  - flow chart 人数加减不一致；
  - participant 消失但无解释；
  - baseline table 中 gender 加总与总人数不一致。
- Mentor 将这些视为真实但多数偏小的 reporting issues。
- 建议把每篇论文的问题整理进大型 summary table，并把详细清单放 supplement。
- 样本暂时聚焦 JAMA 正刊，不纳入子刊。
- 2025 年符合条件的 JAMA RCT 只有十几篇左右，因此可能扩展至 2022–2025 或 2023–2025。
- 不再坚持一定凑满 100 篇。
- 纵向比较仍未定；COVID period 被识别为重要 confounder。
- Mentor 更倾向保留一个简单核心：近期已有 AI 工具，论文仍然出现可避免的问题，说明 routine AI audit 尚未被充分利用。
- 当前个人 $20 订阅受到 token/usage 限制；开始讨论 team/business plan、短期 Pro 报销和 API。
- Mentor 认为 cost-effective model 能工作比只能依靠 $200 最强模型更有推广意义。
- 因 111 条 flags 的人工审核工作量较大，Mentor 同意增加协作者。
- 学生将 lead 项目并担任 first author；帮助人工审计的人可以作为第二、第三作者。参见 [7 月 24 日 transcript：pilot 与分工](July-24/MeetingWithDrLin-07-24-2026_Transcript.txt#L559)。

## 五、截至最后一次会议的实际状态

### 已经较明确的部分

- **方向**：AI 对真实医学论文做内部一致性审计；
- **设计**：以 unsupervised audit 为主，人工验证 AI flags；
- **当前期刊**：倾向 JAMA 正刊；
- **当前对象**：倾向 RCT/original clinical studies；
- **输入**：正文 + supplement，图片不必先排除；
- **pilot**：约 20 篇、111 条候选 flags；
- **初步人工抽查**：两篇中的 flags 大体有效；
- **输出**：主文汇总 + supplement 逐项记录；
- **作者安排**：学生 lead/first author，可增加人工审计协作者；
- **资源**：Mentor 愿意安排团队订阅或报销。

### 仍未最终决定的部分

- 最终样本量是否接近 100；
- 具体年份范围；
- 是否做 longitudinal comparison；
- 是否纳入 COVID 年份；
- 是否加入 PLOS ONE 或期刊质量对比；
- 使用普通 thinking model、最高级 Pro，还是两者做有限比较；
- 版权/AI-training restriction 的正式合规解释；
- 111 条 flags 的完整人工确认结果；
- 问题严重度分类和最终 primary outcome。

## 六、当前最关键的方法学提醒

目前的“111 个问题”仍应表述为 **111 个 AI-generated candidate flags**，不能直接写成 111 个 confirmed errors，原因包括：

1. 每篇最多输出 10 条，数量存在人为上限；
2. 目前只抽查了两篇，而非完整人工 adjudication；
3. 部分 flags 可能是合理的 reporting convention，而非真实错误；
4. minor typo、内部不一致和 substantive analytic error 必须分层；
5. unsupervised 设计可以验证 positive flags，但没有完整 ground truth 时不能直接估计 sensitivity 或 false-negative rate。

因此，下一阶段最关键的工作，是建立规范的人工 adjudication、问题分类、严重度分级及复核流程。
