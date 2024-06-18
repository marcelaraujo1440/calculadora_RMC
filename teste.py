import PySimpleGUI as sg
import numpy as np
import os
import pandas as pd

# Configurações de tema e fonte 
sg.theme('DarkTeal2')

# Funções para manipulação do arquivo CSV
def inicializar_arquivo_contagem():
    if not os.path.exists('contagem_cliques.csv'):
        df = pd.DataFrame(columns=['Botao', 'Contagem'])
        df.to_csv('contagem_cliques.csv', index=False)

def atualizar_contagem(botao):
    botoes_validos = ['Conjuntos', 'Função', 'Operações Básicas', 'Matrizes']
    if botao in botoes_validos:
        df = pd.read_csv('contagem_cliques.csv')
        if botao in df['Botao'].values:
            df.loc[df['Botao'] == botao, 'Contagem'] += 1
        else:
            df = df._append({'Botao': botao, 'Contagem': 1}, ignore_index=True)
        df.to_csv('contagem_cliques.csv', index=False)

def gerar_relatorio():
    df = pd.read_csv('contagem_cliques.csv')
    relatorio = ""
    for index, row in df.iterrows():
        relatorio += f"{row['Botao']}: {row['Contagem']} vezes\n"
    return relatorio

# Inicializar arquivo de contagem
inicializar_arquivo_contagem()

def criar_layout_matriz(linhas, colunas, matriz_num):
    layout = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(sg.Input(size=(5, 1), key=f'M{matriz_num}_r{i}c{j}'))
        layout.append(linha)
    return layout

def pegar_valores_matriz(window, linhas, colunas, matriz_num):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = window[f'M{matriz_num}_r{i}c{j}'].get()
            if valor.replace('.', '', 1).isdigit() or (valor.startswith('-') and valor[1:].replace('.', '', 1).isdigit()):
                linha.append(float(valor))
            else:
                sg.popup_error(f"Valor inválido na matriz {matriz_num}, posição ({i},{j}).")
                return None
        matriz.append(linha)
    return np.array(matriz)

def criar_janela_inicial():
    layout = [
        [sg.Text('Olá, seja bem vindo(a) à', justification='center', font=("Bookman Old Style", 20), pad=(0, 20))],
        [sg.Text('"calculadora sinistra"', justification='center', font=('Cooper Black', 24), pad=(0, 20))],
        [sg.Button('INICIAR', size=(15, 1), font=("Courier", 15, 'bold'), pad=(0, 20))],
        [sg.Text('Desenvolvido por Gabriel Carmo e Marcel Araujo, todos os direitos reservados ©', 
                 justification='center', font=("Courier", 10), pad=(0, 60))]
    ]
    return sg.Window('Calculadora Sinistra', layout, size=(500, 450), element_justification='center', finalize=True)

def criar_janela_secundaria():
    layout = [
        [sg.Text('CALCULADORA SINISTRA', justification='center', font=('Cooper Black', 24), pad=(0, 20))],
        [sg.Text('Escolha uma opção:', justification='center', font=("Bookman Old Style", 20), pad=(0, 20))],
        [sg.Button('Entrar', size=(15, 1), font=("Courier", 15, 'bold')), 
         sg.Button('Voltar', size=(15, 1), font=("Courier", 15, 'bold'), pad=(0, 20))],
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
            ], title='', pad=(0, 10))]
        ], justification='center')],
        [sg.Button('Enviar', size=(15, 1), pad=(10,20)), sg.Button('Voltar', size=(15, 1), pad=(10, 20))]
    ]
    return sg.Window('Entrar', layout, size=(500, 450), element_justification='center', finalize=True)

def janela_op():
    layout = [
        [sg.Text("CALCULADORA SINISTRA", justification='center', font=("Bookman Old Style", 20), pad=(0, 20))],
        [sg.Text("Escolha a sua operação!", justification='center', font=("Bookman Old Style", 15), pad=(0, 20))],
        [sg.Button("Conjuntos", size=(15, 1), font=("Courier", 15, 'bold')), sg.Button("Matrizes", size=(15, 1), font=("Courier", 15, 'bold'))],
        [sg.Button("Função", size=(15, 1), font=("Courier", 15, 'bold')), sg.Button("Operações Básicas", size=(15, 1), font=("Courier", 15, 'bold'))],
        [sg.Button("Histórico", size=(15, 1), font=("Courier", 15, 'bold'), pad=(10,10))]
    ]
    return sg.Window('Calculadora Sinistra', layout, size=(500, 450), element_justification='center', finalize=True)

