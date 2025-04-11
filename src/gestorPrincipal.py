from Inventario import inventario
from gestorFacturas import gestorFacturas
import numpy as np
import os
class gestorPrincipal:
    def __init__(self):
        self.gestInv = inventario()
        self.gesFac = gestorFacturas()

    def agregarAInventario(self,codigo,nombre,tipo,precio,precioVenta,unidadesDisp,porcIVA,umbral):
        if(None == self.gestInv.buscarDispositivo(codigo)):
            self.gestInv.agregarDispositivo(codigo,nombre,tipo,precio,precioVenta,unidadesDisp,porcIVA,umbral)
            return True
        else:
            return False
    
    def registrarEntradaMercancia(self,codigo, cantidad):
        if(self.gestInv.actualizarInventario(1,codigo,cantidad)):
            return True
        else:
            return False
        
    def generarVenta(self):
        opcion = "1"
        listProductos = np.empty(shape=50,dtype=object)
        listCantidades = np.empty(shape=50,dtype=int)
        ultimDisp = 0
        while (opcion != "2"):
            opcion = input((("").ljust(50,"-"))+"\n1.para agregar un objeto a la cuenta\n2. para generar la factura\n"+(("").ljust(50,"-"))+"\nIngrese la opcion deseada: ")
            os.system("cls")
            match(opcion):
                case "1":
                    codigo = input("ingrese el codigo del producto: ")
                    cantidad = int(input("ingrese la cantidad de productos: "))
                    if (self.gestInv.verificarDispo(codigo, cantidad)):
                        self.gestInv.agregarCantidadVendida(codigo,cantidad)
                        self.gestInv.actualizarInventario(0,codigo,cantidad)
                        input(("").ljust(50,"*")+"\n el producto se agrego correctamente\n"+("").ljust(50,"*")+"\nPresione enter para continuar")
                        os.system("cls")
                        listProductos[ultimDisp] = self.gestInv.buscarDispositivo(codigo)
                        listCantidades[ultimDisp] = cantidad
                        ultimDisp +=1
                        print(self.gestInv.verificarUmbral(codigo))
                    else:
                        input(("").ljust(50,"*")+("\nError, no se pudo registrar el producto\n")+("").ljust(50,"*")+"\nPresione enter para continuar")
                        os.system("cls")
                case "2":
                    break
                case _:
                    input(("").ljust(50,"*")+("\nError, Opcion invalida\n")+("").ljust(50,"*")+"\nPresione enter para continuar")
                    os.system("cls")

        self.gesFac.generarVenta(listProductos,listCantidades,ultimDisp)

    def generarInformeMensual(self):
        pass
