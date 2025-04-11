import numpy as np
from Venta import Venta
import os
class gestorFacturas:
    def __init__(self):
        self.ListaFacturas = np.empty(shape=100, dtype=object)
        self.ultFactura = 0

    def generarVenta(self, dispositivos:np.array, cantidades:np.array,ult:int):
        self.ListaFacturas[self.ultFactura] = Venta((self.ultFactura+1),dispositivos,cantidades,ult)
        self.ListaFacturas[self.ultFactura].calcularPrecioTotal()
        input(("").ljust(50,"-")+"\n"+(self.ListaFacturas[self.ultFactura].imprimirFactura())+"\n"+("").ljust(50,"-")+"\nPresione enter para continuar")
        os.system("cls")