<!-- Forma markdown extraída del docx original GSMG_SALPH_SESION_H_INFORME.docx
     (informe de sesión H, 2026-11-23). Texto preservado sin editar; el docx/pdf
     permanecen en el corpus local. -->

**G S M G . I O P U Z Z L E — I N V E S T I G A T I O N R E P O R TSalPhaseIon, sesión HVerificación documental de las siete respuestas, calibración del KDF del autor y batería HG2/HG1/HG3 sobre los sobres auténticosCaso GSMG.io 5 BTC — continuación SalPhaseIon hacia Cosmic DualityPrioridades: HG2 (sha256 + respuestas) · HG1 (79 bytes) · HG3 (orden de instrucciones)354 operaciones registradas · 0 aperturas autenticadas · negativos N67–N75Sobre autenticado J/s (8 fuentes primarias, sesión G) — 23 de noviembre de 2026Z.ai — investigación independiente y reproducible 2026-11-23**

Índice

Nota: este índice se genera con campos de código. Para actualizar los números de página tras editar el documento, haga clic derecho sobre el índice y elija «Actualizar campos».

# 1. Resumen ejecutivo

Esta sesión H del caso SalPhaseIon ejecuta las prioridades fijadas por el usuario: HG2 como frente principal (interpretación «shabefanstoo = sha256 + respuestas»), HG1 (estructura de los 79 bytes del descifrado histórico) y HG3 (orden de instrucciones) como frentes conservados, con matrixsumlist y la receta A de Cosmic Duality como hipótesis paralelas. Se registran 354 operaciones individuales (H001–H354) con entrada exacta, KDF, sobre, salida completa y veredicto, y nueve familias de negativos nuevas (N67–N75).

Tres resultados estructuran la sesión. Primero: la calibración del KDF del autor sobre los blobs primarios de fases 2, 3 y 3.2 demuestra de primera mano que el autor cifró con EVP_BytesToKey(SHA-256) — MD5 falla en los tres — lo que corrige la convención de trabajo de las sesiones anteriores, que privilegiaban MD5. Segundo: las siete respuestas de fase 2 (causality, Safenet, Luna, HSM, 11110, el hex del génesis invertido y el FEN) quedan autenticadas de forma triple: su concatenación de 227 caracteres reproduce el hash 1a57c572…, abre phase3.txt con texto legible y su SHA-256 deriva la dirección sembrada por el propio creador 1M5ypvDbp… (OP_RETURN «You are here because 227 chars were correct»). Tercero: ninguna de las representaciones de HG2 (hex textual, digesto binario como clave directa, o SHA-256 por respuesta antes de concatenar) abre el sobre original J/s, el segundo candado de fase 3.2.2 ni Cosmic Duality: cero aperturas autenticadas en 354 operaciones.

El plaintext de 79 bytes del descifrado histórico sigue siendo solo candidato: es estadísticamente indistinguible de bytes uniformes, su padding 01 aislado aparece al nivel del azar (0,35 % medido frente a ~0,39 % teórico) y las direcciones derivadas de K_C1 y K_C2 no tienen ninguna coincidencia no circular con direcciones conocidas del caso.

# 2. Correcciones obligatorias aplicadas

Tabla 1. Estado de las cuatro correcciones exigidas

