import sqlite3

conexao = sqlite3.connect("data/database.db")
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS dados")