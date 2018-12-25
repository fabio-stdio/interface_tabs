import sqlite3




#def insert_tab(char_t, int_n, char_col, char_ed, char_pub, char_con, char_f, char_l, int_ano, data, double_cp, double_est)
def insert_tab_teste(lista):
	#Comando para o sql.

	#Conexão com a base de dados

	connection = sqlite3.connect("test.db")

	#cursor

	cursor = connection.cursor()


	#sql_command = """ INSERT INTO teste (coluna1, coluna2, coluna3, coluna4, coluna5) VALUES (?, ?, ?, ?, ?)"""
	
	cursor.executemany(""" INSERT INTO teste (coluna1, coluna2, coluna3, coluna4, coluna5) VALUES (?, ?, ?, ?, ?) """, lista)

	connection.commit()

	# Encerra a conexão com o DB.
	connection.close()

