from decimal import Decimal, ROUND_HALF_UP
from dominio.calculo import crear_resultado

def calcular_venta(producto):
    CENT = Decimal("0.01")
    PORC_DSCTO = Decimal("0.1")
    PORC_IVA = Decimal("0.15")
    total = producto["cantidad"]  * producto["precio"] 
    dscto = total * PORC_DSCTO
    dscto = dscto.quantize(CENT, rounding=ROUND_HALF_UP)
    total_sin_dscto = total - dscto
    iva = total_sin_dscto * PORC_IVA
    iva = iva.quantize(CENT, rounding=ROUND_HALF_UP)
    total_sin_dscto_mas_IVA = total_sin_dscto + iva
    return crear_resultado(
            total, 
            dscto, 
            iva, 
            total_sin_dscto, 
            total_sin_dscto_mas_IVA)