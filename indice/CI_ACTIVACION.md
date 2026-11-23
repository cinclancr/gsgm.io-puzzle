# CI — flujo de verificación continua

**Nota de permisos (2026-11-23):** el token de integración usado para la
consolidación carece del ámbito `workflow`, por lo que GitHub rechaza (403) crear
archivos bajo `.github/workflows/` vía API. Este archivo contiene el flujo listo
para activarse MANUALMENTE: crear `.github/workflows/ci.yml` con este contenido
(vía web de GitHub o `git` local). Sin dependencias externas (100% stdlib), versión
fija de Python, sin escaneos criptográficos masivos.

```yaml
name: ci

on:
  push:
    branches: [main]
  pull_request:

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'   # versión fija; scripts 100% stdlib
      - name: Verificacion de hashes de artefactos embebidos
        run: python3 scripts/verifica_hashes.py
      - name: Evidencia de la errata de la auditoria L (E1-E3)
        run: python3 scripts/l_errata_evidence.py
      - name: Ejecucion de la hipotesis H3 (16 variantes)
        run: python3 scripts/fase32_h3.py
```

Qué verifica cada paso:

1. `scripts/verifica_hashes.py` — los artefactos hex embebidos (`datos/`) tienen
   los bytes y SHA-256 ancla correctos (fase 3.2: 2.422 B / `b82afeb8…`; cadena 4:
   1.151 B / `e4269ed5…`).
2. `scripts/l_errata_evidence.py` — las tres erratas de la auditoría L (E1/E2/E3)
   quedan CONFIRMADAS contra `resultados/k_sweep_v3_resumen.json` y los positivos
   de control (P1/P2) contra `datos/`.
3. `scripts/fase32_h3.py` — la hipótesis H3 se re-ejecuta completa (16 variantes
   + control del comparador) y debe terminar con veredicto NEGATIVA.

Los tres scripts terminan con código de salida 0 en caso de éxito; cualquier
desviación hace fallar el CI (detección temprana de corrupción del corpus).
