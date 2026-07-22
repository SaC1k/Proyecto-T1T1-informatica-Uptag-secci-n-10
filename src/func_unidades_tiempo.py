"""
Módulo de conversiones de tiempo
---
Args:
   none.
---
Returns:
    none.
---
Raises:
  except: Por si el usuario ingresa un número inválido
---

Este módulo proporciona una interfaz interactiva de consola para realizar
conversiones entre distintas unidades de tiempo (milisegundos, segundos,
minutos, horas y días) utilizando los segundos como unidad base intermediaria.
"""


def convertidor_tiempo():
    """
    Módulo de conversiones de tiempo
    ---

    La función gestiona todo el flujo del programa:
        1. Presenta un menú desplegable con las opciones disponibles.
        2. Valida las selecciones del usuario (unidades de origen y destino).
        3. Solicita y valida la cantidad numérica a convertir.
        4. Realiza el cálculo utilizando el segundo como unidad base.
        5. Muestra el resultado y consulta al usuario si desea continuar o salir.

    Args:
       none.
    ---
    Returns:
        none.
    ---
    Raises:
      except: Por si el usuario ingresa un número inválido
    ---
    """

    # Factores de conversión a segundos
    factores = {
        "1": ("ms", 0.001, "Milisegundos"),
        "2": ("s", 1.0, "Segundos"),
        "3": ("m", 60.0, "Minutos"),
        "4": ("h", 3600.0, "Horas"),
        "5": ("d", 86400.0, "Días"),
    }

    while True:
        print("\n" + "=" * 90)
        print("    CONVERTIDOR DE TIEMPO")
        print("=" * 90)
        print("1. Milisegundos (ms)")
        print("2. Segundos (s)")
        print("3. Minutos (m)")
        print("4. Horas (h)")
        print("5. Días (d)")
        print("6. Salir")
        print("=" * 90)

        # Elegir opción de origen
        origen = input("Selecciona la unidad de ORIGEN (1-6): ").strip()
        if origen == "6":
            print("\n¡Hasta luego!")
            break

        if origen not in factores:
            print(" Opción inválida. Intenta de nuevo.")
            continue

        # Elegir opción de destino
        destino = input("Selecciona la unidad de DESTINO (1-5): ").strip()
        if destino not in factores:
            print(" Opción inválida. Intenta de nuevo.")
            continue

        # Pedir la cantidad a convertir
        try:
            cantidad = float(input("Ingresa la cantidad a convertir: "))
               # Validar que la cantidad no sea negativa
            if cantidad <= 0:
                print(" Error: No puedes ingresar un valor negativo de tiempo o 0 .")
                continue
        except ValueError:
            print(" Error: Debes ingresar un número válido.")
            continue

        # Realizar el cálculo
        # 1. Pasamos a segundos
        segundos = cantidad * factores[origen][1]
        # 2. Convertimos de segundos a la unidad destino
        resultado = segundos / factores[destino][1]

        # Mostrar resultado
        simbolo_origen = factores[origen][0]
        simbolo_destino = factores[destino][0]
        print(
            f"\n RESULTADO: {cantidad} {simbolo_origen} = {resultado:.4f} {simbolo_destino}"
        )

        # Preguntar si desea hacer otra conversión
        print("\n" + "-" * 90)
        otra = (
            input("¿Deseas realizar otra conversión? (s/n): ").strip().lower()
        )
        if otra != "s":
            print("\n¡Gracias por usar el convertidor! Hasta luego.")
            break


# Iniciar el programa
if __name__ == "__main__":
    convertidor_tiempo()
