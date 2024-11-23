# Taller 1 - Autenticación y Autorización

Esta aplicación Flask demuestra la implementación de conceptos de autenticación y autorización mediante un sistema de gestión de guardería canina.

## Usuarios Registrados

Los siguientes usuarios están disponibles para pruebas:

| Usuario | Contraseña | Rol |
|---------|------------|-----|
| admin | admin | Administrador |
| mario | mario | Usuario regular |
| juan | juan | Usuario regular |
| pedro | pedro | Usuario regular |

## Permisos y Funcionalidades

### Administrador
- El usuario `admin` tiene privilegios de administrador
- Acceso a vistas administrativas:
  - Gestión de cuidadores (caretakers)
  - Gestión de guarderías (daycares)

### Usuarios Regulares
- Los usuarios `mario`, `juan` y `pedro` tienen acceso básico
- Solo pueden visualizar el mensaje de bienvenida
