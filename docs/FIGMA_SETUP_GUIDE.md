# 📋 FIGMA SETUP GUIDE - 10 Pasos

## Crear el Archivo Figma para Comunicador V2

**Tiempo estimado**: ~70 minutos
**Requisitos**: Cuenta de Figma (gratis en figma.com)
**Herramientas**: Token Figma: `figd_8mnNJzZ5UVg3gfHV4XbatVXjTJhHQmwnaVPvDOiO`

---

## 🚀 PASO 1: Abre tu Cuenta Figma

1. Ve a [figma.com](https://figma.com)
2. Inicia sesión con tu cuenta (arturo@...)
3. Haz click en "New File" o "Create new"

---

## 📄 PASO 2: Crea un Nuevo Archivo

1. Click en "New File"
2. Nombre del archivo: **"Comunicador V2 - Autism Communication Aid"**
3. Click en "Create"

---

## 🎨 PASO 3: Crea la Primera Página - Design System

1. En el panel izquierdo, verás "Page 1"
2. Renómbralo a: **"Design System"**
3. Right-click → Rename

---

## 🌈 PASO 4: Añade Colores (Design Tokens)

En la página "Design System":

### Crea un Frame: "Colors"
1. Click en "Frame" tool (shortcut: F)
2. Dibuja un frame grande
3. Nombre: **"Colors"**

### Colores a añadir (como rectángulos etiquetados):

**Primary Colors:**
- #2563EB - Primary Blue (etiqueta: "Primary")
- #1E40AF - Primary Dark
- #DBEAFE - Primary Light

**Status Colors:**
- #10B981 - Success (Verde)
- #06B6D4 - Info (Cyan)
- #DC2626 - Error (Rojo)
- #F59E0B - Warning (Ámbar)

**Neutrals:**
- #111827 - Black
- #6B7280 - Gray
- #F3F4F6 - Light Gray
- #FFFFFF - White

**Adicionales:**
- #9333EA - Purple
- #EC4899 - Pink

---

## 📝 PASO 5: Añade Tipografía

En "Design System", crea otro Frame: **"Typography"**

### Estilos de Texto a crear:

```
H1: Inter, 48px, Bold (700)
H2: Inter, 36px, Semibold (600)
H3: Inter, 24px, Semibold (600)
Body: Inter, 16px, Regular (400)
Caption: Inter, 12px, Medium (500)
Button: Inter, 14px, Semibold (600)
```

**Cómo crear:**
1. Click en "Text" tool (shortcut: T)
2. Dibuja un text box
3. Escribe: "H1 - Heading 1"
4. En el panel derecho, selecciona Font: Inter
5. Size: 48px
6. Weight: Bold

---

## 🧩 PASO 6: Crea Componentes Base

En "Design System", crea un Frame: **"Components"**

### Componente 1: PictoButton

```
Frame name: "PictoButton/Base"
├─ Rectangle (80x80px, rounded 8px, fill: #2563EB)
├─ Image placeholder (60x60px, centered)
└─ Text (12px, "PALABRA")
```

**Estados a crear:**
- Base (default)
- Hover (darker background)
- Active (pressed effect)
- Focus (outline visible)
- Disabled (gray + 50% opacity)

### Componente 2: Button

```
Frame name: "Button/Primary"
├─ Rectangle (120x44px, rounded 6px, fill: #2563EB)
└─ Text (14px bold, "ACCIÓN", color: white)
```

**Variantes:**
- Primary (azul)
- Secondary (gris)
- Error (rojo)

---

## 📱 PASO 7: Crea la Página "Screens"

1. Añade nueva página: "Screens"
2. Crea 3 frames:

### Frame 1: Home - Desktop (1280x720)
```
Header:
├─ ThemeSelector dropdown
└─ Settings button (engranaje)

Main:
├─ PictoGrid 4 columnas x 3 filas (12 pictos)
└─ TextArea (abajo, grande, UPPERCASE)

Footer:
├─ Button "HABLAR" (verde)
├─ Button "LIMPIAR" (gris)
└─ Button "CONFIGURAR" (azul)
```

### Frame 2: Home - Mobile (375x667)
```
Header:
├─ ThemeSelector dropdown
└─ Settings button

Main:
├─ PictoGrid 2 columnas x 4 filas (8 pictos visible)
└─ TextArea (abajo)

Footer:
├─ Button "HABLAR"
├─ Button "LIMPIAR"
└─ Button "CONFIGURAR"
```

### Frame 3: Config Modal (500x600)
```
Tabs:
├─ "Crear Tema"
├─ "Subir Imagen"
└─ "Exportar"

Tab 1 Content:
├─ Input: "Nombre del tema"
└─ Button "CREAR"

Tab 2 Content:
├─ Dropdown: "Selecciona tema"
├─ Input: "Palabra"
├─ File upload: "Elige imagen"
└─ Button "SUBIR"

Tab 3 Content:
├─ Button "EXPORTAR ZIP"
└─ Button "IMPORTAR ZIP"
```

---

## 🔗 PASO 8: Crea Prototipos (Interactividad)

1. Selecciona en "Screens":
   - Home Desktop frame
   - Haz click en "Prototype" tab (arriba derecha)

2. Interacciones a crear:
   - PictoButton click → TextArea se actualiza
   - "HABLAR" button → muestra estado de reproducción
   - "CONFIGURAR" button → Config Modal aparece
   - Settings icon → Config Modal aparece

---

## 📋 PASO 9: Documenta en Figma

1. En cada Frame, añade descripción (Inspector panel):
   - **Home Desktop**: "Main communication interface for desktop (1280x720)"
   - **Home Mobile**: "Mobile version with 2-column layout (375x667)"
   - **Config Modal**: "Settings dialog for theme creation and image upload"

2. En componentes, añade documentación:
   - Nombre
   - Uso
   - Estados
   - Restricciones

---

## 🚀 PASO 10: Comparte y Publica

1. Click en "Share" (arriba derecha)
2. Elige nivel de acceso:
   - **Private**: Solo tú
   - **Editor**: Equipo puede editar
   - **Viewer**: Equipo solo puede ver

3. Copy link y comparte

---

## 📊 Checklist de Finalización

- [ ] Archivo creado: "Comunicador V2 - Autism Communication Aid"
- [ ] Página "Design System" con:
  - [ ] Frame "Colors" (13 colores)
  - [ ] Frame "Typography" (6 escalas)
  - [ ] Frame "Components" (PictoButton, Button, etc.)
- [ ] Página "Screens" con:
  - [ ] Frame "Home - Desktop"
  - [ ] Frame "Home - Mobile"
  - [ ] Frame "Config Modal"
- [ ] Prototipos creados (interactividad)
- [ ] Documentación añadida
- [ ] Compartido con equipo

---

## ✨ Bonus: Mejoras Avanzadas (Opcional)

- Usar Figma Tokens plugin para sincronizar tokens
- Crear design system en Figma's library
- Usar Figma dev mode para developers
- Crear design specs automáticas con design doc generation

---

## 🆘 Troubleshooting

**P: ¿No encuentro la font Inter?**
R: Ve a Assets → Fonts → Busca "Inter" → Add library

**P: ¿Cómo creo componentes reutilizables?**
R: Right-click en un frame → Create component

**P: ¿Cómo exporto código de Figma?**
R: Usa plugins como Figma to React, Anima, etc.

**P: ¿Dónde veo mis design tokens?**
R: Assets panel (izquierda) → Colors / Typography / Components

---

## 📚 Recursos Útiles

- [Figma Docs](https://help.figma.com/)
- [Design System Best Practices](https://www.figma.com/design-systems/)
- [Figma Plugins](https://www.figma.com/community/plugins)
- [Accessibility in Figma](https://www.figma.com/resource-library/accessibility-guide/)

---

**¡Listo! Deberías tener un Design System completo en Figma.** 🎉

Si necesitas ayuda, consulta los otros archivos en esta carpeta:
- `design-system-preview.html` - Preview visual
- `comunicador-design-system.json` - Especificaciones técnicas
