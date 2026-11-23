# CORPUS_INDICE.md — índice del corpus de investigación local (no hospedado)

**Ancla de integridad del corpus de trabajo completo.** El repositorio hospeda los
documentos maestros, datos textuales y scripts reproducibles de las conclusiones
embebidas; el corpus completo (intake binario, experimentos, todos los scripts y
JSON de sesiones) permanece en la máquina de investigación con esta indexación
verificable por hash. Los binarios de terceros no se rehospedan (licencias upstream).

## 1. Estructura por raíz (conteo y tamaño reales)

| Raíz | Contenido | Archivos | Bytes |
|---|---|---|---|
| orig/gsmgiopuzzle/ | corpus forense (raw intake con provenance, derived, experiments 003-072, scripts, tests, docs raíz) | 517 | 61,675,870 |
| download/ | entregables de sesiones B-L (informes MD/PDF, JSON de resultados, CSV de negativas, SCRIPTS_SESION_*) | 171 | 5,556,792 |
| scripts/ | scripts de todas las sesiones (E1-E21, F, G-L, salphaseion_*, selector_*, batteries) | 229 | 5,184,445 |
| orig/GSMG-CLEAN/ | datos derivados del corpus GSMG-CLEAN (DBBI_91, FAED_570, etc.) | 1449 | 267,996,962 |
| data/ | materiales auxiliares (ipynb salphaseion, words_alpha, informes PDF) | 8 | 4,462,976 |
| resultados/ | salidas nuevas de la consolidación (H3, L_ERRATA) | 2 | 8,969 |

## 2. Documentos maestros del corpus (SHA-256)

| Archivo (local) | Bytes | SHA-256 |
|---|---|---|
| download/ESTADO_GSMG.md | 33,315 | `387c4135f2fef49253cea86f84071441cdef4e917c5350edec5f941da9f3f442` |
| download/HALLAZGOS_NUEVOS.md | 42,062 | `386ecc30927b4361ac4cd8ddeb1e49377591cf9dff3926c38b5dab924ce0c1ac` |
| download/AUDITORIA_CRITICA.md | 17,346 | `c8041880a17a2fccafa2ac9ad8004dfeaf324362d4c0b593ba319841c102afe0` |
| download/FASE32_HIPOTESIS.md | 7,656 | `7fbb95f64204b418f299f364cad10550a20de5adae86395bf8864d56394a7cb3` |
| download/AUDITORIA_L_ERRATA.md (local: repo_push/docs/; hospedado en docs/ del repo) | 5,498 | ver `docs/AUDITORIA_L_ERRATA.md` (repo) |
| download/README.md | 3,052 | `51634b1b617a86d927ac5133e7d0f36726f79d40236fd40596dbbff4e83faf72` |
| CHANGELOG.md (repo raíz) | — | ver `CHANGELOG.md` (repo) |
| download/CONFLICTOS_RESUELTOS.md | 8,643 | `6825112567dba8b4bd5b54ef71e6010e4ce9e5c78beb7773cd2b4efa217f29fd` |
| download/PRUEBAS_NEGATIVAS.csv | 28,329 | `87d9d9bb100f4ca934b38f3ee2a28a3aad386d110b87949845dc24101fb7e918` |
| download/negative_ledger.csv | 5,134 | `85afc46a01611fb62e6a47411fd83701a7c873b0a5cdb1075774268b5ca8c763` |
| download/CADENA_1_4_REPRODUCCION.json | 36,631 | `1899808b58174af0b3a0345ba561b48c68cab205c335fd9ecc0a54a392c37be4` |
| download/MANIFEST_SOBRES.csv | 16,761 | `66b0e7863090b34f321c385b15f1235c9b1ca591670a1486b917d417d933aae1` |
| download/AUDITORIA_DEMOS_L.json | 124,713 | `8b7462952d8c423c41f57db6565c6b7efe7b3728a7cd91d89eaa98ca03e4fbba` |
| download/K_RESULTADOS_SESION_K.json | 6,360 | `b474071af17493e8cd30f462f82b23a36243634939d212560f69fa8ab5afa4f6` |
| scripts/k_sweep_v3_results.json | 1,964,484 | `8c5b4f73a014cf5f282555f8c2f796279088d377d3c65bf09526aae02e1681a1` |
| resultados/H3_RESULTADOS.json (hospedado en repo resultados/) | 5,371 | ver `resultados/H3_RESULTADOS.json` (repo) |
| resultados/L_ERRATA_EVIDENCIA.json (hospedado en repo resultados/) | 3,598 | ver `resultados/L_ERRATA_EVIDENCIA.json` (repo) |
| orig/gsmgiopuzzle/README.md | 5,799 | `06268a64fbe262c6bc015ce16ad85d39de34473cb74b16dc80be153974d04673` |
| orig/gsmgiopuzzle/FULL_SUMMARY.md | 37,934 | `e5aeb48ef06e80b54b5a21a034bc8b8e293b0bcb72e713be42ef7f2459be11ca` |
| orig/gsmgiopuzzle/evidence.md | 54,004 | `f532ad305f5d92b9fad2a48cc3d336e783c9a98db0f0cef47ce213af4bcb7d82` |
| orig/gsmgiopuzzle/discoveries.md | 128,413 | `2b5304fce1f156ab57b8fd1cc02bc936cf85ecde6319275861ca04e71b079dad` |
| orig/gsmgiopuzzle/dead_ends.md | 44,515 | `8d8f7d7ac36ee63f973b405108e4666836b9bcc65aebdcb9789b6f8ae08f1283` |
| orig/gsmgiopuzzle/timeline.md | 27,005 | `09ac550b676e5b27744ea79f6959377ee70c548c8538e870dc92b427ab457542` |

