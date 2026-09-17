#!/usr/bin/env python3
"""Build a bilingual meta-audit report from the 20 authoritative Markdown reports."""

from __future__ import annotations

import csv
import math
import re
import statistics
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "meta_report"

REPORTS = {
    "jama.2024.11057": "jama.2024.11057/.ai_paper_validation/final_report.md",
    "jama.2024.12829": "jama.2024.12829/.ai_paper_validation/final_report.md",
    "jama.2024.19585": "jama.2024.19585/.ai_paper_validation/human_adjudication_report.md",
    "jama.2024.2302": "jama.2024.2302/.ai_paper_validation/final_report.md",
    "jama.2024.240147": "jama.2024.240147/.ai_paper_validation/final_report.md",
    "jama.2024.24764": "jama.2024.24764/.ai_paper_validation/final_report.md",
    "jama.2024.4183": "jama.2024.4183/.ai_paper_validation/human_adjudication_report.md",
    "jama.2024.6063": "jama.2024.6063/.ai_paper_validation/final_report.md",
    "jama.2025.11178": "jama.2025.11178/.ai_paper_validation/final_report.md",
    "jama.2025.15440": "jama.2025.15440/.ai_paper_validation/final_report.md",
    "jama.2025.16450": "jama.2025.16450/.ai_paper_validation/final_report.md",
    "jama.2025.19563": "jama.2025.19563/.ai_paper_validation/final_report.md",
    "jama.2025.20765": "jama.2025.20765/.ai_paper_validation/final_report.md",
    "jama.2025.250116": "jama.2025.250116/.ai_paper_validation/final_report.md",
    "jama.2025.4390": "jama.2025.4390/.ai_paper_validation/final_report.md",
    "jama.2025.7583": "jama.2025.7583/.ai_paper_validation/final_report.md",
    "jama.2025.7710": "jama.2025.7710/.ai_paper_validation/final_report.md",
    "jama.2025.9110": "jama.2025.9110/.ai_paper_validation/final_report.md",
    "jama.2025.9663": "jama.2025.9663/.ai_paper_validation/final_report.md",
    "jamasurg.2025.4929": "jamasurg.2025.4929/.ai_paper_validation/final_report.md",
}

EXPECTED_COUNTS = {
    "jama.2024.11057": 2,
    "jama.2024.12829": 9,
    "jama.2024.19585": 3,
    "jama.2024.2302": 3,
    "jama.2024.240147": 8,
    "jama.2024.24764": 4,
    "jama.2024.4183": 9,
    "jama.2024.6063": 10,
    "jama.2025.11178": 10,
    "jama.2025.15440": 1,
    "jama.2025.16450": 4,
    "jama.2025.19563": 6,
    "jama.2025.20765": 8,
    "jama.2025.250116": 7,
    "jama.2025.4390": 7,
    "jama.2025.7583": 2,
    "jama.2025.7710": 2,
    "jama.2025.9110": 6,
    "jama.2025.9663": 5,
    "jamasurg.2025.4929": 5,
}

CATEGORIES = [
    "Arithmetic inconsistency",
    "Cross-document inconsistency",
    "Statistical reporting inconsistency",
    "Participant flow inconsistency",
    "Presentation inconsistency",
]

CATEGORY_ZH = {
    "Presentation inconsistency": "呈现不一致",
    "Statistical reporting inconsistency": "统计报告不一致",
    "Cross-document inconsistency": "跨文档不一致",
    "Arithmetic inconsistency": "算术不一致",
    "Participant flow inconsistency": "受试者流程不一致",
}

ARTICLE_SUMMARY_ZH = {
    "jama.2024.11057": "2项Minor：eTable 4把疑似均值（SD）格式标为中位数（IQR）；eTable 5的“7月应答者”标题覆盖了按随机化总体计算的行。",
    "jama.2024.12829": "3项Major：卒中差值的CI不含点估计；Figure S5的分母及致残性卒中计数冲突；Table S6混用了ITT与PPS。6项Minor集中在S7–S9表头/分母、中心人数、并发症计数和检验方法标签。",
    "jama.2024.19585": "3项Minor：eTable 10把OR标作difference；Figure 2未分时间点说明分母；eFigure 3图例未定义随估计值显示的P值。",
    "jama.2024.2302": "1项Major：摘要称320名婴儿接受手术，正文与流程图合计为281。2项Minor：流程图未明确随机后退出分支；入组信息误指向eTables 1–2而非仅eTable 1。",
    "jama.2024.240147": "1项Major：摘要/Key Points把分析或干预阶段人数称为随机人数。7项Minor包括中心百分比、4/743与0/747等算术错误、孤立脚注、图表间百分比差异及未说明的分母。",
    "jama.2024.24764": "4项Minor：多响应类别未说明；疫情亚组漏写“仅英国”；Figure 2缺少亚组分母/缺失信息；生活质量叙述与day-7的CI和P值不一致。",
    "jama.2024.4183": "2项Major：CNRT+含片剂量在主文与补充图间冲突；补充材料两处数值疑似小数点错位。7项Minor涉及流程算术/措辞、性别计数、效应方向、模拟功效单调性、分母及不良事件限定语。",
    "jama.2024.6063": "3项Major：eTable 4变化值块疑似复制错位、无关结局行整块重复、主表与补充表不良事件总数冲突。7项Minor包括估计符号、百分比、治疗臂对调、依从性、错误eTable引用及图版布局。",
    "jama.2025.11178": "3项Major：随访模式人数不守恒；7行CI排除0但P>.05；多处SMD点估计/CI/符号不可能。7项Minor涉及百分比、重复行/缺失水平标签、亚组表头、调整状态及均值/中位数措辞。",
    "jama.2025.15440": "1项Minor：相同卒中比较在摘要与正文/Figure 4B给出两套95% CI。",
    "jama.2025.16450": "4项Minor：GDB状态分母未披露；B+S列标题分母不符；Table 1与Figure 2的FIO2总数差1；RR被错误展开为risk difference。",
    "jama.2025.19563": "1项Major：Figure 3B展示的HbA1c人群明显大于eTable 14且未解释。5项Minor包括10/59百分比、三处eTable编号、年龄P值脚注、BMI误称weight及百分比/百分点混淆。",
    "jama.2025.20765": "2项Major：eTable 2遗漏一个40人mHealth集群；主文将两类不良事件方向写反。6项Minor包括死亡/不良事件百分比、未标人群、排除死亡后仍称ITT及表题与正文不符。",
    "jama.2025.250116": "2项Major：eFigure 8复制了eFigure 7的推断结果；高分层治疗OR被标作交互作用。5项Minor包括叙述计数、OR小数位、点估计落在CI外及表格字符重复/缺失。",
    "jama.2025.4390": "1项Major：Figure 3的“每100人年率”列实际装的是约71个百人年的观察时间。6项Minor包括种族行复制、调整/未调整CI标签、相同二分类计数不同P值、地区总数、依从性和重复百分比错误。",
    "jama.2025.7583": "2项Minor：对已排除患者使用“符合纳入标准”措辞；MAGIC-MT对照组事件数缺失。",
    "jama.2025.7710": "1项Major：同一主要结局分析单位在women、infants和patients之间冲突。1项Minor：安慰剂种族百分比在正文与Table 1使用不同分母规则。",
    "jama.2025.9110": "6项Minor：性别计数、方案偏离百分比、患者/ICU随机化措辞、两处mean(SD)与median(IQR)标签、以及Supplement 1/3定位错误。",
    "jama.2025.9663": "5项Minor：time-to-death误引eFigure 4；汇总表混用不同分析子集；年份截断；FiO2分数误标百分比；星号无定义。",
    "jamasurg.2025.4929": "2项Major：pN N3回归行内部不可能；主文把补充表的单变量估计称为多变量结果。3项Minor：年龄行和5个OR无法由单元格复算、CONSORT拒绝标签位置冲突。",
}

