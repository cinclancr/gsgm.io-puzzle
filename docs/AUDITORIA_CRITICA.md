# AUDITORIA_CRITICA.md — GSMG.io 5 BTC — auditoría crítica de la investigación
**Sesión L (2026-11-23) — investigación principal independiente. Puzzle: NO RESUELTO.**

**Mandato:** auditar la primera apertura AES que originó la cadena 1→4, reproducir
cada descifrado desde el ciphertext original con documentación completa,
verificar las inconsistencias de la sesión K, inventariar los sobres, y ejecutar
hipótesis nuevas solo con prueba objetiva. Ninguna clave se reclama.

> NOTA DE CONSOLIDACIÓN (2026-11-23): este documento se preserva TAL COMO fue emitido en la
> sesión L. Sus erratas verificables (§3.2 longitud de la preimagen; §3.3 distribución del
> barrido v3 y alcance por sobre) se corrigen en `AUDITORIA_L_ERRATA.md` con evidencia
> reproducible; NADA se reescribe en el original.

---

## 1. Resumen ejecutivo

| # | Resultado de la auditoría | Estado |
|---|---|---|
| 1 | La cadena 1→4 **se reproduce byte a byte** desde 7 sobres primarios; documentación completa por eslabón (contraseña, KDF, clave AES, IV, plaintext HEX, padding) en `CADENA_1_4_REPRODUCCION.json` | Reproducido |
| 2 | Los descifrados de la cadena NO son falsos positivos de padding-01: cada eslabón descansa en cruces comunitarios PREVIOS (2025-08→2026-06) y en encadenamiento criptográfico entre eslabones | Verificado con matices (§3) |
| 3 | El texto de fase 3.2 reconstruido: **2.422 B exactos**, sha256 `b82afeb8…408a34`, pad 10, 11 saltos CRLF intactos (`FASE32_PLAINTEXT_2422B.bin`) | Verificado |
| 4 | Las 7 demos comunitarias con contraseñas reveladas: TODAS verificadas desde el ciphertext original del log; + control triple de k1ng (AES-128/192/256); WIF de Cereal Killer verificado con EC completa | Verificado |
| 5 | Refutaciones X (08f2d4bf…) y JVTRADER (1vzA0tQR…) re-ejecutadas: 0 positivos | Refutado (confirmado) |
| 6 | Sesión K: `sha256("anstoo") = 21ef0533…` ✓; preimagen de `10d6a2c5` corregida (frase completa de 100 chars, no la truncada); estadística de 669 paddings = CBC-only con PKCS#7 real (los modos de flujo nunca cuentan padding) | Errata localizada |
| 7 | Censo de sobres: 81 únicos → 7 del creador + 3 transcripciones corruptas + 7 repostas parciales + 20 extendidas + 44 comunitarios (`MANIFEST_SOBRES.csv`) | Reproducido |
| 8 | Erratum de H19: la cita del «padding de 1 byte» es del comunitario k1ng (2025-05-18, msg 40911), NO del creador | Erratum |
| 9 | Copia cósmica más antigua en telegram (Hii, 2021-04-16): transcripción corrupta por 1 byte (389: 4e→74) | Nuevo |
| 10 | H1 (payload60 sobre tablero estradal) NEGATIVA; H4 (operando 29 B / «+-») NEGATIVA; H2 (mapeo documental del acertijo) VERIFICADA | Hipótesis ejecutadas |

**Conclusión principal:** la cadena 1→4 es material genuino del creador
(criptográficamente encadenado, reproducible con contraseñas publicadas por
terceros hasta 15 meses antes), PERO la interpretación de sus productos — los
35 bloques de 32 B como «claves», las 8 «llaves» intermedias — sigue **sin
autenticación independiente**: 0/310 inventario de direcciones, 0/~10.086
candidatos del selector, entropía de azar. El frente real del puzzle no cambia:
la regla selectora final (35 bloques → d) o material nuevo del creador.

---

## 2. Auditoría de la primera apertura (cadena 1→4) — método y evidencia

`scripts/auditoria_cadena.py` reproduce los 7 eslabones desde bytes primarios
(`orig/gsmg-5btc-puzzle/ciphertexts/`, cross-verificados con Naddiseo/wayback/viva):

