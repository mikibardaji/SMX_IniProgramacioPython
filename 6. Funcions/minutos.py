import math


# declarar una función segundosAMinutos que reciba un entero que seran segudons y me retorne (return)
# me retorne cuantos minutos son. 
def segundosAMinutos (segundos): # Si la función hace calculos el 90% no tendra print
    minutos = math.floor(segundos/60)          # Si tendra return
    return minutos 



# pedir segundos
# llamar a la funcion y recoger el resultado
# mostrar el resultado
seg = int(input("Introduce los segundos que has tardado en atropellar alguien en GTA VI? "))
minutos = segundosAMinutos(seg)
print(f" Has tardado en matar a alguien {minutos} minutos y {seg -(minutos*60)} segundos")
