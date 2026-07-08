Algoritmo sin_titulo
	Definir rep Como Cadena
	rep <- 's'
	Mientras rep='s' Hacer
		numpc <- aleatorio(1,20)
		mientras numus = numpc Hacer
			numus<- Aleatorio(1,20)
		FinMientras
		escribir "ADIVINA EL NUMERO"
		Esperar 1 Segundos
		Borrar Pantalla
		Escribir "-------------------------------------------------------------------------"
		Escribir "///////////////|PRESIONE CUALQUIER TECLA PARA COMENZAR|//////////////////"
		Escribir "-------------------------------------------------------------------------"
		esperar Tecla
		Mientras numpc<>numus Hacer
			Borrar Pantalla
			Escribir 'adivina el numero entre 1 y 20'
			Leer numus
			Mientras numus<=0 O numus>=21 Hacer
				Limpiar Pantalla
				Escribir 'adivina el numero entre 1 y 20'
				Leer numus
			FinMientras
			Mientras numpc<>numus Hacer
				Mientras numpc>numus Hacer
					Limpiar Pantalla
					men <- numus
					Escribir 'el numero es mayor a ', men
					Leer numus
					Mientras numus<=0 O numus>=21 Hacer
						Limpiar Pantalla
						Escribir 'el numero es mayor a ', men
						Leer numus
					FinMientras
				FinMientras
				Mientras numpc<numus Hacer
					Limpiar Pantalla
					may <- numus
					Escribir 'el numero es menor a ', may
					Leer numus
					Mientras numus<=0 O numus>=21 Hacer
						Limpiar Pantalla
						Escribir 'el numero es menor a ', may
						Leer numus
					FinMientras
				FinMientras
				Mientras numus<=0 O numus>=21 Hacer
					Limpiar Pantalla
					Escribir 'ingrese un numero entre 1 y 20'
					Leer numus
				FinMientras
			FinMientras
			Borrar Pantalla
			Escribir 'FELICIDADES GANASTE!!!!!!!!!!'
			Escribir "adivinaste el numero, el numero es ", numus
		FinMientras
		escribir "-------------------------------------------------------------------------"
		Escribir 'quieres volverlo a intentar? s/n?'
		Leer rep
		Mientras rep<>'s' Y rep<>'n' Hacer
			Limpiar Pantalla
			Escribir 'quieres volverlo a intentar? s/n?'
			Leer rep
		FinMientras
		Limpiar Pantalla
	FinMientras
FinAlgoritmo
