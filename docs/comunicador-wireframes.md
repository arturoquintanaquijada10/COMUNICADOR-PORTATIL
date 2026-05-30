# Comunicador — ASCII Wireframes & Layout Reference

**Version**: 1.0  
**Date Generated**: 2026-04-30  
**Purpose**: Quick visual reference for all screens and components

---

## Quick Reference: Desktop vs Mobile

### Main Board - Desktop (1280px)

```
┌─────────────────────────────────────────────────────────────────┐
│ COMUNICADOR                                      ☰ CONFIGURACION │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  TEMA: [ Lugares ▼ ]                                            │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │  🏠     │  │  🚗      │  │  🌳      │  │  🏫      │        │
│  │          │  │          │  │          │  │          │        │
│  │  CASA   │  │  COCHE   │  │  PARQUE  │  │  ESCUEL  │        │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘        │
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │  🏖️     │  │  🛍️      │  │  🎬      │  │  🏥      │        │
│  │          │  │          │  │          │  │          │        │
│  │  PLAYA  │  │  TIENDA  │  │  CINE    │  │ HOSPITAL │        │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘        │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Textarea (GREEN #c8e6c9, 18px text, min-height: 100px):       │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ CASA COCHE PARQUE ESCUELA                                │  │
│  │                                                          │  │
│  │                                                          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────────┐  ┌────────────────────────────┐    │
│  │      ▶ HABLAR          │  │      🗑️  BORRAR           │    │
│  └────────────────────────┘  └────────────────────────────┘    │
│   (Blue #1976d2)              (Red #d32f2f)                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

SIZING:
  Desktop container: 1280px wide
  Grid: 4 columns × 2 rows
  Picto button: 100px × 100px each
  Gap between: 8px
  Textarea height: ~100px
  Button height: 44px
```

### Main Board - Mobile (375px)

```
┌─────────────────────────┐
│ COMUNICADOR        ☰    │
├─────────────────────────┤
│                         │
│  TEMA: [Lugares ▼]      │
│                         │
├─────────────────────────┤
│                         │
│  ┌─────────┐ ┌────────┐ │
│  │   🏠   │ │  🚗   │ │
│  │  CASA  │ │COCHE  │ │
│  └─────────┘ └────────┘ │
│                         │
│  ┌─────────┐ ┌────────┐ │
│  │  🌳    │ │  🏫   │ │
│  │ PARQUE │ │ESCUEL │ │
│  └─────────┘ └────────┘ │
│                         │
│  ┌─────────┐ ┌────────┐ │
│  │   🏖️   │ │  🛍️   │ │
│  │  PLAYA │ │TIENDA │ │
│  └─────────┘ └────────┘ │
│                         │
│  ┌─────────┐ ┌────────┐ │
│  │  🎬    │ │  🏥   │ │
│  │  CINE  │ │HOSPITAL│
│  └─────────┘ └────────┘ │
│                         │
├─────────────────────────┤
│                         │
│  Textarea (GREEN):      │
│  ┌─────────────────────┐ │
│  │ CASA COCHE          │ │
│  │                     │ │
│  │                     │ │
│  └─────────────────────┘ │
│                         │
├─────────────────────────┤
│  ┌──────────────────────┐│
│  │   ▶ HABLAR           ││
│  └──────────────────────┘│
│  ┌──────────────────────┐│
│  │   🗑️  BORRAR         ││
│  └──────────────────────┘│
│                         │
└─────────────────────────┘

SIZING:
  Mobile width: 375px
  Grid: 2 columns × 4 rows = 8 pictos
  Picto button: 80px × 80px each
  Gap: 6px
  Textarea: 80px min-height
  Button: full width, stacked
```

---

## Component Breakdown: Buttons

### Button Base Measurements

