
from interfaz.salida import presentar_menu, presentar_producto,presentar_reporte, presentar_menu_seleccion
from interfaz.entrada import ingresar_producto, ingresar_menu_seleccion
from aplicacion.calculos import calcular_venta

def main():

    producto = ingresar_producto()    
    resultados = calcular_venta(producto)
    presentar_producto(producto)
    presentar_menu()
    seleccion = 1
    while seleccion >0 :        
        seleccion = ingresar_menu_seleccion()
        presentar_menu_seleccion(seleccion, producto, resultados)

if __name__ == "__main__": main()