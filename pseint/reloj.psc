Algoritmo reloj
	Definir h, m, s, op Como Entero
	Escribir 'reloj fantastico"
	Escribir '1// reloj"
	Escribir '2// cronometro"
	Escribir '3// temporizador"
	Leer op
	Repetir
		Si op<1 O op>3 Entonces
			Leer op
		FinSi
	Hasta Que op=1 O op=2 O op=3
	Escribir op
	Si op=1 Entonces
		Escribir 'elige la hora de entrada:'
		Leer h
		Limpiar Pantalla
		Si h<0 Entonces
			h <- h*(-1)
		FinSi
		Si h>23 Entonces
			Repetir
				h <- h-23
			Hasta Que h<24
		FinSi
		Escribir h, ':', '00', ':', '00'
		Leer m
		Limpiar Pantalla
		Si h<0 Entonces
			h <- h*(-1)
		FinSi
		Si m<0 Entonces
			m <- m*(-1)
		FinSi
		Si h>23 Entonces
			Repetir
				h <- h-23
			Hasta Que h<24
		FinSi
		Si m>59 Entonces
			Repetir
				m <- m-59
				h <- h+1
			Hasta Que m<60
		FinSi
		Escribir h, ':', m, ':', '00'
		Leer s
		Limpiar Pantalla
		Si h<0 Entonces
			h <- h*(-1)
		FinSi
		Si m<0 Entonces
			m <- m*(-1)
		FinSi
		Si s<0 Entonces
			s <- s*(-1)
		FinSi
		Si h>23 Entonces
			Repetir
				h <- h-23
			Hasta Que h<24
		FinSi
		Si m>59 Entonces
			Repetir
				m <- m-59
				h <- h+1
			Hasta Que m<60
		FinSi
		Si s>=59 Entonces
			Repetir
				s <- s-59
				m <- m+1
			Hasta Que s<60
		FinSi
		Escribir h, ':', m, ':', s
		Si h<0 Entonces
			h <- h*(-1)
		FinSi
		Si m<0 Entonces
			m <- m*(-1)
		FinSi
		Si s<0 Entonces
			s <- s*(-1)
		FinSi
		Escribir h, ':', m, ':', s
		escribir "presione cualquier tecla para empezar"
		Esperar Tecla
		Limpiar Pantalla
		Repetir
			Escribir '/-------/'
			Escribir h, ':', m, ':', s
			Escribir '/-------/'
			Esperar 1 Segundos
			s <- s+1
			Si s>=59 Entonces
				Repetir
					s <- s-59
					m <- m+1
				Hasta Que s<60
			FinSi
			Si m>=59 Entonces
				Repetir
					m <- m-59
					h <- h+1
				Hasta Que m<60
			FinSi
			Si h>23 Entonces
				Repetir
					h <- h-23
				Hasta Que h<24
			FinSi
			Limpiar Pantalla
		Hasta Que h=25
	FinSi
	Si op=2 Entonces
		h <- 0
		m <- 0
		s <- 0
		Escribir h, ':', m, ':', s
		escribir "presione cualquier tecla para empezar"
		Esperar Tecla
		Limpiar Pantalla
		Repetir
			Escribir '/-------/'
			Escribir h, ':', m, ':', s
			Escribir '/-------/'
			Esperar 1 Segundos
			s <- s+1
			Si s>=59 Entonces
				Repetir
					s <- s-59
					m <- m+1
				Hasta Que s<60
			FinSi
			Si m>=59 Entonces
				Repetir
					m <- m-59
					h <- h+1
				Hasta Que m<60
			FinSi
			Si h>23 Entonces
				Repetir
					h <- h-23
				Hasta Que h<24
			FinSi
			Limpiar Pantalla
		Hasta Que h=25
	FinSi
	si op = 3 entonces 
		h1 <- 0
		m1 <- 0
		s1 <- 0
		Escribir 'elige la hora de entrada:'
		Leer h
		Limpiar Pantalla
		Si h<0 Entonces
			h <- h*(-1)
		FinSi
		Si h>23 Entonces
			Repetir
				h <- h-23
			Hasta Que h<24
		FinSi
		Escribir h, ':', '00', ':', '00'
		Leer m
		Limpiar Pantalla
		Si h<0 Entonces
			h <- h*(-1)
		FinSi
		Si m<0 Entonces
			m <- m*(-1)
		FinSi
		Si h>23 Entonces
			Repetir
				h <- h-23
			Hasta Que h<24
		FinSi
		Si m>59 Entonces
			Repetir
				m <- m-59
				h <- h+1
			Hasta Que m<60
		FinSi
		Escribir h, ':', m, ':', '00'
		Leer s
		Limpiar Pantalla
		Si h<0 Entonces
			h <- h*(-1)
		FinSi
		Si m<0 Entonces
			m <- m*(-1)
		FinSi
		Si s<0 Entonces
			s <- s*(-1)
		FinSi
		Si h>23 Entonces
			Repetir
				h <- h-23
			Hasta Que h<24
		FinSi
		Si m>59 Entonces
			Repetir
				m <- m-59
				h <- h+1
			Hasta Que m<60
		FinSi
		Si s>=59 Entonces
			Repetir
				s <- s-59
				m <- m+1
			Hasta Que s<60
		FinSi
		Escribir h, ':', m, ':', s
		Si h<0 Entonces
			h <- h*(-1)
		FinSi
		Si m<0 Entonces
			m <- m*(-1)
		FinSi
		Si s<0 Entonces
			s <- s*(-1)
		FinSi
		Escribir h, ':', m, ':', s
		escribir "presione cualquier tecla para empezar"
		Esperar Tecla
		Limpiar Pantalla
		Repetir
			Escribir '/-------/'
			Escribir h, ':', m, ':', s
			Escribir '/-------/'
			Esperar 1 Segundos
			s <- s-1
			Si s<0 Entonces
				Repetir
					s <- 59
					m <- m-1
				Hasta Que s>0
			FinSi
			Si m<0 Entonces
				Repetir
					m <- 59
					h <- h-1
				Hasta Que m>1
			FinSi
			Si h>23 Entonces
				Repetir
					h <- h-23
				Hasta Que h<24
			FinSi
			Limpiar Pantalla
		Hasta Que h=h1 y m=m1 y s=s1
		Escribir '/-------/'
		Escribir h, ':', m, ':', s
		Escribir '/-------/'
	FinSi
FinAlgoritmo
