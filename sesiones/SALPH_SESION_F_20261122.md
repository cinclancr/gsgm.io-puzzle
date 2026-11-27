# SALPH_SESION_F_20261122.md — Sesión F: «matrix sum list» como lista de posiciones + relecturas estructurales del Bifid-570

**Investigador:** principal independiente. **Fecha:** 2026-11-22 (continuación sin reinicio).
**Alcance:** solo materiales públicos del puzzle GSMG (caso 2, SalPhaseIon). Ninguna clave privada ajena.
**Veredicto global:** **NEGATIVO reproducible** — 792 ensayos AES propios nuevos (156 F + 360 FH/FI + 276 FJ)
bajo la convención canónica (`sha256hex(answer)` + EVP_BytesToKey/SHA-256, AES-256-CBC) con controles
positivo/negativo (fase 2 / `causality`) en cada batería, puerta L5 sobre ~400 formas y contraste MD5.
0 autenticos; 0 L5; los 5 padding-válidos del lote son el ruido clásico (imprimible 0.28–0.33).
**El sobre SalPhaseIon sigue CERRADO; DBBI/FAED siguen sin lectura final.**

---

## 1. Reproducción y verificación de partida (nivel A)

1. **Parse exacto de la página** (`salphaseion_g1_parse.py`, 1075 chars):
   - dbbi(91) | matrixsumlist(104 bits a/b) | faed(570) | z | lastwordsbeforearchichoice(63) | z |
     thispassword(29) | z | shabefourfirsthintisyourlastcommand(35) | b64(64) | enter(40 bits) | b64(64) | shabefanstoo(12).
   - Los cuatro campos internos re-verificados como AUTO-ETIQUETAS: `matrixsumlist` (13 B),
     `enter` (5 B), `lastwordsbeforearchichoice` (26 B), `thispassword` (12 B).
   - Sobre: 96 B, sal `3ab585348552415d`, sha256 `9e2831e1…4fa7a258` — byte a byte idéntico al blob local.
2. **Bifid-570 re-verificado** (`salphaseion_g3/g4`): cuadro por primera aparición de dbbi
   (`DBIFH/CEGAK/LMNOP/QRSTU/VWXYZ`), período 570 → `BTCSEED`(7) + M91(91, única Z en la posición
   0-based 97) + R472(472). Rieles: **selector (285, 100% b/c/d/e — forzado por el cuadro)** y
   **payload (285, alfabeto de 24 letras sin j)**. El riel payload contiene 13 I y 16 O;
   sin I/O → **payload256 = 256 letras = 2^8** (dato estructural registrado de nuevo).
   El riel payload comienza `TSEDOMKAHS` (invertido: `SHAKMODEST` — extremo ya certificado por 070).

## 2. F-A/FA2 — «matrix sum list» como LISTA DE POSICIONES (nuevo, negativo)

Premisa (nivel B, definiciones del creador 2023): *matrixsumlist = la escena del Arquitecto donde
«Matrix» aparece 9 veces y «sum» una vez («our life is the sum of a remainder of an unbalanced equation»)*.
Lectura nueva: la «matrix sum list» = la lista de posiciones de matrix(9)+sum(1).

**Hechos exactos (nivel R):**
- Diálogo del Arquitecto en la película (Scott Manning, 3847 letras): `matrix` en
  **[34, 392, 703, 949, 1545, 2415, 2549, 3120, 3383]** (9×) y `sum` en **[326]** (1×).
  Lista natural: suma **15416**.
- Monólogo del puzzle (1539 letras): `matrix` **0 veces** — el creador reemplazó
  «inherent to the programming of THE MATRIX» por «…OF THIS PUZZLE» (edit certificado en esta sesión);
  `sum` 1× en [13].
- El pasaje «WHAT A WISEMAN ABOVE HINTED AT IS WORTH HUNDRED FOURTY OF THE INVESTMENT…» del puzzle
  ocupa el lugar del «nearly 99% of all test subjects…» de la película (inserto del creador; el
  «140 caracteres / 23 palabras» de la cita Fresco ya fue re-chequeado por GSMG-CLEAN 14 §3).
