# XD-TO-SWIFTUI Migration Playbook

## Purpose
Map XD screens to SwiftUI views, environment values, dynamic type, accessibility modifiers, navigation stacks, and matched geometry where justified.

## Common Pitfalls
- **Dynamic Type destruction**: XD text layers with fixed frame heights truncate or clip when users enable larger accessibility text sizes. SwiftUI's `Text` grows by default — wrapping it in `.frame(height:)` disables this.
- **Navigation regression**: XD artboards linked linearly map to `NavigationStack` + `NavigationLink`, but SwiftUI's navigation is declarative and path-based. Imperative push/pop from XD prototypes must become `NavigationPath` or enum-based routing.
- **Matched geometry abuse**: `matchedGeometryEffect` is tempting for XD auto-animate transitions, but it breaks when source and destination are in different `NavigationStack` levels. Reserve for same-namespace transitions only.
- **SF Symbols mismatch**: XD icon layers exported as PNG lose the adaptive coloring and weight variants of SF Symbols. Always prefer `Image(systemName:)` over raster icons when the XD design uses Apple's icon set.
- **Color space drift**: XD uses sRGB; SwiftUI renders in Display P3 on supported devices. Colors specified as hex in XD will look subtly different on P3 screens unless defined in Asset Catalog with `Color Space: Display P3`.
- **Environment dependency blindness**: XD artboards show a single visual state, but SwiftUI views respond to `colorScheme`, `sizeCategory`, `layoutDirection`, and `horizontalSizeClass`. A single XD artboard covers none of these.

## Token Translation Rules
| XD Source | SwiftUI Token | Notes |
|-----------|--------------|-------|
| Fill color (hex) | `Color(hex: "#RRGGBB")` or `Color("BrandColor")` | Prefer Asset Catalog named colors for dark/light variant support |
| Text color | `.foregroundColor(.primary)` or `.foregroundColor(Color("TextColor"))` | Semantic colors (`primary`, `secondary`) adapt to dark mode automatically |
| Font family | `.font(.custom("FamilyName", size: N))` | Use `.font(.title)`, `.font(.body)`, etc. for dynamic type support |
| Font weight | `.fontWeight(.bold)` or `.font(.system(size: N, weight: .bold))` | System font weights map cleanly: Light→`.light`, Regular→`.regular`, Semibold→`.semibold`, Bold→`.bold` |
| Line height | `.lineSpacing(N)` | Not an exact match; SwiftUI uses line spacing (extra space between lines), not total line height |
| Spacing (px) | `.padding(N)` or `Spacer().frame(width/height: N)` | Use `VStack(spacing: N)` / `HStack(spacing: N)` for inter-element spacing |
| Border radius (px) | `.cornerRadius(N)` or `.clipShape(RoundedRectangle(cornerRadius: N))` | iOS 17+: `.clipShape(.rect(cornerRadius: N))` supports continuous corners |
| Shadow | `.shadow(color:radius:x:y:)` | No spread equivalent; use multiple shadows or overlay for complex effects |
| Opacity | `.opacity(N)` | Values 0.0-1.0; prefers-reduced-transparency respected automatically |

## Component Mapping Guidelines
- **XD Repeat Grid** → `List` or `LazyVStack` inside `ScrollView` with `ForEach(identifiable:)`; use `List` for platform-consistent rows
- **XD Component (Master)** → `View` struct with `@State`/`@Binding` properties; master→instance overrides → `init` parameters with defaults
- **XD Tab Bar** → `TabView` with `selection` binding; use `Label` for title + icon pairing
- **XD Navigation (artboard links)** → `NavigationStack` with `NavigationLink(value:)` and `.navigationDestination(for:)`
- **XD Hover/Press State** → `.onHover { }` + `.scaleEffect`; `ButtonStyle` custom protocol for press effects
- **XD Auto-Animate** → `withAnimation { }` + `.matchedGeometryEffect(id:in:)` for shared elements; `.transition(.opacity)` for disappear/appear
- **XD Modal/Sheet** → `.sheet(isPresented:)`, `.fullScreenCover()`, or `.popover()` depending on XD artboard overlay style
- **XD Scroll Group** → `ScrollView` with `LazyVStack` for virtualized content

## Migration Checklist
1. [ ] Identify iOS version target from XD artboard context (determines available SwiftUI APIs)
2. [ ] Create Asset Catalog with named colors matching XD brand palette; add dark/light variants
3. [ ] Map XD navigation flow to `NavigationStack` with typed `NavigationPath` or enum-based routes
4. [ ] Replace all `.frame(height:)` on text with `.lineLimit()` and `minimumScaleFactor` for dynamic type
5. [ ] Add `.accessibilityLabel()`, `.accessibilityHint()`, and `.accessibilityAddTraits()` to all interactive views
6. [ ] Export XD raster assets at @2x and @3x; add to Asset Catalog with correct scale factors
7. [ ] Replace raster XD icons with SF Symbols where the XD design uses Apple-standard glyphs
8. [ ] Implement `@Environment(\.colorScheme)` responsive styling if XD shows light mode only
9. [ ] Build `#Preview` for every view with sample data; test dark mode, large text, and RTL in previews
10. [ ] Add `.sensoryFeedback()` for haptic feedback if XD interaction mockups indicate it

## Verification Checklist
- [ ] Xcode builds for iOS target with zero errors and zero warnings
- [ ] Accessibility Inspector audit: every interactive element has a label, every image has a description
- [ ] Dynamic Type test (Largest setting): no text clipping, no layout breakage on any screen
- [ ] VoiceOver navigates screens in XD's intended reading order
- [ ] Dark mode renders correctly if implemented; if not, locked to light with `.preferredColorScheme(.light)`
- [ ] XCTest UI tests pass for critical user flows
- [ ] SwiftUI Previews render for all view variants (loading, empty, error, data-present)