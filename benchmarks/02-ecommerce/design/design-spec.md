# Ecommerce Product Detail Page — Design Specification

## Product Context
Direct-to-consumer apparel brand product detail page. Users browse product imagery, select variants (size, color), read reviews, view related items, and add to cart. The page must convert browsers into buyers while maintaining brand identity.

## User Goals
- See high-quality product images with zoom and gallery navigation
- Select size and color variants with clear availability feedback
- Read customer reviews with filtering and rating distribution
- View related/complementary products without leaving the page
- Add to cart with clear confirmation and no page navigation

## Color Palette
| Token | Hex | Usage |
|---|---|---|
| `surface.page` | `#FFFFFF` | Page background |
| `surface.card` | `#F9FAFB` | Review cards, related product cards |
| `surface.overlay` | `rgba(0,0,0,0.5)` | Zoom modal backdrop |
| `text.primary` | `#111827` | Product name, prices, body |
| `text.secondary` | `#6B7280` | SKU, meta, review dates |
| `action.primary.bg` | `#111827` | Add to cart, primary CTAs |
| `action.primary.text` | `#FFFFFF` | Text on primary buttons |
| `feedback.success` | `#059669` | In-stock, added-to-cart confirmation |
| `feedback.error` | `#DC2626` | Out of stock, form errors |
| `border.default` | `#E5E7EB` | Card borders, divider lines |
| `focus.ring` | `#4F46E5` | Focus indicator |

## Typography Scale
| Token | Size / Line | Weight | Usage |
|---|---|---|---|
| `heading.product` | 28px / 1.2 | 700 | Product name |
| `heading.section` | 18px / 1.3 | 600 | Reviews, related products headings |
| `display.price` | 24px / 1.1 | 700 | Current price |
| `display.price-strikethrough` | 16px / 1.1 | 400 | Original price (with line-through) |
| `body.default` | 15px / 1.6 | 400 | Description, review bodies |
| `label.option` | 13px / 1.4 | 600 | Size/color labels |
| `caption.meta` | 12px / 1.4 | 400 | SKU, review counts |
| Font family: system-ui stack (Inter, -apple-system, Segoe UI) |

## Component Inventory
- **ProductGallery** — Hero image with thumbnail strip; click opens fullscreen zoom modal with pinch/scroll
- **VariantSelector** — Color swatches (circular, 36px) + size chips (rectangular, 44px min); disabled state for unavailable options
- **ProductInfo** — Name, price (with sale/discount display), short description, SKU
- **AddToCart** — Quantity stepper + primary CTA button; transitions to "Added!" confirmation with cart count badge update
- **ReviewList** — Star rating distribution bar chart, sort dropdown (newest/highest/lowest), paginated review cards with avatar/name/date/verified badge
- **ReviewCard** — Rating stars, title, body, fit feedback, photo attachments (if any)
- **RelatedProducts** — Horizontal scroll carousel of ProductCard components with image/name/price
- **BreadcrumbNav** — Home > Category > Subcategory > Product (with schema.org BreadcrumbList markup)
- **StickyAddToCart** — Mobile-only sticky bottom bar with price + add-to-cart (appears on scroll past fold)

## Layout Structure
```
┌─────────────────────────────────────────────┐
│  BREADCRUMBS                                │
├──────────────────────┬──────────────────────┤
│  PRODUCT GALLERY     │  PRODUCT INFO        │
│  (60% width)         │  - Name, price       │
│  - Hero image        │  - Variant pickers   │
│  - Thumbnail strip   │  - Add to cart       │
│                      │  - Description       │
├──────────────────────┴──────────────────────┤
│  REVIEWS (full width, 2-col layout)         │
│  - Rating summary     - Review cards × N    │
├─────────────────────────────────────────────┤
│  RELATED PRODUCTS (horizontal carousel)     │
└─────────────────────────────────────────────┘
```

## Responsive Behavior
- **1024px+**: Two-column layout, gallery occupies left 60%, thumbnails vertical on left edge, sticky product info on right
- **768–1023px**: Gallery stacks above product info, thumbnails become horizontal strip below hero
- **<768px**: Single column, gallery becomes swipeable carousel with dot indicators, sticky add-to-cart bar appears at bottom, related products 2-across grid

## State Descriptions
- **Loading**: Gallery skeleton (gray placeholder with shimmer), product info skeleton (text lines), review skeleton cards (3× gray cards)
- **Empty reviews**: "Be the first to review" CTA with star-rating prompt
- **Variant unavailable**: Option rendered as disabled with strikethrough label; tooltip "Out of stock"
- **Add to cart success**: Button text changes to "✓ Added", mini-cart icon shows count badge (animated), toast appears bottom-left
- **Add to cart error**: Button reverts, inline error message below button ("Could not add to cart. Please try again.")
- **Image zoom**: Fullscreen modal overlay, cursor follows zoom region, Escape or click-outside closes

## Accessibility Requirements
- WCAG 2.2 AA compliance throughout
- Gallery: thumbnails navigable by keyboard (arrow keys), alt text on all product images, zoom modal traps focus
- Variant selectors: `<fieldset>` + `<legend>` for each option group, radio-button semantics, sr-only "selected" announcement
- Reviews: star ratings include aria-label ("4.2 out of 5 stars"), sort dropdown announces changes via live region
- Add to cart: confirmation announced via `aria-live="polite"` region, cart count badge has `aria-label="3 items in cart"`
- Color swatches: include visible text label + tooltip, not color alone
- Sticky mobile bar: does not obscure content, has sufficient contrast, minimum 48px touch target