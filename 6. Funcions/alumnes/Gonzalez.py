def clasificacionJugadorMuertos(muerto):
    if muerto>=0 and muerto<=3:
        print ("Ets un looser")
    elif muerto<=16 and muerto>=4:
        print ("La meva avia fa més morts que tú")
    elif muerto>=17 and muerto<=35:
        print ("Asesino")
    elif muerto>=36 and muerto<=100:       
        print ("Criminal extremadamente buscado")
    else:
        print ("Fuera de limites") 
#Muertes=int(input("A cuantos has matado"))
#clasificacionJugadorMuertos(Muertes)