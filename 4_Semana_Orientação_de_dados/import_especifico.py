from funcoes_do_log import nome_do_usuario, imprimir_no_log


imprimir_no_log(f'Bem Vinda, {nome_do_usuario}')
print()

def imprimir_no_log (texto):
    print(texto)

imprimir_no_log (f'Bem Vinda, {nome_do_usuario}')


