from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import os
import xml.etree.ElementTree as ET


DOCX_PATH = Path("/home/bulunte/ai-paper-val/jama.2024.2302/AI_Paper_Validation_Detailed_Findings_C1_C3_C5.docx")
TEMP_PATH = DOCX_PATH.with_suffix(".formatted.docx")

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
ET.register_namespace("w", W_NS)


def w(tag):
    return f"{{{W_NS}}}{tag}"


def child(parent, tag, first=False):
    node = parent.find(w(tag))
    if node is None:
        node = ET.Element(w(tag))
        if first:
            parent.insert(0, node)
        else:
            parent.append(node)
    return node


def set_attr(node, name, value):
    node.set(w(name), str(value))


def paragraph_text(paragraph):
    return "".join(t.text or "" for t in paragraph.iter(w("t"))).strip()


def set_paragraph_property(paragraph, tag, value=None):
    p_pr = child(paragraph, "pPr", first=True)
    node = child(p_pr, tag)
    if value is not None:
        set_attr(node, "val", value)
    return node


def set_run_format(paragraph, *, color=None, size=None, bold=None, font=None):
    for run in paragraph.findall(w("r")):
        r_pr = child(run, "rPr", first=True)
        if color:
            set_attr(child(r_pr, "color"), "val", color)
        if size:
            set_attr(child(r_pr, "sz"), "val", size)
            set_attr(child(r_pr, "szCs"), "val", size)
        if bold:
            set_attr(child(r_pr, "b"), "val", "1")
            set_attr(child(r_pr, "bCs"), "val", "1")
        if font:
            fonts = child(r_pr, "rFonts")
            for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
                set_attr(fonts, attr, font)


def style_rpr(style, *, color=None, size=None, bold=None, font=None):
    r_pr = child(style, "rPr")
    if color:
        set_attr(child(r_pr, "color"), "val", color)
    if size:
        set_attr(child(r_pr, "sz"), "val", size)
        set_attr(child(r_pr, "szCs"), "val", size)
    if bold:
        set_attr(child(r_pr, "b"), "val", "1")
        set_attr(child(r_pr, "bCs"), "val", "1")
    if font:
        fonts = child(r_pr, "rFonts")
        for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
            set_attr(fonts, attr, font)


def style_ppr(style, *, before=None, after=None, line=None, keep_next=False):
    p_pr = child(style, "pPr")
    spacing = child(p_pr, "spacing")
    if before is not None:
        set_attr(spacing, "before", before)
    if after is not None:
        set_attr(spacing, "after", after)
    if line is not None:
        set_attr(spacing, "line", line)
        set_attr(spacing, "lineRule", "auto")
    if keep_next:
        set_attr(child(p_pr, "keepNext"), "val", "1")


with ZipFile(DOCX_PATH, "r") as source:
    document_xml = source.read("word/document.xml")
    styles_xml = source.read("word/styles.xml")
    entries = {name: source.read(name) for name in source.namelist()}

document = ET.fromstring(document_xml)
styles = ET.fromstring(styles_xml)

# Remove the redundant metadata-title paragraph imported ahead of the designed
# cover title.
body = document.find(w("body"))
if body is not None:
    for element in list(body):
        if element.tag == w("p") and paragraph_text(element) == "AI Paper Validation – Detailed Findings C1, C3, and C5":
            body.remove(element)
            break

# Page setup: A4 with balanced margins.
for section in document.iter(w("sectPr")):
    page_size = child(section, "pgSz")
    set_attr(page_size, "w", "11906")
    set_attr(page_size, "h", "16838")
    margins = child(section, "pgMar")
    for name, value in {
        "top": "1134",
        "right": "1191",
        "bottom": "1134",
        "left": "1191",
        "header": "567",
        "footer": "567",
        "gutter": "0",
    }.items():
        set_attr(margins, name, value)

# Refine Word paragraph styles.
for style in styles.findall(w("style")):
    style_id = style.get(w("styleId"), "")
    if style_id == "Normal":
        style_rpr(style, size="21", font="Aptos")
        style_ppr(style, after="120", line="276")
    elif style_id == "Heading1":
        style_rpr(style, color="17365D", size="36", bold=True, font="Aptos Display")
        style_ppr(style, before="220", after="140", keep_next=True)
    elif style_id == "Heading2":
        style_rpr(style, color="1F4E79", size="27", bold=True, font="Aptos Display")
        style_ppr(style, before="180", after="90", keep_next=True)
    elif style_id == "Heading3":
        style_rpr(style, color="365F91", size="23", bold=True, font="Aptos")
        style_ppr(style, before="140", after="70", keep_next=True)
    elif style_id in {"BlockText", "Quote"}:
        style_rpr(style, color="243746", size="20", font="Aptos")
        style_ppr(style, before="80", after="100", line="276")

page_break_targets = {
    "Executive Summary",
    "Finding C1",
    "Finding C3",
    "Finding C5",
    "Source Document Index",
}

cover_center_targets = {
    "AI Paper Validation",
    "Detailed Explanations of Findings C1, C3, and C5",
    "Effect of Early vs Late Inguinal Hernia Repair on Serious Adverse Event Rates in Preterm Infants: A Randomized Clinical Trial",
    "JAMA. 2024;331(12):1035–1044. doi:10.1001/jama.2024.2302",
    "Article package: jama.2024.2302",
    "Prepared for: Human Adjudication",
}

