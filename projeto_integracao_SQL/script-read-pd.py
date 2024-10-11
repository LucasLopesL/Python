import pandas as pd
import sqlite3

conexao = sqlite3.connect(r"Python\projeto_integracao_SQL\chinook.db")

tabelas_clientes = pd.read_sql("SELECT * FROM custumers", conexao)
print(tabelas_clientes)

conexao.close()
