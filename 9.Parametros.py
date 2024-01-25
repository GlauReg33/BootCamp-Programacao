def soma(num1, num2): #definição da função soma
    calculo = 10+2
    print(f'O resultado da soma é {calculo}')


def subtracao(num1, num2):
    sub = 10-2
    print(f'O resultado da subtração é {sub} ')


def multiplicacao(num1, num2):
    mult = 10*2
    print(f'O resultado da multiplicação é {mult}')

num1 = int(input('Digite o 1º numero: '))
num2 = int(input('Digite o 2º numero: '))

soma (num1, num2) #chamada da função
subtracao(num1, num2)
multiplicacao (num1, num2)