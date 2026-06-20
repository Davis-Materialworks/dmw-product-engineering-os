# XD Asset Pipeline

## Asset classes

- icons: prefer SVG, currentColor, accessible labels when interactive
- illustrations: SVG if simple, optimized raster if complex
- photos: responsive image pipeline, alt text, dimensions
- logos: SVG with clear usage rules
- masks/clips: convert carefully; avoid brittle absolute positioning
- gradients/shadows: convert to tokens when repeated

## Export rules

- Use semantic filenames.
- Deduplicate repeated assets.
- Optimize SVGs but preserve viewBox.
- Avoid embedding text inside images unless required for brand artwork.
- Convert decorative images to aria-hidden or empty alt.
- Provide descriptive alt for informative images.

## Creative Cloud workflow

When assets come from Creative Cloud Libraries, preserve library names, brand context, and source notes where available.
