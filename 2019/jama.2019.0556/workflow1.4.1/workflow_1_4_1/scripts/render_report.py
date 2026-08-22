#!/usr/bin/env python3
"""Render a workflow-1.4 quality-control report as standalone locally linked HTML5."""

from __future__ import annotations

import argparse
import html as html_lib
import re
import shutil
import subprocess
from pathlib import Path


LINK = re.compile(r"\[([^\]]+)\]\((<?[^)]+>?)\)")
TABLE_RULE = re.compile(r"^:?-{3,}:?$")


def inline_markdown(value: str) -> str:
    pieces: list[str] = []
    cursor = 0

    def simple(segment: str) -> str:
        escaped = html_lib.escape(segment)
        escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
        escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
        return escaped

    for match in LINK.finditer(value):
        pieces.append(simple(value[cursor : match.start()]))
        label = simple(match.group(1))
        href = match.group(2).strip()
        if href.startswith("<") and href.endswith(">"):
            href = href[1:-1]
        attributes = ""
        if re.search(r"\.pdf#page=\d+$", href, flags=re.IGNORECASE):
            attributes = ' target="_blank" rel="noopener"'
        pieces.append(f'<a href="{html_lib.escape(href, quote=True)}"{attributes}>{label}</a>')
        cursor = match.end()
    pieces.append(simple(value[cursor:]))
    return "".join(pieces)


def heading_id(title: str, used: set[str]) -> str:
    candidate = re.match(r"((?:C\d{2,}|R\d{3,}))\b", title)
    base = candidate.group(1) if candidate else re.sub(r"[^a-z0-9]+", "-", title.casefold()).strip("-")
    base = base or "section"
    value = base
    counter = 2
    while value in used:
        value = f"{base}-{counter}"
        counter += 1
    used.add(value)
    return value


