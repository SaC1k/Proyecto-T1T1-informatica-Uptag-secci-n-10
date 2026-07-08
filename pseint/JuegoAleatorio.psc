Algoritmo JuegoAleatorio
    Definir dinero, v1, v2, v3, v4, v5, v6, v7, v8, v9 Como Entero
    Definir c1, c2, c3, i Como Entero
    Definir repetir_tiro, repetir_juego Como Caracter
    Definir gano Como Logico
    Dimension variables_temp[9]
    
    Repetir
        // Se inicializa el dinero a 100 al comenzar el juego
        dinero <- 100
        
        Repetir
            // Se restan 5 independientemente de si gana o no
            dinero <- dinero - 5
            
            // Asignar valores aleatorios (entre 1 y 3) a las 9 variables
            v1 <- Aleatorio(1,3)
            v2 <- Aleatorio(1,3)
            v3 <- Aleatorio(1,3)
            v4 <- Aleatorio(1,3)
            v5 <- Aleatorio(1,3)
            v6 <- Aleatorio(1,3)
            v7 <- Aleatorio(1,3)
            v8 <- Aleatorio(1,3)
            v9 <- Aleatorio(1,3)
            
            Escribir "--------------------------------"
            Escribir "Tirada de las 9 variables:"
            // Mostrar en orden de salida en fila de 3 y columnas de 3
            Escribir "[ ", v1, " ]  [ ", v2, " ]  [ ", v3, " ]"
            Escribir "[ ", v4, " ]  [ ", v5, " ]  [ ", v6, " ]"
            Escribir "[ ", v7, " ]  [ ", v8, " ]  [ ", v9, " ]"
            Escribir "--------------------------------"
            
            // Pasamos las variables a un arreglo temporal para contarlas fácilmente
            variables_temp[1] <- v1; variables_temp[2] <- v2; variables_temp[3] <- v3
            variables_temp[4] <- v4; variables_temp[5] <- v5; variables_temp[6] <- v6
            variables_temp[7] <- v7; variables_temp[8] <- v8; variables_temp[9] <- v9
            
            // Reiniciar contadores para esta tirada
            c1 <- 0; c2 <- 0; c3 <- 0
            
            // Contar cuántas veces aparece cada número
            Para i <- 1 Hasta 9 Hacer
                Si variables_temp[i] = 1 Entonces
					c1 <- c1 + 1 
				FinSi
                Si variables_temp[i] = 2 Entonces 
					c2 <- c2 + 1 
				FinSi
                Si variables_temp[i] = 3 Entonces 
					c3 <- c3 + 1 
				FinSi
            FinPara
            
            gano <- Falso
            
            // Verificar qué valor comparte exactamente 3 variables y sumar premios
            Si c1 = 3 Entonces
                dinero <- dinero + 100
                Escribir "¡Tres variables comparten el valor 1! Ganas 100."
                gano <- Verdadero
            FinSi
            
            Si c2 = 3 Entonces
                dinero <- dinero + 150
                Escribir "¡Tres variables comparten el valor 2! Ganas 150."
                gano <- Verdadero
            FinSi
            
            Si c3 = 3 Entonces
                dinero <- dinero + 200
                Escribir "¡Tres variables comparten el valor 3! Ganas 200."
                gano <- Verdadero
            FinSi
            
            // Condición si no se encontró ningún grupo de exactamente 3
            Si gano = Falso Entonces
                Escribir "Ningún valor apareció exactamente 3 veces. No ganas nada en esta ronda."
            FinSi
            
            Escribir "Dinero actual: ", dinero
            
            // Verificar si el juego termina por falta de dinero
            Si dinero <= 0 Entonces
                Escribir "Tu dinero llegó a 0. El juego ha terminado."
                repetir_tiro <- "no"
            SiNo
                Escribir "¿Desea repetir? (si/no)"
                Leer repetir_tiro
            FinSi
            
        Hasta Que Minusculas(repetir_tiro) = "no" O dinero <= 0
        
        // Final del juego actual, opción para reiniciar todo
        Escribir "=============================================="
        Escribir "¿Desea repetir el juego y reiniciar su dinero a 100? (si/no)"
        Leer repetir_juego
        Escribir "=============================================="
        
    Hasta Que Minusculas(repetir_juego) = "no"
    
    Escribir "Gracias por jugar. ¡Hasta pronto!"
FinAlgoritmo