ARTICLE_SUMMARY_EN = {
    "jama.2024.11057": "Two Minor findings: eTable 4 labels mean(SD)-like values as median(IQR), and the eTable 5 responder-only title also covers randomized-denominator rows.",
    "jama.2024.12829": "Three Major findings: a stroke-difference CI excludes its point estimate; Figure S5 conflicts on denominator/disabling stroke counts; and Table S6 mixes ITT and PPS data. Six Minor findings concern S7–S9 headers/denominators, center counts, a complication count, and test-method labeling.",
    "jama.2024.19585": "Three Minor findings: eTable 10 labels an OR as a difference, Figure 2 does not state time-specific denominators, and the eFigure 3 legend fails to define displayed P values.",
    "jama.2024.2302": "One Major finding: the abstract says 320 infants underwent repair, whereas the article and flow diagram total 281. Two Minor findings concern an omitted withdrawal branch and an enrollment cross-reference that should point only to eTable 1.",
    "jama.2024.240147": "One Major finding: the abstract/Key Points call analyzed or intervention-stage populations randomized. Seven Minor findings include center percentages, 4/743 and 0/747 errors, an orphan footnote, cross-display percentages, and an undisclosed denominator.",
    "jama.2024.24764": "Four Minor findings: undisclosed multiple responses, an omitted UK-only subgroup restriction, missing subgroup denominators, and a quality-of-life narrative inconsistent with the day-7 CI/P value.",
    "jama.2024.4183": "Two Major findings: the CNRT+ lozenge dose conflicts across documents, and two supplemental values appear decimal-shifted. Seven Minor findings involve flow arithmetic/wording, sex counts, direction, power monotonicity, denominators, and adverse-event qualification.",
    "jama.2024.6063": "Three Major findings: a copied/incorrect change block, an unrelated row duplicated wholesale, and conflicting adverse-event totals. Seven Minor findings concern estimate sign, percentages, arm reversals, adherence, wrong eTable citations, and layout.",
    "jama.2025.11178": "Three Major findings: follow-up-pattern counts do not conserve N; seven CIs exclude zero while P>.05; and SMD estimates/CIs/signs are impossible. Seven Minor findings concern percentages, duplicate or missing labels, subgroup headers, adjustment status, and mean/median wording.",
    "jama.2025.15440": "One Minor finding: the same stroke comparison has different 95% CIs in the abstract and the Results/Figure 4B.",
    "jama.2025.16450": "Four Minor findings: undisclosed GDB denominators, a B+S header mismatch, a one-person FIO2 discrepancy between Table 1 and Figure 2, and RR expanded as risk difference.",
    "jama.2025.19563": "One Major finding: Figure 3B visibly uses a larger HbA1c population than eTable 14 without explanation. Five Minor findings concern 10/59, three wrong eTable numbers, age-P-value footnotes, BMI called weight, and percent versus percentage points.",
    "jama.2025.20765": "Two Major findings: a 40-person mHealth cluster is omitted and adverse-event direction is reversed in prose. Six Minor findings cover death/adverse-event percentages, an unidentified population, death-excluded ITT wording, and a title/body mismatch.",
    "jama.2025.250116": "Two Major findings: eFigure 8 repeats eFigure 7 inference values, and high-stratum treatment ORs are labeled interactions. Five Minor findings concern a narrative count, OR decimal error, a point estimate outside its CI, and duplicated/missing table characters.",
    "jama.2025.4390": "One Major finding: Figure 3 columns labeled rates per 100 patient-years contain about 71 hundreds of patient-years. Six Minor findings include a duplicated ethnicity row, adjusted/unadjusted CI labeling, identical counts with different P values, geography totals, adherence, and a repeated percentage error.",
    "jama.2025.7583": "Two Minor findings: inclusion wording is applied to excluded patients, and the MAGIC-MT control event count is missing.",
    "jama.2025.7710": "One Major finding: the same primary-outcome analysis unit is called women, infants, and patients. One Minor finding: prose and Table 1 use different placebo-ethnicity denominator conventions.",
    "jama.2025.9110": "Six Minor findings: sex counts, a protocol-deviation percentage, patient-versus-ICU randomization wording, two mean(SD)/median(IQR) labels, and a Supplement 1/3 locator.",
    "jama.2025.9663": "Five Minor findings: a wrong eFigure citation, mixed analytic subsets in a summary, a truncated year, FiO2 fractions labeled percentages, and an undefined asterisk.",
    "jamasurg.2025.4929": "Two Major findings: the pN N3 regression row is internally impossible, and a univariate estimate is presented as multivariable. Three Minor findings concern the age row, five unreproducible ORs, and a CONSORT refusal label.",
}

