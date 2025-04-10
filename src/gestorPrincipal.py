from Inventario import inventario
from gestorFacturas import gestorFacturas
import numpy as np
class gestorPrincipal:
    def __init__(self):
        self.gestInv = inventario()
        self.gesFac = gestorFacturas()

    def agregarAInventario(self,codigo,nombre,tipo,precio,precioVenta,unidadesDisp,porcIVA,umbral):
        if(None != self.gestInv.buscarDispositivo(codigo).codigo):
            self.gestInv.agregarDispositivo(codigo,nombre,tipo,precio,precioVenta,unidadesDisp,porcIVA,umbral)
            return True
        else:
            return False
    
    def registrarEntradaMercancia(self,codigo, cantidad):
        self.gestInv.actualizarInventario(1,codigo,cantidad)
        
    def generarVenta(self):
        opcion = "1"
        listProductos = np.empty(shape=50)
        listCantidades = np.empty(shape=50)
        ultimDisp = 0
        while (opcion != "2"):
            opcion = input("ingrese 1: para agregar un objeto a la cuenta\ningrese 2: para generar la factura\n")
            match(opcion):
                case "1":
                    codigo = input("ingrese el codigo del producto:\n")
                    cantidad = input("ingrese la cantidad de productos:\n")
                    if (self.gestInv.verificarDispo(codigo, cantidad)):
                        self.gestInv.agregarCantidadVendida(codigo,cantidad)
                        self.gestInv.actualizarInventario(0,codigo,cantidad)
                        print("se agrego el producto correctamente")
                        listProductos[ultimDisp] = self.gestInv.buscarDispositivo(codigo)
                        listProductos[ultimDisp] = cantidad
                        ultimDisp +=1
                        self.gestInv.verificarUmbral(codigo)
                    else:
                        print("no se pudo agregar el producto")
                case "2":
                    break
                case _:
                    print("error el valor seleccionado no es una opcion valida")

        self.gesFac.generarVenta(listProductos,listCantidades,ultimDisp)

    def generarInformeMensual(self):
        pass
