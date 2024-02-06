# Pessoa é a nossa classe base

class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self.tipo = 'Pessoa'


    def falar_oi(self):
        print('Oi!Meu nome é {}'.format(self._nome))

    def falar_tipo(self):
        print('Meu tipo é {}'.format(self.tipo))

pessoa = Pessoa('Naira')
pessoa.falar_oi()
pessoa.falar_tipo()
print()

class Estudante(Pessoa): # o nome da classe base vem parênteses
        def __init__(self, nome, curso):
            super().__init__(nome) #Chama o construtorda classe base
            self._curso = curso

        def falar_curso(self):
            print(f'Eu {self._nome}, estudo o curso "{self._curso}"') #A propriedade self._nome é herdada da classe base

        def falar_tipo(self): #Sobrescreva a função original da classe Pessoa
            self._tipo = 'Estudante'
            return super().falar_tipo()
        
estudante = Estudante('Yasmim','Introdução ao Paython')
estudante.falar_oi() #o metodo falar_oi é herdado da classe base
estudante.falar_tipo() #o metodo falar_tipo é herdado da classe base, e sobreescrito na classe derivada
estudante.falar_curso()
print()

print('O objeto estudante é uma instancia da classe Estudante? ', isinstance(estudante, Estudante))
print('O objeto estudante é uma instancia da classe Pessoa? ', isinstance(estudante, Pessoa))
print('A classe Estudante é uma sub-classe de Pessoa? ', issubclass(Estudante, Pessoa))
print('A classe Pessoa é uma sub-classe de Estudante? ',issubclass(Pessoa, Estudante))

class Trabalhador(Pessoa): #Trabalhador também herda de Pessoa
            def __init__(self, nome, profissao):
                super().__init__(nome) # Clama o construtor da classe base
                self._profissao = profissao #atributo privado - só pode ser acessado dentro da classe trabalhador
                self._tipo = 'Trabalhador'

            def falar_profissao(self):
                    print(f'Eu, {self.nome}, exerço a profissão "{self._profissao}"')

            def falar_tipo(self): #sobreescreve a função original da classe Pessoa
                    return super().falar_tipo()
                
class Professor(Trabalhador): #Professor herda de Trabalhador
                    def __init__(self, nome, disciplina):
                        super().__init__(nome, 'Professor') #variaveis privadas não conseguem ser alteradas pela classe derivada
                        self._disciplina = disciplina

                    def falar_disciplina(self):
                            print(f'Eu, {self.nome},dou aula da disciplina "{self._diciplina}"')

                    def falar_tipo(self):
                            self._tipo = 'Professor'
                            return super().falar_tipo()
                        
trabalhadora = Trabalhador('Beatriz, "Desenvolvedora')
trabalhadora.falar_oi()
trabalhadora.falar_tipo()
trabalhadora.falar_profissao()
print()

professora = Professor('Clarise, "Python')
professora.falar_oi()
professora.falar_tipo()
professora.falar_profissao()
print()

#Em Python, todos as classes herdam implicitamente da classe object
class Humano:
    pass

#A classe Humano já começa com vários atributos e métodos
humano = Humano()
print(dir(humano))
print()

#Esses mesmos atributose métodos existem nas classes que declaramos acima
print(dir(professora))
print()
