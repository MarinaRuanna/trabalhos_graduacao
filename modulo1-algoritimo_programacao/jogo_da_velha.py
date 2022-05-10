from random import randint



def novo_tabuleiro():
    return [0, 0 ,0,
            0, 0, 0,
            0, 0, 0]

def imprimir_tabuleiro(tabuleiro):
    for indice, valor in enumerate(tabuleiro):
        if valor == 0:
            print(" ", indice+1, sep="", end='')
        elif valor == 1:
            print(" x", end='')
        else:
            print(" O", end='')

        if indice == 2 or indice == 5:
            print("\n---+---+---\n", end='')

        elif indice < 8:
            print(" |", end='')

    print('\n')



def receber_jogada(jogador):

    try:
        jogada = int(input(f'Digite a posição a jogar de 1 a 9 jogador {jogador}: '))
        return jogada

    except ValueError:
        print("entrada inválida")
        return -1


def posicao_valida(jogada, tabuleiro):
    if jogada < 1 or jogada > 9:
        print("Posição inválida")
        return False

    if tabuleiro[jogada-1] != 0:
        print("Posição ocupada")
        return False

    return True


def muda_jogador(jogador, jogada, tabuleiro):
    if jogador == "X":
        tabuleiro[jogada-1] = 1
        return "O"

    else:
        tabuleiro[jogada-1] = 2
        return "X"

def verifica_fim_do_jogo(jogadas, tabuleiro):

    # Verifica linhas
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
        if tabuleiro[0] == 1:
            print("Jogador X ganhou!!")
            return 1

        elif tabuleiro[0] == 2:
            print("Jogador O ganhou!!")
            return 2

    if tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
        if tabuleiro[3] == 1:
            print("Jogador X ganhou!!")
            return 1

        elif tabuleiro[3] == 2:
            print("Jogador O ganhou!!")
            return 2

    if tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
        if tabuleiro[6] == 1:
            print("Jogador X ganhou!!")
            return 1

        elif tabuleiro[6] == 2:
            print("Jogador O ganhou!!")
            return 2

    # Verifica colunas
    if tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
        if tabuleiro[0] == 1:
            print("Jogador X ganhou!!")
            return 1

        elif tabuleiro[0] == 2:
            print("Jogador O ganhou!!")
            return 2

    if tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
        if tabuleiro[1] == 1:
            print("Jogador X ganhou!!")
            return 1

        elif tabuleiro[1] == 2:
            print("Jogador O ganhou!!")
            return 2

    if tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
        if tabuleiro[2] == 1:
            print("Jogador X ganhou!!")
            return 1

        elif tabuleiro[2] == 2:
            print("Jogador O ganhou!!")
            return 2

    # Verifica diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
        if tabuleiro[0] == 1:
            print("Jogador X ganhou!!")
            return 1

        elif tabuleiro[0] == 2:
            print("Jogador O ganhou!!")
            return 2

    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
        if tabuleiro[2] == 1:
            print("Jogador X ganhou!!")
            return 1

        elif tabuleiro[2] == 2:
            print("Jogador O ganhou!!")
            return 2

    if jogadas > 9:
        print("Deu velha!")
        return -1
    return 0


def jogador_cpu(jogador):
    jogada = randint(1,9)
    while tabuleiro[jogada-1] != 0:
        jogada = randint(1,9)

    print(f'Digite a posição a jogar de 1 a 9 jogador {jogador}: {jogada}')

    return jogada

tabuleiro = novo_tabuleiro()

jogador = "X"
jogadas = 0

while True:

    imprimir_tabuleiro(tabuleiro)
    if jogador == "X":
        jogada = receber_jogada(jogador)
    else:
        jogada = jogador_cpu(jogador)

    if not posicao_valida(jogada, tabuleiro):
        continue
    jogador = muda_jogador(jogador, jogada, tabuleiro)
    jogadas = jogadas + 1

    if verifica_fim_do_jogo(jogadas, tabuleiro) != 0:
        break


