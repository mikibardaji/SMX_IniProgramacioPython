# Els bucles ens serveixen per repetir una o mes vegades
# algunes linees de codi... 

"""x = 1

while x <= 10:
    if x != 5:
        print(x)
    else:
        continue
    x += 1 # x = x + 1"""
"""
numero=0 # numero inventat pero que cumpla la condicion bucle
#demanara numeros fins que fiquin -1 O -2
while (numero!=-1 and numero!=-2):
    numero = int(input("Posa un numero: "))
    print(f"Has ficar el numero .... {numero}")
print("El programa ha acabat.... ")
"""
"""
# Instruccion for
#   variable numero range(valorInicial, valorfinalno inclos)
for numero in range(1,20):
    print(numero)

print("For aumentado de 2 en 2")
for valor in range(50,1,-1):
    print(valor)
"""
manocartas = ["As","J","Q","K"]
jugada = ["As","As","J","Q","As"]
print("Mis cartas")
contAs=0
contJ=0
contK=0
for carta in jugada:
    if (carta == "As"):
        contAs +=1
    elif (carta == "J"): 
        contJ +=1
    elif (carta == "K"):  
        contK +=1   
    print(carta)

if contAs==3 or contJ==3 or contK ==3:
    print("Tienes un trio")
if (contAs==3 or contJ==3 or contK ==3) and (contAs==2 or contJ==2 or contK ==2):
    print("Tienes un full ")