MAJOR_LABELS = {
    ("jama.2024.12829", "1"): (
        "卒中发生差的95% CI不包含其点估计",
        "Stroke incidence-difference CI excludes its point estimate",
    ),
    ("jama.2024.12829", "2"): (
        "Figure S5分母及致残性卒中计数与Table S11冲突",
        "Figure S5 conflicts with its denominator and Table S11 disabling-stroke counts",
    ),
    ("jama.2024.12829", "3"): (
        "Table S6在同一行混用ITT与PPS数据",
        "Table S6 mixes ITT and PPS data",
    ),
    ("jama.2024.2302", "C1"): (
        "摘要把术后退出后的320人误写为接受手术者；实际281人",
        "Abstract mislabels the 320 postwithdrawal cohort as repaired; actual repair total is 281",
    ),
    ("jama.2024.240147", "F1"): (
        "随机化、干预阶段和分析人群在摘要/Key Points中混称",
        "Randomized, intervention-stage, and analyzed populations are conflated",
    ),
    ("jama.2024.4183", "C04"): (
        "CNRT+含片剂量在主文与补充图间为2 mg/4 mg",
        "CNRT+ lozenge dose conflicts as 2 mg versus 4 mg",
    ),
    ("jama.2024.4183", "C08"): (
        "补充材料两处估计/区间疑似小数点错位",
        "Two supplemental estimates/intervals appear decimal-shifted",
    ),
    ("jama.2024.6063", "C04"): (
        "eTable 4疼痛变化值块与无关功能行重复且不合端点",
        "eTable 4 pain-change block duplicates an unrelated function row and conflicts with endpoints",
    ),
    ("jama.2024.6063", "C05"): (
        "下肢力量推断块与背痛行完全重复",
        "Lower-leg-strength inference block exactly duplicates a back-pain row",
    ),
    ("jama.2024.6063", "C07"): (
        "主表与eTable 7不良事件总数相差5例",
        "Main Table and eTable 7 adverse-event totals differ by five",
    ),
    ("jama.2025.11178", "1"): (
        "随访模式单元格总数超过随机化和随访总人数",
        "Follow-up-pattern cells exceed randomized and followed totals",
    ),
    ("jama.2025.11178", "2"): (
        "7行95% CI排除0但配对P值均大于.05",
        "Seven 95% CIs exclude zero while paired P values exceed .05",
    ),
    ("jama.2025.11178", "4"): (
        "多处SMD点估计落在CI外、端点逆序或符号相反",
        "Multiple SMDs fall outside CIs, have reversed endpoints, or opposite signs",
    ),
    ("jama.2025.19563", "C-06"): (
        "Figure 3B的HbA1c分析人群大于eTable 14且未解释",
        "Figure 3B uses a larger HbA1c analysis population than eTable 14 without explanation",
    ),
    ("jama.2025.20765", "F01"): (
        "eTable 2遗漏一个40人mHealth集群",
        "eTable 2 omits a 40-participant mHealth cluster",
    ),
    ("jama.2025.20765", "F02"): (
        "主文把irritability和anxiety的不良事件方向写反",
        "Prose reverses the direction of irritability and anxiety events",
    ),
    ("jama.2025.250116", "C04"): (
        "eFigure 8复制eFigure 7推断值但事件单元格不同",
        "eFigure 8 repeats eFigure 7 inference values despite different event cells",
    ),
    ("jama.2025.250116", "C05"): (
        "高分层治疗OR被标为交互作用并在正文中据此解释",
        "High-stratum treatment ORs are labeled and interpreted as interactions",
    ),
    ("jama.2025.4390", "SCI-01"): (
        "Figure 3“率”列实际为观察人时",
        "Figure 3 rate columns contain person-time",
    ),
    ("jama.2025.7710", "1"): (
        "主要结局分析单位在women、infants和patients之间冲突",
        "Primary-outcome analysis unit conflicts among women, infants, and patients",
    ),
    ("jamasurg.2025.4929", "F-01"): (
        "pN N3回归行的计数、百分比、OR、CI和P值内部不可能",
        "pN N3 row is internally incompatible across counts, percentage, OR, CI, and P value",
    ),
    ("jamasurg.2025.4929", "F-04"): (
        "主文把单变量approach估计称为多变量独立预测结果",
        "Main text presents a univariate approach estimate as multivariable",
    ),
}


