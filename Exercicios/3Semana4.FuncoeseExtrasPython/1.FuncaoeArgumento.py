def somar_tres_numeros(a, b, c):
    soma = a + b + c
    return soma

# Solicita três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Chama a função para obter a soma dos três números informados
resultado = somar_tres_numeros(num1, num2, num3)

# Imprime o resultado
print("A soma dos três números é:", resultado)
