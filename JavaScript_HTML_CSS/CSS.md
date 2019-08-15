# CSS

-Originated in the 2000 as a way to separate concerns in HTML code
-CSS is concerned with the presentation of HTML

Selectors- Ways of selecting HTML elements to apply display properties to
The selector ruleset with the greatest specificity gets applied.

Selector Types:
IDs
Classes

Viewport- Defines content area of screen

Pixel Types:
    1. Hardware- Your screen resolution
    2. Device Independent Pixel (DIP)- Pixel sizing based on physical distance

Device Pixel Ratio- How DIPs get translated to hardware.
DPR = Hardware Pixels per dip

```HTML
<meta name='viewport' content='width=device-width, initial-scale=1'>
```

Minimum button spacing: 40px by 40px

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
