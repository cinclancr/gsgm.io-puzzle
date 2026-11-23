# FASE32_HIPOTESIS.md — hipótesis nuevas de la auditoría L (2026-11-23)

**Contexto verificado:** el texto de fase 3.2 (2.422 B exactos, sha256
`b82afeb86f9e50848220f9b64b744b821400308aea273a1c949b9d2d0e408a34`, pad 10,
11 saltos CRLF intactos) está reconstruido en `FASE32_PLAINTEXT_2422B.bin` y
contiene: monólogo del Arquitecto (1.539 chars) + 149 dígitos VIC + acertijo
final + sobre terminal b45a5e3d embebido. Las 91 letras decodificadas son
`INCASEYOUMANAGETOCRACKTHISTHEPRIVATEKEYSBELONGTOHALFANDBETTERHALFANDTHEYALSONEEDFUNDSTOLIVE`.
Las cuatro aperturas de la cadena 1→4 se reproducen con documentación completa
(`CADENA_1_4_REPRODUCCION.json`); el selector final (35 bloques → d) sigue ABIERTO.

**Instrucciones del creador priorizadas** (todas del monólogo/acertijo, autenticadas):

1. `return to the source codes`
2. `reinserting the prime basics`
3. `twenty-three ciphers, sixteen encryptions and/or seven intertwined passwords`
4. `raising the stakes without extra chances of winning`
5. `as wide as the first one seen`

**Espacio ya cerrado (no se repite):** extracciones por posiciones primas,
operaciones de suma y XOR sobre flujos, reducciones VIC de 149 a 91/100/140,
matrices 10×10 y 10×14, triángulos de la 14×14, 5.040 variantes del alfabeto VIC,
matrixsumlist-como-sumas (11×11 y familias), 19 respuestas de Neo, menú E-TOOL,
23/16/7 y 0x77 como selectores (E18/E18b), calendario b/be sobre rangos primos,
libro de cifras con máscara E10, lastwords 792 AES, ~10.086 candidatos del selector.

---

## H1 — El payload60 como dígitos del tablero estradal (EVIDENCIA ALTA — ejecutada)

**Hipótesis.** «A fubcd-king & oracle-queen, thingky mvps, on a sad board but as
wide as the first one seen» nombra las piezas del tablero estradal de fase 3
(GSMG-CLEAN §5b: «the hint sentence spells it out»). El objeto sin explicación
más fuerte del corpus es el payload de 60 dígitos del calendario b/be
(`difhcc…`, sha256 21cbfa18…). Si «a sad board as wide as the first one seen» =
un segundo tablero estradal de la misma anchura, el payload60 podría ser su
material de dígitos: 60 dígitos → ~30 letras → contraseña del terminal o del selector.

