def funcioSaluda():
    print("Hola com estas soc una funció")
    print("Acabo aquí")

def funcioHola(nom):
    print(f" Hola {nom}, que tal estas? ")
    nom = "Pepe"
    print(f" Hola {nom}, que tal estas? ")

def funcionAnyNacimento(edad):
    anyNacimiento = 2026 - edad
    return anyNacimiento    


print("Hola soc el programa principal")
print("Vaig a cridar a la funció")
funcioSaluda()
print("torno a ser el programa principal")
#funcioSaluda()
#funcioSaluda()
#funcioSaluda()
name = "Miquel Angel"
funcioHola(name)
print(f"programa principal: Hola {name}, que tal estas? ")

#name = "Eric"
#funcioHola(name)
#funcioHola("Jordi")
#funcioHola(1)

edad = int(input("Quants anys tens?"))
anyNaixement = funcionAnyNacimento(edad)
print(f" Naciste el año {anyNaixement}")