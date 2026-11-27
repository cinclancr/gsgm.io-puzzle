# SalPhaseIon — sesión B: continuación reproducible (2026-11-22)

**Alcance exclusivo:** SalPhaseIon. Ninguna clave privada de carteras ajenas se investiga.
Continúa el informe de hoy («104 posiciones primas y separación Bifid 7|91|472») desde el
corpus persistente. Niveles: R = reproducido aquí; CORRECCIÓN = corrije un dato previo;
NEG = negativo acotado; HECHO = aritmética exacta con calificación honesta.

---

## 1. Integridad de fuentes — re-verificada contra el corpus persistente [R]

| pieza | forma exacta | SHA-256 | verificación |
|---|---|---|---|
| DBBI (91) | minúsculas, sin salto de línea | `71fe4625…b6a2c5ca` | = `orig/GSMG-CLEAN/data/DBBI_91.txt` |
| FAED (570) | minúsculas, sin salto de línea | `066191b4…1d5ef3c2` | = `orig/GSMG-CLEAN/data/FAED_570.txt` |
| AES (96 B) | binario | `9e2831e1…4fa7a258` | = `locked_salphaseion_short.bin` (sal `3ab585348552415d`, 80 B ct) |

El flujo compacto 1075 es consistente: `[0:91]`=DBBI, `[91:195]`=binario matrixsumlist
(104 bits → «matrixsumlist», 56 b / 48 a), `[195:765]`=FAED, `z`, campo lastwords
(63 letras → «lastwordsbeforearchichoice»), `z`, campo thispassword (29 → «thispassword»),
`z`, «shabefourfirsthintisyourlastcommand» (literal), línea b64 1 (64), binario enter
(40 bits → «enter»), línea b64 2 (64), «shabefanstoo». Las dos líneas b64 decodifican
byte a byte el blob de 96 B.

## 2. Reproducción de 7|91|472 — confirmada [R]

- Bifid (cuadro de primeras apariciones de DBBI = DBIFHCEGA + resto, sin j; período 570):
  **BTCSEED** al inicio ✓, **Z única en 98** ✓, corte 7|91|472 ✓.
- Mecánica de la Z reproducida: FAED tiene `h` en 49 y 334 (los dos con columna 4);
  con n=570 par, la salida par en 98 = cuadro[col₄₉][col₃₃₄] = cuadro[4][4] = **Z** ✓.
- L5: tokenización `bg` = 64 tokens / 16 códigos; patrón
  `01234556728966286abc61c88b48de3086dd501d5557d6bab5605233df7bbb96` ✓ (idéntico a GSMG-CLEAN).

## 3. Correcciones a los datos de hoy [CORRECCIÓN]

1. **«14 coincidencias de 91 en desplazamientos 0 y 13» no se reproduce.** DBBI vs
   FAED[:91] normalizado a minúsculas da **7** (despl. 0) y **9** (despl. 13); máximo
   16 en despl. 21. Control por 20.000 permutaciones conservando frecuencias: media nula
   9,51, p(≥7)=0,86 — sin señal. La cifra 14/91 debe de venir de otra alineación o de un
   residuo del bug de mayúsculas; en cualquier caso no hay relación DBBI↔FAED.
2. **El «riel impar 100% B/C/D/E» no es un selector diseñado — es un hecho forzado.**
   Las letras a–i del cuadro DBIFHCEGA… viven en filas 0/1; con n=570 **par**, la salida
   impar = cuadro[fila][fila] = la esquina 2×2 {d,b,c,e} y la salida par = cuadro[col][col]
   (25 letras). El riel par **sí contiene i y o** (25 letras, sin j): la nota previa
   «carga sin I/O, 23 letras» era incorrecta. El «selector» de 285 símbolos es un artefacto
   del alfabeto a–i + paridad de n, no una capa de cifrado.
3. (Confirmación) los 104 bits de matrixsumlist son la codificación binaria de la propia
   palabra «matrixsumlist»; usarios como máscara selectora son semánticamente insostenibles
   — coherente con el nulo estadístico p≈0,41 ya reportado.

## 4. Hechos numéricos nuevos [HECHO, con calificación]

- **π(472) = 91 = longitud DBBI**; **π(570) − π(472) = 13 = longitud matrixsumlist**;
  7×13 = 91; π(563)=103; π(98)=25; π(121)=30. La red numérica 570=7+91+472 con
  104=91+13=π(570) y 91=π(472)=7×13 es notable.
- **Pero la explotación directa es degenerada [R]:** R472@primos = 90/91 letras del
  alfabeto {b,c,d,e} + 1 (paridad: p>2 impar ⇒ posición absoluta impar ⇒ riel impar).
  No produce un DBBI-paralelo legítimo; probado además como pieza AES/L5 = nulo (§5).
- **El Z único en 98 replica el idiom del propio flujo**: la página separa campos con `z`
  literal. Lectura estructural: [etiqueta «btcseed»][bloque de 91 terminando en Z][bloque
  de 472] — el M91 es el «campo» natural del que cuelga la etiqueta BTCSEED.
