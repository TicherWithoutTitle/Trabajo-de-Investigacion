#import de la clase datetime para uso en las horas de trabajo
import datetime as dt                           

class Trabajador:
    #atributos:
    __nombre__:str
    __direccion__:str
    __sueldo__:float
    __horaDeIngreso__:dt.timedelta
    __horaDeEgreso__:dt.timedelta
    __horasDeTrabajo__:dt.timedelta
    #fin atributos
    
    def __init__(self, nombre:str,direccion:str|None,sueldo:float,ingreso:dt.timedelta=None,egreso:dt.timedelta=None):
        """
        Purpose: Iniciador de Trabajadores
        
        Horas de Ingreso y Egreso pueden ser dejados nulos
        """
        self.__nombre__ = nombre                #nombre del trabajador
        self.__direccion__ = direccion          #direccion del trabajador
        self.__sueldo__ = sueldo                #sueldo del trabajador
        #sino tiene hora de ingreso o egreso asigna None a todo lo que tiene q ver con las horas de trabajo
        if ingreso!=None and egreso!=None: 
            self.__horaDeIngreso__ = ingreso    #hora de ingreso del trabajador
            self.__horaDeEgreso__ = egreso      #hora de egreso del trabajador
            #las horas de trabajo se infieren a partir de la hora de ingreso y egreso del trabajo
            self.__horasDeTrabajo__=self.__horaDeEgreso__-self.__horaDeIngreso__
        else:
            self.__horasDeTrabajo__=None
            self.__horaDeIngreso__=None
            self.__horaDeEgreso__=None
    #end Init
    
    def getNombre(self):                        #retorna el nombre del trabajador
        return self.__nombre__
    # end def
    
    def getDireccion(self):                     #retorna la direccion del trabajador
        return self.__direccion__
    # end def
    
    def getSueldo(self):                        #retorna el sueldo del trabajador
        return self.__sueldo__
    # end def
    
    def getHoraDeIngreso(self):                 #retorna las horas de ingreso del trabajador
        return self.__horaDeIngreso__
    # end def
    
    def getHoraDeEgreso(self):                  #retorna las horas de egreso del trabajador
        return self.__horaDeEgreso__
    # end def
    
    def getHorasDeTrabajo(self):                #retorna las horas de trabajo totales
        return self.__horasDeTrabajo__
    # end def
    
    def setNombre(self,nombre:str):             #cambia el nombre del trabajador
        self.__nombre__=nombre
    # end def
    
    def setDireccion(self,dir):                 #cambia la direccion del trabajador
        self.__direccion__=dir
    # end def
    
    def setSueldo(self,sueldo):                 #cambia el sueldo del trabajador
        self.__sueldo__=sueldo
    # end def
    
    def setHoraDeIngreso(self,ingreso):         #cambia la hora de ingreso y las de trabajo total
        self.__horaDeIngreso__=ingreso
        self.__horasDeTrabajo__=self.__horaDeEgreso__-self.__horaDeIngreso__
    # end def
    
    def setHoraDeEgreso(self,egreso):           #cambia la hora de egreso y las de trabajo total
        self.__horaDeEgreso__=egreso
        self.__horasDeTrabajo__=self.__horaDeEgreso__-self.__horaDeIngreso__
    # end def

    def __gt__(self,other):                     #sobrecarga del operador >
        if self.__sueldo__==other.__sueldo__:
            return self.__nombre__>other.__nombre__
        return self.__sueldo__>other.__sueldo__
    # end def >
    
    def __ge__(self,other):                     #sobrecarga del operador >=
        return self.__sueldo__>=other.__sueldo__
    # end def >=
    
    def __lt__(self,other):                     #sobrecarga del operador <
        if self.__sueldo__==other.__sueldo__:
            return self.__nombre__<other.__nombre__
        return self.__sueldo__<other.__sueldo__
    # end def <
    
    def __le__(self,other):                     #sobrecarga del operador <=
        return self.__sueldo__<=other.__sueldo__
    # end def <=
    
    def __eq__(self,other):                     #sobrecarga del operador ==
        return self.__nombre__==other.__nombre__ and self.__sueldo__==other.__sueldo__
    # end def ==
    
    def __str__(self):                          #formato de salida a texto en pantalla de la clase
        return f"Trabajador:\nNombre: {self.__nombre__}\nDireccion: {self.__direccion__}\nSueldo: {self.__sueldo__}\nIngreso: {self.__horaDeIngreso__}\nEgreso: {self.__horaDeEgreso__}\nHoras de trabajo: {self.__horasDeTrabajo__}\n===================="
    # end def toString