#import de la clase datetime para uso en las horas de trabajo
import datetime as dt
#import de la clase random para uso en tests
import random as rd
#import de la clase filedialog para su uso en el guardado de archivos 
from tkinter import filedialog

#import de la clase numpy para su uso en lista ndarray
import numpy as np

#import de la clase Trabajador
import classTrabajadorModule.trabajador as trab

class ListaTrabajadores:
    #atributos:
    __lista__:np.ndarray
    __ordenado__:bool                               #saber si se encuentra ordenado
    #fin atributos
    
    def __init__(self):
        """
        Purpose: Iniciador de la lista
        """
        self.__lista__=np.ndarray(0,dtype=trab.Trabajador)
        self.__ordenado__=False
    # end Init
    
    def getLista(self):                         #retorna la lista de trabajadores
        return self.__lista__
    # end def

    def getCantidadDeTrabajadores(self):        #retorna la cantidad de trabajadores de la lista
        return self.__lista__.size
    # end def

    def agregarTrabajador(self):                #agrega un trabajador a la lista
        self.__ordenado__=False
        self.__lista__.resize(self.__lista__.size+1)
        nombre=input("Nombre: ")
        direccion=input("Direccion: ")
        sueldo=float(input("Sueldo: ").replace(",","."))
        ordenado=True
        while(ordenado):
            horaIngreso=float(input("Hora de Ingreso: "))
            minutosIngreso=float(input("Minuto de Ingreso: "))
            horaEgreso=float(input("Hora de Egreso: "))
            minutosEgreso=float(input("Minutos de Egreso: "))
            ingreso=dt.timedelta(minutes=minutosIngreso,hours=horaIngreso)
            egreso=dt.timedelta(minutes=minutosEgreso,hours=horaEgreso)
            if(ingreso<egreso):
                ordenado=False
            else:
                print("El horario de salida es anterior al de llegada, escribalo correctamente")
        self.__lista__[self.__lista__.size-1]=trab.Trabajador(nombre,direccion,sueldo,ingreso,egreso)
    # end def
        
    def ordenarPorSueldo(self):                 #ordena la lista por sueldo de menor a mayor
        self.__ordenado__=True
        self.__lista__.sort()
    # end def

    def buscarTrabajador(self):
        #busca un trabajador por nombre y sueldo (ambos deben coincidir)
        print("Buscando trabajador, indique:\n")
        nombre=input("Nombre: ")
        sueldo=float(input("Sueldo: ").replace(",","."))
        for trabj in self.__lista__:
            if trabj==trab.Trabajador(nombre=nombre,direccion=None,sueldo=sueldo):
                return trabj
        return False
    # end def

    def toText(self):                           #guarda la lista en un archivo (mejora pendiente)
        try:
            #peticion al usuario de directorio y nombre del archivo
            file=filedialog.asksaveasfilename(defaultextension="txt",filetypes=["Texto .txt"],initialfile="archivo.txt")
            self.__lista__.tofile(file,sep=",",format="%s")
        except:
            #en caso de seleccionar cancelar
            print("Usted cancelo la operacion de guardado")
    #end def
    
    def max(self):                              #devuelve el trabajador con sueldo mas alto
        if(self.__ordenado__):                      #si esta ordenado devuelve el ultimo
            return self.__lista__[-1]
        return self.__lista__.max()
    # end def
    
    def min(self):                              #devuelve el trabajador con sueldo mas bajo
        if(self.__ordenado__):                      #si esta ordenado devuelve el primero
            self.__lista__[0]
        return self.__lista__.min()
    # end def
    
    """
    Metodos de Test
    (sin documentar)
    """
    
    def __test__(self):
        # self.__cantidad__+=1
        # if self.__expansion__==self.__cantidad__:
        self.__lista__.resize(self.__lista__.size+1)
        # nombre=input("Nombre: ")
        # direccion=input("Direccion: ")
        sueldo=float(rd.randint(1,3))
        # ingreso=input("Ingreso: ")
        # egreso=input("Egreso: ")
        self.__lista__[self.__lista__.size-1]=trab.Trabajador(None,None,sueldo=sueldo)
    # end def
    
    def __agregarTrabajadorTest__(self):
        self.__cantidad__+=1
        if self.__expansion__==self.__cantidad__:
            self.__lista__.resize(self.__lista__.size+self.__expansion__)
        # nombre=input("Nombre: ")
        # direccion=input("Direccion: ")
        sueldo=float(input("Sueldo: ").replace(",","."))
        # ingreso=input("Ingreso: ")
        # egreso=input("Egreso: ")
        self.__lista__[self.__cantidad__-1]=trab.Trabajador(sueldo=sueldo)
    # end def
    
    def __buscarTrabajadorTest__(self):
        print("Buscando trabajador, indique:\n")
        nombre=input("Nombre: ")
        # direccion=input("Direccion: ")
        sueldo=float(input("Sueldo: ").replace(",","."))
        t1=trab.Trabajador(nombre=nombre,direccion=None,sueldo=sueldo)
        # return self.__lista__.any(axis=0,where=[t1])
        a=np.ufunc.reduce(self.__lista__,axis=0,dtype=trab.Trabajador,out=None,)
        return a
    # end def
    
    def __toTextTest__(self):
        self.__lista__.tofile("/home/ticher/Documentos/Facultad/Unidad 2/Trabajo de Investigacion/archivo.txt",sep=",",format="%s")
    # end def