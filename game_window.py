import PySimpleGUI as sg

sg.theme('Dark Amber')

def check_if_winner(board):   
    for column in range(0, 3):
        print(board)
        if ((0,column) in board.keys()) and ((1, column) in board.keys()) and ((2, column) in board.keys()):
            if board[(0, column)] == board[(1, column)] == board[(2, column)]:
                return board[(0, column)]
    
    for row in range(0, 3):
        if ((row, 0) in board.keys()) and ((row, 1) in board.keys()) and ((row, 2) in board.keys()):
            if board[(row, 0)] == board[(row, 1)] == board[(row, 2)]:
                return board[(row, 0)]

    if ((0,0) in board.keys()) and ((1,1) in board.keys()) and ((2,2) in board.keys()):
        if board[(0,0)] == board[(1,1)] == board[(2,2)]:
            return board[(1,1)]

    if ((2,0) in board.keys()) and ((1,1) in board.keys()) and ((0,2) in board.keys()):
        if board[(2,0)] == board[(1,1)] == board[(0,2)]:
            return board[(2, 0)]        

def initiate_game(players):
    board, player = {}, 0

    layout = [[sg.Text('Current Player: ' + players[player], key='-CURRENT_PLAYER-')]]
    for row in range(3):
        new_row = []
        for column in range(3):
            new_row.append(sg.Button(size=(3, 2), key=(row, column)))
        layout.append(new_row)
    layout.append([sg.Button('Reset'), sg.Button('Cancel')])

    window = sg.Window('TicTacToe', layout, use_default_focus=False)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        
        if event == 'Reset':
            board = {}
            for row in range(3):
                for col in range(3):
                    window[(row, col)].update('')

        elif event not in board:
            board[event] = player
            window[event].update('X' if player else '0')
            is_winner = check_if_winner(board)
            if is_winner is not None:
                sg.popup("The winner is "+ players[player])
                break
            player = (player + 1) % 2
            window['-CURRENT_PLAYER-'].update('Current player: ' + players[player])

    window.close()
    



