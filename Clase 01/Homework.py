import math
from decimal import Decimal

def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    if (type(numero) != int or (numero < 0)):
        return None
    
    lista_binario = []
    while(True):
        lista_binario.insert(0,numero%2)   
        if(numero // 2 == 0):  
            break
        else:
            numero = numero // 2

    return int(''.join(str(x) for x in lista_binario))

def FraccionBinario(numero):
    '''
    Esta función recibe como parámetro un número decimal mayor o igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo decimal binario.
    En caso de que el parámetro no sea de tipo decimal y mayor-igual a 0 retorna None.
    '''
    if (type(numero) != float):
        return None
    
    parte_decimal, parte_entera = math.modf(numero)
    tope_decimales = 24

    if (parte_entera > 0):
        parte_entera_binaria = NumeroBinario(parte_entera)
    else:
        parte_entera_binaria = 0

    lista_binario_decimal = []
    while(True):  
        if(parte_decimal * 2 == 0 or len(lista_binario_decimal) == tope_decimales):  
            break
        else:
            parte_decimal, valor = math.modf(parte_decimal * 2)
            lista_binario_decimal.append(int(valor))  

    return Decimal(str(parte_entera_binaria) + "." + ''.join(str(x) for x in lista_binario_decimal))

def NumeroBinarioRecursiva(numero):
    '''
        Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
        representación binaria. Debe recibir y devolver un valor de tipo entero.
        En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    def __NumeroBinarioRecursiva(numero):

        if (type(numero) != int or (numero < 0)):
            return None
        
        if(numero // 2 == 0):
            return str(numero%2)
        
        return __NumeroBinarioRecursiva(numero // 2) + str(numero % 2)
    
    numero_binario = __NumeroBinarioRecursiva(numero)

    if(numero_binario):
        return int(numero_binario)
    else:
        return numero_binario