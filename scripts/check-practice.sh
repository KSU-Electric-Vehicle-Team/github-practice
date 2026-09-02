#!/usr/bin/env bash

set -euo pipefail

submission_count=0

for submission in practice/*.md; do
  if [[ "$submission" == "practice/template.md" ]]; then
    continue
  fi

  submission_count=$((submission_count + 1))

  if grep -q "TODO" "$submission"; then
    echo "ERROR: Replace every TODO in $submission."
    exit 1
  fi

  if ! grep -Eq '^GitHub username: @[A-Za-z0-9-]+$' "$submission"; then
    echo "ERROR: Add a GitHub username such as @octocat in $submission."
    exit 1
  fi

  if ! grep -Eq '^What I want to learn: .+' "$submission"; then
    echo "ERROR: Complete the learning goal in $submission."
    exit 1
  fi

  if ! grep -Eq '^One thing I changed in this file: .+' "$submission"; then
    echo "ERROR: Describe your change in $submission."
    exit 1
  fi
done

if [[ "$submission_count" -eq 0 ]]; then
  echo "ERROR: No completed practice submissions were found."
  exit 1
fi

echo "Practice files look good."