| Corrección | Aplicación en esta sesión |
|---|---|
| H8/Base64: aceptar J/s como versión histórica y conservar los dos segmentos originales de 64 caracteres | Aplicada. Todos los ensayos usan el sobre J/s (sal 3ab585348552415d) tal como está en el paquete; segmentos A (896–959) y B (1000–1063) sin alterar un solo carácter; la variante R/k no se usa y solo queda inventariada. |
| No declarar autenticado el plaintext de 79 bytes | Aplicada. El descifrado de 5 tokens + EVP-MD5 se reproduce (padding 01, 79 bytes, SHA-256 1449a217…) y se clasifica como candidato; el control aleatorio de 2.000 contraseñas da 7 paddings válidos (0,35 %), es decir, al nivel del azar. |
| No presuponer la división 32+32+15 | Aplicada. HG1 compara esa segmentación con 64+15, 32+47 y 15+32+32 y contra 20.000 controles aleatorios: ningún estadístico distingue los 79 bytes de bytes uniformes; la división queda provisional. |
| No afirmar auditorías sin operaciones individuales | Aplicada. Las 354 operaciones (incluidas las 312 de la batería HG2/HG3) están en H_OPERACIONES_TODAS_SESION_H.csv con texto previo al hash, KDF, sobre, salida hexadecimal completa y veredicto; los barridos externos citados (floflo777) se referencian con su propio registro. |

# 3. Calibración del KDF del autor (hallazgo de base)

Antes de construir contraseñas nuevas se calibró el KDF del autor con los blobs primarios del corpus local y sus claves documentadas y verificadas (sha256 de «causality», de la concatenación de 7 partes y de las tres respuestas de fase 3). El resultado es unívoco y reproducible:

Tabla 2. Descifrado de los blobs de fases 2, 3 y 3.2 bajo ambos KDF

| Blob (sal) | Contraseña documentada | EVP_BytesToKey(MD5) | EVP_BytesToKey(SHA-256) |
|---|---|---|---|
| phase2.txt (06286612…) | eb3efb51…d07e5bf = sha256(causality) | padding inválido; 41 % imprimible | VÁLIDO: «The ironic 2name of the keymakers trying…», 100 % imprimible |
| phase3.txt (9fbc451d…) | 1a57c572…2ec30d5 = sha256(concat 227) | padding inválido; 38 % imprimible | VÁLIDO: «What if the merovingian is wrong…», 100 % imprimible |
| phase32.txt (eefc4c5b…) | 250f3772…61ce4c = sha256(3 respuestas) | padding inválido; 38 % imprimible | VÁLIDO: «I've been waiting for you…», 59,8 % imprimible (bloque EBCDIC) |

Esta calibración coincide con la convención que el propio autor dejó escrita en la página archivada de fases 2 y 3 (captura Wayback 2020-11-12, citada por el repositorio floflo777): «Ciphered with aes-256-cbc /w base64 sha-256(password)» y, para la respuesta de siete partes, «parts 1..7 -> sha-256 -> dgst is the password». Consecuencia operativa: los barridos futuros deben priorizar EVP_BytesToKey(SHA-256) con contraseña sha256hex, y usar MD5 solo como secundario. La afirmación de terceros de que Cosmic Duality usa MD5 no está verificada de primera mano: el hash de plaintext que la respalda (4f7a1e4e…) fue publicado por un solver y su propio repositorio lo reclasifica después como accidente de padding (93/20.000 claves aleatorias dan padding válido).

# 4. HG2 — Verificación documental de las siete respuestas

Las siete respuestas de fase 2/3 se verificaron documento a documento antes de cualquier ensayo criptográfico. Ninguna se asume como «las siete contraseñas entrelazadas» del discurso del Arquitecto: son la respuesta de siete partes que abre la fase 3, y la pista «shabefanstoo» es la que sugiere reaplicarles el método sha256.

Tabla 3. Las siete respuestas: fuente, ubicación, derivación, texto exacto, estado y posición

