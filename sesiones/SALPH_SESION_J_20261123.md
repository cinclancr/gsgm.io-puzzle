# SalPhaseIon — Sesión J (2026-11-23): auditoría del issue «BYTENPHASE» (akaVARU / rayceja)

**Entrada del usuario:** issue del repo puzzlehunt-gsmgio-5btc-puzzle — akaVARU publica la cadena
`BYTENPHASEGBDOEL4YJKSVTML2KSDB` extraída del bloque FAED570; belgvr y Naddiseo exigen metodología
y cuestionan el recorte de «FAE»; akaVARU publica la receta completa (quitar FAE → 563→567→63 grupos
de 9 → sumas mod 26 → Vigenère `THEPROBLEMIS` → quitar YIN → corrientes alternas → XOR 5-bit →
matriz 6×5 → espiral); rayceja la reproduce, corrige el período (12, no 11), cuenta 43.680 claves
compatibles con {YIN + BYTENPHASE} y reporta 144 descifros AES negativos.

**Estado tras esta sesión:** aritmética reproducida al 100 %; crítica estadística de rayceja
**confirmada y reforzada empíricamente**; 0/6 criterios de apertura autenticada; la rama queda
abierta como hipótesis de **prioridad baja**, sin ninguna puerta autenticada.

---

## 0. Resumen ejecutivo

| # | Resultado | Nivel |
|---|---|---|
| 1 | La aritmética de akaVARU se reproduce **exactamente**: las 5 cadenas publicadas (S63, V63, corrientes A/B, espiral) coinciden carácter a carácter; la fórmula «i mod 11» del issue es errata — el período real es **12** (como notó rayceja) | Reproducido |
| 2 | El conteo de rayceja se verifica **exactamente**: 43.680 claves compatibles = 26·20·7·12·1·1 sobre los pares disjuntos (3,4)(5,6)(7,8)(9,10)(11,0)(1,2); además, exigir «YIN» **fuerza** k[0:3] = `THE` | Reproducido |
| 3 | Enumeración COMPLETA de las 43.680 claves: `THEPROBLEMIS` **no está distinguida** dentro de su propia clase de compatibilidad — su resto cubre 5/20 letras mientras una clave alternativa cubre 14/20; su texto plano 0/63 contra 25/63 de la mejor alternativa; **ninguna** de las 43.680 espirales contiene palabra de diccionario > 5 letras | Nuevo — negativo |
| 4 | Monte Carlo nulo calibrado (4.000 permutaciones de FAED): p(prefijo 3-letras relevante) = 0,0028 (teórico ✓); p(evento-frase tipo BYTE+N+PHASE) = 0,0035; p(ambos) ≈ 10⁻⁵ por configuración | Nuevo |
| 5 | Puertas auténticas: 276 descifros (25 candidatos × 4 perfiles × 3 sobres + formas binarias) = **1** padding `01` (perfil raw, sobre Cosmic, imprimible 0,358) = ruido 1/256; puerta DBBI **0**; escalares → direcciones del premio **0/25** | Negativo |
| 6 | «BYTE» leído como instrucción (re-agrupar los 150 bits / 100 bits del resto en bytes, 8 offsets cada uno): imprimible 0,42–0,54 = ruido. La cadena **no** funciona como instrucción operativa | Negativo |
| 7 | Variantes limpias (570 entero, sin mutilar): 13 formas divisorias × filas/cols × 2 convenciones × {plano, Vigenère ±THEPROBLEMIS}, más Vigenère sobre FAED-crudo y sobre la salida Bifid, teclas de dígitos del bloque R1: solo hallazgos de azar (NUKES/MAGAS/ELFIC/WURST/…) | Negativo |
| 8 | Anclaje documental de las dos pistas usadas por akaVARU: «one for one, four for one» es pista de **fase 3.2** (tablero VIC, dígitos reservados 1 y 4; no aparece en la página de SalPhaseIon) y el monólogo del Arquitecto del propio puzzle **no contiene** choice/problem/door — `THEPROBLEMIS` solo se obtiene de la cita externa de la película | Auditado |

