"""
Módulo para la conversión de unidades de masa mediante un menú interactivo.
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

def conversor_de_masa():
    """
    Despliega un menú interactivo en consola para convertir valores entre diferentes
    unidades de masa (métricas e imperiales) usando el gramo como unidad base.
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
    # Factores de conversión a gramos
    factores = {
        "1": ("mg", 0.001, "Miligramos"),
        "2": ("cg", 0.01, "Centigramos"),
        "3": ("dg", 0.1, "Decigramos"),
        "4": ("g", 1.0, "Gramos"),
        "5": ("dag", 10.0, "Decagramos"),
        "6": ("hg", 100.0, "Hectogramos"),
        "7": ("kg", 1000.0, "Kilogramos"),
        "8": ("oz", 28.349523125, "Onzas"),
        "9": ("lb", 453.59237, "Libras"),
        "10": ("st", 6350.29318, "Stone"),
        "11": ("ton", 907184.74, "Toneladas cortas "),
    }
    # Se muestra el menu de unidades
    while True:
        print("="*90)
        print("""
        1. Miligramos (mg)
        2. Centigramos (cg)
        3. Decigramos (dg)
        4. Gramos (g)
        5. Decagramos (dag)
        6. Hectogramos (hg)
        7. Kilogramos (kg)
        8. Onzas (oz)
        9. Libras (lb)
        10. Stone (st)
        11. Toneladas cortas (ton)
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
        # 1. Pasamos a gramos
        gramos = cantidad_origen * factores[origen][1]
        # 2. Convertimos de gramos a la unidad destino
        resultado = gramos / factores[destino][1]

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