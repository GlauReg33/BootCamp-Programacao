login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == "admin" and senha == "admin123":
    print("Acesso permitido!")
else:
    print("Erro: login ou senha incorretos.")