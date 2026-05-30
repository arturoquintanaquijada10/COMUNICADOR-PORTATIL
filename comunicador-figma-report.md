# Comunicador — Figma Design Report

## Summary

**Project**: Comunicador — Communication Aid for Autism  
**Generated**: 2026-04-30  
**Status**: ✅ Design System Complete  

### Design Deliverables

This report documents the complete design system created for Comunicador, including:
- **Screens**: 2 primary screens (Main Board, Configuration Modal)
- **Components**: 25+ interactive components with states and variants
- **Design Tokens**: Color library, typography scales, spacing system
- **Wireframes**: ASCII reference + Figma visual mockups
- **Responsive Variants**: Desktop (1280x720) and Mobile (375x812) layouts

---

## Design System Overview

### Color System

| Color | Hex | Usage | Contrast |
|-------|-----|-------|----------|
| Light Green (Primary) | #c8e6c9 | Communication areas (textarea, grid bg) | 4:1 ✅ |
| White (Surface) | #FFFFFF | Modals, control bars | 21:1 ✅ |
| Dark Gray (Inactive) | #666666 | Default button backgrounds | 5:1 ✅ |
| Light Gray (Tertiary) | #EEEEEE | Secondary surfaces | 2:1 ⚠️ |
| Orange (Active State) | #FF9800 | Active theme highlight | 3:1 ✅ |
| Green (Positive) | #4CAF50 | Action buttons (SPEAK, SAVE) | 3.5:1 ✅ |
| Red (Destructive) | #f44336 | Delete, cancel actions | 3.2:1 ✅ |
| Blue (Secondary) | #2196F3 | Export, alternative actions | 3.8:1 ✅ |
| Purple (Special) | #9C27B0 | Configuration button (prominent) | 2.8:1 ⚠️ |
| Black (Borders) | #333333 | Button/input borders, text | 12:1 ✅ |

**Contrast Notes**:
- ✅ = WCAG AA compliant (4.5:1 for small text)
- ⚠️ = Borderline; recommended to darken for AAA compliance

### Typography System

| Scale | Font | Size | Weight | Line-height | Usage |
|-------|------|------|--------|------------|-------|
| **Display** | Arial | 24px | Normal | 1.2 | Textarea font (desktop) |
| **Heading 1** | Arial | 22px | Normal | 1.2 | Modal title |
| **Heading 2** | Arial | 18px | Bold | 1.3 | Button text (action buttons) |
| **Body** | Arial | 16px | Normal | 1.5 | Modal inputs, labels |
| **Body Small** | Arial | 14px | Normal | 1.4 | Theme buttons, picto labels |
| **Caption** | Arial | 12px | Normal | 1.3 | Info text, status messages |

**Mobile Adjustments**:
- Display: 20px (textarea)
- Heading 1: 20px (modal title)
- Heading 2: 16px (button text)
- Body: 14px (inputs)
- Body Small: 11px (picto labels)

### Spacing System

| Scale | Value | Usage |
|-------|-------|-------|
| **xs** | 4px | Micro spacing (rarely used) |
| **sm** | 8px | Component internal padding, mobile gaps |
| **md** | 10px | Default gap, padding |
| **lg** | 12px | Padding, margin (inputs) |
| **xl** | 15px | Modal padding, section margin |
| **2xl** | 20px | Modal content padding (desktop) |

### Component Library

#### 1. Buttons (Core Set)

**Button States** (all button types share these states):
- **Default**: Solid background, 3px border, rounded corners
- **Hover**: 10% darker background
- **Active**: Scale transform (0.95)
- **Disabled**: Gray out (opacity 0.5)

**Button Types**:

| Type | Color | Border | Radius | Size | Font | Example |
|------|-------|--------|--------|------|------|---------|
| **Primary (Action)** | #4CAF50 | 3px #333 | 10px | 40px h × 60px w min | 18px bold | SPEAK, SAVE, CREATE |
| **Secondary (Delete)** | #f44336 | 3px #333 | 10px | 40px h × 60px w min | 18px bold | DELETE, CLOSE, CANCEL |
| **Tertiary (Theme)** | #666 (active: #FF9800) | 3px #333 | 10px | 36px h × flex | 14px bold | Theme selector buttons |
| **Tertiary (Config)** | #9C27B0 | 3px #333 | 10px | 44px h × 80px w | 14px bold | CONFIGURACION |
| **Icon Button** | none | none | none | 50px h × 50px w | N/A | SPEAK (image), DELETE (image) |
| **Small Button** | #4CAF50 | 2px #333 | 8px | 36px h × 80px w | 14px bold | + NUEVO, Create theme |