- Ensayos: selecciones de letras en las posiciones (film/puzzle, 0/1-based), lista concatenada,
  ordenada, restos mod 1539/570/91/104, sumas acumuladas, spans entre posiciones consecutivas —
  todo por L5 + AES (156+ ensayos). **0 auténticos.**

## 3. F-B — sumas modulares del DBBI 7×13 («suma de un resto») — negativo

Lectura abierta en GSMG-CLEAN 09 §5 (diagonales/anillos/bloques/sumas modulares). Ejecutadas:
sumas de filas/columnas del 7×13 y 13×7 crudas y mod {9, 10, 7, 13, 26, 11}; diagonales y
antidiagonales; letras a1z26 de las sumas; 78 formas → 156 ensayos. **0 auténticos (1 pad-valido
ruido md5, imprimible 0.32).** Las lecturas modulares rectas del 7×13 quedan cerradas.

## 4. F-C — los 30 pares del payload60 como libro de cifras — negativo

Pairs `[49,68,33,79,81,55,98,77,57,52,75,88,58,86,16,48,66,34,26,33,37,65,77,53,43,96,66,79,75,51]`
como índices sobre monólogo(1539)/dbbi(91)/faed(570)/bif(570)/texto film(3847), 0/1-based, directos e
invertidos, y como letras a1z26. Incluido en la batería F. **0 auténticos.**

## 5. F-D — riel selector como primos 2/3/5/7 — negativo

El selector (285 letras b/c/d/e) mapeado a los «prime basics» 2/3/5/7 como flujo de índices
acumulativos sobre monólogo/payload/dbbi y como concatenado de dígitos. La lectura de
bit-posiciones 2/3/5/7 ya estaba cerrada (gsmgiopuzzle 072); esta es la lectura índice/salto.
**0 auténticos.**

## 6. FH — matriz 11×11 COMPLETA con los pares reinsertados — negativo

Completando N55/N56 (que probaron ceros y primos como relleno de las 30 celdas primas):
las 30 celdas primas de la 11×11 rellenas con los 30 pares del payload60 (orden natural,
inverso y suma-de-par). Sumas de filas/columnas (p. ej. filas [335,262,225,278,108,139,132,176,139,350,99],
total 2243) → formas crudas/mod10/a1z26/letras-dígitos/selección del monólogo. 180 formas →
360 ensayos. **0 auténticos; 0 pad-validos.** La contabilidad decisiva de N55 se mantiene:
422+1821=2243 ≠ ninguna suma de cobertura canónica.

## 7. FI — listas como CLAVES de cifrado (abierto en 09 §5) — negativo

payload60(60 dígitos), los 30 pares, y las sumas del póster (filas/col) como claves
Vigenère/Beaufort sobre bif570/pay285/M91/R472/dbbi/faed en alfabeto cuadro(25) y a-z(26).
**0 auténticos.** «Lists used as cipher keys» queda cerrado en su forma clásica directa.

## 8. FJ — batería final estructural — negativo

- Selector/payload como matrices 15×19 / 19×15 / 16×16 (payload256) con valores primos 2/3/5/7 y
  posiciones de cuadro → sumas → formas. La 16×16 del payload256 (suma de posiciones 2845) incluida.
- Bits del selector (570) a bytes: 71/70 bytes, imprimible 31–46% en ambas polaridades y direcciones — ruido.
- **Respuestas de Neo (AnsToo = «respuesta de Neo», def. creador 2023)**: 19 respuestas canónicas
  (`bullshit`/`BULLSHIT`, `no`, `trinity`, `the oracle`, `choice the problem is choice`,
  `if I were you…`, `we won't meet again`, `you haven't answered my question`, …) — **`bullshit`
  nunca había sido probado bajo la convención canónica** (verificado contra CANDIDATOS_AES.csv).
