import tkinter as tk
from wordle import Wordle

class WordleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Worlde em Português")
        self.root.configure(bg = "grey")    # Define cor de fundo como cinza

        self.jogo = Wordle(arquivo_lexico="lexico.txt", tamanho=5, tentativas=6)
        self.tentativa_atual = 0
        
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

        # Entry para input de teclas
        self.entry = tk.Entry(self.root, bg="grey", fg="white", insertbackground="white", font=("Arial", 1))

        self.entry.place(width=0, height=0)
        self.entry.focus()

        # Bind de teclas
        self.root.bind("<Key>", self.tecla_pressionada)

    def tecla_pressionada(self, event):
        if self.tentativa_atual >= self.jogo.tentativas:
            return None
        
    def verificar_palavra(self):
        if self.letra_atual != self.jogo.tamanho:
            print("Palavra incompleta!")
            return
        
        # Pegar a palavra digitada
        palavra = ""
        for i in range(self.jogo.tamanho):
            palavra += self.celulas[self.tentativa_atual][i].cget("text").lower()
        
        # Simplificar a palavra para verificação
        palavra_simplificada = self.jogo._simplifica_palavra(palavra)

        # Verificar se a palavra é válida
        if not self.jogo.verifica_chute(palavra_simplificada):
            print("Palavra inválida")
            return
        

root = tk.Tk()

app = WordleGUI(root)

root.mainloop()
