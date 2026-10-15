frase = input("Introdueix una frase:")
lletra = input("Introdueix una lletra: ")

print("conte la lletra ", lletra in frase);

# find() devuelve la posición  de la frase buscada y -1 si no existe
encontrado = frase.find(lletra)
if (encontrado!=-1):
    print("esta la letra buscada y esta en la posición: " , encontrado)
else:
    print(f"No esta la letra buscada {lletra}")

# count, cuenta cuantas veces, esta esa letra
# por tanto si sale 0 es que no esta

numeroVeces = frase.count(lletra)
print(f"La {lletra} sale {numeroVeces} veces.")