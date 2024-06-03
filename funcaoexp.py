import numpy as np
import matplotlib.pyplot as plt

def verificaraeb(a, b):
    if a == 0:
        return "O valor de a não pode ser 0, digite novamente."
    if b <= 0 or b == 1:
        return "O valor de b não pode ser 0, negativo, nem igual a 1. Digite novamente."
    return None

def cresc_dec(b):
    if b > 1:
        print(f"A função é crescente")
    else:
        print(f"A função é decrescente")

def pedirx():
    x = float(input("Digite aqui o valor de X:\n"))
    return x

def exponencial(a, b, x):
    f = a * b ** x
    return f

def grafico(a, b):
    x_vals = np.linspace(-10, 10, 400)
    y_vals = a * b ** x_vals

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {a} * {b}^x')
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
    a = float(input("Digite o valor de a:\n"))  
    b = float(input("Digite o valor de b:\n")) 
    erro = verificaraeb(a, b)
    if erro:
        print(erro)
        return
    
    while True:
        escolha = menuFuncaoExpondencial()
        if escolha == 4:
            break
        if escolha > 4 or escolha < 1:
            print("Opção inválida...")
            continue
        if escolha == 1:
            cresc_dec(b)
            continue
        if escolha == 2:
            x = pedirx()
            print(f"f({x}) = {exponencial(a, b, x)}")
            continue
        if escolha == 3:
            grafico(a, b)
            continue

