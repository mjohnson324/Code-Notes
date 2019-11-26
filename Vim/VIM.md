# VIM: The Text Editor of Pros, or a Waste of Time?

Notes on Vim commands. Typed in Vim!

## Modes

1. **Normal**: Execute commands
2. **Insert**: Insert text

Press **ESC** to enter normal mode. Takes you out of insert mode and cancels commands.

## Concepts

**Operator-Motion**: A pattern followed by many vim commands. The operator defines the change command and the motion defines what text to operate on. For example, _d motion_ deletes different sets of characters depending on the motion.

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

- [ ] Continue at 3.3
