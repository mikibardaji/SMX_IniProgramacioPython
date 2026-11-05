# Sol·licitar el codi d'inventari a l'usuari
codi = input("Introduir codi de l'inventari: ")

# Validar que almenys tingui 12 posicions
if len(codi) >= 12:
    
    tipus_equip = codi[0:3]    # Els 3 primers 
    any_compra = codi[4:8]     # Els 4 caràcters de l'any
    ciutat = codi[9:12]        # Els 3 últims 
    
    # Crear el codi invertit combinant les variables
    codi_invertit = f"{ciutat}-{tipus_equip}-{any_compra}"
    
    # Mostrar els resultats
    print(f"Tipus d'equip: {tipus_equip}")
    print(f"Any de compra: {any_compra}")
    print(f"Codi invertit: {codi_invertit}")
else:
    print("Error: El codi introduït és massa curt o incorrecte.")