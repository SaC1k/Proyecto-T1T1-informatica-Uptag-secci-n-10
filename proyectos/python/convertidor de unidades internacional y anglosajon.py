def mostrar_resultado(valor, valor_final, sufijo1, sufijo2):
    """
    muestra el resultado final de la conversion de un valor de una unidad a otra unidad de longitud
    
    PARAMETROS
    ----------
    
    valor
        es el valor ingresado por el usuario
    
    valor_final
        el resultado
    
    sufijo1
        es el numero de la posicion dentro de los arreglos que se va a usar para acompañar el valor al final de este para indicar su unidad
    
    sufijo2
        es el numero de la posicion dentro de los arreglos que se va a usar para acompañar el valor_final al final de este para indicar su unidad
    
    Retorna
    ----------
        no retorna nada
    
    """
    
    sufijoIs = ["km", "hm", "dam", "m", "dm", "cm", "mm"]

    sufijoAn = ["in", "f", "yd", "mi"]

    nombreIs = ["kilometros", "hectometros", "decametros", "metros", "decimetros", "centimetros", "milimetros"]

    nombreAn = ["pulgadas", "pies", "yardas", "millas"]

    #Apartir de aqui, se van cambiando los valores numericos por cadenas de texto, que estan guardadas dentro de arreglos
    if sufijo1 > len(sufijoIs):
        nombre1 = nombreAn[sufijo1 - len(nombreIs) - 1]
        sufijo1 = sufijoAn[sufijo1 - len(sufijoIs) - 1]


    else:
        nombre1 = nombreIs[sufijo1 - 1]
        sufijo1 = sufijoIs[sufijo1 - 1]

    if sufijo2 > len(sufijoIs):
        nombre2 = nombreAn[sufijo2 - len(nombreIs) - 1]
        sufijo2 = sufijoAn[sufijo2 - len(sufijoIs) - 1]


    else:
        nombre2 = nombreIs[sufijo2 - 1]
        sufijo2 = sufijoIs[sufijo2 - 1]

    print("De "+nombre1+" a "+nombre2+".","\n"+str(valor) + sufijo1, "son iguales a", str(valor_final) + sufijo2)


def validar_entrada(mensaje, parametro1, parametro2, tipo):
    """
    Recibe la entrada de datos que ingrese el usuario, valida si el dato entra en los requerimientos y retorna este dato
    
    PARAMETROS
    ----------
    
    Mensaje
        Es el mensaje que le indica al usuario que debe de ingresar
    
    Parametro1
        Establece el limite de valores(numero) que puede ingresar el usuario (el minimo)
    
    Parametro2
        Establece el limite de valores(numero) que puede ingresar el usuario (el maximo)
    
    Tipo
        Le indica a la funcion que si va a usar limites o no
            1 si va a usar el limite para un rango de numeros
            2 si no va usar ese rango de numeros
    
    Retorna
    ----------
    La entrada del usuario ya validada
    """
    
    while True:
        
        try:
        
            if tipo == 1:
                entrada = int(input(mensaje))
        
                if parametro1 <= entrada <= parametro2:
                    break
        
                else:
                    print("\npor favor, ingrese un numero valido", "(" + str(parametro1), "-", str(parametro2) + ")")
                    entrada = "f"
        
            elif tipo == 2:
                entrada = float(input(mensaje))
        
        except ValueError:
            print("\npor favor, ingrese un numero valido")
            entrada = "f"
            
        #mientras que no se haya realizado ningun error al ingresar el dato, ya no se repetira el bucle
        if entrada != "f":
            break
    
    return entrada


def convertir_unidadis(valor_final, unidad1, unidad2, unidad):
    """
    Recibe el valor ingresado por el usuario y lo transforma, dentro del sistema internacional, segun sus indicaciones(parametros)
    
    PARAMETROS
    ----------
    
    valor_final
        Es el valor ingresado por el usuario
    
    unidad1
        Es la unidad asignada al valor, utilizada para poder convertirlo a la unidad2
    
    unidad2
        Es una condicion para establecer si el valor a sido convertido o no
    
    unidad
        es un arreglo con un conjunto de valores, valores los cuales se acceden gracias a la unidad1 y unidad2
            los valores del arreglos deben ser digitos (flotantes)
            
            Los valores de los arreglos deben de estar ordenados correctamente(segun el sistema internacional)
            
            La cantidad de datos maxima debe ser igual a la cantidad maxima del dato de la unidad1 y unidad2
    Retorna
    ----------
    La el valor ingresado por el usuario pero ya convertido a la unidad que eligio
    
    """
    unidad1 = unidad[unidad1 - 1]

    unidad2 = unidad[unidad2 - 1]

    while True:
    
        if unidad1 > unidad2:
            unidad1 = unidad1 / 10
            valor_final = valor_final * 10
    
        elif unidad1 < unidad2:
            unidad1 = unidad1 * 10
            valor_final = valor_final / 10
    
        elif unidad1 == unidad2:
            break
    
    return valor_final


