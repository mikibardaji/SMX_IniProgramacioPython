"""
Fes un programa que jugui a pedra-paper-tisora. 
Primer t’ha de demanar a tu que vols. 
Llavors amb un random de 3 opcions la màquina triarà 
lo seu i hauràs de dir si has guanyat/perdut/empatat. 
El random sera un numeric de 3 numeros, 
cada número és correspondrà amb una de les opcions del joc.
"""
import random
jugador = input("Papel,tijeras o piedra")
maquina = random.randint(1,3)
if maquina == 1:
    maquina = "Piedra"
if maquina == 2:
    maquina = "Papel"
if maquina == 3:
    maquina = "Tijeras"
print(f"La maquina ha elegido {maquina}")
if maquina == "Piedra" and jugador == "Papel":
    print("Has ganado:)")

elif maquina == "Papel" and jugador == "Tijeras":
    print("Has ganado:)")

elif maquina == "Tijeras" and jugador == "Piedra":
    print("Has ganado:)")

elif maquina == jugador:
    print("Empate:|")

else: 
    print("Peldiste :(")