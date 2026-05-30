# Comunicador — Communication Aid for Autism

## Project Structure
```
V1/
├── index.html           # Main application (single file, all logic inline)
├── config.js           # Theme definitions and image-to-word mappings
├── iniciar.bat        # Launcher: opens Chrome with --allow-file-access-from-files
├── play.jpg           # READ button icon
├── borrar.png         # DELETE icon
└── temas/             # Static images by theme
    ├── lugares/
    ├── acciones/
    ├── personas/
    └── emociones/
```

## How to Run
Double-click `iniciar.bat` (requires Chrome installed).

**Does NOT work by double-clicking `index.html`** — Chrome blocks local file access without `--allow-file-access-from-files`.

## Configuration (`config.js`)
Static images defined here. Format:
```js
const configuracion = {
    temas: {
        lugares: [
            { imagen: 'casa.png', palabra: 'CASA' },
            { imagen: 'coche.png', palabra: 'COCHE' }
        ],
        acciones: [
            { imagen: 'correr.png', palabra: 'CORRER' }
        ]
    }
};
```
- Image path constructed as `temas/{tema}/{imagen}` — file must exist at that path.
- Custom images (added via the modal) are stored in `localStorage` keyed as `imagenes_{tema}` — do not put them in `config.js`.

## Image Management
- **CONFIGURACION** button (purple, bottom-right): manage themes and add custom images.
- Theme selector creates new themes in memory (also persisted to `temas_custom` in localStorage).
- Import/Export ZIP: exports custom images organized by theme; config images must be added manually.
- **Important**: New themes persist in `localStorage['temas_custom']` as JSON array of theme names.

## Theme Persistence
- **Static themes**: defined in `config.js` — loaded on every page load.
- **Custom themes**: saved in `localStorage['temas_custom']` as JSON array.
- **Images per theme**: stored in `localStorage['imagenes_{tema}']` as JSON array of `{palabra, imagen}` objects.
- When creating a new theme, call `crearNuevoTema()` which updates `configuracion.temas` and persists to `localStorage`.

## Tech
- Vanilla HTML/CSS/JS — no build step, no dependencies except JSZip (CDN).
- Web Speech API (`es-ES`) for TTS, rate 0.9.
- All text uppercased; `text-transform: uppercase` on textarea input.
- **Background colors**: Green (#c8e6c9) for pictos container and text area.
