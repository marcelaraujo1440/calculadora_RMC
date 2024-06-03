import numpy as np
import math
import matplotlib.pyplot as plt

def traco():
    print(50*"-")

def func_2():
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    verificacao(a, b, c)
    traco()
    
    
def verificacao(a, b, c):
    if a == 0:
        traco()
        print("O 'a' não pode ser zero!")
    else:
        delta = calculo_delta(a, b, c)
        verficacao_delta(delta, a, b, c)
        
def calculo_delta(a, b, c):     
    return b**2 - 4*a*c
    
def verficacao_delta(delta, a, b, c):
    
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
        
        while True:
            deseja_grafico = input("Deseja gerar o gráfico dessa função?\n1 - Sim\n2 - Não\n: ")
            if deseja_grafico == "1":
                gerar_grafico(a, b, c, delta)
                break
            elif deseja_grafico == "2":
                break
            else:
                print("Tente com uma opção válida!")
        calcular_f(a, b, c)
            
        
    
    
def gerar_grafico(a, b, c, delta):  
    
        # gerar valores do eixo x e do eixo y do gráfico
        eixo_X = np.linspace(-10, 10, 400)
        eixo_Y = a * eixo_X**2 + b * eixo_X + c
        
        # fórmulas para gerar os vértices das funções
        x_v = -b / (2*a)
        y_v = -delta / (4*a)
     
        if a > 0:
            traco()
            print("É o ponto mínimo") 
            print(f"O vértice da parábola é ({x_v:.2f}, {y_v:.2f})")
            traco()
        else:
            traco()
            print("É o ponto máximo") 
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
    
   
traco()
 # para calcular em função do x   f(x)
def calcular_f(a, b, c):
    x = float(input("Digite um valor para x: "))
    
    # pega os mesmos números já escolhidos pelo usuário lá no começo
    y = a * x**2 + b * x + c
    
    traco()
    
    print(f"O valor de f({x}) é {y:.2f}")
