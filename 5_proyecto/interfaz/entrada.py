from decimal import Decimal,ROUND_HALF_UP
from dominio.producto import crear_producto

def ingresar_producto():
    print("------------------------")
    print("Ingrese los siguientes datos:")
    nombre =  input("\tNombre: ")
    codigo = input("\tCódigo: ")
    cantidad = int(input("\tCantidad: "))
    precio = Decimal(input("\tPrecio: "))
    print("------------------------")
    return crear_producto(nombre, codigo, cantidad, precio)