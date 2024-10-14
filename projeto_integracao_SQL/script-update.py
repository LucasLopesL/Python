import pyodbc


dados_conexao = ("Drivers={'SQLite3 ODBC Driver'}; Server=localhost; Database=chinook.db")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("""
    UPDATE customers SET Email='lucaslopes@reidopython.com.br' WHERE CustumerId=10
""")
cursor.commit()

cursor.close()
conexao.close()
