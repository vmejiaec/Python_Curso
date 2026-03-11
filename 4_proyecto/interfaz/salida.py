def presentar_menu():
    print("--------------------------------------------------")
    print("Menú de cálculos")
    print("\t1 - Cálculo del total")
    print("\t2 - Cálculo del descuento del 10%")
    print("\t3 - Cálculo del IVA del 15%")
    print("\t4 - Cálculo del Total menos dscto y más IVA")
    print("\t5 - Reporte")
    print("\t0 - Salir del programa")
    print("--------------------------------------------------")

def presentar_producto(producto):
    print("------------------------")
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
