# SalPhaseIon — sesión C: códecs de la página sobre la salida Bifid y preimágenes nuevas (2026-11-22)

**Alcance exclusivo:** SalPhaseIon. Ninguna clave privada de carteras ajenas se investiga.
Continúa la sesión B («Integración de la sesión B y nueva prueba») por las dos líneas acordadas,
sin mezclarlas. Niveles: R = reproducido aquí; NEG = negativo acotado; HECHO = aritmética
exacta con calificación honesta; CAL = calibración verificada contra datos reales.

**Estado tras esta sesión: SalPhaseIon sigue sin resolverse.** Se cierran tres familias nuevas
con controles; ninguna produce texto legible, hex64, WIF, coincidencia L5 ni padding autenticado.

---

## 0. Integridad y calibración [R/CAL]

| pieza | SHA-256 (verificado) |
|---|---|
| DBBI (91) | `71fe4625…b6a2c5ca` |
| FAED (570) | `066191b4…1d5ef3c2` |
| Sobre (96 B, `Salted__`, sal `3ab585348552415d`, 80 B ct) | `9e2831e1…4fa7a258` |

- Autotest AES: la fase 3.2 real abre con sha256hex + EVP_BytesToKey/SHA-256 (2422 B, pad 10) ✓.
- **Calibración del códec decimal de la página [CAL]:** a..i=1..9, o=0 → entero → hex → bytes
  (big-endian). Reproduce byte a byte los campos reales: [766:829] → `lastwordsbeforearchichoice`,
  [830:859] → `thispassword`. La segmentación decimal por códigos ASCII da **0** variantes
  completas → el códec bigint queda fijado sin ambigüedad.
- Códec binario a/b (a=0, b=1, 8 bits): reproduce `matrixsumlist` (104 bits) y `enter` (40 bits) ✓.
- Bifid (cuadro de primeras apariciones DBIFHCEGA…, período 570): `btcseed` + bloque-91 (única Z
  en 98) + bloque-472 reproducido ✓.

## 1. Línea 2 — códecs de la propia página sobre `BTCSEED | M91 | R472` [NEG]

**Motivo de la prueba (hueco real):** el laboratorio del repo elimina la `o` antes de mapear
(`replace(/[^a-i]/g,'')`), y el argumento de H2 («faed crudo no puede ser decimal FIELD») solo
cubre el texto crudo. La salida Bifid sí contiene `o` (el riel par), de modo que aplicar el códec
decimal demostrado (con o=0) a los campos etiquetados era una lectura del idiom no probada.

**Objetos:** bifid570, M91, M91z, M90, R472, cola-563, riel impar 285, riel par 285,
portador 282, compañero 281.

