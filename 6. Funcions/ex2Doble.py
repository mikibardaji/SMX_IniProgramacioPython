def doble(numero):
    operacion = numero*2
    return operacion

#Programa principal
num = int(input("que numero quieres que te diga su doble: "))
numDoblado = doble(num)
print(f"El doble de {num} es {numDoblado}")