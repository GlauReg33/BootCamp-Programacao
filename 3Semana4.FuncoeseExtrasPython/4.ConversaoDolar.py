def calcular_compra(moeda, quantidade):
    tabelas_conversao = {
        'Dólar Americano': 4.91,
        'Peso Argentino': 0.02,
        'Dólar Australiano': 3.18,
        'Dólar Canadense': 3.64,
        'Franco Suíço': 0.42,
        'Euro': 5.36,
        'Libra esterlina': 6.21
    }

    if moeda in tabelas_conversao:
        taxa_conversao = tabelas_conversao[moeda]
        compra = quantidade / taxa_conversao
        return compra
    else:
        return None

def main():
    dinheiro_na_carteira = float(input("Digite a quantidade de dinheiro na carteira: "))

    moedas = [
        'Dólar Americano',
        'Peso Argentino',
        'Dólar Australiano',
        'Dólar Canadense',
        'Franco Suíço',
        'Euro',
        'Libra esterlina'
    ]

    for moeda in moedas:
        compra = calcular_compra(moeda, dinheiro_na_carteira)
        if compra is not None:
            print(f"Com R${dinheiro_na_carteira:.2f}, você poderia comprar {compra:.2f} {moeda}")

if __name__ == '__main__':
    main()