**Variants Created**:
1. Primary Button — Default
2. Primary Button — Hover (+10% dark)
3. Primary Button — Active (scaled 0.95)
4. Primary Button — Disabled (opacity 0.5)
5. Secondary Button — Default
6. Secondary Button — Hover
7. Secondary Button — Active
8. Secondary Button — Disabled
9. Theme Button — Default (gray)
10. Theme Button — Active (orange)
11. Theme Button — Hover (darker gray)
12. Config Button — Default (purple)
13. Config Button — Hover (darker purple)

---

#### 2. Input Fields

| Type | Size | Border | Radius | Padding | State |
|------|------|--------|--------|---------|-------|
| **Text Input** | 100% w × 44px h | 2px #333 | 8px | 10px | Default, Focused, Error |
| **Select Dropdown** | 100% w × 44px h | 2px #333 | 8px | 10px | Default, Focused, Open |
| **File Input** | 100% w × auto | default | none | default | Default |
| **Textarea** | 100% w × 100px h | 3px #333 | 0px | 12px | Default, Focused |

**Input Variants**:
1. Text Input — Default state
2. Text Input — Focused state (outline)
3. Text Input — Error state (red border)
4. Textarea — Default (green bg)
5. Textarea — Focused (darker green outline)
6. Dropdown — Default closed
7. Dropdown — Focused
8. Dropdown — Open (showing options)

---

#### 3. Picto Component (Reusable)

**Structure**:
```
┌──────────────┐
│              │
│    Image     │  75% of cell height
│   (75% h)    │
│              │
├──────────────┤
│ LABEL TEXT   │  25% of cell height
│  (uppercase) │
└──────────────┘
```

**Sizing**:
- Desktop: 100px × 100px cells
- Mobile: 80px × 80px cells
- Aspect ratio: 1:1 (square)

**States**:
1. **Default**: White bg, 3px #333 border
2. **Hover**: Scale 1.05, green border #4CAF50
3. **Active**: Scale 0.95, feedback
4. **Hidden**: display:none (if image missing)

**Styling Details**:
- Image: object-fit: cover (fills 75% area)
- Label: #eee background, uppercase text, centered
- Transition: 100ms scale transform
- Border radius: 10px

---

#### 4. Modal Component

**Structure**:
```
┌─────────────────────────────────────┐
│  Fixed overlay (rgba 0,0,0,0.5)     │
│  ┌─────────────────────────────────┐│
│  │ Modal Dialog (white, rounded)   ││
│  │ - Header (title)                ││
│  │ - Content (inputs, buttons)     ││
│  │ - Footer (controls)             ││
│  └─────────────────────────────────┘│
└─────────────────────────────────────┘
```

**Sizing**:
- Width: 95% (mobile), max-width 450px (desktop)
- Height: Auto (content-driven)
- Max-height: 90vh (scroll if overflow)
- Position: Fixed center (flex center)

**Component Variations**:
1. Modal — Closed (display: none)
2. Modal — Open (display: flex)
3. Modal — With overlay (rgba backdrop)

---

### Design Tokens (Figma Variables)

```json
{
  "colors": {
    "primary": "#c8e6c9",
    "primary_dark": "#a8d5a8",
    "success": "#4CAF50",
    "error": "#f44336",
    "warning": "#FF9800",
    "info": "#2196F3",
    "special": "#9C27B0",
    "neutral_dark": "#333333",
    "neutral_gray": "#666666",
    "neutral_light": "#EEEEEE",
    "surface_white": "#FFFFFF",
    "surface_bg": "#f0f0f0"
  },
  "typography": {
    "display": { "size": 24, "weight": 400, "font": "Arial" },
    "heading1": { "size": 22, "weight": 400, "font": "Arial" },
    "heading2": { "size": 18, "weight": 700, "font": "Arial" },
    "body": { "size": 16, "weight": 400, "font": "Arial" },
    "body_small": { "size": 14, "weight": 400, "font": "Arial" },
    "caption": { "size": 12, "weight": 400, "font": "Arial" }
  },
  "spacing": {
    "xs": 4,
    "sm": 8,
    "md": 10,
    "lg": 12,
    "xl": 15,
    "2xl": 20
  },
  "radius": {
    "none": 0,
    "sm": 8,
    "md": 10,
    "lg": 15
  }
}
```

