def clasificacionJugadorMuertos(morts):
    if morts < 0 or morts > 100:
        print("Error: La quantitat d'eliminacions ha d'estar entre 0 i 100.")
    elif morts <= 3:
        print("Ets un looser")
    elif morts <= 16:
        print("La meva avia fa més morts que tú")
    elif morts <= 35:
        print("Ja comences a dominar els carrers de Vice City, però encara et falta carrer.")
    else:
        print("Nivell cap de la màfia: 5 estrelles de recerca i ni el NOOSE et pot aturar.")