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
    
    return novaString

def escolher_palavra(listaPalavra, tamanho):
    return rd.choice([palavra for palavra in listaPalavra if len(palavra) == tamanho])

def jogar():
    listaPalavra = gerar_lista()
    listaSimplificada = simplifica_lista(listaPalavra)

    tamanho = 5
    palavraEscolhida = escolher_palavra(listaPalavra, tamanho)

jogar()