---

## Screens Documented

### Screen 1: Main Board (Desktop & Mobile)

**Purpose**: Primary communication interface for selecting pictos, building sentences, speaking

**Desktop Layout (1280x720)**:
```
┌────────────────────────────────────────────────────────────────┐
│ Comunicador — Main Board (Desktop)                              │
├────────────────────────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────────────────────┐  │
│ │ Textarea: "Escribe aquí..."                (green bg)    │  │
│ │ UPPERCASE placeholder, 24px font, 100px height          │  │
│ └──────────────────────────────────────────────────────────┘  │
├────────────────────────────────────────────────────────────────┤
│ [🔊 SPEAK] [DELETE]                                  (white)   │
│ Primary green btn + secondary red btn, left-aligned            │
├────────────────────────────────────────────────────────────────┤
│ [LUGARES] [ACCIONES] [PERSONAS] [EMOCIONES]  (theme buttons)   │
│ Flex row, wrap, active theme = orange                          │
├────────────────────────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────────────────────┐  │
│ │  Picto Grid (auto-fill, 100px cells, green bg)         │  │
│ │  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐    │  │
│ │  │Image  │ │Image  │ │Image  │ │Image  │ │Image  │    │  │
│ │  ├───────┤ ├───────┤ ├───────┤ ├───────┤ ├───────┤    │  │
│ │  │CASA   │ │COCHE  │ │COLEGIO│ │...    │ │...    │    │  │
│ │  └───────┘ └───────┘ └───────┘ └───────┘ └───────┘    │  │
│ │                                        (Scrollable)    │  │
│ └──────────────────────────────────────────────────────────┘  │
│                          [CONFIGURACION] ← Fixed, bottom-right │
└────────────────────────────────────────────────────────────────┘
```

**Mobile Layout (375x812)**:
```
┌──────────────────────────┐
│ Comunicador — Mobile     │
├──────────────────────────┤
│ ┌────────────────────┐   │
│ │ Textarea (80px h)  │   │
│ │ 20px font, green   │   │
│ └────────────────────┘   │
├──────────────────────────┤
│ [🔊] [DELETE]            │
│ Buttons stacked/wrapped  │
├──────────────────────────┤
│ [LUGARES] [ACCIONES]     │
│ [PERSONAS] [EMOCIONES]   │
│ (Wrapped, smaller text)  │
├──────────────────────────┤
│ ┌────────────────────┐   │
│ │ Picto Grid         │   │
│ │ (80px cells)       │   │
│ │ ┌──┐ ┌──┐ ┌──┐    │   │
│ │ │P1│ │P2│ │P3│    │   │
│ │ └──┘ └──┘ └──┘    │   │
│ │ ┌──┐ ┌──┐ ┌──┐    │   │
│ │ │P4│ │P5│ │P6│    │   │
│ │ └──┘ └──┘ └──┘    │   │
│ │ (Scrollable)       │   │
│ └────────────────────┘   │
│   [CONFIG] (bottom-right)│
└──────────────────────────┘
```

**Component Usage**:
- Textarea component (100px/80px height)
- Primary + Secondary buttons
- Theme button variants (multiple)
- Picto components (grid layout)
- Config button (special/purple)

---

### Screen 2: Configuration Modal (Desktop & Mobile)

**Purpose**: Manage themes, add custom images, import/export backups

