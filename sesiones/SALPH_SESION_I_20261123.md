# SalPhaseIon — Sesión I (2026-11-23): `sha256anstoo`, rama ZION y ying yang

**Estado:** confirmaciones + negativos registrados; **ninguna apertura autenticada**. 400 operaciones documentadas una a una en `I_OPERACIONES_TODAS_SESION_I.csv`.
**Entrada del usuario:** «sha256anstoo falta hacer esto… podría concatenar todas las respuestas anteriores o solo sha al segundo padding… haz pruebas y genera hipótesis; no descartes ZION tampoco que abrió ambos; aun falta hacer ying yang».

---

## 0. Resumen ejecutivo

| # | Resultado | Nivel |
|---|---|---|
| 1 | **Todas las afirmaciones numéricas del informe del usuario se reproducen exactamente** (rama A, rama ZION, cadena WIF, barrido de 32 combinaciones, 18/362.880 de S91) | Reproducido |
| 2 | Se recupera el **hash completo de la salida ZION** que el usuario solo citaba por prefijo/sufijo: `506a9e29cae9a4c75851fd2bf018a21fbfa282dfe8b0ca5861f16030bd560c00` | Reproducido |
| 3 | `sha256anstoo` ejecutado bajo la **convención GSMG probada** (password = sha256(respuesta) hex + EVP_BytesToKey(SHA-256)) y bajo EVP-MD5: **0 aperturas con texto** en J/s, terminal y Cosmic; 1 padding `01` nuevo (I128) al nivel del ruido | Negativo (ruido) |
| 4 | **ying yang hecho**: 12 operaciones XOR / complemento / intercalado sobre los tres materiales de 79 B — sin estructura, sin `0x80`, sin patrón DBBI, sin direcciones, 0 aperturas | Negativo (ruido) |
| 5 | ZION **no** abre terminal, Cosmic, ni la variante R/k, ni su forma de convención → «abrió ambos» **no se reproduce** localmente (discrepancia abierta, §5) | Parcial |
| 6 | Puerta DBBI (autenticación más fuerte disponible, p≈2⁻²¹¹ por digest): **0 coincidencias** sobre ~50 candidatas | Negativo |
| 7 | Direcciones de todas las claves de 32 B derivadas: **0 coincidencias** con HALF / BETTER HALF / sembrada / las 5 vigiladas | Negativo |

**Conclusión de la sesión:** las ramas A y ZION siguen **abiertas como hipótesis de trabajo** (ningún dato nuevo las cierra), pero siguen **sin cumplir ninguno de los 6 criterios de apertura autenticada**. La lectura más dura del marco estadístico: en los barridos históricos de la comunidad se registraron **750 salidas pad=1 frente a 731,9 esperadas por azar** (09_UNFORESEEN_HINT_AND_LAST_WORDS.md §91, recheck `runs/2026-09-13_recheck_755`) — es decir, los «aperturas» de padding `01` históricas, incluidas las de este caso, se comportan exactamente como ruido. Lo único genuinamente autenticado del corpus GSMG sigue siendo la cadena fase 1→2→3→3.2 bajo la convención probada (§2).

---

## 1. Reproducción completa de las dos derivaciones y la cadena WIF

Contenedor en ambas: 96 B, `Salted__` + sal `3ab585348552415d`, 80 B de ciphertext (idéntico a `locked_salphaseion_short.bin` del corpus GSMG-CLEAN). Los dos segmentos de 64 caracteres que lista el usuario **son literalmente las dos líneas del sobre J/s** (`SALPH_AES_ARCHIVADO_DOS_EDICIONES.b64`, variante J/s = históricamente mejor apoyada, H8): el rótulo «(resultado wif)» de su lista era la primera línea del sobre, no un resultado.

