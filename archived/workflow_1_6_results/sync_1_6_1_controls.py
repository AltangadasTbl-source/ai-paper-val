#!/usr/bin/env python3
"""Bring every paper package's workflow controls to the current workflow 1.6.1 template.

Dry run by default; pass --execute to change files. Before replacing anything, each existing control
is checked against what is known to be installed: workflow 1.6 controls must be byte-identical to
multi_agent_template/workflow1.6/, and earlier workflow 1.6.1 controls must match the hashes recorded
in archive_manifest.csv. A file that differs stops the run. Actions are appended to
sync_manifest.csv with SHA-256.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OLD = REPO / "multi_agent_template/workflow1.6"
NEW = REPO / "multi_agent_template/workflow1.6.1"
YEARS = ("2018", "2019", "2024", "2025")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel_files(root: Path) -> list[Path]:
    return sorted(
        p.relative_to(root) for p in root.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    old_controls = rel_files(OLD)
    new_controls = rel_files(NEW)
    installed: dict[tuple[str, str], str] = {}
    with (HERE / "archive_manifest.csv").open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["action"] == "installed_1_6_1_control":
                installed[(f"{row['year']}/{row['paper']}", row["package_path"])] = row["sha256"]
    sync_manifest = HERE / "sync_manifest.csv"
    if sync_manifest.exists():
        with sync_manifest.open(encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                if row["action"] in {"installed_1_6_1_control", "updated_1_6_1_control", "unchanged_1_6_1_control"}:
                    installed[(row["package"], row["path"])] = row["sha256"]
                elif row["action"].startswith("removed"):
                    installed.pop((row["package"], row["path"]), None)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    rows: list[dict[str, str]] = []
    packages = sorted(p for year in YEARS for p in (REPO / year).iterdir() if p.is_dir())
    for pkg in packages:
        key = pkg.relative_to(REPO).as_posix()
        removals: list[tuple[Path, str]] = []
        for rel in old_controls:
            src = pkg / rel
            if (key, rel.as_posix()) in installed:
                continue
            if src.is_file():
                if sha256(src) != sha256(OLD / rel):
                    raise SystemExit(f"{key}/{rel} differs from the workflow 1.6 template; not touching it.")
                removals.append((rel, "removed_1_6_control_identical_to_template"))
        for (pkg_key, rel_text), digest in installed.items():
            if pkg_key != key:
                continue
            src = pkg / rel_text
            if not src.is_file():
                continue
            if sha256(src) != digest:
                raise SystemExit(f"{key}/{rel_text} changed since installation; not touching it.")
            if Path(rel_text) not in new_controls:
                removals.append((Path(rel_text), "removed_obsolete_1_6_1_control"))
        removed = {rel for rel, _ in removals}
        stray = [
            rel for rel in new_controls
            if (pkg / rel).exists() and rel not in removed and (key, rel.as_posix()) not in installed
        ]
        if stray:
            raise SystemExit(f"{key} already has unrecorded files at 1.6.1 control paths: {stray}")
        for rel, action in removals:
            rows.append(dict(utc=stamp, package=key, action=action, path=rel.as_posix(), sha256=sha256(pkg / rel)))
            if args.execute:
                (pkg / rel).unlink()
        if args.execute:
            for rel, _ in removals:
                directory = (pkg / rel).parent
                while directory != pkg and directory.is_dir() and not any(directory.iterdir()):
                    directory.rmdir()
                    directory = directory.parent
        for rel in new_controls:
            dst = pkg / rel
            action = "updated_1_6_1_control" if dst.exists() and rel not in removed else "installed_1_6_1_control"
            if action == "updated_1_6_1_control" and sha256(dst) == sha256(NEW / rel):
                action = "unchanged_1_6_1_control"
            rows.append(dict(utc=stamp, package=key, action=action, path=rel.as_posix(), sha256=sha256(NEW / rel)))
            if args.execute and action != "unchanged_1_6_1_control":
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(NEW / rel, dst)
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["action"]] = counts.get(row["action"], 0) + 1
    print("EXECUTED" if args.execute else "DRY RUN", len(packages), "packages", counts)
    if args.execute:
        manifest = HERE / "sync_manifest.csv"
        new_file = not manifest.exists()
        with manifest.open("a", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            if new_file:
                writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
