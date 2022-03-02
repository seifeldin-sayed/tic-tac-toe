import random
def board_all(player,p,board):
    if p== '1' or p=='2' or p=='3':
        board[0].insert(board[0].index(p),player)
        board[0].remove(p)
    elif p== '4' or p=='5' or p=='6':
        board[1].insert(board[1].index(p),player)
        board[1].remove(p)
    else :
        board[2].insert(board[2].index(p),player)
        board[2].remove(p)
    for col in range(3):
        print( ' ' + board[col][0] +' | '+ board[col][1] + ' | ' + board[col][2])
    return(player)
def swap_player(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return(player)
def check_win(player,board):
    c=0
    for row in range(3):
        if board[row][0]==board[row][1]==board[row][2]:
            print(player + ' won')
            c=1
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col]:
            print(player + ' won')
            c=1
    if board[0][0]==board[1][1]==board[2][2]:
        print(player + ' won')
        c=1
    elif board[0][2]==board[1][1]==board[2][0]:
        print(player + ' won')
        c=1
    return(c)
def play(turn,player,board,bag):
    print(player +' turn')
    p = input("Choose a place:")
    if p.isdigit():
        if p in bag:
            board_all(player,p,board)
            bag.remove(str(p)) 
        else:
            print("you have to enter a number from 1 to 9! ")
            play(turn,player,board,bag)
    else:
        print("you have to enter a number! ")
        play(turn,player,board,bag)
    return(player)
def comp(player,board,bag):
    p = random.choice(bag)
    board_all(player,p,board)
    bag.remove(str(p))
def game():
    bagn=['1','2']
    num_player = input("Enter number of player (1 or 2):")
    while num_player not in bagn:
        num_player = input("Enter number of player (1 or 2):")
    bagp=['x','X','o','O']
    player = input("Enter X or O:").upper()
    while player not in bagp:
        player = input("Enter X or O:").upper()
    turn=1
    board=[ ['1','2','3'],
            ['4','5','6'],
            ['7','8','9']]
    for col in range(3):
            print( ' ' + board[col][0] +' | '+ board[col][1] + ' | ' + board[col][2])
    bag=['1','2','3','4','5','6','7','8','9']
    if num_player== '2':
        while turn<10:
            player=play(turn,player,board,bag)
            c=check_win(player,board)
            player = swap_player(player)
            if c==1:
                break  
            turn+=1
            if turn==10:
                print("it's a tie game")
    else:
        while turn<6:
            player=play(turn,player,board,bag)
            c=check_win(player,board)
            player = swap_player(player)
            if c==1:
                break
            if turn==5:
                print("it's a tie game") 
                break
            print("\n")
            comp(player,board,bag)
            c=check_win(player,board)
            player = swap_player(player)
            if c==1:
                break 
            turn+=1
game()
