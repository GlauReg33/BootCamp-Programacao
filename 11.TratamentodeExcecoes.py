def divisao(a,b):
try:
    resultado = a/b
    print(resultado)

except ZeroDivisionError:
    print(f'Erro: Impossível dividir um valor por zero')
except TypeError as e:
    print(f'Erro: o tipo do dado informado está incorreto. Detalhes:{e}')


divisao (10,2)
    