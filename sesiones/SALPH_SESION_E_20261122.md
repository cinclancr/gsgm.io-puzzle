# SalPhaseIon — sesión E: la operación `matrixsumlist` — familias no estándar de la 11×11 y el eco 23/16/7 (2026-11-22)

**Alcance exclusivo:** SalPhaseIon. Ninguna clave privada de carteras ajenas se investiga.
Continúa la prioridad declarada al cerrar la sesión D del investigador: **identificar la
operación real de `matrixsumlist` mediante una transformación de estado verificable, en
lugar de enumerar índices arbitrarios**. Niveles: R = reproducido aquí; NEG = negativo
acotado; D = aritmética exacta con calificación honesta; B/C = reportado por el
investigador (archivos publicados, no re-ejecutados aquí).

**Estado tras esta sesión: SalPhaseIon sigue sin resolverse.** El frente declarado abierto
(familias de sumas no estándar de la matriz 11×11) queda **cerrado como negativo con
controles**; se registra un **hecho estructural nuevo [R]** (el eco 23/16/7 también es
byte-consistente) y **8 cierres por contabilidad decisiva** sin enumeración. Por
disciplina de prioridad: **0 ensayos AES nuevos** (ninguna verificación estructural exacta
disparó la receta).

---

## 0. Integridad y autotests [R]

| pieza | verificación |
|---|---|
| dbbi (91) / faed (570) / monólogo (1539) / sobre (96 B) / payload60 | sha256 idénticos al registro (71fe4625…, 066191b4…, 9e2831e1…, 21cbfa18…) ✓ |
| parse certificado 83 (15 b / 8 be; be en 11,23,29,47,61,67,79,83) | reproduce el payload60 **exacto** (91 chars, 0 desacuerdos de token) ✓ |
| marcadores 24 ↔ primos 2..89 | amarillo **479**, azul **484**, total **963** ✓; monólogo[479:489] = `PRIVATEKEY` ✓ |
| L2 de la librería | 7×12, columnas, mod 26 A=0 = `hillfexmgsgq` **reproducido** ✓ |
| matrices 11×11 (0/1-based) | idénticas al volcado MATRIX_11x11_DDBI.json ✓ |

Mono complementarios del puente L1 [R, sin promoción]: [484:494] = `TEKEYYOUVE`,
[963:973] = `EEDINGLYEF` — sólo 479 aterriza limpio (`PRIVATEKEY`); el puente
suma→índice sigue siendo una curiosidad de nivel B, no una operación.

## 1. Contabilidad decisiva — cierres sin enumerar [D]

Totales: payload60 = 60 dígitos (**336**); 30 pares (**1821**); matriz de ceros (**422**);
matriz de primos reinsertados (**422 + 1593 = 2015**); `p_i + d_i` (i-ésimo primo + i-ésimo
dígito de payload) = **1773**.

1. Pares como cobertura exacta de la matriz de ceros: 422 ≠ 1821 (y ≠ 336) — **imposible**.
2. Pares como cobertura exacta de la matriz de primos: 2015 ≠ 1821 — **imposible**.
3. Pares = pares de dos primos con cada primo usado 2 veces: 2×1593 = 3186 ≠ 1821 — **imposible**.
4. Pares = p_i + d_i (pareo por orden): 1773 ≠ 1821 — **imposible**.
5. Segmentos entre nulos (cualquier recorrido): total 422 ≠ 1821 — **imposible**.
6. Dominós con nulo=0: rango 1..9 < 16 (par mínimo) — **imposible**.
7. Bloques 2×2 con nulo=0: par máximo 98 > cota 4×9 = 36 — **imposible**.
8. Mapa de ediciones (22 filas estables) como lista de 30 pares / 60 dígitos: longitudes
   incompatibles — **imposible** (cierra «longitudes de edición como sum-list» sin enumerar).

## 2. E1 — familias no estándar de la 11×11 [NEG]

112 listas de valores (2 indexados × {ceros, primos reinsertados}):

| familia | listas | resultado |
|---|---|---|
| dominós canónicos (lectura, espiral-póster, siguiente-no-nulo) | 12 | mejor prefijo 1/30; totales 142–1748, ninguno 1821 |
| bloques 2×2 (top-left mínimo y bottom-right máximo) | 8 | mejor prefijo 1/30; con ceros ≤ 36 (cota); con primos sin coincidencia |
| índices espirales de los 30 nulos (4 recorridos × 2) | 8 | 60 dígitos ≠ payload60 (posicional, sin MC) |
| sumas acumuladas en nulos (4 espirales × {ceros, primos} × {brutas, mod 100}) | 32 | sin coincidencia |
| segmentos cíclicos entre nulos (4 espirales × 2) | 16 | cerrado además por contabilidad (422) |
| coordenadas (r,c)/(c,r) bajo 8 simetrías | 32 | ninguna igualdad con los 30 pares |
| sumas estándar de la matriz de PRIMOS (filas/columnas) | 4 | sin coincidencia con payload60/479/484/963 |

- **Controles Monte Carlo** (800 permutaciones, multiconjunto conservado): dominó
  siguiente-no-nulo (primos) real = 0/30, p = 1,0; bloques (primos) real = 0/30, p = 1,0 —
  ninguna señal sobre el ruido.
