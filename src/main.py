# Documentacion del main

"""
Modulo principal.
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
import convertidor_de_unidades_internacional_y_anglosajon as c_i_a

def main():
    c_i_a.convertidor_de_unidades_internacional_y_anglosajon()

### Comprobación de main ###

if __name__ == "__main__":
    main()