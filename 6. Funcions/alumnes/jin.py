def clasificacionJugadorMuertos(muertos):
    """Imprime por pantalla una frase estilo GTA según las muertes de la partida.
    No devuelve ningún valor."""
    if not isinstance(muertos, int) or isinstance(muertos, bool):
        print("Eso no es un número entero, colega. ¿Te has dado un golpe con el coche?")
    elif muertos < 0 or muertos > 100:
        print("Eh, eso no cuadra: las muertes tienen que estar entre 0 y 100. Revisa el marcador.")
    elif muertos <= 3:
        print("WASTED: ni la policía de Vice City te toma en serio. Eres un looser.")
    elif muertos <= 16:
        print("Mi abuela hace más muertes que tú... y ella solo atropella con el andador.")
    elif muertos <= 35:
        print("Ya empiezas a tener estrella de búsqueda. Los vecinos de Los Santos cierran las ventanas.")
    else:
        print("Nivel Los Santos: cinco estrellas, helicópteros y el ejército detrás de ti. ¡Leyenda!")
