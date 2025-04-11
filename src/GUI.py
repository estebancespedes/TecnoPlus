from gestorPrincipal import gestorPrincipal
import os
"""este es el archivo fuente de el proyecto con la mayor parte de la interfaz de usuario"""
os.system("cls")
gp = gestorPrincipal()
gp.sacarinfoInventario()
opcion = "1"
while(opcion != "3"):
    opcion =input((("").ljust(50,"-"))+"\n1.Menu de ventas\n2.Menu de inventario\n3.Salir\n"+(("").ljust(50,"-"))+"\nIngrese la opcion deseada: ")
    os.system("cls")
    #despliegue del menu de opciones principal
    match(opcion):
        case "1":
            #opcion 1: guarda todas las interacciones con las ventas
            menu2 =input((("").ljust(50,"-"))+"\n1.Generar una nueva venta\n2.generar el informe de ventas mensual\n3.Volver\n"+(("").ljust(50,"-"))+"\nIngrese la opcion deseada: ")
            os.system("cls")
            #despliegue del segundo nivel de menu con opciones de ventas
            match(menu2):
                case "1":
                    # opcion 1: sirve para generar una nueva venta
                    gp.generarVenta()
                case "2":
                    # mas adelante se integrara la generacion del archivo con los datos del informe
                    pass
                case "3":
                    #opcion para volver vacia
                    pass
                case _:
                    #cualquier otro caso sacara mensaje de error y volvera al menu principal
                    input(("").ljust(50,"*")+("\nError, Opcion invalida\n")+("").ljust(50,"*")+"\nPresione enter para continuar")
                    os.system("cls")
        case "2":
            menu2 = input((("").ljust(50,"-"))+"\n1.Agregar nuevo dispositivo al inventario\n2.Registrar mercancia de un producto\n3.Retirar un producto\n4.Volver\n"+(("").ljust(50,"-"))+"\nIngrese la opcion deseada: ")
            os.system("cls")
            #despliegue del segundo nivel de menu con opciones referentes al inventario
            match(menu2):
                case "1":
                    #opcion 1: agregar objetos al inventario
                    if(gp.agregarAInventario(input("Ingrese el codigo de producto: "),input("Ingrese el nombre del producto: "),input("ingrese el tipo de producto: "),int(input("ingrese el precio del objeto: ")),int(input("ingrese el precio de venta del articulo: ")),int(input("ingrese el numero de unidades disponibles en el inventario: ")), int(input("ingrese el porcentaje de iva que tiene el producto: ")),int(input("ingrese el umbral minimo de unidades: ")))):
                        input(("").ljust(50,"*")+"\n el Dispositivo se agrego correctamente\n"+("").ljust(50,"*")+"\nPresione enter para continuar")
                        os.system("cls")
                    else:
                        input(("").ljust(50,"*")+("\nError, no se pudo registrar el dispositivo\n")+("").ljust(50,"*")+"\nPresione enter para continuar")
                        os.system("cls")
                case "2":
                    #opcion 2: registrar entrada de mercancia a el inventario de la empresa
                    if(gp.registrarEntradaMercancia(input("ingrese el codigo del producto: "),int(input("ingrese la cantidad de objetos que ingresaron: ")))):
                        input(("").ljust(50,"*")+"\n el inventario se actualizo correctamente\n"+("").ljust(50,"*")+"\nPresione enter para continuar")
                        os.system("cls")
                    else:
                        input(("").ljust(50,"*")+"\n Error, el inventario no se pudo actualizar\n"+("").ljust(50,"*")+"\nPresione enter para continuar")
                        os.system("cls")
                case "3":
                    #en proceso, la idea es hacer la logica que requiere la eliminacion de un dispositivo
                    pass
                case "4":
                    #este caso esta vacio porque es la opcion volver
                    pass
                case _:
                    input(("").ljust(50,"*")+("\nError, Opcion invalida\n")+("").ljust(50,"*")+"\nPresione enter para continuar")
                    os.system("cls")
        case "3":
            #opcion 3: salir
            gp.guardarinfoInventario()
            break
        case _:
            #cualquier otro caso: mensaje de error
            input(("").ljust(50,"*")+("\nError, Opcion invalida\n")+("").ljust(50,"*")+"\npresione enter para continuar")
            os.system("cls")