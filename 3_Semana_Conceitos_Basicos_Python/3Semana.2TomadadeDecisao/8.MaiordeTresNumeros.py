num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
num3 = float(input('Digite o 3º número: '))

#Determine o maior número usando estruturas condicionais

if num1 > num2 and num1 > num3:
    print('Maior é', num1)
elif num2 > num1 and num2 > num3:
    print('Maior é', num2)
else:
    print('Maior é', num3)