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

# Criar a primeira janela
window1 = criar_janela_inicial()
window2 = None  # Segunda janela não é criada inicialmente

# Loop de eventos
while True:
    window, event, values = sg.read_all_windows()
    
    if event == sg.WINDOW_CLOSED:
        window.close()
        if window == window2:
            window2 = None
        elif window == window1:
            break
    
    if event == 'INICIAR' and window == window1:
        window.hide()
        if window2 is not None:  # Feche a janela secundária se estiver aberta
            window2.close()
        window2 = criar_janela_secundaria()
    
    if event == 'Voltar' and window == window2:
        window2.close()
        window2 = None
        window1.un_hide()
    
    if event == 'Entrar' and window == window2:
        sg.popup('Entrar clicado')
    
    if event == 'Cadastre-se' and window == window2:
        sg.popup('Cadastrar-se clicado')

window1.close()
if window2:
    window2.close()
