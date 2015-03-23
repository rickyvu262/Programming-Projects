#Thanh Vu #17627579 #UCnetid: thanhhv  ICS 32 Spring 2014 Lab 4
import othello_logic


def main():
    
    
    column_board, row_board = user_input_column_row()   # asking user to input number of columns, row
    turn = first_player_move_turn()                     # which player move first

    game_state = othello_logic.Othello_game_state(column_board,row_board,turn)  # create a game_state object from a class

    # default 4 pieces of the game at the beginning
    player, other_player = top_left_player_piece()
    win_method = method_to_win_rule()
    current_board = game_state.pieces_at_game_begin(player,other_player)    # default pieces at beginning game
    user_interface(game_state,current_board,win_method,row_board,column_board,turn)

def user_interface(game_state,current_board,win_method,row_board, column_board,turn):
    
    while True:
    # update the game (while loop) until the game has a winner ( game_over_check -> no more valid moves)
        try:
        
            game_state.copy_board(current_board)        # always want to update the current board after each turn and print it out 
            game_state.location_same_color_piece()      # determine all the locations of that current's player turn and return those locations as a list 


            
            game_state.adjacent_spot_flip_list_move()   # see othello_logic to follow what this function does
                                                        # briefly, check around a piece in order to determine valid moves' location to place a piece. 
                                                        # focus on self.valid_move: location of valid moves
                                                        #          self.flip_pieces: pieces needed to be flipped after a piece is placed
            
            # At every turn always update the current game_board, and check if the game is over, then quit 
            if win_method == 'A':
                if game_state.game_over_check() == True:
                    game_state.copy_board(current_board)
                    winner = game_state.winner_check_most_points()
                    print(winner,'is the winner')
                    quit()
            elif win_method == 'B':
                if game_state.game_over_check() == True:
                    game_state.copy_board(current_board)
                    winner = game_state.winner_check_least_points()
                    print(winner,'is the winner')
                    quit()
            
            # asking the current_plyaer a row and column to input a piece 
            row_select, column_select = user_input(row_board,column_board)

            # update a current board -> remember current_board is the list and the element will keeps updating as the game moves along 
            # meaning elements in the list will be inserted and or changed as you flipping pieces and placing pieces
            current_board = game_state.make_a_move(row_select,column_select)
            
            # after a turn is finished (meaning a current player successfully placed a valid move and flipped some pieces on the game_board)
            # switch current player to the other player and the while true loop takes care the same steps for the other player. 
            game_state.opposite_turn()
        except:
            # if an invalid move is made, catch the exception and ask for another move. 
            print('Please Try again')


def user_input (board_row, board_col):
    while True:
        try:
            row_input = int(input("Select the row: "))-1
            column_input = int(input("Select the column: "))-1
            if 0 <= row_input < board_row and 0 <= column_input < board_col:
                return (row_input,column_input)
        except:
            print("Not a valid column/row number. Please try again")
def user_input_column_row():
    # row and column is even integer from 4-16, ask user again if invalid input
    while True:
        column_input = int(input("Please enter even interger from 4-16 for column of the board game: "))
        row_input = int(input("Please enter even interger from 4-16 for row of the board game: "))
        if 4 <= column_input <= 16 \
                and 4 <= row_input <= 16\
                and column_input % 2 == 0 \
                and row_input % 2 == 0:

            return (column_input,row_input)
        else:
            print("nope")

def first_player_move_turn():
    while True:
        player_move_first = input("Please indicate which player will move first (B or W): ").strip()
        if player_move_first == 'B' or player_move_first == 'W':
            return (player_move_first)
        else:
            print("not a valid command for player's turn.")

def top_left_player_piece():
    while True:
        piece_input = input("Please indicate the color of the piece at the top left of the center of the board game (B or W): ")
        if piece_input == 'B':
            player = piece_input
            other_player = 'W'
            return (player,other_player)
        elif piece_input == 'W':
            player = piece_input
            other_player = 'B'
            return (player,other_player)
        else:
            print("Try a valid command for color of the piece")

def method_to_win_rule():
    while True:
        win_input= input('''
Please Select A: player with most pieces on the board at the end win
              B: player with least pieces on the board at the end win
              ''')
        if win_input == 'A': # access the rule with score counts the most pieces win
            return win_input
        elif win_input =='B': # access the rule with score counts least pieces win
            return win_input


if __name__ == '__main__':
    main()
