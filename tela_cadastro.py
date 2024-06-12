import PySimpleGUI as sg

def create_layout():
    layout = [
        [sg.Text('CALCULADORA SINISTRA', justification='center', size=(50, 1), font=('Any', 15), pad=(0, 20))],
        [sg.Text('cadastro', justification='center', size=(50, 1), font=('Any', 12), pad=(40, 20))],
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
    return sg.Window('Cadastro de Usuário', layout, size=(500, 450))

# Cria a janela com o layout gerado pela função
layout = create_layout()

# Loop de evento para processar "eventos" e obter os "valores" das entradas
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break
    if event == 'Enviar':
        usuario = values['-USUARIO-']
        senha = values['-SENHA-']
        email = values['-EMAIL-']
        print(f'Nome de usuário: {usuario}')
        print(f'Senha: {senha}')
        print(f'Email: {email}')
        # Aqui você pode adicionar qualquer lógica adicional, como validação ou processamento dos dados

# Fecha a janela
window.close()
