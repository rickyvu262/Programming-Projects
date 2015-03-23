#Thanh Vu #17627579 #UCnetid: thanhhv  ICS 32 Spring 2014 Lab 4


# The GUI of the game is not finished. GUI is capable of accepting the user's input and display the beginning of the board with 4 initial pieces
# Also the board can resized as the window resizes. However, the game logic module is finished and can be test with a Othello_user_interface module.

import othello_logic
import tkinter
from tkinter import ttk
from tkinter import StringVar

Default_font = ('Helvetica', 18)
_background_color = 'blue'
Black_player= 'B'
White_player= 'W'
none=' '

class GUI_Othello():
    def __init__(self):


        self._root_window = tkinter.Tk()

        self.square_width = 0
        self.square_height = 0

        self.center_x= 0.5
        self.center_y= 0.5


        self.all_current_piece =[]
        self.all_other_piece =[]

        self.button1 = tkinter.Button(
            master = self._root_window, text = 'Start Game', font= Default_font
        )

        self.button1.grid(
            row = 2, column = 2, padx =5 , pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W
        )

        self._othello_canvas = tkinter.Canvas(
            master= self._root_window, width = 500, height = 500,
            background = _background_color)

        self._othello_canvas.grid(
            row = 3 , column = 0, columnspan = 2 , padx =10, pady=10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W
        )

        self.current_message_string = tkinter.StringVar()
        self.current_message = tkinter.Label(self._root_window, textvariable = self.current_message_string)
        self.current_message.grid(
            row = 3, column = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)


        self.current_score_string = tkinter.StringVar()
        self.current_score = tkinter.Label(
            master= self._root_window, textvariable = self.current_score_string
        )
        self.current_score.grid(
            row = 4, column = 2 , padx=10, pady=10,
            sticky = tkinter.E + tkinter.S
        )

        self._othello_canvas.bind('<Configure>',self.othello_canvas_resized)
        self._othello_canvas.bind('<Button-1>',self.othello_canvas_clicked)
        self.button1.bind('<Button-1>', self.start_game_clicked)

        self.initial_board_drawn = False

        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 0)
        self._root_window.rowconfigure(2, weight = 0)
        self._root_window.rowconfigure(3, weight = 3)
        self._root_window.rowconfigure(4, weight = 3)
        self._root_window.rowconfigure(5, weight = 0)
        self._root_window.rowconfigure(6, weight = 0)
        self._root_window.rowconfigure(7, weight = 0)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)
        self._root_window.columnconfigure(2, weight = 0)

        self.board_size_input()
        self.top_left_piece_input()
        self.game_turn_input()
        self.win_method_input()

    def start(self):
        self._root_window.mainloop()

    def board_size_input(self):
        # dimensison of board input
        self.row_input = tkinter.StringVar()
        self.column_input = tkinter.StringVar()

        self.column_option = ttk.Combobox(
            master = self._root_window, textvariable = self.column_input
        )
        self.column_option['value'] = ('Select # Columns','4','6','8','10','12','14','16')
        self.column_option.current(0)
        self.column_option.grid(column=1,row=0)

        self.row_option = ttk.Combobox(
            master= self._root_window, textvariable = self.row_input
        )
        self.row_option['value'] = ('Select # Rows','4','6','8','10','12','14','16')
        self.row_option.current(0)
        self.row_option.grid(column=1,row=1)

    def top_left_piece_input(self):
        # choose color piece in top left corner
        self.top_left_input = tkinter.StringVar()

        self.top_left_option = ttk.Combobox(
            master = self._root_window, textvariable = self.top_left_input
        )
        self.top_left_option['value']= ('Color on top left','B','W')
        self.top_left_option.current(0)
        self.top_left_option.grid(column= 0, row =1)



    def game_turn_input(self):
        self.player_turn_input = tkinter.StringVar()
        self.player_turn_option = ttk.Combobox(
            master= self._root_window, textvariable = self.player_turn_input
        )

        self.player_turn_option['value']= ('Player Move First','B','W')
        self.player_turn_option.current(0)
        self.player_turn_option.grid(column=1, row =2)

    def win_method_input(self):
        self.win_way_input = tkinter.StringVar()
        self.win_way_option = ttk.Combobox(
            master = self._root_window, textvariable = self.win_way_input
        )

        self.win_way_option['value']= ('Way to Win','Most pieces', 'Least pieces')
        self.win_way_option.current(0)
        self.win_way_option.grid(column = 0, row =2)


    def _draw_one_square_in_abs_coord(self,x1,y1,x2,y2):
        self._othello_canvas.create_rectangle(x1,y1,x2,y2,outline ='black',fill='blue')

    def draw_a_circle_piece_black(self,x1,y1,x2,y2):
        current_width = self._othello_canvas.winfo_width()
        current_height = self._othello_canvas.winfo_height()

        self._othello_canvas.create_oval(current_width * x1,current_height * y1,current_width * x2,current_height * y2,fill='black')

    def draw_a_circle_piece_white(self,x1,y1,x2,y2):
        current_width = self._othello_canvas.winfo_width()
        current_height = self._othello_canvas.winfo_height()

        self._othello_canvas.create_oval(current_width * x1,current_height * y1,current_width * x2,current_height * y2,fill='white')

    def create_board(self,row,column,turn):

        self.board=[]   # self.board is list of all the spot coordinate in term of reactangle shape ([x1,y1,x2,y2])

        self.game_turn = turn
        self.other_piece= White_player

        self.game_board_column = column
        self.game_board_row = row

        current_width = self._othello_canvas.winfo_width()
        current_height = self._othello_canvas.winfo_height()


        self.each_x= current_width/row
        self.each_y= current_height/column

        x1=0.0
        y1=0.0

        x2= self.each_x / current_width
        y2= self.each_y/ current_height

        for i in range(row):

            for i in range(column):
                self.board.append([(x1),(y1),(x2),(y2)])
                y1 = y2
                y2 += self.each_y/current_height
            x1 = x2
            x2 += self.each_x/ current_width
            y1 = 0.0
            y2 = self.each_y/ current_height
        print("coordinate of all possible rectangle on board", self.board)


        for each_square in (self.board):
            self._draw_one_square_in_abs_coord((current_width * each_square[0]),(current_height * each_square[1]),(current_width * each_square[2]),(current_height * each_square[3]))


        self.draw_pieces_at_begin(self.game_turn)

        self.display_game_turn(self.game_turn)

    def start_game_clicked(self,event: tkinter.Event):
        # when the button start game click, generate the board with all info
        num_row = int(self.row_option.get())

        num_column = int(self.column_option.get())

        top_left_color = self.top_left_option.get()

        player_turn = self.player_turn_option.get()

        self.current_player = player_turn

        self.create_board(num_row,num_column,self.current_player)

        global game_state

        game_state = othello_logic.Othello_game_state(num_row,num_column,self.current_player)
        self.other_piece = game_state.convert_two_player()

        self.game_current_board = game_state.pieces_at_game_begin(self.current_player,self.other_piece)

        game_state.location_same_color_piece()
        self.current_player_list = game_state.location_list # current_player coordinate on list coordinate

        self.initial_board_drawn = True


    def display_game_turn(self,player):
        if player == 'B':
            self.current_message_string.set ("Black: Make a Move")
        elif player == 'W':
            self.current_message_string.set ("White: Make a Move")

    def total_current_score(self):
        pass

    def draw_pieces_at_begin(self,player):

        self.each_x_frac = self.each_x / self._othello_canvas.winfo_width()
        self.each_y_frac = self.each_y / self._othello_canvas.winfo_height()


        top_left_x = self.center_x - self.each_x_frac
        top_left_y = self.center_y - self.each_y_frac

        low_right_x = self.center_x + self.each_x_frac
        low_right_y = self.center_y + self.each_y_frac


        if player == 'B': # black at left corner
            self.draw_a_circle_piece_black(top_left_x,top_left_y,self.center_x,self.center_y)
            self.draw_a_circle_piece_black(self.center_x,self.center_y,low_right_x,low_right_y)
            self.draw_a_circle_piece_white(self.center_x - self.each_x_frac,self.center_y,self.center_x,self.center_y + self.each_y_frac)
            self.draw_a_circle_piece_white(self.center_x,self.center_y - self.each_y_frac, self.center_x + self.each_x_frac,self.center_y)


        elif player == 'W':
            self.draw_a_circle_piece_white(top_left_x,top_left_y,self.center_x,self.center_y)
            self.draw_a_circle_piece_white(self.center_x,self.center_y,low_right_x,low_right_y)
            self.draw_a_circle_piece_black(self.center_x - self.each_x_frac,self.center_y,self.center_x,self.center_y + self.each_y_frac)
            self.draw_a_circle_piece_black(self.center_x,self.center_y - self.each_y_frac, self.center_x + self.each_x_frac,self.center_y)

    def othello_canvas_clicked(self,event:tkinter.Event):
        # User makes a move by clicking on the board
        current_width = self._othello_canvas.winfo_width()
        current_height = self._othello_canvas.winfo_height()

        y_move = int(event.y/current_width)+1
        x_move = int(event.x/current_height)+1

        print(event.y,event.x)
        print("this is current hei, wid",current_height,current_width)
        print(y_move,x_move)

        game_state.location_same_color_piece()
        self.current_player_list = game_state.location_list
        game_state.adjacent_spot_flip_list_move()
        self.game_current_board = game_state.make_a_move(x_move,y_move)

    def redraw_game_board(self):
        self.board=[]   # self.board is list of all the spot coordinate in term of reactangle shape ([x1,y1,x2,y2])

        self.game_turn = self.player_turn_option.get()


        self.game_board_column = int(self.column_option.get())
        self.game_board_row = int(self.row_option.get())

        current_width = self._othello_canvas.winfo_width()
        current_height = self._othello_canvas.winfo_height()


        self.each_x= current_width/self.game_board_row
        self.each_y= current_height/self.game_board_column

        x1=0.0
        y1=0.0

        x2= self.each_x / current_width
        y2= self.each_y/ current_height

        for i in range(self.game_board_row):

            for i in range(self.game_board_column):
                self.board.append([(x1),(y1),(x2),(y2)])
                y1 = y2
                y2 += self.each_y/current_height
            x1 = x2
            x2 += self.each_x/ current_width
            y1 = 0.0
            y2 = self.each_y/ current_height
        print("coordinate of all possible rectangle on board", self.board)


        for each_square in (self.board):
            self._draw_one_square_in_abs_coord((current_width * each_square[0]),(current_height * each_square[1]),(current_width * each_square[2]),(current_height * each_square[3]))

        self.draw_pieces_at_begin(self.game_turn)

        self.display_game_turn(self.game_turn)

    def othello_canvas_resized(self, event:tkinter.Event):
        if self.initial_board_drawn == True:
            self._othello_canvas.delete(tkinter.ALL)
            self.redraw_game_board()




if __name__ == '__main__':
    game = GUI_Othello()
    game.start()