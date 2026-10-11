# Contributing

Thanks for helping improve the Windows CMD Mastery documentation.

## Good contributions

- Correct a typo, broken link, or confusing explanation.
- Add a source-grounded index or chapter cross-reference.
- Clarify the difference between CMD syntax and PowerShell syntax.
- Improve safety labeling, prerequisites, expected results, or cleanup steps.
- Add a harmless example that is understandable and reviewable.

## Before submitting

1. Search for existing content to avoid duplication.
2. Cite the volume, chapter, and printed page for source-derived claims.
3. Label new repository-authored material as supplementary when it goes beyond the PDFs.
4. Do not claim commands were tested unless you actually tested them; record the Windows version and test environment.
5. Use synthetic examples and remove secrets, tokens, private paths, and personal data.
6. Never include malware, credential theft, evasion, or unauthorized-access instructions.
7. Confirm that contributed materials may be redistributed under the repository's eventual license terms. The PDFs themselves are marked “All rights reserved”; see [LICENSE-STATUS.md](LICENSE-STATUS.md).

## Validation

Run the internal Markdown-link check from the repository root:

```text
python scripts/validate_links.py
```

The script validates repository-relative links and local anchors. It does not verify external website availability or the technical correctness of commands.

## Pull request expectations

Explain what changed, why it is useful, which files or source chapters are affected, how links were validated, and whether any commands were tested. Keep changes scoped and easy to review.
