# AUDITORIA_L_ERRATA.md — corrección documentada de la auditoría L
**Sesión L-errata (2026-11-23, consolidación del repositorio). Mandato del usuario:
«corregir la auditoría L». Método: re-verificación independiente de cada afirmación
objetiva de `AUDITORIA_CRITICA.md` contra los datos subyacentes; corrección por
documento + evidencia + commit; el texto original se conserva sin reescribir.**

Resultado de la re-verificación: **4 erratas confirmadas** (E1–E4; E4 añadida en
la consolidación del 2026-11-27), **3 positivos confirmados** (P1–P3) y ninguna
afectación a las conclusiones de la auditoría (§7). Evidencia reproducible:
`scripts/l_errata_evidence.py` → `resultados/L_ERRATA_EVIDENCIA.json` (E1–E3) y
`resultados/L_ERRATA_E4_EVIDENCIA.json` (E4).

---

## E1 — Distribución del barrido v3 (§3.3, punto 3)

**Texto original:** «La distribución completa del barrido v3: 6.129 eventos =
6.362 pad-1 + 20 pad-2 + 1 pad-16».

**Defecto:** aritméticamente imposible — 6.362 + 20 + 1 = **6.383**, no 6.129 (un
subconjunto no puede superar al total).

**Evidencia** (`scripts/k_sweep_v3_results.json`, sha256 `8c5b4f73…e1681a1`;
resumen en `resultados/k_sweep_v3_resumen.json`):

