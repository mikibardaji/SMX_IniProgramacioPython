print("--- MENÚ DE SALUT I HABITS ---")
print("A. Hàbits d’estudi")
print("B. Alimentació")
print("C. Hores de son")

# Demanar l'opció a l'usuari upper() perque sigui ajuscula SEGUR
opcio = input("Tria una opció (A, B o C): ").upper()

if opcio == "A":
    
    estudies_tots_els_dies = input("Estudies tots els dies? (SÍ / NO): ").upper()
    hores_dia = (input("Quantes hores al dia? "))
    
    # Condicions per avaluar els hàbits d'estudi
    if estudies_tots_els_dies == "SÍ" and hores_dia >= 1:
        print("Perfecte")
    elif estudies_tots_els_dies == "NO" and hores_dia == 4:
        print("Perfecte")
    else:
        print("Tens que millorar els teus hàbits")

elif opcio == "B":
    # Pregunta sobre alimentació
    calories = int(input("Quantes calories menges al dia? "))
    
    # Condicions per avaluar les calories
    if calories < 1800:
        print("hauries d’alimentar-te més")
    elif calories >= 1800 and calories <= 3200:
        print("Alimentació Saludable")
    else:
        print("Hauries de reduir la teva aportació calòrica")

elif opcio == "C":
    # Comentari directe sobre les hores de son
    print("Les hores recomanades de son són entre 7 i 8")

else:
    # Si prem qualsevol altra lletra o caràcter
    print("opció no valida")