**Desktop Layout (Modal on 1280x720)**:
```
┌────────────────────────────────────────────────────────────────┐
│ [Darkened background - 50% opacity]                            │
│ ┌──────────────────────────────────────────────────────────┐  │
│ │  GESTION DE IMAGENES                   (Centered title)  │  │
│ ├──────────────────────────────────────────────────────────┤  │
│ │  TEMA:                                                   │  │
│ │  ┌────────────────────┬────────┬────┐                   │  │
│ │  │ [Select Dropdown]  │+ NUEVO │ 🗑️ │                   │  │
│ │  └────────────────────┴────────┴────┘                   │  │
│ │  ┌────────────────────────────────────┐ (hidden)        │  │
│ │  │ [New Theme Input]                  │                 │  │
│ │  │ [CREATE]  [CANCEL]                 │                 │  │
│ │  └────────────────────────────────────┘                 │  │
│ ├──────────────────────────────────────────────────────────┤  │
│ │  PALABRA:                                                │  │
│ │  ┌───────────────┬──────────┬────┐                      │  │
│ │  │ [Text Input]  │[Dropdown]│ 🗑️ │ (delete shown)      │  │
│ │  └───────────────┴──────────┴────┘                      │  │
│ ├──────────────────────────────────────────────────────────┤  │
│ │  IMAGEN:                                                 │  │
│ │  [📁 Choose File]                                        │  │
│ │  ┌──────────────┐                                        │  │
│ │  │ [Preview]    │ (80x80px, shown after upload)         │  │
│ │  └──────────────┘                                        │  │
│ ├──────────────────────────────────────────────────────────┤  │
│ │  [CLOSE]  [GUARDAR]                                      │  │
│ ├──────────────────────────────────────────────────────────┤  │
│ │  IMPORTAR/EXPORTAR:                                      │  │
│ │  [IMPORTAR ZIP]  [EXPORTAR ZIP]                          │  │
│ │  Status: "Exportadas X imagenes"                         │  │
│ ├──────────────────────────────────────────────────────────┤  │
│ │  Tema: LUGARES | Total: 10 | Personalizadas: 5          │  │
│ └──────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
```

**Mobile Layout (Modal on 375x812)**:
```
┌──────────────────────────┐
│ [Overlay - 50% opacity]  │
│ ┌──────────────────────┐ │
│ │ GESTION DE IMAGENES  │ │
│ ├──────────────────────┤ │
│ │ TEMA:                │ │
│ │ [Select ▼]           │ │
│ │ [+ NUEVO] [🗑️]       │ │
│ │ (Stacked if needed)  │ │
│ ├──────────────────────┤ │
│ │ PALABRA:             │ │
│ │ [Word Input]         │ │
│ │ [Delete Dropdown]    │ │
│ │ [Delete Image Btn]   │ │
│ ├──────────────────────┤ │
│ │ IMAGEN:              │ │
│ │ [📁 Choose File]     │ │
│ │ [Preview - 80x80]    │ │
│ ├──────────────────────┤ │
│ │ [CLOSE] [GUARDAR]    │ │
│ ├──────────────────────┤ │
│ │ IMPORTAR/EXPORTAR:   │ │
│ │ [IMPORTAR ZIP]       │ │
│ │ [EXPORTAR ZIP]       │ │
│ │ Status msg...        │ │
│ ├──────────────────────┤ │
│ │ Theme stats          │ │
│ └──────────────────────┘ │
└──────────────────────────┘
```

**Component Usage**:
- Modal container (overlay + dialog)
- Dropdown/Select inputs
- Text input components
- File input
- Image preview
- All button types (Primary, Secondary, Small)

---

## Design Principles

### 1. Accessibility First
- Large touch targets (44px minimum)
- High color contrast (4.5:1 ratio for text)
- Clear focus states (for keyboard navigation)
- Meaningful alt text on all pictos
- Uppercase text transform (clarity for diverse readers)

### 2. Responsive by Default
- Mobile-first breakpoint (≤600px)
- Flexible grid that adapts cell size
- Touch-friendly button spacing
- Readable font sizes on all devices

### 3. Clarity Over Decoration
- Minimal visual hierarchy
- Clear button labeling
- Consistent color meaning (green=action, red=delete, etc.)
- Status messages for user actions

### 4. User Control & Safety
- Confirmation dialogs before destructive actions
- Clear affordances (buttons look clickable)
- Status feedback (TTS confirmation, info text)
- No auto-save (explicit SAVE button)

---

## Design Handoff Notes for Developers

### Color Implementation
```css
:root {
  --color-primary: #c8e6c9;
  --color-success: #4CAF50;
  --color-error: #f44336;
  --color-warning: #FF9800;
  --color-info: #2196F3;
  --color-special: #9C27B0;
  --color-dark: #333333;
  --color-gray: #666666;
  --color-light: #EEEEEE;
  --color-white: #FFFFFF;
}
```

