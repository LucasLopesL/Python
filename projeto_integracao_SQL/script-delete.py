import pyodbc


dados_conexao = ("Drivers={'SQLite3 ODBC Driver'}; Server=localhost; Database=chinook.db")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("""
               DELETE FROM albuns WHERE AlbumID = 2
               """)
cursor.commit()

cursor.close()
conexao.close()
