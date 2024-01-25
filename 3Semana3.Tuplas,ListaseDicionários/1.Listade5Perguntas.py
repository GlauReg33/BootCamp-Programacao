respostas = []

pergunta1 = input("Telefonou para a vítima? (s/n): ")
respostas.append(pergunta1)

pergunta2 = input("Esteve no local do crime? (s/n): ")
respostas.append(pergunta2)

pergunta3 = input("Mora perto da vítima? (s/n): ")
respostas.append(pergunta3)

pergunta4 = input("Devia para a vítima? (s/n): ")
respostas.append(pergunta4)

pergunta5 = input("Já trabalhou com a vítima? (s/n): ")
respostas.append(pergunta5)

print("Respostas registradas:", respostas)

positivas = respostas.count("s")

if positivas == 2:
    print("Classificação: Suspeita")
elif positivas >= 3 and positivas <= 4:
    print("Classificação: Cúmplice")
elif positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")