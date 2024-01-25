import tkinter as tk

######################
POWER_POINTS = 2
######################
######################
# images
START_IMAGE_NAME = 'background.png'
NAME_IMAGE_END = 'game_over.png'
########################
######start window######
START_TITLE = 'start'
TEXT_START_BUTTON = 'Click To Start'
HEIGHT_START_BUTTON = 3
WIDTH_START_BUTTON = 20
BG_START_BUTTON = 'pink'
START_BUTTON_X = 530
START_BUTTON_Y = 200
######################
#######game###########
# HEADLINE BOGGLE
HEADLINE_BOGGLE = 'Boggle'
FONT_HEADLINE = 'Helvetice'
FONT_SIZE_HEADLINE = 40
HEADLINE_BOGGLE_COLOR = 'plum2'
HEADLINE_LETTER_COLOR = 'white'

######################
# score
COLOR_SCORE = 'white'
HEADLINE_SCORE = 'score: '
FONT_SIZE_SCORE = 30
SCORE_X_LOC = 20
SCORE_Y_LOC = 10

######################
# window
WINDOW_SIZE_HEIGHT = 500
WINDOW_SIZE_WIDTH = 700
WINDOW_BACKGROUND_COLOR = 'thistle'

######################
# BOARD_SIZE
BOARD_SIZE_X = 4
BOARD_SIZE_Y = 4

######################
# BUTTON STYLE
REGULAR_COLOR = 'mistyrose'
BUTTON_HOVER_COLOR = 'gray'
BUTTON_ACTIVE_COLOR = 'slateblue'
BUTTON_STYLE = {"font": ("Courier", 30),
                "borderwidth": 1,
                "relief": tk.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": 'black'}
BUTTONS_WIDTH_RELATIVE_SIZE = 2 / 3
BUTTONS_HIGHT_RELATIVE_SIZE = 2 / 3
BUTTONS_BG_COLOR_FRAME = 'black'
BUTTONS_WIDTH_RELATIVE_LOC = 3.5
BUTTONS_HIGHT_RELATIVE_LOC = 7
BUTTONS_WEIGHT_IN_GAME_FRAME = 1
BUTTON_BORDER_WIDTH = 10
BUTTON_FG_COLOR = 'mediumvioletred'
BUTTON_WIDTH = 4
BUTTON_HEIGHT = 2

######################
# words box
BG_WORDS_BOX_COLOR = 'black'
WORDS_BOX_WIDTH = 400
WORDS_BOX_HIGHT = 600
WORDS_BOX_X_LOC = 510
WORDS_BOX_Y_LOC = 80

# list box
LIST_BOX_HIGHT = 23
LIST_BOX_WIDTH = 25

# enter words button
BUTTON_ENTER_FG_COLOR = 'mediumvioletred'
BUTTON_ENTER_TEXT = 'Enter a word'
BUTTON_ENTER_BG = 'mistyrose'
BUTTON_ENTER_BORDER_WIDTH = 10
BUTTON_ENTER_WIDTH = 24
BUTTON_ENTER_HEIGHT = 3
BUTTON_ENTER_HIGHLIGHT_COLOR = 'black'
BUTTON_ENTER_X_LOC = 200
BUTTON_ENTER_Y_LOC = 398
BUTTON_ENTER_F_STYLE = {"font": ("Courier", 30),
                        "borderwidth": 1,
                        "relief": tk.RAISED,
                        "bg": REGULAR_COLOR,
                        "activebackground": 'black'}
#################
# timer
TIMER_FG = 'mediumvioletred'
TIMER_SIZE = 10
MINUTES = 3
SECONDS = 0
TIMER_HEIGHT = 3
TIMER_WIDTH = 20
TIMER_TEXT = (f'{MINUTES}' if MINUTES > 9 else f'0{MINUTES}') + ':' + \
             (f' {SECONDS}' if SECONDS > 9 else f'0{SECONDS}')
TIMER_PLACE_X = 20
TIMER_PLACE_Y = 80
TIMER_ONE_SECOND = 1000
SECONDS_IN_MINUTE = 60

# side buttons
UNDO_TEXT = 'Undo'
SIZE_BUTTONS_WIDTH = 10
SIZE_BUTTONS_HEIGHT = 2
X_SIDE_BUTTONS = 30
UNDO_Y = 190
CLEAR_TEXT = 'Clear'
CLEAR_Y = 290
EXIT_Y = 390
EXIT_TEXT = 'Click To Exit'

# current word label
FONT_WORD_LABEL = (FONT_HEADLINE, 20)
BG_C_WORD_LABEL = 'white'
FG_C_WORD_LABEL = 'black'
C_WORD_LABEL_X = 20
C_WORD_LABEL_Y = 150
C_WORD_LABEL_WIDTH = 10
C_WORD_LABEL_HEIGHT = 1

#################
####end##########
LABEL_RESTART_X = 0
LABEL_RESTART_Y = 0
BUTTON_YES_TEXT = 'YES'
BUTTON_NO_TEXT = 'NO'
END_TITLE = 'game ends'
BUTTON_END_WIDTH = 20
BUTTON_END_HEIGHT = 3
BUTTON_YES_X = 130
BUTTON_YES_Y = 400
BUTTON_NO_X = 430
BUTTON_NO_Y = 400
TEXT_FINAL_LABEL_1 = f'Your final score is:'
TEXT_FINAL_LABEL_2 = 'Do You Want To Play Again?'
BG_FINAL_LABEL = 'white'
FINAL_LABEL_HEIGHT = 3
FINAL_LABEL_WIDTH = 30
FINAL_LABEL_FONT = ("Courier", 17)
FINAL_LABEL_X = 145
FINAL_LABEL_Y = 10
