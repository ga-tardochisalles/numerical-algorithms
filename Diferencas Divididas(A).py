'''
Lab 9 Implementação de Diferencas Divididas de Newton
Gabriel Tardochi Salles , TIA = 41822730
'''

# calcula uma diferenca dividida
def calcularDifDiv(a,b):
    menor_x = a[0]
    maior_x = b[1]
    val = (b[2] - a[2])/(maior_x - menor_x)
    return menor_x, maior_x, val

# funcao do metodo
def difDivididas(v):
    # n = quantidade de pares (x,f(x)) para aplicar o metodo
    n = len(v)
    # vet q armazera o resultado dos termos independentes
    vet_termos = [v[0][2]]
    # n - 1 é o numero de novas colunas na tabela depois do input dado
    for k in range(n-1):
        vet_novo = []
        # percorrendo e calculando elemento da coluna
        for i in range(len(v)-1):
            vet_novo.append(calcularDifDiv(v[i], v[i+1]))
        v = vet_novo.copy()
        # armazenando o termo resultante daquela coluna (primeiro termo)
        vet_termos.append(v[0][2])
    print("Termos serao:", str(vet_termos)[1:-1])

# ------------MAIN------------ #

# para cada elemento X do vetor input: X[0] = menor xi dos seus antepassados na tabela dele,
# X[1] = maior xi dos seus antepassados na tabela dele, X[2] = f() dele
vet = [(-2,-2,1), (-1,-1,4), (0,0,11), (1,1,16), (2,2,13), (3,3,-4)]
difDivididas(vet)
