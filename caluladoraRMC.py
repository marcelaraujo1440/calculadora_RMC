import sys
import numpy as np
import math
import matplotlib.pyplot as plt
def traco():
    print(50*"-")
def menu_principal():
    while True:
        print("1 - Conjuntos\n2 - Funções\n3 - Matrizes\n4 - Sair")
        op = int(input("Digite sua opção:\n"))
        if op == 4:
            print("Encerrando...")
            sys.exit()
        if op < 1 or op > 4:
            print("Opção inválida...")
            continue
        else:
            if op == 1:
                menu_conjuntos()
            elif op == 2:
                menu_funcoes()
            elif op == 3:
                menu_matrizes()

def menu_conjuntos():
    while True:
        print("Menu Conjuntos")
        print("1 - Subconjunto proprio\n2 - União\n3 - Diferença\n4 - Interseçao \n5 - Voltar")
        op = int(input("Digite sua opção:\n"))
        traco()
        if op == 5:
            break
        if op < 1 or op > 4:
            print("Opção inválida...")
            continue
        else:
            if op == 1:
                print(subconjunto_proprio())
            elif op == 2:
                print(conjunto_uniao())
            elif op == 3:
                print(diferença())
            elif op == 4:
                print(interseçao())


def subconjunto_proprio():
    A=[]
    B=[]
    
    elementosA=int(input("Qual a quantidade de elementos que você deseja no conjunto A: "))
    elementosB=int(input("Qual a quantidade de elementos que você deseja no conjunto B: "))
    
    for i in range(elementosA):
        a = int(input("Digite um número para o conjunto A: \n"))
        A.append(a)
    
    for i in range(elementosB):
        b = int(input("Digite um número para o conjunto B: \n"))  
        B.append(b)
        #analisa se O conjunto A esta todo em B e se o conjunto B é diferente de A
        verficacao = all(elem in B for elem in A) and set(A) != set(B)
    
    if verficacao:
        return "\nA é subconjunto próprio de B\n"
    else:
        return "\nA não é subconjunto próprio de B\n"
        
     
def conjunto_uniao():
    A = []
    B = []
    #uniao de A com B 
    for i in range(5):
        a = int(input("Digite um número para o conjunto A: \n"))
        A.append(a)
    for i in range(5):
        b = int(input("Digite um número para o conjunto B: \n"))  
        B.append(b)
    operacao = set(A) | set(B) 
    return operacao


def  diferença():
    A = []
    B = []
    #diferença de A e B 
    for i in range(5):
        a = int(input("Digite um número para o conjunto A: \n"))
        A.append(a)
    for i in range(5):
        b = int(input("Digite um número para o conjunto B: \n"))  
        B.append(b)
    operacao = set(A) - set(B) 
    return operacao


def  interseçao():
    A = []
    B = []
    #se existe algum elemento igual entre os 2
    for i in range(5):
        a = int(input("Digite um número para o conjunto A: \n"))
        A.append(a)
    for i in range(5):
        b = int(input("Digite um número para o conjunto B: \n"))  
        B.append(b)
    operacao = set(A) & set(B) 
    return operacao


def menu_funcoes():
    while True:
        print("Menu Funções")
        print("1 - Função de 2º grau\n2 - Funções exponenciais\n3 -\n4 - Voltar")
        op = int(input("Digite sua opção:\n"))
        if op == 4:
            break
        if op < 1 or op > 4:
            print("Opção inválida...")
            continue
        else:
            if op == 1:
                print(func_2())
            elif op == 2:
                print("Chamar a função que faz a opção 2")
            elif op == 3:
                print("Chamar a função que faz a opção 3")

def menu_matrizes():
    while True:
        print("Menu Matrizes")
        print("1 - ...\n2 - ...\n3 - ...\n4 - Voltar")
        op = int(input("Digite sua opção:\n"))
        if op == 4:
            break
        if op < 1 or op > 4:
            print("Opção inválida...")
            continue
        else:
            if op == 1:
                print("Chamar a função que faz a opção 1")
            elif op == 2:
                print("Chamar a função que faz a opção 2")
            elif op == 3:
                print("Chamar a função que faz a opção 3")


def func_2():
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    traco()

    if a == 0:
        traco()
        return "O 'a' não pode ser zero! "
        
    delta = b**2 - 4*a*c

    if delta < 0:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-delta) / (2*a)
        traco()
        print(f"As raízes são complexas: {parte_real:.2f} + {parte_imaginaria:.2f}i e {parte_real:.2f} - {parte_imaginaria:.2f}i\n")
    elif delta == 0:
        raiz = -b / (2*a)
        traco()
        print(f"A raiz é {raiz:.2f}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        traco()
        print(f"As raízes são {raiz1:.2f} e {raiz2:.2f}")
        # gerar valores do eixo x e do eixo y do gráfico
        eixo_X = np.linspace(-10, 10, 400)
        eixo_Y = a * eixo_X**2 + b * eixo_X + c
        
        #formulas para gerar os vertices das funcoes
        x_v=-b/2*a
        y_v=delta/4*a
     
        if x_v >0:
            traco()
            print("É o ponto minimo") 
            print(f"O vértice da parábola é ({x_v:.2f}, {y_v:.2f})")
            traco()
        elif x_v<0:
            traco()
            print("É o ponto maximo") 
            print(f"O vértice da parábola é ({x_v:.2f}, {y_v:.2f})")
            traco()
        
            plt.plot(eixo_X, eixo_Y, label=f'{a}x^2 + {b}x + {c}')
            plt.scatter(x_v, y_v, color='red', zorder=5)  # Adiciona o vértice no gráfico
            plt.text(x_v, y_v, f'({x_v:.2f}, {y_v:.2f})', fontsize=12, verticalalignment='bottom')  # Adiciona texto ao vértice
            plt.title("Função do 2º Grau")
            plt.xlabel("Eixo x")
            plt.ylabel("Eixo y")
            plt.grid(True)
            plt.axvline(x=0, color="k")
            plt.axhline(y=0, color="k")
            plt.legend()  # Adiciona a legenda ao gráfico
            plt.show()
    
    #para calcular em funcao do x
    traco()
    x = float(input("Digite um valor para x: "))
    #pega os mesmos numeros ja escolhidos pelo usuario la no começo
    y = a * x**2 + b * x + c
    traco()
    return f"O valor de f({x}) é {y:.2f}/n{traco()}"


  


 
menu_principal()