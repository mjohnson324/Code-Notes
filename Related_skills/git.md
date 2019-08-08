Version Control- Term for software used to manage changes to documents
	-Tracking and teamwork capabilities

Models:
	a. Box (working directory vs staged changes to commit)
		b. Branch (on which the "box" resides)
			c. Local vs remote (branches)

-Newlines allow separation of of title from body for longer descriptions

Message Guidelines:
	-Limit subject to 50 characters
	-Wrap body at 72 characters
	-Describe commit in an imperative tone
	-Explain what was done and why, not how it was done
	

New branches: git checkout -b [name]

Gitignore:
    Basic: match exact text and directories indicated
    * - matches file names up to/after than point
    ! - negation operator (does not ignore those specific characters)
    ** - matches directory structure anywhere in the project
    [] - matches multiple combinations of ranges of characters specified
    ? - matches single characters (length-specific, not character-specific)
