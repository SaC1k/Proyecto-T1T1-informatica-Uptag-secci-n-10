Funcion reloj(s,m,h)
	si s < 10 y m < 10 y h <10 Entonces
		Escribir "0",h, ":","0", m, ":","0",s
	SiNo
		si s >= 10 y m < 10 y h <10 Entonces
			Escribir "0",h, ":", "0",m, ":",s
		FinSi
		si s < 10 y m >= 10 y h <10 Entonces
			Escribir "0",h, ":", m, ":","0",s
		FinSi	
		si s >= 10 y m >= 10 y h <10 Entonces
			Escribir "0",h, ":", m, ":",s
		FinSi	
		si s < 10 y m < 10 y h >=10 Entonces
			Escribir h, ":","0", m, ":","0",s
		FinSi	
		si s >= 10 y m < 10 y h >=10 Entonces
			Escribir h, ":","0", m, ":",s
		FinSi	
		si s < 10 y m >= 10 y h >=10 Entonces
			Escribir h, ":", m, ":","0",s
		FinSi		
		si s >= 10 y m >= 10 y h >=10 Entonces
			Escribir h, ":", m, ":",s
		FinSi			
	FinSi
FinFuncion

Algoritmo sin_titulo
	h<-0
	m<-0
	s<-0
	Mientras Verdadero hacer
		reloj(s,m,h)
		esperar 1 Segundos
		s<-s+1
		si s = 60 Entonces
			m<-m+1
			s<--60
		FinSi
		si m = 60 Entonces
			h<-h+1
			m<--60
		FinSi
		si h = 24 Entonces
			h<-h-24
		FinSi
		Borrar Pantalla
	FinMientras
FinAlgoritmo