| # | Texto exacto | Fuente original y ubicación | Método de derivación | Estado | Posición en la concat. (base 1) |
|---|---|---|---|---|---|
| 1 | causality | Página de fase 2 (Matrix Reloaded, el Merovingián: «causality — cause and effect»); VERIFIED-SOLUTIONS.md §Phase 2; issue #68 | Contraseña de la página; además parte 1 de la respuesta | CONFIRMADA (hash) | 1–8 |
| 2 | Safenet | Plaintext de phase2.txt (acertijo Mr. Robot): «the ironic name of the keymakers…» | Ironía del nombre del producto Thales/Gemalto SafeNet (HSM) | CONFIRMADA (hash) | 9–15 |
| 3 | Luna | Acertijo: «Crypto finally to the latin 3Moon?» | Luna = «luna» en latín; producto SafeNet Luna | CONFIRMADA (hash) | 16–19 |
| 4 | HSM | Acertijo: «4How so mate?» | Iniciales de la propia frase; Hardware Security Module | CONFIRMADA (hash) | 20–22 |
| 5 | 11110 | LSB de la imagen 14×14 (azul=1, amarillo=0): primeros cinco bits 11110; Naddiseo/unverified/11110.md | Valor necesario para reproducir el hash; significado EO 11110 (JFK) no verificado (brute-force parcial reconocido) | Valor CONFIRMADO; motivo ⚠ | 23–27 |
| 6 | 0x736B…656854 (126 chars) | Hex del mensaje del bloque génesis invertido, línea 1616 de main.cpp | Bytes hex invertidos decodifican «…sknab rof tuoliab dnoces… ehT» = «The Times 03/Jan/2009 Chancellor on brink of second bailout for banks» al revés; el prefijo 0x es literal obligatorio | CONFIRMADA (hash) | 28–167 |
| 7 | B5KR/1r5B/2R5/2b1p1p1/2P1k1P1/1p2P2p/1P2P2P/3N1N2 b - - 0 1 | Acertijo de ajedrez del plaintext de fase 2 («Buddhist forced to move») | Posición FEN completa; el reloj de media jugada «0 1» es el manuscrito del autor (el «1 1» de motor da otro hash) | CONFIRMADA (hash) | 168–232 |

Autenticación triple de la concatenación (por orden de fuerza): (1) sha256(concat) = 1a57c572caf3cf722e41f5f9cf99ffacff06728a43032dd44c481c77d2ec30d5, el digesto publicado que abre phase3.txt; (2) el descifro propio de phase3.txt con esa clave bajo EVP-SHA256 produce «What if the merovingian is wrong…», texto legible con padding válido; (3) la clave privada sha256(concat) deriva la dirección comprimida 1M5ypvDbp124ZtKPbg3GJg1JqNs1x7TPoN, financiada el 2020-03-24 por la cartera vanity del creador (3GSMG24…) con el OP_RETURN «GSMG.io: You are here because 227 chars were correct». La longitud medida es exactamente 227 caracteres. La cadena exacta es:

causalitySafenetLunaHSM111100x736B6E616220726F662074756F6C69

616220646E6F63657320666F206B6E697262206E6F20726F6C6C65636E61

684320393030322F6E614A2F33302073656D695420656854B5KR/1r5B/2R

5/2b1p1p1/2P1k1P1/1p2P2p/1P2P2P/3N1N2 b - - 0 1

Nota sobre convención: la forma autenticada conserva mayúsculas exactas (Safenet, Luna, HSM, hex y FEN tal como se publicaron). En la batería se ensayó también la variante todo-minúsculas exigida por la instrucción HG2 («minúsculas, UTF-8, sin espacios ni separadores»); ambas constan en el CSV.

# 5. HG2 — Batería criptográfica sobre el sobre original

Sobres: el original J/s de SalPhaseIon (prioridad, sal 3ab585348552415d, 80 bytes de ciphertext), el segundo candado de fase 3.2.2 (sal b45a5e3d827593ca, misma forma) y, como objetivo posterior, Cosmic Duality (sal 2d3f6fe06dc950e6, 1.344 bytes). Se distinguieron siempre las cuatro construcciones que el usuario exige no confundir: SHA-256 como digesto, EVP_BytesToKey(MD5), EVP_BytesToKey(SHA-256) y clave AES directa de 32 bytes.

Tabla 4. Representaciones ensayadas por conjunto de entrada

