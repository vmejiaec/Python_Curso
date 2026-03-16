from dominio import producto
from decimal import Decimal

def productos_lista_inicial():
    lista = [
        producto('P010', 'Silla', 'C01', 100, Decimal('23.33')),
        producto('P010', 'Mesa' , 'C01',  20, Decimal('123.50')),
        producto('P010', 'Tasa' , 'C02',  30, Decimal('3.39')),
        producto('P010', 'Vaso' , 'C02',  60, Decimal('1.89'))
    ]
    return lista