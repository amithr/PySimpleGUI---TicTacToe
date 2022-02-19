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
    board, player = {}, 0 # Keeps track of coordinates on the board that respective players have selected

    layout =  [[sg.Text('Current Turn'+ players[player])]]
    for row in range(3):
        new_square_row = []
        for col in range(3):
            new_square_row += [sg.Button(size=(3,2), key=(row,col))]
        layout.append(new_square_row)      
    layout.append([sg.Button('Reset'), sg.Button('Cancel')])

    window = sg.Window('Window Title', layout, use_default_focus=False)


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
            board[event] = player # Assigns a player number to each coordinate on the board
            # Each event is a tuple containing coordinates from the board
            window[event].update('X' if player else '0') # Checks if player is a 1 or 0
            is_winner = check_if_winner(board)
            print(is_winner)
            if is_winner is not None:
                sg.popup("The winner is "+players[player])
                break
            player = (player + 1) % 2 # Can switch between 1 and 0 in an alternating fashion
    window.close()



