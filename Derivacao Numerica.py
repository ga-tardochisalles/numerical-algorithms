import math

def getFlt(flt):
    flt = str(flt)
    was_neg = False
    if not ("e" in flt):
        return flt[:10]
    if flt.startswith('-'):
        flt = flt[1:]
        was_neg = True
    str_vals = str(flt).split('e')
    coef = float(str_vals[0])
    exp = int(str_vals[1])
    return_val = ''
    if int(exp) > 0:
        return_val += str(coef).replace('.', '')
        return_val += ''.join(['0' for _ in range(0, abs(exp - len(str(coef).split('.')[1])))])
    elif int(exp) < 0:
        return_val += '0.'
        return_val += ''.join(['0' for _ in range(0, abs(exp) - 1)])
        return_val += str(coef).replace('.', '')
    if was_neg:
        return_val='-'+return_val
    return return_val[:11]

def f(x):
    return pow(x, 2) - math.log(x)

def drv_real(x):
    return (2*x)-(1/x)

def calcularad(hs,x0):
    print("adiantada")
    i = 6
    for h in hs:
        if i == 6:
            print("       h   3f(x0) 4f(x0+h)  f(x0+2*h)   f'*(x0)  f'(x0)   erro")
        for k in range(i):
            print(" ", end='')
        i -= 1
        parte1 = 3*f(x0)
        parte2 = 4*f(x0+h)
        parte3 = f(x0 + 2*h)
        flinha_calc = (1/(2*h)) * ((parte2)-(parte1)-(parte3))
        flinha_real = drv_real(x0)
        erro = abs(flinha_real-flinha_calc)/abs(flinha_real)
        print(h,": ",getFlt(parte1),getFlt(parte2),getFlt(parte3),getFlt(flinha_calc),getFlt(flinha_real),getFlt(erro))
        print()

def calcularatr(hs,x0):
    print("atrasada")
    i = 6
    for h in hs:
        if i == 6:
            print("        h      f(x0-2h)  4f(x0-h)  3f(x0) f'*(x0) f'(x0) erro")
        for k in range(i):
            print(" ", end='')
        i -= 1
        h = -1*h
        parte1 = f(x0-2*h)
        parte2 = 4 * f(x0 - h)
        parte3 = 3 * f(x0)
        flinha_calc = (1 / (2 * h)) * ((parte1) + (-1*parte2) + (parte3))
        flinha_real = drv_real(x0)
        erro = abs(flinha_real - flinha_calc) / abs(flinha_real)
        print(h, ": ", getFlt(parte1), getFlt(parte2), getFlt(parte3), getFlt(flinha_calc), getFlt(flinha_real), getFlt(erro))
        print()

def calcularcent(hs,x0):
    print("central")
    i = 6
    for h in hs:
        if i == 6:
            print("        h    f(x0+h)    f(x0-h)    f'*(x0)   f'(x0) erro")
        for k in range(i):
            print(" ", end='')
        i -= 1
        parte1 = f(x0+h)
        parte2 = f(x0-h)
        flinha_calc = (1/(2*h)) * ((parte1)+(-1*parte2))
        flinha_real = drv_real(x0)
        erro = abs(flinha_real-flinha_calc)/abs(flinha_real)
        print(h,": ",getFlt(parte1),getFlt(parte2),getFlt(flinha_calc),getFlt(flinha_real),getFlt(erro))
        print()

h_list = [0.1,0.01,0.001,0.0001]
xzero = 1
calcularad(h_list,xzero)
calcularatr(h_list,xzero)
calcularcent(h_list,xzero)

