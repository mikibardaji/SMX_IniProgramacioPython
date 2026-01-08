#Fes un programa en Python que mostri per pantalla un missatge de benvinguda a la programació.
#El text ha d’incloure el teu nom utilitzant una variable.

#Declara una variable amb el preu d’un producte i una altra amb el percentatge d’IVA (21%).
#Calcula el preu final aplicant l’IVA i mostra’l per pantalla.

#📌 Només operadors matemàtics i variables.

#Declara una variable amb una quantitat de segons.
#Calcula quants minuts sencers i segons sobrants representa aquesta quantitat i mostra el resultat.

#Ejercicio 1
print ("Porfavor introduce tu nombre")
Nombre = input ()
print ("Hola!", Nombre,  "Bienvenido a la programacion!")
#Ejercicio 3
Precio = 10  # Precio sin IVA
IVA = 0.21    # 21%
PRECIO_FINAL = Precio * (1 + IVA)
print ("Precio final del producto:", PRECIO_FINAL)
#Ejercicio 4
segundos = 125
minutos = segundos // 60
segundos_restantes = segundos % 60
print (minutos, "minutos y",segundos_restantes, "segundos restantes")