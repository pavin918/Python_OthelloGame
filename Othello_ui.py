#Paul Dao Lab Section 3 Assignment 4 Python 3.3

import Othello_logic

def board(boardtype:str) -> int:
    '''Asks the user for the column size of the board and returns that input'''
    while True:
        try:
            columns = int(input('''Please specify the number of {} you would like on the board.
    Please note that the number should be an even integer between 4 and 16: '''.format(boardtype)))
            if columns >= 4 and columns <= 16 and str(columns / 2)[-1] == '0':
                return columns
            else:
                print('I am sorry that number was not an even integer between 4 and 16')
        except:
            print('Sorry that was not an integer.')

def black_or_white(piece: str) -> str:
    '''Returns color piece'''
    while True:
        if piece == 'B' or piece == 'W':
            return piece
        else:
            print("Sorry that was neither 'b' nor 'w'.")

def first_and_default(something: str) -> str:
    '''Asks the user if black or white should move first and returns that input'''
    while True:
        move1 = input('''Please specify {}
    -Press 'b' for black
    -Press 'w' for white: '''.format(something)).upper().strip()
        if move1 == 'B' or move1 == 'W':
            return move1
        else:
            print("Sorry that was neither 'b' nor 'w'.")

def win_method() -> str:
    '''Asks the user how victory should be determined'''
    while True:
        win = input('''Please select how victory should be determined
    -Press 'm' for most discs on the board at the end of the game
    -Press 'f' for fewest discs on the board ar the end of the game: ''').upper()
        if win == 'M' or win == 'F':
            return win
        else:
            print("Sorry that was neither 'm' nor 'f'.")

def move(place: str, rnum: int) -> int:
    '''Returns the row number the player wants to place a piece in'''
    while True:
        try:
            move = int(input('Please enter a {} number 1-{}: '.format(place, rnum)))
            return move
        except ValueError:
            print('Sorry that was not a number')

def display_board(board: [[str]], rows: int, columns: int) -> None:
        '''Creates and displays the game board'''
        s = '   '
        for i in range(columns):
            if i > 8:
                s += str(i + 1) + ' '
            else:
                s += str(i + 1) + '  '
        s += '\n'


        for row in range(rows):
            if row > 8:
                s += str(row + 1) + ' '
            else:    
                s += str(row + 1) + '  '
            for col in range(columns):
                if board[row][col] == ' ':
                    s += '.  '
                else:
                    s += board[row][col] +  '  '
                
            s += '\n'
        print(s)

def print_turn(currentmove):
    print("It is {}'s turn".format(currentmove))

def ui():
    '''Executes the game'''
    []
    BOARD_ROWS = board("rows")
    BOARD_COLUMNS = board("columns")
    FIRST = first_and_default('who should go first')
    DEFAULT = first_and_default('which color piece is in the top left-position in the default')
    WIN = win_method()
    a = Othello_logic.OthelloGameState(BOARD_ROWS, BOARD_COLUMNS, FIRST, DEFAULT, WIN)
    b = a.new_board()
    d = a.default_board()
    while True:
        display_board(d, BOARD_ROWS, BOARD_COLUMNS)
        print_turn(a.current_move())
        r = move('row', BOARD_ROWS) - 1
        c = move('column', BOARD_COLUMNS) - 1
        try:
            a.place_piece(r, c)
            a.count_pieces()
            print('SCORE:\nBlack:', a._numB, '\nWhite:', a._numW)
            a.change_turn()
            if a.current_move() == a.turn_pass():
                pass
            else:
                if a.current_move() == a.turn_pass():
                    print(a.opposite_turn(), 'has no more moves.', a.opposite_turn(), 'passes.')
                else:
                    if a.victor() == a._BLACK:
                        print ('No more moves can be made.\nBLACK WINS!')
                        break
                    elif a.victor() == a._WHITE:
                        print ('No more moves can be made.\nWHITE WINS!')
                        break
                    elif a.victor() == '':
                        print ("No more moves can be made.\nIt is a TIE.")
                        break
                    else:
                        pass
        except Othello_logic.InvalidMove:
            print('Sorry. That was an invalid move.')
        except Othello_logic.InvalidRowColumn:
            print('Sorry. That row and/or column does not exist')
    display_board(d, BOARD_ROWS, BOARD_COLUMNS)

if __name__ == '__main__':
    ui()
