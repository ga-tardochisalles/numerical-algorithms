'''
Lab 6 Implementação do Algoritmo de BISSECÇÃO
Gabriel Tardochi Salles , TIA = 41822730
'''

# Algoritmo de Bisseccao, recebe as extremidades da busca da raiz(x), n maximo de iteracoes, o epsilon e a funcao
def Bisseccao(ai,bi,n,e,f):
    # variaveis iniciais da primeira iteracao, com estando exatamente entre a e b
    k = 1
    a = ai
    b = bi
    p = (a + b)/2
    # enquanto nao atingir maximo n de iteracoes
    while (k <= n):
        k += 1
        fa = f(a)
        fp = f(p)
        # se a f(p) estiver abaixo de epsilon estabelecido, solucao foi encontrada
        if abs(fp) <= e:
            return p
        # se o produto de f(a) por f(p) for negativo, a solucao estara entre a e p
        elif fa * fp < 0:
            b = p
            p = (a + b)/2
        # se o produto de f(a) por f(p) for positivo, a solucao estara entre p e b
        else:
            a = p
            p = (a + b)/2
    # estouro de limite n iteracoes
    return 'iteracoes máximas atingidas'


# descobre entre os inteiros, o melhor par a,b inicial de uma funcao fnc para procurarmos a raiz entre eles
def acharABi(fnc):
    ai = 0
    bi = 0
    if fnc(ai) < 0:
        # incrementa bi até chegar em um b inicial onde f(b) > 0, entao o ai será bi - 1
        while True:
            if fnc(bi) > 0:
                ai = bi - 1
                break
            else:
                bi += 1
    elif fnc(ai) > 0:
        # decrementa ai até chegar em um a inicial onde f(a) < 0, entao o bi será ai + 1
        while True:
            if fnc(ai) < 0:
                bi = ai + 1
                break
            else:
                ai -= 1
    return ai,bi

# ------------MAIN------------ #

def ex4(x):
    return x**3 + 4*x**2 - 10

ai, bi = acharABi(ex4)
n = 6
e = 0.1
print("Rodando o algoritmo de Bisseccao chegamos em", Bisseccao(ai,bi,n,e,ex4),", com n maximo =", n,"e epsilon =", e)



