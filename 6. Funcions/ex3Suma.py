def suma(num1: int, num2: int):
    resultado = num1 + num2
    return resultado

#programa principa
input_num1 = int(input("Pon el primer numero: "))
input_num2 = int(input("Pon el segundo numero: "))
resultadoSuma = suma(input_num1,input_num2)
print(f"La suma de {input_num1} + {input_num2} = {resultadoSuma}")