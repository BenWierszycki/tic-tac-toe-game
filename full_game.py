# import packages
from IPython.display import clear_output
import random


# create board
def display_board(board):
    print(board[7],' | ',board[8],' | ', board[9], end = '                  ')
    print(7,' | ',8,' | ', 9,)
    print('---------------', end = '               ')
    print('---------------')
    print(board[4],' | ',board[5],' | ', board[6], end = '                  ')
    print(4,' | ',5,' | ', 6)
    print('---------------', end = '               ')
    print('---------------')
    print(board[1],' | ',board[2],' | ', board[3], end = '                  ')
    print(1,' | ',2,' | ', 3)


# assign each player X or O
def player_input():
    marker = ''
    while marker not in ['X','O']:
        marker = input(f'Choose your marker (X or O):  ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# place marker function
def place_marker(board, marker, position):
    board[position] = marker  


# checking if winning requirements fulfilled
def win_check(board, marker):
    if board[1:4] == [marker, marker, marker] or board[4:7] == [marker, marker, marker] or board[7:10] == [marker, marker, marker]:
        print('')
        print(f'{marker} wins!')
        return True
    elif board[1:8:3] == [marker, marker, marker] or board[2:9:3] == [marker, marker, marker] or board[3:10:3] == [marker, marker, marker]:
        print('')
        print(f'{marker} wins!')
        return True
    elif board[1:10:4] == [marker, marker, marker] or board[3:8:2] == [marker, marker, marker]:
        print('')
        print(f'{marker} wins!')
        return True
    else:
        return False


# randomly deciding who goes first
def choose_first():
    first_player = str(random.randint(1,2))
    print(f'Player {first_player} plays first!')
    return first_player


# checking if board position available
def space_check(board, position):
    if board[position] not in ['X','O']:
        return True
    else:
        return False


# checking if board full
def full_board_check(board):
    for i in board[1:10]:
        if i not in ['X','O']:
            return False
    print('')
    print("It's a draw!")
    return True


# choosing board position
def player_choice(board):
    # placeholder for position
    position = 1000
    available = False
    while position not in range(1,10) or available == False:
        position = int(input('Choose position to place your marker:  '))
        if position not in range(1,10):
            print('Please choose an integer from 1-9')                 
        elif space_check(board, position) == False:
            print('This board space is not available!')
        else:
            available = True
    return position


# seeing if replay wanted
def replay():
    play_again_y_n = 'xxxx'
    
    while play_again_y_n.upper() not in ['Y','N']:
        print('')
        play_again_y_n = input('Play Again? (Y or N)')

        if play_again_y_n.upper() not in ['Y','N']:
            clear_output()
            print("Please make sure to choose Y or N.")
    
    return play_again_y_n.upper() == 'Y'
    

# ---------------------------------------------------------------------------------------------------
### THE GAME: 

print('Welcome to Tic Tac Toe!')

game_on = True

while game_on == True:
    # Reset the board
    theBoard = [' '] * 10
    # assign markers
    player1_marker, player2_marker = player_input()
    # randomly choose first player
    turn = choose_first()
    
    play_game = input('Are you ready to play? Enter Y or N')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

        
    while game_on == True:
        if turn == 'Player 1':
            # Player 1's turn.
            clear_output()
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                clear_output()
                display_board(theBoard)
                print('\nCongratulations! Player 1 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    clear_output()
                    display_board(theBoard)
                    print('\nThe game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player 2's turn.
            clear_output()
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                clear_output()
                display_board(theBoard)
                print('\nCongratulations! Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    clear_output()
                    display_board(theBoard)
                    print('\nThe game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        print('\nThanks for playing!')
        break
