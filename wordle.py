import random as rd

class Wordle:
    def __init__(self, arquivo_lexico, tamanho=5, tentativas=6):
        self.arquivo_lexico = arquivo_lexico
        self.tamanho = tamanho
        self.tentativas = tentativas
        self.lista_palavras = self._gerar_lista()
        self.lista_simplificada = self._simplifica_lista(self.lista_palavras)
        self.palavra_escolhida = self._escolher_palavra()
        self.palavra_simplificada = self._simplifica_palavra(self.palavra_escolhida)

    # Método para gerar a lista
    def _gerar_lista(self):
        with open(self.arquivo_lexico, "r", encoding="utf-8") as lexico:
            palavras = [palavra.strip() for palavra in lexico]

        return palavras
    
    # Método para simplificar palavras (remove acentos e cedilha)
    def _simplifica_palavra(self, palavraDaLista):
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
    def _simplifica_lista(self, listaPalavra):
        listaSimplificada = []
        for palavra in listaPalavra:
            listaSimplificada.append(self._simplifica_palavra(palavra))
        return listaSimplificada
    
    # Método para escolher uma palavra aleatória
    def _escolher_palavra(self):
        return rd.choice([palavra for palavra in self.lista_palavras if len(palavra) == self.tamanho])
    
    # Método para verificar se o chute do jogador é válido
    def verifica_chute(self, chute):
        if chute in self.lista_simplificada and len(chute) == self.tamanho:
            return True
        else:
            return False
        
    # Método qpara retornar feedback sobre o chute (o que acertou, errou)
    def feedback_chute(self, chute):

        # Realiza a contagem de cada letra na palavra escolhida
        contagem = {}
        for letra in self.palavra_simplificada:
            contagem[letra] = contagem.get(letra, 0) + 1

        stringFeedback = [""] * self.tamanho

        # Marca as letras na posição certa
        for i in range(self.tamanho):
            if chute[i] == self.palavra_simplificada[i]:
                stringFeedback[i] = "C"
                contagem[chute[i]] -= 1
        
        # Marca letras certas na posição errada
        for i in range(self.tamanho):
            if stringFeedback[i] != "":
                continue

            if chute[i] in self.palavra_simplificada and contagem[chute[i]] > 0:
                stringFeedback[i] = "A"
                contagem[chute[i]] -= 1
            else:
                stringFeedback[i] = "E"
        
        return "".join(stringFeedback)


"""

jogo = Wordle("lexico.txt", tamanho=5, tentativas=8)
jogo.jogar()"""