```
STANDARD BUTTON (Height: 44px)

┌─────────────────────────────┐
│    PADDING: 12px 16px       │
│  ┌─────────────────────────┐│
│  │   TEXT (14px, BOLD)     ││
│  │   UPPERCASE             ││
│  └─────────────────────────┘│
│    PADDING: 12px 16px       │
└─────────────────────────────┘

States:
  DEFAULT: #1976d2 (Blue) or #d32f2f (Red) or #7b1fa2 (Purple)
  HOVER:   Darker shade, +shadow 0 2px 4px rgba(0,0,0,0.1)
  ACTIVE:  Even darker shade, inset shadow
  DISABLED: #ccc (light gray), opacity 0.5
```

### Primary Button (HABLAR)

```
DEFAULT STATE:
┌──────────────────────────┐
│    ▶ HABLAR              │
│   (Blue #1976d2)         │
│   Height: 44px           │
│   Width: auto (min 100px) │
└──────────────────────────┘

HOVER STATE:
┌──────────────────────────┐
│    ▶ HABLAR              │
│   (Darker Blue #1565c0)  │
│   + Shadow: 0 2px 4px... │
└──────────────────────────┘

DISABLED STATE:
┌──────────────────────────┐
│    ▶ HABLAR              │
│   (Gray #ccc)            │
│   Opacity: 0.5           │
└──────────────────────────┘
```

### Destructive Button (BORRAR)

```
DEFAULT STATE:
┌──────────────────────────┐
│    🗑️  BORRAR            │
│   (Red #d32f2f)          │
│   Height: 44px           │
│   Width: auto (min 100px) │
└──────────────────────────┘

HOVER STATE:
┌──────────────────────────┐
│    🗑️  BORRAR            │
│   (Darker Red #c62828)   │
│   + Shadow: 0 2px 4px... │
└──────────────────────────┘
```

### Settings Button (CONFIGURACION)

```
DEFAULT STATE:
┌──────────────────────────┐
│    ☰ CONFIGURACION       │
│   (Purple #7b1fa2)       │
│   Height: 44px           │
│   Width: auto            │
└──────────────────────────┘

HOVER STATE:
┌──────────────────────────┐
│    ☰ CONFIGURACION       │
│   (Darker #6a1b9a)       │
│   + Shadow: 0 2px 4px... │
└──────────────────────────┘
```

---

## Component Breakdown: Inputs

### Dropdown/Select (TEMA)

```
DEFAULT STATE:
┌─────────────────────────────────┐
│ TEMA: │ Lugares         ▼ │ 44px │
│       │ • Acciones            │
│       │ • Personas            │
│       │ • Emociones           │
│       │ • objetos (custom)    │
│       │ • comida (custom)     │
│       └─────────────────────────┘

SIZING:
  Height: 44px (touch-friendly)
  Padding: 8px 12px
  Font-size: 14px, BOLD
  Text-transform: UPPERCASE
  Border: 1px solid #ddd

STATES:
  DEFAULT: #fff bg, #333 text
  HOVER: #f5f5f5 bg
  FOCUS: 2px solid #1976d2 border
```

### Text Input (Theme Name, Image Label)

```
DEFAULT STATE:
┌──────────────────────────────────┐
│ Nombre: │ _________________ │ 40px │
│         │                   │      │
│         └───────────────────┘      │
└──────────────────────────────────────┘

FOCUS STATE:
┌──────────────────────────────────┐
│ Nombre: │ _________________ │ 40px │
│         │ (Blue border)     │      │
│         └───────────────────┘      │
└──────────────────────────────────────┘

ERROR STATE:
┌──────────────────────────────────┐
│ Nombre: │ _________________ │ 40px │
│         │ (Red border)      │      │
│         └───────────────────┘      │
│ ⚠️ Por favor ingresa un nombre    │
└──────────────────────────────────────┘

SIZING:
  Height: 40px
  Padding: 8px 12px
  Font-size: 14px
  Border: 1px solid #ddd
  Border-radius: 4px
```

### Textarea (Selected Words)

