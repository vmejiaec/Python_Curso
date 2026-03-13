def crear_producto(
        nombre, 
        codigo, 
        cantidad, 
        precio,
        esta_promocion = False,
        esta_exento = False):
    return {
        "nombre":nombre, 
        "codigo": codigo, 
        "cantidad": cantidad, 
        "precio": precio,
        "esta_promocion": esta_promocion,
        "esta_exento": esta_exento}