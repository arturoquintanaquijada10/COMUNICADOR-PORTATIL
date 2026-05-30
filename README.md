# Comunicador — Ayuda a la Comunicación para el Autismo

Aplicación web de comunicación aumentativa basada en pictogramas. Diseñada para personas con autismo o dificultades del habla. Seleccionan imágenes organizadas por temas que se convierten en voz sintetizada en español.

## Cómo funciona

1. El usuario selecciona un **tema** (LUGARES, ACCIONES, PERSONAS, EMOCIONES, OBJETOS, ALIMENTOS, OTROS)
2. Pulsa pictogramas dentro del tema → se añaden a la caja de texto superior
3. Pulsa el botón **PLAY** (🔊) para que el navegador lea el texto en voz alta
4. **BORRAR** vacía la caja de texto

## Funcionalidades

| Función | Descripción |
|---------|-------------|
| **7 temas predefinidos** | 222 pictogramas incluidos en `config.js` |
| **Temas personalizados** | Crear/borrar temas con imagen asociada |
| **Añadir pictogramas** | Subir imagen propia o seleccionar de las existentes |
| **Ocultar/mostrar** | Ocultar pictogramas del config sin borrarlos |
| **Password parental** | ⚙️ abajo a la derecha — contraseña en `config.js` (`clave_acceso`, por defecto `sonrie`) — protege los 4 botones de configuración |
| **Exportar config** | Descarga un `config.js` con los cambios (temas creados, pictogramas ocultos, añadidos) |
| **Importar config** | Carga un `config.js` exportado previamente (reemplaza configuración completa) |
| **Pictogramas ocultos** | `localStorage['ocultos_{tema}']` — se filtran en la UI |
| **Persistencia recarga** | Temas eliminados, personalizados, imágenes y contraseñas sobreviven a recarga vía localStorage |

## Configuración parental

Los 4 botones inferiores (TEMAS, PALABRAS, IMP/EXP, CONFIGURACION) están ocultos por defecto. Para acceder:

1. Pulsa ⚙️ (abajo a la derecha)
2. Introduce la contraseña (por defecto: `sonrie`)
3. Se desbloquean los botones; al pulsar ⚙️ de nuevo se vuelven a ocultar

La contraseña se configura en `config.js`:
```js
const configuracion = {
    clave_acceso: 'sonrie',  // ← cambia esto
    temas: { ... }
};
```

## Cómo ejecutar

Abrir `index.html` con Chrome usando `--allow-file-access-from-files`:

```bash
# macOS
open -a "Google Chrome" --args --allow-file-access-from-files index.html

# Windows (doble clic en v2/iniciar.bat)
```

**No funciona abriendo `index.html` directamente** — Chrome bloquea el acceso a archivos locales sin esa bandera.

## Estructura del proyecto

```
COMUNICADOR_WIP/
├── index.html          # App completa (HTML+CSS+JS, todo inline)
├── config.js           # 222 pictogramas + temas_info + clave_acceso
├── imagenes/           # 230 imágenes PNG (todos los pictogramas)
├── borrar.png          # Icono papelera (usado en modales)
├── play.jpg            # Icono de LEER
├── docs/               # Documentación detallada
├── scripts/            # Utilidades (clasificación de pictos)
└── package.json
```

## Persistencia (localStorage)

| Clave | Formato | Propósito |
|-------|---------|-----------|
| `temas_custom` | `string[]` | Nombres de temas personalizados |
| `imagenes_{tema}` | `{palabra, imagen}[]` | Pictogramas añadidos por el usuario |
| `temas_info_custom` | `{tema: {imagen, palabra}}` | Imagen asociada a tema personalizado |
| `ocultos_{tema}` | `string[]` | Nombres de imagen ocultos del config |
| `temas_eliminados` | `string[]` | Temas por defecto borrados por el usuario |

## Tecnología

- **Stack**: Vanilla HTML/CSS/JS — sin build step, sin dependencias
- **Voz**: Web Speech API (`es-ES`, rate 0.9)
- **Persistencia**: localStorage (no necesita servidor)
- **Offline**: 100% local, sin conexión a internet
- **Config**: `config.js` se carga como script, modificaciones en localStorage

## Exportar / Importar

- **Exportar**: genera `conf_[nombre].js` descargable con todos los cambios (temas creados, pictogramas ocultos/añadidos, información de temas)
- **Importar**: reemplaza completamente la configuración actual por la del archivo importado
- Los pictogramas subidos como archivo (base64) NO se incluyen en la exportación; solo los añadidos desde imágenes existentes
