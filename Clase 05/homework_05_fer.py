import random as r 
import numpy as np
import time as t
import os 

class JuegoPila:
    
    def __init__(self):
        self.__pila = []
        self.__extracciones = 0
        self.__lista_extracciones = []
        self.__ganador = False
        self.__calificacion = 10

    def __cargar_pila(self):
        array = np.arange(1,21)
        np.random.shuffle(array)
        self.__pila = list(array)
        return None

    def __mensaje_inicio(self):
        os.system('cls')
        print(">>>>>>>> BIENVENIDO AL JUEGO PILACARTA <<<<<<<< \n\n")
        print(">>El Mazo Ha Sido Mezclado.")
        return None
    
    def __solicitar_extracciones(self):
        entrada = input("Ingrese La cantidad de Cartas que desea Extrear del Mazo: ")
        
        while(True):
            if (not entrada.isdigit() or int(entrada) < 0 or int(entrada) > 20):
                entrada = input("(X) El valor ingresado no es un numero valido. Ingrese un entero entre 1 y 20: ")
            else:
                self.__extracciones = int(entrada)
                break
        return self.__realizar_extracciones()

    def __realizar_extracciones(self):
        if(not self.__esta_vacia()):
            print("\n\n>> Extraeras {} cartas del maso...\n".format(self.__extracciones))
            t.sleep(4)
            for i in range(self.__extracciones):
                self.__lista_extracciones.append(self.__pop())
                print("Carta Extraida: ", self.__lista_extracciones[-1])
                t.sleep(2)
        return None
    
    def __calcular_puntaje(self):

        if(sum(self.__lista_extracciones) <= 50):
            self.__ganador = True
        
        while(True):
            self.__lista_extracciones.append(self.__pop())
            if(sum(self.__lista_extracciones) <= 50):
                self.__calificacion -= 1
            else:
                break
        return self.__mostrar_puntaje()
    
    def __mostrar_puntaje(self):
        if(self.__ganador):
            print("\n\nFELICITACIONES!!! HA GANADO EL JUEGO!!!")
            print("\n\n>> SU PUNTAJE ES DE: ", self.__calificacion)
            print("\n>> SE EXTRAJERON OTRAS {} CARTAS HASTA SUPERAR 50, LAS CUALES FUERON: {}".format(self.__size() - self.__extracciones, self.__lista_extracciones[self.__extracciones:]))
        else:
            print("\n\nGAME OVER!!! HAS PERDIDO EL JUEGO!!!")

        return None

    def __mensaje_final(self):
        print("\n\n\n >>>>>>>> GRACIAS POR JUGAR AL JUEGO PILACARTA <<<<<<<< \n\n\n")
        opcion = str.upper(input("\n\n\n>>>>>>>> DESEA VOLVER A JUGAR? (S/N): "))
        while(True):
            if(opcion not in ("S", "N")):
                opcion = input("\n\n\n>>>>>>>> OPCION INGRESADA INCORRECTA. DESEA VOLVER A JUGAR? >>> (S/N):  ")
            else:
                break

        if(opcion == "S"):
            os.system('cls')
            return True
        else:
            print("\n\n\n!!! JUEGO FINALIZADO !!!")
            return False
    
    def __esta_vacia(self):
        return (self.__pila == [])
    
    def __size(self):
        return len(self.__lista_extracciones)
    
    def __pop(self):
        if self.__pila:
            return self.__pila.pop()
        else:
            return None
    
    def jugar(self):
        self.__cargar_pila()
        self.__mensaje_inicio()
        self.__solicitar_extracciones()
        self.__calcular_puntaje()
        return self.__mensaje_final()
    
import random as r 
import numpy as np
import time as t
import os 
import matplotlib.pyplot as plt

class JuegoJarras:
    
    def __init__(self):
        self.__jarra5 = 0
        self.__jarra3 = 0

    def __llenar(self,jarra):
        if(jarra == 3):
            self.__jarra3 = 3
        else:
            self.__jarra5 = 5

        return self.dibujar()
    
    def __vaciar(self,jarra):
        if(jarra == 3):
            self.__jarra3 = 0
        else:
            self.__jarra5 = 0
        
        return self.dibujar()
    
    def __volcar(self,orig,dest):

        if(orig == 3 and dest == 5):    
            while(self.__jarra5 < 5 and self.__jarra3 > 0):
                self.__jarra3 -=1
                self.__jarra5 +=1
        elif(orig == 5 and dest == 3):
            while(self.__jarra3 < 3 and self.__jarra5 > 0):
                self.__jarra5 -=1
                self.__jarra3 +=1

        return self.dibujar()
    
    def dibujar(self):
        valoresx = ["Jarra 3 lts", "Jarra 5 lts"]
        valoresy = [self.__jarra3, self.__jarra5]
        plt.bar(valoresx,valoresy)
        plt.ylim(0,5)
        plt.xlabel("Jarras")
        plt.xlabel("Cant. Agua")
        plt.title("JUEGO DE LAS JARRAS")
        plt.show()
        return True
    
    def __finalizar_juego(self):
        print(">>>>> GRACIAS POR JUGAR AL JUEGO DED LAS JARRAS <<<<<\n\n")
        print(">>>>> JUEGO FINALIZADO <<<<<\n\n")
        return False
    
    def __menu_opciones(self):
        
        __opciones_validas = [1,2,3,4,5,6,7]
        
        print(">>>>> BIENVENIDO AL JUEGO DED LAS JARRAS <<<<<\n\n")
        print(">> ELIJA UNA DE LAS SIGUIENTES OPCIONES:\n")
        print("(1) Llenar la jarra de 3 litros.")
        print("(2) Llenar la jarra de 5 litros.")
        print("(3) Vaciar la jarra de 3 litros.")
        print("(4) Vaciar la jarra de 5 litros.")
        print("(5) Verter la jarra de 5 litros en la de 3 litros.")
        print("(6) Verter la jarra de 3 litros en la de 5 litros.\n\n")
        print("(7) Finalizar Juego.\n\n")

        opcion = input("Opcion: ")
        while(True):
            if(not str.isdigit(opcion) or int(opcion) not in __opciones_validas):
                opcion = input(">>> Opcion INCORRECTA. INGRESE UNA OPCION DEL 1-7: ")
            else:
                break
            
        match int(opcion):
            case 1:
                continua = self.__llenar(3)
            case 2:
                continua = self.__llenar(5)
            case 3:
                continua = self.__vaciar(3)
            case 4:
                continua = self.__vaciar(5)
            case 5:
                continua = self.__volcar(5,3)
            case 6:
                continua = self.__volcar(3,5)
            case 7:
                continua = self.__finalizar_juego()

        return continua
    
    def jugar(self):
        while(True):
            if(not self.__menu_opciones()):
                break
        return None

# while(True):
#     j = JuegoPila()
#     if(not j.jugar()):
#         break

juego = JuegoJarras()
juego.jugar()