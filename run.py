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