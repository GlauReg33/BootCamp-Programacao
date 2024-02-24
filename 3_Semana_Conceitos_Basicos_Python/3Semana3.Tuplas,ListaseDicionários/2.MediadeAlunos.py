# Lista para armazenar as médias dos alunos
medias = []

# Loop para solicitar as notas e calcular a média de cada aluno
for i in range(5):
    notas = []
    for j in range(4):
        nota = float(input(f"Informe a nota {j+1} do aluno {i+1}: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    medias.append(media)

# Contagem de alunos com média maior ou igual a 7.0
contador = 0
for media in medias:
    if media >= 7.0:
        contador += 1

# Impressão do resultado
print(f"O número de alunos com média maior ou igual a 7.0 é: {contador}")