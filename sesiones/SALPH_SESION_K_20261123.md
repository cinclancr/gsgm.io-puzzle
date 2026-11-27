# SalPhaseIon — Sesión K (2026-11-23): cierre de los frentes AES

**Entrada del usuario:** «continua hasta descifrar los aes usa todos los repos e issues validos
que puedan ser utiles» — descifrar los sobres AES pendientes usando todos los repos e issues
válidos disponibles en el corpus local.

**Estado tras esta sesión:** censo COMPLETO de los 41+ sobres `Salted__` del corpus (creador +
comunidad). Siete sobres comunitarios NUEVOS descifrados con contraseña verificada; tres
afirmaciones falsas refutadas; dos preimágenes de URL identificadas; **el urlblob resiste
~1,77 millones de descifrados** (34 candidatos nuevos incluidos) y queda clasificado como
«probablemente NO material del creador». Ninguna clave, WIF ni dirección se reclama.

---

## 0. Resumen ejecutivo

| # | Resultado | Nivel |
|---|---|---|
| 1 | Censo completo: 8 sobres del creador (7 abiertos en sesiones previas + urlblob) + ~33 sobres comunitarios en logs/repos; todos los sales y autores enumerados | Reproducido |
| 2 | Siete sobres comunitarios descifrados con contraseña VERIFICADA: π-user «choiceis» (sha256hex(uncertainty), EVP-SHA256, cita «Fate, it seems, is not without a sense of irony»), S|h ×2 (sha256hex(choice) → «choicisanillusion…» / «starting is easy persistence is an art»), π-user imRzc0slX (contraseña fase-2 → sha256("") como clave demo), Ханыч Z1DO6zvZ (sha256hex(follow_the_white_rabbit) → sha256(causality) hex), k1ng ×3 (clave 3.2 conocida → «gsmg.io/theseedisplanted»), David Doak (backtothebasics, EVP-SHA256, key/iv coinciden con su transcripción, texto-joke íntegro, pad 0x10×16) | Nuevo |
| 3 | Cereal Killer «task» blob descifrado ([bz5Hnj/=v8GEss, EVP-SHA256): WIF 5J7GYaeb… VÁLIDO (checksum ✓, d=268f5d0b…); direcciones 1Cye1VZ2…/1CMstduu… NO están en el inventario de 310 direcciones — material de prueba del solver («i expect you to say bullshit») | Nuevo |
| 4 | Tres afirmaciones de contraseña refutadas: X 08f2d4bf… (2024) y JVTRADER 1vzA0tQR… (2026, «éxito» con plaintext mojibake) — negativas bajo todos los KDF | Refutado |
| 5 | Ataque de preimagen sobre las 13 URLs hex del CDX: **NUEVAS** 21ef0533… = sha256(«anstoo») y 10d6a2c5… = sha256(«humphhopeisthequintessentialhumandelusion»); controles reproducidos (89727c59=sha256(rosa), 4f7a1e4e=sha256(pt cósmico), 0b0f37ec/c1780cbb/e24bd2c0, f9719d6d=doble-sha); 4 URLs siguen sin identificar tras ~12k candidatos | Nuevo |
| 6 | Puerta 1NULY: 5.586 derivaciones EC (sha256(candidato) como d, comprimida+sin comprimir) = 0 aciertos — consistente con las baterías E previas | Negativo |
| 7 | **urlblob (el único sobre del creador sin abrir):** 1.548.801 descifrados EVP + ~75k PBKDF2 + ~141k modos de flujo + 2.448 finales ≈ **1,77 M** sobre 4.711+ candidatos minados de TODOS los issues (31 + comentarios), walkthrough, docs GSMG-CLEAN, logs Telegram 2019-2026, valores de cadena y permutaciones de tokens, × 5 formas de contraseña × {EVP-MD5/SHA1/SHA256/SHA512 × AES-128/192/256; PBKDF2-SHA1/SHA256 × 10k/100k} × {CBC, CFB, OFB, CTR}: TODOS los padding-válidos = ruido pad=1 a tasa de azar documentada (1/256). CERO aperturas genuinas | Negativo — cierre |
| 8 | WAVE GSMG_WAVE_61c752a5.bin = timbre decreciente 0,113 s (8 kHz, 8-bit mono, picos 496/699/982 Hz) del material OP_RETURN de solver (nov 2026) — NO material del creador | Auditado |

**Conclusión de la sesión:** todos los sobres AES del corpus están ahora clasificados. Los 7 del
creador abiertos (cadenas 1→4 + fases) se mantienen; el urlblob resiste todo el espacio enumerable
de contraseñas derivable de issues/repos/logs — la evidencia (rabbit_r1 + esta batería) apunta a
que NO es material del creador o su contraseña está fuera del corpus. El frente real del puzzle
sigue siendo la regla selectora final (35 bloques → d), no los sobres.

---

## 1. Censo de sobres (K1)

Barrido por contenido de todos los archivos del corpus (< 8 MB) con extracción robusta de
`Salted__` tanto en binario como en base64 multilínea (los logs de Telegram cortan las líneas a
64 chars, estilo `openssl -a`). Clasificación:

- **Creador (8):** phase2 (06286612…), phase3 (9fbc451d…), phase3.2 (eefc4c5b…),
  salph_small (3ab58534…), terminal (b45a5e3d…), cosmic (2d3f6fe0…), + las «dos ediciones»
  archivadas del blob pequeño (bab58534…, con 2 bytes de transcripción corrupta) — **todas
  abiertas en sesiones previas** — y el **urlblob (74c974e3…, 112 B)** sin abrir.
- **Comunidad (~33 únicos):** en telegram_by_year 2023–2026 (barrystyle, Diego Schmidt, X,
  Mahfooz, David Doak, S|h, π-user 3.14159…, k1ng 😎, Ханыч, Cereal Killer, Denis Golovkin,
  Heellrzz, JVTRADER…), en issues (urlblob.txt del repo puzzlehunt) y en los repos solver
  (harness.js, demos.js). Atribución por mensaje con fecha y autor.

Hecho estructural: **el creador nunca publicó un sobre en Telegram** (jrk_messages.txt: 0
ocurrencias); todos los sobres comunitarios son demos/retos entre solvers.

## 2. Sobres comunitarios descifrados (K2) — contraseñas verificadas

| Sobre | Autor/fecha | Contraseña | KDF | Texto plano |
|---|---|---|---|---|
| choiceis (80 B) | π-user 2025-07-21 | sha256hex(«uncertainty») | EVP-SHA256, AES-256 | [16 B binarios/transc.] + «iO not without a sense of irony.» ≈ «Fate, it seems, is not without a sense of irony.» (Matrix), pad 16 |
| 5795984b (64 B) | S|h 2025 | sha256hex(«choice») | EVP-SHA256 | «starting is easy persistence is an art\n», pad 9 |
| aa46dd00 (64 B) | S|h 2025 | sha256hex(«choice») | EVP-SHA256 | «choicisanillusion\nI guess it was like this\n\n:D\n», pad 1 |
| e2991cdc (96 B) | π-user 2025 | sha256hex(«causality») (convención fase-2) | EVP-SHA256 | «e3b0c442…7852b855» = sha256("") en hex, pad 16 — demo del formato clave-hex + 0x10×16 |
| 19d433ba (96 B) | Ханыч 2026-09-15 | sha256hex(«follow_the_white_rabbit») | EVP-SHA256 | sha256(causality) en hex (coincide con su propia afirmación), pad 4 |
| eefc4c5b ×3 (48 B) | k1ng 😎 2025 | clave 3.2 conocida (250f3772…) | EVP-SHA256 | «gsmg.io/theseedisplanted» ×3, pad 8 |
| 4f37245e (304 B) | David Doak 2025 | «backtothebasics» | EVP-SHA256 | key/iv EVP coinciden EXACTO con su transcripción (E118302E…/24E31C49…); texto: «This is a joke. Due to recent events. The guys from the chat have the exact password for the solution, but they don't know what to do with them. […] they don't know what to do)», pad 16 |
| 89a87486 (96 B) | Cereal Killer 2026-09-15 | «[bz5Hnj/=v8GEss» | EVP-SHA256 | WIF válido + 12 B de relleno, pad 16 |

Nota de método: la convención dominante en las demos 2025-2026 es
`contraseña = sha256hex(frase)` + EVP_BytesToKey/**SHA-256** — la misma convención PROBADA de
las fases 2/3/3.2 del creador; la cadena final del creador usa EVP-MD5. Ambas están cubiertas
en todas las baterías.

**WIF del reto de Cereal Killer:** checksum Base58 válido, versión 0x80, sin comprimir:
d = `268f5d0bf787ee1dcf7bf651c94723ce27023a0decbc84ea855509d0e3e2e195`;
direcciones `1Cye1VZ2ztqas8G7CrgMrLYFrzknWQAhyF` / `1CMstduuofveBCEpUqopFyqFQ9Nsh8eB9i` —
no aparecen en DIRECCIONES_TODAS.csv (310 entradas). Es material del reto, no del creador.

## 3. Afirmaciones falsas refutadas (K3)

1. **X (2024-10-21):** «password: 08f2d4bf9b355798419ad5786581891f6eeca4018347555030c7479b5bbde9e9»
   para la cabeza del sobre terminal — NEGATIVO bajo EVP-{MD5,SHA1,SHA256} × {128,192,256}.
2. **JVTRADER (2026-01-19):** «password 1vzA0tQRHbnXKd9C0W1yJ3C:vzDWa4yEERR, pbkdf2 sha1 aes-128»
   con «PLAINTEXT» mojibake — NEGATIVO en ambos sobres del creador bajo todos los KDF
   (incluida su combinación exacta pbkdf2-sha1); el «éxito» anunciado procede de una
   herramienta online que acepta cualquier contraseña.

## 4. Preimágenes de URL (K4) — técnica nueva

La convención «descifra una etapa → sha256(plaintext) → siguiente URL» (rabbit_r1) convierte el
CDX en un oráculo de preimagen de 32 bits por URL. Sobre las 13 URLs hex del CDX:

- **NUEVAS (esta sesión):** `21ef053324184a4d…` = sha256(**«anstoo»**) — el token final de la
  página SalPhaseIon («shabefanstoo»); `10d6a2c5320bfbd4…` = sha256(**«humphhopeisthequintessentialhumandelusion»**).
- Controles reproducidos: 89727c59… = sha256(rosa = texto del póster);
  4f7a1e4e… = sha256(plaintext cósmico) ✓; 0b0f37ec/c1780cbb = variantes «hope…»;
  e24bd2c0 = «ourfirsthintisyourlastcommand»; f9719d6d = sha256(sha256_raw(rosa)).
- Sin identificar (4): 673e3b1a…, a2aefdbb…, aca20ae7…, c2eef34b… — resisten ~12k candidatos
  (pool completo + familias rosa/poema/Decentraland/Mr.Robot/citas Matrix/frases del creador en
  todas las normalizaciones). Eran conjeturas privadas de los probers de 2025-11/2026-01.

## 5. urlblob — batería de cierre (K6)

Candidatos: 4.711 minados (issues 31 cuerpos + todos los comentarios disponibles, walkthrough,
15 docs GSMG-CLEAN, claims de Telegram 2019-2026, valores de cadena K/E/WIF, permutaciones de
tokens ×720, E-fields ×144, XOR-token ×64, URLs CDX) + 34 nuevos de esta sesión.
Formas: direct / sha256hex / sha256raw / md5hex / fromhex.
KDF/modos: EVP-{MD5,SHA1,SHA256,SHA512} × AES-{128,192,256} CBC; PBKDF2-{SHA1,SHA256} ×
{10k,100k}; CFB/OFB/CTR. Total ≈ 1.770.000 descifrados.

Resultado: 669 eventos padding-válidos, **todos** pad=1 con imprimible 0,33-0,46 (ruido a la
tasa histórica documentada 1/256 ≈ 750/731,9); cero eventos con pad≥8, cero `Salted__` interior,
cero texto >0,85 imprimible. Combinado con el barrido comunitario previo (issue #106: ~56k
candidatos × todas las dimensiones openssl = 0), el frente queda **CERRADO**: o el urlblob no es
material del creador (clasificación rabbit_r1: solo visto como URL en 2026; los 6 sales reales
del creador nunca se entregaron como URL), o su contraseña no es derivable del corpus público.

## 6. WAVE (K7)

GSMG_WAVE_61c752a5.bin (948 B): RIFF/WAVE PCM 8-bit mono 8 kHz, 0,113 s, señal decreciente
(rms 38,7→17,4 por bloques de 113 muestras), espectro 496/699/982 Hz, sin XOR-constante de
texto, sin estructura de datos. Es el chime del OP_RETURN de solver (nov 2026) — no material del
creador. DEPRIORIZADO.

## 7. Contabilidad y criterios

**Ensayos de esta sesión:** +~1,77 M descifrados AES (urlblob + demos), +~12k hashes de
preimagen URL, +5.586 derivaciones EC (1NULY), +1 análisis de audio. Acumulado AES del
proyecto: ≈ 11,2 M.

**Criterios de apertura autenticada (urlblob):** ① sobre ✗ (no en materiales del creador;
solo CDX 2026 como URL), ② ✗, ③ KDF probados exhaustivamente ✓, ④ padding ✗ (solo ruido),
⑤ texto/estructura ✗, ⑥ predicción independiente ✗. **0/6 — cierre como frente.**

**Siguientes pasos priorizados:**
1. NO invertir más cómputo en el urlblob salvo material nuevo del creador (p. ej. si el creador
   publica su contraseña o el blob aparece servido en gsmg.io con contenido real).
2. Frente principal sin cambio: regla selectora final (35 bloques de 32 B → d con d·G = pubkey
   del premio) + vigilancia on-chain de 1GSMG1/bc1pwc9 (sesiones F).
3. Las 4 URLs no identificadas del CDX solo valen si alguien publica la lista de conjeturas
   del prober (inteligencia, no cripto).

**Archivos de esta sesión (en `download/`):** `SALPH_SESION_K_20261123.md` (este informe),
`K_RESULTADOS_SESION_K.json`, `K_OPERACIONES_SESION_K.csv`. Scripts reproducibles en
`scripts/`: `sesion_k_candidates.py`, `sesion_k_battery.py` (v1/v2/v3),
`sesion_k_verify.py`, `sesion_k_preimage.py` (v2/v3), `sesion_k_final.py`,
`sesion_k_wave_analysis.py`.

**Ninguna clave, WIF ni dirección se reclama. El puzzle sigue SIN RESOLVER.**
