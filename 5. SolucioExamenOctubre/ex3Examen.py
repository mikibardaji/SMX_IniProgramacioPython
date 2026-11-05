port = int(input("Introdueix el port: "))

# Determinar el trànsit
if port == 80 or port == 443:
    print("Trànsit: Web (HTTP/HTTPS)")
elif port == 22:
    print("Trànsit: Administració Remota (SSH)")
elif port == 53:
    print("Trànsit: Resolució de Noms (DNS)")
else:
    print("Trànsit: Altres serveis / Desconegut")