"""
Fes un programa que jugui a pedra-paper-tisora. 
Primer t’ha de demanar a tu que vols. 
Llavors amb un random de 3 opcions la màquina triarà 
lo seu i hauràs de dir si has guanyat/perdut/empatat. 
El random sera un numeric de 3 numeros, 
cada número és correspondrà amb una de les opcions del joc.
"""
import random

jugador = input("Papel,tijeras(1) o piedra(2)")
mylista = ["Papel","Tijeras","Piedra"]
maquina = random.choice(mylista)

print(f"La maquina ha elegido {maquinaS}")
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