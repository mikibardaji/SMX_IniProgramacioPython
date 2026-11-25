def clasificacionJugadorMuertos(muertos: int):
    if muertos < 0 or muertos > 100:
        print("Error: El número de muertos debe estar entre 0 y 100.")
    elif muertos <= 3:
        print("Ets un looser")
    elif muertos <= 16:
        print("La meva avia fa més morts que tú")
    elif muertos <= 35:
        print("Io que sigui")
    else:
        print("Lo que sigui")