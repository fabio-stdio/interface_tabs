from tkinter import *


class Quadrinhos(Frame):
	campos = 'Título', 'Número', 'Coleção', 'Editora', 'Editora Original', 'Estado de Conservação', 'Arco Fechado?', 'Linha Publicação', 


	def __init__(self):
		super().__init__()

		self.InterRel()

	def InterRel(self):

		self.master.title("Relação de Quadrinhos")
		self.pack(fill=BOTH, expand=True)


		self.fontepadrao = ("Arial", "10")

		#Criação das caixas de texto e os labels ao lado delas para as entradas que irão para a tabela.

		
		frame1 = Frame(self)
		frame1.pack(fill=X)

		rotulo1 = Label(frame1, text="Título", width=6)
		rotulo1.pack(side=LEFT, padx=5, pady=5)

		entrada1 = Entry(frame1)
		entrada1.pack(fill=X, padx=5, expand=True)

		frame2 = Frame(self)
		frame2.pack(fill=X)

		rotulo2 = Label(frame2, text="Número", width=6)
		rotulo2.pack(side=LEFT, padx=5, pady=5)

		entrada2 = Entry(frame2)
		entrada2.pack(fill=X, padx=5, expand=True)

		frame3 = Frame(self)
		frame3.pack(fill=X)

		rotulo3 = Label(frame3, text="Coleção", width=6)
		rotulo3.pack(side=LEFT, padx=5, pady=5)

		entrada3 = Entry(frame3)
		entrada3.pack(fill=X, padx=5, pady=5)

		frame4 = Frame(self)
		frame4.pack(fill=X)

		rotulo4 = Label(frame4, text="Editora", width=6)
		rotulo4.pack(side=LEFT, padx=5, pady=5)

		entrada4 = Entry(frame4)
		entrada4.pack(fill=X, padx=5, expand=True)



def main():

	root = Tk()
	root.geometry("600x600+300+300")
	app = Quadrinhos()
	root.mainloop()


if __name__ == '__main__':
	main()