"""
El radar de velocitat de la ronda
Un radar de velocitat registra el pas de 15 vehicles en un tram limitat a 80 km/h. 
Crea un programa que demani la velocitat de cadascun d'aquests vehicles. En finalitzar, el programa ha de mostrar quants anaven a una velocitat correcta (80 km/h o menys) 
i quants anaven com a mínim amb excés de velocitat (més de 80 km/h).
"""

numVehiculos=1
velocidad = -1
correcto = 0
exceso = 0

while numVehiculos<=4: # cuando sabemos el numero es finito es un for mejor
  velocidad = int(input(f"A que velocidad va el coche {numVehiculos}: ")) 
  if velocidad>80:
    exceso += 1
  else:
    correcto += 1 # correcto +=1
  numVehiculos += 1

#Mpstrar resultado
print(f" numero de vehiculos             {numVehiculos}")
print(f" numero de multas                {exceso}")
print(f" numero de vehiculos correctos:  {correcto}")