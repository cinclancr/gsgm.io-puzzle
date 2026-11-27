# SESIÓN 2026-11-22 (continuación) — L5 masivo, palabras de película, nido del conejo

**Investigador:** principal independiente. **Puzzle GSMG.io 5 BTC: NO RESUELTO.**
Continúa la auditoría del paquete de transferencia 21-nov y la lista de conflictos.

Niveles: R = reproducido aquí; D = documentado; P = público; C = hipótesis; NEG = negativo acotado.

---

## G1. Barrido masivo L5 del patrón DBBI — nivel R (NUEVO, NEGATIVO DECISIVO)

La hipótesis L5 (GSMG-CLEAN, lead 2, exacto): DBBI tokenizada con la regla "b/g inician
tokens de 2 caracteres" produce exactamente 64 tokens / 16 códigos — la forma de un sha256
hex digest sustituido. Verificador: `eq_pattern(sha256(answer)) == DBBI_PATTERN`
(coincidencia casual 2⁻²¹¹·⁷). Control reproducido aquí: la tokenización regenera el patrón
`01234556728966286abc61c88b48de3086dd501d5557d6bab5605233df7bbb96` desde DBBI ✓.

**Espacio barrido en esta sesión (complementario al back-check previo de 16,8M cadenas):**

| fuente | substrings |
|---|---:|
| arquitecto 1539 (GSMG, minúsculas) | 531.186 |
| arquitecto readable (mayúsculas + minúsculas, espacios) | 1.328.362 |
| Scott Manning transcript (raw / lower / compact) | 5.482.967 |
| massassi transcript (lower / compact) | 781.693 |
| bifid output (BTCSEED…) | 146.493 |
| sopa compacta 1075 | 346.978 |
| phase2/phase3/phase3.2 plaintexts (+ lower_compact) | 4.283.233 |
| streams (dbbi, faed, payload60, digits149, vic, checkerboard, hill, dbbi−vic, msg8446) | 102.681 |
| creator hints compilados (raw + lower) | 14.455.564 |
| telegram: 56.477 mensajes completos | 56.477 |
| telegram: substrings de mensajes del creador (Jrk Bgrt) | 2.915.674 |
| extracciones no contiguas (cada k-ésima, primas/no-primas, mitades) + 80 frases de pista | 80 |

**TOTAL: 30.522.837 substrings en 45,5 s — 0 coincidencias.**

