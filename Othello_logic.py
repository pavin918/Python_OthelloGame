#Paul Dao Lab Section 3 Assignment 4 Python 3.3

class InvalidMove(Exception):
    pass

class InvalidRowColumn(Exception):
    pass

class OthelloGameState:
    def __init__(self, rows: int, columns: int, first: str, default: str, win: str):
        self._board = []
        self._NONE = ' '
        self._BLACK = 'B'
        self._WHITE = 'W'
        self._COLUMNS = columns
        self._ROWS = rows
        self._turn = first
        if self._turn == self._BLACK:
            self._other = self._WHITE
        else:
            self._other = self._BLACK
        self._DEFAULT = default
        self._numB = 0
        self._numW = 0
        self._win = win
            
    def new_board(self) -> [[str]]:
        '''Makes a new game board with the size of the board columns and board rows
        specified by the user and is made of empty strings'''
        for row in range(self._ROWS):
            self._board.append([])
            for col in range(self._COLUMNS):
                self._board[-1].append(self._NONE)
        return self._board

    def default_board(self) -> [[str]]:
        '''Places the default pieces'''
        if self._DEFAULT == self._BLACK:
            self._board[self._ROWS // 2 - 1][self._COLUMNS // 2 - 1] = self._DEFAULT
            self._board[self._ROWS // 2][self._COLUMNS // 2] = self._DEFAULT
            self._board[self._ROWS // 2 - 1][self._COLUMNS // 2] = self._WHITE
            self._board[self._ROWS // 2][self._COLUMNS // 2 - 1] = self._WHITE
        else:
            self._board[self._ROWS // 2 - 1][self._COLUMNS // 2 - 1] = self._DEFAULT
            self._board[self._ROWS // 2][self._COLUMNS // 2] = self._DEFAULT
            self._board[self._ROWS // 2 - 1][self._COLUMNS // 2] = self._BLACK
            self._board[self._ROWS // 2][self._COLUMNS // 2 - 1] = self._BLACK
        return self._board
        
    def count_pieces(self) -> None:
        '''Prints out the amount of pieces for each color in the current game state'''
        numblack = 0
        numwhite = 0
        for row in range(self._ROWS):
            for col in range(self._COLUMNS):
                if self._board[row][col] == self._BLACK:
                    numblack += 1
                elif self._board[row][col] == self._WHITE:
                    numwhite += 1
        self._numB = numblack
        self._numW = numwhite
                          
    def place_piece(self, row ,col) -> list:
        '''Determines where player can place piece'''
        self.valid_move(row, col)
        self.flip(row,col)
        self._board[row][col] = self.current_move()
        return self._board

    def _is_valid_column_number(self, column_number: int) -> bool:
        '''Returns True if the column number is valid; else, returns False'''
        return 0 <= column_number < self._COLUMNS

    def _is_valid_row_number(self, row_number: int) -> bool:
        '''Returns True if the row number is valid; else, returns False'''
        return 0 <= row_number < self._ROWS
                
    def valid_move(self, row, col) -> [tuple]:
        '''Given a specfic row and specific column, the function checks the immediate surrounding
        area for a piece of the opposite color continues to check in that direction until it finds the
        current turn's color, empty space, or the end of the board. Returns list of coordinates of pieces that will be flipped
        if the move is valid or returns invalid.'''
        valid = []
        area = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,-1), (-1,1)]
        if self._is_valid_row_number(row) and self._is_valid_column_number(col):
            if self._board[row][col] == ' ':
                for xdelta, ydelta in area:
                    try:
                        if self._board[row + xdelta][col + ydelta] == self.opposite_turn():
                            local_valid = []
                            xdel = row + xdelta
                            ydel = col + ydelta
                            while True:
                                if self._board[xdel][ydel] == self.opposite_turn():                                
                                    local_valid.append((xdel,ydel))
                                    xdel += xdelta
                                    ydel += ydelta
                                if (self._board[xdel][ydel] == ' ')\
                                   or ((xdel > self._ROWS or xdel < 0) or (ydel > self._COLUMNS or ydel < 0)):
                                    break
                                elif self._board[xdel][ydel] == self.current_move():
                                    valid.extend(local_valid)
                                    break
                    except:
                        pass
                if valid == []:
                    raise InvalidMove()

            else:
                raise InvalidMove()
        else:
            raise InvalidRowColumn()
        return valid

    def flip(self, row, col) -> [[str]]:
        '''Takes coordinates of valid_move function and changes the pieces of opposite turn's pieces to the current_move's pieces'''
        for x, y in self.valid_move(row,col):
            self._board[x][y] = self.current_move()
        return self._board

    def current_move(self) -> str:
        '''Defines whose move it is'''
        return self._turn

    def opposite_turn(self) -> str:
        '''Defines who is opponent'''
        if self.current_move() == self._BLACK:
            return self._WHITE
        else:
            return self._BLACK
    
    def change_turn(self) -> str:
        '''Given which player's turn it is, it returns the opposite player's turn'''
        self._turn = self.opposite_turn()
        return self._turn

    def turn_pass(self) -> str:
        '''Automatically changes the turn to the opposite player when there is no more valid moves left on the board
        for the current player's turn'''
        for row in range(self._ROWS):
            for col in range(self._COLUMNS):
                if self._board[row][col] == ' ':
                    try:
                        self.valid_move(row, col)
                    except InvalidMove:
                        pass
                    else:
                        return self.current_move()
        return self.change_turn()        
        
    def victor(self) -> str:
        '''Determines the victor'''
        if self._win == 'F':
            if self._numB < self._numW:
                return self._BLACK
            elif self._numB > self._numW:
                return self._WHITE
            else:
                return ''
        elif self._win == 'M':
            if self._numB > self._numW:
                return self._BLACK
            elif self._numB < self._numW:
                return self._WHITE
            else:
                return ''