def convertir_unidad_an(valor_final, unidad1, unidad2, unidad):
    """
    Recibe el valor ingresado por el usuario y lo transforma segun sus indicaciones(parametros)
    
    PARAMETROS
    ----------
    
    valor_final
        Es el valor ingresado por el usuario
    
    unidad1
        Es la unidad asignada al valor, utilizada para poder convertirlo a la unidad2
    
    unidad2
        Es una condicion para establecer si el valor a sido convertido o no
    
    unidad
        es un arreglo con un conjunto de valores, valores los cuales se acceden gracias a la unidad1 y unidad2
            los valores del arreglos deben ser digitos (flotantes)
            
            Los valores de los arreglos deben de estar ordenados correctamente(segun el sistema anglosajon)
            
            La cantidad de datos maxima debe ser menor a diferencia de la que puede ser el maximo que tiene unidad1 y unidad2 en uno
            por ejemplo, unidad1 y unidad2 su maximo puede ser 4, y la cantidad de datos dentro del arreglo debe ser menor en 1, 3.
    Retorna
    ----------
    La el valor ingresado por el usuario pero ya convertido a la unidad que eligio
    
    """
    unidad1 = unidad1 - 1
    unidad2 = unidad2 - 1

    while True:
    
        if unidad1 > unidad2:
            unidad1 = unidad1 - 1
            valor_final = valor_final * unidad[unidad1]

        elif unidad1 < unidad2:
            valor_final = valor_final / unidad[unidad1]
            unidad1 = unidad1 + 1

        elif unidad1 == unidad2:
            break

    return valor_final


def main():
    while True:
        
        unidadis = [10 ** 3, 10 ** 2, 10 ** 1, 10 ** 0, 10 ** -1, 10 ** -2, 10 ** -3]
        
        unidadan = [12, 3, 1760]

        unidadcon = [2.54, 30.48, 91.44, 1.609]
        
        #establesco el limite que se utilizara como parametro más adelante
        #amentandolo en dos para que tambien acepte la ultima unidad del sistema anglosajon y el numero de salida
        limite_is=len(unidadis)
        limite_an=limite_is+(len(unidadan)+1)
        limite_op = len(unidadis) + len(unidadan) + 2
        
        listaUnidad = """unidades del sistema internacional                      unidades del sistema anglosajon
01|kilometro/km            05|decimetro/dm              08|pulgada/In            11|millas/mi
02|hectometro/hm           06|centimetro/cm             09|Pies/f                12|Salir
03|decametro/dam           07|milimetro/mm              10|Yardas/yd  
04|metro/m
"""

        print("Convertidor de unidades de longitud\n")
        print(listaUnidad)
        unidadEntrada = sufijo1 = validar_entrada(mensaje="\nSeleccione la unidad que quiere convertir: ", parametro1=1,
                                                  parametro2=limite_op, tipo=1)

        if unidadEntrada == limite_op:
            print("\nPrograma finalizado")
            break
    
        print(listaUnidad)
        unidadSalida = sufijo2 = validar_entrada(mensaje="\nSeleccione la unidad en que la va a convertir: ",
                                                 parametro1=1, parametro2=limite_op, tipo=1)

        if unidadSalida == limite_op:
            print("\nPrograma finalizado")
            break
        
        """
        evalua si el programa requiere llamar cual funcion o usar cual proceso 
        o si el requisito de igualda entre unidades elegidas por el usuario se cumple
         
        """
        valor = validar_entrada(mensaje="\ningrese el valor que quieres convertir ", parametro1=1, parametro2=limite_op,
                                tipo=2)
        
        if unidadEntrada==unidadSalida:
            valorFinal= valor
            pass
        
        #conversion interna (sistema internacional)
        elif (1 <= unidadEntrada <= limite_is) and (1 <= unidadSalida <= limite_is):
            valorFinal = convertir_unidadis(valor, unidadEntrada, unidadSalida, unidadis)

        #conversion interna (sistema anglosajon)
        elif ( (limite_is+1) <= unidadEntrada <= limite_an) and ( (limite_is+1) <= unidadSalida <= limite_an):
            valorFinal = convertir_unidad_an(valor, (unidadEntrada - 7), (unidadSalida - 7), unidadan)

        #conversion cruzada o mixta (sistema internacional a sistema anglosajon)
        elif (1 <= unidadEntrada <= limite_is) and ( (limite_is+1) <= unidadSalida <= limite_an):
            
            #dependiendo de la unidad, esta se puede transformar en alguna de las diferentes unidades del sistema anglosajos
            if unidadSalida == 11:
                #el dato de la unidad de salida tiene que concordar con la posicion del valor 10**3 que no hayan errores
                #esto aplica es para milla 
                valorFinal = convertir_unidadis(valor, unidadEntrada, 1, unidadis)

            else:
                #el dato de la unidad de salida tiene que concordar con la posicion del valor 10**-2 que no hayan errores 
                #esto aplica es para pulgadas, pies y yardas
                valorFinal = convertir_unidadis(valor, unidadEntrada, 6, unidadis)
                
            valorFinal = valorFinal / unidadcon[unidadSalida -(limite_is) -1]

        #conversion cruzada o mixta (sistema anglosajon a sistema internacional)
        elif ((limite_is+1) <= unidadEntrada <= limite_an) and (1 <= unidadSalida <= limite_is) :
            
            #dependiendo de la unidad, esta se puede transformar en alguna de las diferentes unidades del sistema internacional
            #esto es para preparar la conversion dentro del sistema internacional
            valorFinal = valor * unidadcon[unidadEntrada - (limite_is) -1]


            if unidadEntrada == 11:
                #esto aplica es para milla 
                unidadEntrada = 1

            else:
                #esto aplica es para pulgadas, pies y yardas
                unidadEntrada = 6

            valorFinal = convertir_unidadis(valorFinal, unidadEntrada, unidadSalida, unidadis)
            
        mostrar_resultado(valor=valor, valor_final=valorFinal, sufijo1=sufijo1, sufijo2=sufijo2)
        
        opcion = validar_entrada(mensaje="""1|ir al menu
2|Salir

seleccione una de las siguientes opciones""", parametro1=1, parametro2=2, tipo=1)
        
        if opcion == 2:
            print("\nPrograma finalizado")
            break

main()