# Milestone Project 1: Creating a tic tac toe game

# Global Variables:
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
p1_marker = ''
p2_marker = ''


# Asking player to choose their symbol
def player_info():
    global p1_marker
    global p2_marker
    player_1 = input("Please Enter a marker, 'x' or 'o'")
    if player_1.lower() == "x":
        player_2 = 'o'
    elif player_1.lower() == "o":
        player_2 = "x"
    else:
        while player_1.lower()!= 'x' or player_1.lower()!= 'o':
            player_1 = input(" Not a valid input, please enter a marker, 'x' or 'o'")
            if player_1.lower() == "x":
                player_2 = 'o'
                break
            if player_1.lower() == "o":
                player_2 = "x"
                break
    p1_marker = player_1.lower()
    p2_marker = player_2.lower()
    return "player 1 has chosen " + player_1.lower() + "\nplayer 2 has chosen " + player_2.lower()


# BoardCreating Function: Creates the tictactoe board
def create_board(xo_list):
    next_line_counter = 0
    final_line_count = 0
    j = 0
    print(" -------------------")
    for i in range(len(xo_list)):
        print(" | " + xo_list[i] + " | ", end="")
        next_line_counter += 1
        final_line_count += 1
        if next_line_counter == 3:
            print("")
            while j < 1:
                print(" -------------------")
                j += 1
            j = 0
            next_line_counter = 0
    return ""


# Inputting player response into board:
def player_input():
    # p1 insert
    player_response = input("Player 1, please enter the position (0-8)")
    if board[int(player_response)] == ' ':
        player_1_response_cast = int(player_response)
        board[player_1_response_cast] = p1_marker
    else:
        while board[int(player_response)] != ' ':
            player_response = input("Position taken, please enter a different position")
        player_1_response_cast = int(player_response)
        board[player_1_response_cast] = p1_marker

    # p2 insert
    player_response = input("Player 2, please enter the position (0-8)")
    if board[int(player_response)] == ' ':
        player_2_response_cast = int(player_response)
        board[player_2_response_cast] = p2_marker
    else:
        while board[int(player_response)] != ' ':
            player_response = input("Position taken, please enter a different position")
        player_2_response_cast = int(player_response)
        board[player_2_response_cast] = p2_marker

    # return board, p1_marker, p2_marker
    return 'player 1 has entered ' + p1_marker + ' into position ' + str(
        player_1_response_cast) + "\nplayer 2 has entered " + p2_marker + ' into position ' + str(
        player_2_response_cast)


#Function for only player 1 on cases where there is only one vacant square left:
def player_1_final_res():
    player_response = input("Player 1, please enter the position (0-8)")
    if board[int(player_response)] == ' ':
        player_1_response_cast = int(player_response)
        board[player_1_response_cast] = p1_marker
    else:
        while board[int(player_response)] != ' ':
            player_response = input("Position taken, please enter a different position")
        player_1_response_cast = int(player_response)
        board[player_1_response_cast] = p1_marker
    return 'player 1 has entered ' + p1_marker + ' into position ' + str(
        player_1_response_cast)

# Function to check for winner in row:
#To Do: should reset x and o check respectively to 0 once a row has been finished
def check_row(game_board):
    x_row_check = 0
    o_row_check = 0
    #Checks when a row has been completed so that row check can be updated to zero
    row_complete_check=0
    # check row for winner(x):
    for i in range(len(game_board)):
        if game_board[i] == 'x':
            x_row_check += 1
        row_complete_check+=1
        if row_complete_check==4:
            if game_board[i] == 'x':
                x_row_check = 1
            else:
                x_row_check = 0
            row_complete_check=1
        if x_row_check == 1 and row_complete_check==3:
            x_row_check = 0
        if x_row_check == 3 and row_complete_check==3:
            print ('player x is the winner')
            return True

    row_complete_check=0

    # check row for winner(o):
    for i in range(len(game_board)):
        if game_board[i] == 'o':
            o_row_check += 1
        row_complete_check+=1
        if row_complete_check==4:
            if game_board[i] == 'o':
                o_row_check=1
            else:
                o_row_check=0
            row_complete_check=1
        if o_row_check == 1 and row_complete_check==3:
            o_row_check = 0
        if o_row_check == 3 and row_complete_check == 3:
            print('player o is the winner!')
            return True

