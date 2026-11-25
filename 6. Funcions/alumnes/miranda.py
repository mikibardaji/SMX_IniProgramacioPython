def clasifiacionjugadoresmuertos():
    bajas = int(input("¿Cuántas bajas llevas en GTA VI? Indica un número del 0 al 100: "))
    if 0 <= bajas <= 3:
        print("Necesitas practicar mucho más la puntería")
    elif 4 <= bajas <= 16:
        print("Todavía estás muy verde, sigue intentándolo")
    elif 17 <= bajas <= 35:
        print("Vas mejorando poco a poco, no te rindas")
    elif 36 <= bajas <= 66:
        print("Buen ritmo, ya has superado el ecuador")
    elif 67 <= bajas <= 100:
        print("Nivel experto, dominas el juego por completo")
    else:
        print("Error: el número debe estar comprendido entre 0 y 100")
