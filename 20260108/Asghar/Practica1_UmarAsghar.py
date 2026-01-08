#ejercici 1, benvingut
nom = input()
print ("Benvingut a la programació, ", nom)

#ejercici 3, percentatge
preu = input()
iva = 21

#converteix el valor en int
preu = int(preu)

#calcul del iva
final = preu + (preu * iva / 100)
print (final)

#ejercici 4, quantitat de segons
segons = input()

#converteix el valor en int
segons = int(segons)

#torna la part entera dividida
minuts = segons // 60

#ens dona el residu
sobrants = segons % 60

#print
print(minuts, "minut i", sobrants, "segons")
