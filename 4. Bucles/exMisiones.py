XP_Obtenidos = 0 # XP de la pantalla
XP_TOTAL = 0 # LA suma de todos
num_missio = 1 # contador de mision

while num_missio <= 4:
    XP_Obtenidos = int(input(f"Pon xp de la mision {num_missio}: "))
    XP_TOTAL += XP_Obtenidos # acumuladora
    num_missio = num_missio + 1 # += num CONTADORA

print(f"Tu experiencia es {XP_TOTAL}")