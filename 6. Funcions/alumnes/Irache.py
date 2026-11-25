def clasificacionJugadorMuertos(Muertes):
    if 0 >= Muertes and Muertes <= 3:
        print("u are a looser")
    elif 4 >= Muertes and Muertes <= 16:
        print("Punteria de tirachinas")
    elif 17 >= Muertes and Muertes <= 35:
        print("Mas pro que el CJ")
    else:  
        print("Se nota el HESOYAM")