| Conjunto de entrada (texto previo al hash) | R1: sha256hex textual | R2: digesto binario como clave directa | R3: sha256 por respuesta antes de concatenar | Resultado |
|---|---|---|---|---|
| S1: concatenación autenticada de 7 partes (227) y su variante minúscula | md5+sha256, 3 sobres | 4 convenciones de IV (ceros, sal×2, md5(sal), sha256(sal)16), 3 sobres | hex 448 chars y binario 224 bytes, 3 sobres, ambos KDF; más clave sha256 de los digestos | 0 aperturas |
| S2: 7 contraseñas de SalPhaseIon (matrixsumlist…secondanswer) y la histórica de 5 tokens | md5+sha256, 3 sobres | idem | idem (7 tokens de la propia página) | 0 aperturas |
| HG3: caption de la imagen inicial (59 chars), su sha256hex 89727c…, URL gsmg.io/89727c…, e inversos de S1/S2/caption | md5+sha256, J/s y 3.2.2 | idem | no aplica | 0 aperturas; 1 padding 01 de ruido (H109) |
| matrixsumlist paralela: sumas de primos de color 479/484/963/5 | md5+sha256, J/s y 3.2.2 | idem | no aplica | 0 aperturas |
| Receta A (yellowblueprimes+matrixsumlist+lastwords+yinyang), su minúscula y la meta-pista de 8 tokens | md5+sha256, 3 sobres | idem | no aplica | 0 aperturas |
| Addendum «hashtthetext»: la propia página SalPhaseIon como texto (compacta 1075, espaciada, sin blobs b64) | md5+sha256, 3 sobres | no | no | 0 aperturas |

Resultado global: 330 operaciones criptográficas (más 24 filas de verificación y HG1 en el CSV maestro), cero aperturas autenticadas. El único padding válido de toda la batería es H109 — sha256hex(sha256hex(caption)) bajo EVP-MD5 sobre el sobre J/s — con último byte 01 y 43 % de imprimibles, la firma exacta del ruido (la referencia aleatoria de la propia sesión da 2/256 paddings válidos). Ningún plaintext superó el 90 % de imprimibles ni produjo palabras del vocabulario del puzzle.

Conclusión de HG2: la interpretación «shabefanstoo = sha256 de las respuestas también» queda descartada en sus tres representaciones para los tres sobres auténticos. La respuesta X que alimenta la contraseña del sobre pequeño no es la concatenación de las siete respuestas de fase 2, ni la de las siete contraseñas de la página, ni el caption, ni la ruta, ni sus inversos, bajo la convención documentada del autor ni bajo MD5.

# 6. HG1 — Estructura de los 79 bytes del descifrado histórico

Los 79 bytes (SHA-256 1449a217…, K_C1 9fa9db91…, K_C2 15173896…, E_C 38d4f4c9…) se usan solo como candidato. Frente a 20.000 controles aleatorios de 79 bytes uniformes:

Tabla 5. Estadísticos observados frente a 20.000 controles aleatorios

| Estadístico | Observado | Percentil entre los controles | Lectura |
|---|---|---|---|
| Entropía (bits/byte) | 6,1266 | 0,955 | dentro del rango aleatorio |
| Chi-cuadrado de uniformidad | 222,4 | 0,082 | dentro del rango aleatorio |
| Proporción de imprimibles | 0,38 | 0,616 | nivel de ruido |
| Racha ASCII imprimible máxima | 5 | 0,887 | sin texto incipiente |

Ninguna partición (32+32+15, 64+15, 32+47, 15+32+32) recibe apoyo estadístico: las entropías de los bloques de 32 bytes (4,875 y 4,9375) son la media aleatoria (4,8818). El WIF sin comprimir de K_C1 reproduce el publicado en el issue #108 (5K2byJMss…), pero ese WIF proviene de un post comunitario derivado del propio K_C1 (validación circular, ya documentada en la sesión G); además, el control demuestra que 1.000 claves aleatorias producen 1.000 WIF sintácticamente válidos: la validez sintáctica no es evidencia.

