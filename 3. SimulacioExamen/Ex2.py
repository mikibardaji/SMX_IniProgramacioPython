# Demanem les emissions de CO2 a l'usuari i les passem a tipus decimal (float)
emissions = float(input("Introdueix el nivell d'emissions de CO2 (g/km): "))

# Comprovem la primera regla: entre 0 i 50 (ambdós inclosos)
if emissions >= 0 and emissions <= 50:
    print("Etiqueta: Eco-Premium (Elèctric/Híbrid Recomanat)")

# Comprovem la segona regla: entre 50 i 200 (sense incloure cap dels dos)
elif emissions > 50 and emissions < 200:
    print("Etiqueta: Eficient (Diesel/Benzina indexat)")

# Comprovem la tercera regla: exactament 200
elif emissions == 200:
    print("Etiqueta: Alta Contaminació (Restringit)")

# Per a qualsevol altre valor (per exemple, valors negatius o superiors a 200)
else:
    print("Etiqueta: Revaluació requerida / Altres mètodes")
