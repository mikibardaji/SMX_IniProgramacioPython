frase = input("Introdueix una frase llarga: ")

pos1 = int(input("Introdueix la primera posició: "))
pos2 = int(input("Introdueix la segona posició: "))

# Retallem la frase entre les dues posicions
frase_retallada = frase[pos1:pos2]

print("La frase retallada és:")
print(frase_retallada)