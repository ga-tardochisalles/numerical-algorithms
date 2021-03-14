'''
Lab 4 Implementação de GAUSS (ex1 aula)
Gabriel Tardochi Salles , TIA = 41822730
'''


#Recebe a matriz com as esquacoes e a quantidade de incognitas do problema
def GAUSS(matriz, incog):
    global complexidade
    v = [0] * incog
    for i in range(incog-1, -1, -1):
        if i < incog - 1:
            j = i + 1
            while j < incog:
                matriz[i][incog] = matriz[i][incog] - matriz[i][j]
                complexidade += 1
                j = j + 1
        v[i] = matriz[i][incog]/matriz[i][i]
        complexidade += 1
        k = i - 1
        while k != -1:
            matriz[k][i] = matriz[k][i] * v[i]
            complexidade += 1
            k = k-1
    return v


# --------MAIN---------- #

complexidade = 0
#testes com dois exemplos
matriz = [[1, 1, 0, 3, 4],
          [0,-1,-1,-5,-7],
          [0, 0, 3,13,13],
          [0, 0, 0,-13,-13]]
incog = 4
print(GAUSS(matriz,incog),"passos para",incog,"incognitas: ",complexidade)

complexidade = 0
matriz2 = [[-1, 1, 0, 2],
          [0,-2,-2,-10],
          [0, 0, 2,  4]]
incog2 = 3
print(GAUSS(matriz2,incog2),"passos para",incog2,"incognitas: ",complexidade)
print ("Algoritmo de complexidade O(n^2)")





