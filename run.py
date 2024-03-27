import curses 
from random import randint

WINDOW_WIDTH = 60
WINDOW_HEIGHT = 20

# Intro
intro = """
   #######  ##     #     ##     #    ##  #######
   #        # #    #    #  #    #   ##   #
   #        #  #   #   #    #   #  ##    #
   #######  #   #  #  ########  ####     ##### 
         #  #    # #  #      #  #  ##    #
         #  #     ##  #      #  #   ##   #
   #######  #      #  #      #  #    ##  #######

   #*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
   #############| Press Enter to Play |############
   #############| Press Esc to Exit |##############
   #*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

########################################################
########################################################
"""
def draw_intro():
    pass

def clear_intro():
    pass

def draw_borders():
    pass

 def draw_game_over(score):
    pass

# Setup window
curses.initscr()
win = curses.newwin(WINDOW_HEIGHT + 2, WINDOW_WIDTH + 2, 0, 0)  # Adding 2 to each dimension for border
win.keypad(1)
curses.noecho()
curses.curs_set(0)

# Initialize colors
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Define snake color as green on black background
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Define food color as red on black background
snake_color_pair = curses.color_pair(1)  # Create a color attribute using the defined color pair

while True:
    draw_intro()
    key = win.getch()
    if key == 10:
        clear_intro()
        draw_borders()
        break
