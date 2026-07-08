Algoritmo pieadra_papel_o_tijera
	Definir oppc, opus Como Entero
	oppc<-Aleatorio(1,3)
	Escribir "juego"
	Escribir 'piedra 1'
	Escribir 'tijera 2'
	Escribir 'papel 3"
	Leer opus
	Esperar 0.5 Segundos
	Borrar Pantalla
	Escribir 'piedra 1'
	Escribir 'tijera 2'
	Escribir 'papel 3"
	Escribir "/----------------------------------------------------------------------/"
	Si opus<=0 o opus>3 Entonces
		Repetir
			Borrar Pantalla
			escribir "elija de nuevo:"
			Escribir piedra "1'
			Escribir tijera "2'
			Escribir papel "3"
			Leer opus
		Hasta Que opus=1 o opus=2 o opus=3
	FinSi
	Si opus=oppc Entonces
		Escribir empate
		Escribir 'elegiste:', opus, '/---/', 'la pc eligio:', oppc
	FinSi
	si opus=1 Y oppc=2 o opus=2 Y oppc=3 o opus=3 Y oppc=1 Entonces
		Escribir "ganaste"
		Escribir 'elegiste:', opus, "//', 'la pc eligio:', oppc
	FinSi
	si oppc=1 Y opus=2 o oppc=2 Y opus=3 o oppc=3 Y opus=1 Entonces
		Escribir "perdiste'
		Escribir 'elegiste", opus, '//", 'la pc eligio", oppc
	FinSi
FinAlgoritmo