#!/home/juliz/venvs/stt/bin/python
"""Create new JAMA trial packages from the authenticated Chrome search catalog.

The JAMA search and article HTML are read through the locally running Chrome
session (see ``jama_browser.ps1``).  Only qualifying packages whose
``jama.<doi-suffix>`` directory does not already exist are created.  The main
article is deliberately *not* downloaded; each new package receives a text
placeholder for the user to obtain it through their library access.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PACKAGE = ROOT / "2024" / "jama.2024.2302"
TEMPLATE_FILES = ("AGENTS.md", "README.md", "prmopt.txt")


def catalog(start_year: int, end_year: int, port: int) -> dict[str, object]:
    date_range = f"{start_year}-01-01 TO {end_year}-12-31"
    command = [
        "powershell.exe",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        "scripts/jama_browser.ps1",
        "eval-file",
        "scripts/jama_collect.js",
        "-Port",
        str(port),
        "-DateRange",
        date_range,
    ]
    result = subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)
    response = json.loads(result.stdout)
    payload = response["result"]["result"]["value"]
    return json.loads(payload) if isinstance(payload, str) else payload


def doi_suffix(doi: str) -> str:
    prefix = "10.1001/jama."
    if not doi.startswith(prefix):
        raise ValueError(f"Unexpected DOI format: {doi}")
    return doi.removeprefix(prefix)


def filename_from_url(url: str) -> str:
    filename = unquote(Path(urlparse(url).path).name)
    if not filename or filename in {".", ".."} or "/" in filename or "\\" in filename:
        raise ValueError(f"Unsafe supplement filename from URL: {url}")
    return filename


def download(url: str, destination: Path) -> None:
    temporary = destination.with_suffix(destination.suffix + ".part")
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(request, timeout=120) as response, temporary.open("wb") as output:
            shutil.copyfileobj(response, output)
        temporary.replace(destination)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def placeholder(article: dict[str, object]) -> str:
    labels = "\n".join(f"- {item['label']}" for item in article["supplements"])
    return (
        "Main article download required\n"
        "============================\n\n"
        "The main article was intentionally not downloaded by the automation. "
        "Please obtain the PDF through your library access and save it in this folder.\n\n"
        f"Title: {article['title']}\n"
        f"DOI: {article['doi']}\n"
        f"JAMA article page: {article['url']}\n\n"
        "Public supplementary files downloaded by the automation:\n"
        f"{labels}\n"
    )


def create_package(
    article: dict[str, object],
    output_root: Path = ROOT,
    template_package: Path = TEMPLATE_PACKAGE,
) -> dict[str, object]:
    folder = output_root / f"jama.{doi_suffix(str(article['doi']))}"
    created = False
    if folder.exists():
        # A package created by this script but interrupted during downloads can be
        # resumed. Existing user packages do not contain this exact placeholder.
        if not (folder / "MAIN_PAPER_TO_DOWNLOAD.txt").is_file():
            return {"folder": str(folder), "status": "already_exists", "files": []}
    else:
        folder.mkdir(parents=True)
        created = True
        for name in TEMPLATE_FILES:
            shutil.copy2(template_package / name, folder / name)
        (folder / "MAIN_PAPER_TO_DOWNLOAD.txt").write_text(placeholder(article), encoding="utf-8")

    try:
        downloaded = []
        for supplement in article["supplements"]:
            destination = folder / filename_from_url(supplement["href"])
            if destination.exists():
                continue
            download(str(supplement["href"]), destination)
            downloaded.append(destination.name)
    except Exception:
        # A new folder is intentionally retained to allow a subsequent safe resume.
        raise
    return {"folder": str(folder), "status": "created" if created else "resumed", "files": downloaded}


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--start-year", type=int, required=True)
    parser.add_argument("--end-year", type=int, required=True)
    parser.add_argument("--port", type=int, default=9223)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("."),
        help="Destination directory relative to the repository root (default: repository root).",
    )
    parser.add_argument(
        "--template-package",
        type=Path,
        default=TEMPLATE_PACKAGE.relative_to(ROOT),
        help="Existing article package whose AGENTS.md, README.md, and prmopt.txt are copied.",
    )
    parser.add_argument(
        "--existing-placeholders-only",
        action="store_true",
        help=(
            "Restore supplements only for packages that already contain "
            "MAIN_PAPER_TO_DOWNLOAD.txt; do not create additional packages."
        ),
    )
    args = parser.parse_args()
    if args.start_year > args.end_year:
        parser.error("--start-year must not exceed --end-year")
    output_root = (ROOT / args.output_dir).resolve()
    template_package = (ROOT / args.template_package).resolve()
    if output_root != ROOT and ROOT not in output_root.parents:
        raise RuntimeError(f"Output directory must be inside the repository: {output_root}")
    if not template_package.is_dir():
        raise RuntimeError(f"Template package not found: {template_package}")
    for name in TEMPLATE_FILES:
        if not (template_package / name).is_file():
            raise RuntimeError(f"Template file not found: {template_package / name}")
    output_root.mkdir(parents=True, exist_ok=True)
    data = catalog(args.start_year, args.end_year, args.port)
    if "eligible" not in data:
        raise RuntimeError(f"Unexpected JAMA catalog response: {json.dumps(data)[:1000]}")
    outcome = []
    failures = []
    skipped_without_placeholder = 0
    for article in data["eligible"]:
        if args.existing_placeholders_only:
            folder = output_root / f"jama.{doi_suffix(str(article['doi']))}"
            if not (folder / "MAIN_PAPER_TO_DOWNLOAD.txt").is_file():
                skipped_without_placeholder += 1
                continue
        try:
            outcome.append(create_package(article, output_root, template_package))
        except Exception as error:
            failures.append({"doi": article["doi"], "title": article["title"], "error": str(error)})
    changed = [item for item in outcome if item["status"] in {"created", "resumed"}]
    print(
        json.dumps(
            {
                "changed": changed,
                "skipped_existing": len(outcome) - len(changed),
                "skipped_without_placeholder": skipped_without_placeholder,
                "catalog_errors": data.get("errors", []),
                "failures": failures,
            },
            indent=2,
        )
    )
    if failures:
        raise RuntimeError(f"Could not retrieve supplements for {len(failures)} package(s)")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"jama_fetch_new.py: {error}", file=sys.stderr)
        raise SystemExit(1)
