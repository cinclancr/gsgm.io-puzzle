# CHANGELOG — investigación GSMG.io 5 BTC

Formato: entradas más recientes arriba. «Sesión» = jornada de investigación con
entregables verificados; los negativos también se registran (disciplina del proyecto).

## 2026-11-23

- **Repositorio** inicial de consolidación (`cinclancr/gsgm.io-puzzle`): estructura,
  meta-documentos, docs maestros, datos textuales, scripts y resultados.
- **Sesión L (auditoría crítica):** auditoría de la primera apertura AES (cadena 1→4
  reproducida byte a byte desde 7 sobres primarios con documentación completa);
  verificación de inconsistencias de la sesión K; censo de 81 sobres;
  `AUDITORIA_CRITICA.md`, `AUDITORIA_DEMOS_L.json`, `MANIFEST_SOBRES.csv`,
  `CADENA_1_4_REPRODUCCION.json`, `FASE32_PLAINTEXT_2422B.bin`.
  - Hipótesis: H1 (payload60/tablero estradal) NEGATIVA; H2 (mapeo documental del
    acertijo) VERIFICADA (documental); H4 (operando 29 B / «+-») NEGATIVA;
    H3 y H5 formuladas.
- **Errata de la auditoría L:** tres correcciones con evidencia
  (`docs/AUDITORIA_L_ERRATA.md`, `resultados/L_ERRATA_EVIDENCIA.json`,
  `resultados/k_sweep_v3_resumen.json`): distribución del barrido v3 (6.383 =
  6.362+20+1, no «6.129»), alcance del barrido (9 sobres, urlblob solo = 695) y
  longitud de la preimagen 10d6a2c5 (109, no «100»).
- **H3 ejecutada:** 2.422 B sobre cuadrícula de 14 columnas con extracción prima,
  16 variantes contra payload60/dbbi/faed — ver `docs/H3_INFORME.md`,
  `scripts/fase32_h3.py`, `resultados/H3_RESULTADOS.json`.
- **Sesiones I, J, K (2026-11-23):** barridos y verificaciones intermedias
  (anstoo, preimagen 10d6a2c5, censo k1, aperturas comunitarias, refutaciones,
  WAVE OP_RETURN, cierre del frente urlblob). Informes en `sesiones/`.

## 2026-11-22

- **Sesiones B–H (SalPhaseIon):** estructura, baterías, tablero estradal, payload60,
  Vigenère/Beaufort, PBKDF2, claves combinadas, barridos AES; informes en `sesiones/`.
- Continuación y plan de ejecución (`sesiones/SESION_20261122_CONTINUACION.md`).

## 2026-11-21

- **Hallazgos H1–H31** (`docs/HALLAZGOS_NUEVOS.md`): auditoría forense del PNG
  original, espiral reproducida, figura central de 37 bloques, mecanismo Bifid,
  sondeos vivos (L/CDX/OP_RETURN), refutaciones.
- **Experimentos E1–E21:** menú de cifrados, matrixsumlist-2, puerta no textual,
  auditoría color→token, transformación canónica, lastwords, selector, direcciones.
- Manifest AES 7.194, ledger de negativas N01–N35, conciliación de candidatos.

## Anteriores (corpus consolidado)

- Intake forense del corpus upstream (raw/manifests, provenance por artefacto:
  web viva, archive.org, GitHub, Telegram), experimentos 003–072, recuperación de
  historia de posts, cadena 1→4 (reproducción), SalPhaseIon (bifid/final),
  GSMG-CLEAN (datos derivados). Índice: `indice/CORPUS_INDICE.md`.
