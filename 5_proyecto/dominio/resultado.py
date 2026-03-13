def crear_resultado(
        total, 
        dscto, 
        iva, 
        total_sin_dscto, 
        total_sin_dscto_mas_IVA):
    return {
        "total": total, 
        "dscto": dscto, 
        "iva": iva, 
        "total_sin_dscto": total_sin_dscto, 
        "total_sin_dscto_mas_IVA": total_sin_dscto_mas_IVA }