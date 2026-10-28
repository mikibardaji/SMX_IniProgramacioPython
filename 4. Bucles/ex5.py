"""
El tallafocs (firewall) d'un servidor de Discord o de jocs en 
línia analitza 10 intents de connexió (valors no nuls). 
Els valors positius són accessos permesos i els negatius 
són intents de hackeig bloquejats. 
Fes un programa que llegeixi aquests 10 números 
i mostri el total de positius i el total de negatius detectats.
"""

negatius = 0
positius = 0

for registres in range(5):
    valor = int(input(f"Introdueix un valor {registres +1}: "))
    if valor > 0:
        positius += 1
    elif valor<0:
        negatius += 1
    # 0 no fa falta contar-lo
print(f"Accesos permesos: {positius}")
print(f"Accesos bloquejats: {negatius}")