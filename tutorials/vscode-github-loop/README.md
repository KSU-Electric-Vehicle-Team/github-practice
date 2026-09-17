# VS Code + GitHub loop

This exercise uses a small Python bug to practice the full class workflow in
VS Code. The screenshots shown in class come from Linux. Button placement can
vary on Windows and macOS, so use the named views and Command Palette commands
when the layout differs.

## Before you start

- Finish the first practice submission in the repository root.
- Open the repository folder in VS Code.
- Select the `evt-onboarding` Python interpreter.
- Start from an up-to-date `main` branch with a clean working tree.

## 1. Make your own copy

1. Create a branch named `practice-YOUR-USERNAME-speed`.
2. Copy the `template` folder to `submissions/YOUR-USERNAME`.
3. Replace `YOUR-USERNAME` with your GitHub username.
4. Open `speed.py` and `test_speed.py` with Quick Open.

Do not edit the shared `template` folder or another student's submission.

## 2. See the failure

Run the test from the repository root:

```sh
python -m unittest discover -s tutorials/vscode-github-loop/submissions/YOUR-USERNAME -v
```

The test should fail because the conversion in `speed.py` is deliberately
wrong. Read the expected and actual values before changing the code.

## 3. Debug and fix it

1. Set a breakpoint on the `return` line in `to_kmh`.
2. Open `test_speed.py` and choose **Debug Test** above the test method.
3. Inspect `mps` and step over the return expression.
4. Correct the conversion so 10 metres per second becomes 36 kilometres per
   hour.
5. Run the test again and confirm that it passes.
6. Run **Tasks: Run Test Task**, then select **EVT: Check coding tutorial**.

## 4. Publish a focused change

1. Open Source Control and inspect both changed files.
2. Stage only your submission folder.
3. Commit with `fix: correct YOUR-USERNAME speed conversion`.
4. Publish the branch to your fork.
5. In GitHub Pull Requests, create a draft PR into the team repository's
   `main` branch.
6. Record the failing test, the fix, and the passing check in the PR body.

## 5. Review and revise

1. Give the PR URL to a partner.
2. The reviewer checks out the PR, reads the diff, and runs the same test.
3. The reviewer leaves one useful comment and submits the review.
4. The author makes the requested change on the same branch, reruns the test,
   commits, and pushes.
5. Recheck the latest diff and `quality` result before requesting lead review.

After a lead merges the PR, switch to `main`, pull from `upstream`, and delete
the finished branch only after confirming that its work is on `main`.
