def clasificacionJugadorMuertos():
    muertos = int(input("Introduce a cuantos has matado en el GTA VI (Del 0 al 100): "))
    if muertos >=0 and muertos <=3:
        print("Te voy a regalar unas manos")
    elif muertos >=4 and muertos <=16:
        print("Hasta mi abuela hace eso")
    elif muertos >=17 and muertos <=35:
        print("Venga va, cada vez estás más lejos")
    elif muertos >=36 and muertos <=66:
        print("Bueno, ya te queda más o menos la mitad")
    elif muertos >=67 and muertos <=100:
        print("Tú si que sabes")
    else:
        print("Tienes que poner un valor entre 0 y 100, aprende a leer")