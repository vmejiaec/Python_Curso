from decimal import Decimal, ROUND_HALF_UP
from dominio import Resultado

# Constante para posición decimal
CENT = Decimal("0.01")
# Constate cero decimal
CERO = Decimal("0.00")
# Constantes para el descto y el iva
PORC_DSCTO = Decimal("0.1")
PORC_IVA = Decimal("0.15")

def calcular_dscto(cantidad, precio, esta_promocion):
    subtotal = cantidad * precio
    # Regla 1: si la venta es superior a 10$ entonces se aplica el dscto
    if subtotal > 10 :
        dscto = subtotal * PORC_DSCTO
        return dscto.quantize(CENT,rounding = ROUND_HALF_UP)
    # Regla 2: si el producto está de promoción y la cantidad es >= 3
    if esta_promocion and cantidad >= 3:
        dscto = subtotal * PORC_DSCTO
        return dscto.quantize(CENT,rounding = ROUND_HALF_UP)
    return CERO

def calcular_iva(valor, esta_exento):
    # Regla: si el producto está exento, el iva es cero
    if esta_exento :
        return CERO
    else :
        iva = valor * PORC_IVA
        return iva.quantize(CENT, rounding = ROUND_HALF_UP)

def calcular_venta(producto):
    total = producto.stock  * producto.precio
    dscto = calcular_dscto(
        producto.stock, 
        producto.precio, 
        producto.esta_de_promocion)
    total_sin_dscto = total - dscto
    iva = calcular_iva(total_sin_dscto, producto.esta_exento_iva)
    total_sin_dscto_mas_IVA = total_sin_dscto + iva
    return Resultado(
            total, 
            dscto, 
            iva, 
            total_sin_dscto, 
            total_sin_dscto_mas_IVA)