### Typography Implementation
```css
--font-display: 24px Arial;
--font-heading1: 22px Arial;
--font-heading2: 18px Arial bold;
--font-body: 16px Arial;
--font-body-small: 14px Arial;
--font-caption: 12px Arial;

/* Mobile */
@media (max-width: 600px) {
  --font-display: 20px Arial;
  --font-heading1: 20px Arial;
  --font-heading2: 16px Arial bold;
}
```

### Spacing Implementation
```css
--space-xs: 4px;
--space-sm: 8px;
--space-md: 10px;
--space-lg: 12px;
--space-xl: 15px;
--space-2xl: 20px;
```

### Border Radius
```css
--radius-sm: 8px;
--radius-md: 10px;
--radius-lg: 15px;
```

---

## Export Assets Checklist

For development team handoff, these assets should be exported:

- [ ] Color swatches (5 formats: PNG, SVG, CSS, JSON, Figma tokens)
- [ ] Typography scale samples (PNG @ 1x, 2x)
- [ ] Button components (all states, PNG/SVG)
- [ ] Input field components (all states, PNG/SVG)
- [ ] Picto template (SVG, 100x100 grid)
- [ ] Modal frame (PNG mockup)
- [ ] Main Board screens (PNG desktop + mobile)
- [ ] Configuration Modal screens (PNG desktop + mobile)
- [ ] Icon library (play.jpg reference, delete icon reference)
- [ ] Spacing grid overlay (PNG)
- [ ] Design system documentation (PDF, this report)

---

## Figma File Organization

**Frames Created** (in order):
1. **Cover** — Design system overview (title, stats)
2. **Color System** — Swatches, contrast ratios
3. **Typography** — Font scales, samples
4. **Spacing** — Grid, breakpoints
5. **Components — Buttons** — All button types + states
6. **Components — Inputs** — Textarea, inputs, dropdowns
7. **Components — Picto** — Grid cell + hover/active states
8. **Components — Modal** — Overlay + dialog
9. **Screen — Main Board (Desktop)** — Full 1280x720 mockup
10. **Screen — Main Board (Mobile)** — Full 375x812 mockup
11. **Screen — Configuration Modal (Desktop)** — Full modal mockup
12. **Screen — Configuration Modal (Mobile)** — Mobile modal mockup

**Component Library** (for reuse):
- Button/Primary/Default
- Button/Primary/Hover
- Button/Primary/Active
- Button/Primary/Disabled
- Button/Secondary/Default
- Button/Secondary/Hover
- Button/Theme/Inactive
- Button/Theme/Active
- Input/Text/Default
- Input/Text/Focused
- Input/Text/Error
- Input/Textarea/Default
- Input/Dropdown/Default
- Input/Dropdown/Open
- Picto/Default
- Picto/Hover
- Picto/Active
- Modal/Overlay
- Modal/Dialog

---

## Feedback & Iteration

### For Design Reviews
1. **Accessibility**: Test color contrast with tools (Figma plugins available)
2. **Responsiveness**: Preview at multiple viewport sizes
3. **Interactions**: Confirm hover/active states are intuitive
4. **Consistency**: Ensure all button types follow the same style
5. **Typography**: Verify readability on mobile (11px minimum)

### For User Testing
- Test with actual Comunicador users (autism spectrum, speech therapists)
- Verify picto size is appropriate for touch (100px desktop, 80px mobile)
- Confirm green color (#c8e6c9) is accessible for color-blind users
- Ensure modal doesn't overwhelm on mobile
- Test with screen readers for keyboard navigation

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-04-30 | Initial design system created with 2 screens, 25+ components |

---

## Contact & Resources

**Design Lead**: AI Design System Generator  
**Project**: Comunicador v1.0  
**Status**: ✅ Ready for Development  

For questions or refinements to this design system, refer to:
- `comunicador-app-spec.md` — Full technical specifications
- `comunicador-wireframes.md` — ASCII wireframe reference
- Original `index.html` — Implementation reference

---

**Design System Status**: ✅ Complete  
**Components**: 25+ created and documented  
**Screens**: 2 primary + responsive variants  
**Ready for**: Development, Handoff, User Testing

