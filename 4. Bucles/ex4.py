"""
Un sistema de telemetria analitza el rendiment d'un videojoc 
i llegeix 10 registres de canvis de fotogrames (FPS)
 o de vida del jugador (valors no nuls). 
 Fes un programa que demani aquests 10 números i finalment mostri un missatge indicant si s'ha detectat algun valor negatiu (que indicaria un error crític o una pèrdua de vida) o si tot ha estat correcte.
"""

algunNegatiu = False
#hayNegativo = 0;
for veces in range(1,11):
   valor = int(input(f"Pon un valor {veces} de vidas si es negativo sera un error "))
   if valor<0 :
     algunNegatiu = True # no imprimo nada!!!!!
     #hayNegativo = 1
#fuera del for al terminar las 10 veces
#if (algunNegatiu==True):
if (algunNegatiu):
   print("Has puesto algun negativo")  
else:
   print("No has puesto ningun negativo")
    