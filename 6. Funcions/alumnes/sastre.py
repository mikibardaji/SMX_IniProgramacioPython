# apellido.py
def clasificacionJugadorMuertos(muertos):
    if muertos < 0:
        print("Muertes negativas jajajajaj .")
    elif muertos > 100:
        print("Más de 100 muertes? Pero calmate.")
    elif muertos <= 5:
        print("Das bastante pena,te falta calle.")
    elif muertos <= 20:
        print("Imagino que estarás empezando chico.")
    elif muertos <= 50:
        print("A la poli no le caes bien.")
    else:
        print("Eres el rey de Vice City cinco estrellas de búsqueda y tan chill.")