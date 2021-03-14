'''
Lab 7 Implementação do Método de Newton
Gabriel Tardochi Salles , TIA = 41822730
'''

# Metodo de Newton, recebe p0, funcao f, derivada fd de f, tolerancia tol, e N máximo de iteracoes permitidas ao algoritmo
def Newton(p0, f, fd, tol, n):
    k = 1
    pa = p0
    while(k<=n):
        p = pa - (f(pa)/fd(pa))
        if abs(p-pa) < tol:
            return print("Rodando o metodo de Newton chegamos em raiz =", p,"com tolerancia =", tol,"e numero de iteracoes =", k)
        k += 1
        pa = p
    return print("O método falhou após",n,"iteracoes !")

# ------------MAIN------------ #


