# CSS

Originated in the 2000 as a way to separate concerns in HTML code, focusing on presentation

The cascade is a combination of inheritance and specificity

Box = width + padding + borders

Formatting context - an element's display setting
outer type- How an element behaves relative to its neighbors
inner type- How an element's children behave

Flexbox- outer type = block, inner type = flex

Flow- relative spacing of elements
Elements out of flow (position, float, etc.) are ignored
Keep in mind how to manage overlap
Layout- flow, flex, grid, multicolumn
Alignment- Applies universally to different layouts

All CSS properties have default values which are applied if not specified

Relative Units- rem (based on the font size of an HTML element), em/ch/ex (font size of parent), vw & vh (viewport units, ranged 1 to 100), vmin & vmax (alternates to height or width depending on which is bigger)
Absolute Units- px and %
Grid- fr (fraction unit) and minmax

## Selector Types

**Selectors**- Ways of selecting HTML elements to apply display properties to them.
The selector ruleset with the greatest specificity gets applied.

1. IDs
2. Classes
3. Elements
4. Pseudo-class- Acts like a class
5. Pseudo-element- Reapplies dynamically

**Viewport**- Defines content area of screen

### Pixel Types

1. Hardware- Your screen resolution
2. Device Independent Pixel (DIP)- Pixel sizing based on physical distance

**Device Pixel Ratio**- How DIPs get translated to hardware.
**DPR**- Hardware Pixels per dip

```HTML
<meta name='viewport' content='width=device-width, initial-scale=1'>
```

Use a minimum of *40px* by *40px* for button spacing
Relative positioning is better for responsive layouts
Width < Max-width < Min-width

Breakpoint: Pixel at which a media query is applied to change site layout
Set breakpoints based on content
Start with the smallest device first

Working Group: Organization responsible for creating CSS
Formatting Context- Technical term for layout mode such flex, grid, etc. Controlled by display
Flow- The default layout
Writing Mode- Text layout (vertical, horizontal, left, right, etc.)
Alignment- Spec for aligning content and items
Multicolumn- layout mode using columns

Trick for preventing unfilled screens by sticking footer at the bottom:
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

## Animation

## Transformation