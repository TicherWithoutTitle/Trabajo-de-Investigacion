#import de la clase ListaTrabajadores
import controllerTrabajadorModule.trabajador_Controller as t

class Menu:
    #atributos:
    __controlador__:t.ListaTrabajadores
    #fin atributos
    
    def __init__(self):
        """
        Purpose: Crear Menu
        """
        self.__controlador__=t.ListaTrabajadores()
    # end Crear Menu
    
    def menu(self):
        entrar=True                                     #variable de control del bucle while
        while(entrar):
            #variable de control del match y printeo de opciones
            eleccion=int(input(self.__opciones__()))    
            match (eleccion):
                case (1):
                    #comment: bucle de agregado de trabajadores
                    flag=True                           #variable de control del bucle de agregado
                    while(flag):
                        self.__controlador__.agregarTrabajador()
                        agregar=input("¿Desea Agregar otro trabajador? Si/No: ").lower()
                        #chequeo de eleccion de salida del usuario
                        if "no"==agregar or "n"==agregar:
                            flag=False
                    # end while
                # end case
                
                case (2):
                    #comment: agrega un unico trabajador
                    self.__controlador__.agregarTrabajador()
                # end case
                
                case (3):
                    #comment: envia la lista de trabajadores a un archivo txt
                    self.__controlador__.toText()
                # end case
                
                case (4):
                    #comment: ordena la lista por sueldo
                    self.__controlador__.ordenarPorSueldo()
                # end case
                
                case (5):
                    #comment: printea el trabajador que mas gana
                    print(self.__controlador__.max())
                # end case
                
                case (6):
                    #comment: printea el trabajador que menos gana
                    print(self.__controlador__.min())
                # end case
                
                case (7):
                    #comment: printea en pantalla la lista completa de trabajadores
                    print(*[trab for trab in self.__controlador__.getLista()])
                # end case
                
                case (8):
                    #commment: printea en pantalla la cantidad de trabajadores 
                    print(f"Cantidad de trabajadore{self.__controlador__.getCantidadDeTrabajadores()}")
                # end case
                
                case (9):
                    #comment: sale del programa
                    entrar=False
                # end case
                
                case (34):
                    #comment: uso exclusivo para test
                    self.__controlador__.__test__()
                    self.__controlador__.toText()
                case (_):
                    print("Esa opcion no es valida")
            # end match
        # end while       
    # end def
    
    def __opciones__(self):
        return """===============================
1. Agregar 1 o más trabajadores
2. Agregar 1 solo trabajador
3. Pasar trabajadores a un archivo
4. Ordenar trabajadores por sueldo ascendente
5. Obtener el maximo sueldo
6. Obtener el minimo sueldo
7. Escribir en pantalla los trabajadores
8. Escribir en pantalla cantidad de trabajadores
9. Salir
===============================
Seleccion: """
    # end def