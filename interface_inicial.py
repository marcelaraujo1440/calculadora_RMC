import PySimpleGUI as sg
import numpy as np

# Configurações de tema e fonte 
sg.theme('DarkTeal2')

def criar_layout_matriz(rows, cols, matrix_num):
    layout = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(sg.Input(size=(5, 1), key=f'M{matrix_num}_r{i}c{j}'))
        layout.append(row)
    return layout

def pegar_valores_matriz(window, rows, cols, matrix_num):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = window[f'M{matrix_num}_r{i}c{j}'].get()
            if value.replace('.', '', 1).isdigit() or (value.startswith('-') and value[1:].replace('.', '', 1).isdigit()):
                row.append(float(value))
            else:
                sg.popup_error(f"Valor inválido na matriz {matrix_num}, posição ({i},{j}).")
                return None
        matrix.append(row)
    return np.array(matrix)

def criar_janela_inicial():
    layout = [
        [sg.Text('Olá, seja bem vindo(a) à', justification='center', font=("Bookman Old Style", 20), pad=(0, 20))],
        [sg.Text('"calculadora sinistra"', justification='center', font=('Cooper Black', 24), pad=(0, 20))],
        [sg.Button('INICIAR', size=(15, 1), font=("Courier", 15, 'bold'), pad=(0, 20))],
        [sg.Text('Desenvolvido por Gabriel Carmo e Marcel Araujo, todos os direitos reservados ©', 
                 justification='center', font=("Courier, 10"), pad=(0, 60))]
    ]
    return sg.Window('Calculadora Sinistra', layout, size=(500, 450), element_justification='center', finalize=True)

def criar_janela_secundaria():
    layout = [
        [sg.Text('CALCULADORA SINISTRA', justification='center', font=('Cooper Black', 24), pad=(0, 20))],
        [sg.Text('Escolha uma opção:', justification='center', font=("Bookman Old Style", 20), pad=(0, 20))],
        [sg.Button('Entrar', size=(15, 1), font=("Courier", 15, 'bold')), 
  ],
        [sg.Button('Voltar', size=(15, 1), font=("Courier", 15, 'bold'), pad=(0, 20))],
        
    ]
    return sg.Window('Calculadora Sinistra', layout, size=(500, 450), element_justification='center', finalize=True)



def janela_entrar():
    layout = [
        [sg.Text('CALCULADORA SINISTRA', justification='center', size=(50, 1), font=('Cooper Black', 24), pad=(0, 20))],
        [sg.Text('Entrar', justification='center', size=(50, 1), font=("Bookman Old Style", 20), pad=(20, 20))],
        [sg.Column([
            [sg.Frame(layout=[
                [sg.Text('Nome de usuário')],
                [sg.InputText(key='-USUARIO-', size=(30, 1))]
            ], title='', pad=(0, 10))],
           [ ],
        ], justification='center')],
        [sg.Button('Enviar', size=(15, 1),pad=(10,20)), sg.Button('Voltar', size=(15, 1), pad=(10, 20))]
    ]
    return sg.Window('Entrar', layout, size=(500, 450),element_justification='center', finalize=True)

def janela_op():
    layout=[

            [sg.Text("CALCULADORA SINISTRA", justification='center', font=("Bookman Old Style", 20), pad=(0, 20)),],
            [sg.Text("Escolha a sua operação!",justification='center', font=( "Bookman Old Style",15), pad=(0, 20))],
            [sg.Button("Conjuntos", size=(15, 1), font=("Courier", 15, 'bold')), sg.Button("Matrizes", size=(15, 1), font=("Courier", 15, 'bold'))],
            [sg.Button("Funções",size=(15, 1), font=("Courier", 15, 'bold')), sg.Button("Raiz Quadrada",size=(15, 1), font=("Courier", 15, 'bold'))],
            [sg.Button("Fatorial",size=(15, 1), font=("Courier", 15, 'bold')), sg.Button("Operações Básicas",size=(15, 1), font=("Courier", 15, 'bold'))],
            [sg.Button("Histórico",size=(15, 1), font=("Courier", 15, 'bold'))],
            
        ]
    return sg.Window('Calculadora Sinistra', layout, size=(500, 450), element_justification='center', finalize=True)

