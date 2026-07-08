funcion gano<-sobre(x,y1,z)
	si x = y1 y x = z Entonces
		si x = 1 Entonces
			gano<-100
		FinSi
		si x =2 Entonces
			gano<-150			
		FinSi
		si x = 3 Entonces
			gano<-200			
		FinSi
	sino 
		escribir "perdiste"
	FinSi
FinFuncion

Algoritmo sin_titulo
	rep<-"s"
	dinero<-25
	gano<-0
	Mientras rep ="s"
		n1<-1
		n2<-2
		n3<-3
		dinero<-100
		gano<-0
		leer juego
		mientras dinero>0 y rep="s" y juego = 2 Hacer
			n1<-Aleatorio(1,7)
			n2<-Aleatorio(1,7)
			n3<-Aleatorio(1,7)
			n4<-Aleatorio(1,7)
			n5<-Aleatorio(1,7)
			n6<-Aleatorio(1,7)
			n7<-Aleatorio(1,7)
			n8<-Aleatorio(1,7)
			n9<-Aleatorio(1,7)
			sobre(aleatorio())
			Escribir n1,"//",n2,"//",n3
			dinero<-dinero-5
			si n1 = n2 y n1 = n3 y n2 = n3 Entonces
				escribir "ganaste"
				dinero<-dinero+gano
				Escribir dinero
				leer rep
			SiNo
				escribir "perdiste"
				Escribir dinero
				Esperar tecla
			FinSi
		FinMientras
		mientras dinero>0 y rep="s" y juego = 1 Hacer
			n1<-Aleatorio(1,7)
			n2<-Aleatorio(1,7)
			n3<-Aleatorio(1,7)
			si n1 = 1 o n1=2 Entonces
				gano<-25
			FinSi
			si n1 = 3 o n1=4 Entonces
				gano<-50
			FinSi
			si n1 = 5 o n1=6 Entonces
				gano<-75
			FinSi
			si n1 = 7  Entonces
				gano<-100
			FinSi
			Escribir n1,"//",n2,"//",n3
			dinero<-dinero-5
			si n1 = n2 y n1 = n3 Entonces
				escribir "ganaste"
				dinero<-dinero+gano
				Escribir dinero
				leer rep
			SiNo
				escribir "perdiste"
				Escribir dinero
				Esperar tecla
			FinSi
		FinMientras
		escribir "fin del juego"
		escribir "repetir"
		leer rep 
	finmientras
FinAlgoritmo
