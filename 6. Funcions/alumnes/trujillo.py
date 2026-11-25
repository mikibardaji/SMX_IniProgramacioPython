def clasificacionJugadorMuertos(morts):
    # Control de valors fora dels límits (0 a 100)
    if morts < 0 or morts > 100:
        print("Ep! Aquest número no surt al mapa de Los Santos. Revisa les dades de la missió.")
        return
    
    # Classificació segons els rangs
    if 0 <= morts <= 3:
        print("Ets un looser. T'han abatut abans de trobar una pistola.")
    elif 4 <= morts <= 16:
        print("La meva àvia fa més morts que tu conduint per Vinewood.")
    elif 17 <= morts <= 35:
        print("Vas fent camí, esquivant la policia com bonament pots.")
    elif 36 <= morts <= 100:
        print("Un autèntic criminal de llegenda per les carrers de Los Santos!")