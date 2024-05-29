import sys

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
        print("1-Subconjunto proprio\n2-União\n3-Diferença\n4-Interseçao \n5-Voltar")
        op = int(input("Digite sua opção:\n"))
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
        print("1 - Função de 1º grau\n2 - ...\n3 - ...\n4 - Voltar")
        op = int(input("Digite sua opção:\n"))
        if op == 4:
            break
        if op < 1 or op > 4:
            print("Opção inválida...")
            continue
        else:
            if op == 1:
                func_1()
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

def func_1():
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    x = int(input("Digite o valor de x: "))
    y = a * x + b
    print(f"O resultado da função de 1º grau é: {y}")

menu_principal()
