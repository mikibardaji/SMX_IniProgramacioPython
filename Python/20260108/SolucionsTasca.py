# EXERCICI 1
# Missatge de benvinguda

nom = input("Introdueix el teu nom: ")
print("Benvingut a la programació,", nom)


# EXERCICI 2
# Suma de dos nombres enters 

num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))
suma = num1 + num2
print("La suma dels dos nombres és:", suma)


# EXERCICI 3
# Preu amb IVA (21%)

preu = float(input("Introdueix el preu del producte: "))
iva = 21
preu_final = preu + (preu * iva / 100)
print("El preu final amb IVA és:", preu_final)


# EXERCICI 4
# Conversió  minuts i segons

segons = int(input("Introdueix una quantitat de segons: "))
minuts = segons // 60
segons_restants = segons % 60
print("Minuts:", minuts)
print("Segons restants:", segons_restants)
