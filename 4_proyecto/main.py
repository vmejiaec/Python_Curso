from decimal import Decimal,ROUND_HALF_UP
from .interfaz.consola import 
    presentar_menu, 
    presentar_producto,
    presentar_reporte

def crear_producto(nombre, codigo, cantidad, precio):
    return {
        "nombre":nombre, 
        "codigo": codigo, 
        "cantidad": cantidad, 
        "precio": precio}

def ingreso_de_datos():
    print("------------------------")
    print("Ingrese los siguientes datos:")
    nombre =  input("\tNombre: ")
    codigo = input("\tCódigo: ")
    cantidad = int(input("\tCantidad: "))
    precio = Decimal(input("\tPrecio: "))
    return crear_producto(nombre, codigo, cantidad, precio)


def crear_resultados(total, dscto, iva, total_sin_dscto, total_sin_dscto_mas_IVA):
    return {
        "total": total, 
        "dscto": dscto, 
        "iva": iva, 
        "total_sin_dscto": total_sin_dscto, 
        "total_sin_dscto_mas_IVA": total_sin_dscto_mas_IVA }

def calculos(producto):
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
    return crear_resultados(
            total, 
            dscto, 
            iva, 
            total_sin_dscto, 
            total_sin_dscto_mas_IVA)

def procesar_seleccion(producto, resultados):
    seleccion = 1
    while seleccion >0 :        
        seleccion = int(input("Elija una opción del menú: "))
        if seleccion == 1:
            print(f"\t\tTotal: ${resultados["total"]}")
        if seleccion == 2:
            print(f"\t\tDescuento: ${resultados["dscto"]}")
        if seleccion == 3:
            print(f"\t\tIVA: ${resultados["iva"]}")
        if seleccion == 4:
            print(f"\t\tTotal - Dscto + IVA: ${resultados["total_sin_dscto_mas_IVA"]}")
        if seleccion == 5:
            presentar_reporte(producto, resultados)
        print("------------------------")

def main():
    print("Ficha del Producto")    
    producto = ingreso_de_datos()    
    resultados = calculos(producto)
    presentar_producto(producto)
    presentar_menu()
    procesar_seleccion(producto, resultados)
    print("Fin del programa")


if __name__ == "__main__": main()