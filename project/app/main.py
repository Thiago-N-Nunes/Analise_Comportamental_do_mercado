import sqlite3
conexao = sqlite3.connect("../app/database.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS dados( 
               clubes TEXT NOT NULL,
               ano INTEGER NOT NULL)""")