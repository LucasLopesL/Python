import pyodbc


# print(pyodbc.drivers())
# dados_conexao = (
#                   "Driver={Driver}";
#                   "Server=Servidor";
#                   "Database=Banco de dados"; 
#                   "UID=Login"; 
#                   "PWD=Senha"
#                  )

dados_conexao = ("Driver={SQLite3 ODBC Driver}; Server=localhost; Database=salarios.db")

conexao = pyodbc.connect(dados_conexao) # Cria a conexção com o banco de dados
cursor = conexao.cursor() # Quem esxecutará os códigos SQL

cursor.execute("SELECT * FROM Salaries")

valores = cursor.fetchall() # Mostra todos os resuldados das cinsultas feitas pelo cursor

cursor.close() #Finaliza a conexão do cursor
conexao.close() # Finaliza a conexão com o Banco de Dados