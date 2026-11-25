def clasificacionJugadorMuertos(morts):

    if morts < 0 or morts > 100:
        print("Error 404: aquest valor no existeix a Vice City. Escriu un número entre 0 i 100.")
    elif morts <= 3:
        print("WASTED! Ets un looser")
    elif morts <= 16:
        print("La meva àvia fa més morts que tú")
    elif morts >= 17 and morts < 50:
        print("Ja tens 2 estrelles! Els polis comencen a fixar-se en tu")
    elif morts >= 50 and morts < 75:
        print("Ja tens 3 estrelles! Ets un criminal ja reconegut a Vice City")
    elif morts >= 75 and morts < 100:
        print("Ja tens 4 estrelles! Estàs a la llista de més buscats de Vice City")
    else:
        print("MISSION PASSED! Respect+ Ets el rei de Vice City!")
