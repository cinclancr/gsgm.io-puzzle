#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H3 — El plaintext de 2.422 B sobre tablero de ancho 14 con extracción prima.
Sesión L (2026-11-23), hipótesis H3 de FASE32_HIPOTESIS.md.

Transformación: volcar los 2.422 B en una cuadrícula de 14 columnas (173 filas),
extraer bytes en filas/columnas/celdas/posiciones primas y comparar con
payload60/dbbi/faed (reproducción estructural). Criterio: coincidencia exacta
de cadena; NINGÚN AES se ejecuta sin coincidencia estructural previa.

Autocontenido: lee datos/ del repo (hex/texto). Ejecutar:
    python3 scripts/fase32_h3.py
Salida: resultados/H3_RESULTADOS.json + resumen en stdout.
"""
import hashlib, json, os, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FALLBACK = Path('/home/z/my-project')

def find(name, *roots):
    for r in roots:
        p = Path(r) / name
        if p.exists():
            return p
    raise FileNotFoundError(name)

# ---- materiales ----
HEX = find('datos/fase32_plaintext_2422b.hex', ROOT, FALLBACK / 'repo_push', FALLBACK / 'download')
PT = bytes.fromhex(HEX.read_text().strip())
assert len(PT) == 2422, len(PT)
SHA_PT = hashlib.sha256(PT).hexdigest()
assert SHA_PT == 'b82afeb86f9e50848220f9b64b744b821400308aea273a1c949b9d2d0e408a34', SHA_PT

P60 = find('datos/payload60_letters.txt', ROOT, FALLBACK / 'repo_push').read_text().strip()
P60D = find('datos/payload60_digits.txt', ROOT, FALLBACK / 'repo_push').read_text().strip()
DBBI = find('datos/DBBI_91.txt', ROOT, FALLBACK / 'repo_push').read_text().strip()
FAED = find('datos/FAED_570.txt', ROOT, FALLBACK / 'repo_push').read_text().strip()
assert len(P60) == 60 and len(P60D) == 60 and len(DBBI) == 91 and len(FAED) == 570

TARGETS = {'payload60_letras': P60, 'payload60_digitos': P60D, 'dbbi_91': DBBI, 'faed_570': FAED}

# ---- cuadrícula ----
W = 14                       # columnas (ancho del tablero del póster)
R = len(PT) // W             # 173 filas exactas: 2422 = 14 × 173
assert R * W == len(PT)

def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False] if n >= 1 else [False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = [False] * len(sieve[i*i::i])
    return [i for i in range(n + 1) if sieve[i]]

def printable(b):
    return sum(32 <= c < 127 for c in b) / max(1, len(b))

def compare(out, name, meta):
    """Comparación estructural contra los 4 materiales: exacta / contiene / contenida / hex."""
    txt = out.decode('latin-1')
    res = {}
    for tname, t in TARGETS.items():
        res[tname] = {
            'exacta': txt == t,
            'contiene_objetivo': t in txt,
            'contenida_en_objetivo': len(txt) <= len(t) and txt in t if txt.isprintable() else False,
            'solo_letras': ''.join(chr(c) for c in out if 97 <= c <= 122),
            'solo_digitos': ''.join(chr(c) for c in out if 48 <= c <= 57),
        }
        res[tname]['letras_igual_objetivo'] = res[tname]['solo_letras'] == t
        res[tname]['digitos_igual_objetivo'] = res[tname]['solo_digitos'] == t
        res[tname]['objetivo_en_letras'] = t in res[tname]['solo_letras']
    hits = [tn for tn, r in res.items() if r['exacta'] or r['letras_igual_objetivo'] or r['digitos_igual_objetivo']]
    contain = [tn for tn, r in res.items() if r['contiene_objetivo'] or r['objetivo_en_letras']]
    return {'resumen': res, 'coincidencias_exactas': hits, 'contenciones_parciales': contain,
            'hex': out.hex()[:64] + ('…' if len(out) > 32 else ''),
            'sha256': hashlib.sha256(out).hexdigest()}

# ---- variantes ----
variants = []
for direccion in ('directo', 'inverso'):
    src = PT if direccion == 'directo' else PT[::-1]
    grid = [src[r*W:(r+1)*W] for r in range(R)]      # volcado por filas (row-major)
    for base in (1, 0):
        pr_rows = [i for i in primes_upto(R if base == 1 else R - 1)] if base == 1 else \
                  [i - 1 for i in primes_upto(R - 1) if i - 1 >= 0]
        # filas primas: 1-based → filas 2,3,5,…,173; 0-based → índices 2,3,5,…,171
        row_idx = [p - base for p in primes_upto(R) if 0 <= p - base < R] if base == 0 else \
                  [p - 1 for p in primes_upto(R) if 1 <= p <= R]
        col_idx = [p - 1 for p in primes_upto(W) if 1 <= p <= W] if base == 1 else \
                  [p for p in primes_upto(W - 1)]
        pos_idx = [p - 1 for p in primes_upto(len(src)) if 1 <= p <= len(src)] if base == 1 else \
                  [p for p in primes_upto(len(src) - 1)]
        def mk(label, extract):
            out = extract()
            v = {'nombre': f'{label}_{base}based_{direccion}', 'modo': label,
                 'indexacion': f'{base}-based', 'direccion': direccion,
                 'longitud': len(out), 'imprimible': round(printable(out), 4)}
            v.update(compare(out, v['nombre'], v))
            variants.append(v)
        mk('filas_primas',  lambda: b''.join(grid[i] for i in row_idx))
        mk('columnas_primas', lambda: b''.join(bytes(g[c] for g in grid) for c in col_idx))
        mk('celdas_ambas_primas', lambda: bytes(g[c] for g in (grid[i] for i in row_idx) for c in col_idx))
        mk('posiciones_globales_primas', lambda: bytes(src[i] for i in pos_idx))

# ---- control positivo del comparador (auto-prueba) ----
ctrl = compare(P60.encode(), 'control', {})
# auto-prueba dura: el propio material como objetivo se detecta exacto
selftest = (ctrl['coincidencias_exactas'] == ['payload60_letras'])
assert selftest, 'control del comparador falló'

total = len(variants)
exact = [v for v in variants if v['coincidencias_exactas']]
contain = [v for v in variants if v['contenciones_parciales']]

resultado = {
    'sesion': 'L-errata-consolidacion', 'fecha': '2026-11-23',
    'hipotesis': 'H3 (FASE32_HIPOTESIS.md): 2422 B en cuadrícula 14 columnas, extracción prima',
    'input': {'bytes': len(PT), 'sha256': SHA_PT, 'filas': R, 'columnas': W,
              'identidad_aritmetica': f'2422 = {W} × {R}; 173 es el primo nº {primes_upto(173).index(173)+1}'},
    'variantes_totales': total,
    'espacio': 'filas/columnas/celdas/posiciones × {1-based, 0-based} × {directo, inverso} '
               '(16 ≥ las 14 variantes declaradas) + filtros solo-letras/solo-dígitos',
    'objetivos': {k: {'longitud': len(v), 'sha256': hashlib.sha256(v.encode()).hexdigest()} for k, v in TARGETS.items()},
    'control_comparador': 'OK (auto-prueba exacta: payload60 detectado contra sí mismo)',
    'coincidencias_exactas': [v['nombre'] for v in exact],
    'contenciones_parciales': {v['nombre']: v['contenciones_parciales'] for v in contain},
    'veredicto': 'POSITIVA (escalar a contraseña)' if exact else
                 ('EXAMINAR (contención parcial sin exactitud)' if contain else 'NEGATIVA'),
    'variantes': [{k: v[k] for k in ('nombre', 'modo', 'indexacion', 'direccion', 'longitud',
                                     'imprimible', 'coincidencias_exactas', 'contenciones_parciales')} for v in variants],
}

OUTJSON = ROOT / 'resultados' / 'H3_RESULTADOS.json'
OUTJSON.parent.mkdir(parents=True, exist_ok=True)
OUTJSON.write_text(json.dumps(resultado, indent=1, ensure_ascii=False))
print(json.dumps({k: resultado[k] for k in ('input', 'variantes_totales', 'coincidencias_exactas',
                                            'contenciones_parciales', 'control_comparador', 'veredicto')},
                 indent=1, ensure_ascii=False))
print('OK →', str(OUTJSON))
