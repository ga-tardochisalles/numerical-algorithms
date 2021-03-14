'''
Lab 4 Implementação de PIVOTAMENTO
Gabriel Tardochi Salles , TIA = 41822730
'''

# Recebe a matriz com as equacoes e quantidades de incognitas do problema
def PIVOTAMENTO(matriz, inc):

    # Acha o pivo para cada passo da diagonal  e faz a substituicao
    def arrumarpivo(lin):
        maiorEl= 0
        linhaPiv = lin

        # procurando maior valor absoluto na coluna
        for k in range(lin, inc):
            if abs(matriz[k][lin]) > maiorEl:
                maiorEl = abs(matriz[k][k])
                linhaPiv = k

        # trocando linhas de lugar (colocando linha pivo no lugar correto)
        for column in range(inc + 1):
            aux = matriz[lin][column]
            matriz[lin][column] = matriz[linhaPiv][column]
            matriz[linhaPiv][column] = aux

    # zerando colunas abaixo da diagonal, coluna por coluna da esqrd -> dir
    for row in range(inc):
        if matriz[row][row] == 0:
            arrumarpivo(row)
        # se o pivo for 0 nao é possivel resolver
        if matriz[row][row] == 0:
            print("Sem solucao.")
            return -1
        # se esta na ultima linha, finalizou o pivotamento
        if row == inc-1:
            return matriz
        # cria as novas linhas a partir do pivo
        for i in range(row + 1, incog):
            const = matriz[i][row] / matriz[row][row]
            for col in range(incog + 1):
                matriz[i][col] = matriz[i][col] - (const * matriz[row][col])
    return matriz


# ------------MAIN------------ #
entrada = [[0, 8, 2, -7],
          [ 3, 5, 2,  8],
          [ 6, 2, 8, 26]]
incog = 3
print("Matriz teste1: ")
for m in range(incog):
    print(entrada[m])
mat = PIVOTAMENTO(entrada, incog)
print("Matriz teste1 apos algoritmo de pivotamento: ")
for linha in range(incog):
    print(mat[linha])

entrada = [[1, -1, 2,-1, -8],
          [ 2, -2, 3,-3,-20],
          [ 1, 1, 1,  0, -2],
          [ 1,-1, 4,  3,  4]]
incog = 4
print("\nMatriz teste2: ")
for p in range(incog):
    print(entrada[p])
mat = PIVOTAMENTO(entrada,incog)
print("Matriz teste2 apos algoritmo de pivotamento: ")
for n in range(incog):
    print(mat[n])