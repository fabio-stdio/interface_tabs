import mysql.connector as mariadb
import os.path

arquivo_db = 'test'

#def insert_tab(char_t, int_n, char_col, char_ed, char_pub, char_con, char_f, char_l, int_ano, data, double_cp, double_est)
def conection(arquivo_db):
	#Cria conexão para o banco de dados específico arquivo_db.

	#Conexão com a base de dados
	try:

		connection = mariadb.connect(database=arquivo_db)
		return connection

	except Error as e:
		print(e)

	return None



def cria_tabela(parametros, tipo):


	conn = conection(arquivo_db)
	cursor = conn.cursor()

	cursor.execute

	



def tarefa_insere(lista):
	#cursor
	conn = conection(arquivo_db)
	cursor = conn.cursor()


	#sql_command = """ INSERT INTO teste (coluna1, coluna2, coluna3, coluna4, coluna5) VALUES (?, ?, ?, ?, ?)"""
	
	cursor.executemany(""" INSERT INTO mtg (carta, tipo, subtipo, raridade, cotação, data_cotação) VALUES (?, ?, ?, ?, ?, ?) """, lista)

	connection.commit()

	# Encerra a conexão com o DB.
	connection.close()

