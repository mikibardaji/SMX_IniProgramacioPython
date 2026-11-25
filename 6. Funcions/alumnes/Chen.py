def JugadorMuertos(morts):
    if 0 <= morts <= 3:
        print("Ets un looser")
    elif 4 <= morts <= 16:
        print("La meva avia fa més morts que tú")
    elif 17 <= morts <= 35:
        print("Vas agafant ritme pels carrers de Los Santos, no està malament")
    elif 36 <= morts <= 100:
        print("Ets una llegenda viva del crim organitzat, la policia ja et té por")
    else:
        print("Número fora de rang! Només s'accepten valors entre 0 i 100.")