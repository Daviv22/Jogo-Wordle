def gerar_lista():
    with open("lexico.txt", "r", encoding="utf-8") as lexico:
        palavras = [palavra.strip() for palavra in lexico]

    return palavras