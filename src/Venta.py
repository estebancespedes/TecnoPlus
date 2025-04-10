class Venta():
    def __init__(self, codigo, listaDisp, listaCant, ult):
        self.__codigo = codigo
        self.__precio=0
        self.__ganancia=0
        self.__Productos=listaDisp
        self.__cantidades=listaCant
        self.__ultProducto=ult

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo):
        self.__codigo=codigo

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self,precio):
        self.__precio=precio

    @property
    def ganancia(self):
        return self.__ganancia

    @ganancia.setter
    def ganancia(self,ganancia):
        self.__ganancia=ganancia

    @property
    def Productos(self):
        return self.__Productos

    @Productos.setter
    def Productos(self,Productos):
        self.__Productos=Productos

    @property
    def cantidades(self):
        return self.__cantidades

    @cantidades.setter
    def cantidades(self,cantidades):
        self.__cantidades=cantidades

    @property
    def ultProducto(self):
        return self.__ultProducto

    @ultProducto.setter
    def ultProducto(self,ultProducto):
        self.__ultProducto=ultProducto

    def __str__(self):
        return str(self.codigo)+' '+str(self.precio)+' '+str(self.ganancia)+' '+str(self.Productos)+' '+str(self.cantidades)+' '+str(self.ultProducto)

    def calcularPrecioTotal(self):
        """ Una vez este completa la factura el metodo calcular precio total va a multiplicar el precio de los objetos por las cantidades asignadas
            y luego lo va a sumar todo para arrojar el valor total"""
        
        for i in range (self.__ultProducto):
            self.__precio += self.__Productos[i].precioIVA*self.__cantidades[i]

    def imprimirFactura(self):
        mensaje  = ("producto").ljust(20) + ("cantidad").ljust(10) + ("precio por unidad").ljust(10) 
        for i in range(self.__ultProducto):
            mensaje += "\n"+str(self.__Productos[i].nombre).ljust(20) + str(self.__cantidades[i]).ljust(10) + str(self.__Productos[i].precioIVA).ljust(10)
        self.calcularPrecioTotal
        mensaje += "\n \nPrecio Total: " + str(self.__precio)
        return mensaje
