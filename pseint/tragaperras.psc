Algoritmo holaMundo
	rep<-"s"
	s<-"s"
	mientras rep="s" Hacer
		n1<-1
		n2<-2
		n3<-3
		dinero<-25
		gano<-0
		Mientras s="s" Hacer
			Escribir "presione cualquier tecla"
			mientras n1 <> n2 o n1 <> n3 o n2 <> n3 Hacer
				n1<-Aleatorio(1,7)
				n2<-Aleatorio(1,7)
				n3<-Aleatorio(1,7)
				Mientras n1 = 1 o n1=2 hacer
					gano<-5
				FinMientras
				Mientras n1 = 1 o n1=2 hacer
					gano<-10
				FinMientras
				Mientras n1 = 1 o n1=2 hacer
					gano<-15
				FinMientras
				Mientras n1 = 1 o n1=2 hacer
					gano<-25
				FinMientras
				Escribir n1,"//",n2,"//",n3
					Escribir "perdiste,presione cualquier tecla"
					Esperar Tecla
			FinMientras
			Escribir "ganaste"
			dinero<-dinero+gano
			escribir "quieres intentar de nuevo?"
			leer s
			Esperar Tecla
		FinMientras
		escribir "quieres jugar de nuevo"
		leer rep
	FinMientras
FinAlgoritmo
