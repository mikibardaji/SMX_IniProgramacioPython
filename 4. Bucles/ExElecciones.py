OpcioA = 0
OpcioB = 0
Blanc = 0
numParticipantes = 1
Voto = ""

while numParticipantes<=5:
    voto = input("Cual es tu voto A/B/BLANCO").upper()

    if voto == "A":
        OpcioA += 1
        print("Has votat a A")
        numParticipantes += 1
    elif voto == "B":
        OpcioB += 1
        numParticipantes += 1
    elif voto == "BLANCO":
        Blanc += 1
        numParticipantes += 1
    else:
        print("Eres un corrupto")
    # numParticipantes += 1 para no contar el corrupot

print("Resultados finales")