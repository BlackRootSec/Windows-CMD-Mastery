# Troubleshooting Workflow

Volume 2 includes networking troubleshooting decision trees (Chapter 34), repair/recovery (Chapter 38), and performance measurement and triage (Chapter 39). Use those chapters for their detailed procedures. This page is a conservative workflow for organizing observations before changing anything.

## A cautious sequence

1. **Define the symptom.** Record what failed, when it began, the exact error, and whether the problem is repeatable.
2. **Establish context.** Record Windows edition/build, account privilege level, network state if relevant, and recent approved changes.
3. **Inspect before changing.** Prefer status and information commands first. Save output to a scratch report only if it contains no secrets or unnecessary personal data.
4. **Narrow the layer.** For networking, follow the source's bottom-up decision tree rather than running an arbitrary command collection.
5. **Make one controlled change at a time.** Have a rollback plan and appropriate authorization. Do not disable security protections as a default troubleshooting tactic.
6. **Verify.** Repeat the original test and record both expected and actual results.
7. **Recover or escalate.** Stop when an action might affect boot, disks, encryption, or protection and the recovery path is unclear.

## What to record

| Field | Notes |
|---|---|
| Symptom | Exact observed behavior, not a conclusion |
| Timestamp | Include timezone when relevant |
| Environment | Windows version/build and relevant configuration |
| Tests | Command or UI action and why it was chosen |
| Results | Exact output with secrets redacted |
| Changes | What changed, by whom, and when |
| Recovery | Cleanup/rollback performed and its verification |
| Remaining uncertainty | What the evidence does not establish |

Use the source book's procedure and verification notes for command syntax and version-sensitive behavior.
