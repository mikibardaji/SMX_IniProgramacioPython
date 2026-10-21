'''
4. Classificador de la qualitat de la connexió (Ping)
Els videojocs competitius mesuren el "ping" (el temps de resposta de la xarxa en mil·lisegons) per indicar als jugadors si tenen una bona experiència de joc o si patiran retards (lag).
Dades a utilitzar: Una variable sencera que guarda el valor del ping actual del jugador.
Objectiu: Crea una estructura condicional que classifiqui el ping:
Si el ping és menor que 50, mostra "Connexió Excel·lent".
Si el ping està entre 50 i 150 (ambdós inclosos), mostra "Connexió Bona".
Si el ping és superior a 150, mostra "Connexió Lenta (Lag)".
'''

ping = float(input("Ingrese el tiempo ping"))
if (ping<0):
    print(f" Valor introducido incorrecto:{ping}")
elif (ping<= 50):
    print(f"Connexió Excel·lent... {ping} ms")
elif (ping<=150):
    print(f"Connexió Bona... {ping} ms") 
else:
    print(f"Connexió Lenta (Lag)... {ping} ms") 
#elif(ping>150):
#else casos erroneos