Direcciones: las direcciones P2PKH de K_C1 y K_C2 (comprimida y sin comprimir) no tienen ninguna coincidencia no circular con el premio 1GSMG1…, la dirección de-split 17ucy…, la tercera puerta 1NULY…, las ocho direcciones sembradas del creador ni el inventario del caso (las dos coincidencias aparentes son las filas C_cadena del propio inventario, generadas de K_C1/K_C2 en sesiones previas). Esto, junto con el barrido de la sesión G (342 combinaciones × 5 formas de dirección frente a 1.529 direcciones), cierra la vía de información verificable para K_C1 y K_C2.

E_C (15 bytes, 38d4f4c90cb45fdfc8cff50d0ed1c5): no cabe como IV de AES (16 bytes) ni como sal (8); la lectura como prefijo/sufijo de contraseña o material del contenedor no tiene evidencia independiente. Las relaciones exploratorias (sha256(K_C1)[:15], sha256(K_C2)[:15], md5 de cada clave, XOR de ambas) son todas falsas; en cualquier caso serían circulares. El «resto estructural llamativo» de 15 bytes se explica de forma más simple: 96 − 16 − 80 = 0 y el plaintext admitido por el contenedor es de 64 a 79 bytes; cualquier plaintext de 64–78 bytes deja un «resto» parecido sin intención alguna.

# 7. HG3 — Orden físico y orden de ejecución; la última orden

El orden físico de aparición en la página (flujo compacto de 1.075 tokens, posiciones base 1) queda documentado así:

Tabla 6. Orden físico de la pista SalPhaseIon (posiciones base 1)

| Etiqueta | Posición (base 1) | Decodificación conocida |
|---|---|---|
| DBBI (91) | 1–91 | clave de primeras apariciones DBIFHCEGA; sin resolver |
| M104 (104 símbolos a/b) | 92–195 | matrixsumlist (ASCII 13×8) |
| FAED (570) | 196–765 | Bifid período 570 → prefijo BTCSEED; cola 472 sin resolver |
| z (separador) | 766 | — |
| Bloque 63 (a–i, o) | 767–829 | lastwordsbeforearchichoice (decimal→hex→ASCII) |
| z (separador) | 830 | — |
| Bloque 29 (a–i, o) | 831–859 | thispassword (decimal→hex→ASCII) |
| z (separador) | 860 | — |
| shabef | 861–865 | lectura publicada: sha256 (hipótesis) |
| ourfirsthintisyourlastcommand | 867–895 | instrucción sin operador identificado |
| Base64 A (64 chars) | 896–959 | primera mitad del sobre J/s; su carácter 64 es la z interna del blob (posición 959) |
| M40 (40 símbolos a/b) | 960–999 | enter (a=0,b=1) |
| Base64 B (64 chars) | 1000–1063 | segunda mitad del sobre J/s |
| shabefanstoo | 1064–1074 | lectura HG2: sha256 + respuestas; ensayada y descartada en esta sesión |

El orden físico no es el orden de ejecución: la cadena de instrucciones visible mezcla material (DBBI, FAED, M104, bloques 63/29, M40), órdenes (shabef, ourfirsthintisyourlastcommand, shabefanstoo) y el propio contenedor cifrado. Las cuatro interpretaciones de la última orden quedaron así:

SHA-256 al final de la concatenación: ensayada como R1/R2 sobre S1, S2, receta A y sumas de primos; 0 aperturas (tabla 4).

Invertir el texto y aplicar SHA-256: inversos de S1 (227), de las 7 contraseñas y del caption, como R1 sobre tres sobres; 0 aperturas.

Primer hint documentado: HASHTHETEXT (espectrograma Decentraland) y «Follow the white rabbit»: el token followthewhiterabbit y hashthetext ya constan como negativos de la sesión E (familia E9); el addendum de esta sesión aplicó literalmente «hash the text» al texto de la propia página (compacta, espaciada y sin blobs) sobre los tres sobres; 0 aperturas.