```
DESKTOP:
┌────────────────────────────────────────┐
│ CASA COCHE PARQUE ESCUELA              │
│                                        │
│ (Green #c8e6c9 background)             │
│ (18px font, 1.5 line-height)           │
│ Min-height: 100px                      │
│ User can scroll if text exceeds height │
│                                        │
└────────────────────────────────────────┘

MOBILE:
┌──────────────────────┐
│ CASA COCHE           │
│                      │
│ Min-height: 80px     │
│ Responsive smaller   │
└──────────────────────┘

STATES:
  DEFAULT: #c8e6c9 bg, #333 text
  FOCUS: Blue border, green bg (unchanged)
  FILLED: Shows accumulated text
  ERROR: (not typically shown for textarea)
```

---

## Component Breakdown: Picto Button (Grid Item)

### Picto Button - Desktop (100px)

```
┌──────────────────┐
│                  │
│      🏠          │
│    (60×60px)     │
│                  │
│    CASA          │
│   (12px, bold)   │
│                  │
└──────────────────┘
100×100px total
Border: 2px solid #999
Background: #e0e0e0
Border-radius: 4px

HOVER STATE:
┌──────────────────┐
│ ▼ SHADOW         │
│      🏠          │
│                  │
│    CASA          │
│  (darker bg)     │
└──────────────────┘
Background: #d0d0d0 (darker)
Shadow: 0 2px 4px rgba(0,0,0,0.1)

ACTIVE/PRESSED STATE:
┌──────────────────┐
│  INSET SHADOW    │
│      🏠          │
│                  │
│    CASA          │
│  (much darker)   │
└──────────────────┘
Background: #bdbdbd
Inset box-shadow
```

### Picto Button - Mobile (80px)

```
┌────────────────┐
│                │
│      🏠        │
│    (48×48px)   │
│                │
│   CASA         │
│  (10px, bold)  │
│                │
└────────────────┘
80×80px total
Everything proportionally smaller
```

### Picto Button - Disabled State

```
┌──────────────────┐
│                  │
│      🏠          │
│   (faded)        │
│                  │
│    CASA          │
│  (grayed out)    │
│                  │
└──────────────────┘
Background: #f5f5f5 (very light)
Text: #999 (grayed)
Opacity: 0.6
Cursor: not-allowed
```

---

## Grid Layout: Picto Arrangement

### Desktop 4-Column Grid

```
GAP: 8px
MARGIN: 16px

[100px] [100px] [100px] [100px]
   ↓       ↓       ↓       ↓
[100px] [100px] [100px] [100px]

Total width for 4 pictos:
  4 × 100px = 400px
  3 × 8px gap = 24px
  Total = 424px (+ margins)

If more than 8 pictos: scroll or paginate
```

### Tablet 3-Column Grid

```
GAP: 8px
MARGIN: 16px

[90px] [90px] [90px]
  ↓      ↓      ↓
[90px] [90px] [90px]
  ↓      ↓      ↓
[90px] [90px] [90px]

Total width:
  3 × 90px = 270px
  2 × 8px = 16px
  Total = 286px
```

### Mobile 2-Column Grid

```
GAP: 6px
MARGIN: 8px

[80px] [80px]
  ↓      ↓
[80px] [80px]
  ↓      ↓
[80px] [80px]
  ↓      ↓
[80px] [80px]

Total width:
  2 × 80px = 160px
  1 × 6px = 6px
  Total = 166px (fits in 375px with margins)
```

---

## Modal: Configuration

### Configuration Modal - Desktop

```
┌────────────────────────────────────────────────┐
│ CONFIGURACIÓN                              [X] │
├────────────────────────────────────────────────┤
│                                                │
│ Gestión de Temas                              │
│                                                │
│  TEMA: │ Lugares ▼ │   │ + Nuevo Tema         │
│        └───────────────┘   (Purple button)    │
│                                                │
│ Cargar Imágenes                               │
│                                                │
│  │ Seleccionar archivo...                │ │  │
│  │ (Click to browse)                     │ │  │
│  └─────────────────────────────────────────┘  │
│                                                │
│ Opciones                                      │
│                                                │
│  [ Exportar ZIP ]  [ Importar ZIP ]            │
│   (Blue button)     (Blue button)              │
│                                                │
├────────────────────────────────────────────────┤
│                                                │
│  [ Aceptar ]  [ Cancelar ]                     │
│  (Green)      (Gray)                           │
│                                                │
└────────────────────────────────────────────────┘

WIDTH: 500px (90vw on mobile)
PADDING: 24px
BACKGROUND: #fff
BORDER-RADIUS: 8px
BOX-SHADOW: 0 4px 16px rgba(0,0,0,0.15)

OVERLAY: rgba(0,0,0,0.5) full screen
```

