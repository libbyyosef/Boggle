from tkinter import *
from constant import *


class GameEnds:
    def __init__(self, root, start, score):
        self.__window = root
        self.__title = END_TITLE
        self.__window.geometry(f'{WINDOW_SIZE_WIDTH}x{WINDOW_SIZE_HEIGHT}')
        self.__window.resizable(False, False)
        self.__bg = None
        self.__big_frame = None
        self.__label_pic = None
        self.__frame = None
        self.__yes_btn = None
        self.__no_btn = None
        self.__label = None
        # variable of the final score
        self.__score = score
        # method play again
        self.__start = start
        self.__pack_widgets = []
        self.__place_widgets = []

    def show(self):
        """creates the widgets on the tk window"""
        self.__bg = tk.PhotoImage(
            file= NAME_IMAGE_END)
        self.__label_pic = Label(self.__window, image=self.__bg)
        self.__label_pic.place(x=LABEL_RESTART_X, y=LABEL_RESTART_Y)
        self.__place_widgets.append(self.__label_pic)
        self.__frame = Frame(self.__window)
        self.__frame.pack()
        self.__pack_widgets.append(self.__frame)
        self.__yes_btn = Button(self.__window, text=BUTTON_YES_TEXT,
                                fg=BUTTON_FG_COLOR,
                                height=BUTTON_END_HEIGHT,
                                width=BUTTON_END_WIDTH,
                                bg=BG_START_BUTTON, command=self.hide)
        self.__no_btn = Button(self.__window, text=BUTTON_NO_TEXT,
                               fg=BUTTON_FG_COLOR, height=BUTTON_END_HEIGHT,
                               width=BUTTON_END_WIDTH,
                               bg=BG_START_BUTTON, command=exit)
        self.__yes_btn.place(x=BUTTON_YES_X, y=BUTTON_YES_Y)
        self.__no_btn.place(x=BUTTON_NO_X, y=BUTTON_NO_Y)
        self.__place_widgets.append(self.__yes_btn)
        self.__place_widgets.append(self.__no_btn)
        self.__label = Label(self.__window, text=f'{TEXT_FINAL_LABEL_1}'
                                                 f'{self.__score} \n '
                                                 f'{TEXT_FINAL_LABEL_2}',
                             bg=BG_FINAL_LABEL, fg=BG_START_BUTTON,
                             height=FINAL_LABEL_HEIGHT, font=FINAL_LABEL_FONT,
                             width=FINAL_LABEL_WIDTH)
        self.__label.place(x=FINAL_LABEL_X, y=FINAL_LABEL_Y)
        self.__place_widgets.append(self.__label)

    def pack_hide(self):
        """unpack the widgets"""
        for widget in self.__pack_widgets:
            widget.pack_forget()

    def place_hide(self):
        """forget the widgets' place"""
        for widget in self.__place_widgets:
            widget.place_forget()

    def hide(self):
        """unpack/hide the widget on the tk window, creates the start window"""
        self.pack_hide()
        self.place_hide()
        self.__start()

    def run(self):
        """starts run the end window"""
        self.__window.mainloop()
