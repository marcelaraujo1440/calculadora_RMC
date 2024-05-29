#função de um algoritimo simples de criação de matriz
def retornodematriz (linhas, colunas):
    matriz = []
    for i in range(linhas):
        linhas = []
        for j in range(colunas):
            elemento = int(input(f"Digite aqui os elementos da sua matriz:\n"))
            linhas.append(elemento)

        matriz.append(linhas)
    return matriz

#função de imprimir matriz ja criada
def printmatriz (matriz):
    for linha in matriz:
        print(linha)

#função para verificar se a matriz é quadrada ex. 2x2 ou 3x3
def verMatQuad (matriz):
    num_linhas = len(matriz) #check numero de linhas
    for linha in matriz: #check numero de colunas
        if len(linha) != num_linhas:
            return False
    return True

        
#função para calcular um determinante
def calcdet(matriz):
    if not verMatQuad(matriz):
        return "A matriz não é quadrada. O determinante não pode ser calculado." #usando a verificação da matriz quadrada
    
    size = len(matriz) #check de tamanho da função
    
    if size == 1:
        return matriz[0][0] #caso a matriz seja de tamanho 1x1 retornar a propria matriz

    if size == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0] #caso a matriz seja de ordem 2x2

    det = 0
    for j in range(size): #caso a matriz seja de outro tamanho 
        submatrix = [linha[:j] + linha[j+1:] for linha in matriz[1:]] 
        det += (-1) ** j * matriz[0][j] * calcdet(submatrix)


    return det, "A matriz é quadrada!"

#função para realizar multiplicações entre matrizes
def multiMatriz(matrizA, matrizB):
    if len(matrizA[0]) != len(matrizB): #check se numero de linhas é == numero de colunas
        return f"O numero de linhas da 1° matriz deve ser igual ao numero de colunas da 2° matriz"
    ordemResultado = [
        [0 for _ in range(len(matrizB[0]))] for _ in range(len(matrizA)) #criando a matriz com o size da matriz resultado porem preenchida com 0
    ] 

    for i in range(len(matrizA)): #linhas da matrizA
        for j in range(len(matrizB[0])): #colunas da matrizB
            for k in range(len(matrizB)): #soma dos produtos da i da matrizA e das j da matrizB
                ordemResultado[i][j] += matrizA[i][k] * matrizB[k][j]    

    return "essa multiplicação é possivel!", printmatriz(ordemResultado) #retorno da matriz resultado que antes estava preenchidas com os 0's agora preenchida com o calculo feito no 3° loop for     

def transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    matrizTransposta = [
        [0 for _ in range (linhas)] for _ in range (colunas) #criação de uma matriz transposta prechida com 0's trocando colunas por linhas e linhas por colunas
    ]
    #agora vamos preencher a nossa matriz transposta com os numeros da nossa matriz principal
    for i in range(linhas):
        for j in range(colunas):
            matrizTransposta[j][i] = matriz[i][j]

    return matrizTransposta
