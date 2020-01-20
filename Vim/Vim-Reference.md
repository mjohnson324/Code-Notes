# VIM: The Text Editor of Pros, or a Waste of Time?

Notes on Vim commands. Typed in Vim!

## Modes

1. **Normal**: Execute commands
2. **Insert**: Insert text

Press **ESC** to enter normal mode. Takes you out of insert mode and cancels commands.

## Concepts

**Operator-Motion**: A pattern followed by many vim commands. The
operator defines the change command and the motion defines what text to
operate on. For example, _d motion_ deletes different sets of characters
depending on the motion.

**Counts**: Motions can be executed repeatedly if preceded by numerical counts. For example, _3$_ moves to the end of the line for the next three lines. For operators the number precedes the motion e.g. _d # motion_

## Basic Commands

:!<command> Enter a terminal command and immediately return to vim
Type | Key | Description
----------------------------
Movement | h | left
| j | down
| k | up
| l | right
| w | move to start of next word
| e | move to end of current word, or the next word if at the end
| $ | move to the end of the line
| 0 | move to the start of the line. **Doesn't respond to counts**.
Exiting Vim | :q | quit
| :q! | quit without saving changes
| :wq | quit and save changes
| :w | save changes without quitting
Insertion | i | insert text before the cursor
| a | insert text after cursor
| A | append text to end of line
| p | Put. Pastes the last set of text deleted after the cursor.
| r | Replace character at the cursor. Type _r_ followed by the character you want to substitute.
Deletion | x | delete character before the cursor
| dw | delete up to start of next word _excluding_ its first character
| d$ | delete end of line _including_ last character
| de | delete to the end of the current word _including_ the last character
| dd | delete the current line. **Count precedes the operator in this case**.
Time Travel | u | undo last command
| U | Fix line. Reverts last line altered to its previous state.
| **CTRl**-R | Redo last command

Commands
:m <location> move lines to specified location. Defaults to current line.
:#: Jump to the line number specified in command mode
:#,# selects multiple lines in visual mode that can be further processed
:sh: enter interactive shell
:!_command_: execute command in Vim. Use for non-interactive commands
:r _text_: Inserts the text output into the current file. Works for both files and command line redirection
:x: save and exit
:vsp: vertical split (tabs left and right); opens with same file by default
:sp: same but horizontal (stacked tabs)
:s/_text_/_replacement_/_command_ : find and replace
Without command, replaces next occurrence
With g, replaces every command in line
%s replaces every occurrence in file
#,# replaces over the specified lines
/ and ?: search operator, find text going forward/backward
n/N: find next/previous instance
control-D: when typing in a command with : see available commands starting with the text
<leader>: A key used to start many custom Vim commands. \ by default.

Searching
\zs: special character denoting starting bracket of an en expression
\ze: same as \zs for the end of an expression
()?+| all require the escape character in searches. {} requires one for the opening bracket.

