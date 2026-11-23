# REPRODUCIBILITY — GSMG.io 5 BTC

## Entorno de verificación

- Python 3.10+ (verificado en 3.12); sin dependencias externas para los scripts de
  este repositorio salvo indicación expresa (hashlib/json/csv/csv estándar).
- `openssl` (solo para reproducciones externas de los eslabones AES; los textos de
  las contraseñas ya están publicados upstream por terceros).
- CI (`.github/workflows/ci.yml`) re-ejecuta los scripts embebidos en cada push/PR.

## Artefactos ancla (SHA-256)

| Artefacto | Bytes | SHA-256 | Forma en este repo |
|---|---|---|---|
| Fase 3.2 plaintext | 2.422 | `b82afeb86f9e50848220f9b64b744b821400308aea273a1c949b9d2d0e408a34` | `datos/fase32_plaintext_2422b.hex` |
| Cadena 4 plaintext | 1.151 | `e4269ed5fbb202a81e5e1aa6b5190fdd1ea126b2c8547ea7cdbdf45387ea135b` | `datos/chain4_plaintext_1151b.hex` |
| Barrido v3 (resultados) | — | `8c5b4f73a014cf5f282555f8c2f796279088d377d3c65bf09526aae02e1681a1` | resumen: `resultados/k_sweep_v3_resumen.json` (archivo completo en corpus local, no hospedado) |
| png del puzzle | 29.931 | `38125bbdf1ea58b9b30b075bc6bf71e4089d04bba37098317e47097e2f2a1830` | corpus local (no hospedado) |

## Scripts ejecutables en este repositorio

```bash
# 1. Verificación de hashes de los datos embebidos
python3 scripts/verifica_hashes.py

# 2. Evidencia de la errata de la auditoría L (§3.2/§3.3 de AUDITORIA_CRITICA.md)
python3 scripts/l_errata_evidence.py

# 3. Hipótesis H3: 2.422 B sobre cuadrícula 14 con extracción prima
python3 scripts/fase32_h3.py
```

Salida esperada: `OK` por verificación, y JSON de resultados en `resultados/`.

## Corpus local completo (no hospedado)

El corpus de trabajo (intake crudo, experimentos 003–072, todos los scripts de
sesión y JSON de resultados) permanece en la máquina de investigación y está
indexado con anclajes de hash en `indice/CORPUS_INDICE.md`. Los materiales binarios
de terceros no se rehospedan en este repositorio (licencias upstream, ver
`SOURCES.md`); los datos necesarios para reproducir las conclusiones embebidas
están en forma textual bajo `datos/`.

## Reglas

- Cada afirmación de estado («VERIFICADA», «NEGATIVA», «NO AUTENTICADO») se apoya
  en un artefacto citado (JSON/CSV/MD) o en un script ejecutable.
- Un resultado negativo también se registra (ledger `negativos/`).
- Ningún script de este repositorio ejecuta fuerza bruta sobre ECDLP/SHA-256/HASH160.
