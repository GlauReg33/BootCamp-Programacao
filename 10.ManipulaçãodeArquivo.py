def multiplicacao():
    mult = 10*2
    print(f'O resultado da multiplicação é {mult}')
    file = 'arquivo.txt'


    #Formas de abertura - Open

 

#Abertura para Escrita
arquivo_escrita = open('file', "w")
arquivo_escrita.write ("Texto a ser escrito")
arquivo_escrita.close()

 # Abertura somente para leitura
arquivo_leitura = open('file', "r")
leitura = arquivo_leitura.read ()
print(leitura)
arquivo_escrita.close()


#Abertura de arquivo binário
arquivo_binario = open('file', "wb")

multiplicacao () #Chamada da função





    