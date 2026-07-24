"""
Módulo para la conversión de unidades de volumen mediante un menú interactivo.
--- 
Args:
    None.
--- 
Returns:
    None.
--- 
Raises:
    None.
--- 
"""
def validar_mayor_cero(mensaje):
    """
    Solicita un número flotante y se asegura de que sea mayor a cero.
    ---
    Args:
        mensaje (str): El mensaje que se mostrará al usuario en la consola.
    ---
    Returns:
        float: El número flotante estrictamente mayor a cero ingresado por el usuario.
    ---
    Raises:
        ValueError: Si ocurre un error al intentar convertir la entrada a float.
    ---
    """
    while True:
        try:
            valor = float(input(mensaje))
            if 0<valor:
                return valor
            else:
                print("Error:La cantidad debe ser mayor a cero. Intente de nuevo.")
        except ValueError:
            print("Error: Introduzca un número válido.")

def conversor_de_volumen():
    """
    Despliega un menú interactivo en consola para convertir valores entre diferentes
    unidades de volumen (métricas e imperiales) usando el litro como unidad base.
    ---
    Args:
        None.
    ---
    Returns:
        None.
    ---
    Raises:
        None.
    ---
    """
    # Factores de conversión a litros
    factores = {
        "1": ("ml", 0.001, "Mililitros"),
        "2": ("cl", 0.01, "Centilitros"),
        "3": ("dl", 0.1, "Decilitros"),
        "4": ("l", 1.0, "litros"),
        "5": ("dal", 10.0, "Decalitros"),
        "6": ("hl", 100.0, "Hectolitros"),
        "7": ("kl", 1000.0, "Kilolitros"),
        "8": ("fl oz", 0.0284130625, "Onzas liquidas"),
        "9": ("cups", 0.284130625, "Tazas"),
        "10": ("pt", 0.56826125, "pintas"),
        "11": ("gal", 4.54609, "galones"),
    }
    # Se muestra el menu de unidades
    while True:
        print("="*90)
        print("""
        1. Mililitros (ml)
        2. Centilitros (cl)
        3. Decilitros (dl)
        4. litros (l)
        5. Decalitros (dal)
        6. Hectolitros (hl)
        7. Kilolitros (kl)
        8. Onzas liquidas (fl oz)
        9. Tazas (cups)
        10. pintas (pt)
        11. galones  (gal)
        12. Salir""")
        print("="*90)
        # Elegir opción de origen
        origen = input("Selecciona la unidad de ORIGEN (1-12): ").strip()
        if origen == "12":
            print("\nSaliste del programa")
            break

        if origen not in factores:
            print(" Opción inválida. Intenta de nuevo.")
            continue

        # Elegir opción de destino
        destino = input("Selecciona la unidad de DESTINO (1-11): ").strip()
        if destino not in factores:
            print(" Opción inválida. Intenta de nuevo.")
            continue
        #el usuario ingresa la cantidad que desea convertir y se comprueba que sea valida
        cantidad_origen=validar_mayor_cero("Ingresa la cantidad a convertir: ")
        # Realizar el cálculo
        # 1. Pasamos a litros
        litros = cantidad_origen * factores[origen][1]
        # 2. Convertimos de litros a la unidad destino
        resultado = litros / factores[destino][1]

        # Mostrar resultado
        simbolo_origen = factores[origen][0]
        simbolo_destino = factores[destino][0]
        print(
            f"\n RESULTADO: {cantidad_origen} {simbolo_origen} = {resultado:.4f} {simbolo_destino}"
        )
        # Se pregunta al usuario si desea realizar otra conversion
        continuar = input("Desea continuar (s/n): ").lower()
        if continuar != "s":
            print("Saliste del programa")
            break
### Comprobación de main ###
if __name__ == "__main__":
    print("ERROR CORRIENDO COMO MODULO")
    conversor_de_volumen()