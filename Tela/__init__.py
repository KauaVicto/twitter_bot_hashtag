import PySimpleGUI as sg

class Tela:

    def __init__(self):
        sg.theme('DefaultNoMoreNagging')
        self.layout = [
            [sg.Text('Hashtags:'), sg.InputText(key='hashtags')],
            [sg.Text('Da conta:'), sg.InputText(key='da_conta')],
            [sg.Text('Para a conta:'), sg.InputText(key='para_conta')],
            [sg.Text('Da data:'), sg.InputText(key='da_data')],
            [sg.Text('Até a data:'), sg.InputText(key='ate_data')],
            [sg.Button('Enviar', key='enviar'), sg.Button('Cancelar', key='cancelar')]
        ]

    def iniciar(self):
        self.janela = sg.Window('Minha janela', self.layout)

        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED or evento == 'cancelar':
                break
            elif evento == 'enviar':
                self.janela.close()
                return valores
        
