def clasificacionJugadorMuertos(muertos):
    if muertos < 0 or muertos > 100:
        print("Error: el valor introducido está fuera de los límites permitidos (0-100).")
    elif 0 <= muertos <= 3:
        print("Rango: Civil. Mantienes un perfil bajo en las calles de Los Santos.")
    elif 4 <= muertos <= 16:
        print("Rango: Asociado. Empiezas a ganar notoriedad entre las bandas locales.")
    elif 17 <= muertos <= 35:
        print("Rango: Profesional. Operas con eficacia y las autoridades ya siguen tu rastro.")
    else:
        print("Rango: Jefe criminal. Controlas la ciudad con el nivel máximo de reputación.")