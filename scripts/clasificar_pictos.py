#!/usr/bin/env python3
import os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGENES = os.path.join(BASE, 'imagenes')

lugares = {'AQUÍ', 'AQUI', 'ABAJO', 'ARRIBA', 'BAJO', 'CASTILLO', 'DENTRO',
           'DONDE', 'DÓNDE', 'DONDE', 'DÓNDE?', 'FUERA', 'GRANJA',
           'LUGAR', 'LUGARES', 'CABANILLAS', 'DONDE?'}

personas = {'ABUELA', 'ABUELO', 'AMIGO', 'AMIGA', 'BEBÉ', 'BEBE', 'CHICA',
            'CHICO', 'GENTE', 'HERMANA', 'HERMANO', 'HOMBRE', 'LAURA',
            'MAMÁ', 'MAMA', 'MAMA', 'MUJER', 'MÁS_PERSONAS', 'NIÑA',
            'NIÑO', 'NIÑOS', 'NOSOTROS', 'PAPÁ', 'PAPA', 'PAPA_ARTURO',
            'PERSONAS', 'PILAR', 'PRIMA', 'PRIMO', 'RITA', 'SALUDOS',
            'SARA', 'TÍA', 'TIA', 'TÍO', 'TIO', 'TU', 'YO',
            'HERMANA_LAURA', 'HERMANA_SARA', 'MAMA_EVA', 'YO_EN_CABANILLAS'}

emociones = {'ABURRO', 'ASUSTADO', 'BIEN', 'CALIENTE', 'CALOR', 'CANSADO',
             'CONTENTO', 'CON_CALOR', 'CON_FRIO', 'DUELE', 'ENFADADO',
             'ENFERMO', 'FRIO', 'FELIZ', 'GUSTA', 'GUSTA_LA_MUSICA',
             'LLORANDO', 'MAL', 'ME_ABURRO', 'ME_DUELE',
             'ME_ESTOY_PONIENDO_NERVIOSO', 'ME_GUSTA', 'ME_GUSTA_LA_MUSICA',
             'ME_MOLESTA_EL_RUIDO', 'MOLESTA', 'NERVIOSO', 'RUIDO',
             'SENTIMIENTOS', 'SENTIR', 'TE_QUIERO', 'TRANQUILO', 'TRISTE'}

alimentos = {'AGUA', 'ALIMENTOS', 'BOCADILLO', 'BOLLO', 'COCACOLA',
             'COMER', 'ENSALADA', 'ESPAGUETIS', 'FANTA', 'GALLETAS',
             'HAMBURGUESA', 'HAMBRE', 'LECHE', 'PAN', 'PIZZA', 'PURÉ',
             'PURE', 'SED', 'SOPA', 'TENGO_HAMBRE', 'TENGO_SED',
             'TORTILLA', 'ZUMO'}

objetos = {'AMARILLO', 'AZUL', 'BABERO', 'BARRIGA', 'BATA', 'BAUL',
           'BIGOTE', 'BLANCO', 'BOCA', 'BRAZO', 'CABEZA', 'CARA',
           'CASCOS', 'COCODRILO', 'COLORES', 'CREMA', 'CUCHARA',
           'CUCHILLO', 'CULO', 'DEDOS', 'DIENTES', 'FORMAS',
           'GAFAS_DE_SOL', 'GRIS', 'LÁPIZ', 'LAPIZ', 'LENGUA',
           'MANOS', 'MARRÓN', 'MARRON', 'MORADO', 'NARIZ', 'NEGRO',
           'OJOS', 'OREJA', 'ORO', 'PARAGUAS', 'PELO', 'PIEDRA',
           'PIERNA', 'PIES', 'PIOJO', 'PLATA', 'PLATO', 'PLAY',
           'ROJO', 'ROSA', 'SERVILLETAS', 'SILLA', 'TABLET', 'TEJADO',
           'TELEFONO', 'TELÉFONO', 'TENEDOR', 'VASO', 'VERDE',
           'LIMPIO', 'SUCIO', 'LLENO', 'VACIO'}

