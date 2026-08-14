#!/usr/bin/env python3
"""Render the audit Markdown as standalone, locally linked HTML5."""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import subprocess
import tomllib
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path)
    parser.add_argument("html", type=Path)
    parser.add_argument("--title", default="AI Paper Validation Report — Pending Human Adjudication")
    parser.add_argument("--css", type=Path)
    parser.add_argument("--config", type=Path)
    args = parser.parse_args()

    source = args.markdown.resolve()
    destination = args.html.resolve()
    if not source.is_file():
        parser.error(f"Markdown input does not exist: {source}")
    configured_pandoc = os.environ.get("AI_VALIDATION_PANDOC")
    if not configured_pandoc and args.config:
        with args.config.expanduser().resolve().open("rb") as handle:
            configured_pandoc = str(tomllib.load(handle).get("tools", {}).get("pandoc", "pandoc"))
    configured_pandoc = configured_pandoc or "pandoc"
    pandoc = shutil.which(configured_pandoc) or (
        configured_pandoc if Path(configured_pandoc).is_file() else None
    )
    if not pandoc:
        raise SystemExit("Pandoc is required to render the standalone HTML report.")

    default_css = Path(__file__).resolve().parent.parent / "assets" / "report.css"
    css_path = (args.css or default_css).resolve()
    if not css_path.is_file():
        raise SystemExit(f"Report stylesheet does not exist: {css_path}")

    destination.parent.mkdir(parents=True, exist_ok=True)
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
            f"title={args.title}",
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
    notice = (
        '<p class="pending-human-adjudication">Pending Human Adjudication: '
        "this report presents source-linked candidate inconsistencies and does not assign "
        "AI validity, severity, acceptance, or rejection decisions.</p>"
    )
    body_match = re.search(r"<body[^>]*>", rendered, flags=re.IGNORECASE)
    if not body_match:
        temporary.unlink(missing_ok=True)
        raise SystemExit("Pandoc output did not contain an HTML body element.")
    rendered = rendered[: body_match.end()] + "\n" + notice + rendered[body_match.end() :]
    rendered = rendered.replace("<meta charset=\"utf-8\" />", "<meta charset=\"utf-8\">", 1)
    if "<html" not in rendered.lower() or "<nav id=\"TOC\"" not in rendered:
        temporary.unlink(missing_ok=True)
        raise SystemExit("Rendered document is not standalone HTML5 with a table of contents.")

    temporary.write_text(rendered, encoding="utf-8")
    temporary.replace(destination)
    print(f"Rendered {html.escape(str(destination))}")


if __name__ == "__main__":
    main()
