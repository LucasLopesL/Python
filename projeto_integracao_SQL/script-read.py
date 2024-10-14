import pyodbc
import pandas as pd

# print(pyodbc.drivers())

dados_conexao = ("Drivers={SQLite3 ODBC Driver}; Server=localhost; Database=chinook.db")

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM customers")
valores = cursor.fetchall()

descricao = cursor.description()
colunas = [tupla[0] for tupla in descricao] # list comprehension

tabela_clientes = pd.DataFrame.from_records(valores, columns=colunas)
print(tabela_clientes)

cursor.close()
conexao.close()
