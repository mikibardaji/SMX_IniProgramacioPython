'''
A la base de dades de la S.H.I.E.L.D. (o de la Lliga de la Justícia), rebrem informació sobre diferents individus amb superpoders. Per poder catalogar-los correctament i saber quins protocols de seguretat activar, hem de crear un programa en Java que utilitzi estructures condicionals niades 
Pregunta inicial: Té un origen humà o terrestre? (esHuma)
SÍ (Origen Humà): Comprova si ha nascut amb poders de forma natural (teGenMutant).
SÍ: El resultat és un MUTANT (Exemple: Lobezno / X-Men).
NO: Comprova si ha patit un accident o experiment de laboratori (experimentat).
SÍ: El resultat és un HUMÀ MUTAT (Exemple: Spiderman o Els 4 Fantàstics).
NO: El resultat és un HUMÀ ENTRENAT (Exemple: Batman o Iron Man).
NO (Origen No-Humà): Comprova si és un ésser mitològic o místic (esDivinitat).
SÍ: El resultat és un DÉU / ENTITAT MÍSTICA (Exemple: Thor o Wonder Woman).
NO: Comprova si és un ésser provinent de l'espai exterior (esExtraterrestre).
SÍ: El resultat és un ALIENÍGENA (Exemple: Superman o el Capità Marvel).
NO: Comprova si el seu cos és artificial o programat (esSintetic).
SÍ: El resultat és un SINTÈTIC / ANDROIDE (Exemple: Visión o cíborgs).
NO: El resultat és un ÉSSER MÀGIC / DEMONÍAC (Exemple: Hellboy o Spawn)
'''

esHuma = input("El superheroi es huma?")

if (esHuma=="Si"):
    esMutant =  input("El superheroi es Mutant?")
    if(esMutant=="Si"):
        print("El superheroi es Mutant")
    else:
        experimental =  input("El superheroi ha patit un experiment?")
        if (experimental=="Sí"):
            print ("Huma mutado por experimento")
        else:
            print("Huma entrenado")
else:
    esDivinitat =  input("El superheroi es divi?")
    if (esDivinitat=="Si"):
        print("Es deu")