El caption cuya huella SHA-256 llevó a SalPhaseIon: GSMGIO5BTCPUZZLECHALLENGE1GSMG1JC9wtdSwfwApgj2xcmJPAwx7prBe (59 chars, sin salto final), su digesto 89727c… y la URL gsmg.io/89727c…, en R1/R2 y también hasheados de nuevo; 0 aperturas (H109 es su único padding, de ruido).

Tabla 7. Salidas textuales previas conservadas (no se convierten en contraseñas confirmadas)

| Fragmento | Fuente y posición (base 1) | Nivel de evidencia |
|---|---|---|
| BTCSEED | Bifid(FAED570), 1–7 | reproducido (único período 570 para esa cuadrícula) |
| SHAKMODEST | Bifid(FAED570), posiciones pares 20,18,…,2 | reproducible; selección exploratoria |
| YOUWON | DBBI−VIC mod26, 22–27 | reproducible; método no confirmado |
| NEO | Bifid(FAED570), Morse canal B, 129–147 y 499–519 | exploratorio (dos variantes superpuestas) |
| ENTER | M40 de la página, 960–999 (demostrado); además Morse+Vigenère 377–393 | reproducido (M40) / exploratorio (Morse) |
| GSMG | Bifid(FAED570), Morse+autoclave, 401–415 | exploratorio |
| AES | Bifid(FAED570), 122–124 | literal reproducido |
| END | Bifid(FAED570), 219–221 | literal reproducido |
| BACK | Bifid(FAED570), 227–230 (y lectura cada 13 en 149,162,175,188) | literal reproducido / exploratorio |
| PRANKS | canal C (pares de Bifid), 82–87 | literal reproducible; interpretación abierta |

# 8. Hipótesis paralelas: matrixsumlist y receta A de Cosmic

matrixsumlist (operador real, H1 del dossier): las sumas de primos por color de la matriz 14×14 (amarillo 479, azul 484, total 963, diferencia 5) y sus dos órdenes se ensayaron como texto previo al hash sobre J/s y 3.2.2 (R1/R2, ambos KDF): 0 aperturas. El operador sigue sin identificación; los barridos externos sobre matrices de la imagen y del riel ya constan como negativos (floflo777 tested.md §16; N06 del ledger). El hilo más prometedor documentado para matrixsumlist/yellowblueprimes sigue siendo la pista del creador entre el poema de enero-2020 y el audio de abril-2020 («Yellow has a number and so does Blue», «primes», «zeroed out») aplicada a objetos no textuales, con la tercera puerta 1NULY… como oráculo offline exacto.

Receta A de Cosmic Duality (key = sha256(yellowblueprimes + matrixsumlist + lastwordsbeforearchichoice + yinyang)): ensayada en forma exacta y minúscula, más la meta-pista completa de 8 tokens, sobre J/s, 3.2.2 y Cosmic bajo R1 (ambos KDF) y R2; 0 aperturas. Cosmic Duality permanece cerrado; el addendum «hashtthetext» y las siete respuestas tampoco lo abren.

# 9. Criterios de validación de una apertura — estado

Ningún candidato de esta sesión (ni el histórico de 5 tokens) cumple el conjunto mínimo exigido: ciphertext de procedencia verificada (sí, en todos los casos), contraseña y bytes exactos de entrada (sí, registrados), KDF/clave/IV/modo reproducibles (sí), padding correcto (solo accidentalmente y al nivel del azar), texto legible o estructura binaria demostrable (no), y una predicción independiente no circular (no). El byte 01 aislado de la contraseña histórica y el de H109 quedan registrados como ruido estadístico; un 0202 u otro padding corto tendría el mismo estatus.

# 10. Contabilidad y reproducibilidad

Tabla 8. Registro de la sesión

