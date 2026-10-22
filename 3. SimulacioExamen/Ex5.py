import random

# ==========================================
# 1. RECOLLIDA DE DADES DEL VIATGER
# ==========================================
nom_complet = input("Introdueix el teu nom complet: ")
edat = int(input("Introdueix la teva edat: "))
pes_maleta = float(input("Introdueix el pes de la teva maleta en kg: "))

# ==========================================
# 2. PROCESSAR EL TEXT
# ==========================================
# Passem el nom a majúscules i traiem espais extres del principi i final
nom_complet = nom_complet.upper().strip()

print("\n--- PROCESSANT CONTROL DE SEGURETAT ---")

# ==========================================
# 3. COMPROVAR LES NORMES (CONDICIONALS)
# ==========================================

# Comprovació del pes de la maleta
if pes_maleta > 23.0:
    print("Avís: La maleta pesa més de 23 kg. Has de pagar una taxa extra.")
else:
    print("Pes de la maleta: Correcte.")

# Comprovació de viatger menor amb prioritat A
# Mirem si l'edat és menor de 18 I si la posició [0] del nom és una 'A'
if edat < 18 and (nom_complet[0:1] == "A" or  nom_complet[0:1] == "a"):
    print("Atenció: Viatger menor amb prioritat A")

# ==========================================
# 4. FACTOR ALEATORI (SORTEIG REVISIÓ)
# ==========================================
# Generem un número aleatori entre 1 i 5
sorteig = random.randint(1, 6)
print(sorteig)
if sorteig == 3:
    print("Codi Vermell: La teva maleta ha estat seleccionada per a una revisió aleatòria.")
else:
    print("Bon viatge, pots passar no farem control de maleta.")