**Conclusión de la sesión:** la observación YIN+BYTENPHASE es real y reproducible, pero (a) la clave
no queda determinada por la observación (43.680 candidatas), (b) `THEPROBLEMIS` no es ni siquiera la
más «legible» de esas candidatas, (c) el resto de 20 valores no es recuperable desde lo publicado,
y (d) ninguna puerta autenticada (AES/DBBI/direcciones) la corrobora. El evento conjunto es
improbable bajo azar puro (~10⁻⁵ por configuración si la clave se eligió de verdad desde la pista),
pero compatible con la multiplicidad histórica de configuraciones ensayadas por la comunidad si la
clave se ajustó a posteriori. Sin nuevo anclaje independiente, esta rama no merece más cómputo.

---

## 1. Reproducción del pipeline (J1)

Datos: FAED570 del textarea verificado por SHA-256
(`066191b4…1d5ef3c2`, idéntico al bloque del issue — verificación de transcripción incluida).
Pipeline: quitar `FAE` → 567 = 63 grupos de 9 → sumas (A=1..I=9) → mod 26 (0=A) → S63 →
resta Vigenère con `THEPROBLEMIS` (período 12) → V63 → quitar `YIN` → corrientes alternas →
XOR de valores 5-bit (A=0..Z=25, crudo, sin mod 26) → matriz 6×5 por filas → espiral desde
la esquina superior izquierda bajando por la columna izquierda.

| Cadena | Publicada | Reproducida |
|---|---|---|
| S63 (sumas) | `RPRRUAVBQMTOLVAZUUVXKNXXPIPDEZSSIEELUSODWOCXFSBYOGZAETLSEOKNAIJ` | ✓ idéntica |
| V63 (Vigenère) | `YINCDMUQMALWSOWKDGUMGBPFWBLONLRHESWTBLKOFABMBGTGVZVLNFKHACCVHBF` | ✓ idéntica |
| Corriente A | `CMQAWOKGMBFBOLHSTLOAMGGZLFHCVB` | ✓ idéntica |
| Corriente B | `DUMLSWDUGPWLNREWBKFBBTVVNKACHF` | ✓ idéntica |
| Espiral | `BYTENPHASEGBDOEL4YJKSVTML2KSDB` | ✓ idéntica |

Primeras 6 sumas = 43,41,43,43,46,52 (coincide con la tabla del issue). El «4» y «2» de la
espiral son los valores crudos 28 y 26 mostrados en alfabeto Base32. Todo el claims aritmético
del issue queda **verificado**; lo que falla es el anclaje (§5) y la cascada (§2–§4).

## 2. El espacio de claves no está determinado — y THEPROBLEMIS no es especial en él (J2)

- Exigir prefijo `YIN` fuerza k[0:3] = `THE` (computado: [19,7,4]). Los 10 símbolos espirales
  `BYTENPHASE` tocan los índices XOR {0,5,10,15,20,25,26,27,28,29} → pares de posiciones de clave
  (3,4)(5,6)(7,8)(9,10)(11,0)(1,2) con soluciones 26·20·7·12·1·1 = **43.680** — exactamente el
  conteo de rayceja, aquí derivado desde la estructura de llenado de la matriz (espiral ≠ orden
  de XOR; por eso los pares son los que son).
- `THEPROBLEMIS` está entre las 43.680. Métricas por clave (enumeración completa):

| Métrica | THEPROBLEMIS | Mejor alternativa | Nulo (4.000 MC) |
|---|---|---|---|
| Cobertura palabras ≥4 del resto (20 sím.) | **5/20** | 14/20 (`THEQULECHNJS`) | — |
| Cobertura de la espiral completa | 9/30 (BYTE+PHASE) | — | media 1,38/30, máx 15/30 |
| Cobertura del texto plano V63 | 0/63 | 25/63 (`THEZBIHLETPS`) | — |
| Palabras ≥5 en espiral | solo `PHASE` | ninguna clave produce > 5 | — |
| Resto todo-letras | no | 7.560 claves (17,3 %) sí | — |

Lectura: dentro de la clase de claves compatibles con la observación, `THEPROBLEMIS` es **mediana o
peor** en todas las métricas de «legibilidad». Si el diseño fuera real y la clave fuera
`THEPROBLEMIS`, el resto de 100 bits sería concreto — pero la observación publicada no permite
recuperarlo: otras 43.679 claves dan restos distintos igual de compatibles, y varias «más legibles»
que la de akaVARU. Esto convierte el argumento de ambigüedad de rayceja en un resultado empírico.

