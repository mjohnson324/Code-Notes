# Git

**Version Control**- Software used to manage and track changes to documents.

## Models of Git

* **Box** with a working directory and staged changes to commit
* **Branch** on which this box resides
* Local and remote branches making up a project

## Message Guidelines

1. Limit subject to 50 characters
2. Wrap body at 72 characters
3. Describe commits in an imperative tone
4. Explain what was done and why, not how it was done

Newlines separate commit titles from the body, tucking away longer descriptions.

## Gitignore Operators

Basic: match exact text and directories indicated
`*` - matches file names up to/after than point
`!` - negation operator (does not ignore those specific characters)
`**` - matches directory structure anywhere in the project
`[]` - matches multiple combinations of ranges of characters specified
`?` - matches single characters (length-specific, not character-specific)