| Eslabón | Sobre (sal, bytes) | Contraseña exacta | KDF | plaintext | pad | cruces |
|---|---|---|---|---|---|---|
| fase 2 | 06286612, 672 B | `sha256hex("causality")` (64 chars ASCII) | EVP-SHA256 | 648 B, sha `e2f9dd65…` ✓ | 8 | sha publicado |
| fase 3 | 9fbc451d, 4112 B | `sha256hex(227 chars)` = `1a57c572…` | EVP-SHA256 | 4090 B, sha `c4ad9455…` ✓ | 6 | sha publicado |
| fase 3.2 | eefc4c5b, 2448 B | `sha256hex("jacquefresco…")` = `250f3772…` | EVP-SHA256 | **2422 B**, sha `b82afeb8…` ✓ | 10 | sha publicado + k1ng triple |
| **cadena 1** | 3ab58534, 96 B | `matrixsumlistenterlastwordsbeforearchichoicethispasswordmatrixsumlist` (69 B) | **EVP-MD5** | 79 B = K_C1‖K_C2‖E_C | **1** | WIF (abajo) |
| **cadena 2** | b45a5e3d, 96 B | WIF `5K2byJMss…z8AT` (51 chars ASCII) | EVP-MD5 | 79 B = K_S1‖K_S2‖E_S | **1** | cita E_S |
| **cadena 3** | 2d3f6fe0, 1344 B | XOR de sha256 RAW de 7 tokens = `a795de11…` | EVP-MD5 | 1327 B, sha `4f7a1e4e…` ✓ | **1** | checkpoint Cuevabit |
| **cadena 4** | 5bbd88ac (oculto), 1168 B | `E_C‖E_S‖E_B[:2]` = `38d4f4c9…259cc` (32 B) | EVP-MD5 | 1151 B, sha `e4269ed5…` ✓ | **1** | contraseña+hash publicados |

### 2.1 ¿Los cruces son independientes? (la pregunta central del mandato)

Sí — verificados con fecha, autor y mensaje:

1. **`sha256(cosmic plaintext) = 4f7a1e4e…c081`** — publicado por **Cuevabit el
   2025-08-09** (telegram msg 46833), 15 meses antes de nuestra reproducción.
   Fuerza: coincidencia de 256 bits. Cuevabit lo re-certificó como checkpoint
   («the known checkpoint», 2026). **Concluyente.**
2. **WIF `5K2byJ…` con payload == K_C1** — publicado por **GalloClaudio64 en el
   issue #68 el 2026-01-01** (post que contiene la cadena completa). El checksum
   Base58Check del WIF es válido (2⁻³²) y el payload coincide con nuestro K_C1
   (2⁻²⁵⁶ si nuestro descifrado fuera erróneo). Re-publicado con el comando
   `openssl` exacto por حسین el 2026-06-17 (msg 65496).
3. **Contraseña de cadena 4 `38d4f4c9…259cc`** — publicada EXACTA (byte a byte)
   por GalloClaudio64 el 2026-01-01, junto con el sha `e4269ed5…` y la estructura
   «+-» + 35×32. Fuerza: 256 bits.
4. **Encadenamiento interno** (no depende de terceros): la contraseña de cadena 2
   es el WIF derivado de K_C1 (cadena 1); la de cadena 4 son fragmentos de las
   cadenas 1, 2 y 3; la cola de cadena 3 XOR-máscara `b657264f…` produce una
   cabecera `Salted__` válida (2⁻⁶⁴) + 1152 B de ciphertext alineado. Una cadena
   errónea no puede cerrar estos eslabones.

### 2.2 Clasificación de autenticidad (aplicando la regla del mandato)

**Regla del mandato:** «si el único resultado positivo es un padding 01,
reclasifica la apertura como no autenticada».

| Apertura | ¿Único positivo = pad 01? | Clasificación |
|---|---|---|
| cadena 1 (SalPhaseIon interior) | NO — cruce WIF (2⁻²⁵⁶+2⁻³²) + publicación previa + encadenamiento | **VERIFICADA** |
| cadena 2 (terminal 3.2.2) | NO — cita E_S exacta (2⁻¹²⁰) + encadenamiento como pieza de la contraseña de cadena 4 | **VERIFICADA** |
| cadena 3 (Cosmic Duality) | NO — checkpoint 256 bits de Cuevabit (2025-08-09) + estructura oculta + encadenamiento | **VERIFICADA** |
| cadena 4 (misterio) | NO como descifrado — contraseña+hash publicados antes + encadenamiento; PERO el contenido (35 bloques) no tiene autenticación interna | **VERIFICADA como descifrado / NO AUTENTICADA como material de claves** |
| urlblob | sí (0 aperturas de ~1,77 M descifrados) | **NO AUTENTICADA — cerrado como frente** |

