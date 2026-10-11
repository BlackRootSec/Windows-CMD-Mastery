# CMD Parser Internals and Edge Cases

**Source:** Volume 1, Part III (Chapters 10–12) and Part IV (Chapter 13); Volume 3, Chapter 47 for the security implications of unsafe batch input.

Topics listed in the source include percent expansion, special characters and tokenizing, block parsing, delayed expansion, redirection, `CALL` and second-pass behavior, command lookup, `PATH`, `PATHEXT`, argument parsing, spaces in paths, quotes, parentheses, code pages, line endings, and standard input.

## Learning objective

Understand that CMD has parsing and expansion rules that can change how a command line is interpreted. When reviewing a script, pay particular attention to user-controlled data, quoting, and multiple parsing passes.

For security implications and defensive patterns, read Volume 3, Chapter 47 and [Defensive Security](../defensive-security/README.md). Avoid experimenting with unknown inputs against valuable files or systems.
