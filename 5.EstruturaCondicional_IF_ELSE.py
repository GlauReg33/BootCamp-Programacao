# Estrutura Condicional IF e Else

# If idade > 17 : Condição para execução (IF - Se)

# Else condição será executada se a anterior for falsa (Else - Senão)

numero = int(input('Digite seu numero: '))

if numero > 0:
    print('numero é positivo')
else:
    print ('numero é negativo')


# While idade > 17: Enquanto a condição for verdadeira, está condição será excutada
    numero = -1
    while numero < 0:
        numero = int(input('Digite seu numero: '))

        print('Número positivo inserido com sucesso')

# For 
frutas = ['maça', 'banana', 'uva'] # declarando uma lista 
for fruta in frutas:
        print (fruta)
