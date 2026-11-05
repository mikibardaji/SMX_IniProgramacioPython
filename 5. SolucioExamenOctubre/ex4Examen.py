password = input("Introdueix la teva contrasenya: ")

# Inicialitzar els punts a 0
punts = 0

# Mirar si en te algun pot tenir més d¡un
if "!" in password or "-" in password or "." in password:
    punts += 6

# 2. Comprovar si conté majúscules i minúscules alhora
if password != password.lower() and password != password.upper():
    punts += 3

# 3. si té més de 8 caràcters
longitud = len(password)
if longitud > 8:
    punts += 4

# 4. Sumar +1 punt per cada caràcter
if longitud > 12:
    caracters_extra = longitud - 12
    punts += caracters_extra

# Mostrar els punts totals aconseguits
print(f"Punts aconseguits: {punts}")

# Estructura condicional final per determinar la fortalesa
if punts <= 7:
    print("Canvia-la ja!!!")
elif punts <= 13:
    print("No està malament, però caldria millorar-la")
elif punts <= 16:
    print("Bona")
else:
    print("Tot un hackerman")