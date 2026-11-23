# GSMG.io 5 BTC — carpeta de entregables (estado 2026-11-21d)

Investigador principal independiente. **El puzzle NO está resuelto; ninguna
clave, WIF ni dirección de premio se reclama.** Niveles de evidencia: A
(originales reproducidos) > B (reproducción de fuente secundaria) > C
(hipótesis) > D (coincidencia posterior).

## Informes de estado y hallazgos
- `ESTADO_GSMG.md` — estado completo de la investigación (actualizado 2026-11-21d).
- `HALLAZGOS_NUEVOS.md` — hallazgos por sesión (H1–H14).
- `report.md` — informe de la sesión 2026-11-21 (+adendum b de enlaces).

## Conciliación de la búsqueda AES (experimentos 2 y 5)
- `MANIFEST_AES_7194.json` — manifest de la ronda de 7.194 AES: 4 lotes,
  procedencia, KDF probado, deduplicación (3.084 filas conservadas, 2.976
  tuplas únicas, 108 duplicados), reglas de validación final.
- `PRUEBAS_NEGATIVAS.csv` — libro mayor de negativas (N01–N35; entrecomillado reparado 2026-11-21d).
- `CANDIDATOS_AES.csv` — 1.227 filas de intentos AES (E9 + E-P60 + E13).
- `candidates.csv` (1.974 filas), `candidates_links.csv` (72),
  `candidates_summary.json`, `candidates_links_summary.json`,
  `E_P60_BATERIA.json`.

## Menú de cifrados, matrixsumlist-2 y puerta no textual (fase 2, 2026-11-21d)
- `E14_ETOOL_MENU.json` — 3.963 decodificaciones del menú de ciphertools.co.uk
  (12/12 controles de ida-y-vuelto); negativo; Hill de floflo refutado.
- `E15_MATRIXSUMLIST2.json` — sumas del payload + segundas lecturas binarias
  bajo la transformación certificada del creador; negativo (4/4 controles).
- `E16_PUERTA_NOTEXTUAL.json` — puerta 1NULY con 24 preimágenes no textuales
  (bitmap del conejo 13×14/37 bloques, BIN bytes, BTCSEED…): 144 derivaciones, 0.

## Auditoría de la regla color→token (experimento 1)
- `E10_AUDITORIA_COLOR_TOKEN.json` — espacio completo de 384 reglas
  «24 colores reales → tokens b/be»: **1 única regla completa** (F→B y residuo
  BY forzados por exactitud estructural); 11/11 controles del canal de color.

## Transformación payload60 → objeto canónico (experimento 3)
- `E12_TRANSFORMACION.json` — familias T1–T11 con 6/6 controles positivos
  (etiquetas, VIC-149, Bifid-faed, Beaufort, sumas de matriz): sin objeto
  canónico; sin pruebas AES (disciplina del experimento 5).

## lastwordsbeforearchichoice sobre textos auténticos (experimento 4)
- `E13_LASTWORDS.json` — inventario de fronteras (monólogo/VIC/3.2/fase 2/
  estructura SalPhaseIon), 39 candidatos nuevos, 117 AES de validación final:
  negativo.

## Imagen y verificación (sesión c)
- `E3_PNG_AUDIT.json`, `E3_VERIFICACION.json` — forense del PNG y segunda
  extracción reproducible.
- `DIRECCIONES_CANDIDATAS.txt` — direcciones y puertas (validación en cadena).
- `manifest.json` — inventario A de artefactos + 33/33 controles históricos.
- `negative_ledger.csv` — ledger previo (N01–N16).

## Scripts reproducibles
- `SCRIPTS/` y `scripts/` — todos los experimentos E1–E13 + reparación del ledger (fuente auditable).