## 3. Marco estadístico honesto (J2b)

Monte Carlo con FAED permutado (misma multiplicidad de letras), clave `THEPROBLEMIS` fija, 4.000 ensayos:

- p(prefijo de 3 letras relevante — YIN/YANG/NEO/KEY/…) = **0,00275** ≈ teórico 50/17.576 = 0,00284 ✓ calibrado.
- p(evento-frase: ≥2 palabras ≥4 cubriendo ≥80 % de una ventana ≥9 dentro de la espiral de 30) = **0,0035**.
- p(ambos en el mismo ensayo) = 0/4.000 (esperado ~0,04 eventos) → conjunto ≈ **10⁻⁵ por configuración**.

Dos lecturas posibles y no distinguibles desde fuera: (i) si la clave se tomó de verdad de la pista
`lastwordsbeforearchichoice`, el evento conjunto es genuinamente sorprendente (~1 en 100.000 por
configuración; la multiplicidad comunitaria de configuraciones análogas no lo explica del todo);
(ii) si la clave se ajustó para producir «YIN» (nótese: **exigir YIN determina que la clave empiece
por THE** — la mitad «significativa» de la clave es un artefacto de la salida deseada), el evento
resta tiene p ≈ 0,0035 por clave tipo THE·, y decenas de claves «clue-plausibles» existen. El corpus
no permite decidir entre (i) y (ii). **Lo que sí decide es la cascada — y no cascada** (§2, §4).

## 4. Puertas auténticas — todo negativo (J3, J3b)

Candidatos: espiral completa (± mayús/minús, variante numérica 28/26), resto de 20, `BYTENPHASE`,
V63/S63 completos, corrientes A/B, `YIN`, `THEPROBLEMIS`, hex del payload de 150/100 bits, y las
formas binarias (payload150, payload100, sus SHA-256 hex) como contraseñas literales.

- 25 candidatos-texto × perfiles {gsmg (convención probada: sha256 hex + EVP-SHA256), raw,
  gsmg-md5, raw-md5} × 3 sobres (J/s, terminal 3.2, Cosmic) + 2×2×3 formas binarias = **276 descifros**.
- Único padding válido: `bytenphasegbdoel4yjksvtml2ksdb` (perfil raw, sobre Cosmic) pad=**1**,
  imprimible 0,358 — exactamente el nivel de ruido 1/256 documentado (750/731,9 históricos).
- Puerta DBBI (autenticación ~2⁻²¹¹ por digest): **0/25**.
- Material derivado como escalar secp256k1 (25 formas, comprimida y sin comprimir): **0** aciertos
  frente a Half / Better Half.
- Reproduce de forma independiente los 144 descifros negativos de rayceja, añadiendo el perfil de
  la convención probada y la puerta DBBI.

## 5. Anclaje documental de las dos piezas nuevas del issue (J4)

1. **«One for one, four for one»** — la pista existe en el corpus, pero pertenece a la página de
   **fase 3.2** (terminal): su significado verificado en la cadena resuelta es el tablero
   estridente (straddling checkerboard) del **cifrado VIC con dígitos reservados 1 y 4**
   (README/caderno Naddiseo; el mismo texto nombra también EBCDIC 1141 y Beaufort para esa página).
   La frase **no aparece** en la página de SalPhaseIon. La lectura de akaVARU («cuatro por una → el
   4.º carácter pasa a ser el 1.º», para justificar quitar FAE) es un préstamo cruzado de etapa sin
   ningún apoyo en el corpus — y la cuestión de fondo de Naddiseo sigue sin respuesta: ¿para qué
   pondría el creador un «FAE» que no sirve para nada?
2. **`THEPROBLEMIS`** — el monólogo del Arquitecto del propio puzzle (1.539 chars, verificado)
   **no contiene** «choice», «problem», «door» ni «archi» (conteos = 0). La clave solo se obtiene de
   la cita de la película («As you adequately put, the problem is choice» — IMDB), una de varias
   lecturas documentadas de `lastwordsbeforearchichoice` (P1–P5 del marco previo; P1 = transcripción
   Scott Manning línea 105). Como clave Vigenère es plausible; como **respuesta** ya fue negativa
   (familia NULY, E9b/E19: `theproblemischoice` y `theniggardlyandtheproblemischoice`, 0).