for paragraph in document.iter(w("p")):
    text = paragraph_text(paragraph)
    if not text:
        continue

    if text in page_break_targets:
        set_paragraph_property(paragraph, "pageBreakBefore", "1")
        set_paragraph_property(paragraph, "keepNext", "1")

    if text in cover_center_targets:
        set_paragraph_property(paragraph, "jc", "center")

    if text == "AI Paper Validation":
        set_paragraph_property(paragraph, "spacing")
        set_run_format(paragraph, color="17365D", size="46", bold=True, font="Aptos Display")
    elif text == "Detailed Explanations of Findings C1, C3, and C5":
        set_run_format(paragraph, color="355B7D", size="30", font="Aptos Display")
    elif text.startswith("Effect of Early vs Late Inguinal Hernia Repair"):
        set_run_format(paragraph, color="202A35", size="24", bold=True, font="Aptos")
    elif text.startswith("Scope note."):
        p_pr = child(paragraph, "pPr", first=True)
        set_attr(child(p_pr, "shd"), "fill", "EAF2F8")
        set_paragraph_property(paragraph, "spacing")
    elif text in {"Finding C1", "Finding C3", "Finding C5"}:
        p_pr = child(paragraph, "pPr", first=True)
        set_attr(child(p_pr, "shd"), "fill", "17365D")
        set_paragraph_property(paragraph, "keepNext", "1")
        set_run_format(paragraph, color="FFFFFF", size="21", bold=True, font="Aptos")
    elif text.startswith("Presentation inconsistency") or text.startswith("Participant flow inconsistency"):
        p_pr = child(paragraph, "pPr", first=True)
        set_attr(child(p_pr, "shd"), "fill", "EAF2F8")

# Apply clear table borders, header shading, and repeating header rows.
table_widths = [
    [1200, 1800, 1200, 5200],                # Executive Summary
    [2200, 1100, 1100, 900, 4100],          # C1 population reconciliation
    [1000, 1400, 1800, 1600, 1400, 2200],   # C3 arm-level reconciliation
    [5600, 1900, 1900],                     # C5 content mapping
    [4300, 3300, 1800],                     # Source document index
]

for table_index, table in enumerate(document.iter(w("tbl"))):
    tbl_pr = child(table, "tblPr", first=True)
    width = child(tbl_pr, "tblW")
    set_attr(width, "type", "pct")
    set_attr(width, "w", "5000")
    set_attr(child(tbl_pr, "tblLayout"), "type", "fixed")

    borders = child(tbl_pr, "tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        border = child(borders, edge)
        set_attr(border, "val", "single")
        set_attr(border, "sz", "6")
        set_attr(border, "color", "8FA3B5")

    configured_widths = table_widths[table_index] if table_index < len(table_widths) else None
    grid = table.find(w("tblGrid"))
    if configured_widths and grid is not None:
        grid_columns = grid.findall(w("gridCol"))
        for column, column_width in zip(grid_columns, configured_widths):
            set_attr(column, "w", column_width)

    rows = table.findall(w("tr"))
    for row_index, row in enumerate(rows):
        tr_pr = child(row, "trPr", first=True)
        set_attr(child(tr_pr, "cantSplit"), "val", "1")
        cells = row.findall(w("tc"))
        if configured_widths:
            for cell, cell_width in zip(cells, configured_widths):
                tc_pr = child(cell, "tcPr", first=True)
                tc_width = child(tc_pr, "tcW")
                set_attr(tc_width, "type", "dxa")
                set_attr(tc_width, "w", cell_width)
        if row_index == 0:
            set_attr(child(tr_pr, "tblHeader"), "val", "1")
            for cell in cells:
                tc_pr = child(cell, "tcPr", first=True)
                set_attr(child(tc_pr, "shd"), "fill", "1F4E79")
                for paragraph in cell.findall(w("p")):
                    p_pr = paragraph.find(w("pPr"))
                    if p_pr is not None:
                        paragraph_shading = p_pr.find(w("shd"))
                        if paragraph_shading is not None:
                            p_pr.remove(paragraph_shading)
                    set_run_format(paragraph, color="FFFFFF", bold=True, font="Aptos")
        elif row_index % 2 == 0:
            for cell in cells:
                tc_pr = child(cell, "tcPr", first=True)
                set_attr(child(tc_pr, "shd"), "fill", "F4F7F9")
        for cell in cells:
            for paragraph in cell.findall(w("p")):
                p_pr = paragraph.find(w("pPr"))
                if p_pr is not None:
                    paragraph_shading = p_pr.find(w("shd"))
                    if paragraph_shading is not None:
                        p_pr.remove(paragraph_shading)

entries["word/document.xml"] = ET.tostring(document, encoding="utf-8", xml_declaration=True)
entries["word/styles.xml"] = ET.tostring(styles, encoding="utf-8", xml_declaration=True)

with ZipFile(TEMP_PATH, "w", ZIP_DEFLATED) as target:
    for name, data in entries.items():
        target.writestr(name, data)

os.replace(TEMP_PATH, DOCX_PATH)
