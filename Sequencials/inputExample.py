#Como recibir datos de entrada en la ejecución
name = input("pon tu nombre ") # Introduccion datos
print(f" Hola {name}, como estas hoy?")
edat = int(input("pon tu edad "))
print(f"Tienes {edat} años")
edat = edat + 1000
print(f"Tienes {edat} años")
dinero = float(input("cuanto dinero tienes en el pantalon? "))
print(f"Tienes {dinero} euros")
dinero = dinero + 500
print(f"Tienes {dinero} euros")
premio = input("cuanto dinero te ha tocado")
print(type(premio))
premio = int(premio)
print(type(premio))
