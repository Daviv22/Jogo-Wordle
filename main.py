import random as rd

def gerar_lista():
    with open("lexico.txt", "r", encoding="utf-8") as lexico:
        palavras = [palavra.strip() for palavra in lexico]

    return palavras

def simplifica_lista(listaPalavra):
    listaSimplificada = []
    for palavra in listaPalavra:
        listaSimplificada.append(simplifica_palavra(palavra))
    return listaSimplificada

def simplifica_palavra(palavraDaLista):
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

def escolher_palavra(listaPalavra, tamanho):
    return rd.choice([palavra for palavra in listaPalavra if len(palavra) == tamanho])

def verifica_chute(chute, listaSimplificada, tamanho):
    if chute in listaSimplificada and len(chute) == tamanho:
        return True
    else:
        return False
    
def feedback_chute(chute, palavraSimplificada, tamanho):
    stringFeedback = [""] * tamanho
    for i in range(5):
        if chute[i] not in palavraSimplificada:
            stringFeedback[i] = "E"
        elif chute[i] == palavraSimplificada[i]:
            stringFeedback[i] = "C"
        elif chute[i] != palavraSimplificada[i] and chute[i] in palavraSimplificada:
            stringFeedback[i] = "A"
    
    return "".join(stringFeedback)

            

def jogar():
    listaPalavra = gerar_lista()
    listaSimplificada = simplifica_lista(listaPalavra)

    tamanho = 5
    palavraEscolhida = escolher_palavra(listaPalavra, tamanho)
    palavraSimplificada = simplifica_palavra(palavraEscolhida)

    tentativas = 6

    while tentativas:
        chute = input("Digite uma palavra: ")
        if verifica_chute(chute, listaSimplificada, tamanho):
            feedback = feedback_chute(chute, palavraSimplificada, tamanho)
            tentativas -= 1
            print(feedback)
            print(chute.upper())
            print(tentativas)
            if feedback == "CCCCC":
                print("Parabéns! Você acertou!!")
                break
            else:
                continue
        else:
            print("chute inválido")

jogar()
