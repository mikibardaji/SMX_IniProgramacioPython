print("Hello World")
print("Introducció a Python")
print("Aquest és el meu primer programa amb python")
print("Espero aprobar el mòdul")
# Declaro variables
nom = "Miquel Angel"
edat = 51
# Com imprimir variables de sortida
print("El teu nom ", nom)
print("La teva edad es " , edat)
print(f"{nom} , tu edad es {edat}") #edat val 51
# Treballar
edat = 52
print(f"{nom} , tu edad es {edat}") #edat ha canviat a 52
edat = edat + 10
print(f"{nom} , tu edad es {edat}") #edat ha canviat a 52
# restarli algo
edat = edat - 8
print(f"La variable edat ara val {edat}")
# dividirla per un numero
# Nomenclatura CamelCase
edadDivision = edat / 2
print(f"La variable edadDivision ara val {edadDivision} i la variable edad vale {edat}")
# multiplicarla per un numero
edadMultiplicacion = edadDivision * 5
print(f"despues de multiplicar vale {edadMultiplicacion}")
# La opcion correcta era hacer todas las operaciones sobre la misma variable
edat = edat / 2
print(f"La variable edat ara val {edat}")
edat = edat * 5
print(f"La variable edat ara val {edat}")