| códec | dígitos retenidos (bifid570 / M91 / R472) | salida | objetivo |
|---|---|---|---|
| decimal a–i/o (o=0) | 403 / 64 / 334 | 168 / 27 / 139 bytes, imprimible 0,36–0,47 | ninguna palabra objetivo |
| sq10 (valores del cuadro, issue #106) | 396 / 65 / 326 | 165 / 27 / 136 bytes, imprimible 0,26–0,41 | ninguna |
| binario a/b | 81 / 10 / 70 bits | ≤10 bytes, imprimible 0,0–0,4 | ninguna |

**Controles:** 12 combinaciones objeto×códec × 2.000 permutaciones (multiconjunto conservado):
p(imprimible ≥ real) entre 0,044 y 0,91; **ninguna salida real** contiene palabra objetivo, y
solo 4/24.000 controles barajados contienen alguna (palabras cortas del léxico de búsqueda a
ritmo 0,02% — la comparación relevante es que el dato real contiene cero); el mínimo 0,044
(bifid570 decimal) no es significativo tras 12 pruebas múltiples. Las corrientes de dígitos no
coinciden con `payload60_digits` ni `digits149`.

**Conclusión [NEG]:** bajo los códecs demostrados por la propia página, el campo colgado de la
etiqueta `BTCSEED` no se decodifica como texto. La lectura «BTCSEED etiqueta una semilla» no
obtiene soporte de estos códecs; la división 7|91|472 sigue siendo estructura reproducible sin
operación conocida.

## 2. Línea 2 — puente columnario 7×13 con la clave `matrixsumlist` [NEG]

91 = 7×13 y `matrixsumlist` tiene exactamente 13 letras: la clave ordena las 13 columnas de
DBBI (empates por posición y por posición inversa). Se probaron 9 transformaciones (leer
columnas, leer filas 13×7, inversa de escritura, y las mismas sobre M91) contra 15 objetivos
(M91, M91z, M90, DBBI, extremos de FAED, R472, hill-282, etiquetas, VIC, payload60).

- Mejor coincidencia real: 16/91 (y solo contra objetivos de estructura interna, no contra M91).
- **Control Monte Carlo (20.000 órdenes aleatorios de columnas):** media 7,08, máximo 15,
  orden de la clave → M91 = 9, p(≥clave) = 0,25.

**Conclusión [NEG]:** no existe puente columnario DBBI↔M91 bajo esta clave. La vía
transposición-clave queda cerrada en su forma directa.

## 3. Línea 1 — preimágenes nuevas del patrón L5 [NEG]

Espacios no cubiertos ni por el back-check de 16,8 M cadenas (2026-09-13) ni por el barrido de
substrings de `l5_sweep.py`:

1. **sha256 de ARCHIVOS completos:** 2.575 archivos del corpus (bytes exactos) + formas de texto
   (strip / lower / compacto / compacto-lower) = **7.559 hashes** → 0 coincidencias del patrón.
2. **Respuesta de 7 partes de la fase 3** (`seven_part_phase3_answer.json`): concatenaciones con
   separadores `''`/espacio/salto/`z`, orden directo e inverso, partes sueltas, mayúsculas y
   minúsculas → 0.
3. **Flujos del mapa de ediciones alineado (v2, 24 filas):** spans fuente, spans del puzzle,
   inserciones puras, reemplazos, por fila, con formas lower/compacto → 0.
4. Textos cósmico/cadena-4/onda como piezas → 0. Total: **953 piezas construidas, 0 L5**.

**Conclusión [NEG]:** si DBBI es un sha256 sustituido, su preimagen no es un archivo completo del
corpus, ni la respuesta de 7 partes, ni ningún flujo diferencial del mapa de ediciones. Esto
refuerza la lectura de la sesión B: la preimagen, de existir, es la **salida de una operación**
aún no identificada (coherente con 15 §4 del corpus: «la operación sigue siendo desconocida»).

## 4. AES sobre el sobre SalPhaseIon — candidatos nuevos [NEG]

56 candidatos nuevos (salidas de códecs 100% imprimibles — ninguna lo fue, así que la familia
(i) quedó vacía por diseño; corrientes de dígitos con o=0 y sq10 como P3 de la receta de 4
piezas y sueltas; salidas columnarias; flujos del mapa de ediciones; 7 partes) × 3 formas de
contraseña {directa, sha256hex, sha256raw} × 2 KDF {SHA-256, MD5} = **336 ensayos**.

- **4 padding-válidos, todos pad=1**, imprimible 0,30–0,38, 0 hex64, 0 WIF (esperados ≈1,3 por
  azar a 1/256; los 4 son indistinguibles del ruido ya documentado).
- 0 coincidencias L5 entre los candidatos. 0 legibles.

**Conclusión [NEG]:** la familia queda cerrada bajo ambos KDF, igual que las 504 de la sesión B.

## 5. Qué queda abierto (frontera honesta, sin cambio de criterio)

- La **operación** que conecta DBBI / FAED / `matrixsumlist` / «last words before archi choice»
  sigue sin identificarse. Todo lo cerrado aquí y antes son implementaciones concretas
  rechazadas, no la inexistencia de la operación.
- El corpus (GSMG-CLEAN 15 §4) mantiene que el siguiente movimiento debe quedar **dentro** del
  puzzle autenticado («You have all the info», #9607/#16624) y que el objeto interno de mayor
  valor es el **mapa completo fuente→reescritura** (splices, inserciones de CODES/HOPEFULLY/
  BASICS/23-16-7/ACTUAL PRIVATE KEY). Esta sesión añade: los flujos literales de ese mapa
  tampoco son la preimagen L5, de modo que el próximo uso del mapa debe ser **operacional**
  (p. ej. como selector o insumo de transformación), no literal.
- Criterio de victoria (sin cambio): descifrado AES auténtico con validación independiente
  (pad de bloque completo / texto legible / estructura externa) o coincidencia L5 (chance
  16!/16⁶⁴ = 2⁻²¹¹·⁷ por digest).

## 6. Archivos

- `scripts/salphaseion_s5_sesionC.py` (copia: `download/SCRIPTS/`) — batería completa con
  autotests, calibraciones y controles.
- `download/SALPH_S5_SESION_C.json` — auditoría completa (L2a, L2b, L1, AES, esperados por azar).

**SalPhaseIon continúa cerrado: sin contraseña, sin descifrado autenticado, sin preimagen L5.**
