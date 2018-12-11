from tkinter import *



campos = 'Título', 'Número', 'Coleção', 'Editora', 'Editora de Origem', 'Conservação', 'Coleção Fechada', 'Linha temporal', 
					'Ano de Publicação', 'Data (se periódico)', 'Preço de Capa (reais)', 'Preço estimado (reais)'

def dados(entries):
	
	titulo = entries['Titulo'].get()
	colecao = entries['Coleção'].get()
	
	