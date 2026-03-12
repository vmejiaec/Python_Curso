# Especificación Funcional - Sistema de Cálculo de Venta (4_proyecto)

## 1. Propósito
Este programa de consola permite registrar un producto y consultar cálculos comerciales básicos:
- Total de venta
- Descuento del 10%
- IVA del 15%
- Total final (total menos descuento más IVA)
- Reporte completo

## 2. Alcance
Incluye:
- Ingreso manual de datos de un producto por consola
- Cálculo único de resultados para el producto ingresado
- Menú interactivo para visualizar resultados parciales o el reporte completo

No incluye:
- Persistencia en base de datos o archivos
- Gestión de múltiples productos en una sola ejecución
- Edición posterior de datos del producto
- Validación robusta de entradas

## 3. Usuarios objetivo
- Estudiantes de introducción a Python
- Docentes que desean mostrar separación básica por capas (dominio, aplicación, interfaz)

## 4. Estructura funcional por capas

### 4.1 Dominio
- `dominio/producto.py`
  - `crear_producto(nombre, codigo, cantidad, precio)`
  - Construye y retorna un diccionario con la estructura del producto.

- `dominio/calculo.py`
  - `crear_resultado(total, dscto, iva, total_sin_dscto, total_sin_dscto_mas_IVA)`
  - Construye y retorna un diccionario con los resultados de cálculo.

### 4.2 Aplicación
- `aplicacion/calculos.py`
  - `calcular_venta(producto)`
  - Ejecuta la lógica de negocio y retorna el diccionario de resultados.

### 4.3 Interfaz
- `interfaz/entrada.py`
  - `ingresar_producto()`
  - `ingresar_menu_seleccion()`

- `interfaz/salida.py`
  - `presentar_menu()`
  - `presentar_producto(producto)`
  - `presentar_reporte(producto, resultados)`
  - `presentar_menu_seleccion(seleccion, producto, resultados)`

### 4.4 Orquestación
- `main.py`
  - Coordina todo el flujo:
    1. Ingresa producto
    2. Calcula resultados
    3. Muestra producto y menú
    4. Procesa opciones del usuario en bucle hasta seleccionar `0`

## 5. Flujo funcional detallado
1. El sistema solicita:
   - Nombre
   - Código
   - Cantidad
   - Precio
2. Se crea el objeto `producto` (diccionario).
3. Se calculan resultados una vez para ese producto.
4. Se presenta el menú de opciones.
5. Mientras la opción sea mayor que 0:
   - Se lee una selección
   - Se muestra el dato solicitado
6. Si la opción es `0`, se muestra mensaje de fin y termina el programa.

## 6. Reglas de negocio implementadas
En `calcular_venta(producto)`:

- Constantes:
  - `CENT = Decimal("0.01")`
  - `PORC_DSCTO = Decimal("0.1")` (10%)
  - `PORC_IVA = Decimal("0.15")` (15%)

- Fórmulas:
  - `total = cantidad * precio`
  - `dscto = total * PORC_DSCTO` (redondeado a 2 decimales, `ROUND_HALF_UP`)
  - `total_sin_dscto = total - dscto`
  - `iva = total_sin_dscto * PORC_IVA` (redondeado a 2 decimales, `ROUND_HALF_UP`)
  - `total_sin_dscto_mas_IVA = total_sin_dscto + iva`

## 7. Estructuras de datos

### 7.1 Producto
Diccionario con claves:
- `nombre` (str)
- `codigo` (str)
- `cantidad` (int)
- `precio` (Decimal)

### 7.2 Resultado
Diccionario con claves:
- `total` (Decimal)
- `dscto` (Decimal)
- `iva` (Decimal)
- `total_sin_dscto` (Decimal)
- `total_sin_dscto_mas_IVA` (Decimal)

## 8. Comportamiento del menú
- Opción `1`: muestra total
- Opción `2`: muestra descuento
- Opción `3`: muestra IVA
- Opción `4`: muestra total final
- Opción `5`: muestra reporte completo
- Opción `0`: muestra "Fin del programa"

## 9. Supuestos y limitaciones actuales
- Si el usuario ingresa texto no numérico en cantidad/precio/opción, puede ocurrir excepción (`ValueError`).
- No hay validación de valores negativos.
- No hay recálculo por cambio de producto (solo un producto por ejecución).
- No hay almacenamiento persistente.

## 10. Criterios de aceptación funcional
Se considera correcto cuando:
1. El sistema permite ingresar un producto sin errores de formato válidos.
2. El menú permite consultar cada opción de cálculo.
3. El reporte muestra todos los campos calculados esperados.
4. La opción `0` finaliza el flujo interactivo.

## 11. Evolución recomendada (siguiente iteración)
- Validación de entradas (tipo, vacíos, negativos).
- Soporte para múltiples productos (`list[producto]`).
- Persistencia en base de datos.
- Recuperación y visualización de productos guardados.
- Separar aún más interfaz de reglas de navegación del menú.