def janela_calculadorabasica():

    col_1 =[ #coluna 3
       [sg.Button('1',size=(8,2),font="bold", pad=(5,15)),sg.Button('2',size=(8,2),font="bold",pad=(5,15)),sg.Button('3',size=(8,2),font="bold",pad=(5,15))],
       [sg.Button('4',size=(8,2),font="bold", pad=(5,15)),sg.Button('5',size=(8,2),font="bold", pad=(5,15)),sg.Button('6',size=(8,2),font="bold", pad=(5,15))],
       [sg.Button('7',size=(8,2),font="bold", pad=(5,15)),sg.Button('8',size=(8,2),font="bold", pad=(5,15)),sg.Button('9',size=(8,2),font="bold", pad=(5,15))],
       [sg.Button('+/-',size=(8,2),font="bold",key="-OPOSTO-", pad=(5,15)),sg.Button('0',size=(8,2),font="bold", pad=(5,15)),sg.Button('.',size=(8,2),font="bold",key="-PONTO-", pad=(5,15))],
       [sg.Button("Voltar",size=(32,2))]
    ]
    col_2 = [ #coluna 2
        [sg.B('*',size=(8,4),key="-MULTI-",font="bold")],
        [sg.B('-',size=(8,4),key="-MENOS-",font="bold")],
        [sg.B('+',size=(8,9),key="-MAIS-",font="bold")],
        ]
    
    col_3 = [ #coluna 3
        [sg.Button('/',size=(8,2),key="-DIV-",font="bold")],
        [sg.Button('-->',size=(8,2),key="-LIMPAR-",font="bold")],
        [sg.Button('CE',size=(8,4),key="-LIMPARTD-",font="bold")],
        [sg.Button('=',size=(8,8),key="-RESULTADO-",font="bold")],
        ]

    layout = [
        [sg.Input(key='-VALOR-',size=(31,3),justification='right',font="bold")],
        [sg.Column(col_1), sg.Column(col_2), sg.Column(col_3)]
    ]

    return sg.Window('Calculadora Básica', layout, finalize=True)

def janela_matriz():
    layout = [
        [sg.Text("Calculadora de Matrizes",font=("Bookman Old Style", 20) , justification='center')],
        [sg.Text("Número de linhas e colunas da Matriz A:", font=("Bookman Old Style", 15) )],
        [sg.InputText(key='-linhaA-', size=(5, 1)), sg.InputText(key='-colunasA-', size=(5, 1))],
        [sg.Button("Criar Matriz A")],
        [sg.Text("Número de linhas e colunas da Matriz B:", font=("Courier", 15))],
        [sg.InputText(key='-linhaB-', size=(5, 1)), sg.InputText(key='-colunasB-', size=(5, 1))],
        [sg.Button("Criar Matriz B")],
        [sg.Frame("Matriz A", [[sg.Column([[]], key='-MATRIZ_A-')]]), 
         sg.Frame("Matriz B", [[sg.Column([[]], key='-MATRIZ_B-')]])],
        [sg.Button("Somar Matrizes"), sg.Button("Multiplicar Matrizes")],
        [sg.Button("Determinante Matriz A"), sg.Button("Determinante Matriz B")],
        [sg.Button("Transposta Matriz A"), sg.Button("Transposta Matriz B")],
        [sg.Text("Resultado:", font=("Courier", 15))],
        [sg.Multiline(key='-RESULTADO-', size=(40, 10), disabled=True)],
        [sg.Button("Voltar")]
    ]
    return sg.Window('Calculadora de Matrizes', layout, finalize=True)

# Criar janelas iniciais
janela1, janela2, janela3, janela4, janela5, janela6, janela7 = criar_janela_inicial(), None, None, None, None, None, None

# Variáveis de controle
matriz_a_cria, matriz_b_cria = False, False
linhaA, colunasA, linhaB, colunasB = 0, 0, 0, 0

