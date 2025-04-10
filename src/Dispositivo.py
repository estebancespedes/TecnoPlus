class Dispositivo():
    """ La clase dispositivo con su respectivo constructor sirve para almacenar todos esos valores que son respectivos
        a cada dispositivo de manera independiente"""
    def __init__(self, codigo, nombre, tipo, precio, unidadesDisp, porcentajeIVA, umbral, precioVenta):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__tipo=tipo
        self.__precio=precio
        self.__precioVenta=precioVenta
        self.__unidadesDisp=unidadesDisp
        self.__porcentajeIVA=porcentajeIVA
        self.__umbral=umbral
        self.__ganancia=(self.__precioVenta - self.__precio)
        self.__precioIVA=((self.__precioVenta*self.__porcentajeIVA)/100)+self.__precioVenta
        self.__cantidadVendida=0
        self.__gananciaPorCantidad=0

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo):
        self.__codigo=codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,tipo):
        self.__tipo=tipo

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self,precio):
        self.__precio=precio

    @property
    def unidadesDisp(self):
        return self.__unidadesDisp

    @unidadesDisp.setter
    def unidadesDisp(self,unidadesDisp):
        self.__unidadesDisp=unidadesDisp

    @property
    def porcentajeIVA(self):
        return self.__porcentajeIVA

    @porcentajeIVA.setter
    def porcentajeIVA(self,porcentajeIVA):
        self.__porcentajeIVA=porcentajeIVA

    @property
    def umbral(self):
        return self.__umbral

    @umbral.setter
    def umbral(self,umbral):
        self.__umbral=umbral

    @property
    def precioIVA(self):
        return self.__precioIVA

    @precioIVA.setter
    def precioIVA(self,precioIVA):
        self.__precioIVA=precioIVA

    @property
    def ganancia(self):
        return self.__ganancia

    @ganancia.setter
    def ganancia(self,ganancia):
        self.__ganancia=ganancia

    @property
    def precioVenta(self):
        return self.__precioVenta

    @precioVenta.setter
    def precioVenta(self,precioVenta):
        self.__precioVenta=precioVenta

    @property
    def cantidadVendida(self):
        return self.__cantidadVendida

    @cantidadVendida.setter
    def cantidadVendida(self,cantidadVendida):
        self.__cantidadVendida=cantidadVendida

    @property
    def gananciaPorCantidad(self):
        return self.__gananciaPorCantidad

    @gananciaPorCantidad.setter
    def gananciaPorCantidad(self,gananciaPorCantidad):
        self.__gananciaPorCantidad=gananciaPorCantidad

    def __str__(self):
        return str(self.codigo)+' '+str(self.nombre)+' '+str(self.tipo)+' '+str(self.precio)+' '+str(self.unidadesDisp)+' '+str(self.porcentajeIVA)+' '+str(self.umbral)+' '+str(self.precioIVA)+' '+str(self.ganancia)+' '+str(self.precioVenta)+' '+str(self.cantidadVendida)+' '+str(self.gananciaPorCantidad)

    def gananciaPorCantidad(self):

        """ Este sirve para generar el informe, multiplica la ganancia del dispositivo por unidad y la multiplica por las cantidades que se vendieron
            se utiliza a la hora de generar el informe del mes"""
    
        self.__gananciaPorCantidad = self.__ganancia * self.__cantidadVendida
        pass 

