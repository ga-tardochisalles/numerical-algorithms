'''
Lab 4 Implementação de JACOBI
Gabriel Tardochi Salles , TIA = 41822730
'''

# Implementacao do Algoritmo de Jacobi Iterativamente
def JACOBI(incog, n, mat, sol_ini, e):
    comp = 0
    # percorrendo e trocando linhas qnd a[i][i] eh zero
    for i in range(incog):
        if mat[i][i] == 0:
            for j in range(i+1, incog):
                if mat[j][i] != 0:
                    for k in range(incog+1):
                        aux = mat[i][k]
                        mat[i][k] = mat[j][k]
                        mat[j][k] = aux
                    break
            #se mesmo trocando linhas de lugar nao houver solucao retorna -1
            if mat[i][i] == 0:
                print("Nao tem solucao.")
                return -1
    # isolando incognitas na matriz
    for i in range(incog):
        div = mat[i][i]
        for j in range(incog+1):
            mat[i][j] = mat[i][j]/div
        for k in range(incog):
            mat[i][k] = mat[i][k] * -1
        mat[i][i] = 0
    # gerando novas solucoes a partir da s.i passada como argumento
    antiga = sol_ini.copy()
    nova = sol_ini.copy()
    k = 1
    while True:
        k += 1
        # gerando nova solucao
        for i in range(incog):
            x = 0
            for j in range(incog):
                comp += 1
                x = x + (mat[i][j] * antiga[j])
            x += mat[i][incog]
            comp += 1
            nova[i] = x
        maxdif = 0.0
        val = 1.0
        # calculando coeficiente e verificando se foi atingida a tolerancia minima
        for i in range(len(antiga)):
            x = abs(nova[i] - antiga[i])
            comp += 1
            if x > maxdif:
                maxdif = x
                if nova[i] != 0:
                    val = abs(nova[i])
        if maxdif/val < e:
            print("Tolerancia minima",e,"foi atingida, solucao encontrada com K = ",k,"\nTempo de execucao: ",comp)
            return nova
        antiga = nova.copy()
    print("Maximo de iteracoes n atingido, solucao atual: ")
    return nova

# ------------------------ MAIN -------------------------- #
entrada = [[10, -1,  2, 0, 6],
          [ -1, 11, -1, 3, 25],
          [  2, -1, 10,-1,-11],
          [  0,  3, -1, 8, 15]]
incog = 4
solIni = [0,0,0,0]
coef = 0.1

print("Resolucao da matriz de equacoes ")
for m in range(incog):
    print(entrada[m])
print(JACOBI(4,100,entrada,solIni,coef))