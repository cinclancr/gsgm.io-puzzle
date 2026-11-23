#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Evidencia de la errata de la auditoría L (AUDITORIA_CRITICA.md, sesión 2026-11-23).

Corrige TRES anotaciones verificables de la §3.2/§3.3 con evidencia reproducible:
  E1 — distribución del barrido v3: «6.129 eventos = 6.362 pad-1 + 20 pad-2 + 1 pad-16»
       es aritméticamente imposible (6.362+20+1 = 6.383). Valores reales:
       EVP 6.129 = 6.109 pad-1 + 19 pad-2 + 1 pad-16; EVP+PBKDF2 6.383 = 6.362+20+1.
  E2 — alcance del barrido v3: cubrió 9 sobres (urlblob + 8 demos), no solo urlblob;
       urlblob solo = 669 EVP + 26 PBKDF2 = 695 eventos (693 pad-1 + 2 pad-2, 0 pad-16);
       los 2 eventos pad-2 de urlblob contradicen «todos pad=1» del informe K.
  E3 — la preimagen de 10d6a2c5… mide 109 chars, no «100 chars» (la §3.2 la describe
       como de 100). El hash SÍ es el correcto.

Verifica también los aciertos que la auditoría sí tiene (positivos de control):
  P1 — sha256("anstoo") = 21ef053324184a4d…  ✓ (como dice la §3.2).
  P2 — el plaintext de fase 3.2 (datos/fase32_plaintext_2422b.hex) = 2.422 B con
       sha256 b82afeb8… ✓ (integridad del artefacto ancla).

