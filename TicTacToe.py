from random import randrange

def display_board(board):
    print(f'''
        +--------+--------+--------+
            |        |        |        |
            |    {board[0][0]}   |    {board[0][1]}   |    {board[0][2]}   |
            |        |        |        |
            +--------+--------+--------+
            |        |        |        |
            |    {board[1][0]}   |    X   |    {board[1][2]}   |
            |        |        |        |
            +--------+--------+--------+
            |        |        |        |
            |    {board[2][0]}   |    {board[2][1]}   |    {board[2][2]}   |
            |        |        |        |
            +--------+--------+--------+
            '''.format()
            )
def enter_move(board):

    while True:
        move = int(input("Enter your move: "))
        
        if move < 1 or move > 9:
            print("Sorry, pick a number 1-9: ")
            continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print('Square is already taken')
            continue
        elif move == 1:
            board[0][0] = 'O'
        elif move == 2:
            board[0][1] = 'O'
        elif move == 3:
            board[0][2] = 'O'
        elif move == 4:
            board[1][0] = 'O'
        elif move == 5:
            board[1][1] = 'O'
        elif move == 6:
            board[1][2] = 'O'
        elif move == 7:
            board[2][0] = 'O'
        elif move == 8:
            board[2][1] = 'O'
        elif move == 9:
            board[2][2] = 'O'

        break
        
 def make_list_of_free_fields(board):

    global freesquares
    freesquares = []

    for row in range(0,3):
        for col in range(0,3):
            if board[row][col] == 'X' or board[row][col] == 'O':
                pass
            else:
                freesquares.append(([row],[col]))
                
    return freesquares
    
def victory_for(board, sign):

    #Horizontal
    if (board[0][0]==board[0][1] and board[0][1] == board[0][2]):
        return True
    elif (board[1][0]==board[1][1] and board[1][1] == board[1][2]):
        return True
    elif (board[2][0]==board[2][1] and board[2][1] == board[2][2]):
        return True
    #Vertical
    elif (board[0][0] == board[1][0] and board[1][0] == board[2][0]):
        return True
    elif (board[0][1] == board[1][1] and board[1][1] == board[2][1]):
        return True
    elif (board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        return True
    #Diagonal
    elif (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return True
    elif (board[2][0] == board[1][1] and board[1][1] ==board[0][2]):
        return True
    else:
        print('No winner yet')
    
    running = False

def draw_move(board):

    while True:
        row = randrange(3)
        col = randrange(3)

        if ([row], [col]) not in freesquares:
            continue
        else:
            board[row][col] = 'X'
            return

board = [
['1','2','3'],
['4','X','6'],
['7','8','9']]

numMoves = 1

player1 = 'O'
comp = 'X'

print('Current board status: ')
print(display_board(board))


while numMoves<9:
    print(enter_move(board))
    numMoves+=1
    #print(display_board(board))

    if victory_for(board, player1) == True:
        print('You won')
        break
    else:
        print('List of free fields: '+ '\n')
        print(make_list_of_free_fields(board))
        print(display_board(board))

    print(draw_move(board))
    numMoves += 1
    print(display_board(board))
    print()

    if victory_for(board, comp) == True:
        print('Computer won')
        break
    else:
        print('List of free fields: ')
        print(make_list_of_free_fields(board))
        print(display_board(board))
else:
    print('Cats game')
        
