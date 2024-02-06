#encapsulamento
class Pessoa:
    def __init__(self, nome, profissao, identidade) -> None:
        self._nome = nome
        self.profissao = profissao
        self._identidade = identidade
    
    def __str__(self) -> str:
        return f'Nome: {self._nome}, Profissao: {self.profissao}, Identidade: {self._identidade}'
    
pessoa1 = Pessoa('Marta Lima','Astronauta', '12345')
print(pessoa1)

    # print()

    # # Se tentarmos alterar um atributo público, nós vamos conseguir
pessoa1.profissao = 'Programador'
print(pessoa1)
print()

    # # Se tentarmos alterar um atributo protegido, nós vamos conseguir também
pessoa1_nome = 'Marta'
print(pessoa1)
print()

    # # Ao tentarmos alterar um atributo privado, o valor não vai ser alterado
pessoa1._identidade = '23525'
print(pessoa1)
print()

