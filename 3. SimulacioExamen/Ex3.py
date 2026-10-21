# Mostrem el menú principal per pantalla
print("=== MENÚ D'AVALUACIÓ DEL VEHICLE ===")
print("I) Revisions mecàniques")
print("II) Consum de combustible")
print("III) Pressió de pneumàtics")

# Demanem l'opció a l'usuari i la passem a majúscules amb .upper()
opcio = input("Tria una opció (I, II, III): ").upper().strip()

# ==========================================
# OPCIÓ I: REVISIONS MECÀNIQUES
# ==========================================
if opcio == "I":
    # Demanem les dades. Passem la resposta a majúscules per si escriuen "si" o "Si"
    revisio = input("Has passat la revisió anual? (SI/NO): ").upper().strip()
    km = int(input("Quants km fa que l’has passat?: "))
    
    if revisio == "SI" and km < 5000:
        print("Perfecte")
    elif revisio == "SI" and km >= 5000 and km <= 7000:
        print("Recorda que a partir dels 7000 hauries de tornar a passar-la")
    else:
        print("Has de millorar el manteniment")

# ==========================================
# OPCIÓ II: CONSUM DE COMBUSTIBLE
# ==========================================
elif opcio == "II":
    km_mes = float(input("Quants quilòmetres fas al mes amb el vehicle?: "))
    velocitat_mitja = float(input("A quina velocitat mitja ho fas?: "))
    
    # Calculem les hores (Temps = Distància / Velocitat)
    hores = km_mes / velocitat_mitja
    
    if hores > 20:
        print("Hauries de caminar més")
    else:
        print("Son poques hores…")

# ==========================================
# OPCIÓ III: PRESSIÓ DE PNEUMÀTICS
# ==========================================
elif opcio == "III":
    print("La pressió dels pneumàtics ha de ser 2,2")

# ==========================================
# OPCIÓ NO VÀLIDA
# ==========================================
else:
    print("Opció no vàlida")
