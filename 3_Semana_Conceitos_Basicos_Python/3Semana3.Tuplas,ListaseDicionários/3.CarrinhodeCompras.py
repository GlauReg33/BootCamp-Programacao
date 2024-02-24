carrinho_de_compras = {}  # Criar um dicionário vazio para o carrinho de compras

# Adicionar produtos e quantidades ao carrinho
carrinho_de_compras['maçã'] = 2
carrinho_de_compras['banana'] = 3
carrinho_de_compras['laranja'] = 1
carrinho_de_compras['abacaxi'] = 4

# Calcular o total do carrinho
total = 0

for produto, quantidade in carrinho_de_compras.items():
    # Aqui você pode substituir os preços reais dos produtos
    # ou calcular o valor total com base em alguma informação externa
    # por exemplo, um banco de dados de preços.
    preco_unitario = 1.5  # Preço unitário fictício de cada produto
    total_produto = preco_unitario * quantidade
    total += total_produto

print("Total do carrinho de compras: R$", total)