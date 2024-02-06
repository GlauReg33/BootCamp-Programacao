from abc import ABC, abstractmethod

# A classe base dos pokemons
class BasePokemon(ABC):
    def __init__(self, nome):
        self.nome = nome
        self._nivel = 1
        self.experiencia = 0

    @abstractmethod
    def ataque_principal(self): #O uso de métodos abstratos torna a classe abstrata.
        pass

    @abstractmethod
    def passar_de_nivel(self):
        pass

    @abstractmethod
    def evoluir(self):
        pass

    @property
    @abstractmethod
    def tipo(self):
        pass

    # Criar um objeto de uma classe abstrata gera um erro
    # Pokemon - BasePokemon ('Pikachu','Elétrica')

class Pikachu(BasePokemon):
    def __init__(self, nome):
        super().__init__(nome)

    def ataque_principal(self):
        print(f'{self.nome} usou choque de trovao!')
        self.experiencia += 2
        self.passar_de_nivel()
    
    def passar_de_nivel(self):
        #Passa de nivel a cada 10 pontos de experiência
        if self.experiencia % 10 == 0:
            self._nivel += 1
            print(f'{self.nome} passou para o nivel {self._nivel}!')
            self.evoluir()

    def evoluir(self):
        if self._nivel == 25:
            print('!!!! Evoluiu para Raichu!!!')
            self.nome = 'Raichu'

    @property
    def tipo(self):
        return 'Elétrico'
    
    def ataque_secundario(self):
        print(f'{self.nome} usou Surra de Calda!')
        self.experiencia += 2
        self.passar_de_nivel()

pokemon = Pikachu('Pikachu')
print(pokemon.nome + 'é um pokemon do tipo ' + pokemon.tipo)
for _ in range(125):
    pokemon.ataque_principal()
    pokemon.ataque_secundario()