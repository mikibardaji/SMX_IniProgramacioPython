import funcionsBardaji
# 
valor1 = funcionsBardaji.valorPositivo("Pon el primer valor positivo: ")
valor2 = funcionsBardaji.valorPositivo("Pon el segundo valor positivo: ")
valor3 = funcionsBardaji.valorPositivo("Pon el tercer valor positivo: ")
valor4 = funcionsBardaji.valorPositivo("Pon el cuarto valor positivo: ")

mayor1o2 = funcionsBardaji.grande(valor1,valor2)
mayorhasta3 = funcionsBardaji.grande(mayor1o2, valor3)
elMasGrande = funcionsBardaji.grande(mayorhasta3,valor4)

print(f" El valor mas grande entre {valor1} , {valor2} , {valor3} y {valor4} es {elMasGrande}")