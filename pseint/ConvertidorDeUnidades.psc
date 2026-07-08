Funcion entrada <- validar_entrada(mensaje, parametro1, parametro2, tipo)
    Definir entrada Como Real
    Definir valido Como Logico
    valido <- Falso
    Repetir
        Escribir ""
        Escribir mensaje Sin Saltar
        Leer entrada;
        Si tipo = 1 Entonces
            Si entrada >= parametro1 Y entrada <= parametro2 Entonces
                valido <- Verdadero;
            Sino
                Escribir ""
                Escribir "por favor, ingrese un numero valido (", parametro1, " - ", parametro2, ")"
            FinSi
        Sino
            valido <- Verdadero
        FinSi
    Hasta Que valido
FinFuncion

SubProceso mostrar_resultado(valor, valor_final, sufijo1, sufijo2)
    Definir sufijoIs, sufijoAn, nombreIs, nombreAn, nombre1, nombre2, suf1, suf2 Como Caracter
    Definir cantidad_sufijoIs Como Entero
    
    Dimension sufijoIs[7], sufijoAn[4], nombreIs[7], nombreAn[4]
    
    sufijoIs[1] <- "km"; sufijoIs[2] <- "hm"; sufijoIs[3] <- "dam"; sufijoIs[4] <- "m"; sufijoIs[5] <- "dm"; sufijoIs[6] <- "cm"; sufijoIs[7] <- "mm"
    sufijoAn[1] <- "in"; sufijoAn[2] <- "f"; sufijoAn[3] <- "yd"; sufijoAn[4] <- "mi"
    
    nombreIs[1] <- "kilometros"; nombreIs[2] <- "hectometros"; nombreIs[3] <- "decametros"; nombreIs[4] <- "metros"; nombreIs[5] <- "decimetros"; nombreIs[6] <- "centimetros"; nombreIs[7] <- "milimetros"
    nombreAn[1] <- "pulgadas"; nombreAn[2] <- "pies"; nombreAn[3] <- "yardas"; nombreAn[4] <- "millas"
	
    cantidad_sufijoIs <- 7;
	
    Si sufijo1 > cantidad_sufijoIs Entonces
        nombre1 <- nombreAn[sufijo1 - cantidad_sufijoIs]
        suf1 <- sufijoAn[sufijo1 - cantidad_sufijoIs]
    Sino
        nombre1 <- nombreIs[sufijo1]
        suf1 <- sufijoIs[sufijo1]
    FinSi
	
    Si sufijo2 > cantidad_sufijoIs Entonces
        nombre2 <- nombreAn[sufijo2 - cantidad_sufijoIs]
        suf2 <- sufijoAn[sufijo2 - cantidad_sufijoIs]
    Sino
        nombre2 <- nombreIs[sufijo2]
        suf2 <- sufijoIs[sufijo2]
    FinSi
	
    Escribir ""
    Escribir ConvertirATexto(valor), suf1, " son iguales a ", ConvertirATexto(valor_final), suf2
FinSubProceso

Funcion valor_final <- convertir_unidadis(valor_final, unidad1, unidad2, unidad)
    unidad1 <- unidad[unidad1];
    unidad2 <- unidad[unidad2];
	
    Repetir
        Si unidad1 > unidad2 Entonces
            unidad1 <- unidad1 / 10
            valor_final <- valor_final * 10
        Sino
            Si unidad1 < unidad2 Entonces
                unidad1 <- unidad1 * 10
                valor_final <- valor_final / 10
            FinSi
        FinSi
    Hasta Que unidad1 = unidad2
FinFuncion

Funcion valor_final <- convertir_unidad_an(valor_final, unidad1, unidad2, unidadan)
    Definir u1, u2 Como Entero;
    valor_final <- valor_final
	
    Repetir
        Si unidad1 > unidad2 Entonces
            unidad1 <- unidad1 - 1
            valor_final <- valor_final * unidadan[unidad1]
        Sino
            Si unidad1 < unidad2 Entonces
                valor_final <- valor_final / unidadan[unidad1]
                unidad1 <- unidad1 + 1
            FinSi
        FinSi
    Hasta Que unidad1 = unidad2
FinFuncion

