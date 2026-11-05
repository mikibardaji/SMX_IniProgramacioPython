"""
Fes un programa que calculi quant medeix la teva casa
A cada volta t'ha de preguntar quant medeix la habitació
Despres preguntar si tens mes habitacions (SI/NO)
Si dius que si, ha de tornar al pas 1 i tornar a preguntar i seguir acumulant els metres
Si dius que no, surt.
Al sortir ha de dir quantes habitacions tens, 
i quant medeix la teva casa
"""
respuesta=""
contHabitaciones=0
metrosAcumHabitacion=0
metrosHabitacionSola=0

while (respuesta!="NO"):
    metrosHabitacionSola = int(input("Cuanto mide tu habitacion? "))
    contHabitaciones += 1
    metrosAcumHabitacion = metrosAcumHabitacion + metrosHabitacionSola
    print(f" Por ahora llevas acumulado {metrosAcumHabitacion} metros")
    print(f"Tu habitacion mide {metrosHabitacionSola}")
    respuesta = input("Tienes mas habitaciones(SI/NO)? ").upper()

print(f" Tienes {contHabitaciones} habitaciones y tu casa mide {metrosAcumHabitacion}")