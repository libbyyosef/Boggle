from ex12_utils import *
from boggle_board_randomizer import *
from constant import *


def open_file():
    """function opens boggle dictionary from file and returns them as a list"""
    with open('boggle_dict.txt') as b:
        text = b.read().split('\n')
        return text


def show_and_run(window):
    """show and run the relevant window"""
    window.show()
    window.run()


class Boggle:
    def __init__(self):
        """function builds board, with 0 points and 0 words guessed"""
        self.__board = randomize_board()
        self.__words_collection = open_file()
        self.__points = 0
        self.__current_word = ''
        self.__current_word_currs = []
        self.__all_words = []
        self.__letter_delete = None

    def update_score_correct_word_b(self, len_word, score, headline_score):
        """function adds to score len of guessed word in power of 2"""
        self.__points += len_word ** POWER_POINTS
        score['text'] = f'{headline_score} {self.__points}'

    def get_points(self):
        """function returns points"""
        return self.__points

    def get_letter_delete(self):
        return self.__letter_delete

    def undo_word(self, curr):
        """function undoes selection of last letter"""
        if len(self.__current_word) > 0 and len(self.__current_word_currs):
            self.__letter_delete = self.__board[curr[0]][curr[1]]
            self.__current_word = self.__current_word[:-(len(
                self.__letter_delete))]
            self.__current_word_currs.remove(curr)

    def update_current_word_b(self, letter, curr):
        """adds coordinate to current word currs, and adds letter on
        coordinate's cell to current word if coordinate is legal"""
        if curr not in self.__current_word_currs:
            self.__current_word_currs.append(curr)
            if check_path_coordinates(self.__current_word_currs, self.__board):
                self.__current_word += letter
            else:
                self.__current_word_currs.remove(curr)

    def get_current_word(self):
        """function returns current word"""
        return self.__current_word

    def get_word_currs(self):
        """returns current words coordinates"""
        return self.__current_word_currs

    def enter_word_b(self):
        """checks if entered word was not chosen yet and in words collection
        and that words currs are legal, if so, adds to all words the word and
        returns True"""
        check = False
        if self.__words_collection and check_path_coordinates(
                self.__current_word_currs,
                self.__board) and self.__current_word \
                not in self.__all_words and self.__current_word in \
                self.__words_collection:
            self.__all_words.append(self.__current_word)
            check = True
        return check

    def clear_guess_box(self):
        """function clears string from guess box"""
        self.__current_word = ''
        self.__current_word_currs.clear()

    def is_fine_path(self):
        """checks if coordinates of current word are legal"""
        if check_path_coordinates(self.__current_word_currs, self.__board):
            return True

    def get_board(self):
        """function returns board"""
        return self.__board
