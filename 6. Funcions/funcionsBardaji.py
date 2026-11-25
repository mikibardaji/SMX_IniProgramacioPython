def grande(entero1, entero2):
    if (entero1>entero2):
        mayor = entero1
    else:
        mayor = entero2
    return mayor

#Funcion que pide un valor y lo retorna (si es positivo) si no lo es
#se repite hasta que sea positivo (no hace return hasta que no es positivo)
def valorPositivo(frase):
    numeroPositivo = 0
    while(numeroPositivo<=0):
        #numeroPositivo = int(input("Pon un valor positivo: "))
        numeroPositivo = int(input(frase))
    return numeroPositivo