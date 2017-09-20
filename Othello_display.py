#Python 3.3
import Othello_ui
import Othello_logic

a = Othello_logic.OthelloGameState(Othello_ui.BOARD_ROWS, Othello_ui.BOARD_COLUMNS, Othello_ui.FIRST, Othello_ui.DEFAULT)
b = a.new_board()
c = a.default_board()
a._board
def display_board(board: [[str]], rows: int, columns: int) -> None:
        '''Creates and displays the game board'''
        s = '   '
        for i in range(1, columns + 1):
            if i > 9:
                s += str(i) + ' '
            else:
                s += str(i) + '  '
        s += '\n'


        for row in range(rows):
            if row > 9:
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

##print(a.valid_move(4, 2))
##a.place_piece(4, 2)
####print(a.valid_move(2, 4))
####print(a.valid_move(3, 5))
####print(a.valid_move(5, 3))
####print(a.valid_move(7, 6))
##display_board(c, Othello_ui.BOARD_ROWS, Othello_ui.BOARD_COLUMNS)
##print(a.count_pieces())
##print(a.change_turn())
##print(a.valid_move(5, 2))
##a.place_piece(5, 2)
##display_board(c, Othello_ui.BOARD_ROWS, Othello_ui.BOARD_COLUMNS)
##print(a.change_turn())
##print(a.valid_move(5, 3))
##a.place_piece(5, 3)
##display_board(c, Othello_ui.BOARD_ROWS, Othello_ui.BOARD_COLUMNS)
##print(a.change_turn())
##print(a.valid_move(5, 4))
##a.place_piece(5, 4)
##display_board(c, Othello_ui.BOARD_ROWS, Othello_ui.BOARD_COLUMNS)
##print(a.change_turn())
##print(a.valid_move(6, 5))
##a.place_piece(6, 5)
##display_board(c, Othello_ui.BOARD_ROWS, Othello_ui.BOARD_COLUMNS)
##print(a.change_turn())
##print(a.valid_move(5, 5))
##a.place_piece(5, 5)
##display_board(c, Othello_ui.BOARD_ROWS, Othello_ui.BOARD_COLUMNS)
##print(a.change_turn())
##print(a.valid_move(6, 2))
##a.place_piece(6, 2)
##display_board(c, Othello_ui.BOARD_ROWS, Othello_ui.BOARD_COLUMNS)
##print(a.change_turn())
##print(a.valid_move(7, 5))
##a.place_piece(7, 5)
##display_board(c, Othello_ui.BOARD_ROWS, Othello_ui.BOARD_COLUMNS)
##print(a.change_turn())
##print(a.valid_move(8, 5))
##a.place_piece(8, 5)
##display_board(c, Othello_ui.BOARD_ROWS, Othello_ui.BOARD_COLUMNS)
