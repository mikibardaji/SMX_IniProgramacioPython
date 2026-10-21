"""
Fes un programa per gestionar brackets de partits de futbol.
 S’ha de demanar a l’usuari els noms (en ordre) de 4 equips.
   Després, el programa anirà demanant a l’usuari per
     cada partit el resultat del primer equip, 
     i el ordinador fara un random (del 1 al 10) pels gols 
     del segon equip.
Quant és sapigui el guanyador passarà a la final. 
En cas d’empat guanya el primer equip. 
Ho ha de fer fins que hi hagi un guanyador. 
Nota: Si vols que siguin partides d’un altre joc, pots fer-ho, l'únic que tu hauras de sapiguer el limit superior e inferior del random de puntuació, pel joc que escolleixis.
"""
import random

equipo1 = input("introduce equipo1: ")
equipo2 = input("introduce equipo2: ")
equipo3 = input("introduce equipo3: ")
equipo4 = input("introduce equipo4: ")

# PARTIDO 1
goles1 = int(input(f"Goles del {equipo1}"))
goles2 = random.randint(1,10)
print(f"equipo2 ha marcado {goles2}")

if goles1 >= goles2:
    semifinales1 = equipo1
else:
    semifinales1 = equipo2
   
print(f"el ganador de la semifinal1 {semifinales1} ")

# PARTIDO 2
goles3 = int(input(f"Goles del {equipo3}"))
goles4 = random.randint(1,10)
print(f"equipo2 ha marcado {goles4}")

if goles3 >= goles4:
    semifinales2 = equipo3
else:
    semifinales2 = equipo4
   
print(f"el ganador de la semifinal2 {semifinales2} ")


# FINAL
golesf1 = random.randint(1,10)
golesf2 = random.randint(1,10)
print(f"{semifinales1} ha marcado {golesf1}")
print(f"{semifinales2} ha marcado {golesf2}")

if golesf1 >= golesf2:
    ganador = semifinales1
else:
    ganador = semifinales2

print(f"Campeón: {ganador}")