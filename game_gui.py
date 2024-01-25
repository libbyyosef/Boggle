from tkinter import *
from boggle_logic import *
from constant import *


class GameGui:
    """creates an object of the game window"""

    def __init__(self, root, end):
        self.__end = end
        self.__root = root
        self.__root.geometry(f'{WINDOW_SIZE_WIDTH}x{WINDOW_SIZE_HEIGHT}')
        self.__root.configure(bg=WINDOW_BACKGROUND_COLOR)
        self.__root.resizable(False, False)
        self.__root.title(HEADLINE_BOGGLE)
        self.__boggle = None
        self.__board = None
        self.__headline = None
        self.__score = None
        self.__buttons = {}
        self.__pushed_buttons = {}
        self.__undo_button = None
        self.__button_exit = None
        self.__clear_button = None
        self.__enter_b = None
        self.__game_frame = None
        self.__chosen_words_frame = None
        self.__words_box = None
        self.__scroller = None
        self.__list_box = None
        self.__current_word_label = None
        self.__mins = MINUTES
        self.__sec = SECONDS
        self.__timer = None
        self.__pack_widgets = []
        self.__place_widgets = []

    def forget_pack_widgets(self):
        """unpack the widget that were created by pack"""
        for widget in self.__pack_widgets:
            widget.pack_forget()

    def forget_place_widget(self):
        """forget the place of the widget in the list of place widgets"""
        for widget in self.__place_widgets:
            widget.place_forget()

    def show(self):
        """created the widgets on the tk window"""
        self.initialize_game()

    def hide(self):
        """remove the widgets from the tk window"""
        score = self.__boggle.get_points()
        for b in self.__buttons.values():
            b.grid_forget()
        self.forget_pack_widgets()
        self.forget_place_widget()
        self.__end(score)

    def initialize_game(self):
        """sets new values to the initial values, creates widgets"""
        self.__boggle = Boggle()
        self.__board = self.__boggle.get_board()
        self.__headline = tk.Label(self.__root, text=HEADLINE_BOGGLE,
                                   font=(FONT_HEADLINE, FONT_SIZE_HEADLINE),
                                   bg=WINDOW_BACKGROUND_COLOR,
                                   fg=HEADLINE_LETTER_COLOR)
        self.__headline.pack(side=tk.TOP)
        self.__pack_widgets.append(self.__headline)
        self.__undo_button = tk.Button(self.__root, text=UNDO_TEXT,
                                       bg=BUTTON_ENTER_BG,
                                       fg=BUTTON_ENTER_FG_COLOR,
                                       font=BUTTON_ENTER_F_STYLE,
                                       borderwidth=BUTTON_ENTER_BORDER_WIDTH,
                                       width=SIZE_BUTTONS_WIDTH,
                                       height=SIZE_BUTTONS_HEIGHT,
                                       highlightbackground=BUTTON_ENTER_HIGHLIGHT_COLOR,
                                       command=self.undo)
        self.__undo_button.place(x=X_SIDE_BUTTONS, y=UNDO_Y)
        self.__place_widgets.append(self.__undo_button)
        self.__clear_button = tk.Button(self.__root, text=CLEAR_TEXT,
                                        bg=BUTTON_ENTER_BG,
                                        fg=BUTTON_ENTER_FG_COLOR,
                                        font=BUTTON_ENTER_F_STYLE,
                                        borderwidth=BUTTON_ENTER_BORDER_WIDTH,
                                        width=SIZE_BUTTONS_WIDTH,
                                        height=SIZE_BUTTONS_HEIGHT,
                                        highlightbackground=BUTTON_ENTER_HIGHLIGHT_COLOR,
                                        command=self.clear_guess)
        self.__clear_button.place(x=X_SIDE_BUTTONS, y=CLEAR_Y)
        self.__place_widgets.append(self.__clear_button)
        self.__button_exit = tk.Button(self.__root, text=EXIT_TEXT,
                                       bg=BUTTON_ENTER_BG,
                                       fg=BUTTON_ENTER_FG_COLOR,
                                       font=BUTTON_ENTER_F_STYLE,
                                       borderwidth=BUTTON_ENTER_BORDER_WIDTH,
                                       width=SIZE_BUTTONS_WIDTH,
                                       height=SIZE_BUTTONS_HEIGHT,
                                       highlightbackground=BUTTON_ENTER_HIGHLIGHT_COLOR,
                                       command=exit)
        self.__button_exit.place(x=X_SIDE_BUTTONS, y=EXIT_Y)
        self.__place_widgets.append(self.__button_exit)
        self.__score = tk.Label(self.__root,
                                text=f'{HEADLINE_SCORE}'
                                     f'{self.__boggle.get_points()}',
                                font=(FONT_HEADLINE, FONT_SIZE_SCORE),
                                bg=WINDOW_BACKGROUND_COLOR, fg=COLOR_SCORE)
        self.__score.place(x=SCORE_X_LOC, y=SCORE_Y_LOC)
        self.__place_widgets.append(self.__score)
        self.__game_frame = tk.Frame(self.__root,
                                     width=(
                                             BUTTONS_WIDTH_RELATIVE_SIZE *
                                             WINDOW_SIZE_WIDTH),
                                     height=(
                                             BUTTONS_HIGHT_RELATIVE_SIZE *
                                             WINDOW_SIZE_HEIGHT),
                                     highlightbackground=BUTTONS_BG_COLOR_FRAME)
        self.__game_frame.place(
            x=WINDOW_SIZE_WIDTH / BUTTONS_WIDTH_RELATIVE_LOC,
            y=WINDOW_SIZE_HEIGHT / BUTTONS_HIGHT_RELATIVE_LOC)
        self.__place_widgets.append(self.__game_frame)
        self.create_buttons(self.__board)
        self.__words_box = tk.Frame(self.__root, width=WORDS_BOX_WIDTH,
                                    height=WORDS_BOX_HIGHT,
                                    highlightbackground=BG_WORDS_BOX_COLOR)
        self.__scroller = tk.Scrollbar(self.__words_box)
        self.__scroller.pack(side=RIGHT, fill=Y)
        self.__pack_widgets.append(self.__scroller)
        self.__list_box = Listbox(self.__words_box,
                                  yscrollcommand=self.__scroller.set,
                                  width=LIST_BOX_WIDTH,
                                  height=LIST_BOX_HIGHT)
        self.__list_box.pack(side=LEFT)
        self.__pack_widgets.append(self.__list_box)
        self.__scroller.config(command=self.__list_box.yview)
        self.__words_box.place(x=WORDS_BOX_X_LOC, y=WORDS_BOX_Y_LOC)
        self.__place_widgets.append(self.__words_box)
        self.create_enter_word_button()
        self.__current_word_label = tk.Listbox(self.__root,
                                               font=FONT_WORD_LABEL,
                                               bg=BG_C_WORD_LABEL,
                                               fg=FG_C_WORD_LABEL,
                                               width=C_WORD_LABEL_WIDTH,
                                               height=C_WORD_LABEL_HEIGHT)
        self.__current_word_label.place(x=C_WORD_LABEL_X, y=C_WORD_LABEL_Y)
        self.__place_widgets.append(self.__current_word_label)
        self.__mins = MINUTES
        self.__sec = SECONDS
        self.__timer = self.create_timer()
        self.update_time()

    def clear_guess(self):
        """erase the word from the current word (label and variable) and
        turns back the bg colors to pink"""
        self.__boggle.clear_guess_box()
        self.__current_word_label.insert(0, '')
        for b in self.__pushed_buttons:
            self.__buttons[b]['bg'] = REGULAR_COLOR
        self.__pushed_buttons = {}

    def create_buttons(self, board):
        """creates the game letters buttons """
        for i in range(len(board)):
            self.__game_frame. \
                grid_columnconfigure(i, weight=BUTTONS_WEIGHT_IN_GAME_FRAME)
        for row in range(len(board)):
            for col, cell in enumerate(board[row]):
                button = tk.Button(self.__game_frame, text=str(cell),
                                   bg=REGULAR_COLOR, fg=BUTTON_FG_COLOR,
                                   font=BUTTON_STYLE,
                                   borderwidth=BUTTON_BORDER_WIDTH,
                                   width=BUTTON_WIDTH,
                                   height=BUTTON_HEIGHT,
                                   command=lambda letter=cell, curr=(
                                       row, col): self.update_current_word(
                                       letter,
                                       curr))
                button.grid(row=row, column=col, sticky=tk.NSEW)
                self.__buttons[(row, col)] = button

    def undo(self):
        """erase the last cube letters and color them pink back"""
        if len(self.__buttons) > 0:
            current_word = self.__boggle.get_current_word()
            current_path = self.__boggle.get_word_currs()
            if len(current_path) > 0:
                self.__buttons[(current_path[-1])]['bg'] = REGULAR_COLOR
                del (self.__pushed_buttons[current_path[-1]])
                self.__boggle.undo_word(current_path[-1])
                letter_delete = self.__boggle.get_letter_delete()
                self.__current_word_label.insert(0, current_word[
                                                    :-len(letter_delete)])

    def update_current_word(self, letter, curr):
        """adds the guess letters to the fit variable and to the current
        word label, as long it  is valid"""
        word_before_update = self.__boggle.get_current_word()
        self.__boggle.update_current_word_b(letter, curr)
        current_word = self.__boggle.get_current_word()
        self.__current_word_label.insert(0, current_word)
        if word_before_update != current_word:
            self.__buttons[curr]['bg'] = 'black'
            self.__pushed_buttons[curr] = self.__buttons[curr]

    def create_enter_word_button(self):
        """creates the enter button"""
        self.__enter_b = tk.Button(self.__root, text=BUTTON_ENTER_TEXT,
                                   bg=BUTTON_ENTER_BG,
                                   fg=BUTTON_ENTER_FG_COLOR,
                                   font=BUTTON_ENTER_F_STYLE,
                                   borderwidth=BUTTON_ENTER_BORDER_WIDTH,
                                   width=BUTTON_ENTER_WIDTH,
                                   height=BUTTON_ENTER_HEIGHT,
                                   highlightbackground=BUTTON_ENTER_HIGHLIGHT_COLOR,
                                   command=lambda: self.enter_word())
        self.__enter_b.place(x=BUTTON_ENTER_X_LOC, y=BUTTON_ENTER_Y_LOC)

    def insert_text(self):
        """add text to the list box,(the current word)"""
        text = self.__boggle.get_current_word()
        self.__list_box.insert(END, ' ' + text)

    def update_score_correct_word(self, len_word):
        """update score if it is valid word guess"""
        self.__boggle.update_score_correct_word_b(len_word, self.__score,
                                                  HEADLINE_SCORE)

    def enter_word(self):
        """when click the enter button, if the guess is valid it adds to
        the visual box of words and to the fit variable, colord all the
        pushed button to pink"""
        if self.__boggle.enter_word_b():
            current_word = self.__boggle.get_current_word()
            self.update_score_correct_word(len(current_word))
            self.insert_text()
        self.clear_guess()

    def create_timer(self):
        """function creates timer for game"""
        timer = tk.Label(self.__root, width=TIMER_WIDTH, height=TIMER_HEIGHT,
                         text=TIMER_TEXT,
                         fg=TIMER_FG, font=(FONT_HEADLINE, TIMER_SIZE))
        timer.place(x=TIMER_PLACE_X, y=TIMER_PLACE_Y)
        return timer

    def update_time(self):
        """function updates timer to be one second less every second"""
        if self.__sec == 0 and self.__mins == 0:
            self.hide()
        else:
            self.__sec -= 1
            if self.__sec < 0:
                self.__mins -= 1
                self.__sec = SECONDS_IN_MINUTE - 1
            min_str = f'{self.__mins}' if self.__mins > 9 \
                else f'0{self.__mins}'
            sec_str = f'{self.__sec}' if self.__sec > 9 else f'0{self.__sec}'
            self.__timer.config(text=min_str + ':' + sec_str)
            self.__timer.after(TIMER_ONE_SECOND, self.update_time)

    def run(self):
        """starts run the game window"""
        self.__root.mainloop()
