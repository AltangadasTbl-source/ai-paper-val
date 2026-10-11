#!/usr/bin/env python3
"""Archive workflow 1.6.1 run results and swap every package's controls to workflow 1.6.2.

Dry run by default; pass --execute to move files. For each of the 45 packages in 2018/, 2019/,
2024/ and 2025/:
- moves .ai_paper_validation/review_1_6_1/ (except its preprocessing/ folder, which holds reusable
  extraction assets and stays in place), final_report_1_6_1.{md,html}, and any
  .ai_paper_validation/review_1_6/ files that the server runs re-created, to
  archived/workflow_1_6_1_results/<year>/<paper>/ with the same package-relative paths;
- removes the workflow 1.6.1 controls after confirming each is byte-identical to
  multi_agent_template/workflow1.6.1/ (a differing control is archived instead);
- copies the workflow 1.6.2 controls from multi_agent_template/workflow1.6.2/.
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
OLD = REPO / "multi_agent_template/workflow1.6.1"
NEW = REPO / "multi_agent_template/workflow1.6.2"
YEARS = ("2018", "2019", "2024", "2025")
RESULT_ROOTS = (
    ".ai_paper_validation/review_1_6_1",
    ".ai_paper_validation/final_report_1_6_1.md",
    ".ai_paper_validation/final_report_1_6_1.html",
    ".ai_paper_validation/review_1_6",
)
KEPT_PREFIX = ".ai_paper_validation/review_1_6_1/preprocessing/"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def files_under(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    if not root.is_dir():
        return []
    return sorted(p for p in root.rglob("*")
                  if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc")


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
    packages = sorted(p for year in YEARS for p in (REPO / year).iterdir() if p.is_dir())
    rows: list[dict[str, str]] = []
    kept = 0
    for pkg in packages:
        year, paper = pkg.parent.name, pkg.name
        if not (pkg / "workflow_1_6_1").is_dir():
            raise SystemExit(f"package lacks workflow 1.6.1 controls: {pkg}")
        for root in RESULT_ROOTS:
            for src in files_under(pkg / root):
                rel = src.relative_to(pkg)
                if rel.as_posix().startswith(KEPT_PREFIX):
                    kept += 1
                    continue
                dst = ARCHIVE / year / paper / rel
                digest = sha256(src)
                rows.append(dict(year=year, paper=paper, action="archived_result", package_path=rel.as_posix(),
                                 archive_path=dst.relative_to(REPO).as_posix(), bytes=str(src.stat().st_size), sha256=digest))
                if args.execute:
                    if dst.exists():
                        raise SystemExit(f"archive path exists: {dst}")
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(src), dst)
                    if sha256(dst) != digest:
                        raise SystemExit(f"hash mismatch after move: {dst}")
        for rel in old_controls:
            src = pkg / rel
            if not src.is_file():
                raise SystemExit(f"missing 1.6.1 control: {src}")
            digest = sha256(src)
            identical = digest == sha256(OLD / rel)
            dst = ARCHIVE / year / paper / rel
            rows.append(dict(year=year, paper=paper,
                             action="removed_control_identical_to_template" if identical else "archived_control",
                             package_path=rel.as_posix(),
                             archive_path=f"multi_agent_template/workflow1.6.1/{rel.as_posix()}" if identical else dst.relative_to(REPO).as_posix(),
                             bytes=str(src.stat().st_size), sha256=digest))
            if args.execute:
                if identical:
                    src.unlink()
                else:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(src), dst)
        if args.execute:
            dirs = {(pkg / r).parent for r in old_controls}
            for root in RESULT_ROOTS:
                if (pkg / root).is_dir():
                    dirs |= {p for p in (pkg / root).rglob("*") if p.is_dir()} | {pkg / root}
            for directory in sorted(dirs, key=lambda p: len(p.parts), reverse=True):
                while directory != pkg and directory.is_dir() and not any(directory.iterdir()):
                    directory.rmdir()
                    directory = directory.parent
        for rel in new_controls:
            dst = pkg / rel
            if dst.exists() and (args.execute or rel not in old_set):
                raise SystemExit(f"refusing to overwrite existing control: {dst}")
            rows.append(dict(year=year, paper=paper, action="installed_1_6_2_control", package_path=rel.as_posix(),
                             archive_path="", bytes=str((NEW / rel).stat().st_size), sha256=sha256(NEW / rel)))
            if args.execute:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(NEW / rel, dst)
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["action"]] = counts.get(row["action"], 0) + 1
    print(("EXECUTED" if args.execute else "DRY RUN"), f"packages={len(packages)}", counts,
          f"kept_preprocessing_files={kept}")
    if args.execute:
        with manifest.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
