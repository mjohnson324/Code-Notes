# Git

**Version Control**- Software used to manage and track changes to documents.

## Key Concepts

- **Dev Environment** - Consists of your *working directory* (unsaved changes), *staged changes* (ready to commit to the local repo) and the *local repository* (ready to push to the remote). This applies separately to each branch in a project.
- **Interactive mode** applies multiple git commands to make changes to a branch. Useful for actions like squashing.
- **Public History** - history that is part of the remote repository.

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

## Important Commands and Options

*--continue* and *--abort* - options that allow you to continue in the event of a conflict. The first proceeds with a merge while the second reverses it.
*--amend* - An option for commit that integrates additional changes to an existing commit and allows you to alter the existing message.
  - Great for fixing bad commits.

**Git-secret** - A tool for storing secrets like keys
**Rebase** - Similar to merge but alters current branch to set another branch's commit as the common ancestor. Defaults to HEAD.
  - Integrates changes from the other branch into the current one
  - Useful for frequent merging of non-conflicting branches
  - Cleaner commit history than *merge* which adds an additional commit
**Stash** - Stores uncomitted changes in a stack-like manner.
  - Useful for *pull* and *fetch* conflicts
**Pull** - merges changes from a remote branch
  - Use *--r* option to rebase instead of merging branches.
**Cherry-pick** - Select specific commits from one branch to merge into another.
**Squash** - combines multiple commits into one. By default merges the commit in question with the one before it.