**Sobre los 35 bloques de 32 B:** quedan expresamente fuera del estatus de
«claves genuinas». Hechos: 35/35 son escalares secp256k1 válidos (esperado en
material aleatorio); exactamente 7 contienen 0x77 en los índices [0,2,3,8,9,12,26];
la entropía (7,83; chi² 253) es indistinguible de azar; 0 coincidencias con la
pubkey del premio en ~10.086 candidatos del selector y 0/310 en el inventario de
direcciones. La derivación de las 16 direcciones de las 8 «llaves» intermedias
(re-ejecutada hoy) da 0 aciertos contra los 4 objetivos. Si los bloques son
claves, la regla selectora que las combina no está en el corpus local.

**Errata estructural detectada en H19:** la cita «could make it so that the
padding is 1 byte so we would dismiss it as a false positive» NO es del creador:
es del miembro comunitario **k1ng (2025-05-18, msg 40911)**. No existe fuente
del creador que declare deliberado el padding-1. La justificación del pad-1
descansa solo en la evidencia de §2.1.

### 2.3 ¿De dónde salió la receta de la cadena? (procedencia)

`GalloClaudio64` (issue #68, 2025-12-25 y 2026-01-01) publicó la receta completa.
Cadena de custodia documentada (post_history_recovery/CHAIN4_TIMELINE.md):
2025-12-25 (puntero «think triangular… XOR triangle») → 2026-01-01 (tronco
completo con contraseñas y hashes) → 2026-03/04 (EnigmAnderson #87: crib-drag,
split@246, tail sha `9f06936a`) → 2026-04-26 (andersonbig #84) → 2026-06-10
(marcofortina #92). La anomalía «1168−1151 = 17 no es PKCS#7» que señalaba esa
cronología queda explicada: los 17 B = cabecera OpenSSL `Salted__`+sal (16) + pad (1).
El propio GalloClaudio64 marcó la única debilidad: la procedencia del token
`secondanswer` (cadena 3) — sin anclaje literal en el puzzle («provenance is the
only weak link»).

---

## 3. Verificación de las inconsistencias de la sesión K

1. **`SHA256("anstoo")`** = `21ef053324184a4d…` — **coincide** con la preimagen
   del informe ✓ (re-computado).
2. **`SHA256("humphhopeisthequintessentialhumandelusion")`** = `f156d167…` —
   **NO coincide** con `10d6a2c5…` (el usuario tenía razón). **Bytes exactos
   localizados:** la preimagen real es
   `humphhopeisthequintessentialhumandelusionsimultaneouslythesourceofyourgreateststrengthandyourgreatestweakness`
   (100 chars — la cita completa de la película, sin puntuación). El JSON de la
   sesión K (`k_preimage_v2.json`) tenía el acierto correcto; el TEXTO del
   informe citó la forma truncada. Corregido (N62).
3. **Estadística de 669 paddings válidos:** re-auditada en el código de las
   baterías (`sesion_k_battery*.py`). Los 669 eventos del urlblob provienen
   EXCLUSIVAMENTE de ensayos AES-CBC con comprobación PKCS#7 real
   (`pt[-pad:] == bytes([pad])*pad`); los modos CFB/OFB/CTR (~141k descifrados)
   comprobaron solo cabecera `Salted__`/texto imprimible y generan 0 eventos de
   padding — no hay mezcla de modos. La distribución completa del barrido v3:
   6.129 eventos = 6.362 pad-1 + 20 pad-2 + 1 pad-16 (el pad-16 = control
   positivo «choiceis» de π-user, imprimible 0,77); consistente con ruido a
   1/256. Nota: el JSON final registra 684 eventos para urlblob (baterías
   acumuladas); 669 = solo el barrido v3.
4. **Inventario de sobres:** ver §4; separa originales (7), transcripciones
   corruptas (3), repostas parciales (7), repostas extendidas (20), demos con
   sal reutilizada (19) y demos propias (25).
5. **Erratas menores de sesión K documentadas (N63):** Ханыч 19d433ba: pad=16
   (el informe decía 4); Cereal Killer: relleno de 13 B (el informe decía 12;
   el propio autor dijo «random 13 byte»); el blob de k1ng es de 48 B por
   ciphertext (no total). Ninguna afecta a las conclusiones.

---

## 4. Censo de sobres (MANIFEST_SOBRES.csv) — 81 únicos por sha256

- **CREADOR (7):** fase 2 (672 B, `a0891445…`), fase 3 (4112 B, `9163a38d…`),
  fase 3.2 entrada (2448 B, `9d172dc0…`), terminal 3.2.2 (96 B, `291dfd6f…`),
  SalPhaseIon interior (96 B, `9e2831e1…`), Cosmic Duality (1344 B,
  `b1895055…`), urlblob (112 B, `25b3619a…` — probablemente NO del creador).
  Los 7 están ABIERTOS/verificados salvo urlblob (cerrado como frente).
- **TRANSCRIPCIONES CORRUPTAS (3):** dos ediciones Heellrzz 2024-03-30 (sal
  hex `3a→ba`, `5d→5f` + ciphertext corrupto) y la copia cósmica de Hii del
  **2021-04-16** (1 byte: 389 4e→74) — la más antigua en telegram, ahora
  explicada como error de transcripción y no como «edición temprana».
- **REPOSTAS PARCIALES (7) / EXTENDIDAS (20):** cabezas y recortes de los
  sobres del creador circulados por el chat (31 reposts del terminal desde
  2020-05).
- **COMUNITARIOS (44):** 25 con sal propia + 19 que reutilizan una sal del
  creador (p. ej. X 2024 publicó la cabeza del terminal con su propia sal).
  **8 verificados hoy con contraseña revelada:** choiceis (π-user, sha256hex
  «uncertainty» → cita Matrix, pad 16), S|h ×2 (sha256hex «choice» → frases,
  pad 9 / pad 1 con texto 100% imprimible — control genuino de pad-1),
  π-user e2991cdc (sha256hex «causality» → sha256 de vacío, pad 16), Ханыч
  (sha256hex «follow_the_white_rabbit» → sha256(causality) hex, pad 16 —
  coincide con su afirmación del msg 72037), k1ng ×3 (clave 250f3772… →
  «gsmg.io/theseedisplanted» en AES-128/192/256, pad 8), David Doak
  («backtothebasics», EVP-SHA256, key/iv coinciden con su transcripción
  E118302E/24E31C49, pad 16), Cereal Killer («[bz5Hnj/=v8GEss» → WIF válido
  + 13 B de relleno, pad 16 — ver §5).
- **El creador nunca publicó un sobre en Telegram** (0 ocurrencias en
  jrk_messages.txt): todos los sobres del chat son material comunitario.

---

## 5. El WIF de Cereal Killer (prueba de principio de la sección 6 del mandato)
El sobre 89a87486 (96 B, 2026-09-15, msg 72026) con contraseña `[bz5Hnj/=v8GEss`
(EVP-SHA256) produce 64 B = WIF(51) + relleno(13) + pad 16. Verificación
criptográfica completa: checksum Base58Check **válido** (versión 0x80, sin
comprimir); d = `268f5d0bf787ee1dcf7bf651c94723ce27023a0decbc84ea855509d0e3e2e195`;
P2PKH sin comprimir `1Cye1VZ2ztqas8G7CrgMrLYFrzknWQAhyF`; comprimida
`1CMstduuofveBCEpUqopFyqFQ9Nsh8eB9i`; **ninguna** está en el inventario de 310
direcciones ni coincide con los 4 objetivos. Es material del reto del solver,
no del creador — exactamente como exige el criterio del mandato («una dirección
matemáticamente válida no demuestra nada»). El intercambio completo (msgs
72026-72073, leído hoy) documenta: Ханыч lo abrió con la contraseña dada;
SATE: «acabas de abrir un blob AES con la contraseña correcta, nada más»;
Cereal Killer: «its random 13 byte… with private key to make 64 byte data».

**Con las 8 «llaves» de cadena (K_C1…K_H2):** 16 derivaciones EC re-ejecutadas
hoy (comprimida + sin comprimir): 0 coincidencias con 1GSMG1/17ucy/1NULY/3GSMG24
— consistente con su rol de material intermedio. Para los 35 bloques se
mantienen las dos hipótesis no excluidas del mandato: material de claves bajo
una regla selectora no encontrada, o material intermedio/decoy del creador. El
oráculo (d·G = pubkey 04f4d1bbd9…33559 → hash160 a9553269… → 1GSMG1…) queda
re-verificado.

---

## 6. Hipótesis nuevas (máx. 5) — formulación, orden por evidencia y ejecución

Ver `FASE32_HIPOTESIS.md` (documento completo) y `scripts/fase32_hipotesis1.py`.
Resumen: **H1** (payload60 como dígitos del tablero estradal — evidencia alta)
ejecutada → **NEGATIVA** (N60: decodificación = ruido; 18 AES = 0). **H2**
(mapeo documental del acertijo final) ejecutada → **VERIFICADA** (los términos
del acertijo cierran sobre el tablero VIC, el FEN de fase 3 y el WIF — el
acertijo ES la clave del tablero, ya documentado por GSMG-CLEAN §5b).
**H3** (2422 B sobre cuadrícula 14 con extracción prima) formulada, pendiente.
**H4** (operando 29 B / «+-» aritmético) ejecutada → **NEGATIVA** (N61: 0/12
contra el oráculo). **H5** (segunda lectura EBCDIC) formulada, pendiente
(probabilidad baja). El tablero estradal histórico se derivó programáticamente
(straddles 1,4; 21 celdas) alineando los 149 dígitos con las 91 letras conocidas.

---

## 7. Estados consolidados

| Objeto | Estado |
|---|---|
| Cadena pública (fases 0-3.2, rosa) | VERIFICADA (33/33 controles + re-ejecución de hoy) |
| Cadena 1→4 (4 eslabones AES) | VERIFICADA como descifrado; interpretación de productos NO AUTENTICADA |
| Texto fase 3.2 (2422 B) | VERIFICADO (reconstruido, saltos intactos) |
| 7 demos comunitarias + k1ng triple | VERIFICADAS (contraseñas reveladas) |
| X 08f2d4bf…, JVTRADER 1vzA0tQR… | REFUTADAS (0 positivos re-ejecutados) |
| urlblob (112 B) | NO AUTENTICADO / CERRADO (~1,77 M descifrados = 0) |
| Selector final (35 bloques → d) | PENDIENTE (espacio local agotado; requiere premisa nueva) |
| 1NULY / claves de cadena / 35 bloques como claves | PENDIENTE / NO AUTENTICADO |
| Libro Time-Life, /TheArchitectChoice | PENDIENTE (materiales no disponibles — hueco declarado) |
| H1/H4 de esta sesión | NEGATIVAS (N60/N61) |
| H2 de esta sesión | VERIFICADA (documental) |

**Reglas de validación mantenidas** (fijadas 2026-11-21d): el padding de un byte
no valida por sí solo; la única prueba de un escalar es la dirección exacta;
sin fuerza bruta sobre ECDLP/SHA-256/HASH160; sin promover SHA/direcciones
«válidas» sin regla de origen + control positivo.

## 8. Límites declarados

- El texto real del libro Time-Life «Cosmic Duality» y los originales de
  /TheArchitectChoice y /followthewhiterabbit NO existen en los materiales
  locales; prohibido presuponer su contenido.
- Los 4 URLs CDX sin identificar (673e3b1a…, a2aefdbb…, aca20ae7…, c2eef34b…)
  resistieron ~12k candidatos; solo valen si alguien publica las conjeturas
  del prober.
- El lote poemas 4.110 de enlaces conserva solo conteo citado (nivel B/C).
- Ninguna clave, WIF ni dirección se reclama. **El puzzle sigue SIN RESOLVER.**

## 9. Archivos de esta sesión

`CADENA_1_4_REPRODUCCION.json` (reproducción documental completa) ·
`FASE32_PLAINTEXT_2422B.bin` · `CADENA4_PLAINTEXT_1151B.bin` (re-emitido) ·
`MANIFEST_SOBRES.csv` (81 sobres clasificados) · `AUDITORIA_DEMOS_L.json`
(41 verificaciones) · `FASE32_HIPOTESIS.md` · `PRUEBAS_NEGATIVAS.csv` (+N60-N63) ·
scripts reproducibles: `scripts/auditoria_cadena.py`, `scripts/auditoria_demos.py`,
`scripts/reclasifica_manifest.py`, `scripts/fase32_hipotesis1.py`.
