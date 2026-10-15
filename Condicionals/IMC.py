"""
Fes un programa per calcular l’IMC. 
(Índex Massa Corporal) que digui a l’usuari la classificació:

"""

peso = float(input("Cuanto pesas: "))
altura = float(input("Cuanto mides: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Tienes infrapeso")
elif 18.5 <= imc and imc <=24.9:
    print("Estas normal")
elif 25.0 <= imc and imc <= 26.9:
    print("Tienes sobrepeso")
else:
    print("Tienes Sobrepeso extremo")
