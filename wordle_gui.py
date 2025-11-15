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
        titulo = tk.Label(self.root, text="Wordle")

        # Frame para o grid de letras
        self.frame_grid = tk.Frame(self.root, bg="grey")
        self.frame_grid.pack(pady=10)


