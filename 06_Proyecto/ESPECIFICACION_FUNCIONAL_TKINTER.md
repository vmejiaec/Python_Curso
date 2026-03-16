# Especificación Funcional — Sistema de Ventas con Tkinter (06_Proyecto)

## 1. Objetivo
Construir una aplicación de escritorio con Tkinter para gestionar productos, clientes y facturas, operando con datos en memoria (sin base de datos), e incluir un reporte gráfico de barras con ventas por cliente.

## 2. Alcance

### Incluye
- Interfaz gráfica en Tkinter.
- CRUD de productos.
- CRUD mínimo de clientes.
- Registro de facturas de venta.
- Cálculo de subtotal, descuento, IVA y total de factura.
- Reporte gráfico de barras: total vendido por cliente.
- Almacenamiento temporal en listas de objetos durante la ejecución.

### No incluye
- Persistencia en base de datos.
- Persistencia en archivos.
- Multiusuario/autenticación.
- Reportería avanzada (PDF/Excel).

## 3. Entidades del dominio (objetos)

## 3.1 Producto
Atributos mínimos:
- `codigo: str`
- `nombre: str`
- `codigo_categoria: str`
- `stock: int`
- `precio: Decimal`
- `esta_promocion: bool`
- `esta_exento_iva: bool`

## 3.2 Cliente
Atributos mínimos:
- `cedula: str`
- `nombre: str`
- `email: str`

## 3.3 Categoria
Atributos mínimos:
- `codigo: str`
- `nombre: str`

## 3.4 Factura
Atributos mínimos:
- `numero: str`
- `fecha: str` (formato sugerido `YYYY-MM-DD`)
- `cedula_cliente: str`
- `codigo_producto: str`
- `precio: Decimal`
- `cantidad: int`
- `subtotal: Decimal`
- `descuento: Decimal`
- `iva: Decimal`
- `total: Decimal`

## 4. Arquitectura funcional propuesta

```text
06_Proyecto/
  main.py
  dominio/
    producto.py
    cliente.py
    categoria.py
    factura.py
    resultado.py
  aplicacion/
    servicios_producto.py
    servicios_cliente.py
    servicios_factura.py
    calculos.py
    reportes.py
  interfaz/
    app_tk.py
    vistas/
      vista_productos.py
      vista_clientes.py
      vista_facturas.py
      vista_reportes.py
    componentes/
      formularios.py
      tablas.py
      mensajes.py
  infraestructura/
    repositorio_memoria.py
```

### Capas
- **Dominio:** clases y validaciones básicas.
- **Aplicación:** casos de uso (CRUD, cálculos, reporte).
- **Interfaz (Tkinter):** formularios, botones, tablas, gráfico.
- **Infraestructura:** repositorios en memoria (listas).

## 5. Almacenamiento en memoria
Listas administradas por repositorios en memoria:
- `productos: list[Producto]`
- `clientes: list[Cliente]`
- `categorias: list[Categoria]`
- `facturas: list[Factura]`

Reglas:
- Claves únicas: `producto.codigo`, `cliente.cedula`, `factura.numero`.
- La información se pierde al cerrar la aplicación.

## 6. Requerimientos funcionales

## RF-01 Ventana principal
La aplicación debe abrir una ventana principal con navegación a módulos:
- Productos
- Clientes
- Facturas
- Reportes
- Salir

## RF-02 CRUD de productos
Debe permitir:
- Crear producto.
- Listar productos en una tabla.
- Buscar producto por código.
- Actualizar producto.
- Eliminar producto.

## RF-03 CRUD mínimo de clientes
Debe permitir:
- Crear cliente.
- Listar clientes.
- Buscar cliente por cédula.
- Actualizar cliente.
- Eliminar cliente.

## RF-04 Registro de factura
Debe permitir registrar una factura seleccionando cliente y producto, con cantidad.
Al confirmar, calcular automáticamente:
- `subtotal = precio * cantidad`
- `descuento` (reglas del negocio)
- `iva`
- `total`

Debe descontar stock del producto cuando la factura sea válida.

## RF-05 Validación de stock
Si la cantidad solicitada excede el stock, el sistema no debe facturar y debe mostrar mensaje de error.

## RF-06 Reporte gráfico de barras
Debe generar un gráfico de barras con:
- **Eje X:** nombre o cédula del cliente.
- **Eje Y:** monto total vendido acumulado por cliente.
- Fuente de datos: facturas registradas en memoria.

Opciones mínimas:
- Botón “Generar reporte”.
- Mensaje cuando no existan facturas.

## RF-07 Mensajería de usuario
Toda operación (crear, actualizar, eliminar, facturar) debe mostrar confirmación o error mediante cuadros de diálogo.

## 7. Reglas de negocio y cálculos
- Descuento 10% si subtotal > 10 o si el producto está en promoción y cantidad >= 3.
- IVA 15% salvo productos exentos.
- Cálculos monetarios con `Decimal` y redondeo `ROUND_HALF_UP` a 2 decimales.
- No permitir valores negativos en precio, stock o cantidad.

## 8. Reglas de validación
- Producto:
  - Código obligatorio y único.
  - Nombre obligatorio.
  - Precio >= 0.
  - Stock >= 0.
- Cliente:
  - Cédula obligatoria y única.
  - Nombre obligatorio.
  - Email válido (mínimo contiene `@`).
- Factura:
  - Número obligatorio y único.
  - Cliente y producto deben existir.
  - Cantidad > 0.

## 9. Flujo principal de uso
1. Usuario abre aplicación.
2. Registra categorías (opcional si vienen predefinidas).
3. Registra productos y clientes.
4. Registra facturas.
5. Consulta tablas de datos.
6. Abre módulo reportes y genera gráfico de barras por cliente.
7. Cierra aplicación.

## 10. UI mínima requerida (Tkinter)

### 10.1 Vista Productos
- Formulario de captura (código, nombre, categoría, stock, precio, promoción, exento).
- Botones: Nuevo, Guardar, Buscar, Actualizar, Eliminar, Limpiar.
- Tabla (`Treeview`) para listar productos.

### 10.2 Vista Clientes
- Formulario (cédula, nombre, email).
- Botones CRUD.
- Tabla de clientes.

### 10.3 Vista Facturas
- Campos: número, fecha, cliente, producto, cantidad.
- Campos solo lectura para subtotal, descuento, iva, total.
- Botón Registrar factura.
- Tabla de facturas.

### 10.4 Vista Reportes
- Botón “Generar ventas por cliente”.
- Área embebida de gráfico de barras (matplotlib en Tkinter).

## 11. Criterios de aceptación
El requerimiento se considera cumplido cuando:
1. La aplicación funciona en interfaz gráfica Tkinter.
2. El CRUD de productos opera completamente en memoria.
3. El CRUD mínimo de clientes opera en memoria.
4. Se pueden registrar facturas válidas con actualización de stock.
5. Se muestra un gráfico de barras con ventas acumuladas por cliente.
6. No se usa base de datos en ningún módulo.

## 12. Consideraciones técnicas recomendadas
- Usar `ttk` para widgets (`Treeview`, `Notebook`, `Combobox`).
- Usar `dataclass` para entidades de dominio.
- Encapsular listas en repositorios en memoria para no acoplar UI con estructuras internas.
- Para el gráfico, usar `matplotlib` + `FigureCanvasTkAgg`.

## 13. Evolución futura
- Persistencia en SQLite.
- Exportación de reportes a PDF/Excel.
- Soporte para múltiples productos por factura (detalle de factura).
- Filtros por fecha/cliente en reportes.
