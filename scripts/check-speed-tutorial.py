#!/usr/bin/env python3
"""Run the VS Code tutorial tests in every student submission folder."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUBMISSIONS = ROOT / "tutorials" / "vscode-github-loop" / "submissions"


def main() -> int:
    submission_dirs = sorted(
        path
        for path in SUBMISSIONS.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )

    if not submission_dirs:
        print("No coding tutorial submissions to check.")
        return 0

    failed = False
    for submission in submission_dirs:
        required = [submission / "speed.py", submission / "test_speed.py"]
        missing = [path.name for path in required if not path.is_file()]
        if missing:
            print(f"ERROR: {submission.relative_to(ROOT)} is missing: {', '.join(missing)}")
            failed = True
            continue

        print(f"Checking {submission.relative_to(ROOT)}")
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "unittest",
                "discover",
                "-s",
                str(submission),
                "-p",
                "test_*.py",
                "-v",
            ],
            cwd=ROOT,
            check=False,
        )
        failed = failed or result.returncode != 0

    if failed:
        print("One or more coding tutorial submissions failed.")
        return 1

    print("Coding tutorial submissions look good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
