from dominio import Producto
from decimal import Decimal

def productos_lista_inicial():
    lista = [
        Producto('P011', 'Silla', 'C01', 100, Decimal('23.33')),
        Producto('P012', 'Mesa' , 'C01',  20, Decimal('123.50')),
        Producto('P013', 'Tasa' , 'C02',  30, Decimal('3.39')),
        Producto('P014', 'Vaso' , 'C02',  60, Decimal('1.89'))
    ]
    return lista