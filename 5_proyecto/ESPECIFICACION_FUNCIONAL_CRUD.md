# Especificación Funcional — CRUD de Productos con Clases y Objetos (5_proyecto)

## 1. Objetivo
Implementar una aplicación pequeña de consola para gestionar productos mediante operaciones CRUD usando clases/objetos, con almacenamiento en memoria (listas), sin base de datos.

## 2. Alcance
### Incluye
- CRUD completo de productos:
  - Crear producto
  - Consultar productos (lista y por código)
  - Actualizar producto
  - Eliminar producto
- Cálculo de venta por producto (subtotal, descuento, IVA, total final).
- Entidades mínimas adicionales para mantener coherencia del dominio:
  - Cliente
  - Categoría
  - Factura
- Persistencia temporal en listas de objetos durante la ejecución.

### No incluye
- Base de datos.
- API web.
- Persistencia en archivos.
- Autenticación/usuarios.

## 3. Modelo de dominio (clases)

## 3.1 Producto
Atributos (alineados al dominio actual y ajustados a nombres consistentes):
- `codigo: str`
- `nombre: str`
- `codigo_categoria: str`
- `stock: int`
- `precio: Decimal`
- `esta_promocion: bool = False`
- `esta_exento_iva: bool = False`

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
- `fecha: date | str` (según nivel del curso)
- `cedula_cliente: str`
- `codigo_producto: str`
- `precio: Decimal`
- `cantidad: int`

## 3.5 ResultadoVenta (objeto de salida de cálculos)
- `total: Decimal`
- `dscto: Decimal`
- `total_sin_dscto: Decimal`
- `iva: Decimal`
- `total_final: Decimal`

---

## 4. Organización de código propuesta (capas)

```text
5_proyecto/
  main.py
  dominio/
    producto.py
    cliente.py
    categoria.py
    factura.py
    resultado.py
  aplicacion/
    servicios_producto.py
    servicios_catalogos.py
    servicios_facturacion.py
    calculos.py
  interfaz/
    entrada.py
    salida.py
    menu.py
  infraestructura/
    repositorios_memoria.py
```

### 4.1 Dominio
Define clases y reglas básicas de consistencia (sin `input/print`).

### 4.2 Aplicación
Implementa casos de uso y coordinación de reglas:
- CRUD producto
- Búsquedas por código
- Cálculo de venta
- Generación de factura básica

### 4.3 Interfaz
Solo interacción por consola:
- Menús
- Lectura de datos
- Impresión de resultados y mensajes

### 4.4 Infraestructura (en memoria)
Contiene listas de objetos y operaciones de repositorio (buscar, agregar, actualizar, eliminar).

---

## 5. Almacenamiento en memoria
Se manejan listas de objetos en runtime:
- `productos: list[Producto]`
- `clientes: list[Cliente]`
- `categorias: list[Categoria]`
- `facturas: list[Factura]`

Regla general:
- La identificación se hace por clave natural (`codigo`, `cedula`, `numero`).
- No se permite duplicidad de claves.

---

## 6. Requerimientos funcionales

## RF-01 Crear producto
El sistema debe permitir ingresar un producto y agregarlo a la lista si el código no existe.

## RF-02 Listar productos
El sistema debe mostrar todos los productos registrados.

## RF-03 Consultar producto por código
El sistema debe permitir buscar un producto por su código y mostrarlo.

## RF-04 Actualizar producto
El sistema debe permitir modificar campos editables de un producto existente.

## RF-05 Eliminar producto
El sistema debe eliminar un producto por código (si existe).

## RF-06 Cálculo de venta
El sistema debe calcular:
- Total
- Descuento
- Base sin descuento
- IVA
- Total final

Reglas iniciales sugeridas (manteniendo app pequeña):
- Descuento 10% si subtotal > 10 o si está en promoción y cantidad >= 3.
- IVA 15% salvo productos exentos.
- Redondeo monetario a 2 decimales con `Decimal` y `ROUND_HALF_UP`.

## RF-07 Entidades de apoyo
El sistema debe permitir al menos registrar y consultar:
- Categorías (código, nombre)
- Clientes (cédula, nombre, email)

## RF-08 Factura básica
El sistema debe permitir crear una factura mínima referenciando:
- Cliente existente
- Producto existente
- Precio y cantidad

(Para mantener tamaño pequeño, CRUD completo de factura no es obligatorio; crear/listar es suficiente en esta iteración.)

---

## 7. Reglas de validación mínimas
- `codigo` de producto no vacío y único.
- `stock >= 0`.
- `precio >= 0`.
- `cedula` de cliente no vacía y única.
- `email` con formato básico válido (mínimo contiene `@`).
- `codigo_categoria` debe existir en catálogo de categorías.
- Al facturar, `codigo_producto` y `cedula_cliente` deben existir.

---

## 8. Flujo principal de usuario
1. Iniciar programa.
2. Mostrar menú principal CRUD de productos.
3. Ejecutar operación seleccionada.
4. Mostrar resultado/mensaje.
5. Repetir hasta opción salir.

Menú sugerido:
- 1: Crear producto
- 2: Listar productos
- 3: Buscar producto por código
- 4: Actualizar producto
- 5: Eliminar producto
- 6: Calcular venta de un producto
- 7: Gestión mínima de clientes/categorías
- 8: Crear factura básica
- 0: Salir

---

## 9. Casos límite y comportamiento esperado
- Buscar producto inexistente: mostrar mensaje claro, no lanzar excepción al usuario final.
- Eliminar producto inexistente: informar que no se encontró.
- Actualizar con datos inválidos: rechazar y mantener estado previo.
- Lista vacía: mostrar “no hay registros”.

---

## 10. Criterios de aceptación
Se considera cumplido el requerimiento cuando:
1. El producto se maneja como objeto de clase (no diccionario).
2. Existe CRUD funcional de productos en memoria.
3. La interfaz de consola permite operar el CRUD sin errores por flujo normal.
4. Se conservan cálculos de venta con `Decimal` y redondeo correcto.
5. Cliente, Categoría y Factura existen como clases con atributos mínimos definidos.
6. No se usa base de datos; todo funciona con listas de objetos.

---

## 11. Notas de implementación recomendadas (didácticas)
- Usar `dataclass` para entidades de dominio en nivel introductorio.
- Separar estrictamente:
  - Dominio: clases y reglas
  - Aplicación: casos de uso
  - Interfaz: `input/print`
- Evitar lógica de negocio dentro de la capa de interfaz.
- Mantener funciones cortas y con una responsabilidad.
