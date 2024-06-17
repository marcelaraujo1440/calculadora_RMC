import PySimpleGUI as sg
import numpy as np
import pandas as pd
import os

# Configurações de tema e fonte
sg.theme('DarkTeal2')

# Nome do arquivo CSV para armazenar o histórico
historico_CSV = 'historico.csv'

# Função para criar o arquivo CSV se não existir
def criar_arquivo_csv():
    if not os.path.exists(historico_CSV):
        df = pd.DataFrame(columns=['Usuario', 'Operacao', 'Resultado'])
        df.to_csv(historico_CSV, index=False)

# Função para adicionar uma entrada no histórico
def adicionar_ao_historico(usuario, operacao, resultado):
    df = pd.read_csv(historico_CSV)
    df = df.append({'Usuario': usuario, 'Operacao': operacao, 'Resultado': resultado}, ignore_index=True)
    df.to_csv(historico_CSV, index=False)

# Função para ler o histórico de um usuário específico
def ler_historico(usuario):
    df = pd.read_csv(historico_CSV)
    historico_usuario = df[df['Usuario'] == usuario]
    return historico_usuario

# Função para criar a janela inicial
def criar_janela_inicial():
    layout = [
        [sg.Text('Olá, seja bem vindo(a) à', justification='center', font=("Bookman Old Style", 20), pad=(0, 20))],
        [sg.Text('"calculadora sinistra"', justification='center', font=('Cooper Black', 24), pad=(0, 20))],
        [sg.Button('INICIAR', size=(15, 1), font=("Courier", 15, 'bold'), pad=(0, 20))],
        [sg.Text('Desenvolvido por Gabriel Carmo e Marcel Araujo, todos os direitos reservados ©', 
                 justification='center', font=("Courier", 10), pad=(0, 60))]
    ]
    return sg.Window('Calculadora Sinistra', layout, size=(500, 450), element_justification='center', finalize=True)

# Função para criar a janela secundária
def criar_janela_secundaria():
    layout = [
        [sg.Text('CALCULADORA SINISTRA', justification='center', font=('Cooper Black', 24), pad=(0, 20))],
        [sg.Text('Escolha uma opção:', justification='center', font=("Bookman Old Style", 20), pad=(0, 20))],
        [sg.Button('Entrar', size=(15, 1), font=("Courier", 15, 'bold')), 
  ],
        [sg.Button('Voltar', size=(15, 1), font=("Courier", 15, 'bold'), pad=(0, 20))],
        
    ]
    return sg.Window('Calculadora Sinistra', layout, size=(500, 450), element_justification='center', finalize=True)

# Função para criar a janela de login
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

# Função para criar a janela de opções
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

# Função para criar a janela da calculadora básica
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

# Função para criar a janela da calculadora de matrizes
def janela_matriz():
    layout = [
        [sg.Text('Calculadora de Matrizes', font=('Cooper Black', 24))],
        [sg.Text('Matriz A', font=('Bookman Old Style', 15))],
        [sg.Text('Número de linhas:', size=(15, 1)), sg.InputText(key='-linhasA-', size=(5, 1))],
        [sg.Text('Número de colunas:', size=(15, 1)), sg.InputText(key='-colunasA-', size=(5, 1))],
        [sg.Text('Matriz B', font=('Bookman Old Style', 15))],
        [sg.Text('Número de linhas:', size=(15, 1)), sg.InputText(key='-linhasB-', size=(5, 1))],
        [sg.Text('Número de colunas:', size=(15, 1)), sg.InputText(key='-colunasB-', size=(5, 1))],
        [sg.Button('Definir Matrizes')],
        [sg.Button('Voltar', size=(15, 1), font=('Courier', 15, 'bold'), pad=(10, 20))]
    ]
    return sg.Window('Calculadora de Matrizes', layout, finalize=True)

# Função para criar a janela das matrizes com os campos para inserção de valores
def janela_matriz_valores(linhasA, colunasA, linhasB, colunasB):
    layout = [
        [sg.Text('Preencha os valores das matrizes:', font=('Cooper Black', 20))],
        [sg.Frame('Matriz A', [
            [sg.InputText(size=(5, 1), key=f'A-{i}-{j}') for j in range(colunasA)] for i in range(linhasA)
        ])],
        [sg.Frame('Matriz B', [
            [sg.InputText(size=(5, 1), key=f'B-{i}-{j}') for j in range(colunasB)] for i in range(linhasB)
        ])],
        [sg.Button('Multiplicar Matrizes')],
        [sg.Button('Voltar', size=(15, 1), font=('Courier', 15, 'bold'), pad=(10, 20))]
    ]
    return sg.Window('Valores das Matrizes', layout, finalize=True)

# Função para pegar os valores das matrizes da janela
def pegar_valores_matriz(window, linhas, colunas, prefixo):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            try:
                valor = float(window[f'{prefixo}-{i}-{j}'].get())
                linha.append(valor)
            except ValueError:
                sg.popup_error('Por favor, insira apenas números nas matrizes.')
                return None
        matriz.append(linha)
    return np.array(matriz)

# Função para criar a janela do histórico
def janela_historico(usuario):
    historico = ler_historico(usuario)
    layout = [
        [sg.Text(f'Histórico de {usuario}', font=('Cooper Black', 20), justification='center')],
        [sg.Table(values=historico.values.tolist(),
                  headings=historico.columns.tolist(),
                  display_row_numbers=True,
                  auto_size_columns=False,
                  col_widths=[15, 20, 20],
                  justification='center',
                  key='-HISTORICO-')],
        [sg.Button('Voltar', size=(15, 1), font=("Courier", 15, 'bold'), pad=(10, 20))]
    ]
    return sg.Window('Histórico', layout, size=(600, 400), element_justification='center', finalize=True)

