import pyodbc
import pandas as pd
import sqlite3

# print(pyodbc.drivers())

# dados_conexao = ('Drivers={SQLite3 ODBC Driver};Server=localhost;Database=salarios.sqlite');
# conexao2 = pyodbc.connect(dados_conexao)
# cursor = pyodbc.cursor()

# cursor.execute("SELECT * FROM Salaries")
# valores = cursor.fetchall()
# descricao = cursor.description()
# colunas = [desc[0] for desc in descricao]
# tabela_salarios2 = pd.DataFrame.from_records(valores, columns=colunas)

# print(tabela_salarios2)

# cursor.close()
# conexao2.close()

conexao = sqlite3.connect(r'Python\projeto_integracao_SQL\salarios.sqlite')
tabela_salarios = pd.read_sql("SELECT * FROM Salaries", conexao)

tabela_salarios_sf = tabela_salarios.loc[tabela_salarios["Agency"] == "San Francisco", :]

# Qual foi a média de salário ao longo do ano

tabela_salario_medio = tabela_salarios_sf[["TotalPay", "TotalPayBenefits", "Year"]].groupby("Year").mean()
print(f'A média de salário com e sem benefícios ao longo dos anos:\n{tabela_salario_medio}')

# Quantos funcionários tiveram ao longo dos anos

tabela_fucionarios = tabela_salarios_sf[["Id", "Year"]].groupby("Year").count()
print(f'A quantidade de funcionários ao longo dos anos:\n{tabela_fucionarios}')

# Qual foi a evolução do total gasto com salários ao longo dos anos

tabela_salario = tabela_salarios_sf[["TotalPay", "TotalPayBenefits", "Year"]].groupby("Year").sum()
print(f'O total gasto com salários com e sem benefícios ao longo dos anos:\n{tabela_salario}')
