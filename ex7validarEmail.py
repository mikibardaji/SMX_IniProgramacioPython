"""
Escriu un programa que validi si pots entrar o no a una xarxa del proven amb el teu correu electrònic.
Ha de validar això:

-Si el correu electrònic acaba amb @proven.cat i te una longitud de almenys 15 caracters amb total es valid.
-Si acaba amb qualsevol correu electrònic, que no sigui aquesta terminació no ha de ser valid, però important han d’haver fica’t una terminació d’email, o sigui hi te que existir una @.
-Si no existeix una @, vol dir que sol t’han posat la part de davant del correu electrònic, has de comprovar en aquest cas que almenys té 5 caracters i un cop sigui valid has de mostrar 
   el teu email és xxxxx@proven.cat (on li haurà concatenat la terminació del correu electrònic)
Un cop passat el correu electrònic en aquest cas t’ha de proposar un password, que es construira reemplaçant la lletra a per el caracter 1(no el numero), la lletra e pel caràcter 2, i així amb totes les vocals...
"""


email = input("Introdueix el teu:")

if "@" in email:
    if email.endswith("@proven.cat") and len(email) >= 15:
        print("email ok")
    else:
        print("Correu no valid debe tener 15 caracteres")
else: #no has escrito la @
    if (len(email)<5):
        print("Correu no valid ha de tenir 5 caracters o més")
    else:
        correuComplet = email + "@proven.cat"
        password = email
        password = password.replace("a","1").replace("A","1")
        password = password.replace("e","2").replace("E","2")
        print(f"El teu correu es {correuComplet} i el password proposat es {password}")