def janela_calculadorabasica():
    col_1 = [  # coluna 1
       [sg.Button('1', size=(8, 2), font="bold", pad=(5, 15)), sg.Button('2', size=(8, 2), font="bold", pad=(5, 15)), sg.Button('3', size=(8, 2), font="bold", pad=(5, 15))],
       [sg.Button('4', size=(8, 2), font="bold", pad=(5, 15)), sg.Button('5', size=(8, 2), font="bold", pad=(5, 15)), sg.Button('6', size=(8, 2), font="bold", pad=(5, 15))],
       [sg.Button('7', size=(8, 2), font="bold", pad=(5, 15)), sg.Button('8', size=(8, 2), font="bold", pad=(5, 15)), sg.Button('9', size=(8, 2), font="bold", pad=(5, 15))],
       [sg.Button('+/-', size=(8, 2), font="bold", key="-OPOSTO-", pad=(5, 15)), sg.Button('0', size=(8, 2), font="bold", pad=(5, 15)), sg.Button('.', size=(8, 2), font="bold", key="-PONTO-", pad=(5, 15))],
       [sg.Button("Voltar", size=(32, 2))]
    ]
    col_2 = [  # coluna 2
        [sg.Button('*', size=(8, 4), key="-MULTI-", font="bold")],
        [sg.Button('-', size=(8, 4), key="-MENOS-", font="bold")],
        [sg.Button('+', size=(8, 9), key="-MAIS-", font="bold")]
    ]
    
    col_3 = [  # coluna 3
        [sg.Button('/', size=(8, 2), key="-DIV-", font="bold")],
        [sg.Button('-->', size=(8, 2), key="-LIMPAR-", font="bold")],
        [sg.Button('CE', size=(8, 4), key="-LIMPARTD-", font="bold")],
        [sg.Button('=', size=(8, 8), key="-RESULTADO-", font="bold")]
    ]

    layout = [
        [sg.Input(key='-VALOR-', size=(31, 3), justification='right', font="bold")],
        [sg.Column(col_1), sg.Column(col_2), sg.Column(col_3)]
    ]

    return sg.Window('Calculadora Básica', layout, finalize=True)

def janela_matriz():
    layout = [
        [sg.Text("Calculadora de Matrizes", font=("Bookman Old Style", 25), justification='center')],
        [sg.Text("Número de linhas e colunas da Matriz A:", font=("Bookman Old Style", 15) )],
        [sg.InputText(key='-linhaA-', size=(5, 1)), sg.InputText(key='-colunasA-', size=(5, 1))],
        [sg.Button("Criar Matriz A", size=(20, 1), font=("Bookman Old Style", 10))],
        [sg.Text("Número de linhas e colunas da Matriz B:", font=("Bookman Old Style", 15) )],
        [sg.InputText(key='-linhaB-', size=(5, 1)), sg.InputText(key='-colunasB-', size=(5, 1))],
        [sg.Button("Criar Matriz B", size=(20, 1), font=("Bookman Old Style", 10))],
        [sg.Text('', key='-erro-', text_color='red')],
        [sg.Button("Multiplicar", size=(20, 1), font=("Bookman Old Style", 10)), sg.Button("Voltar", size=(20, 1), font=("Bookman Old Style", 10))]
    ]
    return sg.Window('Calculadora de Matrizes', layout, finalize=True)

def janela_matriz_valores(linhasA, colunasA, linhasB, colunasB):
    layoutA = criar_layout_matriz(linhasA, colunasA, 1)
    layoutB = criar_layout_matriz(linhasB, colunasB, 2)
    layout = [
        [sg.Frame('Matriz A', layoutA, font=("Bookman Old Style", 15))],
        [sg.Frame('Matriz B', layoutB, font=("Bookman Old Style", 15))],
        [sg.Button('Calcular', font=("Bookman Old Style", 10)), sg.Button('Voltar', font=("Bookman Old Style", 10))]
    ]
    return sg.Window('Valores das Matrizes', layout, finalize=True)

# Função de multiplicação de matrizes
def multiplicar_matrizes(A, B):
    return np.dot(A, B)