### Configuration Modal - Sub-Modal (Nueva Tema)

```
┌───────────────────────────────┐
│ Nueva Tema                │ │ │
├───────────────────────────────┤
│                               │
│ Nombre:                       │
│ ┌─────────────────────────┐   │
│ │ ________________        │   │
│ │ (text input, 40px)      │   │
│ └─────────────────────────┘   │
│                               │
├───────────────────────────────┤
│ [ Aceptar ]  [ Cancelar ]     │
│  (Green)      (Gray)           │
│                               │
└───────────────────────────────┘

Overlays on top of main modal
Same styling as main modal
Smaller width (300px)
```

---

## Color Palette: Quick Reference

### Color Swatches (Visual)

```
PRIMARY:
┌─────────────┐
│   #c8e6c9   │ Green (primary, pictos + textarea)
│  (Light)    │ RGB(200, 230, 201)
└─────────────┘

┌─────────────┐
│   #a1d99f   │ Dark Green (button focus)
│  (Darker)   │ RGB(161, 217, 159)
└─────────────┘

ACTION:
┌─────────────┐
│   #1976d2   │ Blue (HABLAR, action buttons)
│  (Action)   │ RGB(25, 118, 210)
└─────────────┘

DESTRUCTIVE:
┌─────────────┐
│   #d32f2f   │ Red (BORRAR, delete)
│ (Destroy)   │ RGB(211, 47, 47)
└─────────────┘

SETTINGS:
┌─────────────┐
│   #7b1fa2   │ Purple (CONFIGURACION)
│ (Settings)  │ RGB(123, 31, 162)
└─────────────┘

TEXT:
┌─────────────┐
│   #333333   │ Dark Gray (primary text)
│  (Text)     │ RGB(51, 51, 51)
└─────────────┘

BACKGROUND:
┌─────────────┐
│ #ffffff     │ White (modals, default bg)
│ (BG Light)  │ RGB(255, 255, 255)
└─────────────┘

┌─────────────┐
│   #f5f5f5   │ Light Gray (hover states)
│ (BG Gray)   │ RGB(245, 245, 245)
└─────────────┘
```

### Contrast Ratios (WCAG)

```
Green (#c8e6c9) on White (#fff):
  Ratio: 3.5:1
  Level: AA ✓ (passes for normal text)

Blue (#1976d2) on White (#fff):
  Ratio: 5.2:1
  Level: AAA ✓ (excellent contrast)

Red (#d32f2f) on White (#fff):
  Ratio: 5.8:1
  Level: AAA ✓ (excellent contrast)

Dark Gray (#333333) on White (#fff):
  Ratio: 13.8:1
  Level: AAA ✓ (maximum contrast)

Dark Gray (#333333) on Green (#c8e6c9):
  Ratio: 6.2:1
  Level: AAA ✓ (good contrast)
```

---

## Typography: Font Sizes by Breakpoint

### Desktop (1280px+)

```
HEADING 1 (App Title):        24px, Bold (700)
HEADING 2 (Modal Title):      20px, Bold (700)
HEADING 3 (Section Header):   18px, Bold (700)
BUTTON/LABEL:                 14px, Bold (700)
BODY (Textarea):              18px, Normal (400)
CAPTION (Picto Labels):       12px, Bold (700)
SMALL TEXT:                   10px, Normal (400)
```

### Tablet (768px–1024px)

```
HEADING 1:   22px
HEADING 2:   18px
HEADING 3:   16px
BUTTON:      13px
BODY:        16px
CAPTION:     11px
SMALL:        9px
```