- Composites lastwords+firsthint (`humph hope…` + `followthewhiterabbit`, + sha256hex(followthewhiterabbit),
  + rosa) y la frase Humph-Hope completa en 3 formas.
- 138 formas → 276 ensayos + contraste Cosmic. **0 auténticos (4 pad-validos ruido ≤0.33).**

## 9. Hechos estructurales nuevos de la sesión (nivel R)

1. **La «matrix sum list» cinematográfica** = posiciones [34, 392, 703, 949, 1545, 2415, 2549, 3120, 3383, 326]
   (suma 15416) sobre las 3847 letras del diálogo del Arquitecto; en el monólogo del puzzle
   «matrix» fue reemplazado por «this puzzle» — el propio texto del puzzle apunta al monólogo
   MODIFICADO como campo de la operación.
2. El pasaje insertado por el creador («wise man above … hundred fourty of the investment») reemplaza
   al «nearly 99% of all test subjects» de la película — región de máxima concentración de edits del creador.
3. El extremo del riel payload (`TSEDOMKAHS` ↔ `SHAKMODEST` invertido) es el complemento del encabezado
   `BTCSEED`: el creador diseñó la primera decena del riel payload para leerse al revés.
4. payload256 = 256 letras (= 2^8) tras eliminar I/O del riel payload — coincide con la pista
   «yinyang/superposiciones» (I/O = yin/yang; «zeroed out» ↔ 'o'=0) como objeto abierto.

## 10. Estado de los frentes tras la sesión F

| Frente | Estado |
|---|---|
| matrixsumlist como posición-lista (film/puzzle) | **CERRADO (negativo)** |
| matrixsumlist como sumas modulares del 7×13 | **CERRADO (negativo)** |
| pares payload60 como libro de cifras | **CERRADO (negativo)** |
| selector como primos-índice (2/3/5/7) | **CERRADO (negativo)** |
| 11×11 con pares reinsertados | **CERRADO (negativo)** |
| listas como claves clásicas | **CERRADO (negativo)** |
| respuestas de Neo (incl. bullshit) | **CERRADO (negativo)** |
| bits del selector como bytes | **CERRADO (ruido)** |
| payload256 (16×16, sin I/O) como objeto yinyang | ABIERTO — siguiente lectura estructural |
| «hundred fourty»/«wise man above» como puntero | ABIERTO (nivel C) |

**Prioridad declarada para la próxima sesión:** antes de otra contraseña SHA-256, identificar la
operación real de `matrixsumlist` sobre el monólogo MODIFICADO del puzzle (el texto al que el propio
texto apunta al sustituir «the matrix» por «this puzzle»): la zona de edits del creador
(«wise man above / hundred fourty / take the private key») es la única región del monólogo con
instrucciones nuevas del creador y aún no tiene una regla de operación verificable.

## 11. Archivos reproducibles

- `scripts/salphaseion_g1_parse.py` — parse exacto + auto-etiquetas + sobre.
- `scripts/salphaseion_g2_faed.py`, `g3_bifid_full.py`, `g4_rails.py` — rieles y estructura Bifid.
- `scripts/salphaseion_g5_tokens.py` — estructura de tokens L5 de dbbi (64/16; chi² 23.5, p≈0.078 uniforme).
- `scripts/salphaseion_g6_payload.py` — riel payload: dígitos a-i, segmentos, coordenadas base-5.
- `scripts/salphaseion_fa_matrixsum.py`, `fa2_diff.py` — listas matrix/sum + diff film/puzzle.
- `scripts/salphaseion_f_bateria.py`, `fh_fi.py`, `fj_bateria.py` — baterías F (792 ensayos).
- `download/SALPH_FA_MATRIXSUMLIST.json`, `SALPH_FA2_DIFF.json`, `SALPH_F_BATERIA.json`,
  `SALPH_FH_FI_RESULTADOS.json`, `SALPH_FJ_BATERIA.json`, `SALPH_G6_PAYLOAD.json`.

**Contabilidad acumulada propia:** 7.738 (previa) + 792 (sesión F) = **8.530 ensayos AES**, todos negativos.
