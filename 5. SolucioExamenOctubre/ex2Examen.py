import random

print("--- Generador de Claus Temporals SMX ---")

# Generar 4 números aleatoris
num1 = random.randint(97, 122)
num2 = random.randint(97, 122)
num3 = random.randint(97, 122)
num4 = random.randint(97, 122)

# Convertir cada número al seu caràcter 
lletra1 = chr(num1)
lletra2 = chr(num2)
lletra3 = chr(num3)
lletra4 = chr(num4)

# Concatenar 
password = lletra1 + lletra2 + lletra3 + lletra4

# Mostrar 
print(f"La contrasenya de 4 lletres generada és: {password}")