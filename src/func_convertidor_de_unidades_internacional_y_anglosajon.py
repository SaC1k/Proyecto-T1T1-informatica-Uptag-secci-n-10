# Documentacion del main

"""
Modulo convertidor de unidades internacional y anglosajon.
--- 
Args:
    None.
--- 
Returns:
    None.
--- 
Raises:
    Exception: Si ocurre un error inesperado.
--- 
"""

# Importacion de librerias y modulos.

import sys
import time
import os
import platform
import random

def validar_entrada(mensaje, parametro1, parametro2, tipo):
    """
    Funcion principal Validar entrada.
    -
            Recibe la entrada de datos que ingrese el usuario, valida si el dato entra en los requerimientos y retorna este dato.
    
    Args:
        - msg es el mensaje que le indica al usuario que debe de ingresar.
        - parametro1 establece el limite de valores(numero) que puede ingresar el usuario (el minimo).
        - parametro2 establece el limite de valores(numero) que puede ingresar el usuario (el maximo).
    ---

    Returns:
        La entrada del usuario ya validada.
    ---

    Raises:
        Exception = Si ocurre un error inesperado.
    ---
    """

    print("-"*100)

    while True:
        try:
            if tipo == 1:
                entrada = int(input(mensaje))
        
                if parametro1 <= entrada <= parametro2:
                    break
        
                else:
                    print("-"*100+"\n"+"ERROR","\nPor favor, ingrese un numero valido...", "(" + str(parametro1), "-", str(parametro2) + ")","\n"+"-"*100)
                    entrada = "f"
        
            elif tipo == 2:
                entrada = float(input(mensaje))
                if entrada >= 0:
                    break
        
                else:
                    print("-"*100+"\n"+"ERROR","\nPor favor, ingrese un numero positivo valido...","\n"+"-"*100)
                    entrada = "f"
        
        except ValueError:
            print("-"*100+"\n"+"ERROR","\nPor favor, ingrese un numero valido...","\n"+"-"*100)
            entrada = "f"
            
        if entrada != "f":
            print("-"*100)
            break
    return entrada

def devolver_cadena(cadena, cadenaIs, cadenaAn):
    """
    Funcion principal Devolver entrada.
    -
            Cambia el valor entero del dato de tipo entero a una cadena de caracteres, sean nombres o sufijos.
    
    Args:
        - cadena
            el valor de esta variable va a ser cambiado por una cadena de testo segun su valor
            
        - cadenaIs
            es la lista de cadenas de caracteres del sistema internacional (nombres o sufijos) cual se utilizara para intercambiar el valor de dato
                tambien sirve de limite para asignar las cadenas de texto del sistema anglosajon
        
        - cadenaAn
            es la lista de cadenas de caracteres del sistema anglosajon (nombres o sufijos) cual se utilizara para intercambiar el valor de dato

    ---

    Returns:
        Retorna el dato con su cadena asignada.
    ---

    Raises:
        Exception = Si ocurre un error inesperado.
    ---
    """

    #Apartir de aqui, se van cambiando los valores numericos por cadenas de texto, que estan guardadas dentro de arreglos
    if cadena > len(cadenaIs):
        cadena = cadenaAn[cadena - len(cadenaIs) - 1]


    else:
        cadena = cadenaIs[cadena - 1]
    return cadena

def convertir_unidadis(valor_final, unidad1, unidad2, unidad):
    """
    Funcion principal Converir unidadis.
    -
            Cambia el valor entero del dato de tipo entero a una cadena de caracteres, sean nombres o sufijos.
    
    Args:
        - cadena
            el valor de esta variable va a ser cambiado por una cadena de testo segun su valor
            
        - cadenaIs
            es la lista de cadenas de caracteres del sistema internacional (nombres o sufijos) cual se utilizara para intercambiar el valor de dato
                tambien sirve de limite para asignar las cadenas de texto del sistema anglosajon
        
        - cadenaAn
            es la lista de cadenas de caracteres del sistema anglosajon (nombres o sufijos) cual se utilizara para intercambiar el valor de dato

    ---

    Returns:
        Retorna el dato con su cadena asignada.
    ---

    Raises:
        Exception = Si ocurre un error inesperado.
    ---
    """

    unidad1 = unidad[unidad1 - 1]
    unidad2 = unidad[unidad2 - 1]

    while unidad1 != unidad2:
        if unidad1 > unidad2:
            unidad1 = unidad1 / 10
            valor_final = valor_final * 10
    
        elif unidad1 < unidad2:
            unidad1 = unidad1 * 10
            valor_final = valor_final / 10
    
    return valor_final


