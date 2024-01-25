from start_window import *
from game_gui import *
from boggle_logic import *
from game_ends_window import *


class Control:
    """an object that control the other objects of the game"""
    def __init__(self):
        """initialize the control object"""
        self.__root = tk.Tk()
        self.__game = None
        self.__end = None
        self.__start = None

    def start(self):
        """the method creates the widgets of the first window on the tk root"""
        self.__start = StartWindow(self.__root, self.game)
        show_and_run(self.__start)

    def game(self):
        """the method creates the widgets of the game window on the tk root
        and hides the widgets of the first window"""
        self.__game = GameGui(self.__root, self.end)
        show_and_run(self.__game)

    def end(self, score):
        """the method creates the widgets of the end window on the tk root
                and hides the widgets of the game window, if the player
                wants another game , it called the start method that show
                the first window widgets, otherwise it exits the program"""
        self.__end = GameEnds(self.__root, self.start, score)
        show_and_run(self.__end)


if __name__ == "__main__":
    """creates a control object and activate it when the player open the 
    program"""
    controller = Control()
    controller.start()
