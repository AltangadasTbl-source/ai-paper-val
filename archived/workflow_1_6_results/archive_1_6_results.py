#!/usr/bin/env python3
"""Archive workflow 1.6 run results and swap the package controls to workflow 1.6.1.

Dry run by default; pass --execute to move files. For each listed package:
- moves .ai_paper_validation/review_1_6/ and final_report_1_6.{md,html} to
  archived/workflow_1_6_results/<year>/<paper>/ with the same package-relative paths;
- removes the workflow 1.6 controls after confirming each is byte-identical to
  multi_agent_template/workflow1.6/ (a differing control is archived instead);
- copies the workflow 1.6.1 controls from multi_agent_template/workflow1.6.1/.
Every action is recorded with SHA-256 in archive_manifest.csv.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ARCHIVE = Path(__file__).resolve().parent
OLD = REPO / "multi_agent_template/workflow1.6"
NEW = REPO / "multi_agent_template/workflow1.6.1"
PACKAGES = [
    *(f"2019/{name}" for name in (
        "jama.2019.0556", "jama.2019.10517", "jama.2019.12618", "jama.2019.14231",
        "jama.2019.14630", "jama.2019.14901", "jama.2019.17380", "jama.2019.2210",
        "jama.2019.4755", "jama.2019.7505",
    )),
    *(f"2018/{name}" for name in (
        "jama.2017.21906", "jama.2018.0156", "jama.2018.0948", "jama.2018.6496", "jama.2018.8802",
    )),
]
RESULT_PATHS = (
    ".ai_paper_validation/review_1_6",
    ".ai_paper_validation/final_report_1_6.md",
    ".ai_paper_validation/final_report_1_6.html",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def files_under(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*") if p.is_file()) if root.is_dir() else ([root] if root.is_file() else [])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    manifest = ARCHIVE / "archive_manifest.csv"
    if args.execute and manifest.exists():
        raise SystemExit("archive_manifest.csv exists; refusing to run again.")
    old_controls = [p.relative_to(OLD) for p in files_under(OLD)]
    new_controls = [p.relative_to(NEW) for p in files_under(NEW)]
    old_set = set(old_controls)
    rows: list[dict[str, str]] = []
    for package in PACKAGES:
        pkg = REPO / package
        year, paper = package.split("/")
        for result in RESULT_PATHS:
            for src in files_under(pkg / result):
                rel = src.relative_to(pkg)
                dst = ARCHIVE / year / paper / rel
                digest = sha256(src)
                rows.append(dict(year=year, paper=paper, action="archived_result", package_path=rel.as_posix(),
                                 archive_path=dst.relative_to(REPO).as_posix(), bytes=str(src.stat().st_size), sha256=digest))
                if args.execute:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(src), dst)
                    if sha256(dst) != digest:
                        raise SystemExit(f"hash mismatch after move: {dst}")
        for rel in old_controls:
            src = pkg / rel
            if not src.is_file():
                continue
            digest = sha256(src)
            identical = digest == sha256(OLD / rel)
            dst = ARCHIVE / year / paper / rel
            rows.append(dict(year=year, paper=paper,
                             action="removed_control_identical_to_template" if identical else "archived_control",
                             package_path=rel.as_posix(),
                             archive_path=f"multi_agent_template/workflow1.6/{rel.as_posix()}" if identical else dst.relative_to(REPO).as_posix(),
                             bytes=str(src.stat().st_size), sha256=digest))
            if args.execute:
                if identical:
                    src.unlink()
                else:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(src), dst)
        if args.execute:
            for directory in sorted({(pkg / r).parent for r in old_controls} | {pkg / ".ai_paper_validation/review_1_6"},
                                    key=lambda p: len(p.parts), reverse=True):
                while directory != pkg and directory.is_dir() and not any(directory.iterdir()):
                    directory.rmdir()
                    directory = directory.parent
        for rel in new_controls:
            dst = pkg / rel
            if dst.exists() and (args.execute or rel not in old_set):
                raise SystemExit(f"refusing to overwrite existing control: {dst}")
            rows.append(dict(year=year, paper=paper, action="installed_1_6_1_control", package_path=rel.as_posix(),
                             archive_path="", bytes=str((NEW / rel).stat().st_size), sha256=sha256(NEW / rel)))
            if args.execute:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(NEW / rel, dst)
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["action"]] = counts.get(row["action"], 0) + 1
    print(("EXECUTED" if args.execute else "DRY RUN"), counts)
    if args.execute:
        with manifest.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
