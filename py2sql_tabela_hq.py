import sqlite3




#Conexão com a base de dados

connection = sqlite3.connect("test.db")

#cursor

cursor = connection.cursor()

def insert_tab(char_t, int_n, char_col, char_ed, char_pub, char_con, char_f, char_l, int_ano, data, double_cp, double_est):
	#Comando para o sql.

	sql_command = """ INSERT INTO HQ VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""