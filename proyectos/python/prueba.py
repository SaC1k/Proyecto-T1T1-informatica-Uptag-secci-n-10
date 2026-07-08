""" n cantidad de estudiantes, nota de estudiante, acumulativo de estudiante y promedio del estudiante, acumulativo de promedio de la seccion
condicionales de <=0 y >20, requisito min 12pts, lista de estudiantes aprobados, lista de estudiantes desaprobados,
"""
n=5
desaprovado=0
aprobado=0
for i in range(1,n+1):
    acum=0
    print("estudiante",i)
    for j in range(1,6):
        nota=int(input("nota qui: "))
        if nota <=0 or nota > 20:
            while nota <=0 or nota > 20:
                nota=int(input("ingrese un valor valido, nota qui: "))
        else:
            acum=acum+nota
            nombre 
    if acum/5 >=12:
        aprobado+=1
    else:
        desaprovado+=1
print("aprobados",aprobado,"desaprobados",desaprovado)