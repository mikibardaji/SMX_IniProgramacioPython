import random
# PREMIO_JACKPOT = 5000
PREMIO_JACKPOT = random.randint(5000, 50000000)
numero = int(input("Que numero crees que saldra? "))
numeroMaquina = random.randint(1,3)
print(f"el numero es {numeroMaquina}")

if(numeroMaquina == numero):
    print(f" Has ganado {PREMIO_JACKPOT} €")
else:
    print(f"Has perdido!!!! LOSER!!!!{PREMIO_JACKPOT} €")