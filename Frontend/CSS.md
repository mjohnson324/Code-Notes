# CSS3

A language for specifying the display of HTML in browsers. Originated in the 2000 as a way to separate concerns in HTML code.

## References

- [Codrops CSS Reference](https://tympanus.net/codrops/css_reference/)
- [Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [CSS Lengths](https://css-tricks.com/the-lengths-of-css/)

## Key Terms

- **Breakpoint**: Pixel at which a media query is applied to change site layout
- **Working Group**: The organization responsible for creating CSS
- **Formatting Context**- Technical term for layout mode such flex, grid, etc. Controlled by display
- **Writing Mode**- Text layout (vertical, horizontal, left, right, etc.)
- **Alignment**- Spec for aligning content and items. Applies universally to different layouts
- **Formatting context** - an element's display setting
- **outer type**- How an element behaves relative to its neighbors
- **inner type**- How an element's children behave
- **Selectors**- Ways of selecting HTML elements to apply display properties to them.
- **Property**- A characteristic of an element.
- **Rule**- A set of properties applied to a particular selector
- **Parent**- Element that contains an element
- **Child**- Element nested in another element
- **Sibling**- Elements nested within the same parent not nested within each other
- **Viewport**- A property defining content area of screen
- **Device Pixel Ratio**- How DIPs get translated to hardware. Hardware Pixels per dip


### Layouts

**Flow**- relative spacing of elements. The default layout
**Flexbox**- *outer type* = block, *inner type* = flex
**Grid**- *outer type* = block, *inner type* = grid
**Multicolumn**- layout mode using columns

### Units


| Unit Type | name | Meaning |
|-----------|------|---------|
| Relative  | rem  | Based on the font size of the root element. |
| | em | Based on the font size of the parent. *Note that font-size cascades* |
| | vw/vh | Viewport units, ranged 1 to 100. Based on size of window. |
| | vmin/vmax | Similar to viewport but alternates between height or width depending on which is larger |
| | % | Percentage. Set based on dimensions of the parent container. Root element references window. |
| Absolute | px | Pixels. The easiest unit to interpret. Unresponsive. |
| Grid | fr | Fractional unit. Defined as a fraction of the grid container dimensions. |

### Pixel Types

1. Hardware- Your screen resolution
2. Device Independent Pixel (DIP)- Pixel sizing based on physical distance

## Key Concepts

- The cascade is a combination of inheritance and specificity
- Element size = width + padding + borders
- Elements out of flow (position, float, etc.) are ignored in layout
- All CSS properties have default values which are applied if not specified
- For any element, the selector ruleset with the greatest specificity gets applied.
- Later defined rules override previous ones
- IDs must be unique to a web page

### Prioritizing dimensions

- Width < Max-width < Min-width (substitute height with width for the rules for height)

## Selector Types Defined from Most to Least Specific

1. User-defined
2. Style attribute (*avoid*)
3. *@media* rules
4. !important (*avoid*)
5. IDs- preceded by
6. Classes / attributes / pseudo-classes
7. Child elements
8. Adjacent siblings
9. Descendants
10. Elements/pseudo-elements (*pseudo-elements reapply dynamically*)
11. Inheritance from parent
12. Default browser styles

### Selector Syntax

- **#**- IDs
- **.**- Classes
- **selector:**- Pseudoclasses
- **selector::**- Pseudoelements

### Combining Selectors

- **Combination**- Selectors joined together. Applies only to elements meeting all criteria
- **Descendant**- Selectors separated by a space. Applies to elements that are descendants of the former selector.
- **Child**- Selectors separated by *>*. Applies to elements that are the immediate children of the former selector.
- **Adjacent Sibling**- Selectors separarted by *+*. Applies to a sibling element immediately following the former selector.

### Attribute Selectors

An element name followed by an attribute specified in brackets `element[attribute="value"]`. The following modifiers can be appended to the attribute name to modify its behavior:

- **None**- Exact match
- **^**- Starts with the specified value
- **$**- Ends with the specified value
- __*__- Contains the specified value
- **~**- Contains the specified value separated by spaces
- **|**- Exact match or followed by a dash

## Tips

- Use a minimum of *40px* by *40px* for button spacing
- Relative positioning is better for responsive layouts
- Set breakpoints based on content
- For responsive designs, start with the smallest device first

## Media Queries

Media queries are key to responsive design. They can be used to define specify rules that apply to specific viewport sizes.

```css
@media screen and (rule) {
  rules
}
```

## Tricks

Preventing unfilled screens by sticking footer at the bottom:

```css
#root {
  min-height: calc(100% - $footer_height);
  position: relative;
  padding-bottom: (size of footer);
}

footer {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
}
```

## Animation

## Transformation