acciones = {'ABIERTO', 'AHORA', 'ALTO', 'BORRAR', 'CANTAR',
            'CERRADO', 'CHARLA_RAPIDA', 'COGER', 'DAR',
            'DEPORTE', 'DESCANSAR', 'DESCRIBIR', 'DESPUES',
            'DORMIR', 'DUCHAR', 'ELIMINAR', 'ESTAR', 'HACER',
            'IR', 'JUGAR', 'LAVAR_LAS_MANOS', 'LAVAR_LOS_DIENTES',
            'MAS', 'MORDER', 'MUCHO', 'NADA', 'NECESITO_LOS_CASCOS',
            'NECESITO_TIEMPO', 'NOVEDADES', 'NO', 'OCIO',
            'OPINIONES', 'OTRA_COSA', 'PASEAR', 'PEGAR', 'PEINAR',
            'PEQUEÑO', 'PINTAR', 'POCO', 'PONER', 'PURPURINA',
            'QUERER', 'QUITAR', 'SALIR', 'SALTAR', 'SANGRA_LA_NARIZ',
            'SENTAR', 'SER', 'SUBIR', 'TENER', 'TIEMPO', 'TODO',
            'TRABAJAR', 'TU_SOLITO', 'VENIR', 'VER', 'VESTIR',
            'VOLVER', 'YA_ESTA',
            '¡AY_QUE_LIO!', '¡ESTE_CHICO!', '¡QUE_PESTE!',
            '¿COMO?', '¿ME_AYUDAS?', '¿QUE?', '¿QUIEN?'}

themes = {
    'lugares': lugares,
    'personas': personas,
    'emociones': emociones,
    'alimentos': alimentos,
    'objetos': objetos,
    'acciones': acciones,
}

def theme_for(name):
    name_no_suffix = re.sub(r'_\d+$', '', name)
    words = {name, name_no_suffix}
    parts = set(name.split('_'))
    all_candidates = words | parts

    scores = {}
    for theme, wordset in themes.items():
        match = all_candidates & wordset
        if match:
            scores[theme] = len(match)

    if not scores:
        return 'otros'

    max_score = max(scores.values())
    best = [t for t, s in scores.items() if s == max_score]

    priority = ['personas', 'emociones', 'alimentos', 'lugares', 'objetos', 'acciones']
    for p in priority:
        if p in best:
            return p
    return best[0]

files = sorted([f for f in os.listdir(IMAGENES) if f.endswith('.png') and not f.startswith('page')])

result = {t: [] for t in ['lugares', 'acciones', 'personas', 'emociones', 'objetos', 'alimentos', 'otros']}

for f in files:
    name_no_ext = f.replace('.png', '')
    palabra = name_no_ext.replace('_', ' ').strip()
    # Clean up: remove trailing _ artifacts
    palabra = re.sub(r'\s+', ' ', palabra)
    theme = theme_for(name_no_ext)
    result[theme].append((f, palabra))

# Write config.js
lines = ['const configuracion = {', '    temas: {']
for theme in ['lugares', 'acciones', 'personas', 'emociones', 'objetos', 'alimentos', 'otros']:
    lines.append(f"        {theme}: [")
    for filename, palabra in sorted(result[theme], key=lambda x: x[1]):
        lines.append(f"            {{ imagen: '{filename}', palabra: '{palabra}' }},")
    lines.append("        ],")
lines.append("    }")
lines.append("};")

config_path = os.path.join(BASE, 'config.js')
with open(config_path, 'w') as f:
    f.write('\n'.join(lines))

total = sum(len(v) for v in result.values())
print(f"config.js written with {total} entries")
for t in ['lugares', 'acciones', 'personas', 'emociones', 'objetos', 'alimentos', 'otros']:
    items = sorted(result[t], key=lambda x: x[1])
    print(f"\n  {t} ({len(items)}):")
    for f, p in items:
        print(f"    {f:40s} -> {p}")
