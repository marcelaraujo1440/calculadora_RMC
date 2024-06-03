import numpy as np
import matplotlib.pyplot as plt

def pedir_valores():
    while True:
        a = int(input(f"Digite um valor para a:\n"))
        b = int(input(f"Digite um valor para b:\n"))
        if a == 0:
            print("O valor de a não pode ser 0, digite novamente.")
            continue
        elif b >= 0 or b == 1:
            print("O valor de a não pode ser 0, nem igual a 1. Digite novamente.")
            continue
        else:
            return a, b

def cresc_dec(b):
    if b > 1:
        print(f"A função é crescente")
    else:
        print(f"A função é decrescente")

def pedirx ():
    x = float(input(f"Digite aqui o valor de X:\n"))
    return x

def exponencial (a, b, x):
    f = a*b**x
    return f

def grafico ():  #não esta pronto!!!!
    
    x = exponencial()
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'f(x) = {a} * {b}^x')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title('Gráfico da Função Exponencial')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
     

