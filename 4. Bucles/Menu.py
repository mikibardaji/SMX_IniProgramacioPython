# Mostrar un menu con 3 opciones tipo
# 1 .- Opcion 1
# 2.- Opcion 2
# 3.- Opcion 3
# Que opcion quieres
# Mientras no pongas ninguna opcion correcta se vuelve a pintar el menu
# Cuando aprietes una sales del menu e imprimes que opcion has apretado

opcio = -1

while (opcio!=3 and opcio !=2 and opcio!=1):
    print("1.- Jugar" 
    "      2.- Cambiar" \
    "      3.- Salir")
    opcio = int(input("Que opcion quieres? "))
    if (opcio==1):
        print("Jugando a fifa")
    elif (opcio==2):
        print("Cambiando equipo...")
    elif (opcio==3):
        print("Saliendo juego...")
    else:
        print("Opcion no valida")

print("Salida")