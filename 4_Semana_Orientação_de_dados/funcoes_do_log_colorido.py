import colorama

colorama.init()

nome_de_usuario = 'Dori'

def imprimir_no_log(texto, nivel='info'):
    if nivel.lower == 'info':
        print(colorama.Fore.LIGHTBLACK_EX + f'info: ', end='')
        print( colorama.Style.RESET_ALL+texto)
    elif nivel.lower == 'aviso':
        print(colorama.Fore.YELLOW + f'aviso: ', end='')
        print( colorama.Style.RESET_ALL+texto)
    elif nivel.lower == 'erro':
        print(colorama.Fore.RED + f'erro: ', end='')
        print( colorama.Style.RESET_ALL+texto)
    else:
        print(colorama.Fore.RED + 'Erro interno - nivel desconhecido de mensagem' + colorama.Style.RESET_ALL)