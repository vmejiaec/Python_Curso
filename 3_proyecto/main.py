from decimal import Decimal,ROUND_HALF_UP

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

def presentar_producto(producto):
    print("------------------------")
    print("Datos del producto")
    print(f"{producto["codigo"]} : "
          f"{producto["nombre"]} - "
          f"{producto["cantidad"]} und. - "
          f"${producto["precio"]}" )

def presentar_menu_calculos():
    print("------------------------")
    print("Menú de cálculos")
    print("\t1 - Cálculo del total")
    print("\t2 - Cálculo del descuento del 10%")
    print("\t3 - Cálculo del IVA del 15%")
    print("\t4 - Cálculo del Total menos dscto y más IVA")
    print("\t5 - Reporte")
    print("\t0 - Salir del programa")

def crear_respuesta(total, dscto, iva, total_sin_dscto, total_sin_dscto_mas_IVA):
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
    return crear_respuesta(
            total, 
            dscto, 
            iva, 
            total_sin_dscto, 
            total_sin_dscto_mas_IVA)

def presentar_reporte(producto):
    presentar_producto(producto)
    respuesta = calculos(producto)
    print(f"\tTotal: \t\t\t{respuesta["total"]}")
    print(f"\tDscto 10%: \t\t{respuesta["dscto"]}")
    print(f"\tTotal - Dscto: \t\t{respuesta["total_sin_dscto"]}")
    print(f"\tIVA: \t\t\t{respuesta["iva"]}")
    print(f"\tTotal - Dscto + IVA: \t{respuesta["total_sin_dscto_mas_IVA"]}")

def procesar_seleccion(producto):
    # Constantes y Cálculos
    respuesta = calculos(producto)
    # Procesar selección
    seleccion = 1
    while seleccion >0 :        
        seleccion = int(input("Elija una opción del menú: "))

        # Presentación 
        if seleccion == 1:
            print(f"\t\tTotal: ${respuesta["total"]}")
        if seleccion == 2:
            print(f"\t\tDescuento: ${respuesta["dscto"]}")
        if seleccion == 3:
            print(f"\t\tIVA: ${respuesta["iva"]}")
        if seleccion == 4:
            print(f"\t\tTotal - Dscto + IVA: ${respuesta["total_sin_dscto_mas_IVA"]}")
        if seleccion == 5:
            presentar_reporte(producto)
        print("------------------------")

def main():
    print("Ficha del Producto")    
    producto = ingreso_de_datos()    
    presentar_producto(producto)
    presentar_menu_calculos()
    procesar_seleccion(producto)
    print("Fin del programa")


if __name__ == "__main__": main()