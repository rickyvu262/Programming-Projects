# Darpan Patel 35198867 Thanh Vu 17627579 Lab 4 ICS 32
import protocolmodule
import socket
import collections
import user_and_network_module
import connectfour

#create a namedtuple action_column that has 2 fields action (DROP/POP) and column(int) 
action_column = collections.namedtuple('action_column',['action','column'])

### connect is a namedtuple with 3 fields (from protocol module)
def user_interface():
    # Print out a short introduction to the game Connectfour function
    welcome_message()
    # ask for username function
    user_name = username_ask()
    # specify host and port, woodhouse.ics.uci.edu, port:4444
    connect= host_port_input()

    # after connection successful, now proceed the game.

    # But need to proceed the conversation behind the scene with the server first
    protocolmodule.connect_login(connect,user_name)
    # pass the welcome username, now request game by typing AI from client
    protocolmodule.request_game(connect)

    return connect

    #let's print the empty board game and PROCEED the game
    #with client taking the 1st action, and updated the board_game

def players_phase():
    connect = user_interface()


    game_board = connectfour.new_game_state()

    # Creat and return ConnectFourGame brand new game

    while True:
        # print empty board and updated board after every click by each player
        user_and_network_module.print_board(game_board)
        # check the current state to determine the winner
        if win_check(game_board)== ' ': # if no winner yet, the next turn is executed.
            (game_board,column_specified,action_input) = user_and_network_module.turn(game_board)
            #extract the column number and action input to store in a namedtuple
            each_turn_action= action_column(action_input,column_specified)
            #check if your last move indicates the winning move!
            if win_check(game_board)== 'R':
                print("Congratulations, You're the new champ!")
                quit()
            elif win_check(game_board) == 'Y':
                print("Yellow is the winner of the game")
                quit()


            #client send the action and column number to socket in protocol format
            client_move = str(each_turn_action.action).upper() + ' ' + str(each_turn_action.column)
            server_counter_move= protocolmodule.send_valid_move(connect,client_move)
            #extracted the server's move from the protocol and use it to make a move and update the current game state
            game_board = computer_move(server_counter_move,game_board)


        elif win_check(game_board)!= ' ':# if winner is determined, print out the winner and quit the game
            if win_check(game_board)== 'R':
                print ("Congratulations! You are the new champ!")
            else:
                print(" Yellow is the winner of the game")
            quit()

def win_check(current_state:tuple):
    #check if the game is over yet and return R/Y for the winning player
    return connectfour.winning_player(current_state)

def computer_move(server_counter_action : str, current_state:'current game state'):
    # split the server's action into action and column
    action_column = server_counter_action.split()
    action = action_column[0]
    column = action_column [1]
    # drop/pop a piece and update the current state of the game
    if action == 'DROP':
        current_state = connectfour.drop_piece(current_state,int(column) - 1)
        return current_state
    elif action == 'POP':
        current_state = connectfour.pop_piece(current_state,int(column) - 1)
        return current_state

def username_ask():
    # Repeatedly ask for username input until they entered a valid username. Otherwise, print error and try again.
    while True:
        username_specify = input('Username:')
        if ' ' not in username_specify and '\t' not in username_specify:
            print("Welcome " + username_specify)
            return username_specify
        else:
            print("Invalid username. Please Try again")

def host_port_input():
    # asking user to specify the host and port. 
    while True:
        try:
            host_input= str(input('Please enter the host:')).strip()
            port_input= int(input('Please enter the port:'))
            
            connect = protocolmodule.connectfour_conversation(host_input,port_input) # if connection valid, return a namedtuple connect in this module
            return connect
        # if host and port are not valid, print error and exit the program
        except:
            print("invalid host and port.")
            quit()
        
def welcome_message():
    print(" Welcome to the game of Connectfour, where only the strong can survive!")
    print("\n")
    print(" Please type in username.")
    print(" (Note: username does not have any white space in between or after)")
    print("\n")

if __name__ == '__main__':
    players_phase()
