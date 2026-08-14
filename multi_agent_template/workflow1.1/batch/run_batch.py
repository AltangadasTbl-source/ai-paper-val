#!/usr/bin/env python3
"""Launch isolated Codex workers; leave every paper decision to the worker agent."""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import re
import shutil
import subprocess
import tomllib
from pathlib import Path
from typing import Any


SOURCE_SUFFIXES = {".pdf", ".doc", ".docx"}
MANAGEMENT_DIRECTORIES = {"batch", "audit"}


def natural_key(value: str) -> list[object]:
    return [int(part) if part.isdigit() else part.casefold() for part in re.split(r"(\d+)", value)]


def package_has_source(package: Path) -> bool:
    return any(
        path.is_file() and path.suffix.lower() in SOURCE_SUFFIXES for path in package.iterdir()
    )


def discover_packages(root: Path, selected: list[str] | None) -> list[Path]:
    if selected:
        packages = [(root / name).resolve() for name in selected]
        invalid = [
            path
            for path in packages
            if path.parent != root or not path.is_dir() or not package_has_source(path)
        ]
        if invalid:
            raise SystemExit(f"Invalid direct-child paper packages: {invalid}")
    else:
        packages = [
            path
            for path in root.iterdir()
            if path.is_dir()
            and not path.name.startswith(".")
            and path.name not in MANAGEMENT_DIRECTORIES
            and package_has_source(path)
        ]
    packages.sort(key=lambda path: natural_key(path.name))
    if not packages:
        raise SystemExit("No direct-child paper package was found.")
    return packages


def archive_or_create_audit(package: Path, policy: str, run_id: str) -> Path:
    audit = package / "audit"
    if not audit.exists() or not any(audit.iterdir()):
        audit.mkdir(parents=True, exist_ok=True)
        return audit
    if policy == "fail":
        raise RuntimeError(f"{audit} is not empty; use --existing-audit archive to rerun.")
    history = package / ".audit_history"
    history.mkdir(parents=True, exist_ok=True)
    destination = history / run_id
    counter = 1
    while destination.exists():
        destination = history / f"{run_id}-{counter:02d}"
        counter += 1
    audit.replace(destination)
    audit.mkdir(parents=True)
    return audit


def valid_result(path: Path, audit: Path) -> bool:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    if payload.get("run_status") not in {"COMPLETED", "NEEDS_HUMAN_INPUT"}:
        return False
    if payload.get("artifacts", {}).get("final_report_html") != "audit/final_report.html":
        return False
    html_report = audit / "final_report.html"
    validation_path = audit / "audit_validation.json"
    if not html_report.is_file() or html_report.stat().st_size == 0:
        return False
    try:
        validation = json.loads(validation_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return validation.get("status") == "PASS"


def run_package(
    root: Path,
    package: Path,
    prompt: str,
    schema: Path,
    codex: str,
    retries: int,
    existing_audit: str,
    run_id: str,
) -> dict[str, Any]:
    try:
        audit = archive_or_create_audit(package, existing_audit, run_id)
    except Exception as error:
        return {"paper_package": package.name, "status": "FAILED", "error": str(error)}

    attempts = audit / "worker_attempts"
    attempts.mkdir(parents=True, exist_ok=True)
    for attempt in range(1, retries + 2):
        result = attempts / f"attempt-{attempt:02d}.result.json"
        events = attempts / f"attempt-{attempt:02d}.events.jsonl"
        errors = attempts / f"attempt-{attempt:02d}.stderr.log"
        command = [
            codex,
            "exec",
            "--strict-config",
            "--approve-for-me",
            "--ephemeral",
            "--cd",
            str(package),
            "--output-schema",
            str(schema),
            "--output-last-message",
            str(result),
            "--json",
            "-",
        ]
        with events.open("w", encoding="utf-8") as stdout, errors.open(
            "w", encoding="utf-8"
        ) as stderr:
            completed = subprocess.run(
                command,
                input=prompt,
                text=True,
                stdout=stdout,
                stderr=stderr,
                cwd=root,
            )
        if completed.returncode == 0 and valid_result(result, audit):
            shutil.copyfile(result, audit / "result.json")
            return {
                "paper_package": package.name,
                "status": "COMPLETED",
                "attempts": attempt,
                "result": str((audit / "result.json").relative_to(root)),
                "report": str((audit / "final_report.html").relative_to(root)),
            }
    return {
        "paper_package": package.name,
        "status": "FAILED",
        "attempts": retries + 1,
        "error": f"See {attempts.relative_to(root)}",
    }


def main() -> None:
    root_default = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=root_default)
    parser.add_argument("--workers", type=int, choices=range(2, 5))
    parser.add_argument("--retries", type=int, choices=range(0, 4))
    parser.add_argument("--existing-audit", choices=("fail", "archive"))
    parser.add_argument("--packages", nargs="+")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    if not (root / ".git").exists():
        raise SystemExit(f"The collection root must be a Git repository: {root}")
    with (root / "ai-validation.toml").open("rb") as handle:
        settings = tomllib.load(handle)
    launcher = settings["launcher"]
    workers = args.workers if args.workers is not None else int(launcher["workers"])
    retries = args.retries if args.retries is not None else int(launcher["retries"])
    existing_audit = args.existing_audit or str(launcher["existing_audit"])
    if workers not in range(2, 5):
        raise SystemExit("Worker concurrency must be between 2 and 4.")
    if retries not in range(0, 4):
        raise SystemExit("Retries must be between 0 and 3.")
    if existing_audit not in {"fail", "archive"}:
        raise SystemExit("existing_audit must be fail or archive.")
    codex_setting = str(settings["runtime"]["codex"])
    codex = shutil.which(codex_setting) or (
        codex_setting if Path(codex_setting).expanduser().is_file() else None
    )
    if not codex:
        raise SystemExit(f"Codex CLI was not found: {codex_setting}")

    packages = discover_packages(root, args.packages)
    if args.dry_run:
        print(json.dumps({"workers": workers, "packages": [p.name for p in packages]}, indent=2))
        return

    prompt = (root / "batch/prompt.md").read_text(encoding="utf-8")
    schema = root / "batch/result.schema.json"
    run_id = dt.datetime.now().strftime("run-%Y%m%d-%H%M%S")
    results: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(
                run_package,
                root,
                package,
                prompt,
                schema,
                codex,
                retries,
                existing_audit,
                run_id,
            )
            for package in packages
        ]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
            print(f"[{result['status']}] {result['paper_package']}", flush=True)

    results.sort(key=lambda item: natural_key(str(item["paper_package"])))
    summary = {
        "run_id": run_id,
        "completed": sum(item["status"] == "COMPLETED" for item in results),
        "failed": sum(item["status"] != "COMPLETED" for item in results),
        "results": results,
    }
    print(json.dumps(summary, indent=2))
    raise SystemExit(0 if summary["failed"] == 0 else 1)


if __name__ == "__main__":
    main()
