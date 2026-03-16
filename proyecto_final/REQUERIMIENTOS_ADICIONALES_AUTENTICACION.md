# Requerimientos Adicionales — Autenticación y Control de Acceso por Roles

## 1. Objetivo
Ampliar el sistema actual para incluir autenticación de usuarios y autorización por roles, manteniendo persistencia en MySQL.

## 2. Alcance
### Incluye
- Inicio de sesión (login) de usuarios.
- Gestión de usuarios por parte del administrador.
- Asignación de roles a usuarios.
- Validación de permisos por rol para cada funcionalidad del sistema.

### No incluye
- Integración con proveedores externos de identidad (Google, Microsoft, etc.).
- Recuperación de contraseña por correo.
- Doble factor de autenticación (2FA).

## 3. Roles requeridos

## 3.1 Administrador
Permisos:
- Acceso total al sistema.
- CRUD de categorías, productos, clientes y facturas.
- Gestión completa de usuarios (crear, consultar, actualizar, activar/desactivar, asignar rol).
- Acceso a todos los reportes.

## 3.2 Jefe
Permisos:
- Acceso a módulos de operación (categorías, productos, clientes, facturas, reportes).
- Sin acceso al módulo de usuarios.

Restricción explícita:
- No puede crear, editar, eliminar ni listar usuarios.

## 3.3 Facturador
Permisos:
- Crear facturas.
- Consultar facturas (según política de negocio).
- Ejecutar reporte de ventas.

Restricciones explícitas:
- No puede acceder a usuarios.
- No puede administrar categorías/productos/clientes (excepto consultas mínimas necesarias para facturar, si aplica).

## 4. Requerimientos funcionales adicionales

## RFA-01 Login de usuario
El sistema debe permitir:
- Ingresar con usuario y contraseña.
- Validar credenciales contra la base de datos.
- Denegar acceso si credenciales son inválidas o usuario está inactivo.

## RFA-02 Sesión activa
Tras login exitoso, el sistema debe:
- Crear una sesión de usuario.
- Mantener en memoria el usuario autenticado y su rol.
- Permitir cierre de sesión.

## RFA-03 Autorización por rol
El sistema debe validar permisos antes de cada operación sensible:
- Si el rol no tiene permiso, bloquear operación y mostrar mensaje de acceso denegado.

## RFA-04 Gestión de usuarios (solo Administrador)
El administrador debe poder:
- Crear usuario.
- Asignar rol (`ADMINISTRADOR`, `JEFE`, `FACTURADOR`).
- Actualizar datos del usuario.
- Cambiar contraseña.
- Activar o desactivar usuario.
- Consultar listado de usuarios.

## RFA-05 Asignación de rol al crear usuario
Al crear usuario, el administrador debe seleccionar exactamente un rol.

## RFA-06 Menú dinámico por rol
El sistema debe mostrar en la interfaz solo las opciones autorizadas para el rol autenticado.

## RFA-07 Auditoría básica (recomendada)
Registrar al menos:
- Usuario que ejecuta operación.
- Fecha/hora.
- Acción (`LOGIN`, `INSERT`, `UPDATE`, `DELETE`, `FACTURAR`, etc.).

(Para mantener tamaño pequeño, esta auditoría puede ser mínima y opcional en primera iteración.)

## 5. Modelo de datos adicional (MySQL)

## 5.1 Tabla `rol`
Campos mínimos:
- `id` (PK)
- `nombre` (único): `ADMINISTRADOR`, `JEFE`, `FACTURADOR`

## 5.2 Tabla `usuario`
Campos mínimos:
- `id` (PK)
- `username` (único)
- `password_hash`
- `nombre`
- `email`
- `id_rol` (FK -> rol.id)
- `activo` (bool)
- `fecha_creacion`

## 5.3 (Opcional) Tabla `auditoria`
Campos mínimos:
- `id` (PK)
- `id_usuario`
- `accion`
- `detalle`
- `fecha_hora`

## 6. Reglas de seguridad mínimas
- No almacenar contraseñas en texto plano.
- Guardar `password_hash` (hash seguro con salt).
- Validar intentos de login y mensajes genéricos en fallo (sin revelar si usuario existe).
- Usar consultas parametrizadas para evitar inyección SQL.

## 7. Reglas de autorización por módulo

### 7.1 Usuarios
- Administrador: permitido.
- Jefe: denegado.
- Facturador: denegado.

### 7.2 Facturación
- Administrador: permitido.
- Jefe: permitido.
- Facturador: permitido (crear factura + reporte).

### 7.3 Reportes
- Administrador: permitido.
- Jefe: permitido.
- Facturador: permitido (al menos reporte de ventas requerido).

### 7.4 Catálogos (productos/clientes/categorías)
- Administrador: permitido completo.
- Jefe: permitido completo (excepto usuarios).
- Facturador: solo consulta mínima si se requiere para facturar (sin CRUD administrativo).

## 8. Flujo funcional esperado
1. Usuario abre sistema.
2. Se presenta pantalla de login.
3. Usuario ingresa credenciales.
4. Sistema valida credenciales y estado.
5. Si login es exitoso, se carga menú según rol.
6. Cada operación valida permisos.
7. Si no tiene permiso, se bloquea y notifica.
8. Usuario puede cerrar sesión.

## 9. Criterios de aceptación
Se considera cumplido cuando:
1. Existe login funcional con validación en MySQL.
2. Existen los tres roles requeridos (`ADMINISTRADOR`, `JEFE`, `FACTURADOR`).
3. El administrador puede crear usuarios y asignarles rol.
4. El jefe no puede acceder al módulo de usuarios.
5. El facturador solo puede crear facturas y ejecutar reporte.
6. El sistema valida acceso por rol antes de operar.
7. Las contraseñas se almacenan con hash, no en texto plano.

## 10. Compatibilidad con requerimientos existentes
Este documento amplía los requerimientos funcionales ya definidos para el sistema con MySQL.
No reemplaza CRUD ni facturación existentes; agrega seguridad de acceso por usuario/rol.
