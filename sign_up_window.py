import PySimpleGUI as sg
import game_window

layout = [
            [sg.Text("Enter the first name:"), sg.Input(key='-FIRST_PLAYER-', do_not_clear=True, size=(20, 1))],
            [sg.Text("Enter your second name:"), sg.Input(key='-SECOND_PLAYER-', do_not_clear=True, size=(20, 1))],
            [sg.Button('Start the Game'), sg.Exit()]
        ]


window = sg.Window('Tic Tac Toe', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Start the Game':
        players = [values['-FIRST_PLAYER-'], values['-SECOND_PLAYER-']]
        game_window.initiate_game(players)

window.close()