while True:
    window, evento, valores = sg.read_all_windows()
    
    if window == janela1 and evento == sg.WINDOW_CLOSED:
        break

    if window == janela2 and evento == sg.WINDOW_CLOSED:
        break

    if window == janela3 and evento == sg.WINDOW_CLOSED:
        break

    if window == janela4 and evento == sg.WINDOW_CLOSED:
        break

    if window == janela5 and evento == sg.WINDOW_CLOSED:
        break

    if window == janela6 and evento == sg.WINDOW_CLOSED:
        break

    if window == janela7 and evento == sg.WINDOW_CLOSED:
        break
    
    if window == janela1 and evento == 'INICIAR':
        janela1.hide()
        janela2 = criar_janela_secundaria()
    
    if window == janela2 and evento == 'Entrar':
        janela2.hide()
        janela4 = janela_entrar()

    #if window == janela2 and evento == 'Cadastre-se':
      #  janela2.hide()
       # janela3 = janela_Cadastro()

    if window == janela2 and evento == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela3 and evento == 'Voltar':
        janela3.hide()
        janela2.un_hide()
    
    if window == janela4 and evento == 'Voltar':
        janela4.hide()
        janela2.un_hide()

    if window == janela4 and evento == 'Enviar':
        # Aqui você pode implementar a lógica de verificação de login
        janela4.hide()
        janela5 = janela_op()

    if window == janela3 and evento == 'Enviar':
        # Aqui você pode implementar a lógica de cadastro
        sg.popup('Cadastro realizado com sucesso!')
        janela3.hide()
        janela2.un_hide()

    if window == janela5 and evento == 'Voltar':
        janela5.hide()
        janela4.un_hide()
    
    if window == janela5 and evento == "Operações Básicas":
        janela5.hide()
        janela6 = janela_calculadorabasica()
        
    if window == janela6 and evento == "Voltar":
        janela6.hide()
        janela5.un_hide()

    if window == janela5 and evento == "Matrizes":
        janela5.hide()
        janela7 = janela_matriz()
    
    if window == janela7 and evento == "Voltar":
        janela7.hide()
        janela5.un_hide()

    if window == janela7 and evento == "Criar Matriz A":
        linhaA, colunasA = int(valores['-linhaA-']), int(valores['-colunasA-'])
        window['-MATRIZ_A-'].update(visible=True)
        window.extend_layout(window['-MATRIZ_A-'], criar_layout_matriz(linhaA, colunasA, 1))
        matriz_a_cria = True

    if window == janela7 and evento == "Criar Matriz B":
        linhaB, colunasB = int(valores['-linhaB-']), int(valores['-colunasB-'])
        window['-MATRIZ_B-'].update(visible=True)
        window.extend_layout(window['-MATRIZ_B-'], criar_layout_matriz(linhaB, colunasB, 2))
        matriz_b_cria = True

    if window == janela7 and evento == "Somar Matrizes" and matriz_a_cria and matriz_b_cria:
        matriz_a = pegar_valores_matriz(window, linhaA, colunasA, 1)
        matriz_b = pegar_valores_matriz(window, linhaB, colunasB, 2)
        if matriz_a is not None and matriz_b is not None:
            if matriz_a.shape == matriz_b.shape:
                result = matriz_a + matriz_b
                window['-RESULTADO-'].update(result)
            else:
                sg.popup_error("As matrizes devem ter o mesmo tamanho para serem somadas.")

    if window == janela7 and evento == "Multiplicar Matrizes" and matriz_a_cria and matriz_b_cria:
        matriz_a = pegar_valores_matriz(window, linhaA, colunasA, 1)
        matriz_b = pegar_valores_matriz(window, linhaB, colunasB, 2)
        if matriz_a is not None and matriz_b is not None:
            if colunasA == linhaB:
                result = np.dot(matriz_a, matriz_b)
                window['-RESULTADO-'].update(result)
            else:
                sg.popup_error("O número de colunas da Matriz A deve ser igual ao número de linhas da Matriz B.")

    if window == janela7 and evento == "Determinante Matriz A" and matriz_a_cria:
        matriz_a = pegar_valores_matriz(window, linhaA, colunasA, 1)
        if matriz_a is not None:
            if linhaA == colunasA:
                det_a = np.linalg.det(matriz_a)
                window['-RESULTADO-'].update(f'Determinante da Matriz A: {det_a}')
            else:
                sg.popup_error("A Matriz A deve ser quadrada para calcular o determinante.")

    if window == janela7 and evento == "Determinante Matriz B" and matriz_b_cria:
        matriz_b = pegar_valores_matriz(window, linhaB, colunasB, 2)
        if matriz_b is not None:
            if linhaB == colunasB:
                det_b = np.linalg.det(matriz_b)
                window['-RESULTADO-'].update(f'Determinante da Matriz B: {det_b}')
            else:
                sg.popup_error("A Matriz B deve ser quadrada para calcular o determinante.")

    if window == janela7 and evento == "Transposta Matriz A" and matriz_a_cria:
        matriz_a = pegar_valores_matriz(window, linhaA, colunasA, 1)
        if matriz_a is not None:
            trans_a = np.transpose(matriz_a)
            window['-RESULTADO-'].update(f'Transposta da Matriz A:\n{trans_a}')

    if window == janela7 and evento == "Transposta Matriz B" and matriz_b_cria:
        matriz_b = pegar_valores_matriz(window, linhaB, colunasB, 2)
        if matriz_b is not None:
            trans_b = np.transpose(matriz_b)
            window['-RESULTADO-'].update(f'Transposta da Matriz B:\n{trans_b}')

window.close()
