import sqlite3


Conexao = sqlite3.connect('banco')
cursor = Conexao.cursor()

#Criar uma tabela
#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#Renomear uma tabela
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#Criar uma coluna
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#Renomear uma coluna
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

#Criando a tabela que será excluida
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#Drop exclui toda a tabela
#cursor.execute('DROP TABLE produtos')
#Comando para incluir dados na tabela
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email,telefone) VALUES(1, "iSADORA", "França", "isadora@ig", 236443)')
#Criando mais dados para a planilha
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email,telefone) VALUES(2, "Maria", "Brasil", "isadora@ig", 236443)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email,telefone) VALUES(3, "Jose", "Argentina", "isadora@ig", 236443)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email,telefone) VALUES(4, "Glaucia", "Russia", "isadora@ig", 236443)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email,telefone) VALUES(5, "Maristela", "EUA", "isadora@ig", 236443)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email,telefone) VALUES(6, "Amanda", "Africa do Sul", "isadora@ig", 236443)')
#Criação de uma linha duplicada para ser excluida
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email,telefone) VALUES(6, "Amanda", "Africa do Sul", "isadora@ig", 236443)')
#Para exclusão
#cursor.execute('DELETE FROM usuario where id=6')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email,telefone) VALUES(1, "iSADORA", "França", "isadora@ig", 236443)')

#Para visualizar aqui no terminal os dados da tabela no Dbeaver
#dados = cursor.execute('SELECT * FROM usuario')
#for usuario in dados:
    #print(usuario)

#Para visualizar aqui no terminal somente alguns dados da tabela no Dbeaver
#dados = cursor.execute('SELECT nome, telefone FROM usuario')
#for usuario in dados:
    #print(usuario)
#Com condições
#dados = cursor.execute('SELECT nome, telefone FROM usuario where id>2')
#for usuario in dados:
    #print(usuario)

# Alterar o dado de uma coluna
#cursor.execute('UPDATE usuario SET endereco="Minas Gerais" Where nome="Jose"')

#Ordenando a tabela, crescente
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome')
#for usuario in dados:
    #print(usuario)
#Descrecente
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')
#for usuario in dados:
    #print(usuario)

#cursor.execute('UPDATE usuario SET nome="Isadora" Where id="1"')

#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome, id DESC')
#for usuario in dados:
    #print(usuario)

#Limite e Distancia
#dados = cursor.execute('SELECT * FROM usuario LIMIT 3')
#for usuario in dados:
    #print(usuario)

#GROUP BY e HAVING
#dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')
#for usuario in dados:
    #print(usuario)

#Criando a tabela gerentes
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

#Incluindo dados
#cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(2, "Maria", "Brasil", "isadora@ig")')
#cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(8, "Cintia", "São Paulo", "Cintia@ig")')
#cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(1, "João", "São Paulo", "Cintia@ig")')

#JOIN's
# JOIN - INNER JOIN
#dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')
#for usuario in dados:
    #print(usuario)

# JOIN - LEFT JOIN
#dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.nome')
#for usuario in dados:
    #print(usuario)

# JOIN - RIGHT JOIN
#dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.id = gerentes.nome')
#for usuario in dados:
    #print(usuario)

# JOIN - FULL JOIN
#dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.id = gerentes.nome')
#for usuario in dados:
    #print(usuario)
#Sub-Consultas
dados = cursor.execute('SELECT * FROM usuario WHERE nome IN(SELECT nome FROM gerentes)')
for usuario in dados:
    print(usuario)

Conexao.commit()
Conexao.close

