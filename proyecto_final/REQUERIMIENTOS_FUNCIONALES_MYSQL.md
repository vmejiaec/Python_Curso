# Requerimientos Funcionales del Sistema (MySQL)

## 1. Objetivo
Implementar un sistema de gestión comercial con persistencia en MySQL para administrar productos, clientes, categorías y facturas mediante operaciones SQL directas (`SELECT`, `INSERT`, `UPDATE`, `DELETE`), sin API y sin autenticación.

## 2. Alcance
### Incluye
- Persistencia en base de datos MySQL.
- Operaciones CRUD de entidades principales.
- Consultas de negocio con `SELECT` (filtros, ordenamientos, totales).
- Registro y consulta de facturas.
- Reportes básicos de ventas.

### No incluye
- API REST o servicios web.
- Login/autenticación/autorización.
- Integraciones externas.

## 3. Entidades y atributos mínimos

## 3.1 Categoria
- `codigo` (PK)
- `nombre`

## 3.2 Producto
- `codigo` (PK)
- `nombre`
- `codigo_categoria` (FK -> categoria.codigo)
- `stock`
- `precio`
- `esta_promocion`
- `esta_exento_iva`

## 3.3 Cliente
- `cedula` (PK)
- `nombre`
- `email`

## 3.4 Factura
- `numero` (PK)
- `fecha`
- `cedula_cliente` (FK -> cliente.cedula)

## 3.5 FacturaDetalle
- `id` (PK autoincremental)
- `numero_factura` (FK -> factura.numero)
- `codigo_producto` (FK -> producto.codigo)
- `precio`
- `cantidad`
- `subtotal`
- `descuento`
- `iva`
- `total`

## 4. Requerimientos funcionales por módulo

## RF-01 CRUD de categorías
El sistema debe permitir:
- Crear categoría (`INSERT`).
- Consultar categorías (`SELECT`).
- Actualizar nombre de categoría (`UPDATE`).
- Eliminar categoría (`DELETE`) cuando no tenga productos asociados.

## RF-02 CRUD de productos
El sistema debe permitir:
- Crear producto con categoría existente (`INSERT`).
- Consultar productos (`SELECT`) y consultar por código (`SELECT ... WHERE`).
- Actualizar datos del producto (`UPDATE`).
- Eliminar producto (`DELETE`) cuando no esté referenciado en facturas.

## RF-03 CRUD de clientes
El sistema debe permitir:
- Crear cliente (`INSERT`).
- Listar clientes (`SELECT`).
- Buscar cliente por cédula (`SELECT ... WHERE`).
- Actualizar datos del cliente (`UPDATE`).
- Eliminar cliente (`DELETE`) cuando no tenga facturas asociadas.

## RF-04 Registro de factura
El sistema debe permitir:
- Crear encabezado de factura (`INSERT` en `factura`).
- Insertar uno o más detalles (`INSERT` en `factura_detalle`).
- Calcular por ítem: subtotal, descuento, IVA y total.
- Descontar stock del producto (`UPDATE producto SET stock = stock - cantidad`).
- Ejecutar el registro dentro de una transacción SQL (`BEGIN`, `COMMIT`, `ROLLBACK`).

## RF-05 Consulta de facturas
El sistema debe permitir:
- Listar facturas con datos de cliente (`SELECT` con `JOIN`).
- Consultar factura por número (`SELECT ... WHERE`).
- Consultar detalles de una factura (`SELECT` sobre `factura_detalle`).

## RF-06 Actualización y anulación de factura
El sistema debe permitir:
- Actualizar una factura (si la regla de negocio lo permite) con `UPDATE`.
- Eliminar/anular factura con `DELETE` lógico o físico según configuración.
- Revertir stock cuando se elimine/anule factura (si aplica regla de negocio).

## RF-07 Reportes de ventas
El sistema debe permitir consultas SQL para:
- Total vendido por cliente (`SELECT ... GROUP BY cedula_cliente`).
- Total vendido por producto (`SELECT ... GROUP BY codigo_producto`).
- Ventas por rango de fechas (`SELECT ... WHERE fecha BETWEEN ...`).
- Top clientes por monto (`SELECT ... ORDER BY total DESC LIMIT N`).

## 5. Reglas de negocio mínimas
- Descuento: 10% si subtotal > 10 o si producto en promoción y cantidad >= 3.
- IVA: 15% salvo productos exentos de IVA.
- No permitir venta con stock insuficiente.
- No permitir precios ni cantidades negativas.
- No permitir claves primarias duplicadas.

## 6. Reglas de validación
- `producto.codigo`, `cliente.cedula`, `factura.numero` son obligatorios y únicos.
- `cliente.email` debe tener formato válido básico.
- `producto.codigo_categoria` debe existir.
- `factura.cedula_cliente` debe existir.
- `factura_detalle.codigo_producto` debe existir.

## 7. Requerimientos de integridad en base de datos
- Definir PK en todas las tablas.
- Definir FK para relaciones.
- Definir restricciones de no nulos en campos obligatorios.
- Definir índices en campos de búsqueda frecuente (`codigo`, `cedula`, `fecha`).
- Usar tipo decimal para importes monetarios.

## 8. Operaciones SQL esperadas
- Consultas: `SELECT`, `SELECT ... JOIN`, `SELECT ... GROUP BY`, `SELECT ... ORDER BY`.
- Escritura: `INSERT`, `UPDATE`, `DELETE`.
- Control transaccional: `BEGIN`, `COMMIT`, `ROLLBACK`.

## 9. Flujo funcional general
1. Registrar categorías, productos y clientes.
2. Consultar y mantener catálogos (CRUD).
3. Registrar facturas con detalle y actualización de stock.
4. Consultar facturas y detalles.
5. Generar reportes SQL de ventas.

## 10. Criterios de aceptación
Se considera aceptado cuando:
1. El sistema ejecuta CRUD completo de categorías, productos y clientes con MySQL.
2. El registro de factura inserta encabezado/detalle y actualiza stock en transacción.
3. Se pueden ejecutar reportes por cliente, producto y fecha mediante `SELECT`.
4. Se respetan llaves primarias/foráneas y validaciones de negocio.
5. No existe API ni autenticación; toda la lógica opera directamente con MySQL.

## 11. Consideraciones técnicas recomendadas
- Motor: InnoDB (soporte de transacciones y FK).
- Uso de consultas parametrizadas para evitar inyección SQL.
- Manejo de errores SQL con rollback en operaciones críticas.
- Separar consultas en una capa de acceso a datos para mantener orden del proyecto.
