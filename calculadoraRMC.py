import sys
import numpy as np
import matplotlib.pyplot as plt
from matriz import *
from conjuntos import *
from funcao2grau import *

from funcaoexp import *



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
        print("1 - Subconjunto proprio\n2 - União\n3 - Diferença\n4 - Intersecçao \n5 - Voltar")
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



def menu_funcoes():
    while True:
        print("Menu Funções")
        print("1 - Função de 2º grau\n2 - Funções exponenciais\n3 - Voltar")
        op = int(input("Digite sua opção:\n"))
        if op == 3:
            break
        if op < 1 or op > 3:
            print("Opção inválida...")
            continue
        else:
            if op == 1:
                print(func_2())
            elif op == 2:
                print(pedir_valores())
         

def menu_matrizes():
    while True:
        print("Menu Matrizes")
        print("1 - Calcular determinante\n2 - Multiplicação de matrizes\n3 - Matriz transposta\n4 - Voltar")
        op = int(input("Digite sua opção:\n"))
        if op == 4:
            break
        if op < 1 or op > 4:
            print("Opção inválida...")
            continue
        else:
            if op == 1:
                i = int(input(f"Digite aqui o numero de linhas da sua matriz:\n"))
                j = int(input(f"Digite aqui o numero de colunas da sua matriz:\n"))
                matriz = retornodematriz(i,j)
                printmatriz(matriz)
                print(calcdet(matriz))
            elif op == 2:
                a = int(input(f"Digite aqui o numero de linhas da matriz 1\n"))
                b = int(input(f"Digite aqui o numero de colunas da matriz 1\n"))

                c = int(input(f"Digite aqui o numero de linhas da matriz 2\n"))
                d = int(input(f"Digite aqui o numero de colunas da matriz 2\n"))
                matriz1 = retornodematriz(a,b)
                printmatriz(matriz1)

                matriz2 = retornodematriz(c,d)
                printmatriz(matriz2)
                print(multiMatriz(matriz1, matriz2))
            elif op == 3:
                i = int(input(f"Digite aqui o numero de linhas da sua matriz:\n"))
                j = int(input(f"Digite aqui o numero de colunas da sua matriz:\n"))
                matriz = retornodematriz(i,j)
                printmatriz(matriz)
                printmatriz(transposta(matriz))


 
menu_principal()