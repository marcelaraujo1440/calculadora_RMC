import PySimpleGUI as sg

# Configurações de tema e fonte
sg.theme('DarkBlue3')

def criar_janela_inicial():
    layout = [
        [sg.Text('Olá, seja bem vindo(a) à', justification='center', font=('Any', 20), pad=(0, 20))],
        [sg.Text('"calculadora sinistra"', justification='center', font=('Any', 30, 'bold'), pad=(0, 20))],
        [sg.Button('INICIAR', size=(15, 1), font=('Any', 15, 'bold'), pad=(0, 20))],
        [sg.Text('Desenvolvido por Gabriel Carmo e Marcel Araujo, todos os direitos reservados ©', 
                 justification='center', font=('Any', 10), pad=(0, 60))]
    ]
    return sg.Window('Calculadora Sinistra', layout, size=(500, 450), element_justification='center', finalize=True)

def criar_janela_secundaria():
    layout = [
        [sg.Text('CALCULADORA SINISTRA', justification='center', font=('Any', 20), pad=(0, 20))],
        [sg.Text('Escolha uma opção:', justification='center', font=('Any', 15), pad=(0, 20))],
        [sg.Button('Entrar', size=(15, 1), font=('Any', 15, 'bold')), 
         sg.Button('Cadastre-se', size=(15, 1), font=('Any', 15, 'bold'), pad=(20, 0))],
        [sg.Button('Voltar', size=(15, 1), font=('Any', 15, 'bold'), pad=(0, 20))],
        [sg.Text('Desenvolvido por Gabriel Carmo e Marcel Araujo, todos os direitos reservados ©', 
                 justification='center', font=('Any', 10), pad=(0, 60))]
    ]
    return sg.Window('Calculadora Sinistra', layout, size=(500, 450), element_justification='center', finalize=True)

def janela_Cadastro():
    layout = [
        [sg.Text('CALCULADORA SINISTRA', justification='center', size=(50, 1), font=('Any', 15), pad=(0, 20))],
        [sg.Text('cadastro', justification='center', size=(50, 1), font=('Any', 15), pad=(40, 20))],
        [sg.Column([
            [sg.Frame(layout=[
                [sg.Text('Nome de usuário')],
                [sg.InputText(key='-USUARIO-', size=(30, 1), enable_events=True)]
            ], title='', pad=(0, 10))],
            [sg.Frame(layout=[
                [sg.Text('Senha')],
                [sg.InputText(key='-SENHA-', size=(30, 1), password_char='*', enable_events=True)]
            ], title='', pad=(0, 10))],
            [sg.Frame(layout=[
                [sg.Text('Email')],
                [sg.InputText(key='-EMAIL-', size=(30, 1), enable_events=True)]
            ], title='', pad=(0, 10))]
        ], justification='center')],
        [sg.Button('Enviar', size=(15, 1),pad=(10,20)), sg.Button('Voltar', size=(15, 1), pad=(10, 20))]
    ]
    return sg.Window('Cadastro de Usuário', layout, size=(500, 450),element_justification='center', finalize=True)

def janela_entrar():
    layout = [
        [sg.Text('CALCULADORA SINISTRA', justification='center', size=(50, 1), font=('Any', 15), pad=(0, 20))],
        [sg.Text('Entrar', justification='center', size=(50, 1), font=('Any', 15), pad=(40, 20))],
        [sg.Column([
            [sg.Frame(layout=[
                [sg.Text('Nome de usuário')],
                [sg.InputText(key='-USUARIO-', size=(30, 1), enable_events=True)]
            ], title='', pad=(0, 10))],
            [sg.Frame(layout=[
                [sg.Text('Senha')],
                [sg.InputText(key='-SENHA-', size=(30, 1), password_char='*', enable_events=True)]
            ], title='', pad=(0, 10))],
        ], justification='center')],
        [sg.Button('Enviar', size=(15, 1),pad=(10,20)), sg.Button('Voltar', size=(15, 1), pad=(10, 20))]
    ]
    return sg.Window('Entrar', layout, size=(500, 450),element_justification='center', finalize=True)

def janela_op():
    layout=[

            [sg.Text("CALCULADORA SINISTRA", justification='center', font=('Any', 20), pad=(0, 20)),],
            [sg.Text("Escolha a sua operação!",justification='center', font=('Any', 15), pad=(0, 20))],
            [sg.Button("Conjuntos", size=(15, 1), font=('Any', 15, 'bold')), sg.Button("Matrizes", size=(15, 1), font=('Any', 15, 'bold'))],
            [sg.Button("Funções",size=(15, 1), font=('Any', 15, 'bold')), sg.Button("Raiz Quadrada",size=(15, 1), font=('Any', 15, 'bold'))],
            [sg.Button("Fatorial",size=(15, 1), font=('Any', 15, 'bold')), sg.Button("Operações Básicas",size=(15, 1), font=('Any', 15, 'bold'))],
            [sg.Button("Histórico",size=(15, 1), font=('Any', 15, 'bold'))],
            
        ]
    return sg.Window('Calculadora Sinistra', layout, size=(500, 450), element_justification='center', finalize=True)

# Criar a primeira janela
window1 = criar_janela_inicial() #janela inicial
window2 = None  # entrar ou cadastre-se
window3 = None #cadastre-se
window4 = None # entrar
window5 = None #operações

# Loop de eventos
while True:
    window, evento, valores = sg.read_all_windows()
    
    if evento == sg.WINDOW_CLOSED:
        window.close()
        if window == window2:
            window2 = None
        if window == window3:
            window3 = None
        elif window == window1:
            break
    
    if evento == 'INICIAR' and window == window1:
        window.hide()
        if window2 is not None:  # Feche a janela secundária se estiver aberta
            window2.close()
        window2 = criar_janela_secundaria()
    
    if evento == 'Voltar' and window == window2: #esse é da 1
        window2.close()
        window2 = None
        window1.un_hide()
    
    if evento == 'Voltar' and window == window3:
        window3.close()
        window3 = None
        window2.un_hide()
    
    if evento == 'Voltar' and window == window4:
        window4.close()
        window4 = None
        window2.un_hide()
    
    if evento == 'Entrar' and window == window2:
        window2.hide()
        if window4 is not None:  # Feche a janela secundária se estiver aberta
            window4.close()
        window4 = janela_entrar()
    
    if evento == 'Cadastre-se' and window == window2:
        window2.hide()
        if window3 is not None:  # Feche a janela secundária se estiver aberta
            window3.close()
        window3 = janela_Cadastro()

    elif evento == 'Conjuntos' and window == window5:
        sg.popup('Conjuntos clicado')

    elif evento == 'Matrizes' and window == window5:
        sg.popup('Matrizes clicado')
    
    elif evento == "Funções" and window == window5:
        sg.popup('Funções clicado')
    
    elif evento == 'Raiz Quadrada' and window == window5:
        sg.popup('Raiz Quadrada clicado') 
    
    elif evento == 'Fatorial' and window == window5:
        sg.popup('Fatorial clicado')
    elif evento == 'Operações Básicas' and window == window5:
        sg.popup('Operações Básicas clicado')
    
    elif evento == 'Histórico' and window == window5:
        sg.popup('Histórico clicado')

    if evento== 'Enviar' and window == window3:
        usuario = valores['-USUARIO-']
        senha = valores['-SENHA-']
        email = valores['-EMAIL-']
        print(f'Nome de usuário: {usuario}')
        print(f'Senha: {senha}')
        print(f'Email: {email}')
    
        
window1.close()
if window2:
   window2.close()