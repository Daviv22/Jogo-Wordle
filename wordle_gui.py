import tkinter as tk
from wordle import Wordle

class WordleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Worlde em Português")
        self.root.configure(bg = "grey")    # Define cor de fundo como cinza

        self.jogo = Wordle(arquivo_lexico="lexico.txt", tamanho=5, tentativas=6)
        
        self.criar_interface()

    def criar_interface(self):
        #Título
        titulo = tk.Label(self.root, text="Wordle", bg="grey")
        titulo.pack(pady=20)

        # Frame para o grid de letras
        self.frame_grid = tk.Frame(self.root, bg="grey")
        self.frame_grid.pack(pady=10)

        # Criar grid de células
        self.celulas = []
        for i in range(self.jogo.tentativas):
            linha = []
            for j in range(self.jogo.tamanho):
                celula = tk.Label(self.frame_grid)
                celula.grid(row=i, column=j, padx=5, pady=5)
                linha.append(celula)
            self.celulas.append(linha)

root = tk.Tk()

app = WordleGUI(root)

root.mainloop()
