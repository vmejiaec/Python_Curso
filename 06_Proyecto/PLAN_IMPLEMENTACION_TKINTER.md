# Plan de Implementación — Proyecto Tkinter (06_Proyecto)

## 1. Objetivo del plan
Definir una ruta de implementación incremental para construir la aplicación de escritorio en Tkinter, manteniendo almacenamiento en memoria y cubriendo CRUD, facturación y reporte gráfico de ventas por cliente.

## 2. Enfoque de trabajo
- Implementación por iteraciones cortas (Sprints/Fases).
- Cada fase debe dejar el sistema ejecutable.
- Separación por capas desde el inicio: dominio, aplicación, interfaz e infraestructura en memoria.
- Primero funcionalidad, luego mejoras de UX y robustez.

## 3. Supuestos
- Python 3.11+ disponible.
- Tkinter disponible en el entorno.
- Se permitirá usar matplotlib para el gráfico de barras.
- Sin persistencia (datos en memoria durante la ejecución).

## 4. Estructura objetivo

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

## 5. Roadmap por fases

## Fase 0 — Preparación del proyecto
### Objetivo
Dejar estructura base y punto de arranque.

### Tareas
- Crear carpetas y archivos base.
- Definir dependencias (matplotlib).
- Preparar ventana principal Tkinter (`main.py` + `app_tk.py`).

### Entregables
- Aplicación abre una ventana principal vacía o con menú básico.
- Estructura de carpetas establecida.

### Criterio de salida
- La app inicia sin errores.

---

## Fase 1 — Dominio + infraestructura en memoria
### Objetivo
Modelar entidades y repositorios en memoria.

### Tareas
- Definir clases de dominio (`Producto`, `Cliente`, `Categoria`, `Factura`, `ResultadoVenta`).
- Crear repositorios en memoria con operaciones básicas:
  - agregar
  - listar
  - buscar por clave
  - actualizar
  - eliminar
- Implementar validaciones mínimas de entidad.

### Entregables
- Módulo de dominio funcional.
- Repositorios en memoria probados con datos de ejemplo.

### Criterio de salida
- Se puede crear/listar/buscar entidades desde código (sin UI completa).

---

## Fase 2 — CRUD de productos (UI completa)
### Objetivo
Tener el módulo de productos usable de punta a punta.

### Tareas
- Construir `vista_productos.py` con:
  - formulario
  - botones CRUD
  - tabla (`Treeview`)
- Conectar eventos de botones con `servicios_producto.py`.
- Manejar validaciones y mensajes al usuario.

### Entregables
- CRUD de productos operando en interfaz gráfica.

### Criterio de salida
- Usuario crea, consulta, actualiza y elimina productos desde la UI.

---

## Fase 3 — CRUD mínimo de clientes + catálogo de categorías
### Objetivo
Incorporar entidades de apoyo para facturación.

### Tareas
- Construir `vista_clientes.py` con CRUD mínimo.
- Incorporar gestión básica de categorías (crear/listar), en vista propia o integrada.
- Validar unicidad de cédula y código de categoría.

### Entregables
- Gestión de clientes funcional.
- Catálogo de categorías operativo.

### Criterio de salida
- Existen clientes y categorías cargables y consultables por interfaz.

---

## Fase 4 — Facturación
### Objetivo
Registrar ventas y aplicar reglas de cálculo.

### Tareas
- Construir `vista_facturas.py`.
- Selección de cliente y producto.
- Captura de cantidad.
- Cálculo automático con `aplicacion/calculos.py`:
  - subtotal
  - descuento
  - IVA
  - total
- Actualizar stock al facturar.
- Guardar factura en lista de facturas.

### Entregables
- Registro de factura completo.
- Tabla/listado de facturas.

### Criterio de salida
- Se registra factura válida y se actualiza stock correctamente.

---

## Fase 5 — Reporte gráfico de barras (ventas por cliente)
### Objetivo
Visualizar ventas acumuladas por cliente.

### Tareas
- Implementar agregación en `aplicacion/reportes.py`:
  - total vendido por cédula/cliente
- Construir `vista_reportes.py`.
- Embebido de gráfico de barras con matplotlib en Tkinter.
- Manejar estado sin datos (mensaje de “sin facturas”).

### Entregables
- Reporte gráfico interactivo con botón “Generar”.

### Criterio de salida
- El gráfico muestra correctamente ventas por cliente con datos reales de facturas en memoria.

---

## Fase 6 — Cierre, calidad y documentación
### Objetivo
Consolidar experiencia de uso y documentación final.

### Tareas
- Revisar consistencia de mensajes y validaciones.
- Mejorar navegación entre vistas.
- Documentar arquitectura y guía de uso.
- Pruebas manuales de regresión (escenarios críticos).

### Entregables
- Documento de usuario.
- Checklist de pruebas completado.

### Criterio de salida
- Aplicación estable para demo/clase.

## 6. Backlog priorizado
1. Arranque de app Tkinter.
2. Dominio y repositorios en memoria.
3. CRUD productos en UI.
4. CRUD clientes.
5. Facturación con reglas.
6. Reporte de barras por cliente.
7. Hardening UX/documentación.

## 7. Pruebas mínimas por fase

### Productos
- Crear producto válido.
- Rechazar código duplicado.
- Actualizar precio/stock.
- Eliminar producto existente e inexistente.

### Clientes
- Crear cliente válido.
- Rechazar cédula duplicada.
- Validar email básico.

### Facturación
- Factura con cliente y producto existentes.
- Rechazar cantidad mayor a stock.
- Verificar descuento/IVA/total.
- Verificar decremento de stock.

### Reporte
- Sin facturas: mostrar mensaje.
- Con facturas: barras por cliente correctas.

## 8. Riesgos y mitigación
- Riesgo: acoplar lógica de negocio en UI.
  - Mitigación: toda regla en servicios de aplicación.
- Riesgo: errores monetarios por float.
  - Mitigación: usar Decimal y redondeo uniforme.
- Riesgo: inconsistencias de estado en memoria.
  - Mitigación: centralizar repositorios y operaciones CRUD.
- Riesgo: complejidad visual temprana en Tkinter.
  - Mitigación: construir vistas simples por fases.

## 9. Definición de terminado (DoD)
Una fase se considera terminada si:
- Cumple su criterio de salida.
- No rompe funcionalidades previas.
- Tiene validaciones básicas de entrada.
- Tiene mensajes de éxito/error visibles para usuario.
- Está documentada en breve (qué hace, cómo probar).

## 10. Sugerencia de ritmo (referencial)
- Fase 0: 0.5 día
- Fase 1: 1 día
- Fase 2: 1–1.5 días
- Fase 3: 0.5–1 día
- Fase 4: 1–1.5 días
- Fase 5: 0.5–1 día
- Fase 6: 0.5 día

Total estimado: 5 a 7 días de trabajo incremental para una versión completa y demostrable.
