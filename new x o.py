import random
def display_board(board):
    i=1
    for _ in range(3):
        print(' '+ board[i]+ '|'+ board[i+1] +'|'+board[i+2])
        if i<7:
            print('-------')
        i+=3
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
def place_marker(board, marker, position):
    board[position] = marker
def palyer_sign():
    sign=' '
    while not (sign=='X' or sign=='O' ):
        sign=input("palyer 1: chose X or O:").upper()
        if sign=='X':
            return('X','O')
        else:
            return('O','X')
def check_win(Board):
    j=k=1
    for _ in range(3):
        if (Board[j]==Board[j+1]==Board[j+2]!=' '):
            return True
        j+=3
        if (Board[k]==Board[k+3]==Board[k+6]!=' '):
            return True
        k+=1
    if ((Board[1]==Board[5]==Board[9]!=' ')or(Board[3]==Board[5]==Board[7]!=' ')):
        return True
    return False
def space_check(board, position):
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9): '))
        
    return position
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    Board = [' '] * 10
    player1_marker, player2_marker = palyer_sign()
    turn = choose_first()
    print(turn + ' will go first.')
    
        #play_game = input('Are you ready to play? Enter Yes or No.')

        #if play_game.lower()[0] == 'y':
    game_on = True
        #else:
            #game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(Board)
            position = player_choice(Board)
            place_marker(Board, player1_marker, position)

            if check_win(Board):
                display_board(Board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(Board):
                    display_board(Board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn.
            
            display_board(Board)
            position = player_choice(Board)
            place_marker(Board, player2_marker, position)

            if check_win(Board):
                display_board(Board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(Board):
                    display_board(Board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break