def clean_md(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("`", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def scientific_section(text: str) -> str:
    start = re.search(
        r"^#{1,3}\s+(?:\d+\.\s*)?(?:Scientific Findings|Scientific Issues|Final scientific issues)\s*$",
        text,
        flags=re.M | re.I,
    )
    if not start:
        raise ValueError("Scientific findings section not found")
    rest = text[start.end() :]
    end = re.search(
        r"^(?:#{1,3}\s+(?:\d+\.\s*)?(?:Rejected and Uncertain Candidates|Disposition summary|"
        r"AI Training Restriction Summary)|Excluded from the scientific list:)",
        rest,
        flags=re.M | re.I,
    )
    return rest[: end.start()] if end else rest


def split_findings(section: str) -> list[str]:
    lines = section.splitlines()
    starts = []
    for i, line in enumerate(lines):
        if re.match(r"^#{2,4}\s+", line):
            starts.append(i)
        elif re.match(r"^\d+\.\s+\*\*", line):
            starts.append(i)
    if not starts:
        return []
    parts = []
    for j, start in enumerate(starts):
        end = starts[j + 1] if j + 1 < len(starts) else len(lines)
        parts.append("\n".join(lines[start:end]).strip())
    return parts


def infer_category(segment: str) -> str:
    for category in CATEGORIES:
        if re.search(re.escape(category), segment, flags=re.I):
            return category
    raise ValueError(f"Category not found in: {segment[:180]}")


def infer_severity(segment: str) -> str:
    head = "\n".join(segment.splitlines()[:8])
    major = bool(re.search(r"\bMajor\b", head, flags=re.I))
    minor = bool(re.search(r"\bMinor\b", head, flags=re.I))
    if major and not minor:
        return "Major"
    if minor and not major:
        return "Minor"
    raise ValueError(f"Severity ambiguous in: {head[:300]}")


def infer_id_title(segment: str, index: int) -> tuple[str, str]:
    first = clean_md(segment.splitlines()[0])
    first = re.sub(r"^#{2,4}\s*", "", first)
    first = re.sub(r"^\d+\.\s*", "", first)
    ids = re.findall(r"\b(?:C|F|V|SCI|TAC|FFC)[-_]?\d+\b", first, flags=re.I)
    finding_id = ids[0].upper() if ids else str(index)
    # Prefer a heading-style descriptive title; otherwise use the first evidence/value sentence.
    title = first
    title = re.sub(
        r"^(?:[A-Z]+[-_]?\d+\s*[—-]\s*)?(?:Major|Minor)\s*[—-]\s*", "", title
    )
    title = re.sub(
        r"^(?:[A-Z]+[-_]?\d+\s*[—-]\s*)?"
        r"(?:Arithmetic|Cross-document|Statistical reporting|Participant flow|Presentation)"
        r" inconsistency\s*[—:/-]\s*(?:Major|Minor)?\s*",
        "",
        title,
        flags=re.I,
    )
    if not title or title.lower().startswith(
        ("category:", "category / severity:", "category /")
    ):
        candidates = []
        for line in segment.splitlines()[1:]:
            plain = clean_md(line.lstrip("- "))
            if plain.lower().startswith(
                (
                    "compared values",
                    "source evidence",
                    "values/statements",
                    "compared statements",
                    "source evidence",
                )
            ):
                candidates.append(plain.split(":", 1)[-1].strip())
        title = candidates[0] if candidates else first
    title = re.sub(r"^(?:[A-Z]+[-_]?\d+\s*[—-]\s*)", "", title)
    return finding_id, title[:220]


def artifact_tags(segment: str) -> list[str]:
    """Multi-label reporting loci inferred from each accepted finding's full evidence text."""
    s = clean_md(segment).lower()
    tags = []
    if re.search(r"\babstract\b|\bkey points\b|\bnarrative\b|\bprose\b|\bresults text\b|\bmain text\b", s):
        tags.append("Narrative/abstract")
    if re.search(r"\btable 1\b|\bbaseline (?:table|measures|characteristics)\b", s):
        tags.append("Table 1/baseline")
    if re.search(r"\betable\b|\be-table\b", s):
        tags.append("Supplementary table")
    if re.search(r"\befigure\b|\be-figure\b", s):
        tags.append("Supplementary figure")
    if re.search(r"\bfigure 1\b|\bconsort\b|\bparticipant flow\b|\bflow (?:diagram|figure)\b", s):
        tags.append("Flow diagram")
    if re.search(r"\bfigure\b", s) and "Flow diagram" not in tags:
        tags.append("Other figure")
    if re.search(r"\btable\b", s) and "Table 1/baseline" not in tags and "Supplementary table" not in tags:
        tags.append("Other main table")
    if not tags:
        tags.append("Other/unspecified")
    return tags


def mechanism_tags(segment: str) -> list[str]:
    """Multi-label issue mechanisms used for the text-mining section."""
    s = clean_md(segment).lower()
    tags = []
    rules = [
        ("Denominator/population", r"denominator|population|analysis set|analysis unit|missing|complete-case|itt\b|per-protocol|\bpp\b"),
        ("Count/percentage arithmetic", r"recalculat|recompute|\b\d+\s*/\s*\d+|percentage|percentages|does not reconcile|do not reconcile|sum to|total"),
        ("CI/point-estimate compatibility", r"confidence interval|\b95% ci\b|\bci\b.*(?:exclude|outside|endpoint|limit)|point estimate"),
        ("P value/test labeling", r"\bp[ =<]\s*\.?\d|p value|p-value|chi-square|fisher|statistical test|significant"),
        ("Effect measure/model label", r"odds ratio|relative risk|risk difference|rate ratio|hazard ratio|interaction|univariate|multivariable|adjusted|unadjusted|model"),
        ("Summary-statistic/unit label", r"mean \(sd\)|median \(iqr\)|mean difference|median difference|unit|percentage points|fraction|rate per"),
        (
            "Cross-reference/citation",
            r"cross-reference|citation|cites? .*?(?:etable|efigure)|"
            r"refers? to unrelated|"
            r"document locator|table numbers do not match|supplement 1 although",
        ),
        ("Duplicate/transposed content", r"duplicate|duplicat|identical|repeats?|arm-reversed|reversed|copied"),
        ("Participant-flow wording", r"randomized|withdraw|excluded|enrollment|flow|consort|follow-up"),
        ("Footnote/title/caption/legend", r"footnote|title|caption|legend|heading|header|marker|asterisk"),
    ]
    for label, pattern in rules:
        if re.search(pattern, s):
            tags.append(label)
    return tags or ["Other wording/definition"]


def parse_reports() -> list[dict[str, str]]:
    rows = []
    for article, relpath in REPORTS.items():
        path = ROOT / relpath
        text = path.read_text(encoding="utf-8")
        try:
            section = scientific_section(text)
        except ValueError as exc:
            raise ValueError(f"{article}: {exc}") from exc
        parts = split_findings(section)
        if len(parts) != EXPECTED_COUNTS[article]:
            raise ValueError(
                f"{article}: parsed {len(parts)} findings, expected {EXPECTED_COUNTS[article]}"
            )
        for index, segment in enumerate(parts, 1):
            finding_id, title = infer_id_title(segment, index)
            rows.append(
                {
                    "article": article,
                    "finding_id": finding_id,
                    "severity": infer_severity(segment),
                    "category": infer_category(segment),
                    "title": title,
                    "artifact_tags": "; ".join(artifact_tags(segment)),
                    "mechanism_tags": "; ".join(mechanism_tags(segment)),
                    "source_report": relpath,
                    "evidence_text": clean_md(segment),
                }
            )
    return rows


def write_csv(rows: list[dict[str, str]]) -> None:
    path = OUT / "audit_findings.csv"
    fields = list(rows[0])
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def pct(n: int, d: int) -> str:
    return f"{100 * n / d:.1f}%"


def wilson(x: int, n: int, z: float = 1.959963984540054) -> tuple[float, float]:
    p = x / n
    den = 1 + z * z / n
    center = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return center - half, center + half


def md_escape(value: object) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")


def md_table(headers: list[str], rows: list[list[object]], aligns: list[str] | None = None) -> str:
    if aligns is None:
        aligns = ["---"] * len(headers)
    output = [
        "| " + " | ".join(md_escape(x) for x in headers) + " |",
        "| " + " | ".join(aligns) + " |",
    ]
    output.extend("| " + " | ".join(md_escape(x) for x in row) + " |" for row in rows)
    return "\n".join(output)


def counts_by_article(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    result = []
    for article in REPORTS:
        subset = [r for r in rows if r["article"] == article]
        major = sum(r["severity"] == "Major" for r in subset)
        minor = len(subset) - major
        result.append({"article": article, "Major": major, "Minor": minor, "Total": len(subset)})
    return result


def tag_summary(rows: list[dict[str, str]], field: str) -> list[tuple[str, int, int]]:
    tags = Counter()
    papers: dict[str, set[str]] = {}
    for row in rows:
        for tag in row[field].split("; "):
            tags[tag] += 1
            papers.setdefault(tag, set()).add(row["article"])
    return [(tag, count, len(papers[tag])) for tag, count in tags.most_common()]


def yaml_header(language: str) -> str:
    if language == "zh":
        title = "20篇JAMA系列论文报告一致性审计：汇总与统计分析"
        subtitle = "基于最终保留的Major与Minor问题"
        lang_line = "lang: zh-CN"
    else:
        title = "Reporting-Consistency Audit of 20 JAMA-Family Articles"
        subtitle = "Synthesis and statistical analysis of retained Major and Minor findings"
        # The local minimal TeX distribution does not include Babel's American module.
        lang_line = ""
    return f"""---
title: "{title}"
subtitle: "{subtitle}"
date: "2026-07-23"
{lang_line}
documentclass: article
fontsize: 10pt
geometry:
  - top=20mm
  - bottom=21mm
  - left=20mm
  - right=20mm
mainfont: "Noto Serif CJK SC"
sansfont: "Noto Sans CJK SC"
monofont: "Noto Sans Mono CJK SC"
colorlinks: true
linkcolor: "2B5D86"
urlcolor: "2B5D86"
toc: true
toc-depth: 2
numbersections: true
header-includes:
  - |
    \\usepackage{{booktabs}}
    \\usepackage{{longtable}}
    \\usepackage{{array}}
    \\usepackage{{float}}
---
"""


def build_report_zh(rows: list[dict[str, str]]) -> str:
    n_findings = len(rows)
    article_rows = counts_by_article(rows)
    n_major = sum(r["severity"] == "Major" for r in rows)
    n_minor = n_findings - n_major
    major_papers = sum(r["Major"] > 0 for r in article_rows)
    totals = [int(r["Total"]) for r in article_rows]
    lo_any, hi_any = wilson(20, 20)
    lo_major_p, hi_major_p = wilson(major_papers, 20)
    lo_major_i, hi_major_i = wilson(n_major, n_findings)

    cat_rows = []
    for category, count in Counter(r["category"] for r in rows).most_common():
        subset = [r for r in rows if r["category"] == category]
        majors = sum(r["severity"] == "Major" for r in subset)
        cat_rows.append(
            [
                CATEGORY_ZH[category],
                count,
                pct(count, n_findings),
                majors,
                pct(majors, count),
                len({r["article"] for r in subset}),
            ]
        )

    article_table = md_table(
        ["论文包", "Major", "Minor", "合计"],
        [[r["article"], r["Major"], r["Minor"], r["Total"]] for r in article_rows],
        ["---", "---:", "---:", "---:"],
    )
    category_table = md_table(
        ["审计类别", "问题数", "占111项", "Major数", "类别内Major占比", "涉及论文数"],
        cat_rows,
        ["---", "---:", "---:", "---:", "---:", "---:"],
    )
    artifact_zh = {
        "Supplementary table": "补充表（eTable）",
        "Narrative/abstract": "正文叙述/摘要",
        "Other figure": "其他主文图",
        "Other main table": "其他主文表",
        "Flow diagram": "流程图/CONSORT图",
        "Supplementary figure": "补充图（eFigure）",
        "Table 1/baseline": "Table 1/基线表",
        "Other/unspecified": "其他/未特指",
    }
    artifact_table = md_table(
        ["载体/位置（多标签）", "涉及问题数", "涉及论文数"],
        [[artifact_zh.get(t, t), n, p] for t, n, p in tag_summary(rows, "artifact_tags")],
        ["---", "---:", "---:"],
    )
    mechanism_zh = {
        "Count/percentage arithmetic": "计数/百分比复算",
        "Denominator/population": "分母/分析人群",
        "Footnote/title/caption/legend": "脚注/标题/图注/图例",
        "Cross-reference/citation": "交叉引用/文献定位",
        "P value/test labeling": "P值/检验标签",
        "Participant-flow wording": "受试者流程措辞",
        "Summary-statistic/unit label": "汇总统计量/单位标签",
        "Duplicate/transposed content": "复制/转置/重复内容",
        "Effect measure/model label": "效应量/模型标签",
        "CI/point-estimate compatibility": "CI/点估计相容性",
        "Other wording/definition": "其他措辞/定义",
    }
    mechanism_table = md_table(
        ["词典主题（多标签）", "命中问题数", "涉及论文数"],
        [[mechanism_zh.get(t, t), n, p] for t, n, p in tag_summary(rows, "mechanism_tags")],
        ["---", "---:", "---:"],
    )

    major_list = []
    for row in rows:
        if row["severity"] != "Major":
            continue
        key = (row["article"], row["finding_id"])
        if key not in MAJOR_LABELS:
            raise KeyError(f"Missing Major label: {key}")
        major_list.append(
            [
                row["article"],
                row["finding_id"],
                CATEGORY_ZH[row["category"]],
                MAJOR_LABELS[key][0],
            ]
        )

    parts = [yaml_header("zh")]
    parts.append(
        f"""
# 摘要

本报告汇总根目录下20个论文审计包的权威终稿：18份
`final_report.md`及2份优先级更高的`human_adjudication_report.md`。仅纳入
“Scientific Findings/Scientific Issues”中的最终保留问题；Rejected、Uncertain、
合规筛查和候选阶段问题均不计入。

20篇论文均至少有1项最终保留问题（100%，Wilson 95% CI
{lo_any*100:.1f}%–{hi_any*100:.1f}%）。共计{n_findings}项，其中Major
{n_major}项（{pct(n_major, n_findings)}；Wilson 95% CI
{lo_major_i*100:.1f}%–{hi_major_i*100:.1f}%），Minor {n_minor}项
（{pct(n_minor, n_findings)}）。{major_papers}/20篇含至少1项Major
（{pct(major_papers,20)}；Wilson 95% CI {lo_major_p*100:.1f}%–
{hi_major_p*100:.1f}%）。

最常见审计类别是呈现不一致（49项，44.1%），但跨文档不一致虽然只有17项，
其中8项为Major（47.1%），是Major密度最高的主要类别。按报告载体进行多标签
文本编码时，补充表参与69项问题、覆盖18篇论文，是最集中的风险区域。流程图
参与15项问题、覆盖10篇论文；但只有5项被正式归入“受试者流程不一致”，说明
流程图还经常承载分母、标签和跨文档问题。

> 结论口径：这里的“问题”是各审计终稿中**保留并提交人工裁决**的问题，
> 不等同于已经完成作者确认或更正的事实错误。

# 数据与方法

## 纳入与权威文件选择

- 共20个审计包：19篇JAMA、1篇JAMA Surgery；8个包名为2024，12个为2025。
- 若存在`human_adjudication_report.md`，优先于`final_report.md`；本次为
  `jama.2024.19585`和`jama.2024.4183`。
- 每份报告只截取最终科学问题区段；Rejected和Uncertain不进入分子。
- 同一问题只能计入一个正式审计类别，但载体位置和文本主题允许多标签。
- 完整逐问题账本见`meta_report/audit_findings.csv`，含111行、来源报告路径和
  规范化证据文本。

## 统计方法

计数、比例、均值、中位数、四分位数和范围均由逐问题账本计算。论文层面比例
给出Wilson 95%置信区间。文本挖掘采用预先编写的规则词典，对每个已接受问题的
标题、位置、比较值、依据与核验说明进行多标签编码；因此“涉及问题数”表示该
载体或主题出现在证据链中，不一定是唯一根因，也不能相加为111。

一个关键限制是每篇审计最多保留10项最终问题；本样本有2篇正好达到10项。
因此{n_findings}是“最终优先保留问题数”，不是所有可发现瑕疵的无上限总数。

# 数值结果

## 论文层面负担

每篇问题数均值为{statistics.mean(totals):.2f}，标准差
{statistics.stdev(totals):.2f}；中位数{statistics.median(totals):.1f}，
四分位距3–8，范围1–10。2024包为48项/8篇（均值6.00；Major 10项），
2025包为63项/12篇（均值5.25；Major 12项）。这只是描述性比较；样本不是随机
抽样，年份与审计复杂度、补充材料体量及审计成熟度混杂。

![各论文Major与Minor问题数。颜色堆叠总高为最终保留问题数。](figures/article_findings.pdf){{ width=92% }}

{article_table}

## 错误类型汇总

{category_table}

![正式审计类别及严重度。](figures/category_severity.pdf){{ width=92% }}

最值得注意的不是单纯“最多”，而是严重度结构：跨文档不一致8/17为Major，
受试者流程不一致2/5为Major；相比之下，呈现不一致虽数量最大，但Major为6/49，
算术不一致只有1/16为Major。也就是说，高频小错主要集中在呈现层，而一旦主文、
补充材料、图表或分析人群之间出现实质冲突，更容易升级为Major。

![20篇论文的类别谱。每格为该论文在该类别的最终保留问题数。](figures/category_heatmap.pdf){{ width=96% }}

# 常见出问题的位置

{artifact_table}

![问题证据链涉及的载体。一个问题可同时涉及多个载体。](figures/artifact_involvement.pdf){{ width=92% }}

## 补充表与Table 1

补充表是最突出的薄弱点：69/111项问题的证据链涉及eTable，覆盖18/20篇。
常见模式包括表头分母与单元格百分比不一致、ITT/PPS/安全集混用、重复或错位
复制、效应量/模型标签错误、脚注与表体不一致。Table 1/基线表参与9项问题、
覆盖9篇，典型例子是性别计数不守恒、FIO2总数在Table 1与Figure 2间差1、
钙通道阻滞剂百分比重复错误、种族百分比使用不同分母规则。

## 流程图

流程图/CONSORT图参与15项问题、覆盖10篇；正式“受试者流程不一致”只有5项、
覆盖4篇。两组数不同是因为流程图还会触发呈现、跨文档与统计人群问题。高价值
检查包括：逐节点守恒；区分randomized、treated、followed、analyzed；明确随机
后退出/失访分支；确认随机化单位（患者还是集群）；核对图中术语是否与正文和
Table 2分析集一致。

## 正文、图、脚注和cross-reference

正文/摘要参与28项问题、覆盖15篇；其他主文图参与22项、其他主文表参与21项。
人工复核确认至少5项明确的cross-reference定位错误：`jama.2024.2302`、
`jama.2024.6063`、`jama.2025.19563`、`jama.2025.9110`和
`jama.2025.9663`。此外，词典编码显示脚注/标题/图注/图例是高频主题，说明
生产环节的语义标签与数值本身同样需要独立核对。

# 统计显著性、CI、P值与概念定义

## 置信区间

人工复核定位出7项以CI错误或CI相容性为核心的问题，涉及
`jama.2024.12829`、`jama.2024.4183`、`jama.2025.11178`（2项）、
`jama.2025.15440`、`jama.2025.250116`及`jamasurg.2025.4929`。
模式包括点估计落在CI外、CI端点逆序、相同比较在摘要/正文给出不同CI，以及
CI与P值的零假设结论不一致。最严重的集中实例是`jama.2025.11178`：7行95%
CI排除0但P值均大于.05，且另有多处SMD点估计落在其CI外。

## P值与检验方法

至少5项问题把P值或检验方法作为核心矛盾：`jama.2024.12829`的“Chi-square”
行实际复现Fisher exact；`jama.2024.24764`的生活质量“不存在差异”叙述与
day-7 P=.02/CI排除0冲突；`jama.2025.11178`出现成组CI–P不一致；
`jama.2025.19563`同一年龄效应有两套P值脚注；`jama.2025.4390`相同的
二分类计数给出不同P值。这里应区分“P值计算错误”“检验方法标签错误”和
“叙述未限定全局交互/时间点比较”三类，不宜合并成单一统计错误。

## 文本与概念定义

文本挖掘显示，分母/分析人群、脚注/标题/图注、效应量/模型名称、汇总统计量/
单位标签均反复出现。典型概念性错误包括：OR被标为difference、RR被展开为
risk difference、单变量估计被称为多变量、分层内治疗OR被称为interaction、
median(IQR)被标为mean(SD)、FiO2分数被标为百分比，以及同一分析单位被称作
women/infants/patients。这类错误常不改变单元格数字，却直接改变读者对估计量、
人群或统计模型的理解。

{mechanism_table}

# 22项Major问题

{md_table(["论文包", "问题ID", "类别", "Major问题摘要"], major_list,
          ["---", "---", "---", "---"])}

# 逐篇汇总（Major与Minor均纳入）
"""
    )
    for row in article_rows:
        parts.append(
            f"""
## {row['article']}

**Major {row['Major']}；Minor {row['Minor']}；合计 {row['Total']}。**

{ARTICLE_SUMMARY_ZH[row['article']]}
"""
        )
    parts.append(
        """
# 解释、局限与建议

1. **优先审计补充表。** 对每个eTable执行列级分母推断、百分比复算、效应量/
   CI/P值三元组检查，以及相邻行重复块检测。
2. **把人群阶段做成显式数据字典。** randomized、treated、safety、ITT、
   complete-case、PPS及death-excluded不能只靠上下文推断。
3. **图表应与生成数据反向核验。** 尤其是流程图守恒、Figure列标题/单位、
   eFigure复制粘贴和图注统计量定义。
4. **cross-reference做机器化链接检查。** 主文中的eTable/eFigure/Supplement
   编号应与实际标题和文件位置建立一一映射。
5. **统计一致性应做成发布前门禁。** 点估计必须落在CI内；双侧P值、CI与零假设
   结论应一致；相同2×2单元格在相同方法下不得产生不同P值；调整状态和模型名称
   必须与输出一致。

本分析受以下限制：每篇最多10项的上限造成右删失；审计包并非随机样本；不同包
的文档数量、OCR质量和审计范围不同；报告类别由原审计定义，文本主题为规则词典
多标签编码；终稿中的“accepted/retained”仍待或已提交人工裁决，不能直接解释为
作者已确认的勘误。

# 可追溯输出

- `meta_report/audit_findings.csv`：111项逐问题账本。
- `meta_report/article_counts.csv`：论文层面Major/Minor计数。
- `meta_report/category_counts.csv`：类别×严重度计数。
- `meta_report/artifact_counts.csv`：载体多标签统计。
- `meta_report/mechanism_counts.csv`：文本主题多标签统计。
- `meta_report/generate_report.py`与`meta_report/analysis.R`：可复算脚本。

权威来源报告如下：
"""
    )
    parts.extend(f"- `{article}`：`{path}`" for article, path in REPORTS.items())
    return "\n".join(parts)


def build_report_en(rows: list[dict[str, str]]) -> str:
    n_findings = len(rows)
    article_rows = counts_by_article(rows)
    n_major = sum(r["severity"] == "Major" for r in rows)
    n_minor = n_findings - n_major
    major_papers = sum(r["Major"] > 0 for r in article_rows)
    totals = [int(r["Total"]) for r in article_rows]
    lo_any, hi_any = wilson(20, 20)
    lo_major_p, hi_major_p = wilson(major_papers, 20)
    lo_major_i, hi_major_i = wilson(n_major, n_findings)

    cat_rows = []
    for category, count in Counter(r["category"] for r in rows).most_common():
        subset = [r for r in rows if r["category"] == category]
        majors = sum(r["severity"] == "Major" for r in subset)
        cat_rows.append(
            [category, count, pct(count, n_findings), majors, pct(majors, count),
             len({r["article"] for r in subset})]
        )
    article_table = md_table(
        ["Article package", "Major", "Minor", "Total"],
        [[r["article"], r["Major"], r["Minor"], r["Total"]] for r in article_rows],
        ["---", "---:", "---:", "---:"],
    )
    category_table = md_table(
        ["Audit category", "Findings", "Share of 111", "Major", "Major within category", "Articles"],
        cat_rows,
        ["---", "---:", "---:", "---:", "---:", "---:"],
    )
    artifact_table = md_table(
        ["Artifact/location (multi-label)", "Finding mentions", "Articles"],
        [[t, n, p] for t, n, p in tag_summary(rows, "artifact_tags")],
        ["---", "---:", "---:"],
    )
    mechanism_table = md_table(
        ["Dictionary theme (multi-label)", "Finding hits", "Articles"],
        [[t, n, p] for t, n, p in tag_summary(rows, "mechanism_tags")],
        ["---", "---:", "---:"],
    )
    major_list = []
    for row in rows:
        if row["severity"] != "Major":
            continue
        key = (row["article"], row["finding_id"])
        if key not in MAJOR_LABELS:
            raise KeyError(f"Missing Major label: {key}")
        major_list.append(
            [row["article"], row["finding_id"], row["category"], MAJOR_LABELS[key][1]]
        )

    parts = [yaml_header("en")]
    parts.append(
        f"""
# Executive summary

This report synthesizes the authoritative final Markdown report in each of 20 article
audit packages: 18 `final_report.md` files and two higher-priority
`human_adjudication_report.md` files. Only retained items in the final Scientific
Findings/Scientific Issues section were counted. Rejected, Uncertain, compliance-screen,
and candidate-stage items were excluded.

All 20 articles had at least one retained finding (100%; Wilson 95% CI
{lo_any*100:.1f}%–{hi_any*100:.1f}%). There were {n_findings} findings: {n_major}
Major ({pct(n_major,n_findings)}; Wilson 95% CI {lo_major_i*100:.1f}%–
{hi_major_i*100:.1f}%) and {n_minor} Minor ({pct(n_minor,n_findings)}).
{major_papers}/20 articles had at least one Major finding ({pct(major_papers,20)};
Wilson 95% CI {lo_major_p*100:.1f}%–{hi_major_p*100:.1f}%).

Presentation inconsistency was the most frequent formal category (49; 44.1%).
Cross-document inconsistency was less common (17) but 8/17 were Major (47.1%),
the highest Major density among the main categories. Multi-label artifact coding found
supplementary tables in the evidence chain of 69 findings across 18 articles, making
them the clearest concentration of risk. Flow diagrams were involved in 15 findings
across 10 articles, although only five findings were formally categorized as participant
flow inconsistency; the remainder concerned denominators, labels, or cross-document
alignment.

> Interpretation: “finding” means retained in the audit report and submitted for human
> adjudication. It does not necessarily mean author-confirmed error or completed correction.

# Data and methods

## Inclusion and source selection

- The 20 packages comprise 19 JAMA articles and one JAMA Surgery article; eight package
  IDs are from 2024 and 12 from 2025.
- A `human_adjudication_report.md` was preferred when present
  (`jama.2024.19585` and `jama.2024.4183`); otherwise `final_report.md` was used.
- Only final retained scientific findings were parsed. Rejected and Uncertain items
  were excluded from numerators.
- Each finding has one formal audit category, while artifact locations and text themes
  are multi-label.
- The complete 111-row ledger is `meta_report/audit_findings.csv`, including the source
  report path and normalized evidence text.

## Analysis

Counts, proportions, mean, median, quartiles, and range were calculated from the
finding-level ledger. Wilson 95% confidence intervals are reported for article-level
proportions. Text mining used a rule-based dictionary over each accepted finding's
title, locations, compared values, basis, and verification instructions. Thus an
artifact/theme count means involvement in the evidence chain, not necessarily the sole
root cause, and multi-label totals do not sum to 111.

Each audit could retain no more than 10 final findings; two articles reached that cap.
The total of {n_findings} is therefore the count of prioritized final findings, not an
uncapped inventory of every detectable defect.

# Quantitative results

## Burden by article

The mean was {statistics.mean(totals):.2f} findings per article (SD
{statistics.stdev(totals):.2f}); the median was {statistics.median(totals):.1f},
IQR 3–8, range 1–10. The 2024 packages contributed 48 findings across eight articles
(mean 6.00; 10 Major), while the 2025 packages contributed 63 across 12 articles
(mean 5.25; 12 Major). This is descriptive only: the packages are not a random sample,
and year is confounded with package complexity and audit maturity.

![Major and Minor findings by article.](figures/article_findings.pdf){{ width=92% }}

{article_table}

## Formal error categories

{category_table}

![Formal audit category and severity.](figures/category_severity.pdf){{ width=92% }}

Severity structure matters more than frequency alone. Cross-document inconsistency
had 8 Major findings among 17, and participant-flow inconsistency had 2 among 5.
Presentation findings were far more numerous but only 6/49 were Major; arithmetic
inconsistency had only 1 Major among 16. High-frequency low-level defects therefore
clustered in presentation, whereas substantive conflict between the main article,
supplements, figures, or analysis populations was more likely to become Major.

![Error-category profile by article.](figures/category_heatmap.pdf){{ width=96% }}

# Common failure points

{artifact_table}

![Artifacts involved in each finding's evidence chain; labels are nonexclusive.](figures/artifact_involvement.pdf){{ width=92% }}

## Supplementary tables and Table 1

Supplementary tables were involved in 69/111 findings across 18/20 articles. Recurrent
patterns were header denominators that disagreed with cell percentages, mixtures of
ITT/PPS/safety populations, duplicated or shifted blocks, mislabeled effect measures
or models, and footnotes that contradicted the body. Table 1/baseline material was
involved in nine findings across nine articles, including nonconserving sex counts,
a one-person FIO2 discrepancy between Table 1 and Figure 2, a repeated calcium-channel
blocker percentage error, and different ethnicity-denominator conventions.

## Flow diagrams

Flow/CONSORT diagrams were involved in 15 findings across 10 articles, while only five
findings across four articles carried the formal participant-flow category. The
difference reflects presentation, population, and cross-document problems that surfaced
through a flow figure. High-yield checks are node conservation; explicit separation of
randomized, treated, followed, and analyzed populations; postrandomization withdrawal
branches; the unit of randomization; and agreement with prose and Table 2 analysis sets.

## Narrative, figures, footnotes, and cross-references

Narrative/abstract text was involved in 28 findings across 15 articles; other main
figures in 22 and other main tables in 21. Manual review confirmed at least five direct
cross-reference/location errors: `jama.2024.2302`, `jama.2024.6063`,
`jama.2025.19563`, `jama.2025.9110`, and `jama.2025.9663`. Dictionary coding also
flagged footnotes, titles, captions, and legends repeatedly, showing that semantic
labels require checks independent of the numerical cells.

# Statistical significance, confidence intervals, P values, and definitions

## Confidence intervals

Manual review identified seven findings centered on CI error or incompatibility:
`jama.2024.12829`, `jama.2024.4183`, two in `jama.2025.11178`,
`jama.2025.15440`, `jama.2025.250116`, and `jamasurg.2025.4929`.
Patterns included a point estimate outside its CI, reversed limits, different CIs for
the same comparison across abstract and body, and CI/P-value disagreement. The most
concentrated example was `jama.2025.11178`: seven rows had 95% CIs excluding zero
while their P values exceeded .05, plus a separate group of SMDs outside their CIs.

## P values and test methods

At least five findings made the P value or test method a central contradiction:
“Chi-square” rows that reproduced Fisher exact results (`jama.2024.12829`);
an unqualified no-difference narrative despite day-7 P=.02 and a CI excluding zero
(`jama.2024.24764`); grouped CI–P disagreement (`jama.2025.11178`);
two age P-value footnotes (`jama.2025.19563`); and identical binary counts with
different P values (`jama.2025.4390`). These should be separated into calculation
errors, method-label errors, and narrative failure to distinguish global interaction
from time-specific contrasts.

## Text and conceptual definitions

Recurring conceptual defects included an OR labeled “difference,” RR expanded as risk
difference, a univariate estimate described as multivariable, within-stratum treatment
ORs labeled interactions, median(IQR) labeled mean(SD), FiO2 fractions labeled
percentages, and one analysis unit called women, infants, and patients. These defects
may leave cell values unchanged while materially changing interpretation of the
estimand, population, or model.

{mechanism_table}

# The 22 Major findings

{md_table(["Article", "Finding", "Category", "Major finding synopsis"], major_list,
          ["---", "---", "---", "---"])}

# Article-by-article synthesis (Major and Minor)
"""
    )
    for row in article_rows:
        parts.append(
            f"""
## {row['article']}

**Major {row['Major']}; Minor {row['Minor']}; total {row['Total']}.**

{ARTICLE_SUMMARY_EN[row['article']]}
"""
        )
    parts.append(
        """
# Interpretation, limitations, and recommendations

1. **Audit supplementary tables first.** Apply column-level denominator inference,
   percentage recomputation, estimate/CI/P-value checks, and adjacent-row duplicate
   block detection.
2. **Use an explicit population-stage dictionary.** Randomized, treated, safety, ITT,
   complete-case, PPS, and death-excluded populations should never rely on context alone.
3. **Validate figures back against generation data.** Priorities are flow conservation,
   figure units and headers, eFigure copy/paste, and caption definitions.
4. **Automate cross-reference resolution.** Every eTable/eFigure/Supplement locator in
   the main article should map one-to-one to the actual title and file location.
5. **Make statistical consistency a release gate.** A point estimate must lie within
   its CI; two-sided P values, CIs, and null conclusions should align; identical 2×2
   cells under the same method cannot yield different P values; adjustment and model
   labels must agree with source output.

Limitations include the 10-finding cap, nonrandom package selection, heterogeneous
document volume/OCR/audit scope, use of the source audit taxonomy, and rule-based
multi-label text coding. Retained/accepted findings were submitted for or framed as
human adjudication and should not be read as completed author-confirmed errata.

# Reproducibility and provenance

- `meta_report/audit_findings.csv`: 111-row finding ledger.
- `meta_report/article_counts.csv`: Major/Minor counts by article.
- `meta_report/category_counts.csv`: category-by-severity counts.
- `meta_report/artifact_counts.csv`: multi-label artifact counts.
- `meta_report/mechanism_counts.csv`: multi-label text-theme counts.
- `meta_report/generate_report.py` and `meta_report/analysis.R`: reproducible scripts.

Authoritative source reports:
"""
    )
    parts.extend(f"- `{article}`: `{path}`" for article, path in REPORTS.items())
    return "\n".join(parts)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    rows = parse_reports()
    write_csv(rows)
    (OUT / "jama_audit_report_zh.md").write_text(
        build_report_zh(rows), encoding="utf-8"
    )
    (OUT / "jama_audit_report_en.md").write_text(
        build_report_en(rows), encoding="utf-8"
    )
    print(f"Parsed {len(rows)} accepted findings from {len(REPORTS)} reports.")
    print("Severity:", dict(Counter(r["severity"] for r in rows)))
    print("Category:", dict(Counter(r["category"] for r in rows)))
    for article in REPORTS:
        subset = [r for r in rows if r["article"] == article]
        print(
            article,
            len(subset),
            Counter(r["severity"] for r in subset),
            Counter(r["category"] for r in subset),
        )


if __name__ == "__main__":
    main()
