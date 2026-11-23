# H3_INFORME.md — ejecución de la hipótesis H3 (fase 3.2, cuadrícula 14)
**Sesión L (2026-11-23), mandato del usuario: «ejecutar H3». Estado: EJECUTADA →
NEGATIVA. Ninguna clave se reclama; sin AES sin coincidencia estructural previa
(criterio de la propia hipótesis).**

## 1. Hipótesis ejecutada (FASE32_HIPOTESIS.md §H3)

«Return to the source codes» = el texto fuente de fase 3.2; «as wide as the first
one seen» = el tablero 14×14 del póster; «reinserting the prime basics» = marcar
posiciones/filas primas. Transformación: volcar los 2.422 B en una cuadrícula de
14 columnas, extraer los bytes en filas/columnas/posiciones primas y comparar con
payload60/dbbi/faed; solo ante coincidencia exacta escalar a contraseña.

## 2. Verificación del input

- `datos/fase32_plaintext_2422b.hex` → 2.422 B exactos, sha256
  `b82afeb86f9e50848220f9b64b744b821400308aea273a1c949b9d2d0e408a34` ✓ (ancla del artefacto).
- Identidad aritmética: **2.422 = 14 × 173**; 173 es el **40.º primo**; la cuadrícula
  es exactamente 173 filas × 14 columnas sin resto.

## 3. Método (16 variantes, cubre las 14 declaradas y las excede)

Espacio ejecutado: **{filas primas, columnas primas, celdas ambas-primas,
posiciones globales primas} × {1-based, 0-based} × {directo, inverso}** = 16
variantes, con filtros post-hoc **solo-letras** (a–z) y **solo-dígitos** (0–9) por
variante, contra los 4 materiales conocidos:
`payload60` (letras `difhcc…`, 60), `payload60-dígitos` (60), `dbbi_91` (91) y
`faed_570` (570) — todos con longitud y sha256 verificados en el JSON de resultados.

**Control del comparador:** auto-prueba exacta (el payload60 se detecta contra sí
mismo como coincidencia exacta) ✓ — la maquinaria de comparación funciona; un
positivo habría sido detectado.

## 4. Resultado

| Métrica | Valor |
|---|---|
| Variantes ejecutadas | 16 (+ filtros letras/dígitos) |
| Coincidencias exactas (cadena o solo-letras/solo-dígitos) | **0** |
| Contenciones parciales (objetivo ⊂ salida o salida ⊂ objetivo) | **0** |
| Escalación a contraseña (AES) | **No procede** (criterio de la hipótesis) |
| Veredicto | **NEGATIVA** |

Salida completa: `resultados/H3_RESULTADOS.json` (por variante: modo, indexación,
dirección, longitud, imprimible, sha256, coincidencias, contenciones).

## 5. Consecuencia operativa (mandato del usuario)

El mandato decía: «continuar con la resolución del selector de 35 bloques
únicamente si la evidencia lo justifica». H3 era la hipótesis formulada pendiente
de mayor evidencia (MEDIA) y **no produjo coincidencia estructural alguna**: no
existe justificación para atacar el selector por esta vía. El frente del selector
(35 bloques → d) queda como en la auditoría L §7: PENDIENTE, requiere premisa nueva
con control positivo o material nuevo del creador. H5 (segunda lectura EBCDIC)
queda formulada-pendiente con probabilidad BAJA (no ejecutada; su espacio de
codepages CP273/CP037/CP500/CP1026/CP1141 sigue abierto para una sesión futura).

## 6. Registro en el libro mayor de negativas

Entrada **N64** (para el ledger local `PRUEBAS_NEGATIVAS.csv`):

| Campo | Valor |
|---|---|
| ID | N64 |
| Sesión | L-errata (2026-11-23) |
| Objeto | fase 3.2 plaintext 2.422 B en cuadrícula 14×173 con extracción prima (16 variantes) |
| Comparación | payload60 (letras/dígitos), dbbi_91, faed_570 — 0 exactas, 0 parciales |
| Evidencia | `resultados/H3_RESULTADOS.json`, `scripts/fase32_h3.py` |
| Resultado | NEGATIVA |

## 7. Reproducción

```bash
python3 scripts/fase32_h3.py     # 16 variantes + control del comparador → NEGATIVA
```
