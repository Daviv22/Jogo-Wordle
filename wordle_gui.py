import tkinter as tk
from wordle import Wordle

class WordleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Worlde em Português")
        self.root.configure(bg="#121213")    # Define cor de fundo como cinza

        self.jogo = Wordle(arquivo_lexico="lexico.txt", tamanho=5, tentativas=6)
        self.tentativa_atual = 0
        self.letra_atual = 0

        # Cores do Wordle
        self.cor_certa = "#538d4e"      # Verde - letra certa no lugar certo
        self.cor_presente = "#b59f3b"   # Amarelo - letra certa no lugar errado
        self.cor_errada = "#3a3a3c"     # Cinza escuro - letra não está na palavra
        self.cor_vazia = "#121213"      # Preto - célula vazia
        self.cor_borda = "#3a3a3c"      # Cinza escuro - borda das células
        
        self.criar_interface()

    def criar_interface(self):
        #Título
        titulo = tk.Label(self.root, text="Wordle", font=("Arial", 32, "bold"), bg="#121213", fg="white")
        titulo.pack(pady=20)

        # Frame para o grid de letras
        self.frame_grid = tk.Frame(self.root, bg="#121213")
        self.frame_grid.pack(pady=10)

        # Criar grid de células
        self.celulas = []
        for i in range(self.jogo.tentativas):
            linha = []
            for j in range(self.jogo.tamanho):
                celula = tk.Label(self.frame_grid, text="", font=("Arial", 24, "bold"),
                                  width=3, height=1, bg=self.cor_vazia, fg="white",
                                  relief="solid", borderwidth=2, bd=2,
                                  highlightbackground=self.cor_borda,
                                  highlightthickness=2)
                celula.grid(row=i, column=j, padx=5, pady=5)
                linha.append(celula)
            self.celulas.append(linha)

        # Entry para input de teclas
        self.entry = tk.Entry(self.root, bg="#121213", fg="white", insertbackground="white", font=("Arial", 1))

        self.entry.place(width=0, height=0)
        self.entry.focus()

        # Botão de novo jogo
        self.btn_novo = tk.Button(self.root, text="Novo Jogo", font=("Arial", 12),
                                  command=self.novo_jogo, bg="#538d4e", fg="white",
                                  activebackground="#6aaa64", activeforeground="white")
        self.btn_novo.pack(pady=10)

        # Bind de teclas
        self.root.bind("<Key>", self.tecla_pressionada)

    def tecla_pressionada(self, event):
        if self.tentativa_atual >= self.jogo.tentativas:
            return None
        
        tecla = event.char.lower()

        # Backspace
        if event.keysym == "BackSpace":
            if self.letra_atual > 0:
                self.letra_atual -= 1
                self.celulas[self.tentativa_atual][self.letra_atual].config(text="")

        # Enter
        elif event.keysym == "Return":
            self.verificar_palavra()
        
        # Letras
        elif tecla.isalpha() and self.letra_atual < self.jogo.tamanho:
            self.celulas[self.tentativa_atual][self.letra_atual].config(text=tecla.upper())
            self.letra_atual += 1
        
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
        
        # Obter feedback
        feedback = self.jogo.feedback_chute(palavra_simplificada)

        for i in range(self.jogo.tamanho):
            if feedback[i] == "C":
                cor = self.cor_certa
            elif feedback[i] == "A":
                cor = self.cor_presente
            else:
                cor = self.cor_errada

            self.celulas[self.tentativa_atual][i].config(bg=cor)

        # Verifica vitória
        if feedback == "C" * self.jogo.tamanho:
            print("Parabéns! Você ganhou!")
            self.tentativa_atual = self.jogo.tentativas # Bloqueia tentativas
            return

        # Próxima tentativa
        self.tentativa_atual += 1
        self.letra_atual = 0

        # Verificar derrota
        if self.tentativa_atual >= self.jogo.tentativas:
            print(f"Você perdeu! A palavra era {self.jogo.palavra_escolhida}")

    def novo_jogo(self):
        # Reinicia o jogo
        self.jogo = Wordle(self.jogo.arquivo_lexico, self.jogo.tamanho, self.jogo.tentativas)
        self.tentativa_atual = 0
        self.letra_atual = 0

        # Limpar todas as células
        for i in range(self.jogo.tentativas):
            for j in range(self.jogo.tamanho):
                self.celulas[i][j].config(text="", bg=self.cor_vazia)

root = tk.Tk()

app = WordleGUI(root)

root.mainloop()
