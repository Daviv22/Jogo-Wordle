import random as rd

class Wordle:
    def __init__(self, arquivo_lexico, tamanho=5, tentativas=6):
        self.arquivo_lexico = arquivo_lexico
        self.tamanho = tamanho
        self.tentativas = tentativas
        self.lista_palavras = self.gerar_lista()
        self.lista_simplificada = self.simplifica_lista(self.lista_palavras)
        self.palavra_escolhida = self.escolher_palavra()
        self.palavra_simplificada = self.simplifica_palavra(self.palavra_escolhida)

    # Método para gerar a lista
    def gerar_lista(self):
        with open("lexico.txt", "r", encoding="utf-8") as lexico:
            palavras = [palavra.strip() for palavra in lexico]

        return palavras
    
    # Método para simplificar palavras (remove acentos e cedilha)
    def simplifica_palavra(self, palavraDaLista):
        novaString = ""
        for c in palavraDaLista:
            if c in ['á', 'ã', 'â']:
                novaString += 'a'
            elif c in ['é', 'ê']:
                novaString += 'e'
            elif c in ['ó', 'õ', 'ô']:
                novaString += 'o'
            elif c == 'ú':
                novaString += 'u'
            elif c == 'ç':
                novaString += 'c'
            else:
                novaString += c    
        
        return novaString.lower()
    
    # Método para simplificar a lista inteira
    def simplifica_lista(self, listaPalavra):
        listaSimplificada = []
        for palavra in listaPalavra:
            listaSimplificada.append(self.simplifica_palavra(palavra))
        return listaSimplificada
    
    # Método para escolher uma palavra aleatória
    def escolher_palavra(self):
        return rd.choice([palavra for palavra in self.lista_palavras if len(palavra) == self.tamanho])