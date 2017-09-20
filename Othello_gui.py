#Paul Dao Lab Sec 3 Lab Asst 5 Python 3.3
import tkinter
import Othello_logic
import Othello_dialog

class Display:
    def __init__(self, row: int, col: int, first: str, default: str, win: str):
        self._root_window = tkinter.Tk()

        self._logic = Othello_logic.OthelloGameState(row, col, first, default, win)
        self._new_game = self._logic.new_board()
        self._game_time = self._logic.default_board()

        self._columns = col
        self._rows = row
        self._first = first
        self._default = default
        self._win = win

        self._root_window.title('Othello')

        self._frame = tkinter.Frame(master = self._root_window, background = '#F50C0C')

        self._frame.grid(
            row = 0, columnspan = 3, padx = 5, pady = (5, 0),
            sticky = tkinter.NSEW)
        
        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 500, height = 500,
            background = '#187330')

        self._black_count = tkinter.Label(master = self._frame, text = ('Black: ' + str(self._logic._numB)), font = ('Helvetica', 16), background = '#F50C0C')
        self._black_count.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = tkinter.NSEW)
        self._white_count = tkinter.Label(master = self._frame, text = ('White: ' + str(self._logic._numW)), font = ('Helvetica', 16), background = '#F50C0C')
        self._white_count.grid(row = 0, column = 2, padx = 5, pady = 5, sticky =  tkinter.NSEW)

        self._color = ''

        self._black_turn = "Black's turn"
        self._white_turn = "White's turn"

        if self._first == 'B':
            self._color = 'black'
            self._turn = tkinter.Label(master = self._frame, text = self._black_turn, font = ('Helvetica', 16), background = '#F50C0C')
            self._turn.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = tkinter.N + tkinter.S)
        else:
            self._color = 'white'
            self._turn = tkinter.Label(master = self._frame, text = self._white_turn, font = ('Helvetica', 16), background = '#F50C0C')
            self._turn.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = tkinter.N + tkinter.S)

        self._canvas.grid(
            row = 1, column = 0, padx = 3, pady = 5,
            sticky = tkinter.NSEW)

        self._frame.rowconfigure(0, weight = 1)
        self._frame.columnconfigure(0, weight = 1)
        self._frame.columnconfigure(1, weight = 1)
        self._frame.columnconfigure(2, weight = 1)
        
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)


        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 8)
        self._root_window.columnconfigure(0, weight = 1)

        self._col_width = 0
        self._row_height = 0

    def start(self) -> None:
        '''Starts the Othello game'''
        self._root_window.mainloop()

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        '''Creates a black or white piece in the cell clicked and redraws the board and pieces'''
        self._redraw_all_spots(event)
        self._place_pieces(event)
        
    def _draw_board(self):
        '''Draws the default board with the pieces in place and displays the default piece count(or number of pieces)'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        self._col_width = (canvas_width)/ self._columns
        self._row_height = (canvas_height)/ self._rows
        for row in range(1, self._rows):
            self._canvas.create_line(0, (canvas_height * (row / self._rows)), canvas_width, (canvas_height * (row / self._rows)))
            for col in range(1, self._columns):
                self._canvas.create_line((canvas_width * (col / self._columns)), 0, (canvas_width * (col / self._columns)), canvas_height)
        for row in range(self._rows):
            for col in range(self._columns):
                if self._game_time[row][col] == 'W':
                    self._canvas.create_oval(self._col_width * col, self._row_height * row, (self._col_width * (col + 1)), (self._row_height * (row + 1)), fill = 'white')
                elif self._game_time[row][col] == 'B':
                    self._canvas.create_oval(self._col_width * col, self._row_height * row, (self._col_width * (col + 1)), (self._row_height * (row + 1)), fill = 'black')
                else:
                    pass
        self._logic.count_pieces()
        self._black_count['text'] = 'Black: ' + str(self._logic._numB)
        self._white_count['text'] = 'White: ' + str(self._logic._numW)

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''Calls on the function that redraws the board, lines, pieces, turn, and number of pieces for black and white every time the board is reconfigured'''
        # Whenever the Canvas' size changes, redraw all of the spots,
        # since their sizes have changed, too.
        self._redraw_all_spots(event)

    def _redraw_all_spots(self, event: tkinter.Event) -> None:
        '''Redraws the board, lines, pieces, turn, and number of pieces for black and white every time the board is reconfigured'''
        self._canvas.delete(tkinter.ALL)
        self._draw_board()

    def _place_pieces(self, event: tkinter.Event):
        '''Places the pieces in the cell that was clicked and does not allow a piece placement when a line or intersection of lines is clicked'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        self._col_width = (canvas_width) / self._columns
        self._row_height = (canvas_height) / self._rows
        for row in range(self._rows):
            for col in range(self._columns):
                if (event.x > (self._col_width * col)) and event.x < (self._col_width * (col + 1)) and (event.y > self._row_height * row) and (event.y < self._row_height * (row + 1)):
                    x_index = int((event.y) // self._row_height)   #If the click happens in the area bounded by the lines described in the above 'if' statement
                    y_index = int((event.x) // self._col_width)    #the index for for row and column for placing the piece onto the board will be created
                    
                    try: #In the try statement, the game logic is applied and a 'B' or 'W' is placed onto the board and represented as a black or white oval.
                         #The score is also displayed.
                        
                        self._logic.place_piece(x_index, y_index)
                        self._logic.count_pieces()
                        self._black_count['text'] = 'Black: ' + str(self._logic._numB)
                        self._white_count['text'] = 'White: ' + str(self._logic._numW)
                        self._canvas.create_oval(self._col_width * col, self._row_height * row, (self._col_width * (col + 1)), (self._row_height * (row + 1)), fill = self._color)
                        
                    except Othello_logic.InvalidMove:
                        pass
                    
                    except Othello_logic.InvalidRowColumn:
                        pass
                    
                    else: #After the 'try' statement is successful, the turn will change and the game will show who's turn it is.
                        self._logic.change_turn()
                        
                        if self._logic.current_move() == 'B':
                            self._turn["text"] = self._black_turn
                            
                        else:
                            self._turn["text"] = self._white_turn
                            
                        if self._logic.current_move() == self._logic.turn_pass():
                            pass                                                  
                        
                        else:
                            if self._logic.current_move() == self._logic.turn_pass():#After the current turn's player has made a move, and the other player has
                                                                                     #no valid moves, then the turn will go back to the current player    
                                if self._logic.current_move() == 'B':
                                    self._turn['text'] = self._black_turn
                                    
                                else:
                                    self._turn['text'] = self._white_turn
                                
                            else: #If both players can't make a move, the game ends and whoever has the most or fewest will win and the game will show who wins
                                if self._logic.victor() == self._logic._BLACK:
                                    self._turn["text"] = 'No more moves. Black wins!'
                                    break
                                
                                elif self._logic.victor() == self._logic._WHITE:
                                    self._turn["text"] = 'No more moves. White wins!'
                                    break
                                
                                elif self._logic.victor() == '':
                                    self._turn["text"] = 'No more moves. It is a tie'
                                    break
                                
                                else:
                                    pass
                                
                else:
                    pass
        self._draw_board()

if __name__ == '__main__':
    b = Othello_dialog.Dialog()
    b.start()
    a = Display(b.row, b.col, b.move, b.default, b.win)
    a.start()
