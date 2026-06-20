# XD-TO-REACT-NATIVE Migration Playbook

## Purpose
Map XD mobile artboards to screens, navigation stacks, safe-area layouts, gestures, native accessibility labels, dynamic type, and platform conventions.

## Common Pitfalls
- **Safe area blindness**: XD artboards show edge-to-edge layouts that collide with device notches, status bars, and home indicators on real devices. Every full-bleed artboard needs `SafeAreaView` wrapping.
- **Navigation stack assumptions**: XD prototypes often use artboard-to-artboard links that do not map 1:1 to React Navigation stacks. Nested stacks, tab navigators, and modals must be explicitly modeled.
- **Gesture conflicts**: XD tap targets bleed into swipe zones (e.g., list items inside a swipeable row). On device, these gestures compete — priority must be assigned.
- **Dynamic type breakage**: XD text layers with fixed bounding boxes overflow when the user's accessibility font size is larger than the design assumption. All text must use `allowFontScaling` or flexible containers.
- **Platform divergence**: XD artboards designed at a single size look different on iOS vs. Android due to different system fonts, navigation patterns, and default spacings. A single artboard cannot serve both platforms.
- **Shadow/elevation mismatch**: XD drop shadows do not translate to Android elevation or iOS shadow properties — each platform requires separate shadow styling.

## Token Translation Rules
| XD Source | React Native Token | Notes |
|-----------|-------------------|-------|
| Fill color (hex) | `StyleSheet.create({ backgroundColor: '#hex' })` | Use `PlatformColor()` or `DynamicColorIOS()` for platform-specific colors |
| Text color (hex) | `StyleSheet.create({ color: '#hex' })` | Respect dark mode via `useColorScheme()` or `Appearance` API |
| Font family | `fontFamily: 'System'` (default) | iOS: San Francisco, Android: Roboto; custom fonts need `react-native.config.js` linking |
| Font size (pt) | `fontSize: N` | Do not hard-code; use `PixelRatio.getFontScale()` or `useWindowDimensions()` for scaling |
| Spacing (px) | `margin/padding: N` | Use theme-based spacing constants; 8px grid preferred |
| Border radius (px) | `borderRadius: N` | Valid range; no issue with direct px mapping |
| Shadow (XD blur/spread) | iOS: `shadowColor/Offset/Opacity/Radius`, Android: `elevation: N` | Dual-style required; Android elevation is 0-24 integer only |
| Opacity | `opacity: 0.N` | Valid; note that `opacity` affects the entire subtree, including text |

## Component Mapping Guidelines
- **XD Repeat Grid** → `FlatList` with `keyExtractor` and `renderItem`; `SectionList` if grouped
- **XD Scroll Group** → `ScrollView` with `contentContainerStyle`; prefer `FlatList` for long lists
- **XD Tab Bar** → Bottom Tab Navigator (`@react-navigation/bottom-tabs`) or custom `TabBar`
- **XD Modal/Overlay** → `Modal` component with `transparent={true}` and `animationType="slide"`
- **XD Swipe Gesture** → `PanResponder` or `react-native-gesture-handler`'s `Swipeable`
- **XD Input Field** → `TextInput` with `keyboardType`, `autoComplete`, and `returnKeyType` set
- **XD Component (Master)** → Custom component with `Props` type; instance overrides → optional props with defaults

## Migration Checklist
1. [ ] Identify device size from XD artboard (iPhone 14/15, Pixel, etc.) and set as primary target
2. [ ] Wrap every screen root in `<SafeAreaView>` with appropriate `edges` prop
3. [ ] Define navigation structure: Stack, Tab, Drawer, or nested — match XD artboard links
4. [ ] Audit all XD text layers for dynamic type compatibility — remove fixed height constraints
5. [ ] Extract colors into a shared theme object; add dark mode variants if XD specifies them
6. [ ] Map XD tap targets to `TouchableOpacity`/`Pressable` with minimum 44x44pt hit area
7. [ ] Export XD assets at @2x and @3x; place in appropriate iOS/Android asset directories
8. [ ] Implement `accessibilityLabel`, `accessibilityRole`, and `accessibilityHint` on every interactive element
9. [ ] Test `useWindowDimensions()` hook for responsive layouts across device sizes
10. [ ] Add `KeyboardAvoidingView` for screens with input fields positioned low on the artboard

## Verification Checklist
- [ ] Build runs on both iOS simulator and Android emulator with zero red-screen errors
- [ ] Safe area audit: no content hidden behind notch, status bar, or home indicator
- [ ] Accessibility Inspector (iOS) / TalkBack (Android) navigates all interactive elements in order
- [ ] Device font size set to largest — no text clipping or overflow
- [ ] Offline/error/empty states render correctly (XD may not show these — implement them)
- [ ] Gesture handlers do not conflict with scroll views or parent navigators
- [ ] `npx react-native-doctor` reports zero warnings