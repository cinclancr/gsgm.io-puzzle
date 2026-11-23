# GSMG.io — 5 BTC Puzzle · Repositorio de investigación forense independiente

**Estado del puzzle: NO RESUELTO.** Ninguna clave, WIF ni dirección de premio se reclama.
Este repositorio consolida una línea de investigación independiente (criptoanálisis
forense, verificación documental y criptográfica) sobre el challenge GSMG.io 5 BTC.

Mantenedor: `cinclancr` (investigador principal). Consolidación inicial: 2026-11-23.

---

## 1. Qué es este repositorio

Consolidación de la investigación acumulada (sesiones 2026-11-21 → 2026-11-23, sesiones
B–L) sobre materiales upstream del puzzle, con reglas de validación estrictas:

- **Niveles de evidencia:** A = originales reproducidos; B = reproducción independiente
  de fuente secundaria; C = hipótesis explícita; D = coincidencia posterior.
- **Estándar de tres partes (obligatorio):** *Reproducción* (la operación reproduce los
  mismos bytes) ≠ *Autenticación* (evidencia independiente enlaza esos bytes con la
  transformación esperada por el puzzle) ≠ *Solución* (el resultado satisface la prueba
  criptográfica final). Un hash igual a uno publicado NO es autenticación por sí solo.
- **Prohibiciones:** fuerza bruta sobre ECDLP/SHA-256/HASH160; promover direcciones
  «válidas» sin regla de origen y control positivo; repetir familias de hipótesis ya
  cerradas como negativas (ver `negativos/PRUEBAS_NEGATIVAS.csv`).

## 2. Hechos verificados (resumen)

| Objeto | Estado | Evidencia |
|---|---|---|
| Cadena pública (fases 0–3.2, rosa) | VERIFICADA (33/33 controles) | corpus upstream |
| Cadena 1→4 (7 eslabones AES) | VERIFICADA como descifrado, byte a byte | `resultados/CADENA_1_4_REPRODUCCION.json` |
| Texto fase 3.2 (2.422 B, sha256 b82afeb8…) | VERIFICADO | `datos/fase32_plaintext_2422b.hex` |
| Censo de sobres (81 únicos) | REPRODUCIDO | sesiones K/L (auditoría) |
| 35 bloques de 32 B (cadena 4) como claves | NO AUTENTICADO; selector ABIERTO | 0/310 direcciones, 0/~10.086 candidatos |
| urlblob (112 B) | CERRADO como frente (~1,77 M descifrados = 0) | sesiones K/L |

El frente real del puzzle: la **regla selectora final** (35 bloques de 32 B → d) o
material nuevo del creador (libro Time-Life «Cosmic Duality», /TheArchitectChoice).

## 3. Estructura

```
README.md            — este archivo
CHANGELOG.md         — cronología de sesiones y eventos del repositorio
REPRODUCIBILITY.md   — entorno, hashes de artefactos, cómo re-ejecutar
SOURCES.md           — fuentes upstream, procedencia y licencias
SECURITY.md          — política de seguridad y límites declarados
docs/                — documentos maestros: ESTADO_GSMG, HALLAZGOS, auditorías (K/L),
                       hipótesis, erratas y correcciones
sesiones/            — informes de sesión B–L (diario de investigación)
negativos/           — libro mayor de pruebas negativas (N01–N63)
datos/               — materiales del puzzle en forma textual verificable (hex/texto)
scripts/            — scripts reproducibles (verificación, auditoría, hipótesis)
resultados/         — JSON de resultados clave
indice/              — índice del corpus local completo (anclajes SHA-256)
.github/workflows/  — CI (verificación de hashes y consistencia, sin escaneos cripto)
```

## 4. Procedencia

Este repositorio NO es un fork git de terceros: es un repositorio de consolidación
propio. Los materiales upstream (Naddiseo/gsmgio-5btc-puzzle, puzzlehunt/…,
floflo777/open-crypto-puzzles, jackdevs66/GSMG5_CDuality, web/archivos) se citan con
procedencia y hash en `SOURCES.md`; sus licencias se respetan y NO se rehospedan
bloques binarios de terceros (ver `indice/CORPUS_INDICE.md` para la localización
local de cada artefacto).

## 5. Reproducción rápida

```bash
python3 scripts/verifica_hashes.py        # hashes de artefactos embebidos (hex)
python3 scripts/l_errata_evidence.py      # evidencia de la errata de la auditoría L
python3 scripts/fase32_h3.py               # ejecución de la hipótesis H3 (14 variantes)
```

Detalles y dependencias: `REPRODUCIBILITY.md`.
