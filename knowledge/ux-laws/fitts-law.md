# Fitts's Law

## Principle
The time to acquire a target is a function of the distance to the target and the size of the target. Mathematically: T = a + b × log₂(2D/W), where D is distance from the starting point and W is the target width along the axis of motion. Larger and closer targets are faster to reach.

## How to Detect Violations in XD Artboards
- **Measure touch target sizes**: Any interactive element smaller than 44×44pt (iOS HIG) or 48×48dp (Material Design) on a mobile artboard is a Fitts's Law violation. Measure with XD's ruler tool.
- **Check edge affinity**: Primary actions positioned in the center of the screen (far from thumb zone on mobile) or far from natural cursor position on desktop violate Fitts's Law. The screen edges are "infinitely large" targets — use them.
- **Audit destructive action placement**: "Delete" or "Cancel" buttons placed adjacent to "Save" or "Submit" with equal size violate Fitts's Law because the cost of a mis-click is catastrophic. Destructive actions should be smaller or farther from primary actions.
- **Verify spacing between targets**: If two interactive elements are closer than 8pt on mobile or 4pt on desktop, Fitts's Law is violated because a finger or cursor cannot reliably distinguish them.

## Concrete XD-to-Code Examples
1. **Mobile bottom sheet with tiny close button**: The XD artboard shows a modal with a 16×16pt "X" close button in the top-right corner. For thumb-driven interaction, move the close action to a swipe-down gesture and add a 44pt tall drag handle at the top edge. Code consequence: `GestureDetector` + `onVerticalDragEnd` with threshold instead of a small `GestureDetector` wrapping an icon.
2. **Desktop settings page with "Save" at the top**: The XD artboard places "Save Changes" at the top of a long form. The user's cursor is at the bottom after filling the form. Move "Save" to a sticky bottom bar or add a floating save button that follows scroll. Code consequence: `position: sticky` footer bar or `IntersectionObserver`-triggered floating button.
3. **Two adjacent danger actions**: The XD artboard shows "Archive Project" and "Delete Project" as two equal-sized, adjacent buttons. Increase the distance between them, make "Delete" a text link or outline style, and add a confirmation dialog. Code consequence: distinct `variant="destructive"` styling and an `AlertDialog` confirmation step.

## When to Invoke Fitts's Law in a Design Critique
- Before finalizing any mobile screen — audit all touch targets
- When reviewing forms — ensure submit buttons are in the natural completion zone
- When a design includes dismiss/close/cancel actions that are hard to reach
- During accessibility review — small targets fail WCAG 2.5.5 (Target Size)

## Common False Positives
- **Infinite scroll feeds**: Individual items in a feed can be small because the user scrolls the feed to the target, reducing effective distance to near-zero. The real target is the scroll container, not the items within it.
- **Keyboard-driven interfaces**: If the expected interaction is keyboard navigation (Tab/Enter/Escape), target size is irrelevant. The "target" is the tab order, which has zero visual distance.
- **Context menus**: Right-click menus appear at the cursor location, making all items effectively distance-zero. Small menu items that would otherwise violate Fitts's Law are acceptable when the menu opens at the pointer.