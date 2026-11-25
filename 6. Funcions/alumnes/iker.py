def clasificacionJugadorMuertos(muertos):

    if muertos >= 0 and muertos <= 3:
        print("Ets un looser")

    elif muertos >= 4 and muertos <= 16:
        print("La meva avia fa més morts que tú")

    elif muertos >= 17 and muertos <= 35:
        print("No son muchos")

    elif muertos >= 36 and muertos <= 100:
        print("Son muchos")

    else:
        print("Numero invalido ")