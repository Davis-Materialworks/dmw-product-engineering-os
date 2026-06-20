# XD-TO-FLUTTER Migration Playbook

## Purpose
Map XD designs to themed widgets, design tokens, adaptive layouts, semantics, golden tests, and route structure.

## Common Pitfalls
- **Material vs. Cupertino mismatch**: XD designs may follow iOS patterns but get rendered with Material widgets by default. Match the platform expectation — use `ThemeData` with `platform: TargetPlatform.iOS` when the XD artboard targets iOS.
- **Widget rebuild cascades**: XD prototypes show instantaneous state changes, but Flutter's `setState` triggers the entire widget subtree to rebuild. Unmanaged state causes jank and lost scroll position.
- **Layout overflow**: XD artboards have fixed dimensions; Flutter widgets render in dynamic viewports. `Row`/`Column` children overflow silently unless wrapped with `Expanded`, `Flexible`, or `SingleChildScrollView`.
- **Golden test flakiness**: Pixel-perfect golden tests break on every Flutter SDK update due to anti-aliasing changes, font hinting differences, and platform channel mock state. Never use golden tests as the sole verification method.
- **Custom painter overuse**: Complex XD vector art tempts developers to use `CustomPainter` for everything. This bypasses the semantics tree, breaking accessibility and hit-testing. Use standard widgets whenever possible.
- **Hot reload illusion**: Hot reload works for UI changes but not for state initialization changes. XD state variations require full restart to verify correctly.

## Token Translation Rules
| XD Source | Flutter Token | Notes |
|-----------|--------------|-------|
| Fill color (hex) | `Color(0xFFRRGGBB)` or `Theme.of(context).colorScheme` | Always prefer theme tokens over hard-coded colors |
| Text color (hex) | `TextStyle(color: Color(0xFF...))` | Use `DefaultTextStyle` for inherited text colors |
| Font family | `TextStyle(fontFamily: 'CustomFont')` | Declare in `pubspec.yaml` under `fonts:`; use `GoogleFonts` package for web fonts |
| Font size (pt) | `TextStyle(fontSize: N)` | Respect `MediaQuery.textScaleFactor` for accessibility |
| Font weight | `FontWeight.w{N}` | Map XD weight name to numeric: Thin(100)→w100, Regular(400)→w400, Bold(700)→w700 |
| Spacing (px) | `EdgeInsets.all(N)` or `SizedBox(width/height: N)` | Use `const` constructors for static spacing |
| Border radius (px) | `BorderRadius.circular(N)` | Continuous corners if XD uses iOS-style smooth corners |
| Shadow | `BoxShadow(color, blurRadius, offset, spreadRadius)` | Spread available in Flutter, unlike React Native |
| Opacity | `Opacity(opacity: 0.N)` widget or `Color.withOpacity(0.N)` | `Color.withOpacity` is cheaper; `Opacity` widget triggers repaint |

## Component Mapping Guidelines
- **XD Repeat Grid** → `ListView.builder` with `itemBuilder` and `itemCount`; use `ListView.separated` if dividers exist
- **XD Component (Master)** → `StatelessWidget` + constructor params; master→instance overrides become named parameters with defaults
- **XD Artboard** → `Scaffold` or full-screen `Widget`; route via `Navigator.push` or `GoRouter`
- **XD Tab Bar (iOS style)** → `CupertinoTabScaffold` + `CupertinoTabBar`; Android → `BottomNavigationBar`
- **XD Hover/Press State** → `StatefulWidget` with `_isHovered`/`_isPressed` booleans, or `InkWell` with `splashColor`
- **XD Auto-Animate** → `AnimatedContainer`, `AnimatedOpacity`, `Hero` for shared-element transitions, or `AnimationController` for custom timelines
- **XD Overlay/Modal** → `showDialog` (Material) or `showCupertinoModalPopup` (iOS); `showBottomSheet` for bottom sheets

## Migration Checklist
1. [ ] Identify target platform from XD artboard context (iOS, Android, or both)
2. [ ] Define `ThemeData` with brand colors, typography, and spacing extracted from XD tokens
3. [ ] Create `pubspec.yaml` with all required dependencies and font declarations
4. [ ] Build widget tree from XD layer hierarchy: outermost artboard → Scaffold → Column/Row → children
5. [ ] Wrap every `Row`/`Column` child that could overflow in `Expanded` or `Flexible`
6. [ ] Add `Semantics` widget to every interactive element with `label`, `hint`, and `value`
7. [ ] Export XD raster assets at @2x and @3x; declare in `pubspec.yaml` under `assets:`
8. [ ] Implement named routes (`GoRouter` or `Navigator 2.0`) matching XD artboard link structure
9. [ ] Add `MediaQuery`-aware layout breakpoints for tablet/desktop if XD includes them
10. [ ] Configure golden tests with `matchesGoldenFile` for critical screens (use with caution)

## Verification Checklist
- [ ] `flutter analyze` returns zero issues
- [ ] `flutter test` passes all unit and widget tests
- [ ] Golden tests pass on canonical CI runner (same OS, same Flutter SDK version)
- [ ] Accessibility audit via `SemanticsDebugger` — all interactive elements have labels
- [ ] Text scaling test: `MediaQuery(textScaleFactor: 2.0)` — no overflow
- [ ] `flutter build` succeeds for all target platforms (iOS, Android, web if applicable)
- [ ] Performance: no "UI thread exceeded budget" warnings in profile mode