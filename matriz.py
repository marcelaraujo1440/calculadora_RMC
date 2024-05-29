def retornodematriz (linhas, colunas):
    matriz = []
    for i in range(linhas):
        linhas = []
        for j in range(colunas):
            elemento = int(input(f"Digite aqui os elementos da sua matriz:\n"))
            linhas.append(elemento)

        matriz.append(linhas)
    return matriz

def printmatriz (matriz):
    for linha in matriz:
        print(linha)

i = int(input(f"Digite aqui o numero de linhas da sua matriz:\n"))
j = int(input(f"Digite aqui o numero de colunas da sua matriz:\n"))

matriz = retornodematriz(i,j)
printmatriz(matriz)


def verMatQuad (matriz):
    num_linhas = len(matriz)
    for linha in matriz:
        if len(linha) != num_linhas:
            return False
    return True

        

def calcdet(matriz):
    if not verMatQuad(matriz):
        return "A matriz não é quadrada. O determinante não pode ser calculado."
    
    size = len(matriz)
    
    if size == 1:
        return matriz[0][0]

    if size == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    det = 0
    for j in range(size):
        submatrix = [linha[:j] + linha[j+1:] for linha in matriz[1:]] 
        det += (-1) ** j * matriz[0][j] * calcdet(submatrix)

    return det


print(calcdet(matriz))
