# Darpan Patel 35198867 Thanh Vu 17627579 Lab 4 ICS 32
import connectfour
import collections



def turn(current_state:tuple):
    # During each turn, the current state of the game is updated and
    # the player is asked to specified the column and the action (drop/pop)
    # that he/she wants to take. The function returns the current state of the game after the valid action has been made.

    while True:
        # asking user to specify the column number to take action
        try:

            column_specified = int(input('What column would you like to drop the tile in or pop a piece?: '))
            column_valid = []
            for i in range(1,8):
                column_valid.append(i)

            if column_specified in column_valid:
                (current_state,column_specified,action_input) = user_action_input(current_state, column_specified)
                return (current_state,column_specified,action_input)
            else:
                print("Please enter another valid column to take action")
                
        except:
            print('column command is invalid. Please enter an integer for column number')

            
        
def print_board(current_state:tuple):
    # display the board game from the beginning and after each successful move from each player
    board_game=[]
    for i in range(connectfour.BOARD_ROWS):
        board_game.append([])
    title_num = ''
    num = 0
    for item in range(len(board_game)+1):
        num+=1
        title_num+='{} '.format(num)

    print(title_num)
    for row_list in current_state.board:
        for column_number in range(len(row_list)):
            board_game[column_number].append(row_list[column_number])

    for row in board_game:
        result = ''
        for place in row:
            if place == 'R' or place =='Y':
                result+=('{} '.format(place))
            else:
               result+=('{} '.format('.')) 
                         
        print(result)
        

def user_action_input(current_state: tuple, column_specified: int):
    # ask the player to specify their action (drop/ pop) in the column they selected.
    # Ask the user to specify again if the action is invalid move on the selected column.
    while True:
        try:
            user_act_input= input('Please Select--- Drop or Pop  : ').lower()
            if user_act_input == 'pop':
                return (connectfour.pop_piece(current_state,int(column_specified-1)), column_specified, user_act_input)

            elif user_act_input == 'drop':
                return(connectfour.drop_piece(current_state, int(column_specified-1)),column_specified, user_act_input)


            else:
                print('not a valid command action!')
        except:
            print('invalid move on {} column or invalid column. Please enter another column.'.format(column_specified))
            current_state= turn(current_state)
            return current_state