def convertir_unidadan(valor_final, unidad1, unidad2, unidad):
    """
    Funcion principal Converir unidadan.
    -
            Recibe el valor ingresado por el usuario y lo transforma segun sus indicaciones(parametros)
    
    Args:
        - valor_final
            Es el valor ingresado por el usuario
    
        - unidad1
            Es la unidad asignada al valor, utilizada para poder convertirlo a la unidad2
        
        - unidad2
            Es una condicion para establecer si el valor a sido convertido o no
        
        - unidad
            es un arreglo con un conjunto de valores, valores los cuales se acceden gracias a la unidad1 y unidad2
                los valores del arreglos deben ser digitos (flotantes)
                
                Los valores de los arreglos deben de estar ordenados correctamente(segun el sistema anglosajon)
                
                La cantidad de datos maxima debe ser menor a diferencia de la que puede ser el maximo que tiene unidad1 y unidad2 en uno
                por ejemplo, unidad1 y unidad2 pueden tener un maximo de 4 opciones
                y la cantidad de datos dentro del arreglo debe ser menor en 1, 3.
    ---

    Returns:
        La el valor ingresado por el usuario pero ya convertido a la unidad que eligio.
    ---

    Raises:
        Exception = Si ocurre un error inesperado.
    ---
    """

    unidad1 = unidad1 - 1
    unidad2 = unidad2 - 1

    while unidad1 != unidad2:
        if unidad1 > unidad2:
            unidad1 = unidad1 - 1
            valor_final = valor_final * unidad[unidad1]

        elif unidad1 < unidad2:
            valor_final = valor_final / unidad[unidad1]
            unidad1 = unidad1 + 1

    return valor_final

