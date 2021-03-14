'''
Lista de Ex 10 - Metodo MMQ
Gabriel Tardochi Salles , TIA = 41822730
'''

class Ponto:
    def __init__(self, i, x, y):
        self.i = i
        self.x = x
        self.y = y
        self.x_quadrado = x ** 2
        self.xy = x * y

def MMQ(pontos_dict):
    sum_x = sum([ponto.x for ponto in pontos_dict.values()])
    sum_y = sum([ponto.y for ponto in pontos_dict.values()])
    sum_x_quadrado = sum([ponto.x_quadrado for ponto in pontos_dict.values()])
    sum_xy = sum([ponto.xy for ponto in pontos_dict.values()])
    m = len(pontos_dict.keys())
    a0 = ((sum_x_quadrado*sum_y)-(sum_xy*sum_x))/((m*sum_x_quadrado) - (sum_x**2))
    a1 = ((m*sum_xy)-(sum_x*sum_y))/((m*sum_x_quadrado) - (sum_x**2))
    print(sum_x, sum_y, sum_x_quadrado, sum_xy)
    print("Eq Reta: P(x) = (", a1, ")x + (", a0, ")", sep='')
    print("Com a0 =", a0, " e a1 =", a1)


# --------MAIN---------- #
n = int(input("Numero de pontos? "))
p_dict = {}
for i in range(n):
    x, y = [float(x) for x in input("Digite o par x y separado somente por espaco: ").split()]
    p_dict[i] = Ponto(i, x, y)
for p in p_dict.values():
    print(p.i, p.x, p.y, p.x_quadrado, p.xy)
MMQ(p_dict)



