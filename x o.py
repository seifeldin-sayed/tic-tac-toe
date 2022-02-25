def board_all(player,p,board_1,board_2,board_3):
    if p=='1':
        board_1.remove('1')
        board_1.insert(0,player)
    elif p=='2':
        board_1.remove('2')
        board_1.insert(1,player)
    elif p=='3':
        board_1.remove('3')
        board_1.insert(2,player)
    elif p=='4':
        board_2.remove('4')
        board_2.insert(0,player)
    elif p=='5':
        board_2.remove('5')
        board_2.insert(1,player)
    elif p=='6':
        board_2.remove('6')
        board_2.insert(2,player)
    elif p=='7':
        board_3.remove('7')
        board_3.insert(0,player)
    elif p=='8':
        board_3.remove('8')
        board_3.insert(1,player)
    elif p=='9':
        board_3.remove('9')
        board_3.insert(2,player)
    print(board_1)
    print(board_2)
    print(board_3)
    return(player)
def swap_player(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return(player)
def check_win(player,board_1,board_2,board_3):
    c=0
    if board_1[0]==board_2[0]==board_3[0]:
        print(player + ' won')
        c=1
    elif board_1[1]==board_2[1]==board_3[1]:
        print(player + ' won')
        c=1
    elif board_1[2]==board_2[2]==board_3[2]:
        print(player + ' won')
        c=1
    elif board_1[0]==board_1[1]==board_1[2]:
        print(player + ' won')
        c=1
    elif board_2[0]==board_2[1]==board_2[2]:
        print(player + ' won')
        c=1
    elif board_3[0]==board_3[1]==board_3[2]:
        print(player + ' won')
        c=1
    elif board_1[0]==board_2[1]==board_3[2]:
        print(player + ' won')
        c=1
    elif board_1[2]==board_2[1]==board_3[0]:
        print(player + ' won')
        c=1
    return(c)
def play(turn,player,board_1,board_2,board_3,bag):
    print(player +' turn')
    p = input("Choose a place:")
    if p.isdigit():
        if p in bag:
            board_all(player,p,board_1,board_2,board_3)
            bag.remove(str(p)) 
        else:
            print("you have to enter a number from 1 to 9! ")
            play(turn,player,board_1,board_2,board_3,bag)
    else:
        print("you have to enter a number! ")
        play(turn,player,board_1,board_2,board_3,bag)
    return(player)
def game():
    bagp=['x','X','o','O']
    player = input("Enter X or O:").upper()
    while player not in bagp:
        player = input("Enter X or O:").upper()
    turn=1
    board_1 = [ '1' , '2' , '3' ]
    board_2 = [ '4' , '5' , '6' ]
    board_3 = [ '7' , '8' , '9' ]
    print(board_1)
    print(board_2)
    print(board_3)
    bag=['1','2','3','4','5','6','7','8','9']
    while turn<10:
        player=play(turn,player,board_1,board_2,board_3,bag)
        c=check_win(player,board_1,board_2,board_3)
        player = swap_player(player)
        if c==1:
            break  
        turn+=1
        if turn==10:
            print("it's a tie game")  
game()