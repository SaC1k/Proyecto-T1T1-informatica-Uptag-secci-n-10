Algoritmo sin_titulo
	Escribir 'resolver ecuaciones', 'a*x^2+b*x+c=0'
	Definir a, b, c, x Como Real
	Escribir 'Ingrese los siguientes valores:'
	Escribir 'ingrese el valor a:'
	Leer a
	Escribir 'ingrese el valor b:'
	Leer b
	Escribir 'ingrese el valor c:'
	Leer c
	Escribir 'analizando datos '
	cant_sub <- b^2-4*a*c
	Repetir
		Si cant_sub<0 Entonces
			Escribir 'error, no se puede realizar la operación', 'intenté de nuevo'
			Escribir 'ingrese el valor a:'
			Leer a
			Escribir 'ingrese el valor b:'
			Leer b
			Escribir 'ingrese el valor c:'
			Leer c
			cant_sub <- b^2-4*a*c
			Escribir 'analizando datos'
		FinSi
	Hasta Que cant_sub>0
	x1 <- (-b-rc(cant_sub))/2*a
	x2 <- (-b+rc(cant_sub))/2*a
	Escribir '-----------/resultados/-----------'
	Escribir 'x1 es igual a:', x1
	Escribir 'x2 es igual a:', x2
FinAlgoritmo
