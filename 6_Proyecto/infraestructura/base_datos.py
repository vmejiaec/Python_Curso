from dominio import Producto, Cliente, Categoria, Factura
from decimal import Decimal

def db_productos():
    lista = [
        Producto('P011', 'Ratón', 'C01', 30, Decimal('12.33')),
        Producto('P012', 'Teclado' , 'C01',  20, Decimal('21.50')),
        Producto('P013', 'Pantalla' , 'C01',  9, Decimal('123.50')),
        Producto('P014', 'Mesa' , 'C02',  12, Decimal('32.39')),
        Producto('P015', 'Silla' , 'C02',  24, Decimal('18.89'))
    ]
    return lista

def db_clientes():
    lista = [
        Cliente('171234567', 'Pablo', 'pablo01@g.com'),
        Cliente('171234568', 'Pedro', 'pedro23@g.com'),
        Cliente('171234569', 'María', 'maria11@g.com')
    ]
    return lista

def db_categorias():
    lista = [
        Categoria('C01','Informática'),
        Categoria('C02','Hogar')
    ]
    return lista

def db_facturas():
    lista = [
        Factura('26-001','171234569','P013',2, Decimal("114.52")),
    ]
    return lista

