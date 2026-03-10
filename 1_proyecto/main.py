def main():
    print ("Proyecto")
    print("Ficha del Producto")
    print("------------------------")
    print("Ingrese los siguientes datos:")
    producto_nombre =  input("\tNombre: ")
    producto_codigo = input("\tCódigo: ")
    producto_cantidad = int(input("\tCantidad: "))
    producto_precio = float(input("\tPrecio: "))
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
    print("\t0 - Salir del programa")
    # Procesar la opción seleccionada
    seleccion = 1
    while seleccion >0 :
        seleccion = int(input("Elija una opción del menú: "))
        total = producto_cantidad * producto_precio
        total_menos_dscto = total - total * 0.1
        total_menos_dscto_mas_IVA = total_menos_dscto - total_menos_dscto*0.15
        if seleccion == 1:
            print(f"\t\tTotal: ${total}")
        if seleccion == 2:
            print(f"\t\tDescuento: ${total * 0.1}")
        if seleccion == 3:
            print(f"\t\tIVA: ${total_menos_dscto * 0.15}")
        if seleccion == 4:
            print(f"\t\tTotal - Dscto + IVA: ${total_menos_dscto_mas_IVA}")
        print("------------------------")

if __name__ == "__main__":
    main()