# SECURITY — política de seguridad

## Qué publica este repositorio

- Hashes, direcciones públicas, materiales del puzzle en forma textual y resultados
  de verificación. **Ningún material de control de fondos reales.**
- Contraseñas y WIF citados en las auditorías son material YA publicado upstream por
  sus autores comunitarios (issues de GitHub/Telegram, 2020–2026) y están verificados
  como NO-premio (derivan direcciones ausentes del inventario de objetivos).

## Qué nunca contendrá

- Secretos, credenciales, tokens de sesión o claves privadas del premio.
- Volcados de datos privados de personas (los logs comunitarios citados son
  upstream públicos).

## Límites de método

- Prohibido: fuerza bruta sobre ECDLP/SHA-256/HASH160; escaneos masivos en CI.
- Validación mínima aceptada: padding-1 NO valida; una dirección «matemáticamente
  válida» no valida; solo la regla de origen + control positivo autentica
  (estándar de tres partes del README).

## Divulgación responsable

- Hallazgos que afecten a fondos o a terceros: abrir un issue privado del repositorio
  primero; nada se publica sin verificación doble.
