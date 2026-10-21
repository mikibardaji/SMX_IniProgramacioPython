'''
Comprovació d'espai al disc dur (SSD)
Abans de començar la descàrrega automàtica d'un nou videojoc o d'una actualització del sistema, la consola ha de verificar si hi ha prou emmagatzematge disponible a la unitat de disc.
Dades a utilitzar: Una variable decimal per a l'espai lliure actual al disc (en GB) i una altra variable decimal per a la mida total que ocupa el videojoc (en GB).
Objectiu: 
Compara els valors. Si l'espai lliure és major o igual que la mida del joc, mostra el missatge "Espai suficient. Començant descàrrega..." I te que mostrar quin percentatge del disc ocupara, això és calcula dividint el pes del joc entre el pes del disc i multiplicant-ho per 100. 
Si el joc és més gran que l'espai disponible, mostra "Error: Falta espai al disc".
'''


espacioLibre = float(input("Espacio libre al disco: "))
medidaJuego = float(input("Mida del juego: "))
if (espacioLibre>=medidaJuego):
    porcentaje = (medidaJuego/espacioLibre)*100
    print(f"Espacio suficiente, el juego ocupa {porcentaje} %")
else:
    print("ERROR FALTA ESPACIO EN DISCO")