3. **Lectura competidora verificada del mismo material:** FAED570 está verificado como texto cifrado
   Bifid (cuadrícula DBIFHCEGA, pliegue período 570) con múltiples señales diseñadas independientes
   (prefijo BTCSEED, SHAKMODEST en el riel impar, Z única en 97 con corte 91/472, anclas 472/479
   ↔ TAKETHEPRIVATEKEY/PRIVATEKEY del monólogo). La capa de sumas de grupos de akaVARU exigiría un
   segundo diseño plantado sobre el mismo bloque con salida solo 10/30 legible — sin eco estructural
   independiente (la salida Bifid sí los tiene).

## 6. Variantes limpias y controles (J5)

- **570 entero (sin mutilar):** 13 formas divisorias (19×30, 30×19, 15×38, 38×15, 10×57, 57×10,
  6×95, 95×6, 5×114, 114×5, 3×190, 190×3, 2×285) × sumas de filas/columnas × 2 convenciones (0=A/1=A)
  × {plano, Vigenère −, Vigenère + THEPROBLEMIS} → 11 «hallazgos» de palabras aisladas
  (NUKES, MAGAS, ELFIC, YOJAN, ORGIC, SERRA, LINJE, COHERT, WASHY, ACMIC, WURST, POTTO, CAROB) —
  exactamente el nivel esperado de azar (~150 lecturas contra diccionario de 370k palabras), ninguna
  frase, ninguna instrucción.
- **Vigenère THEPROBLEMIS** sobre FAED-crudo (mod 26) y sobre la salida Bifid P (ambos signos):
  ruido (mejor hallazgo: HARKED, 6 letras en 570 — esperado ~0,1–0,5 por cadena aleatoria).
- **Controles de mutilación:** quitar los últimos 3 en vez de FAE (o dejar los 3 finales) → basura
  total (prefijo ZIHJYF, espiral RRLDSIY5EZRM7JXC7SJR). La posición del recorte es determinante —
  como cabría esperar tanto de un diseño como de una coincidencia bien afinada.
- **Tecla de dígitos del bloque R1** (63 dígitos, a–i/o → 1–9/0) sobre las 63 sumas
  (suma±dígito, Vigenère de dígitos): ruido. El 63 del bloque R1 es la longitud del texto de la
  instrucción, no un vínculo diseñado con los 63 grupos de 9.

## 7. Registro, criterios y siguientes pasos

**Archivos de esta sesión (en `download/`):** `SALPH_SESION_J_20261123.md` (este informe),
`J_RESULTADOS_SESION_J.json`, `J_OPERACIONES_SESION_J.csv` (276 descifros, uno por fila),
`scripts/sesion_j_bytenphase.py` (reproducible, semilla 20261123).

**Criterios de apertura autenticada — rama BYTENPHASE:** ① sobre verificado ✓ (J/s = corpus,
idéntico); ② cadenas reproducibles ✓ (100 %); ③ KDF probado y variantes ✓; ④ padding ✗ (un `01`
de azar en Cosmic); ⑤ texto/estructura demostrable ✗ (10/30 símbolos, resto indeterminado);
⑥ predicción independiente ✗ (DBBI 0, direcciones 0). **0 de los criterios duros** — idéntico
estado que las ramas A/ZION de las sesiones G–I.

**Siguientes pasos priorizados:**
1. No invertir más cómputo en esta rama salvo nuevo anclaje (p. ej. que el creador confirme
   públicamente una segunda capa sobre FAED, o que otra fase use la misma receta
   suma-de-grupos+Vigenère+XOR de forma verificable).
2. Mantener H-I1/H-I2/H-I3 como frentes principales (lastwords bajo convención probada;
   matrixsumlist como operación real sobre DBBI/FAED; puerta DBBI como autenticador universal).
3. Si el issue recibe comentarios nuevos (verificación del hallazgo de 43.680 claves por parte de
   otros), re-auditar solo las variantes que aporten anclaje nuevo.

**Contabilidad:** +276 ensayos AES (≈9.437 acumulados), +1.024 enumeraciones completas de claves,
+4.000 ensayos Monte Carlo, +~150 lecturas limpias de matriz.
