"""
El sistema de càlcul d'un joc necessita processar 
els multiplicadors i punts d'experiència base 
dels 10 primers nivells d'una masmorra (de l'1 al 10). 
Fes un programa que calculi i mostri per pantalla la 
suma total d'aquests 10 primers números
"""
acumVuelta = 0
for vuelta in range(1,11):
    acumVuelta = acumVuelta + vuelta

print(f"La suma es {acumVuelta}")

"""
Fes un programa que calculi quant medeix la teva casa
A cada volta t'ha de preguntar quant medeix la habitació
Despres preguntar si tens mes habitacions (SI/NO)
Si dius que si, ha de tornar al pas 1 i tornar a preguntar i seguir acumulant els metres
Si dius que no, surt.
Al sortir ha de dir quantes habitacions tens, 
i quant medeix la teva casa
"""