# Iniciar criação do arquivo de histórico
criar_arquivo_csv()

# Variáveis iniciais
usuario_atual = None

# Criar janela inicial
janela1, janela2, janela3, janela4, janela5, janela6, janela7, janela8 = criar_janela_inicial(), None, None, None, None, None, None, None

while True:
    window, event, values = sg.read_all_windows()
    
    if event == sg.WIN_CLOSED:
        window.close()
        if window == janela1:
            break
        elif window == janela2:
            janela2 = None
        elif window == janela3:
            janela3 = None
        elif window == janela4:
            janela4 = None
        elif window == janela5:
            janela5 = None
        elif window == janela6:
            janela6 = None
        elif window == janela7:
            janela7 = None
        elif window == janela8:
            janela8 = None

    if window == janela1 and event == 'INICIAR':
        janela2 = criar_janela_secundaria()
        janela1.close()
        janela1 = None

    if window == janela2 and event == 'Entrar':
        janela3 = janela_entrar()
        janela2.close()
        janela2 = None

    if window == janela3 and event == 'Enviar':
        usuario_atual = values['-USUARIO-']
        sg.popup(f'Bem-vindo(a), {usuario_atual}!')
        janela4 = janela_op()
        janela3.close()
        janela3 = None

    if window == janela3 and event == 'Voltar':
        janela2 = criar_janela_secundaria()
        janela3.close()
        janela3 = None
        
    if window == janela2 and event == 'Voltar':
        janela1 = criar_janela_inicial()
        janela2.close()
        janela2 = None
        
    if window == janela4 and event == 'Voltar':
        janela3 = janela_entrar()
        janela4.close()
        janela4 = None

    if window == janela4 and event == 'Conjuntos':
        # Lógica para a calculadora de conjuntos
        pass

    if window == janela4 and event == 'Matrizes':
        janela5 = janela_matriz()
        janela4.close()
        janela4 = None

    if window == janela4 and event == 'Funções':
        # Lógica para a calculadora de funções
        pass

    if window == janela4 and event == 'Raiz Quadrada':
        # Lógica para a calculadora de raiz quadrada
        pass

    if window == janela4 and event == 'Fatorial':
        # Lógica para a calculadora de fatorial
        pass

    if window == janela4 and event == 'Operações Básicas':
        janela6 = janela_calculadorabasica()
        janela4.close()
        janela4 = None

    if window == janela4 and event == 'Histórico':
        janela7 = janela_historico(usuario_atual)
        janela4.close()
        janela4 = None
        
    if window == janela5 and event == 'Definir Matrizes':
        linhasA = int(values['-linhasA-'])
        colunasA = int(values['-colunasA-'])
        linhasB = int(values['-linhasB-'])
        colunasB = int(values['-colunasB-'])
        janela8 = janela_matriz_valores(linhasA, colunasA, linhasB, colunasB)
        janela5.close()
        janela5 = None
        
    if window == janela8 and event == 'Multiplicar Matrizes':
        matriz_a = pegar_valores_matriz(window, linhasA, colunasA, 'A')
        matriz_b = pegar_valores_matriz(window, linhasB, colunasB, 'B')
        if matriz_a is not None and matriz_b is not None:
            try:
                resultado = np.dot(matriz_a, matriz_b)
                sg.popup('Resultado da multiplicação:', resultado)
                adicionar_ao_historico(usuario_atual, 'Multiplicação de Matrizes', str(resultado))
            except ValueError:
                sg.popup_error('Erro na multiplicação. Verifique as dimensões das matrizes.')

    if window == janela8 and event == 'Voltar':
        janela5 = janela_matriz()
        janela8.close()
        janela8 = None

    if window == janela7 and event == 'Voltar':
        janela4 = janela_op()
        janela7.close()
        janela7 = None

    if window == janela6:
        if event in '1234567890':
            window['-VALOR-'].update(values['-VALOR-'] + event)
        elif event == '-PONTO-':
            window['-VALOR-'].update(values['-VALOR-'] + '.')
        elif event == '-OPOSTO-':
            if values['-VALOR-']:
                window['-VALOR-'].update(str(-float(values['-VALOR-'])))
        elif event == '-LIMPAR-':
            window['-VALOR-'].update(values['-VALOR-'][:-1])
        elif event == '-LIMPARTD-':
            window['-VALOR-'].update('')
        elif event in ['-MAIS-', '-MENOS-', '-MULTI-', '-DIV-']:
            operador = event
            valor1 = values['-VALOR-']
            window['-VALOR-'].update('')
        elif event == '-RESULTADO-':
            valor2 = values['-VALOR-']
            try:
                if operador == '-MAIS-':
                    resultado = float(valor1) + float(valor2)
                elif operador == '-MENOS-':
                    resultado = float(valor1) - float(valor2)
                elif operador == '-MULTI-':
                    resultado = float(valor1) * float(valor2)
                elif operador == '-DIV-':
                    resultado = float(valor1) / float(valor2)
                window['-VALOR-'].update(resultado)
                adicionar_ao_historico(usuario_atual, f'Operação Básica ({operador})', str(resultado))
            except Exception as e:
                sg.popup_error('Erro na operação:', e)

        elif event == 'Voltar':
            janela4 = janela_op()
            janela6.close()
            janela6 = None