| Bloque | Volumen | Resultado |
|---|---|---|
| Operaciones individuales registradas (H001–H354) | 354 (330 criptográficas + 24 de verificación/HG1) | 0 aperturas autenticadas |
| Negativos nuevos | N67–N75 (9 familias) | todas negativas; documentadas para no repetirlas |
| Controles de azar | 2.000 contraseñas aleatorias sobre J/s+MD5 (7 paddings válidos, 0,35 %); 256 sobre J/s+MD5 (2); 20.000 controles de 79 bytes; 1.000 WIF aleatorios | el padding aislado queda cuantificado al nivel del azar |
| Barridos externos citados (no repetir) | floflo777: ~335,7 M de reducciones directas; 1.358.577 contraseñas del sobre pequeño (oracle corregido); 5.040 órdenes de las 7 partes × 7 formas × 2 KDF sobre ambos candados; 62,6 M de candidatos 2026-09-01/02 | 0 coincidencias; cubren las lecturas literales de lastwords/thispassword sobre todos los textos disponibles |

Tabla 9. Entregables de la sesión H

| Archivo | Contenido |
|---|---|
| GSMG_SALPH_SESION_H_INFORME.docx / .pdf | este informe |
| H_OPERACIONES_TODAS_SESION_H.csv | las 354 operaciones con entrada, KDF, sobre, salida hexadecimal completa y veredicto |
| H_PRUEBAS_NEGATIVAS_SESION_H.csv | N67–N75 con insumos y resultado |
| SCRIPTS_SESION_H/ (5 scripts) | calibración KDF, verificación documental, batería HG2/HG3, HG1, consolidación y addendum hashtthetext |
| H_VERIFICACION_DOCUMENTAL.json | 7 partes (227), dirección sembrada, sobres, posiciones base 1, descifrado histórico y control de azar |
| H_KDF_CALIBRACION.json | descifrado de fases 2/3/3.2 bajo ambos KDF |
| H_BATERIA_RESULTADOS.json | detalle de las 330 operaciones criptográficas |
| H_HG1_ESTRUCTURA79.json | estadísticos, segmentaciones, WIF/direcciones, control aleatorio, E_C |

# 11. Conclusiones y siguientes pasos

Se confirmó: la convención criptográfica del autor (sha256hex como contraseña + EVP_BytesToKey(SHA-256)) calibrada sobre blobs primarios; la autenticación triple de las siete respuestas de fase 2 y de su concatenación de 227 caracteres (hash, descifro y dirección sembrada del creador); el mapa exacto de posiciones base 1 de la página (1.075 tokens); y la ausencia de toda coincidencia no circular para K_C1/K_C2/E_C. Fallaron: las tres representaciones de HG2 sobre los tres sobres auténticos, las cuatro interpretaciones de la última orden, las sumas de primos de matrixsumlist, la receta A de Cosmic y la lectura literal «hasht the text» de la propia página. Sigue abierto: la respuesta X del sobre pequeño bajo la convención calibrada (EVP-SHA-256 prioritario), el operador real de matrixsumlist sobre objetos no textuales con la tercera puerta como oráculo, y la apertura autenticada de Cosmic Duality.

Pasos concretos propuestos para la sesión I, por orden de prioridad: (1) re-barrido de las familias de contraseñas históricamente ensayadas bajo EVP-SHA-256, ya que las sesiones B–F priorizaron MD5 y las conclusiones de esos negativos están parcialmente descatalogadas por la calibración; (2) explotación del oráculo on-chain del creador (direcciones sembradas y tercera puerta 1NULY…) con construcciones no textuales de la matriz de color — «Yellow has a number and so does Blue / primes / zeroed out» — que es la pista documentada que queda viva para matrixsumlist/yellowblueprimes; (3) si aparece cualquier padding válido con texto, someterlo de inmediato al oráculo de direcciones del propio puzzle (premio, sembradas, tercera puerta) antes de declarar nada; (4) mantener E_C como no-material hasta que exista evidencia independiente.