| Ítem | Valor reproducido | ¿Coincide con el informe? |
|---|---|---|
| A: 5 tokens + EVP-MD5 @ J/s | 79 B (padding `01`), SHA-256 `1449a2178eea7c0e3fabac8c1ad2afa294be4fc1800c594a025a056e88c626bf` | ✓ |
| ZION + EVP-SHA256 @ J/s | 79 B (padding `01`), SHA-256 `506a9e29cae9a4c75851fd2bf018a21fbfa282dfe8b0ca5861f16030bd560c00` | ✓ (prefijo y sufijo; hash completo recuperado aquí) |
| WIF no comprimida de K_C1 | `5K2byJMssxFKuTgnk9YQjpBz5FhkwwF2LaZoAyTus8HjGEpz8AT` | ✓ |
| WIF(K_C1) + EVP-MD5 @ terminal 3.2 | 79 B (padding `01`), SHA-256 `b40fce72ef5638e4f79b3233e653f8a5dbdb0d4ae2009d2d3da2c98b70f4d004` | ✓ |
| Barrido 32 combos (mitades A/B × WIF comp/unc × MD5/SHA-256 × J/s+terminal) | **Solo sobrevive** A → primera mitad → WIF sin comprimir → terminal con MD5 | ✓ (idéntico al informe) |
| S91: 9 letras distintas, orden de primeras apariciones | `dbifhcega` = DBIFHCEGA | ✓ |
| Ordenaciones de las 9 letras que son subsecuencia de S91[:17] | **18 de 362.880** | ✓ |
| Z único en la salida Bifid 570 | posición 1-based 98 | ✓ |
| K_S1 / K_S2 / E_S de la segunda salida | `b06fa6f2…309c4b` / `b11d211c…aea597` / `740a25de4b8e946d0a5ae2667a23a2` | ✓ (coinciden con RESULTADOS_VERIFICADOS_AES_Y_BIFID.json) |

Material nuevo registrado (rama ZION, para re-tests futuros, JSON `I_RESULTADOS_SESION_I.json` → `material_79B`):

- `B79` (ZION): `2aa3fb73…efefa86f` — K_B1 `2aa3fb73bebd876823eca6ba65e7311bea5f753a8524656bc1c9a4b40236beed`, K_B2 `de4e4ebb…599e48396`, E_B `32d1b03bcc738df1264a03efefa86f` (15 B); WIF de K_B1 sin comprimir: `5J94n2zr8Kxr9nEDWYX84Whe7Fv4iogZupjtEQEZuYd7Qcim83Q`.
- `XOR(K_C1,K_C2)` = `8abee307a10bb0c257d002282425596a4cbc3bf868f4c05c8e299d09998ae629`; `XOR(E_C,E_S)` = `4cded117473acbb2c295176b74f267`.

**Recordatorio obligatorio (correcciones del usuario, vigentes):** ninguna de estas salidas está autenticada; la división 32+32+15 sigue siendo provisional y podría ser casual; el padding `01` aislado no constituye solución.

---

## 2. Marco de calibración: por qué «01» no basta (y cuánto pesa realmente)

1. **Convención probada del autor** (01_PROVEN_CHAIN.md §0, `tools/check_candidate.py`): password = `sha256(respuesta)` en 64 hex minúsculas + `EVP_BytesToKey(SHA-256)` + AES-256-CBC. Abrió **fase 2** (`causality`), **fase 3** (respuesta de 7 partes, autenticada además por la dirección sembrada `1M5ypvDbp…`), y **fase 3.2** (`jacquefrescogiveitjustonesecondheisenbergsuncertaintyprinciple`). **MD5 falla en las tres** (H_KDF_CALIBRACION.json).
2. **Ambas ramas violan la convención**: A usa EVP-MD5 (KDF incorrecto); ZION usa el KDF correcto pero una contraseña literal de 4 letras (no es `sha256(respuesta)` en hex).
3. **Estadística del padding**: P(pad válido | contraseña errónea) ≈ 1/256 (control sesión H: 7/2000 = 0,35 %). La comunidad registró **750 pad=1 vs 731,9 esperados** (09 §91) — nivel de azar puro. Tres «aperturas» citadas por el usuario (A, ZION, la tercera de 448 caracteres) viven dentro de esa distribución de ruido.
4. **El eslabón WIF es débil por construcción**: dado el `A79`, el barrido prueba 32 combinaciones sobre dos sobres; bajo azar, P(≥1 dé `01`) ≈ 1−(255/256)³² ≈ **11,8 %**. Que «solo sobreviva» una combinación es exactamente lo que el azar produce con frecuencia.
5. Los 79 B son **indistinguibles de uniformes** (HG1, sesión H: entropía/χ²/imprimible dentro del rango de 20.000 controles) — no hay estructura interna que apoye 32+32+15.

---

## 3. `sha256anstoo` — qué significa la etiqueta y qué se probó

### 3.1 La etiqueta, leída

