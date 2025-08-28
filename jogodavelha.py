

linhas = [1,2,3]
colunas = [1,2,3]

tabuleiro = {
    1: {1: ' ', 2: ' ', 3: ' '},
    2: {1: ' ', 2: ' ', 3: ' '},
    3: {1: ' ', 2: ' ', 3: ' '}
}

def mostrar_tabuleiro():
    print("   1     2     3")
    print("1  {} | {}   | {}  |".format(tabuleiro[1][1], tabuleiro[1][2], tabuleiro[1][3]))
    print("  ----------------")
    print("2  {} | {}   | {}  |".format(tabuleiro[2][1], tabuleiro[2][2], tabuleiro[2][3]))
    print("  ----------------")
    print("3  {} | {}   | {}  |".format(tabuleiro[3][1], tabuleiro[3][2], tabuleiro[3][3]))

def escolher_jogada(jogador , linha, coluna):
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        return True  # jogada válida, mesmo sem vitória
    else:
        print("Jogada inválida! Tente novamente.")
        return False


def limpar_tabuleiro():
    for linha in linhas:
        for coluna in colunas:
            tabuleiro[linha][coluna] = ' '

def verificar_vitoria(jogador):
    # Verifica linhas
    for linha in linhas:
        if tabuleiro[linha][1] == tabuleiro[linha][2] == tabuleiro[linha][3] == jogador:
            return True

    # Verifica colunas
    for coluna in colunas:
        if tabuleiro[1][coluna] == tabuleiro[2][coluna] == tabuleiro[3][coluna] == jogador:
            return True

    # Verifica diagonais
    if tabuleiro[1][1] == tabuleiro[2][2] == tabuleiro[3][3] == jogador:
        return True
    if tabuleiro[1][3] == tabuleiro[2][2] == tabuleiro[3][1] == jogador:
        return True

    return False

print("---------------Jogo da Velha---------------")
mostrar_tabuleiro()
print("---------Escolha-----Sua---Jogada----------")
print("---------x---------------------------0-----")



jogador = 'x'  # Começa com 'x'

while True:
    print(f"Vez do jogador: {jogador}")
    linha = int(input("Digite a linha (1, 2 ou 3): "))
    coluna = int(input("Digite a coluna (1, 2 ou 3): "))

    if linha not in linhas or coluna not in colunas:
        print("Coordenadas inválidas! Escolha entre 1, 2 ou 3.")
        continue

    if escolher_jogada(jogador, linha, coluna):
        mostrar_tabuleiro()
        if verificar_vitoria(jogador):
            print(f"Jogador {jogador} venceu!")
            break  # agora está no lugar certo!
        jogador = '0' if jogador == 'x' else 'x'
limpar_tabuleiro()