bebida = 'refrigerante'
def cardapio():
    global bebida
    comida = 'humburguer'
    bebida = 'suco'
    print('comida: ', comida)
    print('bebida: ', bebida)

    cardapio()
    print('bebida: ', bebida)


    