- La página dice `shabef` + `anstoo` al final (`shabefanstoo`, posición 1075) y `shabef` + `ourfirsthintisyourlastcommand` antes del sobre (08_SALPHASEION_RECIPE.md §0.1: **b=2, e=5, f=6 en A1Z26 ⇒ `shabef` = `sha256`**; el usuario escribe `sha256anstoo` = la misma decodificación).
- Lectura documentada (08, ítem 10 de la receta, «checked by the proven convention»): **«sha256: answers too» — las respuestas se hashean antes de usarse**. No describe una operación nueva sobre los 79 B: es el **manual del sobre** — la misma convención que abrió fases 2/3/3.2.
- Consecuencia operativa: la forma correcta de «concatenar todas las respuestas anteriores y aplicar SHA-256» no es hashear los 79 B intermedios, sino formar la **respuesta** y usar `sha256(respuesta)` como contraseña con **EVP-SHA-256**. Eso es exactamente lo que batió esta sesión.

### 3.2 Batería (convención y variante MD5; 3 sobres: J/s, terminal, Cosmic)

Candidatos con texto previo al hash registrado uno a uno (CSV, columna `texto_previo_exacto`):

- **18 formas de la cadena del usuario** (U1–U18): con `z` literales (la forma física de la página: `z1|z2|z3` separan FAED-decodificado / lastwords / thispassword / shabef), sin `z`, con `z` como separador, mayúsculas, con los dos segmentos Base64 y `shabefanstoo` final, solo estructura (dbifhcega+btcseed570+…), solo bifid570, inversa, histórica sin `enter`, histórica con `enter`, respuesta de fase 3.2, mensaje VIC completo, `halfandbetterhalf`, token `yinyang`, `59` (479⊕484).
- **4 WIF** (K_C1/K_C2 comp/unc), **2 hex de 79 B** (A y segundo), **3 binarios** (A79, B79, segundo79 crudos).
- **«Solo sha al segundo [padding]»**: `sha256(segundo79)` como contraseña, `sha256(segundo79 ‖ 01)`, `sha256(A79)`, `sha256(WIF)`, `sha256(01)` — sobre los tres sobres, ambos KDF.
- **Cada candidata pasó además por la puerta DBBI** (patrón de repetición de `sha256(respuesta)` frente a la tokenización b/g de DBBI; una coincidencia = autenticación, p≈2⁻²¹¹ por digest).

**Resultados (400 operaciones):**
- Convención EVP-SHA-256: **0 aperturas** con cualquiera de las ~50 candidatas en los tres sobres.
- EVP-MD5: 1 novedad — **I128**: `sha256(jacquefresco…principle)` + MD5 sobre J/s → 79 B pad `01` (imprimible 0,443). Interesante pero **ruido**: es la respuesta autenticada de fase 3.2 usada con el KDF equivocado.
- Puerta DBBI: **0/50**. Direcciones: **0/…** (todas las claves de 32 B derivadas frente a HALF, BETTER HALF, sembrada, las 5 vigiladas, incluida la forma P2SH-P2WPKH del creador).

### 3.3 «enter»

La lista del usuario coloca `enter` **entre los dos segmentos Base64** — exactamente donde está en la página. La lectura mecánica documentada (08 §0.2) es que `enter` registra el **salto de línea del propio `openssl enc -a`** (64 caracteres + CR/LF + 64 caracteres): el mismo patrón aparece en el sobre terminal dentro del plaintext de fase 3.2 y en el textarea de Cosmic (28 líneas de 64). La interpretación «enter = instrucción para el siguiente» y la mecánica coinciden en la posición; ambas lo excluyen como material de clave.

---

## 4. ying yang — hecho (pendiente del usuario) — resultado: negativo de ruido

**Anclaje literario real de la pista (no conjetural):** el bloque VIC decodificado de fase 3.2 dice «IN CASE YOU MANAGE TO CRACK THIS **THE PRIVATE KEYS BELONG TO HALF AND BETTER HALF** AND THEY ALSO NEED FUNDS TO LIVE» — dos mitades (yin/yang) es la estructura declarada del premio. El token `yinyang` es el 4.º de la receta A del creador (`yellowblueprimes matrixsumlist lastwordsbeforearchichoice yinyang`); su forma-de-contraseña ya estaba en negativos (sesión H).

Batería ejecutada sobre A79 / B79 / S79 (12 resultados, JSON → `yinyang_analisis`):

