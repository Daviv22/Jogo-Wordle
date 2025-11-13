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
    
    # Método para verificar se o chute do jogador é válido
    def verifica_chute(self, chute):
        if chute in self.lista_simplificada and len(chute) == self.tamanho:
            return True
        else:
            return False
        
    # Método qpara retornar feedback sobre o chute (o que acertou, errou)
    def feedback_chute(self, chute):
        stringFeedback = [""]
        for i in range(self.tamanho):
            if chute[i] == self.palavra_simplificada:
                stringFeedback.append("C")
            elif chute[i] in self.palavra_simplificada[i]:
                stringFeedback.append("A")
            else:
                stringFeedback.append("E")
        
        return "".join(stringFeedback)
    
    def jogar(self):
        """Controla o loop principal do jogo."""
        print(f"Bem-vindo ao Wordle! Adivinhe a palavra de {self.tamanho} letras.")
        tentativas_restantes = self.tentativas

        while tentativas_restantes > 0:
            chute = input("Digite uma palavra: ").lower()
            if not self.verifica_chute(chute):
                print("Chute inválido! Tente novamente.")
                continue

            feedback = self.feedback_chute(chute)
            print(feedback)
            print(chute.upper())
            tentativas_restantes -= 1
            print(f"Tentativas restantes: {tentativas_restantes}\n")

            if feedback == "C" * self.tamanho:
                print("🎉 Parabéns! Você acertou a palavra!")
                break
        else:
            print(f"Você perdeu! A palavra era: {self.palavra_escolhida.upper()}")


jogo = Wordle("lexico.txt", tamanho=5, tentativas=8)
jogo.jogar()