Algoritmo ConvertidorDeUnidades
    Definir unidadis, unidadan, unidadcon, valor, valorFinal Como Real;
    Definir limite, unidadEntrada, unidadSalida, sufijo1, sufijo2, opcion Como Entero;
    Definir salir_programa Como Logico;
    
    Dimension unidadis[7]
    unidadis[1] <- 10^3; unidadis[2] <- 10^2; unidadis[3] <- 10^1; unidadis[4] <- 10^0
    unidadis[5] <- 10^(-1); unidadis[6] <- 10^(-2); unidadis[7] <- 10^(-3)
    
    Dimension unidadan[3]
    unidadan[1] <- 12; unidadan[2] <- 3; unidadan[3] <- 1760
    
    Dimension unidadcon[4]
    unidadcon[1] <- 2.54; unidadcon[2] <- 30.48; unidadcon[3] <- 91.44; unidadcon[4] <- 1.609
    
    limite <- 7 + 3 + 2
    salir_programa <- Falso
    
    Repetir
        Escribir "Convertidor de unidades de longitud"
        Escribir ""
        Escribir "unidades del sistema internacional                      unidades del sistema anglosajon";
        Escribir "01|kilometro/km            05|decimetro/dm              08|pulgada/In            11|millas/mi"
        Escribir "02|hectometro/hm           06|centimetro/cm             09|Pies/f                12|Salir"
        Escribir "03|decametro/dam           07|milimetro/mm              10|Yardas/yd  "
        Escribir "04|metro/m"
        Escribir ""
        
        unidadEntrada <- validar_entrada("Seleccione la unidad que quiere convertir: ", 1, limite, 1)
        sufijo1 <- unidadEntrada
		
        Si unidadEntrada = limite Entonces
            Escribir ""
            Escribir "Programa finalizado"
            salir_programa <- Verdadero;
        Sino
            Escribir ""
            Escribir "unidades del sistema internacional                      unidades del sistema anglosajon"
            Escribir "01|kilometro/km            05|decimetro/dm              08|pulgada/In            11|millas/mi"
            Escribir "02|hectometro/hm           06|centimetro/cm             09|Pies/f                12|Salir"
            Escribir "03|decametro/dam           07|milimetro/mm              10|Yardas/yd  "
            Escribir "04|metro/m"
            
            unidadSalida <- validar_entrada("Seleccione la unidad en que la va a convertir: ", 1, limite, 1);
            sufijo2 <- unidadSalida;
            
            Si unidadSalida = limite Entonces
                Escribir ""
                Escribir "Programa finalizado"
                salir_programa <- Verdadero;
            Sino
                valor <- validar_entrada("ingrese el valor que quieres convertir: ", 1, limite, 2);
                
                Si (unidadEntrada >= 1 Y unidadEntrada <= 7) Y (unidadSalida >= 1 Y unidadSalida <= 7) Entonces
                    valorFinal <- convertir_unidadis(valor, unidadEntrada, unidadSalida, unidadis)
                    
                Sino
                    Si (unidadEntrada >= 8 Y unidadEntrada <= 11) Y (unidadSalida >= 8 Y unidadSalida <= 11) Entonces
                        valorFinal <- convertir_unidad_an(valor, (unidadEntrada - 7), (unidadSalida - 7), unidadan)
                        
                    Sino
                        Si (unidadEntrada >= 1 Y unidadEntrada <= 7) Y (unidadSalida >= 8 Y unidadSalida <= 11) Entonces
                            Si unidadSalida = 11 Entonces
                                valorFinal <- convertir_unidadis(valor, unidadEntrada, 1, unidadis);
                            Sino
                                valorFinal <- convertir_unidadis(valor, unidadEntrada, 6, unidadis);
                            FinSi
                            valorFinal <- valorFinal / unidadcon[unidadSalida - 7]
                            
                        Sino
                            Si (unidadEntrada >= 8 Y unidadEntrada <= 11) Y (unidadSalida >= 1 Y unidadSalida <= 7) Entonces
                                valorFinal <- valor * unidadcon[unidadEntrada - 7]
                                
                                Si unidadEntrada = 11 Entonces
                                    unidadEntrada <- 1;
                                Sino
                                    unidadEntrada <- 6;
                                FinSi
                                
                                valorFinal <- convertir_unidadis(valorFinal, unidadEntrada, unidadSalida, unidadis)
                            FinSi
                        FinSi
                    FinSi
                FinSi
                
                mostrar_resultado(valor, valorFinal, sufijo1, sufijo2)
                
                Escribir ""
                Escribir "1|ir al menu"
                Escribir "2|Salir"
				op <- validar_entrada("seleccione una de las siguientes opciones: ", 1, 2, 1)
                
                Si op = 2 Entonces
                    Escribir ""
                    Escribir "Programa finalizado"
                    salir_programa <- Verdadero
                FinSi
            FinSi
        FinSi
    Hasta Que salir_programa
FinAlgoritmo