def gerar_lista():
    with open("lexico.txt", "r", encoding="utf-8") as lexico:
        palavras = [palavra.strip() for palavra in lexico]

    return palavras

def simplifica_lista(listaPalavra):
    listaSimplificada = []
    for palavra in listaPalavra:
        listaSimplificada.append(simplifica_palavra(palavra))
    return listaSimplificada

def jogar():
    listaPalavra = gerar_lista()
    listaSimplificada = simplifica_lista(listaPalavra)
    print(listaPalavra)
    print(listaSimplificada)

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

jogar()
