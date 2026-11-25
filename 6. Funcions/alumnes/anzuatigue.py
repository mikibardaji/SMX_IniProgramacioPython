def clasificacionJugadorMuertos(muertes):

    if muertes < 0 or muertes > 100:
        print("Este numero no es valido!")

    elif muertes >= 0 and muertes <= 3:
        print("Eres el mas malo de Los Santos")

    elif muertes >= 4 and muertes <= 16:
        print("Mi prima hace mas muertos que tu")

    elif muertes >= 17 and muertes <= 35:
        print("Ja comienzas a ser peligroso por las calles")

    elif muertes >= 36 and muertes <= 100:
        print("Eres una leyenda de Los Santos!")