# Variáveis de controle de janelas
janela1, janela2, janela3, janela4, janela_matriz, janela_matriz_valores, janela_calculadorabasica = criar_janela_inicial(), None, None, None, None, None, None

# Loop principal do PySimpleGUI
while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        window.close()
        if window == janela1:
            break
        continue

    if event == 'INICIAR' and window == janela1:
        janela2 = criar_janela_secundaria()
        janela1.hide()

    if event == 'Voltar':
        if window == janela2:
            janela1.un_hide()
            window.close()
        elif window == janela3:
            janela2.un_hide()
            window.close()
        elif window == janela4:
            janela2.un_hide()
            window.close()
        elif window == janela_calculadorabasica:
            janela4.un_hide()
            window.close()
        elif window == janela_matriz:
            janela4.un_hide()
            window.close()
        elif window == janela_matriz_valores:
            janela_matriz.un_hide()
            window.close()

    if event == 'Entrar' and window == janela2:
        janela3 = janela_entrar()
        janela2.hide()

    if event == 'Enviar' and window == janela3:
        if values['-USUARIO-']:
            sg.popup(f"Bem-vindo(a), {values['-USUARIO-']}!")
            janela4 = janela_op()
            janela3.close()
        else:
            sg.popup_error("Por favor, insira um nome de usuário válido.")

    if event == 'Conjuntos' and window == janela4:
        atualizar_contagem('Conjuntos')
        sg.popup("Função Conjuntos ainda não implementada.")

    if event == 'Matrizes' and window == janela4:
        atualizar_contagem('Matrizes')
        janela_matriz = janela_matriz()
        janela4.hide()

    if event == 'Função' and window == janela4:
        atualizar_contagem('Função')
        sg.popup("Função Função ainda não implementada.")

    if event == 'Operações Básicas' and window == janela4:
        atualizar_contagem('Operações Básicas')
        janela_calculadorabasica = janela_calculadorabasica()
        janela4.hide()

    if event == 'Histórico' and window == janela4:
        relatorio = gerar_relatorio()
        sg.popup_scrolled(relatorio, title="Histórico de Cliques")

    if event == 'Criar Matriz A' and window == janela_matriz:
        try:
            linhasA = int(values['-linhaA-'])
            colunasA = int(values['-colunasA-'])
            if linhasA > 0 and colunasA > 0:
                sg.popup(f"Matriz A de {linhasA}x{colunasA} criada.")
            else:
                window['-erro-'].update("Número de linhas e colunas deve ser maior que 0.")
        except ValueError:
            window['-erro-'].update("Por favor, insira números válidos para linhas e colunas.")

    if event == 'Criar Matriz B' and window == janela_matriz:
        try:
            linhasB = int(values['-linhaB-'])
            colunasB = int(values['-colunasB-'])
            if linhasB > 0 and colunasB > 0:
                sg.popup(f"Matriz B de {linhasB}x{colunasB} criada.")
            else:
                window['-erro-'].update("Número de linhas e colunas deve ser maior que 0.")
        except ValueError:
            window['-erro-'].update("Por favor, insira números válidos para linhas e colunas.")

    if event == 'Multiplicar' and window == janela_matriz:
        try:
            linhasA = int(values['-linhaA-'])
            colunasA = int(values['-colunasA-'])
            linhasB = int(values['-linhaB-'])
            colunasB = int(values['-colunasB-'])
            if colunasA == linhasB:
                janela_matriz_valores = janela_matriz_valores(linhasA, colunasA, linhasB, colunasB)
                janela_matriz.hide()
            else:
                window['-erro-'].update("Número de colunas de A deve ser igual ao número de linhas de B.")
        except ValueError:
            window['-erro-'].update("Por favor, insira números válidos para linhas e colunas.")

    if event == 'Calcular' and window == janela_matriz_valores:
        linhasA = int(values['-linhaA-'])
        colunasA = int(values['-colunasA-'])
        linhasB = int(values['-linhaB-'])
        colunasB = int(values['-colunasB-'])
        A = pegar_valores_matriz(window, linhasA, colunasA, 1)
        B = pegar_valores_matriz(window, linhasB, colunasB, 2)
        if A is not None and B is not None:
            resultado = multiplicar_matrizes(A, B)
            sg.popup(f"Resultado da multiplicação:\n{resultado}")
