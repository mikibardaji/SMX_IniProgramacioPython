# Sistema de seguretat d'un ascensor (Pes màxim 400kg)
PESO_LIMITE = 400
pesoPersona = -1
sumaPersonas = 0
excesoPeso = False 
# VARIABLE FLAG
print("Introdueix el pes dels passatgers que van pujant:")

while excesoPeso == False and pesoPersona != 0 : 
    pesoPersona = float(input("Pes del passatger (0 per acabar): ")) 
#    if pes_passatger == 0: 
#        break  con esto sale del bucle pero es lo mismo que pesoPersona != 0
    sumaPersonas += pesoPersona 
    if sumaPersonas > PESO_LIMITE: 
        alarma_encesa = True # El flag canvia d'estat
if excesoPeso==True:  # if excesoPeso es lo mismo porque es un booleano 
    print(f"ALARMA! Pes màxim superat ({sumaPersonas}kg). L'ascensor no es mourà.")
else: print(f"Pes correcte ({pes_total}kg). Tancant portes.")