**Prueba objetiva (ejecutada, `scripts/fase32_hipotesis1.py`).**
(a) El mapeo dígito→letra del tablero se derivó PROGRAMÁTICAMENTE alineando los
149 dígitos históricos con las 91 letras conocidas (sin suposiciones):
straddles confirmados (1,4); celdas F=0,U=2,B=3,C=5,D=6,O=7,R=8,A=9,
L=11,E=12,T=13,H=14,I=15,N=16,G=17,K=18,Y=19,M=40,V=41,P=42,S=43 — 21 celdas.
(b) El payload60 se decodificó sobre ese tablero: `?ADRBBOARICAROOCOCUOCRRCRRDN?`
RDDBPDBBBODCOOCBSADDDOAOCC?` — RUIDO (5 celdas del cola 44-49 no usadas por
los 149 dígitos históricos, texto sin sentido).
(c) 9 candidatos (decodificación/directo/sha256hex/raw × 3 formas) × EVP-{MD5,SHA256}
× {terminal b45a5e3d, urlblob} = **0 aperturas**.

**Estado: NEGATIVA.** El payload60 no es material de dígitos del tablero estradal
histórico. Registrada en PRUEBAS_NEGATIVAS.csv (N60).

## H2 — Autenticación documental del acertijo final (EVIDENCIA ALTA — ejecutada)

**Hipótesis.** El acertijo final de fase 3.2 describe la ruta real del sobre
terminal: «Raising the stakes» = derivar el WIF («stakes» = billetera/clave
privada); «A fubcd-king & oracle-queen, thingky mvps» = las piezas del tablero
estradal; «on a sad board but as wide as the first one seen» = el tablero con
la misma anchura que el primero (el de fase 3); «without extra chances of
winning» = determinista (sin fuerza bruta).

**Prueba objetiva (ejecutada).** Verificación programática del mapeo:
`FUBCD` ∈ tablero VIC (primeras 5 letras) ✓; `THINGKYMVPS` ∈ tablero VIC
(subcadena literal) ✓; letras de KING/QUEEN/ORACLE todas en el tablero+cola ✓;
rey blanco (Kg8) y rey negro (ke4) presentes en el FEN de fase 3 ✓;
`12/16 = 0,75` de los términos del acertijo cierran sobre materiales auténticos.

**Estado: VERIFICADA (documental).** El acertijo ES la clave del tablero (ya
documentado por GSMG-CLEAN) y su lectura coherente apunta al WIF como ruta del
terminal — consistente con la autenticación de la cadena 2 por cruce comunitario
previo. No produce transformación nueva por sí misma; refuerza la clasificación
de la cadena como genuina.

## H3 — El plaintext de 2.422 B sobre tablero de ancho 14 con extracción prima (EVIDENCIA MEDIA — formulada, no ejecutada aún)

**Hipótesis.** «Return to the source codes» = el texto fuente de fase 3.2 (los
2.422 B reconstruidos); «as wide as the first one seen» = el tablero 14×14 del
póster (el primero visto en el puzzle); «reinserting the prime basics» = marcar
las posiciones/filas primas. La transformación: volcar los 2.422 B en una
cuadrícula de 14 columnas, extraer los bytes en filas/columnas/posiciones primas
y comparar el material resultante con payload60/dbbi/faed (reproducción
estructural); solo ante coincidencia exacta escalar a contraseña.

**Prueba propuesta (objetiva).** 14 variantes (fila/columna/ambas, primos
1-based/0-based, directo/inverso) contra los materiales conocidos; criterio de
coincidencia exacta de cadena (no AES hasta verificar estructura). **Pendiente
de ejecución por orden de prioridad** (ver limitaciones al final).

## H4 — El operando de 29 B de la cabecera de cadena 4 (EVIDENCIA MEDIA — ejecutada, negativa)

**Hipótesis.** La cabecera de cadena 4 («+-» 2b2d + operando de 29 B) nunca fue
decodificada. «+-» podría ser una instrucción aritmética (suma/resta) sobre los
35 bloques y el operando la máscara/selector de bloques.

**Prueba objetiva (ejecutada).**
(a) Operando como máscara XOR repetida sobre los bloques → ruido (imprimible 0,16-0,38).
(b) Bloques[i] ± Bloques[j] mod N para los pares del acertijo (23±16, 16±7,
23±7, pares 0x77 adyacentes) → d·G vs pubkey del premio = **0 coincidencias**.
(c) Suma/XOR de los 7 bloques con 0x77 → 0 coincidencias.
(d) El operando como escalar (BE/LE) → 0 coincidencias.

**Estado: NEGATIVA.** Registrada (N61).

## H5 — Segunda lectura EBCDIC de la zona de letras (EVIDENCIA BAJA — formulada, no ejecutada)

**Hipótesis.** «Return to the source codes» podría referirse a la zona EBCDIC
(bytes 447-1985 del plaintext) del código fuente original: una segunda lectura
con codepage alternativo (p. ej. EBCDIC-CP037 vs CP500/CP1026) revelaría material
no leído. **Pendiente; probabilidad baja** (la lectura histórica ya produce el
material coherente del Bifid-570/monólogo).

---

## Orden de ejecución y resultado

| # | Hipótesis | Evidencia | Prueba | Resultado |
|---|---|---|---|---|
| H1 | payload60 sobre tablero estradal | ALTA | ejecutada | **NEGATIVA** (ruido; 18 AES = 0) |
| H2 | mapeo documental del acertijo | ALTA | ejecutada | **VERIFICADA** (documental; refuerza autenticidad de cadena) |
| H3 | 2422 B en cuadrícula 14 con primos | MEDIA | formulada | PENDIENTE |
| H4 | operando 29 B / «+-» aritmético | MEDIA | ejecutada | **NEGATIVA** (0/12 contra oráculo) |
| H5 | segunda lectura EBCDIC | BAJA | formulada | PENDIENTE |

**Balance:** la primera hipótesis con prueba objetiva (H1) se ejecutó y resultó
negativa; H4 (barata, misma sesión) también negativa; H2 verifica
documentalmente la ruta del terminal. El frente real del puzzle (regla selectora
35 bloques → d) permanece ABIERTO y las hipótesis H3/H5 no lo atacan
directamente: requieren o bien material nuevo (libro Time-Life «Cosmic
Duality», /TheArchitectChoice) o una premisa de regla nueva con control
positivo independiente — condiciones ya declaradas en ESTADO_GSMG §7.
