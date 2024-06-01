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

