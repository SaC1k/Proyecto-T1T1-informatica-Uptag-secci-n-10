Algoritmo sin_titulo
	rep<-"s"
	mientras rep="s" Hacer
		costo<-0.5
		costous<-0 
		leer Min
		si min = 1 y min <= 3 Entonces
			costous<-costo
			Escribir costo
		finsi
		si min > 0 y min > 3 entonces
			mientras min > 3 Hacer
				min<-min-1
				costo<-costo +0.1
			FinMientras
			costous<-costo
			escribir costous
		FinSi
		si min < 0 Entonces
			Escribir "por favor ingrese el dato correctamente"
		FinSi
		si costous > 0 Entonces
			Escribir "quieres calcular otro precio de una llamada"
			leer rep
			Mientras rep <> "s" y rep <> "n"
				leer rep
			FinMientras
		FinSi
	FinMientras
FinAlgoritmo
