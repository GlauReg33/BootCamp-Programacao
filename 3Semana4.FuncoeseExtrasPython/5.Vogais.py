def contar_vogais(frase):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador

frase = input("Insira uma frase: ")
total_vogais = contar_vogais(frase)
print("Total de vogais na frase:", total_vogais)