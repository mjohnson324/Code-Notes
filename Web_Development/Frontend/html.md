# HTML

Microsoft word for the internet.
For details on specific elements refer to the [Mozilla Development Network](https://developer.mozilla.org/)

## Key Terms

- **Element** - Container specifying the nature of a portion of a document
- **Tag** - Signifies the opening and closing of an element
- **Attribute** - A characteristic of an element
- **Value** - An attribute's state
- **Nesting** - Placing one element inside another
- **Container**- An element that has elements within it (eg. ul with li)

## Key Concepts

- Elements are like boxes, and they can contain more boxes
- Content can overflow a container
- Margins do not alter an element's size; the other properties do
- Element Sizing: **Margin** -> **Border** -> **Padding** -> **Element**

## Semantic HTML

- **Head** - for holding a page's metadata, including:
  ```html
  <title>Title</title>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  ```
- **Header**- For holding elements at the top of the page
- **Footer**- Like the header, but for the bottom
- **Nav**- Navigation, for holding links
- **Article**- Holding text (posts, comments, etc.)
- **Aside**- A sidebar
- **Figure**- Images, graphics, code samples, etc.
- **Figcaption**- Complementary caption text for a figure
- **Section**- For partitioning distinct parts of a site
	- Don't use sections as substitutes for divs
- **Div**- For everything else; the generic element
- **Lists** *(ordered, unordered, definitions)*- self-explanatory
- **Media**- Includes *images*, *video*, *audio*, *math*, *canvas*, and *svg*

## Tips

- Assign `rel="noopener noreferrer"` for anchors to prevent hacks when _blank is set as target