| Batería | Eventos | pad-1 | pad-2 | pad-16 | Suma |
|---|---|---|---|---|---|
| EVP (AES-CBC, PKCS#7 real) | 6.129 | 6.109 | 19 | 1 | 6.129 ✓ |
| PBKDF2 | 254 | 253 | 1 | 0 | 254 ✓ |
| Stream (CFB/OFB/CTR) | 0 | — | — | — | 0 ✓ |
| **Combinada (EVP+PBKDF2)** | **6.383** | **6.362** | **20** | **1** | **6.383 ✓** |

**Corrección:** la frase mezcló el total de la batería EVP (6.129) con la
distribución combinada EVP+PBKDF2 (que suma 6.383). Lecturas correctas:
- EVP solo: **6.129 = 6.109 pad-1 + 19 pad-2 + 1 pad-16**;
- distribución completa: **6.383 = 6.362 pad-1 + 20 pad-2 + 1 pad-16**
  (el pad-16 sigue siendo el control positivo «choiceis» de π-user, imprimible 0,771 ✓).

## E2 — Alcance del barrido v3 (§3.3, punto 3, suplemento)

**Defecto:** el texto presenta los totales 6.129/6.383 en el contexto del urlblob
sin declarar que el barrido v3 cubrió **9 sobres** (urlblob + 8 demos comunitarias).
El conteo por sobre (`counts` del JSON): urlblob 669, demos 625–715.

**Evidencia:** urlblob solo = 669 EVP + 26 PBKDF2 = **695 eventos** (693 pad-1 +
2 pad-2, 0 pad-16). Los 2 eventos pad-2 de urlblob (candidatos «tools\\», imprimible
0,372; y «lastwordsbeforearchichoicethispasswordsecondanswermatrixsumliste»,
imprimible 0,415 — ruido) **contradicen el «todos pad=1» del informe K (§5)** —
errata suplementaria del informe K que la auditoría L no había cubierto.

**Corrección:** la nota «669 = solo el barrido v3» es correcta (669 = EVP de urlblob
en v3) y se mantiene; añádese: «(más 26 PBKDF2 → 695 eventos de urlblob en v3; el
barrido v3 cubrió 9 sobres en total)».

## E3 — Longitud de la preimagen de 10d6a2c5 (§3.2, punto 2 y §1 fila 6)

**Texto original:** «la preimagen real es humphhope…weakness (100 chars — la cita
completa de la película, sin puntuación)».

**Defecto:** la preimagen correcta mide **109 chars**, no 100.

**Evidencia** (re-computado): la cadena
`humphhopeisthequintessentialhumandelusionsimultaneouslythesourceofyourgreateststrengthandyourgreatestweakness`
tiene exactamente 109 caracteres y su sha256 es
`10d6a2c5320bfbd47d35f18dd67f177ae5a5f4b5d18a8a5127361c2941a92908` ✓ (empareja
`10d6a2c5…`). La forma truncada (41 chars) da `f156d167…` como decía la auditoría.
**El hash y la identificación de la preimagen son CORRECTOS; solo la anotación de
longitud (100) es errónea.** La §1 fila 6 hereda la misma anotación («frase completa
de 100 chars») y se corrige igualmente a «frase completa de 109 chars».

---

## E4 — Colisión de IDs N60–N63 del libro mayor de negativas (§6/§7/§9) — añadida 2026-11-27

**Defecto:** la auditoría L registró sus 4 familias de negativos como **N60–N63**
en `PRUEBAS_NEGATIVAS.csv` (citadas así en §6, §7 y §9 de `AUDITORIA_CRITICA.md`),
pero esos IDs ya estaban ocupados por filas anteriores de la sesión F
(2026-11-22, N60–N66, presentes en el mismo libro mayor). Espacio completo de la
serie N tras revisar todos los ledgers: `negative_ledger.csv` N01–N16 (ledger
previo); libro mayor N17–N56 + N60–N66 (sesión F); ledger propio de la sesión H
**N67–N75** (`H_PRUEBAS_NEGATIVAS_SESION_H.csv`, corpus local); N57–N59 citados
en textos (sesión G / sesión D del investigador) sin filas en ledgers.

**Corrección:** las 4 filas de la auditoría L pasan a **N76–N79** (primeros IDs
libres de la serie): N60→**N76** (H1 payload60/tablero estradal), N61→**N77**
(H4 operando 29 B / «+-»), N62→**N78** (erratum preimagen 10d6a2c5), N63→**N79**
(erratas menores sesión K). Ningún otro campo cambia. Las citas «N60/N61» de
§6/§7 y «+N60-N63» de §9 se leen con este mapa.

**Evidencia** (`resultados/L_ERRATA_E4_EVIDENCIA.json`): detección programática
de duplicados antes/después; libro mayor de 51 filas, rango N17–N79, sin
duplicados ni colisiones con ningún otro ledger de la serie N. Nota de proceso:
durante la corrección un primer writer falló a mitad de escritura y truncó el
archivo; se recuperó con `scripts/l_ledger_recover.py` (copia historico N17–N53
byte-verificada contra las filas supervivientes + 14 líneas de la lectura íntegra
previa al daño) verificando que el estado recuperado reproducía exactamente el
conteo verificado antes del daño (51 filas, duplicados N60–N63, rango N17–N63).

---

## Positivos confirmados (lo que la auditoría L tiene correcto)

- **P1:** `sha256("anstoo") = 21ef053324184a4d…` ✓ (re-computado).
- **P2:** el plaintext de fase 3.2: 2.422 B exactos, sha256 `b82afeb8…408a34` ✓
  (verificado desde `datos/fase32_plaintext_2422b.hex`).
- **P3:** el resumen del barrido v3 concuerda con el archivo fuente completo
  (ancla de hash coincidente) ✓.
- También re-verificados durante la consolidación: censo = 81 sobres (7 creador /
  3 corruptas / 7 parciales / 20 extendidas / 44 comunitarias ✓ vs
  `MANIFEST_SOBRES.csv`); `AUDITORIA_DEMOS_L.json` = 41 verificaciones ✓;
  plaintexts de cadena 3 (1.327 B, `4f7a1e4e…`) y cadena 4 (1.151 B, `e4269ed5…`) ✓.

## Impacto en las conclusiones

**Ninguno.** Las tres erratas son de anotación (transcripción de totales y una
longitud); no tocan eslabones, contraseñas, hashes ni clasificaciones de la §2/§7.
El estado consolidado de la auditoría L queda como fue emitido, con estas
correcciones anexadas. La regla «una errata se corrige con documento + evidencia +
commit, jamás reescribiendo» queda aplicada y documentada.

## Reproducción

```bash
python3 scripts/l_errata_evidence.py     # E1/E2/E3 CONFIRMADA + P1/P2/P3 OK
# E4: verificación estructural del libro mayor (51 filas, N17–N79, sin duplicados)
python3 - <<'EOF'
import csv
from collections import Counter
rows = list(csv.reader(open('negativos/PRUEBAS_NEGATIVAS.csv', encoding='utf-8')))
ids = [r[0] for r in rows[1:]]
assert len(ids) == 51 and not [k for k, v in Counter(ids).items() if v > 1]
assert {'N76', 'N77', 'N78', 'N79'} <= set(ids)
print('OK')
EOF
```
