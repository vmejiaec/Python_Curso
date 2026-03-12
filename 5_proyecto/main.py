
from interfaz.salida import presentar_menu, presentar_producto,presentar_reporte, presentar_menu_seleccion
from interfaz.entrada import ingresar_producto
from aplicacion.calculos import calcular_venta

def main():

    lista_productos = []
    continua = "S"
    while continua != "N":
        producto = ingresar_producto()
        lista_productos.append(producto)
        continua = input("Desea continuar? (S/N)")

    for item in lista_productos:
        presentar_producto(item)
    
    presentar_menu()
    
    resultados = calcular_venta(producto)
    opcion = 1
    while opcion >0 :        
        opcion = int(input("Elija una opción del menú: "))
        presentar_menu_seleccion(opcion, producto, resultados)

if __name__ == "__main__": main()