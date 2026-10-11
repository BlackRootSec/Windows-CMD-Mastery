# Getting Started

## Choose your entry point

- **New to command lines:** read Volume 1, Chapters 1–3, then work through the command reference.
- **Comfortable with basic CMD:** review Volume 1's parser and batch-scripting chapters before moving to Volume 2.
- **Windows administration focus:** use Volume 2 as a structured reference, while checking prerequisites for each exercise.
- **Defensive security focus:** build the fundamentals first; Volume 3 explicitly relies on command parsing and batch knowledge.

## Prepare a scratch space

Create a folder that contains only test artifacts. Avoid system folders, personal documents, shared folders, and production data. Use the same dedicated folder throughout your exercises so cleanup can be verified.

Example path for planning: `C:\CMD-Lab`. Create it manually in File Explorer or use a low-impact command only after reviewing what it does.

## Learn deliberately

1. Read the full lab objective and prerequisites.
2. Identify whether the instructions inspect state or change it.
3. Type and explain each command yourself.
4. Compare the output with the expected result from the source.
5. Perform and verify cleanup.
6. Note OS version, edition, privilege context, and any differences.

## CMD versus PowerShell

CMD (`cmd.exe`) and PowerShell are different command interpreters. They have different syntax and parsing rules. This repository is centered on CMD and batch scripting. If a guide mentions a PowerShell alternative, it must be clearly labeled as PowerShell.

## Verify version-sensitive behavior

Windows commands can differ by build, edition, policy, and installed features. Consult the source book's verification notes and current official Microsoft documentation before relying on a command in operational work.
