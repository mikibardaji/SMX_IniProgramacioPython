"""
 El tallafocs del servidor de joc
Un servidor de videojocs rep connexions de jugadors de tot el món. Per evitar atacs, el sistema ha de comprovar si l'adreça IP del jugador que es vol connectar coincideix exactament amb la IP d'un bot maliciós = “192.168.1.30” registrat a la base de dades.
Dades a utilitzar: Una variable de text per a la IP del jugador i una altra per a la IP del bot.
Objectiu: Mostra el missatge "Connexió bloquejada" si les dues adreces IP són iguals. En cas contrari, mostra "Connexió permesa".

"""
#dip bot registrado
ipBot = "192.168.1.30"
ipJugador = input("Pon l'adreça ip? ")
if (ipJugador==ipBot):
    print("IpBloquejada")
else:
    print("Puedes acceder")