import pyodbc

dados_conexao = (
    "Drivers={SQLite3 ODBC Driver};" 
    "Server=localhost;"
    "Database=chinook.db"
    )

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("""INSERT INTO albuns (Title, ArtistId)
                    VALUES
                        ('Lucas Rei do Python', '10')"""
                )

cursor.commit()
cursor.close()
conexao.close()