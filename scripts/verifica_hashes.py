#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificación de hashes de los artefactos embebidos en datos/ (REPRODUCIBILITY.md).
Ejecutar: python3 scripts/verifica_hashes.py"""
import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FALLBACK = Path('/home/z/my-project')

def find(name):
    for r in (ROOT, FALLBACK / 'repo_push', FALLBACK / 'download'):
        p = r / name
        if p.exists():
            return p
    raise FileNotFoundError(name)

CHECKS = [
    ('datos/fase32_plaintext_2422b.hex', 2422,
     'b82afeb86f9e50848220f9b64b744b821400308aea273a1c949b9d2d0e408a34'),
    ('datos/chain4_plaintext_1151b.hex', 1151,
     'e4269ed5fbb202a81e5e1aa6b5190fdd1ea126b2c8547ea7cdbdf45387ea135b'),
]
ok = True
for name, n, want in CHECKS:
    data = bytes.fromhex(find(name).read_text().strip())
    got = hashlib.sha256(data).hexdigest()
    good = len(data) == n and got == want
    ok &= good
    print(f"{'OK ' if good else 'FAIL'} {name}: {len(data)} B sha256={got[:16]}…")
print('VERIFICACION:', 'TODO OK' if ok else 'FALLO')
raise SystemExit(0 if ok else 1)
