class Logavel:
    def __init__(self) -> None:
        self.nome_de_classe = ' '
    def logar(self,mensagem):
        print('Mensagem da classe ' + self.nome_de_classe + ': ' + mensagem)


class Conexao:
    def __init__(self) -> None:
        self.servidor = ' '
    def conectar(self):
        print('Conectando ao banco de dados no servidor ' + self.servidor)
        #  Lógica para realizar a conexão aqui

class MySqDatabase (Conexao, Logavel):
    def __init__(self) -> None:
        super().__init__()
        self.nome_de_classe = 'MySqlDatabase'
        self.servidor = 'MeuServidor'

def framework(objeto):
    if isinstance(objeto, Conexao):
        objeto.conectar()
    if isinstance(objeto, Logavel):
        mensagem = 'Olá mulheres maravilhosas do Bootcamp de Python'
        objeto.logar(mensagem)

Conexao_mysql = MySqDatabase()
framework(Conexao_mysql)