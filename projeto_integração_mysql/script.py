import mysql.connector


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="bdvendas"
)

cursor = conexao.cursor()

# CRUD

# CREATE

nome_create = "Garrafa"
valor_create = 33
comando_create = f'''
INSERT INTO vendas(nome_produto, valor)
VALUES ('{nome_create}', {valor_create})
'''
cursor.execute(comando_create)
cursor.commit()

# READ

comando_read = 'SELECT * FROM vendas'
cursor.execute(comando_read)

# UPDATE
nome_update = "Garrafa"
valor_update = 21
comando_update = f'''
UPDATE vendas 
SET valor = {valor_update} 
WHERE 
    nome_produto = "{nome_update}"
'''
cursor.execute(comando_update)
cursor.execute()

# DELETE
nome_delete = "Garrafa"
comando_delete = f'''
DELETE FROM vendas 
WHERE 
    nome_produto == "{nome_delete}" 
'''
cursor.execute(comando_delete)
cursor.commit()


cursor.close()
conexao.close()
