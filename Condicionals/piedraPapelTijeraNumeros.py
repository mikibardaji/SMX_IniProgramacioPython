"""
Fes un programa que jugui a pedra-paper-tisora. 
Primer t’ha de demanar a tu que vols. 
Llavors amb un random de 3 opcions la màquina triarà 
lo seu i hauràs de dir si has guanyat/perdut/empatat. 
El random sera un numeric de 3 numeros, 
cada número és correspondrà amb una de les opcions del joc.
"""
import random
piedra = 2
tijeras = 1
papel = 0
jugador = int(input("Papel(0),tijeras(1) o piedra(2)"))
maquina = random.randint(0,2)
if maquina == 1:
    maquinaS = "Piedra"
if maquina == 2:
    maquinaS = "Papel"
if maquina == 3:
    maquinaS = "Tijeras"
print(f"La maquina ha elegido {maquinaS}")
if maquina == piedra and jugador == papel:
    print("Has ganado:)")

elif maquina == papel and jugador == tijeras:
    print("Has ganado:)")

elif maquina == tijeras and jugador == piedra:
    print("Has ganado:)")

elif maquina == jugador:
    print("Empate:|")

else: 
    print("Peldiste :(")