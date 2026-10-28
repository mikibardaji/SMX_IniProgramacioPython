"""
Fes el mateix programa per llistar els ports parells 
de l'1 al 100 de la partida multijugador, però aquesta 
vegada el bucle ha d'avançar d'1 en 1. 
Però aquest cop els ports del 50 al 60 estan ocupats i 
no s'han de mostrar i el port 74 tampoc...

"""

for puerto in range(1, 101):
    if 50 <= puerto <= 60 or puerto == 74:
        continue
    if puerto  % 2  == 0:
     print(f"{puerto} correcto")