- Payload60 como 30 pares de dígitos: **máximo exactamente 98** (la posición de la Z),
  mínimo 16, suma 1821. El par 7º (98) selecciona precisamente la Z en bifid[1..98].

## 5. Baterías nuevas — negativas y cerradas [NEG]

1. **AES sobre el sobre SalPhaseIon: 504 ensayos** (84 candidatos × 3 formas de contraseña
   {directa, sha256hex, sha256raw} × 2 KDF {EVP_BytesToKey SHA-256, MD5}). Autotest: abre la
   fase 3.2 real con la convención probada (2422 B, pad 10) ✓. Resultado: **4
   padding-válidos, todos pad=1 con imprimible 0,30–0,38** (esperados ≈2 por azar);
   0 legibles, 0 hex64, 0 WIF. **La familia de 4 piezas queda cerrada bajo ambos KDF.**
2. **L5 — el hueco de la sesión de hoy:** el patrón DBBI sobre los 84 candidatos (familia
   4 piezas `dbbi+matrixsumlist+P3+lastwords…` con 27 variantes de P3, separadores `z`/`\n`,
   plantillas de etiquetas de la cadena-1 de H19, piezas sueltas y pares): **0
   coincidencias**. Ninguna construcción probada es «sha256(answer) sustituido».
3. **Re-auditoría de la cadena-1 de H19 (ayer):** `matrixsumlist enter lastwords…
   thispassword matrixsumlist` + MD5 → pad=1, 79 B, imprimible 0,38 = el fluke clásico
   documentado por GSMG-CLEAN («79 B MD5 fluke»). La apertura de ayer no se sostiene;
   coherente con la re-auditoría de hoy (G2/G7).
4. **Payload60 como 30 posiciones 1-based** en bifid[1..98] (incluye el par 98→Z),
   FAED[1..98] y arquitecto[1..98]: ninguna cadena legible.
5. **Payload60 como 30 pares (fila,columna)** contra la matriz 11×11 de DBBI (ceros en
   posiciones primas): 11/30 caen en ceros (azar ≈7,4), conjunto ≠ ceros, dígitos sin
   señal; contra el póster 14×14: 4 B / 0 Y (azar); como índice de celda 1–121: sin señal.
6. **Doble Bifid(570):** IC 0,0742 pero ilegible y sin Z; dec(M91), dec(M90), dec(dbbi),
   enc(dbbi): sin estructura; **M91 ≠ enc(dbbi), ≠ dec(dbbi), ≠ anagrama, 8/91**.
7. **De-Vigenère del riel par con el riel impar de clave** (4 offsets × 2 direcciones):
   IC 0,043–0,046 = uniforme.
8. **Vigenère/Beaufort con las etiquetas del puzzle como claves** (matrixsumlist,
   lastwords…, btcseed, enter, thispassword…) sobre 12 piezas: 168 combinaciones,
   **0 palabras objetivo**; las IC altas son artefactos del alfabeto bcde degenerado.

## 6. Próxima dependencia (frontera honesta)

Ninguna lectura de DBBI / M91 / R472 / 104 primas / payload60 está autenticada ni por el
AES ni por L5. Lo que sí es sólido: (a) el idiom separador z/Z ⇒ M91 es un campo con
etiqueta «btcseed»; (b) el techo 98 del payload60 (= posición de la Z) apunta al bloque
BTCSEED+M91 — pero toda lectura posicional probada es nula. Los frentes que requieren
insumo nuevo siguen siendo: el texto del libro Time-Life «Cosmic Duality», los niveles
L1+ de /puzzle, el material de /TheArchitectChoice, y el experimento declarado pendiente
del frente matrixsumlist (sumas no estándares 11×11 ↔ 30 pares del payload; esta sesión
añade la lectura por coordenadas como negativa adicional y el argumento contable de que
los pares no pueden ser sumas de cobertura: 1821 vs 422/3079).

## 7. Archivos

- `scripts/salphaseion_s1_estructura.py` — reproducción completa (fuentes, campos, Bifid, rieles, π(x), 14/91).
- `scripts/salphaseion_s2_bateria.py` — 504 ensayos AES + L5 (autotest fase 3.2).
- `scripts/salphaseion_s3_payload60.py` — payload60 como posiciones/coordenadas; doble Bifid; de-Vigenère.
- `scripts/salphaseion_s4_vigenere.py` — 168 Vigenère/Beaufort con claves-etiqueta.
- `download/SALPH_S1_ESTRUCTURA.json`, `SALPH_S2_BATERIA.json`, `SALPH_S3_PAYLOAD60.json`, `SALPH_S4_VIGENERE.json`.

**Criterio de victoria (sin cambio):** descifrado AES auténtico con validación
independiente (padding de bloque completo / texto legible / estructura externa) o
coincidencia L5. SalPhaseIon sigue sin resolverse.
