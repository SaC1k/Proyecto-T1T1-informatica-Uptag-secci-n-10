"""
Módulo de conversiones de temperatura
---
Args:
    None.
---
Returns:
    None.
---
Raises:
    Except: Por si el usuario ingresa un número inválido en la consola
---

Este módulo proporciona una interfaz interactiva de consola para realizar
conversiones entre distintas escalas de temperatura (Celsius, Fahrenheit 
y Kelvin) utilizando fórmulas matemáticas correspondientes.
"""

def conversor_de_la_temperatura():
    """
        Interfaz principal del conversor de temperatura
        ---
        Args:
        none.
        ---
        Returns:
            none.
        ---
        Raises:
        ValueError: Por si el usuario ingresa un valor de temperatura que no es numérico
        ---

        Esta función ejecuta un bucle infinito que maneja la interacción con el usuario.
        Solicita las escalas de origen y destino, captura el valor a convertir, llama 
        a la función de cálculo y muestra el resultado. Permite al usuario decidir cuándo salir.
        """ 

    ## Bucle principal del conversor de temperatura
    while True:
        print("\n" + "=" * 90)
        print("    CONVERSOR DE TEMPERATURA")         
        print("=" * 90)

    ## Solicitud de la escala base y la escala final al usuario
    
        print('Ingresa la escala que se usará como base (C, F, K):')
        escala_base = input().upper()
        if escala_base not in ('C', 'F', 'K'):
            print('Escala inválida. Intenta de nuevo.')
            continue

    ## Solicitud de la escala final al usuario 

        print('Ingresa la escala a la que se desea convertir (C, F, K):')
        escala_final = input().upper()
        if escala_final not in ('C', 'F', 'K'):
            print('Escala inválida. Intenta de nuevo.')
            continue

    ## Solicitud del valor de la temperatura al usuario y manejo de errores    

        try:
            print('Ingresa el valor de la temperatura')
            valor_de_la_temperatura = float(input())
        except ValueError:
            print('Valor inválido, intenta de nuevo.')
            continue

    ## Llamada a la función de conversión y presentación del resultado

        resultado = conversion(valor_de_la_temperatura, escala_base, escala_final)
        print(f'{valor_de_la_temperatura} {escala_base} = {resultado} {escala_final}')

        print('Ingrese la letra "S" si no desea continuar, ingrese cualquier otra tecla si desea seguir operando con normalidad')
        elegir = input()
        if elegir.lower() == 's':
            break

## Función de conversión de temperatura
def conversion(valor_de_la_temperatura, escala_base, escala_final):
    if escala_base == 'C':
        if escala_final == 'F':
            return valor_de_la_temperatura * 1.8 + 32
        elif escala_final == 'K':
            return valor_de_la_temperatura + 273.15
        else:
            return valor_de_la_temperatura
    elif escala_base == 'F':
        if escala_final == 'C':
            return (valor_de_la_temperatura - 32) / 1.8
        elif escala_final == 'K':
            return (valor_de_la_temperatura + 459.67) * 5 / 9
        else:
            return valor_de_la_temperatura
    elif escala_base == 'K':
        if escala_final == 'C':
            return valor_de_la_temperatura - 273.15
        elif escala_final == 'F':
            return valor_de_la_temperatura * 9 / 5 - 459.67
        else:
            return valor_de_la_temperatura
    else:
        return valor_de_la_temperatura

#comprobamos si el archivo se esta ejecutando como modulo
if __name__ == "__main__":
    print(
        " Error: Este archivo es un MÓDULO y no se puede ejecutar directamente."
    )