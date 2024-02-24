#Solicitar a idade do usuário
idade = int(input('Digite a sua idade: '))

#Verificar a faixa etária

if idade < 13:
    print('Você é uma criança.')
elif idade < 18:
    print('Você é um adolescente.')
elif idade < 60:
    print('Você é uma adulto.')
else:
    print('Você é um idoso.')