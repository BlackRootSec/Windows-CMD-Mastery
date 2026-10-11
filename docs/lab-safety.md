# Lab Safety and Reversibility

The supplied volumes state that commands are for systems you own or are explicitly authorized to administer and advise running labs in an isolated virtual machine with a snapshot. They also warn that configuration, security, disk, boot, and encryption changes can cause data loss.

## Before each lab

- [ ] Read the objective, prerequisites, expected result, and cleanup instructions.
- [ ] Confirm the target is owned by you or explicitly within your authorization.
- [ ] Determine whether the commands are read-only, state-changing, or potentially destructive.
- [ ] Take a VM snapshot before a lab that can modify system or security state.
- [ ] Disconnect the lab from networks that are not needed and not under your control.
- [ ] Use synthetic data and a dedicated scratch directory.
- [ ] Keep a note of the system version and the commands you ran.

## Risk labels

| Label | Meaning | Practice |
|---|---|---|
| Read-only | Inspects state without intentionally modifying it | Still review privacy and permissions before recording output. |
| State-changing | Modifies files, settings, configuration, or other state | Prefer a disposable VM; back up relevant test data and know how to revert. |
| Potentially destructive | Could cause data loss, impair boot or protection, or change disks/encryption | Do not run casually; use a snapshot and only follow a source lab with a clear recovery procedure. |

## After the lab

1. Compare the result to the source's expected result.
2. Execute the documented cleanup.
3. Verify that temporary files, tasks, service entries, or other lab artifacts were removed as required.
4. Restore the snapshot when appropriate.
5. Record any mismatch instead of improvising risky fixes.

This page is general guidance; it does not replace a lab's own prerequisites, caution labels, or cleanup procedure. Never execute unfamiliar command examples during documentation generation or just to see what they do.
