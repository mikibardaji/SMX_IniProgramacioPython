'''
Al menú de la botiga del joc, un usuari pot introduir dos codis promocionals de text per aconseguir monedes virtuals gratuïtes. Un dona 1000 monedes i un de 500 monedes. El sistema ha de verificar que el text escrit coincideixi de manera exacta (recorda que les majúscules i minúscules compten).
Dades a utilitzar: Una variable de text amb el codi que ha escrit el jugador. Els codis amb els dos cupons han d’estar definits al programa i sempre son els mateixos, no els introdueix el comprador.
Objectiu: Escriu la condició que mostri "1000 monedes afegides!" si el text coincideix completament,  "500 monedes afegides!" si el text coincideix amb el segon text, o "Codi invàlid" si hi ha qualsevol diferència.
'''

CODIGO_1000 = "GAMER1000"
CODIGO_500 = "PLAY500"

codigoJugador = input("Introduce tu codigo promocional: ")

if (codigoJugador == CODIGO_1000):
    print ("1000 monedas añadidas")
elif (codigoJugador == CODIGO_500):
    print ("500 monedas añadidas")
else:
    print ("Codigo invalido")