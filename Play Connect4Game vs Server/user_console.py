# Darpan Patel 35198867 Thanh Vu 17627579 Lab 4 ICS 32
import connectfour
import user_and_network_module

def main():
    # Creat and return ConnectFourGame brand new game
    game_board = connectfour.new_game_state()
    while True:
        # print empty board and updated board after every click by each player
        user_and_network_module.print_board(game_board)
        # check the current state to determine the winner
        if win_check(game_board)== ' ': # if no winner yet, the next turn is executed.
            (game_board,column_specified,action_input) = user_and_network_module.turn(game_board)
        elif win_check(game_board)!= ' ':# if winner is determined, print out the winner and quit the game
            if win_check(game_board)== 'R':
                print ("Red is the winner of the game")
            else:
                print(" Yellow is the winner of the game")
            quit()


def win_check(current_state:tuple):
     return connectfour.winning_player(current_state)


if __name__ == '__main__':
    main()

