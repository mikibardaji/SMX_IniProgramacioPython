aportacions = 0
estalvi = 0
alumnesTotal = 0
DINERO_LIMITE = 500

while aportacions < DINERO_LIMITE:
    estalvi = int(input(f"Quants diners aportes a l'excursió l'alumne {alumnesTotal+1}? "))
    aportacions += estalvi # sumo el estalvi
    alumnesTotal += 1 #conto alumnes que aporten

# calculo els diners qeu han sobrat
sobra = aportacions - DINERO_LIMITE
print(f" {alumnesTotal} alumnes han aportat 500 € i els hi ha sobrat {sobra} €")