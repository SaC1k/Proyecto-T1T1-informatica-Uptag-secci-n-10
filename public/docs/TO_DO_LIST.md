* [X] IMPLEMENTACIÓN #1: FALTA DE MODULARIZACIÓN DE CONVERSORES PRINCIPALES, URGENTE ARREGLO DE ERRORES ORTOGRÁFICOS, DISEÑO NO CONSISTENTE, NECESIDAD DE MEJORAS VISUALES UI/UX, DOCUMENTACIÓN NO PROFESIONAL, FALTA DE DISTINCIÓN EN LA DISTRIBUCIÓN ENTRE LOS GRUPOS Y MIEMBROS, SIN ORGANIZACIÓN NIVELADA DE ARCHIVOS Y CARPETAS CON NOMENCLATURA ESTRUCTURADA, SIN ARCHIVOS .GIT, WORKFLOWS, TEMPLATES Y PUBLIC, FALTA DE LICENCIA, VARIABLES INÚTILES, SIN DIRECTRICES DE SEGURIDAD, SIN AUTOMATIZACIONES PROLONGADAS DE AUTOAYUDA COMO DEPENDABOT O CODEQL OFICIALES DE GITHUB, SIN CONFIGURACIÓN DE IDES COMO VS CODE, SIN COMPROBACIÓN DEL

  ```
  if __name__ == "__main__":
  ```

  SIN DOCUMENTACIÓN DEL MÓDULO Y FUNCIONES EN EL ARCHIVO  `convertidor de unidades internacional y anglosajon.py`. ADEMÁS, NO SIGUE LAS DIRECTRICES DE NOMENCLATURA SNAKE_CASE, CONTENÍA ESPACIOS Y PROVOCABA ERRORES DE EJECUCIÓN EN CIERTOS ENTORNOS, SE LE DEBE AGREGAR EL SUFIJO

  ```
  "func" de manera que quede: func_convertidor_de_unidades_internacional_y_anglosajon.py
  ```

  (FRANCISCO GARCÍA) | COMO LO SOLUCIONÉ: Refactoricé integralmente el módulo y renombrando el archivo a la convención snake_case sin espacios para corregir fallos de entorno. Modularicé las funciones principales de conversión, eliminé variables redundantes y agregué la comprobación `if __name__ == "__main__":`. Añadí docstrings completos para el módulo y sus funciones, corregí la ortografía en toda la interfaz y unifiqué el diseño visual (UI/UX) en consola. Además, reestructuré la jerarquía de carpetas del proyecto, añadí la licencia, las directrices de seguridad, la asignación de miembros y la configuración de VS Code, e integré el ecosistema de `.git` con workflows, templates, directorio public y automatizaciones de GitHub como Dependabot y CodeQL. (FRANCISCO GARCÍA)
* [ ] IMPLEMENTACION #2: DESCRIPCION DEL IMPLEMENTACION (NOMBRE) | COMO LO SOLUCIONE (NOMBRE)
* [ ] IMPLEMENTACION #3: DESCRIPCION DEL IMPLEMENTACION (NOMBRE) | COMO LO SOLUCIONE (NOMBRE)
* [ ] IMPLEMENTACION #4: DESCRIPCION DEL IMPLEMENTACION (NOMBRE) | COMO LO SOLUCIONE (NOMBRE)
* [ ] IMPLEMENTACION #5: DESCRIPCION DEL IMPLEMENTACION (NOMBRE) | COMO LO SOLUCIONE (NOMBRE)

*PLANTILLA: IMPLEMENTACION #NUMERO DESCRIPCION DEL IMPLEMENTACION (NOMBRE) | COMO LO SOLUCIONE (NOMBRE)*

* Posteriormente de realizar un diagnostico de pruebas de cajas negras grupalmente no se encontro ningun error critico que detenga el programa.
* Realizaremos la reingeneria añadiendo nuevas caracteristicas. Estructuradas en este TODOLIST.
* Nos centraremos en modulizar.