Tab completion is enabled for commands
Commands can be chained.
Movements can be multiplied with numbers.
operator-number-motion: perform given action number times.
If lines are selected in visual mode they will be saved via :w FILENAME
To turn off an option in vimrc, prepend “no” (e.g. noic

Command Mode
control-R: redo
u - undo
z- fold (follow with a,c,o,r,m, or their caps to fold in different ways)

Macros:
q: Record a macro and register it to a-z.
@: Play a macro recorded under a-z.

Non-Typing Text Operations (Cut, Paste, Delete, etc.)
d: cut
dd: cut line
D: Cut from cursor to end of line
y: copy selection
Y: copy line
p: Paste after cursor
P: Paste on cursor
J: Join selected lines (next one to current one by default)
r: Replace character under cursor
x/X: Delete/backspace
~: Toggle case
>/<: Indent/unindent lines. Responds to motion commands.

(/): move to the next/previous sentence as defined by periods.
{/}: move to the next/previous paragraph (separated by newlines)
control-f/control-b: move forward/backward one page
gg: move to start of file
#G: move to line # (end of file if no number)
hjkl: movement keys
H: move to top of window
M: move to middle of window
L: move to bottom of window
$: end of line
0: start of line
^: start of line excluding whitespace
w: start of next word
e: end of current word
b: previous word
f/F/t/T: find next/previous character. T and t stop before the character.
W/E/B: only accounts for whitespace
control-o: retrace steps backward
control-i: retrace steps forward
%: move to next matching bracket
*/#: find next/previous instance of word under cursor.
m: set marks using a-z
`: move to mark set by m
[[/]]: Jump to next/previous { in column 0.

Insertion
A: insert at end of line
I: insert before 1st non-space character
o: insert on new line below
O: insert on new line above
R: replace mode
s: Delete character under cursor, enter insert mode
c: change (delete/insert)
S: change whole line
C: Change to end of line.

Visual Mode: Operators act automatically on visual selections
v: enter visual mode (cursor)
V: select whole lines
control-v: select columns (move cursor down and only high characters in same column)

Moving lines:
:<optional range>m <destination>

Vim:
-p for new tab, -o for new window
Vim has fuzzy completion, so partial spelling works if Vim can map to the full word
<C-W> = rezise all windows equally
:verbose shows option
:tabs lists tabs
:tabn, :tabp cycles
:tabedit <file> opens file in new tab
<ctrl-w> hjkl, w cycles
:noh
Tabs take priority over windows. In a given tab only one file name is displayed.
:<,>:s/$/,/ places commas at the end of the given line range.
autocmd BufRead,BufNewFile *.<type> set filetype=<type>

# Vim Reference

## Global

- **:help keyword** - open help for keyword
- **K** - open man page for word under the cursor

## Cursor movement

- **hjlk** - move cursor
- **H** - move to top of screen
- **M** - move to middle of screen
- **L** - move to bottom of screen
- **w** - jump forwards to the start of a word
- **W** - jump forwards to the start of a word (words can contain punctuation)
- **e** - jump forwards to the end of a word
- **E** - jump forwards to the end of a word (words can contain punctuation)
- **b** - jump backwards to the start of a word
- **B** - jump backwards to the start of a word (words can contain punctuation)
- **%** - move to matching character (default supported pairs: '()', '{}', '[]' - *use `:h matchpairs` in vim for more info)*
- **0** - jump to the start of the line
- **^** - jump to the first non-blank character of the line
- **$** - jump to the end of the line
- **g_** - jump to the last non-blank character of the line
- **gg** - go to the first line of the document
- **G** - go to the last line of the document
- **5G** - go to line 5
- **fx** - jump to next occurrence of character x
- **tx** - jump to before next occurrence of character x
- **Fx** - jump to previous occurence of character x
- **Tx** - jump to after previous occurence of character x
- **;** - repeat previous f, t, F or T movement
- **,** - repeat previous f, t, F or T movement, backwards
- **}** - jump to next paragraph (or function/block, when editing code)
- **{** - jump to previous paragraph (or function/block, when editing code)
- **zz** - center cursor on screen
- **Ctrl + e** - move screen down one line (without moving cursor)
- **Ctrl + y** - move screen up one line (without moving cursor)
- **Ctrl + b** - move back one full screen
- **Ctrl + f** - move forward one full screen
- **Ctrl + d** - move forward 1/2 a screen
- **Ctrl + u** - move back 1/2 a screen

**Tip** Prefix a cursor movement command with a number to repeat it. For example, **4j** moves down 4 lines.

## Insert mode - inserting/appending text

- **i** - insert before the cursor
- **I** - insert at the beginning of the line
- **a** - insert (append) after the cursor
- **A** - insert (append) at the end of the line
- **o** - append (open) a new line below the current line
- **O** - append (open) a new line above the current line
- **ea** - insert (append) at the end of the word
- **Esc** - exit insert mode

## Editing

- **r** - replace a single character
- **J** - join line below to the current one with one space in between
- **gJ** - join line below to the current one without space in between
- **gwip** - reflow paragraph
- **cc** - change (replace) entire line
- **C** - change (replace) to the end of the line
- **c$** - change (replace) to the end of the line
- **ciw** - change (replace) entire word
- **cw** - change (replace) to the end of the word
- **s** - delete character and substitute text
- **S** - delete line and substitute text (same as cc)
- **xp** - transpose two letters (delete and paste)
- **u** - undo
- **Ctrl + r** - redo
- **.** - repeat last command

## Marking text (visual mode)

- **v** - start visual mode, mark lines, then do a command (like y-yank)
- **V** - start linewise visual mode
- **o** - move to other end of marked area
- **Ctrl + v** - start visual block mode
- **O** - move to other corner of block
- **aw** - mark a word
- **ab** - a block with ()
- **aB** - a block with {}
- **ib** - inner block with ()
- **iB** - inner block with {}
- **Esc** - exit visual mode

## Visual commands

- **&gt;** - shift text right
- **&lt;** - shift text left
- **y** - yank (copy) marked text
- **d** - delete marked text
- **~** - switch case

## Registers

- **:reg** - show registers content
- **"xy** - yank into register x
- **"xp** - paste contents of register x

**Tip** Registers are being stored in ~/.viminfo, and will be loaded again on next restart of vim.
**Tip** Register 0 contains always the value of the last yank command.

## Marks

- **:marks** - list of marks
- **ma** - set current position for mark A
- **`a** - jump to position of mark A
- **y`a** - yank text to position of mark A

## Macros

- **qa** - record macro a
- **q** - stop recording macro
- **@a** - run macro a
- **@@** - rerun last run macro

## Cut and paste

- **yy** - yank (copy) a line
- **2yy** - yank (copy) 2 lines
- **yw** - yank (copy) the characters of the word from the cursor position to the start of the next word
- **y$** - yank (copy) to end of line
- **p** - put (paste) the clipboard after cursor
- **P** - put (paste) before cursor
- **dd** - delete (cut) a line
- **2dd** - delete (cut) 2 lines
- **dw** - delete (cut) the characters of the word from the cursor position to the start of the next word
- **D** - delete (cut) to the end of the line
- **d$** - delete (cut) to the end of the line
- **x** - delete (cut) character

## Exiting

- **:w** - write (save) the file, but don't exit
- **:w !sudo tee %** - write out the current file using sudo
- **:wq** or **:x** or **ZZ** - write (save) and quit
- **:q** - quit (fails if there are unsaved changes)
- **:q!** or **ZQ** - quit and throw away unsaved changes
- **:wqa** - write (save) and quit on all tabs

## Search and replace

- **/pattern** - search for pattern
- **?pattern** - search backward for pattern
- **\vpattern** - 'very magic' pattern: non-alphanumeric characters are interpreted as special regex symbols (no escaping needed)
- **n** - repeat search in same direction
- **N** - repeat search in opposite direction
- **:%s/old/new/g** - replace all old with new throughout file
- **:%s/old/new/gc** - replace all old with new throughout file with confirmations
- **:noh** - remove highlighting of search matches

## Search in multiple files

- **:vimgrep /pattern/ {file}** - search for pattern in multiple files

e.g.**:vimgrep /foo/ **/***

- **:cn** - jump to the next match
- **:cp** - jump to the previous match
- **:copen** - open a window containing the list of matches

## Working with multiple files

- **:e file** - edit a file in a new buffer
- **:bnext** or **:bn** - go to the next buffer
- **:bprev** or **:bp** - go to the previous buffer
- **:bd** - delete a buffer (close a file)
- **:ls** - list all open buffers
- **:sp file** - open a file in a new buffer and split window
- **:vsp file** - open a file in a new buffer and vertically split window
- **Ctrl + ws** - split window
- **Ctrl + ww** - switch windows
- **Ctrl + wq** - quit a window
- **Ctrl + wv** - split window vertically
- **Ctrl + wh** - move cursor to the left window (vertical split)
- **Ctrl + wl** - move cursor to the right window (vertical split)
- **Ctrl + wj** - move cursor to the window below (horizontal split)
- **Ctrl + wk** - move cursor to the window above (horizontal split)

## Tabs

- **:tabnew** or **:tabnew file** - open a file in a new tab
- **Ctrl + wT** - move the current split window into its own tab
- **gt** or **:tabnext** or **:tabn** - move to the next tab
- **gT** or **:tabprev** or **:tabp** - move to the previous tab
- **#gt** - move to tab number #
- **:tabmove #** - move current tab to the #th position (indexed from 0)
- **:tabclose** or **:tabc** - close the current tab and all its windows
- **:tabonly** or **:tabo** - close all tabs except for the current one
- **:tabdo *command*** - run the command on all tabs (e.g. `:tabdo q` - closes all opened tabs)
