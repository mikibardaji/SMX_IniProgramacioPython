# Demanem el codi de la mostra a l'usuari
codi = input("Introdueix el codi de la mostra biològica: ")

# Extraiem el tipus de microbi (els 3 primers caràcters)
tipus_microbi = codi[0:3]

# Extraiem l'any de recollida (caràcters de la posició 4 a la 7, recordant que el guió és la posició 3)
# En el patró BAC-2026..., el '2' és la posició 4 i el '6' és la 7. En Python s'indica [4:8] perquè l'últim no s'inclou.
any_recollida = codi[4:8]

# Extraiem el codi del cultiu (les 4 últimes posicions utilitzant índexs negatius)
codi_cultiu = codi[-4:]

# Mostrem els resultats per pantalla
print("\n--- DADES EXTRAIDES ---")
print("Tipus de microbi:", tipus_microbi)
print("Any de recollida:", any_recollida)
print("Codi del cultiu:", codi_cultiu)