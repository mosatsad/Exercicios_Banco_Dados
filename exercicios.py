import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# 1. Crie uma Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR (100))')


# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Isadora", 19, "Matematica")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Maria", 20, "Ingles")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Joao", 21, "Ciencia de dados")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Rodrigo", 20, "Estatistica")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Ana Maria", 23, "Engenharia")')


# 3. Consultas Básicas. - Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".
df = cursor.execute('SELECT * FROM alunos')

for usuario in df:
    print(usuario)


# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
df = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20 ')

for usuario in df:
   print(usuario)


# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
df = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome ')

for usuario in df:
   print(usuario)


# d) Contar o número total de alunos na tabela.
df = cursor.execute('SELECT COUNT (*) FROM alunos')

for usuario in df:
   print(usuario)


# 4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade = 22 WHERE nome = "Ana Maria" ')

# b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE id = 4')


# 5. Criar uma Tabela e Inserir Dados, Crie uma tabela chamada "clientes" com os campos: id (chave
# primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.


cursor.execute('DROP TABLE clientes')

cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "Pedro", 21, 900.50)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Mariana", 23, 1110.50)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "Carlos Daniel", 50, 3050.90)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Paulina", 47, 6150.10)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "Esmeralda", 36, 2200.10)')


# 6. 
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
df = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

for usuario in df:
   print(usuario)


# b) Calcule o saldo médio dos clientes.
df = cursor.execute('SELECT AVG(saldo) as media_saldo FROM clientes')

for usuario in df:
   print(usuario)


# c) Encontre o cliente com o saldo máximo.
df = cursor.execute('SELECT nome, saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')

for usuario in df:
   print(usuario)


# d) Conte quantos clientes têm saldo acima de 1000.
df = cursor.execute('SELECT COUNT(*) as qtd_clientes FROM clientes WHERE saldo > 1000')

for usuario in df:
   print(usuario)


# 7. 
# a) Atualize o saldo de um cliente específico.
df = cursor.execute('UPDATE clientes SET saldo = 5000.10 WHERE nome = "Esmeralda" ')


# b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id = 2')

# 8.  Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando 
# o id da tabela "clientes"), produto (texto) e valor (real). 

cursor.execute('CREATE TABLE compras (id TEXT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor FLOAT, FOREIGN KEY(cliente_id) REFERENCES clientes(id))')

# Insira algumas compras associadas a clientes existentes na tabela "clientes". 
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES ("XYZ50", 1, "Smartphone Samsung", 900.50)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES ("XYZ60", 2, "Pendrive Kingston", 30.90)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES ("XYZ70", 3, "Mouse sem fio", 41.50)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES ("XYZ80", 4, "Tablet Lenovo", 789.70)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES ("XYZ30", 5, "Fone sem fio JBL - 500", 199.89)')


# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
df = cursor.execute('SELECT b.nome, a.produto, a.valor FROM compras AS a LEFT JOIN clientes as b ON b.id = a.cliente_id ')

for usuario in df:
   print(usuario)


conexao.commit()

conexao.close