**Veredicto (NEG, decisivo):** si DBBI = sha256(answer) sustituido, el answer NO es ningún
substring contiguo (longitud 4-400) de ningún texto canónico disponible — ni extracción
no contigua simple (cada k-ésima letra, posiciones primas, mitades) ni frase específica de
las pistas del creador ("follow the white rabbit", poema #1710 completo, "wewont", "hush
hush", 23/16/7, etc.). Junto al back-check previo (16,8M cadenas): **~47M cadenas, 0 matches**.
El answer, si L5 es verdadero, requiere: una transformación no generada mecánicamente, una
combinación no contigua, o material no disponible (libro Time-Life, página previa a
/TheArchitectChoice, urlblob completo).

## G2. Batería AES con frases canónicas de la película — nivel R (NUEVO, NEGATIVO)

Resolución del conflicto #12 (secuencia canónica verificada contra dos transcripts):

1. El discurso de las dos puertas del Arquitecto TERMINA con: "…she is going to die and
   there is nothing you can do to stop it. **Hope: it is the quintessential human
   delusion, simultaneously the source of your greatest strength and your greatest
   weakness.**"
2. Neo: "If I were you, I would hope that we don't meet again."
3. Arquitecto: **"We won't."** ← última línea antes de que Neo cruce la puerta.
4. Neo camina por la puerta izquierda.

"We won't" NO es post-elección (corrección al conflicto #12): es la última palabra del
Arquitecto antes de la ejecución de la elección. Scott Manning añade "Humph." antes de
Hope; massassi no.

**Batería:** 72 frases de la película (ending completo, dos-puertas, momento de la verdad,
cadena de reacción, predecesores/love/Trinity, niveles de supervivencia) × 3 formas
(raw/sha256hex/sha256raw) × 2 KDF (EVP-SHA-256/EVP-MD5) × 3 blobs = **1.296 trials:
0 aperturas auténticas** (3 padding-válidos = falsos positivos clásicos pad=1 +
entropía 6,0-7,9). Las "last words before archi choice" canónicas NO abren los AES.

## G3. urlblob recuperado localmente — nivel R (aclaración)

El 4º blob (112 B = `Salted__` + sal `74c974e3f92e64b5` + 96 B ciphertext) SÍ existe
localmente: `scripts/urlblob_battery.py` lo recuperó de URLs capturadas en el CDX de
Wayback. Nota de la librería: "probablemente NO material del creador" (solo visto como URL
en 2026; los 6 sales reales nunca se entregaron como URL); 60 passwords probadas = 0.
El barrido de dominio amplio del CDX sigue bloqueado por el proxy local (limitación
declarada; verificado de nuevo esta sesión — web.archive.org bloqueado por categoría).

## G4. Creador identificado en Telegram — nivel R

**Jrk Bgrt ES el creador**: publicó #8446 (binario 161 B), #1710 (poema rosa), #5966/#5969
("You are at the prime part already???"), #6509 ("unforseen hint"), #225 (sha256 de la
frase flor). Sus 492 mensajes (2.915.674 substrings) quedaron cubiertos por el barrido L5.

**Poema rosa #1710 completo (nivel R):**
> Roses are White but often Red.
> Yellow has a number and so does Blue.
> Go back to the first puzzle piece without further ado.
>
> It might have shown you only one door, beware that the rabbits nest may contain a whole
> lot more.
>
> Hush hush.

## G5. Nido del conejo — bitmap extraído y lecturas — nivel R (NUEVO, NEGATIVO)

Conforme al poema ("the rabbits nest may contain a whole lot more"), extracción directa
del bitmap del conejo desde el póster (7 celdas (6,6)…(8,6), sub-retícula 5×5 de bloques
15×15):

- **37 bloques llenos** confirmados (informe previo ✓), bounding box recortado **13×14**.
- Lecturas probadas: filas→bits→bytes, columnas→bits, 4 orientaciones (rot90/180/270,
  fliph, flipv), contorno, interior — **0 decodificaciones ASCII** (printable 9-27% =
  ruido). El contorno = la figura completa (todas las piezas son borde; sin interior).
- Conteos por fila [2,3,3,3,2,4,5,4,4,5,0,1,1], por columna [4,2,6,3,3,1,4,1,2,2,1,2,2,4]
  (suma 37). Lecturas a1z26 = sin sentido.

**NEG registrado:** el bitmap del conejo no es un canal ASCII/binario directo en las
lecturas estándar. Pendiente con premisa nueva: posiciones de bloques como coordenadas
(37 = primo), lectura del patrón de rayado (4 trazos diagonales superiores), o reglas de
contorno específicas.

## G6. matrixsumlist — hipótesis de sumas de FAED refutada — nivel R (NUEVO, NEG)

Idea estructural nueva probada: payload60 tiene 60 dígitos = 30 pares de 2 dígitos, y
FAED tiene 570 = 30×19 letras exactas. Si payload60 = lista de sumas de filas de la matriz
FAED 30×19, los 30 números de 2 dígitos coincidirían.

**Refutado:** suma total FAED = 3.079; suma de pares del payload = 1.821 (incompatibles
desde la contabilidad). Verificadas TODAS las disposiciones de matriz (30×19, 19×30,
15×38, 38×15, 57×10, 10×57, 6×95, 95×6, 5×114, 114×5, 2×285, 285×2, 3×190, 190×3):
ninguna fila/columna-suma reproduce el payload60. El operador matrixsumlist sigue
desconocido.

## G7. Estado consolidado tras la sesión

**Permanece cerrado/negativo (acumulado):**
- 3 AES finales CERRADOS (~2.000 trials esta sesión sobre convención canónica + MD5 + formas).
- L5: ~47M cadenas sin match (la hipótesis L5 sigue viva pero el answer es inaccesible por
  substrings).
- yin-yang geométrico: refutado bajo modelo nulo (sesión anterior de esta auditoría).
- Frases de película (ambos transcripts): 0 en AES y 0 en L5.
- Bitmap del conejo: sin lectura directa.
- FAED como matrixsumlist: refutado.

**Frentes genuinamente abiertos:**
1. **El operador matrixsumlist** — la transformación que produce el answer desde
   DBBI/FAED (la pista del creador: "You are at the prime part already" = el calendario
   b/be certificado; #6509 "unforeseen hint" = identificado como ese mensaje).
2. **El answer de lastwordsbeforearchichoice** — no es substring de ningún texto
   disponible; requiere el operador de (1) o material no disponible.
3. **Vigilancia on-chain** de 1GSMG1 (más firmas de d_premio) y bc1pwc9 (taproot de P).
4. **Libro Time-Life "Cosmic Duality"** y página previa a /TheArchitectChoice (no
   accesibles localmente; CDX bloqueado por proxy).

## G8. OP_RETURN «Good job, Neo!» y 1NULY — re-verificación EN CADENA [A] (NUEVO, 2026-11-22)

En vivo (API blockstream.info/esplora; GOODJOB_NULY_VERIFICACION.json):

- **148XH2…** OP_RETURN «Good job, Neo!» — txid `364de511fda4a139bc20d356a3e97ff1077987daa23818fcdf1fdca748286990`, bloque 624209, **2020-04-03 11:48:30 UTC**, 1000 sats, entrada desde 3GSMG24 (1200 sats).
- **13HGhj…** OP_RETURN «Good job, Neo!» — txid `722fbf3507b025e7618a4b3764b7b74d67c4d02e24b18f610f8e657d6b69e4cb`, **MISMO bloque 624209, misma hora** — el creador plantó ambas demostraciones juntas.
- **1NULY7…** (tercera puerta): 1 sola tx (`d6ff3da1…`, bloque 624768, **2020-04-07 04:17:21 UTC**, 1050 sats desde 3GSMG24), sin mensaje, intacta.

Cronología certificada nivel A: 24-mar plantadas sha256 → **3-abr ambos controles de ceros/reversión en el bloque 624209** → 7-abr la tercera puerta → 8-abr «And Oen» (Telegram #3404, registrado) → 21-may «First or zero» (PUZ #4105, registrado: indexación 0/1) → 25/26-dic-2021 primos+anulación de caracteres. Las demostraciones de ceros SON ANTERIORES a todas las pistas de ceros de SalPhaseIon, como propone el marco del usuario.

## G9. Puerta 1NULY con construcciones «24 y 24», 196 bits y primos-ceros — nivel R (NUEVO, NEGATIVO)

Controles 2/2 reproducidos en forma COMPRIMIDA en ambas: raw-lpad32 → 148XH2…; bits-reversed (192 bits invertidos) → 13HGhj…. **Identidad estructural verificada:** invertir los 196 bits de la matriz (192+0000) produce EXACTAMENTE la clave bits-reversed — los 4 bits finales '0000' son transparentes a la lectura invertida; la lectura directa de 196 = MSG desplazado 4 bits (no es clave).

Batería N54 (scripts/gsmg_zeros_battery.py, ZEROS_PUERTA_BATERIA.json): 36 candidatos / 72 derivaciones contra 1NULY/1GSMG/17ucy — XOR del mensaje y su inversión; suma/restas mod n; sha256 de las concatenaciones 48 B en ambos órdenes; sha256(MSG) XOR sha256(rev); truncaciones 42 y 32 B (primeros/últimos/centrales) del par de 48 B; 196 directa/invertida; bytes invertidos; anulación prima de bytes y de bits (0/1-based) sobre 192 y 196; intercalado primo/no-primo entre el mensaje y su inversión; XOR de las dos claves de 256 bits. **0 coincidencias.** El espacio de combinaciones directas del par «24 y 24» queda cerrado como negativo.

## G10. Reinserción de ceros en dbbi/faed → matriz → sumas vs payload60 — nivel R (NUEVO, NEGATIVO + HECHO ESTRUCTURAL)

Controles: FIELD1/FIELD2 (a=1..i=9, o=0 → lastwordsbeforearchichoice / thispassword) y sha256 del payload60.

- **Batería N55** (scripts/gsmg_zero_reinsertion.py, MATRIXSUM_ZEROS_BATERIA.json): ceros en posiciones primas del original (0/1-based) + uniformes k=2..12; 75 variantes, 234 matrices; sumas de filas/columnas (planas, mod 10, pad02) y valor de fila/columna por cada celda nula; decodificación FIELD de las cadenas restauradas (mejor 0.58 = ruido). **0 reproducciones del payload60.** Contabilidad decisiva: los 30 pares del payload suman **1821** vs dbbi 422 / faed 3079 — la reinserción no altera totales, luego payload60-junto-pares NUNCA es sumas de cobertura total de dbbi/faed bajo reinserción alguna.
- **HECHO ESTRUCTURAL NUEVO (nivel R):** la única longitud original consistente con «ceros en las posiciones primas» es **L = 121 = 11×11** para dbbi(91) y L = 695 = 5×139 para faed(570). La matriz 11×11 concreta (ambos indexados) está volcada en MATRIX_11x11_DDBI.json con TODAS sus familias de sumas (N56: filas, columnas, toroidales ambas direcciones, diagonales rectas, por celda nula) — 0 vs payload60. Sus 30 celdas nulas = π(121) ↔ los 30 pares del payload60: el emparejamiento con sumas NO estándar (pares de celdas, espirales, bloques de 4) queda como el siguiente experimento concreto del frente matrixsumlist.

## Archivos de la sesión

- `download/L5_SWEEP_RESULTS.json` — barrido 30,5M (texts, hits=0).
- `download/MOVIE_WORDS_RESULTS.json` — 1.296 trials AES frases película.
- `download/RABBIT_BITMAP.json` — bitmap del conejo 13×14 + conteos.
- `scripts/l5_sweep.py`, `scripts/movie_words.py`, `scripts/rabbit_nest.py` — reproducibles.
- `download/GOODJOB_NULY_VERIFICACION.json` — verificación en cadena de los OP_RETURN 2020 y 1NULY (G8).
- `download/ZEROS_PUERTA_BATERIA.json` — puerta: 36 candidatos / 72 derivaciones, 0 (G9/N54).
- `download/MATRIXSUM_ZEROS_BATERIA.json` — reinserción: 75 variantes / 234 matrices, 0 (G10/N55).
- `download/MATRIX_11x11_DDBI.json` — la matriz 11×11 de dbbi y todas sus familias de sumas (G10/N56).
- `scripts/gsmg_goodjob_verify.py`, `scripts/gsmg_zeros_battery.py`, `scripts/gsmg_zero_reinsertion.py`, `scripts/gsmg_matrix11.py` — reproducibles.

**Criterio de victoria (sin cambio):** AES auténtico con validación independiente o clave
d probada por dG == Q_objetivo. **GSMG NO RESUELTO.**
