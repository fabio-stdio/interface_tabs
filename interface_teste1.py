from tkinter import *



campos = 'Título', 'Número', 'Coleção', 'Editora', 'Editora de Origem', 'Conservação', 'Coleção Fechada', 'Linha temporal', 'Ano de Publicação', 'Data (se periódico)', 'Preço de Capa (reais)', 'Preço estimado (reais)'

def dados(entries):

	#função com o dicionário com os lables para pegar as entradas nas caixas de testo que serão montadas na função formulario.
	
	titulo = entries['Titulo'].get()
	colecao = entries['Coleção'].get()
	editora = entries['Editora'].get
	publisher = entries['Editora de origem'].get
	conserv = entries['Conservação'].get
	fechada = entries['Coleção Fechada'].get
	temp = entries['Linha temporal'].get
	ano_pub = entries['Ano de Publicação'].get
	data = entries['Data (se peródico)'].get
	price_cp = entries['Preço de Capa (reais)'].get
	price = entries['Preço estimado (reais)'].get

	# Falta passar para a função que irá alimentar a tabela em py2sql_hq.py

def formulario(root, campos):

	# Montagem das caixas de texto e do formulário.

	#Para a função dados.
	entries = {}

	for campo in campos:
		row = Frame(root)
		lab = Label(row, width=40, text=campo+":", anchor='w')
		ent = Entry(row)
		row.pack(side=TOP, fill=X, padx=5, pady=5)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		entries[campo] = ent

	return entries


if __name__=='__main__':
	root = Tk()
	ents = formulario(root, campos)
	#Para habilitar o enter como se fosse o botão submeter.
	root.bind('<Return>', (lambda event, e=ents: dados(e)))
	b1 = Button(root, text='Submeter',command=(lambda e=ents: dados(e)))
	b1.pack(side=LEFT, padx=5, pady=5)
	#Botão de saída.
	b2 = Button(root, text='Sair', command=root.quit)
	b2.pack(side=LEFT, padx=5, pady=5)
	root.mainloop()




	