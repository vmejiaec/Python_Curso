from decimal import Decimal,ROUND_HALF_UP

def main():
    print ("Proyecto")
    print("Ficha del Producto")
    print("------------------------")
    print("Ingrese los siguientes datos:")
    producto_nombre =  input("\tNombre: ")
    producto_codigo = input("\tCódigo: ")
    producto_cantidad = int(input("\tCantidad: "))
    producto_precio = Decimal(input("\tPrecio: "))
    print("------------------------")
    # Presentar el producto ingresado
    print("------------------------")
    print("Datos del producto")
    print(f"{producto_codigo} : {producto_nombre} - {producto_cantidad} und. - ${producto_precio}")
    print("------------------------")
    # Presentar el menú de cálculos
    print("Menú de cálculos")
    print("\t1 - Cálculo del total")
    print("\t2 - Cálculo del descuento del 10%")
    print("\t3 - Cálculo del IVA del 15%")
    print("\t4 - Cálculo del Total menos dscto y más IVA")
    print("\t5 - Reporte")
    print("\t0 - Salir del programa")
    # Procesar la opción seleccionada
    seleccion = 1
    while seleccion >0 :
        seleccion = int(input("Elija una opción del menú: "))
        # Constantes y Cálculos
        CENT = Decimal("0.01")
        PORC_DSCTO = Decimal("0.1")
        PORC_IVA = Decimal("0.15")
        total = producto_cantidad * producto_precio
        dscto = total * PORC_DSCTO
        dscto = dscto.quantize(CENT, rounding=ROUND_HALF_UP)
        total_menos_dscto = total - dscto
        iva = total_menos_dscto * PORC_IVA
        iva = iva.quantize(CENT, rounding=ROUND_HALF_UP)
        total_menos_dscto_mas_IVA = total_menos_dscto + iva
        # Presentación 
        if seleccion == 1:
            print(f"\t\tTotal: ${total}")
        if seleccion == 2:
            print(f"\t\tDescuento: ${dscto}")
        if seleccion == 3:
            print(f"\t\tIVA: ${iva}")
        if seleccion == 4:
            print(f"\t\tTotal - Dscto + IVA: ${total_menos_dscto_mas_IVA}")
        if seleccion == 5:
            print(f"{producto_codigo} : {producto_nombre} - {producto_cantidad} und. - ${producto_precio}")
            print(f"\tTotal: \t\t\t{total}")
            print(f"\tDscto 10%: \t\t{dscto}")
            print(f"\tTotal - Dscto: \t\t{total_menos_dscto}")
            print(f"\tIVA: \t\t\t{iva}")
            print(f"\tTotal - Dscto + IVA: \t{total_menos_dscto_mas_IVA}")
        print("------------------------")

if __name__ == "__main__":
    main()