- **Positivos plantados**: comparador de pares (dispara), fontanería de bloques (caso 3×3
  manual: tl = 7, br = 23 ✓), espiral del póster (caso 3×3 ✓), dominó con matriz sintética
  por regla real: 29/30 (el conflicto estructural nulos-2/3 que comparten el
  siguiente-no-nulo limita el máximo). Los comparadores y la fontanería quedan validados.
- **Micro-objetivos** {479, 484, 963, 336, 1821, 1593} en las 112 listas: **ninguno**.

**Conclusión [NEG]:** ninguna familia canónica de pares de celdas, bloques de 4, espirales,
coordenadas o primos reinsertados reproduce los 30 pares del payload60. La lectura
«matrixsumlist = sumas (estándar o no estándar) de la 11×11 de dbbi» queda cerrada en su
espacio canónico; lo que queda fuera es asignación libre (enumeración arbitraria), que la
prioridad declarada excluye.

## 3. E2 — el eco 23/16/7 y la anchura 14 del acertijo [NEG]

El acertijo del tablero («…on a sad board but as wide as the first one seen») y la sustitución
del Arquitecto («23 ciphers, 16 encryptions, 7 passwords») motivaron el barrido de los valores
de celda de los dos parses bajo formas con anchura 14:

- parses {84-celdas (23/16/7), 83-celdas certificado} × signos {b−/be+ (librería), b+/be−,
  b−/be−, b+/be+} × formas {6×14, 14×6, 7×12, 12×7, 4×21, 21×4, 3×28, 28×3, 2×42, 42×2,
  plano} × lecturas {filas, columnas, ambas} × mod 26 {A=0, A=1} = **336 salidas**.
- Objetivos: hill-282, vic-91 (mensaje del tablero), dbbi, faed-91, M91, R472, payload60,
  `hillfexmgsgq`, `privatekey`.
- **Resultado: 0 coincidencias nuevas.** La única igualdad es la **reproducción** de
  `hillfexmgsgq` (parse 84, b−/be+, 7×12, columnas, A=0) — el control positivo de la
  librería, no un hallazgo.
- **Control MC** (1.000 shuffles del multiconjunto, 6×14): tasa de palabras objetivo ≥4
  letras = **0,001** — las salidas mod-26 son ruido; `hillfexmgsgq` es la cola conocida de
  ese ruido bajo una convención forzada (la propia librería lo cavea).

## 4. Hecho estructural nuevo [R]

**El parse de 84 celdas (23 slots primos, 16 b, 7 be — exactamente los números de la
película sustituidos por el Arquitecto) es TAMBIÉN byte-consistente con dbbi**: 0
desacuerdos de token, 91 caracteres consumidos, 61 celdas de carga. El calendario
certificado del póster (F→B entre los marcadores 20/21) selecciona el parse de 83 (15 b /
8 be). El eco 23/16/7 es, por tanto, **aritmética y gramaticalmente admisible**, pero no
la regla realizada — se registra como hecho, sin promoción (coherente con E10: 1 regla
completa de 384).

## 5. Integración de la sesión D del investigador [B/C, reportado]

- Precisión de la tabla pública: **22 intervalos de edición compartidos** por las
  transcripciones (no 24; las dos filas extra son dependientes de la versión del diálogo) —
  coherente con el volcado v2 (Scott/spelled estable: 22 filas).
- Experimento de los 22 intervalos como operadores de selección: **432 extracciones, 396
  secuencias distintas, 3 padding-01 (compatibles con azar, ~20 %), 0 descifrados
  autenticados**; 2.000 controles por permutación sin evidencia positiva. Archivos
  reproducibles publicados por el investigador (script, intervalos, resultados AES y
  controles). Integrado al estado del caso como familia cerrada; no re-ejecutado aquí.

## 6. Qué queda abierto (frontera honesta, sin cambio de criterio)

- La **operación** que conecta dbbi / faed / `matrixsumlist` / «last words before archi
  choice» sigue sin identificarse. Con esta sesión, el espacio «sumas de la 11×11» queda
  agotado en su forma canónica y en su contabilidad.
- El puente L1 (amarillo 479 → `PRIVATEKEY`) sigue siendo la coincidencia operativa más
  limpia del frente color-prima-suma, pero 484 y 963 no aterrizan limpio: una sola
  coincidencia no es una regla.
- Criterio de victoria (sin cambio): descifrado AES auténtico con validación independiente
  o coincidencia L5 (chance 16!/16⁶⁴ = 2⁻²¹¹·⁷ por digest). **0 ensayos AES ejecutados**
  en esta sesión por disciplina de prioridad (la receta canónica sólo se dispara ante una
  verificación estructural exacta; no la hubo).

## 7. Archivos

- `scripts/salphaseion_s6_sesionE.py` (copia: `download/SCRIPTS/`) — batería completa:
  autotests, contabilidad, 112 familias, E2, controles y positivos plantados.
- `download/SALPH_S6_SESION_E.json` — auditoría completa.

**SalPhaseIon continúa cerrado: sin contraseña, sin descifrado autenticado, sin preimagen L5.**
