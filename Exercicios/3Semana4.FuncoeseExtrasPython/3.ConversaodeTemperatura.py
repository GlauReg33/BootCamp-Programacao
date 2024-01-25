def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def menu():
    print("Selecione a opção desejada:")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")
    print("3. Sair")

while True:
    menu()
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius} graus Celsius equivalem a {fahrenheit} graus Fahrenheit.\n")
    elif opcao == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit} graus Fahrenheit equivalem a {celsius} graus Celsius.\n")
    elif opcao == '3':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")