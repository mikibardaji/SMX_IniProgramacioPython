def clasificacionJugadorMuertos(muertos):
  if 0 <= muertos <= 3:
    print("Eres un flojo")
  elif 4 <= muertos <= 16:
    print("Mi abuela hace más bajas que tú")
  elif 17 <= muertos <= 35:
    print("Vas sobreviviendo como puedes")
  elif 36 <= muertos <= 100:
    print("Eres una leyenda absoluta de la calle")
  else:
    print("Número de enemigos fuera del rango permitido (0-100)")