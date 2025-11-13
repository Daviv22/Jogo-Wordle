class Wordle:
    def __init__(self, arquivo_lexico, tamanho=5, tentativas=6):
        self.arquivo_lexico = arquivo_lexico
        self.tamanho = tamanho
        self.tentativas = tentativas
        self.lista_palavras = self.gerar_lista()
        self.lista_simplificada = self.simplifica_lista(self.lista_palavras)
        self.palavra_escolhida = self.escolher_palavra()
        self.palavra_simplificada = self.simplifica_palavra(self.palavra_escolhida)