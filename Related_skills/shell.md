# Bash

* **Root**- The parent directory
* **Working Directory**- Directory in which you currently reside
* **Option**- Command extensions which modify a command's default behavior. Options can be grouped together after a - in any order
* **Redirection**- When standard input/output/error are rerouted

## Useful apt commands

* Check broken dependencies- `apt check`
* Remove uninstalled deb packages- `apt autoclean`
* Clear space by removing unused packages- `apt autoremove`
* Remove a package and its configuration files: `apt purge`

## Control Flow Operators

* `||`- OR
* `!`- NOT
* `&&`- AND
* `;;`- Ends case statements


## Redirection Operators: command _ file

* `|&`- Passes standard output and error
* `|`- "Pipe" passes output of 1st as input to 2nd
* `<`- Read-only
* `>`- Creates/overwrites file
* `2>`- Variant for errors (> implies 1>)
* `>|`- Same as > but bypasses overwrite restrictions
* `<>`- Read and write
* `>>`- Appends to existing files
* `&>`- Standard error & output

## Other Syntax

* `&`- Background task (1st runs in background)
* `;`- 2nd command runs regardless of how 1st ends up
* `(`- Group and launch commands
* `{`- Group but do not launch commands in subshell

## Useful Commands

* **cp** -nibr
  * cp overwrites files without asking
  * The last directory listed is interpreted as the target directory
  * i asks before overwriting
  * n prevents overwriting
  * b backs up a file before overwriting
  * r copies recursively (for directories)
* **cat** -nbs
  * Short for "catenate" (combines files in the order specified)
  * Combo outputs can be redirected to new files.
  * n numbers lines
  * b numbers non-empty lines
  * s combines consecutive empty lines into one

* **less** file1 file2 file3 etc.
  * Use for paging through a file (better than cat for long files)
  * N numbers lines (-n undoes it)
  * m shows % read (-M also shows current line # in view)
    * q to quit
    * G in file to go to end; g to go to beginning
    * I to ignore case in searches
    * /word to find the word or regular expression in the text

* **man** _command_
  * Look up documentation on commands in the terminal
