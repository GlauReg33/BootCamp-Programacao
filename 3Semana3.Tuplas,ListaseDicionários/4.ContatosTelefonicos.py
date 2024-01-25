contatos = {
    'João': '123456789',
    'Maria': '987654321',
    'Pedro': '456789123',
    'Ana': '321654987'
}

# Função para procurar um contato pelo nome
def procurar_contato():
    nome = input("Digite o nome do contato que deseja procurar: ")
    if nome in contatos:
        telefone = contatos[nome]
        print(f"O telefone de {nome} é: {telefone}")
    else:
        print(f"Não foi encontrado um contato com o nome {nome}.")

# Chamar a função de busca de contato
procurar_contato()