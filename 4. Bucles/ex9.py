"""
8. Adivinar numero. 
Farem un programa on el ordinador pensi inicalment un numero del 1 al 100 
(un random), i despres demani al usuari que adivini el numero... Si no l'encerta ha d'anar donant pistes dient si es mes gran o més petit. El programa continua fins que el usuari acerta el numero. Per fer proves, quant el ordinador pensi el numero , feu que el mostri per pantalla i aixi veureu si funciona correctament. Quant ja estigui provat, aquest xivato ho treieu.
Crear un random del 1 al 100 (y guardarlo en variable)
Preguntar el valor que crees tu? (guardarlo en otra variable)
Si el numero del jugador es mayor que el de la maquina (“Ordenador: Mi numero es mas pequeño”)
Si el numero del jugador es menor qu el de la maquina (“ccfdcffd”)
si son iguales mostrar acertaste
mientras no sean iguales volver al paso 2
"""
import random
NUMERO_INTENTOS = 10
intento = 1
numero_secreto = random.randint(1,100)
numero_jugador = int(input("Introduce tu numero: "))

while numero_jugador != numero_secreto and intento < NUMERO_INTENTOS:
    if numero_secreto < numero_jugador:
        print("El numero que has puesto es mas grande")
    else:
        print("El numero que has puesto es mas pequeño")
    vidas = NUMERO_INTENTOS - intento
    print(f"Te quedan {vidas} intentos...")
    numero_jugador = int(input("Introduce otro numero: "))
    intento += 1

if numero_jugador == numero_secreto:    
 print("Has ganado")
 print(f"Has intentado {intento} veces") 

else:
 print ("La maquina ha ganado, te has quedado sin intentos")
 print(F"el numero de la maquina era {numero_secreto}")