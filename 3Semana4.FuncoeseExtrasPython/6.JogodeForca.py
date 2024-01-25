import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'jogos', 'computador', 'desenvolvimento']
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    exibicao = ''
    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra + ' '
        else:
            exibicao += '_ '
    return exibicao

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 6

    print('Bem-vindo ao Jogo da Forca!')
    print('A palavra possui', len(palavra_secreta), 'letras.')

    while True:
        print('\n' + exibir_palavra(palavra_secreta, letras_corretas))

        if '_' not in exibir_palavra(palavra_secreta, letras_corretas):
            print('Parabéns! Você ganhou!')
            break

        if tentativas == 0:
            print('Você perdeu! A palavra era:', palavra_secreta)
            break

        letra = input('Digite uma letra: ').lower()

        if letra in letras_corretas:
            print('Você já tentou essa letra. Tente novamente.')

        elif letra in palavra_secreta:
            print('Letra correta!')
            letras_corretas.append(letra)

        else:
            print('Letra incorreta!')
            tentativas -= 1

        print('Tentativas restantes:', tentativas)

jogar_forca()