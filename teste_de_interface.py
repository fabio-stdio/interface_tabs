from tkinter import *
import py2sql_tabela_hq as py_sql

campos = 'carta', 'tipo', 'subtipo', 'raridade', 'cotação', 'data'

def data_mtg(entries):

	lista = []

	titulo = entries['carta'].get()
	tipo = entries['tipo'].get()
	subtipo = entries['subtipo'].get
	raridade = entries['raridade'].get
	cotação = entries['cotação'].get
	data_cot = entries['data'].get


	for item in campos:
		lista.append(item)



	py_sql.tarefa_insere(lista)


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
	root.bind('<Return>', (lambda event, e=ents: data_mtg(e)))
	b1 = Button(root, text='Submeter',command=(lambda e=ents: data_mtg(e)))
	b1.pack(side=LEFT, padx=5, pady=5)
	#Botão de saída.
	b2 = Button(root, text='Sair', command=root.quit)
	b2.pack(side=LEFT, padx=5, pady=5)
	root.mainloop()