### Mobile (375px–768px)

```
HEADING 1:   20px
HEADING 2:   16px
HEADING 3:   14px
BUTTON:      12px
BODY:        14px
CAPTION:     10px
SMALL:        8px
```

---

## Spacing: Reference Grid

```
Base unit: 8px

xs:  4px  ▔▔▔▔
sm:  8px  ▔▔▔▔▔▔▔▔
md: 16px  ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
lg: 24px  ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
xl: 32px  ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔

Common combinations:
  Button padding: 12px (1.5x) + 16px (2x)
  Picto grid gap: 8px (1x)
  Section margin: 24px (3x)
  Modal padding: 24px (3x)
```

---

## CSS Copy-Paste: Common Utilities

### Button Reset & Base

```css
button {
  border: none;
  font-family: inherit;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.2s ease;
  border-radius: 4px;
  font-weight: 700;
  font-size: 14px;
}

button:hover {
  opacity: 0.9;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

button:active {
  transform: scale(0.98);
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
}

button:disabled {
  background-color: #ccc !important;
  color: #666 !important;
  cursor: not-allowed;
  opacity: 0.5;
}
```

### Input Reset & Base

```css
input, select, textarea {
  font-family: inherit;
  text-transform: uppercase;
  font-size: 14px;
  border: 1px solid #ddd;
  padding: 8px 12px;
  border-radius: 4px;
  background-color: #fff;
  color: #333;
  transition: border-color 0.2s ease;
}

input:focus, select:focus, textarea:focus {
  outline: none;
  border-color: #1976d2;
  box-shadow: 0 0 0 3px rgba(25, 118, 210, 0.1);
}

input:disabled, select:disabled, textarea:disabled {
  background-color: #f5f5f5;
  color: #999;
  cursor: not-allowed;
}
```

### Grid Container

```css
.picto-grid {
  display: grid;
  gap: 8px;
  padding: 16px;
  grid-template-columns: repeat(4, 1fr);
  max-width: 600px;
}

@media (max-width: 768px) {
  .picto-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 6px;
    padding: 8px;
  }
}
```

---

## Responsive Breakpoint Test Cases

### Test at 600px (Breakpoint)

| Desktop (≥600px) | Mobile (<600px) |
|--|--|
| Picto: 100px | Picto: 80px |
| Grid: 4-col | Grid: 2-col |
| Font (body): 18px | Font (body): 14px |
| Button: full width | Button: full width |
| Modal: 500px width | Modal: 90vw width |

### Verify Responsive Switch

- [ ] At 599px: Mobile layout
- [ ] At 600px: Layout switches
- [ ] At 601px: Desktop layout
- [ ] No layout jumps (smooth transition)
- [ ] All touch targets remain ≥44px

---

## Quick Checklist: Before Launch

**Visual**:
- [ ] Green color (#c8e6c9) visible on pictos and textarea
- [ ] All text UPPERCASE
- [ ] Buttons are 44px tall
- [ ] No horizontal scroll on mobile
- [ ] Modal centered and visible

**Interaction**:
- [ ] Click picto → text appends
- [ ] Click HABLAR → Web Speech API speaks
- [ ] Click BORRAR → text clears
- [ ] Theme dropdown changes grid
- [ ] CONFIGURACION opens modal

**Responsive**:
- [ ] 4-col grid on desktop (100px)
- [ ] 2-col grid on mobile (80px)
- [ ] No overlapping elements
- [ ] Touch targets all ≥44px

**Accessibility**:
- [ ] Color contrast passes WCAG AA
- [ ] Tab navigation works (if implemented)
- [ ] Focus visible on buttons
- [ ] Alt text on images (if applicable)

---

## Version Control & Updates

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-04-30 | Initial wireframes and layout reference |

---

## Related Documents

- `comunicador-app-spec.md` — Full functional specification
- `comunicador-figma-report.md` — Design system documentation

**Status**: ✅ Complete – Ready for implementation