def fallback_render(
    source: Path, destination: Path, title: str, css_path: Path, profile: str
) -> None:
    lines = source.read_text(encoding="utf-8").splitlines()
    rendered: list[str] = []
    toc: list[tuple[int, str, str]] = []
    used_ids: set[str] = set()
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("```"):
            language = line[3:].strip()
            code: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                code.append(lines[index])
                index += 1
            rendered.append(
                f'<pre><code class="language-{html_lib.escape(language)}">'
                + html_lib.escape("\n".join(code))
                + "</code></pre>"
            )
        elif match := re.match(r"^(#{1,6})\s+(.+)$", line):
            level = len(match.group(1))
            heading = match.group(2).strip()
            identifier = heading_id(heading, used_ids)
            candidate_class = (
                ' class="candidate-card"'
                if level == 2 and re.match(r"^C\d{3,}\s+[—-]", heading)
                else ""
            )
            rendered.append(
                f'<h{level} id="{identifier}"{candidate_class}>{inline_markdown(heading)}</h{level}>'
            )
            if level <= 3:
                toc.append((level, identifier, heading))
        elif (
            "|" in line
            and index + 1 < len(lines)
            and "|" in lines[index + 1]
            and all(
                TABLE_RULE.fullmatch(cell.strip())
                for cell in lines[index + 1].strip().strip("|").split("|")
            )
        ):
            headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
            index += 2
            rows: list[list[str]] = []
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                rows.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")])
                index += 1
            index -= 1
            rendered.append("<table><thead><tr>" + "".join(f"<th>{inline_markdown(cell)}</th>" for cell in headers) + "</tr></thead><tbody>")
            for row in rows:
                padded = row + [""] * max(0, len(headers) - len(row))
                rendered.append("<tr>" + "".join(f"<td>{inline_markdown(cell)}</td>" for cell in padded[: len(headers)]) + "</tr>")
            rendered.append("</tbody></table>")
        elif re.match(r"^\s*[-*]\s+", line):
            items: list[str] = []
            while index < len(lines) and (match := re.match(r"^\s*[-*]\s+(.+)$", lines[index])):
                items.append(match.group(1))
                index += 1
            index -= 1
            rendered.append("<ul>" + "".join(f"<li>{inline_markdown(item)}</li>" for item in items) + "</ul>")
        elif re.match(r"^\s*\d+\.\s+", line):
            items = []
            while index < len(lines) and (match := re.match(r"^\s*\d+\.\s+(.+)$", lines[index])):
                items.append(match.group(1))
                index += 1
            index -= 1
            rendered.append("<ol>" + "".join(f"<li>{inline_markdown(item)}</li>" for item in items) + "</ol>")
        elif line.startswith(">"):
            rendered.append(f"<blockquote>{inline_markdown(line.lstrip('> ').strip())}</blockquote>")
        elif line.strip():
            rendered.append(f"<p>{inline_markdown(line.strip())}</p>")
        index += 1

    toc_html = '<nav id="TOC"><ul>' + "".join(
        f'<li class="toc-level-{level}"><a href="#{identifier}">{inline_markdown(text)}</a></li>'
        for level, identifier, text in toc
    ) + "</ul></nav>"
    notice = (
        '<p class="pending-human-adjudication">Pending Human Adjudication: '
        f"workflow {html_lib.escape(profile)} is a quantitative quality-control review. It reports "
        "every candidate found under the completed scope and does not assign AI validity, severity, "
        "acceptance, rejection, or correction decisions.</p>"
    )
    document = (
        "<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        f"<title>{html_lib.escape(title)}</title><style>\n{css_path.read_text(encoding='utf-8')}\n</style>"
        f"</head><body>{notice}{toc_html}{''.join(rendered)}</body></html>\n"
    )
    destination.write_text(document, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path)
    parser.add_argument("html", type=Path)
    parser.add_argument("--profile", required=True, choices=("1.4.1", "1.4.2"))
    parser.add_argument("--title")
    parser.add_argument("--css", type=Path)
    args = parser.parse_args()

    source = args.markdown.expanduser().resolve()
    destination = args.html.expanduser().resolve()
    title = args.title or (
        f"Quantitative Quality-Control Review {args.profile} — Pending Human Adjudication"
    )
    if not source.is_file():
        parser.error(f"Markdown input does not exist: {source}")
    pandoc = shutil.which("pandoc")
    default_css = Path(__file__).resolve().parent.parent / "assets" / "report.css"
    css_path = (args.css or default_css).expanduser().resolve()
    if not css_path.is_file():
        raise SystemExit(f"Report stylesheet does not exist: {css_path}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    if not pandoc:
        fallback_render(source, destination, title, css_path, args.profile)
        print(f"Rendered {destination} with the dependency-free fallback (Pandoc unavailable)")
        return
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    subprocess.run(
        [
            pandoc,
            "--from=gfm",
            "--to=html5",
            "--standalone",
            "--toc",
            "--toc-depth=3",
            "--metadata",
            f"title={title}",
            "--output",
            str(temporary),
            str(source),
        ],
        cwd=source.parent,
        check=True,
    )

    rendered = temporary.read_text(encoding="utf-8")
    style = f"<style>\n{css_path.read_text(encoding='utf-8')}\n</style>\n"
    rendered = rendered.replace("</head>", style + "</head>", 1)
    rendered = re.sub(
        r'<a href="([^"]+\.pdf#page=\d+)"',
        r'<a href="\1" target="_blank" rel="noopener"',
        rendered,
        flags=re.IGNORECASE,
    )
    rendered = re.sub(
        r'<h2([^>]*\bid="c\d{3,}[^"]*"[^>]*)>',
        r'<h2\1 class="candidate-card">',
        rendered,
        flags=re.IGNORECASE,
    )
    notice = (
        '<p class="pending-human-adjudication">Pending Human Adjudication: '
        f"workflow {html_lib.escape(args.profile)} is a quantitative quality-control review. It "
        "reports every candidate found under the completed scope and does not assign AI validity, "
        "severity, acceptance, rejection, or correction decisions.</p>"
    )
    body_match = re.search(r"<body[^>]*>", rendered, flags=re.IGNORECASE)
    if not body_match:
        temporary.unlink(missing_ok=True)
        raise SystemExit("Pandoc output did not contain an HTML body element.")
    rendered = rendered[: body_match.end()] + "\n" + notice + rendered[body_match.end() :]
    if "<html" not in rendered.casefold() or '<nav id="TOC"' not in rendered:
        temporary.unlink(missing_ok=True)
        raise SystemExit("Rendered document is not standalone HTML5 with a table of contents.")
    temporary.write_text(rendered, encoding="utf-8")
    temporary.replace(destination)
    print(f"Rendered {destination}")


if __name__ == "__main__":
    main()
