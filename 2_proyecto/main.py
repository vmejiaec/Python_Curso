from decimal import Decimal,ROUND_HALF_UP

def ingreso_de_datos():
    print("------------------------")
    print("Ingrese los siguientes datos:")
    nombre =  input("\tNombre: ")
    codigo = input("\tCódigo: ")
    cantidad = int(input("\tCantidad: "))
    precio = Decimal(input("\tPrecio: "))
    return nombre, codigo, cantidad, precio

def presentar_producto(codigo, nombre, cantidad, precio):
    print("------------------------")
    print("Datos del producto")
    print(f"{codigo} : {nombre} - {cantidad} und. - ${precio}")

def presentar_menu_calculos():
    print("------------------------")
    print("Menú de cálculos")
    print("\t1 - Cálculo del total")
    print("\t2 - Cálculo del descuento del 10%")
    print("\t3 - Cálculo del IVA del 15%")
    print("\t4 - Cálculo del Total menos dscto y más IVA")
    print("\t5 - Reporte")
    print("\t0 - Salir del programa")

def calculos(cantidad, precio):
    CENT = Decimal("0.01")
    PORC_DSCTO = Decimal("0.1")
    PORC_IVA = Decimal("0.15")
    total = cantidad * precio
    dscto = total * PORC_DSCTO
    dscto = dscto.quantize(CENT, rounding=ROUND_HALF_UP)
    total_sin_dscto = total - dscto
    iva = total_sin_dscto * PORC_IVA
    iva = iva.quantize(CENT, rounding=ROUND_HALF_UP)
    total_sin_dscto_mas_IVA = total_sin_dscto + iva
    return total, dscto, iva, total_sin_dscto, total_sin_dscto_mas_IVA

def presentar_reporte(codigo, nombre, cantidad, precio):
    presentar_producto(codigo, nombre, cantidad, precio)
    total, dscto, iva, total_sin_dscto, total_sin_dscto_mas_IVA = calculos(cantidad, precio)
    print(f"\tTotal: \t\t\t{total}")
    print(f"\tDscto 10%: \t\t{dscto}")
    print(f"\tTotal - Dscto: \t\t{total_sin_dscto}")
    print(f"\tIVA: \t\t\t{iva}")
    print(f"\tTotal - Dscto + IVA: \t{total_sin_dscto_mas_IVA}")

def procesar_seleccion(codigo, nombre, cantidad, precio):
    seleccion = 1
    while seleccion >0 :
        seleccion = int(input("Elija una opción del menú: "))
        # Constantes y Cálculos
        total, dscto, iva, total_sin_dscto, total_sin_dscto_mas_IVA = calculos(cantidad, precio)
        # Presentación 
        if seleccion == 1:
            print(f"\t\tTotal: ${total}")
        if seleccion == 2:
            print(f"\t\tDescuento: ${dscto}")
        if seleccion == 3:
            print(f"\t\tIVA: ${iva}")
        if seleccion == 4:
            print(f"\t\tTotal - Dscto + IVA: ${total_sin_dscto_mas_IVA}")
        if seleccion == 5:
            presentar_reporte(codigo, nombre, cantidad, precio)
        print("------------------------")

def main():
    print("Ficha del Producto")    
    nombre, codigo, cantidad, precio = ingreso_de_datos()    
    presentar_producto(codigo, nombre, cantidad, precio)
    presentar_menu_calculos()
    # Procesar la opción seleccionada
    procesar_seleccion(codigo, nombre, cantidad, precio)
    print("Fin del programa")


if __name__ == "__main__": main()