def convertidor_de_unidades_internacional_y_anglosajon():
    while True:    

        # Unidades del sistema internacional (kilometro, hectometro, decametro, metro, decimetro, centimetro, milimetro)
        unidadis = [10 ** 3, 10 ** 2, 10 ** 1, 10 ** 0, 10 ** -1, 10 ** -2, 10 ** -3]
        nombreIs = ["Kilometros", "Hectometros", "Decametros", "Metros", "Decimetros", "Centimetros", "Milimetros"]
        sufijoIs = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
        
        # Unidades del sistema anglosajon (pulgada, pies, yardas, millas)
        unidadan = [12, 3, 1760]
        nombreAn = ["Pulgadas", "Pies", "Yardas", "Millas"]
        sufijoAn = ["in", "f", "yd", "mi"]
        
        # Valores de conversion entre los dos sistemas 
        # Para pulgada, pies y yardas los valores estan convertidos en centimetros
        # Para millas lo el valor esta convertido en kilometros
        unidadcon = [2.54, 30.48, 91.44, 1.609]
        
        # Establesco el limite que se utilizara como parametro más adelante
        # Amentandolo en dos para que tambien acepte la ultima unidad del sistema anglosajon y el numero de salida
        limite_is=len(unidadis)
        limite_an=limite_is+(len(unidadan)+1)
        limite_op = len(unidadis) + len(unidadan) + 2
        
        listaUnidad = f"""
Unidades del Sistema Internacional                          Unidades del Sistema Anglosajon
01 | Kilometro/km            05 | Decimetro/dm              08 | Pulgada/In           11 | Millas/mi
02 | Hectometro/hm           06 | Centimetro/cm             09 | Pies/f               12 | Salir del Convertidor de unidades de longitud.
03 | Decametro/dam           07 | Milimetro/mm              10 | Yardas/yd
04 | Metro/m
----------------------------------------------------------------------------------------------------
"""

        print("\n"+"-"*100)
        print(" "*30+"Convertidor de unidades de longitud")

        unidadEntrada = sufijoEntrada = nombreEntrada = validar_entrada(mensaje=listaUnidad+"Seleccione la unidad que quiere convertir: ", parametro1=1, parametro2=limite_op, tipo=1)

        print("-"*100)
    
        if unidadEntrada == limite_op:
            break

        nombreEntrada = devolver_cadena(cadena= nombreEntrada, cadenaIs= nombreIs, cadenaAn= nombreAn)
        sufijoEntrada = devolver_cadena(cadena= sufijoEntrada, cadenaIs= sufijoIs, cadenaAn= sufijoAn)
        
        unidadSalida = sufijoSalida = nombreSalida = validar_entrada(mensaje=listaUnidad+"\nDe "+nombreEntrada+" a cual otra unidad la desea convertir: ", parametro1=1, parametro2=limite_op, tipo=1)
        
        print("-"*100)

        if unidadSalida == limite_op:
            break
        
        nombreSalida = devolver_cadena(cadena= nombreSalida, cadenaIs= nombreIs, cadenaAn= nombreAn)
        sufijoSalida = devolver_cadena(cadena= sufijoSalida, cadenaIs= sufijoIs, cadenaAn= sufijoAn)
        
        # Evalua sí el programa requiere llamar cual funcion o usar cual proceso o si el requisito de igualda entre unidades elegidas por el usuario se cumple
        
        valor = validar_entrada(mensaje="\nIngrese el valor que quieres convertir de "+nombreEntrada+" a "+nombreSalida+": ", parametro1=1, parametro2=limite_op, tipo=2)
        print("-"*100)
        
        if unidadEntrada==unidadSalida:
            valorFinal= valor
        
        # Conversion interna (sistema internacional)
        elif (1 <= unidadEntrada <= limite_is) and (1 <= unidadSalida <= limite_is):
            valorFinal = convertir_unidadis(valor_final=valor, unidad1=unidadEntrada, unidad2=unidadSalida, unidad=unidadis)

        # Conversion interna (sistema anglosajon)
        elif ( (limite_is+1) <= unidadEntrada <= limite_an) and ( (limite_is+1) <= unidadSalida <= limite_an):
            valorFinal = convertir_unidadan(valor_final=valor, unidad1=(unidadEntrada - limite_is), unidad2=(unidadSalida - limite_is), unidad=unidadan)

        # Conversion cruzada o mixta (sistema internacional a sistema anglosajon)
        elif (1 <= unidadEntrada <= limite_is) and ( (limite_is+1) <= unidadSalida <= limite_an):
            
            # Dependiendo de la unidad, esta se puede transformar en alguna de las diferentes unidades del sistema anglosajos
            if unidadSalida == 11:
                # El dato de la unidad2 de la funcion tiene que concordar con la posicion del valor 10**3 en la lista, contando a partir de 1,unidadis para que no hayan errores
                
                # Esto aplica es para milla 
                valorFinal = convertir_unidadis(valor_final=valor, unidad1=unidadEntrada, unidad2=1, unidad=unidadis)

            else:
                # El dato de la unidad2 de la funcion tiene que concordar con la posicion del valor 10**-2 en la lista, contando a partir de 1, unidadis  para que no hayan errores 
                # Esto aplica es para pulgadas, pies y yardas
                valorFinal = convertir_unidadis(valor_final=valor, unidad1=unidadEntrada, unidad2=6, unidad=unidadis)
                
            valorFinal = valorFinal / unidadcon[unidadSalida -(limite_is) -1]

        # Conversion cruzada o mixta (sistema anglosajon a sistema internacional)
        elif ((limite_is+1) <= unidadEntrada <= limite_an) and (1 <= unidadSalida <= limite_is) :
            
            # Dependiendo de la unidad, esta se puede transformar en alguna de las diferentes unidades del sistema internacional
            # Esto es para preparar la conversion dentro del sistema internacional
            valorFinal = valor * unidadcon[unidadEntrada - (limite_is) -1]


            if unidadEntrada == 11:
                # Esto aplica es para milla
                # El dato de la unidad de entrada tiene que concordar con la posicion del valor 10**3 de la lista, contando a partir de 1, unidadis para que no hayan errores
                unidadEntrada = 1

            else:
                # Esto aplica es para pulgadas, pies y 
                # El dato de la unidad de entrada tiene que concordar con la posicion del valor 10**-2 en la lista, contando a partir de 1, unidadis para que no hayan errores 
                unidadEntrada = 6

            valorFinal = convertir_unidadis(valor_final=valorFinal, unidad1=unidadEntrada, unidad2=unidadSalida, unidad=unidadis)
        
        print("De "+nombreEntrada+" a "+nombreSalida+".","\n\n"+str(valor) + sufijoEntrada, "es igual a", str(valorFinal) + sufijoSalida)  
        
        opcion = validar_entrada(mensaje="""
                                1 | Ir al menu.
                                2 | Salir del convertidor de longitudes.
----------------------------------------------------------------------------------------------------
Seleccione una de las siguientes opciones: """, 
parametro1=1, parametro2=2, tipo=1)

        if opcion == 2:
            break

### Comprobación de main ###

if __name__ == "__main__":
    print("ERROR CORRIENDO COMO MODULO")