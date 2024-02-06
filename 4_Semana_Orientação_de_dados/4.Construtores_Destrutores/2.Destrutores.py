class Minha_Classe:
    def __init__(self, nome) -> None:
        self.nome = nome
        print(f'Minha_Classe1: Chamouo construtor padrão de {'nome'}')

    def _del_ (self):
      print(f'Minha_Classe1: Chamou o destrutor de {self.nome}')  

print('Comecou a execução do programa')
Objeto1 = Minha_Classe ('Obejto1')
print('Vai terminar a execução do programa')
exit()