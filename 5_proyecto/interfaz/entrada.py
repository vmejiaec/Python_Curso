from decimal import Decimal,ROUND_HALF_UP
from dominio import Producto

def ingresar_producto():
    print("------------------------")
    print("Ingrese los siguientes datos:")
    nombre =  input("\tNombre: ")
    codigo = input("\tCódigo: ")
    stock = int(input("\tStock: "))
    precio = Decimal(input("\tPrecio: "))
    print("------------------------")
    return Producto(codigo, nombre, "C01" , stock, precio)