'''
A l’assignatura de Xarxes heu après quins valors 
pot prendre un codi de xarxa, feu un programa que demani els 4 codis d¡una adreça ip aaaa.bbbb.cccc.xxxx, per cadascun que falli ha de mostrar que hi ha un error i avisar-lo de quins valors son possibles. I sol en el cas que tots els valors siguin correctes, ha d’escriure Adreça Correcta. Fixeu-vos que quant és incorrecta, no ha de sortir Adreça Correcta i si és correcta, sí

'''

correcto = True
aaaa = int(input("introduce el bloque aaaa: "))
bbbb = int(input("introduce el bloque bbbb: "))
cccc = int(input("introduce el bloque cccc: "))
dddd = int(input("introduce el bloque dddd: "))

if (aaaa<0 or aaaa>256):
    print("error en el bloque a")
    correcto = False
if (bbbb<0 or bbbb>256):
    print("error en el bloque b")
    correcto = False
if (cccc<0 or cccc>256):
    print("error en el bloque c")
    correcto = False

if (correcto==True):
    print(f"Ip correcte {aaaa}.{bbbb}.{cccc}.{dddd}")
