import numpy as np
from Dispositivo import Dispositivo
import os
class inventario:
    """ La clase Inventario como su nombre lo dice tiene un vector que guarda todos los dispositivos que van entrando al almacen de la empresa
        cada dispositivo tiene sus respectivos datos y son almacenados en el vector Inventario"""
    
    def __init__(self):
        self.inventario = np.empty(shape = 100, dtype=Dispositivo)
        self.__numDispositivos = 0

    @property
    def numDispositivos(self):
        return self.__numDispositivos 

    def agregarDispositivo(self,codigo, nombre, tipo, precio, precioVenta, unidadesDisp, porcIVA, umbral):
        """ Cada que se use este metodo (el usuario desee agregar nuevos articulos) el programa va a crear un nuevo objeto de tipo Dispositivo
            y lo va a guardar en la casilla correspondiente (la variable ult se encarga de asignar esta posicion)"""
        
        for i in range (self.__numDispositivos):
            if (self.inventario[i].codigo == codigo):
                 return False
        self.inventario[self.__numDispositivos] = Dispositivo(codigo,nombre,tipo,precio,unidadesDisp,porcIVA,umbral,precioVenta)
        self.__numDispositivos += 1
        return True
    
    def buscarDispositivo(self,codigo):
        for i in range(self.__numDispositivos):
            if (self.inventario[i].codigo == codigo):
                return self.inventario[i]
        return None

    
    def verificarDispo(self, codigo, cantidad):
        """ Este metodo recibe el codigo de producto y lo busca en el vector inventario, una vez lo encuentre
            compara las unidades disponibles con la cantidad que el usuario pretende comprar 
            si hay unidades suficientes retorna true de lo contrario false"""
        
        for i in range (self.__numDispositivos):
            if ((codigo == self.inventario[i].codigo)&(cantidad<= self.inventario[i].unidadesDisp)):
                return True
        return False
    
    def verificarUmbral(self, codigo):
        """ El metodo umbral recibe el codigo de producto y analiza la cantidad disponible con el umbral que ingreso el usuario
            la idea es que se use cada vez que se modifiquen las unidades en el inventario de cada producto y el metodo por si solo 
            si hay menos unidades que el umbral va a mostrar el respectivo mensaje"""
        
        for i in range (self.__numDispositivos):
            if (codigo == self.inventario[i].codigo):
                if(self.inventario[i].unidadesDisp > self.inventario[i].umbral):
                    return "el dispositivo: "+self.inventario[i].nombre+" cuenta con: "+str(self.inventario[i].unidadesDisp)+" unidades disponibles en Inventario"
                else:
                    return  "el dispositivo: "+self.inventario[i].nombre+" cuenta con: "+self.inventario[i].unidadesDisp+" unidades disponibles en Inventario, Es necesario solicitar mas"
            else:
                return "Error: el dispositivo con codigo: "+codigo+" No se pudo encontrar en el sistema"
            
    def actualizarInventario(self, opcion:int, codigo, cantidad):
        """ Este metodo agrupa dos funciones mediante un switch, una para restar los objetos vendidos del inventario 
            y otra para sumar las nuevas unidades que hallan entrado a la bodega, este switch no lo maneja el usuario,
            el progrma lo gestiona de manera automatica"""
        match(opcion):
            case 0:
                """opcion 0: sirve para registrar en el inventario del producto las unidades retiradas del inventario"""
                for i in range(self.__numDispositivos):
                    if (self.inventario[i].codigo == codigo):
                        self.inventario[i].unidadesDisp -= cantidad
                
            case 1:
                """opcion 1: sirve para registrar las unidades que ingresan a la bodega de la empresa y sumarlas a las unidades del respectivo product"""
                for i in range(self.__numDispositivos):
                    if (self.inventario[i].codigo == codigo):
                        self.inventario[i].unidadesDisp += cantidad
                        return True
                    
    def limpiarVentas(self):
        """ Este metodo recorre todo el vector de objetos y para limpiarlo le asigna el valor null a la casilla
            se usa luego de generar el informe para volver a reunir datos para el informe del siguiente mes"""
        
        for i in range (self.__numDispositivos):
            self.inventario[i].cantidadVendida = 0
            self.inventario[i].gananciaPorCantidad = 0

    def agregarCantidadVendida(self, codigo,cantidad):
        """ Este metodo se utiliza para llevar un conteo de la cantidad de dispositivos vendida y calcular luego para el informe
            por lo general debe usarse despues de cada venta"""
        for i in range(self.__numDispositivos):
            if (codigo ==  self.inventario[i].codigo):
                self.inventario[i].cantidadVendida += cantidad

    def calcularGanancias(self):
        """sirve para calcular las ganancias objeto por objeto registrado y luego llevarlo al informe"""
        for i in range (self.__numDispositivos):
            self.inventario[i].calcularGanancias()

    def almacenarInventario(self, opcion):
        match(opcion):
            case 1:
                #en caso de querer guardar informacion de el inventario de productos en un archivo
                try:
                    file= open("ficheros\\inventario.csv","w",encoding="utf-8")
                    file.write("Codigo;Nombre;Tipo;Precio;Precio Venta;Unidades Disp;porcentaje IVA;Umbral;Ganancia;Precio IVA;Cantidad Vendida;Ganancia por Cantidad\n")
                    for i in range(self.__numDispositivos):
                        linea = self.inventario[i].codigo+";"+self.inventario[i].nombre+";"+self.inventario[i].tipo+";"+str(self.inventario[i].precio)+";"+str(self.inventario[i].precioVenta)+";"+str(self.inventario[i].unidadesDisp)+";"+str(self.inventario[i].porcentajeIVA)+";"+str(self.inventario[i].umbral)+";"+str(self.inventario[i].ganancia)+";"+str(self.inventario[i].precioIVA)+";"+str(self.inventario[i].cantidadVendida)+";"+str(self.inventario[i].gananciaPorCantidades)+"\n"
                        file.write(linea)
                    return True
                except Exception as error:
                    print(error)
                    return False
                finally:
                    file.close()
            case 2:
                try:
                    file= open("ficheros\\inventario.csv","r")
                    linea = file.readline()
                    while(linea != ""):
                        linea = file.readline()
                        a = linea.split(";")
                        self.agregarDispositivo(a[0],a[1],a[2],int(a[3]),int(a[4]),int(a[5]),int(a[6]),int(a[7]))
                    return True
                except Exception as error:
                    print(error)
                    return False
                finally:
                    file.close()