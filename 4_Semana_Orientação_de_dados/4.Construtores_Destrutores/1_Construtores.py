#Construtor padrão
class Minha_Classe1:
    def __init__(self) -> None:
        print('MinhaClasse1: Chamou o construtor padrão')

class Minha_Classe2:
    pass #não faz nada

#Construtor parametrizado
class Minha_Classe3:
    def __init__(self, param) -> None:
        print(f'Minha_Classe3: Chamou o construtor parametrizado com o parâmentro {param}')

objeto1 = Minha_Classe1()
objeto2 = Minha_Classe2()
objeto3 = Minha_Classe3('meu objeto')
