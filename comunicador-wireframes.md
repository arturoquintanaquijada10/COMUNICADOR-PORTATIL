# Comunicador — Wireframes & ASCII Reference

## Quick Reference Diagrams

All screens with ASCII wireframes for quick visualization during development.

---

## Screen 1: Main Board — Desktop Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          COMUNICADOR — MAIN BOARD                        │
│                         Desktop Layout (1280x720)                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  TEXT AREA                                 [#caja-texto]         │  │
│  │  "Escribe aquí..."                                              │  │
│  │  UPPERCASE | 24px | 100px height | Green #c8e6c9              │  │
│  │  Placeholder text shown when empty                             │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                           │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  [🔊 SPEAK BUTTON]  [🗑️ DELETE BUTTON]                          │  │
│  │  Image icon (play.jpg)    Red button (#f44336)                 │  │
│  │  Green bg #4CAF50        text: "BORRAR"                        │  │
│  │  Hover: darker green      18px bold                            │  │
│  │  3px black border         3px black border                     │  │
│  │  10px radius              10px radius                          │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                           │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  THEME BUTTONS (Flex row, wrap)                                 │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │  │
│  │  │ LUGARES  │ │ACCIONES  │ │PERSONAS  │ │EMOCIONES │ ...      │  │
│  │  │ Active   │ │ Inactive │ │ Inactive │ │ Inactive │           │  │
│  │  │ Orange   │ │ Gray     │ │ Gray     │ │ Gray     │           │  │
│  │  │#FF9800   │ │#666666   │ │#666666   │ │#666666   │           │  │
│  │  │ [btn]    │ │ [btn]    │ │ [btn]    │ │ [btn]    │           │  │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │  │
│  │  Flex: 1 min-width:70px, gap:8px, wrap                         │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                           │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                    PICTO GRID                                    │  │
│  │                  [#contenedor-botones]                           │  │
│  │                                                                   │  │
│  │  Green bg #c8e6c9                                               │  │
│  │  CSS Grid: auto-fill, minmax(100px, 1fr)                        │  │
│  │  Gap: 10px                                                       │  │
│  │  Padding: 10px                                                   │  │
│  │                                                                   │  │
│  │  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐              │  │
│  │  │ IMG1 │  │ IMG2 │  │ IMG3 │  │ IMG4 │  │ IMG5 │              │  │
│  │  │      │  │      │  │      │  │      │  │      │              │  │
│  │  │      │  │      │  │      │  │      │  │      │              │  │
│  │  ├──────┤  ├──────┤  ├──────┤  ├──────┤  ├──────┤              │  │
│  │  │CASA  │  │COCHE │  │ ... │  │...   │  │...   │              │  │
│  │  └──────┘  └──────┘  └──────┘  └──────┘  └──────┘              │  │
│  │                                                                   │  │
│  │  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐              │  │
│  │  │ IMG6 │  │ IMG7 │  │ IMG8 │  │ IMG9 │  │IMG10 │              │  │
│  │  │      │  │      │  │      │  │      │  │      │              │  │
│  │  │      │  │      │  │      │  │      │  │      │              │  │
│  │  ├──────┤  ├──────┤  ├──────┤  ├──────┤  ├──────┤              │  │
│  │  │...   │  │...   │  │...   │  │...   │  │...   │              │  │
│  │  └──────┘  └──────┘  └──────┘  └──────┘  └──────┘              │  │
│  │                                                                   │  │
│  │  (Scrollable if content > viewport height)                      │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                           │
│                              ┌─────────────────────┐                    │
│                              │  [CONFIGURACION]    │                    │
│                              │  Purple #9C27B0     │                    │
│                              │  Fixed bottom-right │                    │
│                              │  z-index: 100       │                    │
│                              └─────────────────────┘                    │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘

PICTO BUTTON DETAIL (100x100px cell):
┌──────────────────┐
│                  │  100px
│    IMAGE         │  75%
│   (75% height)   │  of
│                  │  cell
├──────────────────┤
│ LABEL TEXT       │  100px
│ (25% height)     │  25%
│ UPPERCASE        │  of
│                  │  cell
└──────────────────┘
  100px wide
  1:1 aspect ratio
  3px border #333
  10px radius
  white background
  Hover: scale 1.05, green border
  Active: scale 0.95
```

---

## Screen 1: Main Board — Mobile Layout

```
┌─────────────────────────────────────────────┐
│        COMUNICADOR — MOBILE LAYOUT           │
│          (375x812 viewport)                  │
├─────────────────────────────────────────────┤
│                                              │
│  ┌───────────────────────────────────────┐ │
│  │ TEXT AREA                             │ │
│  │ "Escribe aquí..."                    │ │
│  │ 80px height | 20px font | Green bg   │ │
│  └───────────────────────────────────────┘ │
│                                              │
│  ┌───────────────────────────────────────┐ │
│  │ [🔊] [DELETE]                         │ │
│  │ Buttons wrapped, smaller (16px font) │ │
│  └───────────────────────────────────────┘ │
│                                              │
│  ┌───────────────────────────────────────┐ │
│  │ [LUGARES] [ACCIONES]                  │ │
│  │ [PERSONAS] [EMOCIONES]                │ │
│  │ Theme buttons wrapped (12px font)    │ │
│  │ Smaller min-width: 60px               │ │
│  └───────────────────────────────────────┘ │
│                                              │
│  ┌───────────────────────────────────────┐ │
│  │      PICTO GRID (Mobile)              │ │
│  │  80px cells × 80px (1:1 aspect)       │ │
│  │  Auto-fill: minmax(80px, 1fr)         │ │
│  │  Gap: 8px                              │ │
│  │  Green bg #c8e6c9                      │ │
│  │                                        │ │
│  │  ┌────┐ ┌────┐ ┌────┐ ┌────┐         │ │
│  │  │ P1 │ │ P2 │ │ P3 │ │ P4 │         │ │
│  │  ├────┤ ├────┤ ├────┤ ├────┤         │ │
│  │  │TX1 │ │TX2 │ │TX3 │ │TX4 │         │ │
│  │  └────┘ └────┘ └────┘ └────┘         │ │
│  │                                        │ │
│  │  ┌────┐ ┌────┐ ┌────┐ ┌────┐         │ │
│  │  │ P5 │ │ P6 │ │ P7 │ │ P8 │         │ │
│  │  ├────┤ ├────┤ ├────┤ ├────┤         │ │
│  │  │TX5 │ │TX6 │ │TX7 │ │TX8 │         │ │
│  │  └────┘ └────┘ └────┘ └────┘         │ │
│  │                                        │ │
│  │  (Scrollable if overflow)              │ │
│  └───────────────────────────────────────┘ │
│                                              │
│                [CONFIG]                     │
│          Fixed bottom-right                 │
│          10px from edge                     │
│                                              │
└─────────────────────────────────────────────┘

MOBILE PICTO BUTTON DETAIL (80x80px):
┌────────────────┐
│      IMAGE     │  80px
│     (60px)     │  1:1
│                │
├────────────────┤
│  LABEL (11px)  │
│   UPPERCASE    │
└────────────────┘
  80px wide
```

---

## Screen 2: Configuration Modal — Desktop

```
┌────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  [OVERLAY - Fixed, Full viewport, rgba(0,0,0,0.5)]               │
│                                                                     │
│    ┌────────────────────────────────────────────────────────┐    │
│    │         GESTION DE IMAGENES                    [TITLE] │    │
│    ├────────────────────────────────────────────────────────┤    │
│    │                                                        │    │
│    │  TEMA:                                                │    │
│    │  ┌──────────────────────┬──────────┬────────────┐    │    │
│    │  │ [SELECT DROPDOWN ▼]  │+ NUEVO   │  🗑️ DELETE │    │    │
│    │  │ All themes listed    │  Green   │ Image btn  │    │    │
│    │  │ - lugares            │#4CAF50   │ (35px)     │    │    │
│    │  │ - acciones           │          │            │    │    │
│    │  │ - personas           │          │            │    │    │
│    │  │ - emociones          │          │            │    │    │
│    │  │ - miTema (custom)    │          │            │    │    │
│    │  └──────────────────────┴──────────┴────────────┘    │    │
│    │                                                        │    │
│    │  ┌─ NEW THEME SECTION (Hidden initially) ─────────┐  │    │
│    │  │ [Input: "Nombre del nuevo tema..."]             │  │    │
│    │  │ [CREATE - Green]  [CANCEL - Red]               │  │    │
│    │  └────────────────────────────────────────────────┘  │    │
│    │                                                        │    │
│    ├────────────────────────────────────────────────────────┤    │
│    │                                                        │    │
│    │  PALABRA:                                             │    │
│    │  ┌──────────────────────┬──────────┬──────────────┐  │    │
│    │  │ [TEXT INPUT]         │[DROPDOWN]│ 🗑️ DELETE    │  │    │
│    │  │ "Escribe la palabra" │Custom    │ (if custom   │  │    │
│    │  │ UPPERCASE            │images    │  images)     │  │    │
│    │  │                      │for theme │              │  │    │
│    │  └──────────────────────┴──────────┴──────────────┘  │    │
│    │                                                        │    │
│    ├────────────────────────────────────────────────────────┤    │
│    │                                                        │    │
│    │  IMAGEN:                                              │    │
│    │  [📁 FILE INPUT - Choose Image]                       │    │
│    │  Accept: image/*                                      │    │
│    │                                                        │    │
│    │  ┌─────────────────┐                                  │    │
│    │  │ [PREVIEW IMAGE] │  (80x80px, hidden until upload)│    │
│    │  │ Thumbnail shown │                                  │    │
│    │  └─────────────────┘                                  │    │
│    │                                                        │    │
│    ├────────────────────────────────────────────────────────┤    │
│    │                                                        │    │
│    │  [CERRAR - Red]     [GUARDAR - Green]                │    │
│    │   #f44336            #4CAF50                          │    │
│    │   Cancel modal        Save image to localStorage      │    │
│    │                                                        │    │
│    ├─────────────────── SEPARATOR ────────────────────────┤    │
│    │                                                        │    │
│    │  IMPORTAR/EXPORTAR:                                   │    │
│    │  [IMPORTAR ZIP - Orange]  [EXPORTAR ZIP - Blue]      │    │
│    │   #FF9800                  #2196F3                    │    │
│    │   File picker (.zip)       Download backup            │    │
│    │                                                        │    │
│    │  Status: "Exportadas 12 imagenes" (or error msg)     │    │
│    │          Font: 12px, gray #666, margin-top: 8px      │    │
│    │                                                        │    │
│    ├────────────────────────────────────────────────────────┤    │
│    │                                                        │    │
│    │  Tema: LUGARES | Total: 10 | Personalizadas: 5       │    │
│    │  (Info text, 14px gray, updated on theme change)     │    │
│    │                                                        │    │
│    └────────────────────────────────────────────────────────┘    │
│                                                                     │
│  Modal sizing:                                                     │
│  - Width: max-width 450px                                         │
│  - Height: auto (content-driven)                                  │
│  - Padding: 20px                                                  │
│  - Border-radius: 15px                                            │
│  - Background: white #FFFFFF                                      │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

---

## Screen 2: Configuration Modal — Mobile

```
┌──────────────────────────────────────────────┐
│                                               │
│  [OVERLAY - 50% opacity, full viewport]      │
│                                               │
│  ┌────────────────────────────────────────┐ │
│  │    GESTION DE IMAGENES           [X]   │ │
│  ├────────────────────────────────────────┤ │
│  │                                        │ │
│  │  TEMA:                                 │ │
│  │  ┌──────────────────────────────────┐ │ │
│  │  │ [SELECT DROPDOWN ▼]              │ │ │
│  │  │ - lugares                        │ │ │
│  │  │ - acciones                       │ │ │
│  │  │ - ...                            │ │ │
│  │  └──────────────────────────────────┘ │ │
│  │  [+ NUEVO] [DELETE]                   │ │
│  │  (Stacked on mobile)                  │ │
│  │                                        │ │
│  │  [NEW THEME INPUT - hidden]           │ │
│  │                                        │ │
│  ├────────────────────────────────────────┤ │
│  │                                        │ │
│  │  PALABRA:                              │ │
│  │  ┌──────────────────────────────────┐ │ │
│  │  │ [Word Input]                     │ │ │
│  │  └──────────────────────────────────┘ │ │
│  │  [Delete Dropdown] [Delete Button]    │ │
│  │                                        │ │
│  ├────────────────────────────────────────┤ │
│  │                                        │ │
│  │  IMAGEN:                               │ │
│  │  [📁 Choose File]                      │ │
│  │  ┌──────────────┐                      │ │
│  │  │ [Preview]    │                      │ │
│  │  └──────────────┘                      │ │
│  │                                        │ │
│  ├────────────────────────────────────────┤ │
│  │                                        │ │
│  │  [CERRAR]  [GUARDAR]                   │ │
│  │  (Stacked on mobile)                  │ │
│  │                                        │ │
│  ├────────────────────────────────────────┤ │
│  │                                        │ │
│  │  IMPORTAR/EXPORTAR:                    │ │
│  │  [IMPORTAR ZIP]                        │ │
│  │  [EXPORTAR ZIP]                        │ │
│  │  (Stacked on mobile)                  │ │
│  │  Status: "..."                         │ │
│  │                                        │ │
│  ├────────────────────────────────────────┤ │
│  │                                        │ │
│  │  Tema: LUGARES                         │ │
│  │  Total: 10 | Pers: 5                  │ │
│  │  (Wrapped on mobile)                  │ │
│  │                                        │ │
│  └────────────────────────────────────────┘ │
│                                               │
│  Modal sizing (mobile):                      │
│  - Width: 95%                                │
│  - Margin: 10px auto                         │
│  - Padding: 15px                             │
│  - Responsive text & button sizes            │
│                                               │
└──────────────────────────────────────────────┘
```

---

## Component Breakdown

### Button Components

**PRIMARY BUTTON (Action - Green)**
```
┌─────────────────┐
│   SPEAK TEXT    │
│ or similar      │
│ Background:     │
│ #4CAF50         │
│ Hover: #45a049  │
│ Text: white     │
│ Border: 3px #333│
│ Radius: 10px    │
│ Padding: 8-20px │
│ Font: 18px bold │
│ Cursor: pointer │
└─────────────────┘
```

**SECONDARY BUTTON (Destructive - Red)**
```
┌─────────────────┐
│   DELETE TEXT   │
│ or similar      │
│ Background:     │
│ #f44336         │
│ Hover: #d32f2f  │
│ Text: white     │
│ Border: 3px #333│
│ Radius: 10px    │
│ Padding: 8-20px │
│ Font: 18px bold │
│ Cursor: pointer │
└─────────────────┘
```

**THEME BUTTON (Inactive)**
```
┌─────────────────┐
│  LUGARES TEXT   │
│ or theme name   │
│ Background:     │
│ #666666         │
│ Hover: #555555  │
│ Text: white     │
│ Border: 3px #333│
│ Radius: 10px    │
│ Padding: 8-12px │
│ Font: 14px bold │
│ Flex: 1         │
│ Min-width: 70px │
└─────────────────┘
```

**THEME BUTTON (Active)**
```
┌─────────────────┐
│  LUGARES TEXT   │
│ (Active theme)  │
│ Background:     │
│ #FF9800         │
│ Text: white     │
│ Border: 3px     │
│ #FF9800         │
│ Radius: 10px    │
│ Padding: 8-12px │
│ Font: 14px bold │
│ Flex: 1         │
│ Min-width: 70px │
└─────────────────┘
```

---

### Input Components

**TEXTAREA**
```
┌─────────────────────────────┐
│ "Escribe aquí..."           │
│                             │
│ User can type here          │
│ Text auto-uppercases        │
│ Placeholder shown when empty│
│                             │
│ Background: #c8e6c9        │
│ Border: 3px #333           │
│ Font: 24px, normal          │
│ Padding: 12px               │
│ Resize: none                │
│ Height: 100px (desktop)     │
│       80px (mobile)         │
│ Overflow-y: auto            │
└─────────────────────────────┘
```

**TEXT INPUT**
```
┌─────────────────────────────┐
│ Escribe la palabra...       │
│                             │
│ Background: white           │
│ Border: 2px #333           │
│ Radius: 8px                 │
│ Padding: 10px               │
│ Font: 16px                  │
│ Width: 100%                 │
│ Placeholder: gray           │
└─────────────────────────────┘
```

**DROPDOWN/SELECT**
```
┌─────────────────────────────┐
│ Select a theme...      ▼   │
│                             │
│ Options shown on click      │
│ Background: white           │
│ Border: 2px #333           │
│ Radius: 8px                 │
│ Padding: 10px               │
│ Font: 16px                  │
│ Width: 100% or flex         │
│ Height: 44px                │
└─────────────────────────────┘
```

**FILE INPUT**
```
┌─────────────────────────────┐
│ [📁 Choose File]            │
│ Accepts: image/*            │
│ (browser default style)     │
│ Margin-bottom: 12px         │
└─────────────────────────────┘
```

**IMAGE PREVIEW**
```
┌─────────────────┐
│                 │
│   [Preview]     │  80x80px
│                 │  Hidden until
│   Image box     │  file selected
│                 │
│ Border: 2px #333
│ Radius: 8px     │
│ Object-fit: cover
│ Margin-top: 8px │
│ Display: none   │
│ (toggled)       │
└─────────────────┘
```

---

### Grid Layout System

**PICTO GRID (Desktop)**
```
Container: #contenedor-botones
Display: grid
Grid-template-columns: repeat(auto-fill, minmax(100px, 1fr))
Gap: 10px
Padding: 10px
Overflow-y: auto
Align-content: start
Background: #c8e6c9
Height: flex (1 = fill remaining space)

Result:
┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐
│  │ │  │ │  │ │  │ │  │
├──┤ ├──┤ ├──┤ ├──┤ ├──┤
│  │ │  │ │  │ │  │ │  │
└──┘ └──┘ └──┘ └──┘ └──┘
100px cells, responsive columns
```

**PICTO GRID (Mobile)**
```
Grid-template-columns: repeat(auto-fill, minmax(80px, 1fr))
Gap: 8px
Padding: 8px
Result: More columns per row, smaller cells
```

---

### Modal Layout

**MODAL OVERLAY**
```
Position: fixed
Top: 0, Left: 0, Width: 100%, Height: 100%
Background: rgba(0, 0, 0, 0.5)
Display: flex (when open)
Justify-content: center
Align-items: center
Z-index: 1000
```

**MODAL DIALOG**
```
Background: white
Padding: 20px (desktop), 15px (mobile)
Border-radius: 15px
Width: 95% (mobile), 450px (desktop, max)
Max-height: 90vh
Overflow-y: auto (if needed)
Box-shadow: implicit (browser default)
```

---

## Color Palette Reference

```
PRIMARY (Communication)
#c8e6c9 - Light green, main accent

ACTIONS (Interactive)
#4CAF50 - Green, positive/speak/save
#45a049 - Green dark, hover
#f44336 - Red, delete/cancel
#d32f2f - Red dark, hover
#2196F3 - Blue, export/info
#1976D2 - Blue dark, hover

STATE (UI Feedback)
#FF9800 - Orange, active/selected
#e68a00 - Orange dark, hover

NEUTRAL (Background & Text)
#FFFFFF - White, surfaces
#EEEEEE - Light gray, tertiary surfaces
#666666 - Dark gray, default buttons
#555555 - Gray dark, hover
#333333 - Black, borders & text

SPECIAL
#9C27B0 - Purple, config button
#7B1FA2 - Purple dark, hover
#f0f0f0 - Body background (very light gray)
```

---

## Typography Scale

```
DISPLAY
Font: Arial, sans-serif
Size: 24px (desktop), 20px (mobile)
Weight: 400 (normal)
Usage: Textarea content

HEADING 1
Font: Arial, sans-serif
Size: 22px (desktop), 20px (mobile)
Weight: 400 (normal)
Usage: Modal title "GESTION DE IMAGENES"

HEADING 2
Font: Arial, sans-serif
Size: 18px (desktop), 16px (mobile)
Weight: 700 (bold)
Usage: Button text

BODY
Font: Arial, sans-serif
Size: 16px
Weight: 400 (normal)
Usage: Modal labels & inputs

BODY SMALL
Font: Arial, sans-serif
Size: 14px (desktop), 11px (mobile)
Weight: 400 (normal)
Usage: Theme button text, picto labels

CAPTION
Font: Arial, sans-serif
Size: 12px
Weight: 400 (normal)
Usage: Info text, status messages
```

---

## Responsive Breakpoint

```
DESKTOP (> 600px)
├─ Textarea: 24px font, 100px height
├─ Buttons: 18px font, 40px min-height
├─ Picto cells: 100px × 100px
├─ Gap: 10px
├─ Modal: max-width 450px
└─ Padding: 20px

MOBILE (≤ 600px)
├─ Textarea: 20px font, 80px height
├─ Buttons: 16px font, 36px min-height
├─ Picto cells: 80px × 80px
├─ Gap: 8px
├─ Modal: 95% width
└─ Padding: 15px
```

---

## Spacing Reference

All layout uses multiples of base unit (4px):

```
4px  = xs (rarely used)
8px  = sm (component gaps on mobile)
10px = md (default gap & padding)
12px = lg (modal label spacing)
15px = xl (modal padding mobile)
20px = 2xl (modal padding desktop)
```

---

## Border & Radius Reference

```
BUTTONS
Border: 3px solid #333
Radius: 10px
Padding: 8-20px

INPUTS
Border: 2px solid #333
Radius: 8px
Padding: 10px

MODALS
Border: none (white bg)
Radius: 15px
Padding: 15-20px

PICTOS
Border: 3px solid #333
Radius: 10px
Padding: none
```

---

## Interactive States

```
BUTTON DEFAULT
Background: solid color
Border: 3px solid #333
Transform: none
Cursor: pointer

BUTTON HOVER
Background: 10% darker
Border: 3px solid #333
Transform: none
Cursor: pointer

BUTTON ACTIVE
Background: solid color
Border: 3px solid #333
Transform: scale(0.95)
Cursor: pointer

PICTO HOVER
Background: white
Border: 3px solid #4CAF50 (green)
Transform: scale(1.05)
Cursor: pointer

PICTO ACTIVE
Background: white
Border: 3px solid #333
Transform: scale(0.95)
Cursor: pointer
```

---

## Quick Copy-Paste CSS

```css
/* Color Variables */
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

/* Typography */
body {
  font-family: Arial, sans-serif;
}

/* Buttons */
.btn-accion {
  padding: 8px 20px;
  font-size: 18px;
  border: 3px solid #333;
  border-radius: 10px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.1s;
}

.btn-accion:hover {
  background-color: var(--color-gray);
}

.btn-accion:active {
  transform: scale(0.95);
}

/* Inputs */
input[type="text"], select, textarea {
  border: 2px solid #333;
  border-radius: 8px;
  padding: 10px;
  font-size: 16px;
  font-family: Arial, sans-serif;
}

/* Grid */
#contenedor-botones {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  gap: 10px;
  padding: 10px;
  background-color: var(--color-primary);
}

/* Mobile */
@media (max-width: 600px) {
  #contenedor-botones {
    grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
  }
}
```

---

## Summary

This wireframe reference serves as a quick visual guide during development. Use alongside the detailed specification (`comunicador-app-spec.md`) for:
- Exact pixel values
- Interaction behaviors
- Data flow
- Accessibility requirements

**Version**: 1.0  
**Last Updated**: 2026-04-30  
**Status**: ✅ Ready for Development

