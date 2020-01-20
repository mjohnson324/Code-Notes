Consult WCAG to learn more.

Key Qualities:
1. Percievable (text, color)
2. Operable (#1 is keyboard accessibility)
3. Understandable (& predictable)
4. Robust

Go-Tos:
Use alt-tags on images. Empty alt strings indicate images that can be ignored
set tabindex=-1 means to ignore an element
Use the role attribute intelligently to specify intended behavior (like "button" for anchors)
Semantic Headings (use h's properly!)
Be judicious with colors
Don't substitute text with images
16px and 1.5 line-height for body content
12px for aside text
set lang on html
Use sections sparingly

Major Takeaways From Accessibility Paper:
There are a lot of disabled people, enough to establish a second Facebook
They make bank
Designing for them improves websites for everyone.
Writing Guidelines:
Use direct and succinct sentences
Use bulleted lists
Place the main point and keywords at the beginning of elements!
Repetitive phrasing annoys users
Use empty alts for decorative elements
Don't expect users to know what "navigation" means. Try "skip to main content" instead.
Users search by subject matter and stop after a few words. This can make questions annoying (think "NYHAIS - Who are we?" Instead of "Who we are")
Reader Guidelines:
Screen Readers = Vim. They have one mode for reading and another for typing!
Minimize the number of links per page. Screen readers count them.
Know screen reader features, and that users rarely know all of them.
Spell properly where possible. Screen readers get confused by combo words. <acronym> and <abbr> tags help!
Screen readers can get confused by alt-tags and text that don't match. Match them!
Screen readers interpret page refreshes as new pages. Prevent it if users are scanning the same page.
Design:
Make one website accessible. No one wants the text version.
Readers can make lists of page links. Make the text inside of them descriptive.
Anchor links: essential for navigating multi-subject pages.
Headers: clear, meaningful, parallel. This makes finding relevant subjects a lot easier.
Forms: near the beginning of a page. Why? Because users may try to scan the whole page instead of using a command to find them.
Inputs: use labels! Add extra information with title attributes. Switching reader modes to check fields is overkill.
