# Ordem de precedência

calculo = 2+5*5
print (calculo)

calculo1 = (2+5)*5
print (calculo1)


calculo2 = (2+5)*((5+4)*3)
print (calculo2)


# Operações relacionais

# == - igual
igual = (5 == 5)
print (igual)

# > - maior
maior = (5 > 5)
print (maior)

# >= - maior igual
maior_igual = 5 >= 5
print(maior_igual)
# < - menor

menor = (5 < 5)
print(menor)

# <= - menor igual

menor_igual = (5 <= 5)
print(menor_igual)

# != - diferente

diferente = (5 != 6)
print (diferente)

#Formatação de Mensagem

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero:'))
soma = numero1+numero2

print (f'Asoma dos números digitados é {soma}')