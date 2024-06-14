import PySimpleGUI as sg
import numpy as np

# Configurações de tema e fonte 
sg.theme('DarkTeal2')

def create_matrix_layout(rows, cols, matrix_num):
    layout = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(sg.Input(size=(5, 1), key=f'M{matrix_num}_r{i}c{j}'))
        layout.append(row)
    return layout

def get_matrix_values(window, rows, cols, matrix_num):
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
                [sg.InputText(key='-USUARIO-', size=(30, 1), enable_events=True)]
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
        [sg.InputText(key='-ROWS_A-', size=(5, 1)), sg.InputText(key='-COLS_A-', size=(5, 1))],
        [sg.Button("Criar Matriz A")],
        [sg.Text("Número de linhas e colunas da Matriz B:", font=("Courier", 15))],
        [sg.InputText(key='-ROWS_B-', size=(5, 1)), sg.InputText(key='-COLS_B-', size=(5, 1))],
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
matrix_a_created, matrix_b_created = False, False
rows_a, cols_a, rows_b, cols_b = 0, 0, 0, 0

while True:
    window, event, values = sg.read_all_windows()
    
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break

    if window == janela2 and event == sg.WINDOW_CLOSED:
        break

    if window == janela3 and event == sg.WINDOW_CLOSED:
        break

    if window == janela4 and event == sg.WINDOW_CLOSED:
        break

    if window == janela5 and event == sg.WINDOW_CLOSED:
        break

    if window == janela6 and event == sg.WINDOW_CLOSED:
        break

    if window == janela7 and event == sg.WINDOW_CLOSED:
        break
    
    if window == janela1 and event == 'INICIAR':
        janela1.hide()
        janela2 = criar_janela_secundaria()
    
    if window == janela2 and event == 'Entrar':
        janela2.hide()
        janela4 = janela_entrar()

    #if window == janela2 and event == 'Cadastre-se':
      #  janela2.hide()
       # janela3 = janela_Cadastro()

    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela2.un_hide()
    
    if window == janela4 and event == 'Voltar':
        janela4.hide()
        janela2.un_hide()

    if window == janela4 and event == 'Enviar':
        # Aqui você pode implementar a lógica de verificação de login
        janela4.hide()
        janela5 = janela_op()

    if window == janela3 and event == 'Enviar':
        # Aqui você pode implementar a lógica de cadastro
        sg.popup('Cadastro realizado com sucesso!')
        janela3.hide()
        janela2.un_hide()

    if window == janela5 and event == 'Voltar':
        janela5.hide()
        janela4.un_hide()
    
    if window == janela5 and event == "Operações Básicas":
        janela5.hide()
        janela6 = janela_calculadorabasica()
        
    if window == janela6 and event == "Voltar":
        janela6.hide()
        janela5.un_hide()

    if window == janela5 and event == "Matrizes":
        janela5.hide()
        janela7 = janela_matriz()
    
    if window == janela7 and event == "Voltar":
        janela7.hide()
        janela5.un_hide()

    if window == janela7 and event == "Criar Matriz A":
        rows_a, cols_a = int(values['-ROWS_A-']), int(values['-COLS_A-'])
        window['-MATRIZ_A-'].update(visible=True)
        window.extend_layout(window['-MATRIZ_A-'], create_matrix_layout(rows_a, cols_a, 1))
        matrix_a_created = True

    if window == janela7 and event == "Criar Matriz B":
        rows_b, cols_b = int(values['-ROWS_B-']), int(values['-COLS_B-'])
        window['-MATRIZ_B-'].update(visible=True)
        window.extend_layout(window['-MATRIZ_B-'], create_matrix_layout(rows_b, cols_b, 2))
        matrix_b_created = True

    if window == janela7 and event == "Somar Matrizes" and matrix_a_created and matrix_b_created:
        matrix_a = get_matrix_values(window, rows_a, cols_a, 1)
        matrix_b = get_matrix_values(window, rows_b, cols_b, 2)
        if matrix_a is not None and matrix_b is not None:
            if matrix_a.shape == matrix_b.shape:
                result = matrix_a + matrix_b
                window['-RESULTADO-'].update(result)
            else:
                sg.popup_error("As matrizes devem ter o mesmo tamanho para serem somadas.")

    if window == janela7 and event == "Multiplicar Matrizes" and matrix_a_created and matrix_b_created:
        matrix_a = get_matrix_values(window, rows_a, cols_a, 1)
        matrix_b = get_matrix_values(window, rows_b, cols_b, 2)
        if matrix_a is not None and matrix_b is not None:
            if cols_a == rows_b:
                result = np.dot(matrix_a, matrix_b)
                window['-RESULTADO-'].update(result)
            else:
                sg.popup_error("O número de colunas da Matriz A deve ser igual ao número de linhas da Matriz B.")

    if window == janela7 and event == "Determinante Matriz A" and matrix_a_created:
        matrix_a = get_matrix_values(window, rows_a, cols_a, 1)
        if matrix_a is not None:
            if rows_a == cols_a:
                det_a = np.linalg.det(matrix_a)
                window['-RESULTADO-'].update(f'Determinante da Matriz A: {det_a}')
            else:
                sg.popup_error("A Matriz A deve ser quadrada para calcular o determinante.")

    if window == janela7 and event == "Determinante Matriz B" and matrix_b_created:
        matrix_b = get_matrix_values(window, rows_b, cols_b, 2)
        if matrix_b is not None:
            if rows_b == cols_b:
                det_b = np.linalg.det(matrix_b)
                window['-RESULTADO-'].update(f'Determinante da Matriz B: {det_b}')
            else:
                sg.popup_error("A Matriz B deve ser quadrada para calcular o determinante.")

    if window == janela7 and event == "Transposta Matriz A" and matrix_a_created:
        matrix_a = get_matrix_values(window, rows_a, cols_a, 1)
        if matrix_a is not None:
            trans_a = np.transpose(matrix_a)
            window['-RESULTADO-'].update(f'Transposta da Matriz A:\n{trans_a}')

    if window == janela7 and event == "Transposta Matriz B" and matrix_b_created:
        matrix_b = get_matrix_values(window, rows_b, cols_b, 2)
        if matrix_b is not None:
            trans_b = np.transpose(matrix_b)
            window['-RESULTADO-'].update(f'Transposta da Matriz B:\n{trans_b}')

window.close()