Ejecutar:  python3 scripts/l_errata_evidence.py
Salida: resultados/L_ERRATA_EVIDENCIA.json + resumen stdout. Todo PASS = evidencia completa.
"""
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FALLBACK = Path('/home/z/my-project')

def find(name, *roots):
    for r in roots:
        p = Path(r) / name
        if p.exists():
            return p
    raise FileNotFoundError(name)

ev = {'sesion': 'L-errata', 'fecha': '2026-11-23',
      'objeto': 'AUDITORIA_CRITICA.md §3.2/§3.3 — correcciones con evidencia', 'erratas': {}, 'positivos': {}}

# ---------- carga del resumen del barrido v3 ----------
RES = find('resultados/k_sweep_v3_resumen.json', ROOT, FALLBACK / 'repo_push', FALLBACK / 'download')
resumen = json.loads(RES.read_text())

def dist_ok(d, total, pad1, pad2, pad16):
    return (d['eventos'] == total and d['pad_dist'].get('1') == pad1
            and d['pad_dist'].get('2') == pad2 and d['pad_dist'].get('16', 0) == pad16)

evp, pbk, comb, url = resumen['evp'], resumen['pbkdf2'], resumen['combinado_evp_pbkdf2'], resumen['urlblob_solo']

# ---------- E1: aritmética de la distribución ----------
ev['erratas']['E1_distribucion_barrido_v3'] = {
    'texto_original': '«La distribución completa del barrido v3: 6.129 eventos = 6.362 pad-1 + 20 pad-2 + 1 pad-16»',
    'defecto': '6.362+20+1 = 6.383 ≠ 6.129 (un subconjano no puede superar al total)',
    'valores_reales': {
        'evp': {'eventos': evp['eventos'], 'pad_dist': evp['pad_dist'],
                'suma_ok': dist_ok(evp, 6129, 6109, 19, 1)},
        'evp_pbkdf2': {'eventos': comb['eventos'], 'pad_dist': comb['pad_dist'],
                       'suma_ok': dist_ok(comb, 6383, 6362, 20, 1)},
    },
    'lectura_correcta': 'EVP solo: 6.129 = 6.109 pad-1 + 19 pad-2 + 1 pad-16; '
                        'completa (EVP+PBKDF2): 6.383 = 6.362 pad-1 + 20 pad-2 + 1 pad-16',
    'veredicto': 'CONFIRMADA' if dist_ok(evp, 6129, 6109, 19, 1) and dist_ok(comb, 6383, 6362, 20, 1) else 'FALLO DE EVIDENCIA',
}

# ---------- E2: alcance del barrido ----------
counts = resumen['counts']
ev['erratas']['E2_alcance_barrido_v3'] = {
    'texto_original': '§3.3 discute urlblob y presenta «6.129/6.383» sin declarar que el barrido v3 cubrió 9 sobres',
    'defecto': 'el total 6.129/6.383 es de TODOS los sobres del barrido (urlblob + 8 demos); '
              'urlblob solo = 669 EVP + 26 PBKDF2 = 695 eventos (693 pad-1 + 2 pad-2, 0 pad-16)',
    'sobres_del_barrido': counts,
    'urlblob_evp': counts.get('urlblob'),
    'urlblob_total_v3': {'eventos': url['eventos'], 'pad_dist': url['pad_dist'],
                         'suma_ok': dist_ok(url, 695, 693, 2, 0)},
    'urlblob_pad2': resumen.get('urlblob_pad2_eventos', []),
    'suplemento_informe_K': 'SALPH_SESION_K §5 «669 eventos padding-válidos, todos pad=1» es '
                            'contradicho por los 2 eventos pad-2 de urlblob (candidatos «tools\\\\» '
                            'imprimible 0,372 y «lastwordsbefore…secondanswer…matrixsumliste» '
                            'imprimible 0,415 — ruido); la nota de la propia auditoría (684 acumulados '
                            'vs 669 v3) queda como está.',
    'veredicto': 'CONFIRMADA' if counts.get('urlblob') == 669 and dist_ok(url, 695, 693, 2, 0) else 'FALLO DE EVIDENCIA',
}

# ---------- E3: longitud de la preimagen ----------
QUOTE = ('humphhopeisthequintessentialhumandelusionsimultaneouslythesourceof'
         'yourgreateststrengthandyourgreatestweakness')
TRUNC = 'humphhopeisthequintessentialhumandelusion'
h_full, h_trunc = hashlib.sha256(QUOTE.encode()).hexdigest(), hashlib.sha256(TRUNC.encode()).hexdigest()
ev['erratas']['E3_longitud_preimagen'] = {
    'texto_original': '§3.2: «la preimagen real es humphhope…weakness (100 chars — la cita completa de la película…)»',
    'defecto': 'la preimagen correcta mide 109 chars, no 100',
    'longitud_real': len(QUOTE),
    'sha256_completa': h_full,
    'coincide_con_10d6a2c5': h_full.startswith('10d6a2c5'),
    'sha256_forma_truncada': h_trunc,
    'truncada_es_f156d167': h_trunc.startswith('f156d167'),
    'nota': 'el HASH citado por la auditoría es correcto; solo la ANOTACIÓN de longitud (100) es errónea',
    'veredicto': 'CONFIRMADA' if len(QUOTE) == 109 and h_full.startswith('10d6a2c5') else 'FALLO DE EVIDENCIA',
}

# ---------- positivos de control (lo que la auditoría sí tiene bien) ----------
ev['positivos']['P1_anstoo'] = {
    'sha256': hashlib.sha256(b'anstoo').hexdigest(),
    'prefijo_esperado': '21ef053324184a4d',
    'ok': hashlib.sha256(b'anstoo').hexdigest().startswith('21ef053324184a4d'),
}
HEX = find('datos/fase32_plaintext_2422b.hex', ROOT, FALLBACK / 'repo_push', FALLBACK / 'download')
pt = bytes.fromhex(HEX.read_text().strip())
ev['positivos']['P2_plaintext_fase32'] = {
    'bytes': len(pt), 'sha256': hashlib.sha256(pt).hexdigest(),
    'esperado': 'b82afeb86f9e50848220f9b64b744b821400308aea273a1c949b9d2d0e408a34',
    'ok': len(pt) == 2422 and hashlib.sha256(pt).hexdigest() == 'b82afeb86f9e50848220f9b64b744b821400308aea273a1c949b9d2d0e408a34',
}
# ancla del archivo fuente completo (solo verificación local; en el repo queda como cita)
src = FALLBACK / 'scripts' / 'k_sweep_v3_results.json'
if src.exists():
    ev['positivos']['P3_ancla_barrido_v3'] = {
        'sha256_fuente': hashlib.sha256(src.read_bytes()).hexdigest(),
        'ok': hashlib.sha256(src.read_bytes()).hexdigest() == resumen['sha256_fuente'],
    }

ev['veredicto_global'] = ('ERRATAS CONFIRMADAS: ' + ', '.join(
    k.split('_')[0] + '=' + v['veredicto'] for k, v in ev['erratas'].items())
    + ' | positivos: ' + ', '.join(k + '=' + ('OK' if v.get('ok') else 'FALLO') for k, v in ev['positivos'].items()))

OUT = ROOT / 'resultados' / 'L_ERRATA_EVIDENCIA.json'
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(ev, indent=1, ensure_ascii=False))
print(json.dumps({'erratas': {k: {'veredicto': v['veredicto']} for k, v in ev['erratas'].items()},
                  'positivos': {k: v.get('ok') for k, v in ev['positivos'].items()},
                  'veredicto_global': ev['veredicto_global']}, indent=1, ensure_ascii=False))
print('OK →', str(OUT))
