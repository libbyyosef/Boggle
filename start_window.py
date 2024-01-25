from tkinter import *
from constant import *


class StartWindow:
    """creates an object of the start window"""
    def __init__(self, root, game):
        """initialize the start window"""
        self.__window = root
        self.__title = START_TITLE
        self.__window.geometry(f'{WINDOW_SIZE_WIDTH}x{WINDOW_SIZE_HEIGHT}')
        self.__window.resizable(False, False)
        self.__bg = None
        self.__frame = None
        self.__label = None
        self.__start_btn = None
        # game is a method the show game window and hide start window
        self.__game = game
        self.__pack_widgets = []

    def pack_widgets(self):
        """pack the widgets in pack widgets' list"""
        for widget in self.__pack_widgets:
            widget.pack()

    def show(self):
        """creates widget on the tk root"""
        self.__bg = tk.PhotoImage(
            file= START_IMAGE_NAME)
        self.__frame = Frame(self.__window)
        self.__pack_widgets.append(self.__frame)
        self.__label = Label(self.__frame, image=self.__bg)
        self.__pack_widgets.append(self.__label)
        self.__start_btn = Button(self.__frame, text=TEXT_START_BUTTON,
                                  fg=BUTTON_FG_COLOR,
                                  height=HEIGHT_START_BUTTON,
                                  width=WIDTH_START_BUTTON,
                                  bg=BG_START_BUTTON,
                                  command=self.hide)
        self.__start_btn.place(x=START_BUTTON_X, y=START_BUTTON_Y)
        self.pack_widgets()

    def forget_pack_widgets(self):
        """unpack the widget that were created by pack"""
        for widget in self.__pack_widgets:
            widget.pack_forget()

    def hide(self):
        """hides the widgets that were created, the ones that were created
        on the frame disappear when the frame disappear, so there is no need
        to unpack/forget place them also"""
        self.forget_pack_widgets()
        self.__game()

    def run(self):
        """starts run the start window"""
        self.__window.mainloop()
