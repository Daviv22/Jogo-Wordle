from wordle import Wordle

jogo = Wordle("./lexico.txt")

def jogar():
    """Controla o loop principal do jogo."""
    print(f"Bem-vindo ao Wordle! Adivinhe a palavra de {jogo.tamanho} letras.")
    tentativas_restantes = jogo.tentativas

    while tentativas_restantes > 0:
        chute = input("Digite uma palavra: ").lower()
        if not jogo.verifica_chute(chute):
            print("Chute inválido! Tente novamente.")
            continue

        feedback = jogo.feedback_chute(chute)
        print(feedback)
        print(chute.upper())
        tentativas_restantes -= 1
        print(f"Tentativas restantes: {tentativas_restantes}\n")

        if feedback == "C" * jogo.tamanho:
            print("🎉 Parabéns! Você acertou a palavra!")
            break
    else:
        print(f"Você perdeu! A palavra era: {jogo.palavra_escolhida.upper()}")

jogar()