| Operación | len | imprimible | byte 0x80 | DBBI | direcciones | aperturas |
|---|---|---|---|---|---|---|
| XOR(mitad1, mitad2) de A / B / segundo | 32 ×3 | 0,31–0,38 | no | no | 0 | 0 |
| XOR rama A ⊕ rama B (79 B) | 79 | 0,329 | no | no | 0 | 0 |
| XOR(A79 ⊕ segundo79) | 79 | 0,456 | no | no | 0 | 0 |
| XOR(B79 ⊕ segundo79) | 79 | 0,342 | no | no | 0 | 0 |
| XOR mitades cruzadas A⊕B (1 y 2) | 32 ×2 | 0,28–0,44 | no | no | 0 | 0 |
| XOR colas E_C ⊕ E_S | 15 | 0,40 | no | no | — | 0 |
| Complemento (~) de A79 y de segundo79 | 79 ×2 | 0,30–0,33 | no | no | 0 | 0 |
| Intercalado K_C1∥K_C2 | 64 | 0,438 | no | no | 0 | 0 |

Cada resultado se probó como: (a) **clave AES directa** (IV ceros y sal×2, tres sobres); (b) **respuesta bajo convención** (su SHA-256 como contraseña); (c) **clave privada** (WIF + P2PKH/P2SH frente a vigiladas). **Todo negativo.** Si ying yang es un operador, **no es ninguno de estos XOR/complementos/intercalados sobre el material de 79 B** — los interpretandos probables eran ruido desde el principio (§2.5).

---

## 5. Rama ZION — qué sobrevive y qué no

- **Sobrevive:** `ZION` + EVP-SHA-256 abre J/s con pad `01` y 79 B reproducibles (hash completo arriba). Es la única de las tres aperturas que usa el **KDF del autor** (SHA-256), aunque la contraseña siga sin ser de la forma `sha256(respuesta)`.
- **No sobrevive (esta sesión, registrado):** ZION/zion/Zion en terminal y Cosmic (ambos KDF); ZION sobre la variante **R/k** del sobre (ambos KDF); la forma de convención `sha256(ZION)`-hex en los tres sobres; `salvationofzion` literal y de convención; la cadena WIF de B79 (las 16 combinaciones de sus mitades).
- **«ZION abrió ambos» — discrepancia abierta:** no se reproduce en ninguna lectura local disponible («ambos» sobres de SalPhaseIon J/s+R/k; SalPhaseIon + terminal; ambos KDF). Los resultados guardados del ChatGPT del usuario (que él mismo no pudo reabrir) podrían contener la combinación exacta. **Pendiente:** recuperar de ese registro la contraseña exacta + KDF + contenedor para cerrar la discrepancia. Mientras tanto, la rama ZION se mantiene **viva como hipótesis** con su material B79 registrado (§1), pero su única apertura reproducible sigue siendo J/s.

---

## 6. Hipótesis generadas (pedidas por el usuario) y su ranking