def check_collumn(game_board):
    x_collumn_check=0
    o_collumn_check=0
    collumn_complete_check=0
    #Check collumn for winner(x):
    for i in range(len(game_board) - 6):
        for j in range(i, len(game_board), 3):
            if game_board[j]=='x':
                x_collumn_check+=1
            collumn_complete_check+=1
            if collumn_complete_check == 4:
                if game_board[i] == 'x':
                    x_collumn_check = 1
                else:
                    x_collumn_check = 0
                collumn_complete_check = 1
            if x_collumn_check == 1 and collumn_complete_check == 3:
                x_collumn_check = 0
                collumn_complete_check=0
            if x_collumn_check==3 and collumn_complete_check==3:
                print('player x is the winner!')
                return True

    collumn_complete_check=0
    #Check collumn for winner(o):
    for i in range(len(game_board) - 6):
        for j in range(i, len(game_board), 3):
            if game_board[j]=='o':
                o_collumn_check+=1
            collumn_complete_check+=1
            if collumn_complete_check == 4:
                if game_board[i] == 'o':
                    o_collumn_check = 1
                else:
                    o_collumn_check = 0
                collumn_complete_check = 1
            if o_collumn_check == 1 and collumn_complete_check == 3:
                o_collumn_check = 0
                collumn_complete_check=0
            if o_collumn_check==3 and collumn_complete_check==3:
                print('player o is the winner!')
                return True

#Check diagonal from left:
def check_left_diag(game_board):
    x_left_diag_check=0
    o_left_diag_check=0
    #Check for x:
    for i in range(0,len(game_board),4):
        if game_board[i]=='x':
            x_left_diag_check+=1
        if game_board[i]!='x':
            x_left_diag_check=0
            break
    if x_left_diag_check==3:
        print('player x is the winner')
        return True
    #Check for o:
    for i in range(0,len(game_board),4):
        if game_board[i]=='o':
            o_left_diag_check+=1
        if game_board[i]!='o':
            o_left_diag_check=0
            break
    if o_left_diag_check==3:
        print('player o is the winner')
        return True

#Check diagonal from right:
def check_right_diag(game_board):
    x_right_diag_check=0
    o_right_diag_check=0
    #Check for x:
    for i in range(2,len(game_board),2):
        if game_board[i]=='x':
            x_right_diag_check+=1
        if game_board[i]!='x':
            x_right_diag_check=0
            break
        if x_right_diag_check==3:
            print('player x is the winner')
            return True
    #Check for o:
    for i in range(2,len(game_board),2):
        if game_board[i]=='o':
            o_right_diag_check+=1
        if game_board[i]!='o':
            o_right_diag_check=0
            break
        if o_right_diag_check==3:
            print('player o is the winner')
            return True


def check_diag(game_board):
     if check_left_diag(game_board) or check_right_diag(game_board):
         return True

def clear_board(game_board):
    for i in range(len(game_board)):
        game_board[i]=' '
    return game_board


def tic_tac_toe():
    vacancy_check=0
    i = 0
    print(player_info())
    while i < 5:
        for j in range(len(board)):
            if board[j]==' ':
                vacancy_check+=1
        if vacancy_check==1:
            print(player_1_final_res())
            if check_row(board):
                print(create_board(board))
                break
            elif check_collumn(board):
                print(create_board(board))
                break
            elif check_right_diag(board):
                print(create_board(board))
                break
            else:
                print(create_board(board))
                print('No winner')
                play_again = input("Would you like to play again? y for yes, n for no")
                if play_again.lower() == 'y':
                    return tic_tac_toe()
                elif play_again.lower() == 'n':
                    return 'Thank you for playing'
                else:
                    while play_again.lower() != 'y' or play_again.lower() != 'n':
                        play_again = input("Would you like to play again? y for yes, n for no")
                        if play_again.lower() == 'y':
                            return tic_tac_toe()
                        if play_again.lower() == 'n':
                            return 'Thank you for playing'
                break
        print(player_input())
        vacancy_check = 0
        print(create_board(board))
        if check_row(board):
            break
        if check_collumn(board):
            break
        if check_right_diag(board):
            break
        i += 1
    play_again = input("Would you like to play again? y for yes, n for no")
    if play_again.lower() == 'y':
        clear_board(board)
        return tic_tac_toe()
    elif play_again.lower() == 'n':
        return 'Thank you for playing'
    else:
        while play_again.lower() != 'y' or play_again.lower() != 'n':
            play_again = input("Would you like to play again? y for yes, n for no")
            if play_again.lower() == 'y':
                clear_board(board)
                return tic_tac_toe()
            if play_again.lower() == 'n':
                return 'Thank you for playing'
    return ''

print(tic_tac_toe())


# test_board=['x','x','x','x','x','x','x','x','x']

# print(test_board)
# print(clear_board(test_board))


