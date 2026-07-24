"""
Modulo convertidor de unidades de masa 
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

def mostrar_menu_unidades():
    """Muestra la lista de unidades con su número."""

    unidades = [
        "Kilogramos (kg)",
        "Hectogramos (hg)",
        "Decagramos (dag)",
        "Gramos (g)",
        "Decigramos (dg)",
        "Centigramos (cg)",
        "Miligramos (mg)",
        "Onzas (oz)",
        "Libras (lb)",
        "Toneladas cortas (ton)"
    ]

    print("\nUnidades de masa disponibles:")
    for i, u in enumerate(unidades, 1):
        print(f"{i}. {u}")
    return unidades

def obtener_opcion_menu(mensaje, opciones_validas):
    """Pide una opción y la valida, repitiendo hasta que sea correcta."""
    
    while True:
        try:
            opcion = input(mensaje).strip()
            if opcion in opciones_validas:
                return opcion
            print(f"Opción no válida. Debes elegir entre: {', '.join(opciones_validas)}")
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
            raise  # para salir del programa si el usuario presiona Ctrl+C
        except Exception as e:
            print(f"Error inesperado: {e}. Intenta de nuevo.")

def obtener_numero(mensaje):
    """Pide un número (float) y valida que sea correcto."""
    
    while True:
        try:
            valor = input(mensaje).strip()
            if not valor:
                print("No puedes dejar vacío. Ingresa un número.")
                continue
            return float(valor)
        except ValueError:
            print("Error: Debes ingresar un número válido (puede tener decimales).")
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
            raise
        except Exception as e:
            print(f"Error inesperado: {e}. Intenta de nuevo.")

def obtener_indice_unidad(mensaje, maximo):
    """Pide un número de unidad y valida que esté en el rango."""
    
    while True:
        try:
            entrada = input(mensaje).strip()
            if not entrada:
                print("No puedes dejar vacío. Ingresa un número.")
                continue
            indice = int(entrada)
            if 1 <= indice <= maximo:
                return indice - 1  # devuelve índice 0-based
            print(f"Debes elegir un número entre 1 y {maximo}.")
        except ValueError:
            print("Error: Debes ingresar un número entero.")
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
            raise
        except Exception as e:
            print(f"Error inesperado: {e}. Intenta de nuevo.")

def convertir_masa(valor, unidad_origen, unidad_destino, factores):  
    """pide el valor de origen y lo convierte al valor de destino
    arg:toma el valor anterior y usando el diccionario com valores de conversion a gramos lo lleva hacia la unidad de destino"""
    
    try:
        return valor * factores[unidad_origen] / factores[unidad_destino]
    except KeyError:
        raise ValueError("Unidad no soportada.")

def main():
    """muestra y define los factores, valores y unidades que son convertidas"""
    print("=== CONVERSOR DE UNIDADES DE MASA ===\n")
    
    # Definimos los factores de conversión a GRAMOS (base)
    factores = {
        "Kilogramos (kg)": 1000.0,
        "Hectogramos (hg)": 100.0,
        "Decagramos (dag)": 10.0,
        "Gramos (g)": 1.0,
        "Decigramos (dg)": 0.1,
        "Centigramos (cg)": 0.01,
        "Miligramos (mg)": 0.001,
        "Onzas (oz)": 28.3495,
        "Libras (lb)": 453.592,
        "Toneladas cortas (ton)": 907184.74  # 1 tonelada corta = 907.18474 kg
    }

    while True:
        # Mostrar unidades y obtener lista de nombres
        unidades = mostrar_menu_unidades()
        maximo = len(unidades)

        # Seleccionar unidad de origen
        idx_origen = obtener_indice_unidad(
            f"\nElige el número de la unidad de ORIGEN (1-{maximo}): ",
            maximo
        )
        origen = unidades[idx_origen]

        # Seleccionar unidad de destino
        idx_destino = obtener_indice_unidad(
            f"Elige el número de la unidad de DESTINO (1-{maximo}): ",
            maximo
        )
        destino = unidades[idx_destino]

        # Si origen y destino son iguales, podemos advertir y continuar igual
        if origen == destino:
            print("(Has elegido la misma unidad, el resultado será el mismo valor)")

        # Obtener el valor a convertir
        valor = obtener_numero("Ingresa el valor a convertir: ")

        # Realizar la conversión
        try:
            resultado = convertir_masa(valor, origen, destino, factores)
            print(f"\n✅ {valor} {origen} = {resultado:.6f} {destino}")

        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")

        # Preguntar si desea hacer otra conversión
        continuar = obtener_opcion_menu(
            "\n¿Deseas hacer otra conversión? (s/n): ",
            ['s', 'n', 'S', 'N']
        ).lower()
        if continuar == 'n':
            print("\n¡Hasta luego!")
            break

if __name__ == "__main__":
    print(
        " Error: Este archivo es un MÓDULO y no se puede ejecutar directamente."
    )