| ID | Hipótesis | Base | Cómo se cerraría / falsaría |
|---|---|---|---|
| **H-I1** | La respuesta de SalPhaseIon es **«the last words before archi choice»** (P1–P5 de 09 §2, con P1 = transcript Scott Manning línea 105, justo antes de que Neo camine hacia la puerta) usada bajo la **convención probada** | El marco entero (receta ítems 4–5); los barridos previos de lastwords usaron oráculos en parte raw-only | Re-pasar los referentes P1–P5 con `check_candidate.py` (perfil `gsmg`) sobre los 3 sobres; la puerta DBBI da autenticación inmediata si acierta |
| **H-I2** | `matrixsumlist` es una **operación real** (pista «no prevista» #5966/#5969: «You are at the prime part already») cuya lista de sumas produce la respuesta de H-I1 | 08 §1; L1 479/484; ninguna de las ~160k construcciones previas funcionó | Encontrar la operación de sumas que decodifique bajo las tres codificaciones de la propia página; validar con puerta DBBI |
| **H-I3** | **DBBI es el sustituto del digest** (L5): `sha256(respuesta)` tokenizado coincide con la estructura b/g de DBBI | 08 §2; la puerta de autenticación más fuerte de toda la página (2⁻²¹¹); 16,8 M cadenas ya pasadas sin coincidencia | Cualquier candidata nueva pasa por esta puerta gratis (ya integrado en esta sesión: 0/50) |
| **H-I4** | La rama **ZION** corresponde a una «respuesta» corta real del autor con KDF correcto pero literal (ruptura parcial de convención) | ZION usa SHA-256 y abre; pero p=1/256 + 750/731,9 históricos | Encontrar una segunda apertura independiente con la MISMA salida (p. ej. el registro ChatGPT de «ambos») o una dirección derivada que colisione |
| **H-I5** | La cadena **A→WIF→terminal→…→Cosmic** es real y el autor encadenó sobres con derivaciones de las salidas | La cadena produce `01` en cada capa; pero cada eslabón ≈1/256 con docenas de formas probadas | Un eslabón que entregue **texto legible** o un **marcador Salted__** interno genuino (el de la literatura comunitaria — 1.327 B, máscara XOR — no es autónomo: se construye a partir de la propia cadena) |
| **H-I6** | ying yang es un operador **distinto** de XOR (p. ej. relacionar las dos mitades por su suma módulo 2^n, o las dos ramas A/B por otra composición) — y por eso el XOR dio ruido | VIC «half and better half»; negativo completo de XOR | Enumerar composiciones binarias alternativas y pasarlas por la misma batería de esta sesión (barato; registro listo) |

**Descartes motivados (esta sesión):** ying-yang-como-XOR del material de 79 B (ruido en 12 formas); `sha256anstoo` como hash de las salidas intermedias de 79 B en cualquiera de sus 5 formas; `sha256(ZION)`-de-convención; `59 = 479⊕484` como respuesta.

---

## 7. Registro, criterios y siguientes pasos

**Archivos de esta sesión (todos en `download/`):**
- `I_OPERACIONES_TODAS_SESION_I.csv` — 400 operaciones, una por fila (id, categoría, entrada exacta previa al hash, KDF, sobre, sal, salida, padding, imprimible, sha256, puerta DBBI, direcciones, veredicto).
- `I_PRUEBAS_NEGATIVAS_SESION_I.csv` — subset negativo (394 filas) para no repetir.
- `I_RESULTADOS_SESION_I.json` — resumen + material de 79 B completo + análisis ying yang.
- `scripts/sesion_i_sha256anstoo.py` + `scripts/sesion_i_addendum.py` — reproducibles.

**Los 6 criterios de apertura autenticada — estado de las ramas A/ZION/cadena WIF:** ① sobre verificado ✓ (J/s = GSMG-CLEAN, idéntico); ② contraseña e bytes exactos ✓ (reproducidos); ③ KDF reproducible ✓ pero **off-convention**; ④ padding ✓ (`01` — nivel ruido); ⑤ texto/estructura demostrable **✗** (uniforme); ⑥ predicción independiente **✗** (puerta DBBI 0; direcciones 0). **0 de los criterios duros.**

**Siguientes pasos priorizados:**
1. Cerrar la discrepancia «ZION abrió ambos»: recuperar el registro exacto guardado por el usuario (contraseña+KDF+contenedor de la segunda apertura).
2. H-I1: re-pasar los referentes P1–P5 (y todas las cadenas de esta sesión) por `check_candidate.py` perfil `gsmg` — media hora de cómputo, puerta DBBI incluida.
3. Recuperar el texto exacto de la tercera contraseña de 448 caracteres (solo consta su comportamiento; conservarla como control, según el propio usuario).
4. Vigilancia on-chain diaria: sin cambios que afecten al caso (cron activo, próximas ejecución 2026-11-23 09:00 Costa Rica).

---

## Apéndice A — La cadena del usuario, aclarada

```
dbifhcega                         ← S91: orden de primeras apariciones (verificado)
matrixsumlist                     ← M104 (a/b binario), pos. 92–195
btcseed…iel (570)                 ← FAED vía Bifid DBIFHCEGA, prefijo BTCSEED, z@98
z | lastwordsbeforearchichoice    ← z1(766) + bloque 63 (a–i/o)
z | thispassword                  ← z2(830) + bloque 29
z | sha256                        ← z3(860) + shabef (b=2,e=5,f=6)
ourfirsthintisyourlastcommand     ← literal de la página
U2FsdGVkX1…rd9z                   ← sobre J/s, línea 1 (64) — NO es «resultado wif»
enter                             ← M40 (a/b), = salto de línea de openssl -a (08 §0.2)
QvX0…jJ                           ← sobre J/s, línea 2 (64)
sha256anstoo                      ← shabefanstoo = «sha256: answers too» (manual del sobre)
```
