import random

# ==========================================
# 1. TRIAR EL NÚMERO DE LA CARTA
# ==========================================
# Generem un número aleatori de l'1 al 13
num_aleatori = random.randint(1, 13)

# Traduïm el número al text de la carta de pòquer
if num_aleatori == 1:
    carta = "A"  # L'as de pòquer
elif num_aleatori == 11:
    carta = "J"
elif num_aleatori == 12:
    carta = "Q"
elif num_aleatori == 13:
    carta = "K"
elif num_aleatori == 2:
    carta = "2"
else:
    # Si és del 2 al 10, passem el número a text (string) per poder-lo concatenar després
    carta = str(num_aleatori)

# ==========================================
# 2. TRIAR EL PAL DE LA CARTA
# ==========================================
# Generem un número aleatori de l'1 al 4 per als pals
pal_aleatori = random.randint(1, 4)

if pal_aleatori == 1:
    pal = "Cors"
elif pal_aleatori == 2:
    pal = "Diamants"
elif pal_aleatori == 3:
    pal = "Piques"
else:
    pal = "Trebols"

# ==========================================
# 3. MOSTRAR EL RESULTAT CONCATENAT
# ==========================================
# Unim els dos strings amb un espai o la paraula "de"
resultat = carta + " de " + pal

print("--- LA TEVA CARTA ---")
print(resultat)