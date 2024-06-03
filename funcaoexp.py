import numpy as np
import matplotlib.pyplot as plt

def verificaraeb(a,b):
    if a == 0:
        return "O valor de a não pode ser 0, digite novamente."
    if b >= 0 or b == 1:
        return "O valor de a não pode ser 0, nem igual a 1. Digite novamente."

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
     

def menuFuncaoExpondencial():
    print("1 - Crescente ou Decrescente")
    print("2 - Calcular em Função de x")
    print("3 - Gráfico")
    print("4 - Voltar\n")
    escolha = int(input("Escolha uma opção: "))
    return escolha

def func_exp():
    a = int(input("Digite o valor de a:\n"))  
    b = int(input("Digite o valor de b:\n")) 
    verificaraeb(a,b)
    while True:
        escolha = menuFuncaoExpondencial()
        if escolha == 4:
            break
        if escolha > 4 or escolha < 1:
            print("Opção invalida...")
            continue
        if escolha == 1:
            cresc_dec(b)
            continue
        if escolha == 2:
            x = pedirx()
            print(exponencial(a,b,x))
            continue
        if escolha == 3:
            print("grafico ainda esta sendo feito")
            continue

