# Documentación del main

"""
Módulo principal del Selector de Convertidores de Unidades.
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

# Importación de librerías y módulos.

import sys
import os
import func_convertidor_de_unidades_internacional_y_anglosajon
import func_conversor_de_volumen
import func_convertidor_de_masa
import func_unidades_de_temperatura
import func_unidades_tiempo

def main():
    """
    Función principal del Selector de Convertidores de Unidades.
        1. Convertidor de Longitud
        2. Convertidor de Masa (Próximamente)
        3. Convertidor de Volumen (Próximamente)
        4. Convertidor de Temperatura (Próximamente)
        5. Convertidor de Tiempo (Próximamente)
        6. Salir
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

    os.system('cls' if os.name == 'nt' else 'clear')
    print("BIENVENIDO AL...")
    
    print(r"""
 _____ _____ _   _ _   _ ___________ _____ ___________ ___________  ______ _____   _   _ _   _ ___________  ___ ______ _____ _____ 
/  __ \  _  | \ | | | | |  ___| ___ \_   _|_   _|  _  \  _  | ___ \ |  _  \  ___| | | | | \ | |_   _|  _  \/ _ \|  _  \  ___/  ___|
| /  \/ | | |  \| | | | | |__ | |_/ / | |   | | | | | | | | | |_/ / | | | | |__   | | | |  \| | | | | | | / /_\ \ | | | |__ \ `--. 
| |   | | | | . ` | | | |  __||    /  | |   | | | | | | | | |    /  | | | |  __|  | | | | . ` | | | | | | |  _  | | | |  __| `--. \
| \__/\ \_/ / |\  \ \_/ / |___| |\ \  | |  _| |_| |/ /\ \_/ / |\ \  | |/ /| |___  | |_| | |\  |_| |_| |/ /| | | | |/ /| |___/\__/ /
 \____/\___/\_| \_/\___/\____/\_| \_| \_/  \___/|___/  \___/\_| \_| |___/ \____/   \___/\_| \_/\___/|___/ \_| |_/___/ \____/\____/ 
                                                                                                                                   
                                                                                                                                   """)

    print("El Convertidor de Unidades te espera...")
    input("\n=== PRESIONA ENTER PARA INICIAR EL PROGRAMA ===")

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 100)
        print("MENU DE OPCIONES DEL CONVERTIDOR".center(100))

        opciones = [
            "Convertidor de Longitud",     # 1 - Implementado
            "Convertidor de Masa",         # 2 - Placeholder
            "Convertidor de Volumen",      # 3 - Placeholder
            "Convertidor de Temperatura",  # 4 - Placeholder
            "Convertidor de Tiempo",       # 5 - Placeholder
            "Salir del Programa"           # 6 - Salida
        ]

        print("=" * 100)
        print(r"""
  __  __                        _                         _                       
 |  \/  |                      | |                       (_)                      
 | \  / | ___ _ __  _   _    __| | ___    ___  _ __   ___ _  ___  _ __   ___  ___ 
 | |\/| |/ _ \ '_ \| | | |  / _` |/ _ \  / _ \| '_ \ / __| |/ _ \| '_ \ / _ \/ __|
 | |  | |  __/ | | | |_| | | (_| |  __/ | (_) | |_) | (__| | (_) | | | |  __/\__ \
 |_|  |_|\___|_| |_|\__,_|  \__,_|\___|  \___/| .__/ \___|_|\___/|_| |_|\___||___/
                                              | |                                 
                                              |_|                                 
""")
        print("=" * 100)
        print("( INDICE. ) | [ OPCION. ]")
        print("-" * 80)

        for indice, opcion in enumerate(opciones):
            if opcion == opciones[-1]:
                print(f"( {indice + 1}. ) | [ {opcion}. ] | [ Control + C para Salir ]")
            else:
                print(f"( {indice + 1}. ) | [ {opcion}. ]")

        print("-" * 80)

        try:
            opcion_usuario = int(input(f"\nSeleccione una opción dentro del rango 1 a {len(opciones)}...\n >>> ")) - 1

            if 0 <= opcion_usuario < len(opciones):
                print(f"\nSeleccionó la opción: {opciones[opcion_usuario]}.")

            if opcion_usuario == 0:
                func_convertidor_de_unidades_internacional_y_anglosajon.convertidor_de_unidades_internacional_y_anglosajon()

            elif opcion_usuario == 1:
                func_convertidor_de_masa.main()

            elif opcion_usuario == 2:
                func_conversor_de_volumen.conversor_de_volumen()

            elif opcion_usuario == 3:
                func_unidades_de_temperatura.conversor_de_la_temperatura()

            elif opcion_usuario == 4:
                func_unidades_tiempo.convertidor_tiempo()

            elif opcion_usuario == 5:
                # Salir
                break

            else:
                print(f"\nError: Opción inválida. Seleccione un número entre 1 y {len(opciones)}.")

        except Exception as error:
            print(f"\nError de entrada: {error}. Intente nuevamente.")

        input("\n=== Presiona ENTER para volver al MENU PRINCIPAL ===\n")

    print("\n¡Gracias por utilizar el Convertidor de unidades!")


### Comprobación de main ###
if __name__ == "__main__":
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        main()

    except KeyboardInterrupt:
        print("\n\nError: (Control + C) Detectado salida abrupta...")

    except Exception as error:
        print(f"\nError fatal del sistema: {error}")

    print("\nSaliendo del programa...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Convertidor de unidades finalizado con éxito...\n")
    sys.exit()

else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Error: El módulo '{__name__}' no está diseñado para ser importado directamente.")