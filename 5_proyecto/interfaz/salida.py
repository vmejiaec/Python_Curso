
def presentar_menu():
    MENU_OPCIONES = (
        "1 - Consultar la lista de productos",
        "2 - Consultar un producto por código",
        "3 - Ingreso de un nuevo producto",
        "4 - Modificar un producto",
        "5 - Borrado de un producto",
        "0 - Salir"
    )
    print("-------------  MENU PRINCIPAL  -------------------")
    for opcion in MENU_OPCIONES:
        print(f"\t{opcion}")
    print("--------------------------------------------------")

def presentar_producto(producto):
    print("Datos del producto")
    print(f"{producto["codigo"]} : "
          f"{producto["nombre"]} - "
          f"{producto["cantidad"]} und. - "
          f"${producto["precio"]}" )

def presentar_reporte(producto, resultados):
    presentar_producto(producto)
    print(f"\tTotal: \t\t\t{resultados["total"]}")
    print(f"\tDscto 10%: \t\t{resultados["dscto"]}")
    print(f"\tTotal - Dscto: \t\t{resultados["total_sin_dscto"]}")
    print(f"\tIVA: \t\t\t{resultados["iva"]}")
    print(f"\tTotal - Dscto + IVA: \t{resultados["total_sin_dscto_mas_IVA"]}")


def presentar_menu_seleccion(seleccion, producto, resultados):
    print("------------------------")
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
    if seleccion == 0:
        print("Fin del programa")
    print("------------------------")