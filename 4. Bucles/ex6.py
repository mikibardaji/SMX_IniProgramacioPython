"""
El programa ha de demanar números contínuament 
fins que s'introdueixi un 0 (que significa "Fi de la partida"). 
En acabar, el programa ha de mostrar si s'ha pSilgon número negatiu), 
quants números eren positius (curacions) i quants negatius (atacs rebuts). 
"""

positiu=0
negatiu = 0
print("Introduce registros de la partida... (0 para acabar) ")
numero = float(input("Introduce valor de vida: "))
while numero != 0:
    if (numero>0):
        positiu +=1
    elif (numero < 0):
        negatiu += 1
    numero = float(input("Introduce valor de vida: "))    
print("Log de partida")
print(f"tienes {positiu} curaciones")
print(f"tienes {negatiu} daños")
if (negatiu>0):
    print("HAS RECIBIDO ALGUN DAÑO")
else:
    print("NO HA HABIDO ATAQUES")