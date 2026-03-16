class producto:
    def __init__(self, 
                 codigo,
                 nombre,
                 codigo_categoria,
                 stock,
                 precio,
                 esta_de_promocion = False,
                 esta_exento_iva = False):
        self.codigo = codigo
        self.nombre = nombre
        self.codigo_categoria = codigo_categoria
        self.stock = stock
        self.precio = precio
        self.esta_de_promocion = esta_de_promocion
        self.esta_exento_iva = esta_exento_iva
