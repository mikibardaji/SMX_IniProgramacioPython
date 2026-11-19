"""El llançament de la moneda
Fes un programa que simuli el llançament d’una moneda. 
El programa llançarà 20 vegades la moneda i mostrarà per pantalla una ‘C’ per a cara i un ‘+’ per a creu. 
El programa haurà de comptar el número de cares i el número de creus. 
Al finalitzar, haurà de mostrar el número total de tirades que ha fet i quantes cares i creus han sortit.
"""

import random
cara = 0
cruz = 0
moneda = ""
lanzamientos = 0

for lanzamientos in range(1,21):
    moneda = random.choice(["Cara","Creu"])
    print(f"{moneda}")
    if (moneda=="Cara"):
        cara += 1
    else:
        cruz += 1
    #aumentar lanzamientos 

print(f" Lanzamientos:   {lanzamientos}")
print(f" Ha salido cara: {cara}")
print(f" Ha salido cruz: {cruz}")