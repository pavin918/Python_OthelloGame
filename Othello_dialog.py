#Paul Dao Lab Sec 3 Lab Asst 5 Python 3.3

import tkinter

default_font = ('Helvetica', 14)

class Dialog:
    def __init__(self):
        self._dialog_window = tkinter.Tk()

        self._dialog_window.title('New Game')

        row_label = tkinter.Label(master = self._dialog_window, text = 'How many rows do you want?',
                                  font = default_font)

        row_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.N +tkinter. S)

        rows_and_cols = [4, 6, 8, 10, 12, 14, 16]
        
        self.num_rows = tkinter.IntVar()
        self.num_rows.set(rows_and_cols[0])
        row_options = tkinter.OptionMenu(self._dialog_window, self.num_rows, *rows_and_cols)
        row_options.grid(row = 0, column = 2, sticky = tkinter.E + tkinter.N + tkinter.S)
    
        col_label = tkinter.Label(master = self._dialog_window, text = 'How many columns do you want?',
                                  font = default_font)

        col_label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.N +tkinter. S)

        self.num_cols = tkinter.IntVar()
        self.num_cols.set(rows_and_cols[0])
        col_options = tkinter.OptionMenu(self._dialog_window, self.num_cols, *rows_and_cols)

        col_options.grid(row = 1, column = 2, sticky = tkinter.E + tkinter.N + tkinter.S)
        

        first_move = tkinter.Label(master = self._dialog_window, text = 'Who will go first?',
                                   font = default_font)
                                   
        first_move.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.N +tkinter. S)

        self.your_move = tkinter.StringVar()
        self.your_move.set('B')
        b_button = tkinter.Radiobutton(master = self._dialog_window, text = 'Black', variable = self.your_move, value = 'B')
        b_button.grid(row = 2, column = 1, sticky = tkinter.E + tkinter.N + tkinter.S)
        w_button = tkinter.Radiobutton(master = self._dialog_window, text = 'White', variable = self.your_move, value = 'W')
        w_button.grid(row = 2, column = 2, sticky = tkinter.E + tkinter.N + tkinter.S)

        position = tkinter.Label(master = self._dialog_window, text = 'Who will be in the top-left corner of the default position of the pieces?',
                                 font = default_font)

        position.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.N +tkinter. S)

        self.def_pos = tkinter.StringVar()
        self.def_pos.set('B')
        b_button2 = tkinter.Radiobutton(master = self._dialog_window, text = 'Black', variable = self.def_pos, value = 'B')
        b_button2.grid(row = 3, column = 1, sticky = tkinter.E + tkinter.N + tkinter.S)
        w_button2 = tkinter.Radiobutton(master = self._dialog_window, text = 'White', variable = self.def_pos, value = 'W')
        w_button2.grid(row = 3, column = 2, sticky = tkinter.E + tkinter.N + tkinter.S)
        
        winning_method = tkinter.Label(master = self._dialog_window, text = 'Who will win?',
                                       font = default_font)

        winning_method.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.N +tkinter. S)

        self.win_method = tkinter.StringVar()
        self.win_method.set('M')
        m_button = tkinter.Radiobutton(master = self._dialog_window, text = 'Most', variable = self.win_method, value = 'M')
        m_button.grid(row = 4, column = 1, sticky = tkinter.E + tkinter.N + tkinter.S)
        f_button = tkinter.Radiobutton(master = self._dialog_window, text = 'Fewest', variable = self.win_method, value = 'F')
        f_button.grid(row = 4, column = 2, sticky = tkinter.E + tkinter.N + tkinter.S)


     
        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)

        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

        self._dialog_window.rowconfigure(2, weight = 1)
        self._dialog_window.columnconfigure(2, weight = 1)

        self._dialog_window.rowconfigure(3, weight = 1)

        self._dialog_window.rowconfigure(4, weight = 1)

        self._dialog_window.rowconfigure(5, weight = 1)

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(row = 5, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(master = button_frame, text = 'OK', font = default_font,
                                   command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = default_font,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)


        self._ok_clicked = False
        self.row = 0
        self.col = 0
        self.move = ''
        self.default = ''
        self.win = ''
    def start(self):
        self._dialog_window.mainloop()
    def was_ok_clicked(self) -> bool:
        return self._ok_clicked
    
    def return_num_rows(self):
        return self._row

    def return_num_cols(self):
        return self._col

    def return_your_move(self):
        return self._move

    def return_def_pos(self):
        return self._default

    def return_win_method(self):
        return self._win

    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self.row = self.num_rows.get()
        self.col = self.num_cols.get()
        self.move = self.your_move.get()
        self.default = self.def_pos.get()
        self.win = self.win_method.get()
        self._dialog_window.destroy()


    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()

