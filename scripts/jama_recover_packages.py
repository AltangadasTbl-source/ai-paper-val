#!/home/juliz/venvs/stt/bin/python
"""Recover a small set of packages when a catalog request is rate-limited.

This uses normal page navigation in the locally running isolated Chrome
profile, then delegates package creation and public-CDN downloads to the same
safe helpers used by ``jama_fetch_new.py``.
"""

from __future__ import annotations

import json
import subprocess
import time

from jama_fetch_new import ROOT, create_package


TARGETS = {
    "10.1001/jama.2024.23898": "https://jamanetwork.com/journals/jama/fullarticle/2827435",
    "10.1001/jama.2024.0318": "https://jamanetwork.com/journals/jama/fullarticle/2815401",
    "10.1001/jama.2024.0572": "https://jamanetwork.com/journals/jama/fullarticle/2814932",
}
EXPRESSION = (
    "JSON.stringify({doi:document.querySelector('meta[name=\\\"citation_doi\\\"]')?.content,"
    "title:document.querySelector('meta[name=\\\"citation_title\\\"]')?.content,"
    "url:location.href,supplements:[...document.querySelectorAll('a.supplement-download')]"
    ".map(a=>({label:a.parentElement.innerText.replace(/\\s+/g,' ').trim(),href:a.href}))})"
)


def browser(command: str, value: str) -> dict[str, object]:
    invocation = [
        "powershell.exe",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        "scripts/jama_browser.ps1",
        command,
        value,
        "-Port",
        "9223",
    ]
    result = subprocess.run(invocation, cwd=ROOT, check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def article(doi: str, url: str) -> dict[str, object]:
    for attempt in range(3):
        browser("navigate", url)
        time.sleep(4)
        result = browser("eval", EXPRESSION)
        data = json.loads(result["result"]["result"]["value"])
        if data.get("doi") == doi and data.get("supplements"):
            return data
        time.sleep(attempt + 1)
    raise RuntimeError(f"Could not load supplements for {doi}")


def main() -> None:
    completed = []
    failures = []
    for doi, url in TARGETS.items():
        try:
            completed.append(create_package(article(doi, url)))
        except Exception as error:
            failures.append({"doi": doi, "error": str(error)})
    print(json.dumps({"completed": completed, "failures": failures}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