## 3. Informes de sesión B–L (local, no hospedados salvo los ya embebidos)

| Informe | Bytes | SHA-256 |
|---|---|---|
| download/SALPH_SESION_B_20261122.md | 7,945 | `a4834dab2aa685b4b5d0e1f5d46f2e5d6a03dd18a6c05833cc8fd0098ac90a43` |
| download/SALPH_SESION_C_20261122.md | 7,742 | `785049f63a367771c7dd5267971a3e2cd4c312b3876b3cd817292920e4c7d608` |
| download/SALPH_SESION_E_20261122.md | 8,803 | `79c17242d031b2a4f9b4d077de7f63ed8d6dbecdb4cbee6880c0fb413738aefa` |
| download/SALPH_SESION_F_20261122.md | 9,785 | `d50f4c1c73805dca1a480524ca1249b852b0bace7d67fe90b77ade315f782df4` |
| download/SALPH_SESION_G_20261123.md | 974 | `5e4c6c6b5b23a1656cbb77149281495e37415b156bb3c487cd542a89390bfd34` |
| download/SALPH_SESION_I_20261123.md | 18,207 | `3500a8500dd39a9c65df0ff83038a4d15eec5b02470c5abf3e91dc9d15f1d559` |
| download/SALPH_SESION_J_20261123.md | 13,990 | `4b8f21f8e82d7dbad44defbd8d61a5da454c0d4eb286c59085882e15ddb51383` |
| download/SALPH_SESION_K_20261123.md | 11,777 | `3f2975902cf23699e76dfa619bd053dc252b2e1ab6292c51e97e06da8ac811f7` |
| download/SESION_20261122_CONTINUACION.md | 12,853 | `8781dd4ce6d3ea6ded2e0cadcf76c8ba3f0161cf26484042e0115951a51e06ae` |

## 4. Nota de regeneración

El intake crudo (`raw/`) tiene manifiesto propio (`raw/manifests/raw_manifest.jsonl`)
y cada artefacto web lleva `provenance.json`. Los experimentos 069-072 llevan
`SNAPSHOT_SHA256.json`. Los datos hospedados en este repositorio (`datos/`) son
verificables con `scripts/verifica_hashes.py`.
