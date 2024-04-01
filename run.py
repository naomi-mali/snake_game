import curses
from random import randint
import time

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
   #############| Press Space to Pause |###########
   #############| Press Esc to Exit |##############
   #*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

########################################################
########################################################
"""

def draw_intro():
    win.clear()
    win.addstr(0, 0, intro)
    win.refresh()

def clear_intro():
    win.clear()
    win.refresh()

def draw_borders():
    win.border('|', '|', '-', '-', '+', '+', '+', '+')

def draw_game_over(score):
    win.clear()
    game_over_message = """
        Game Over!
        Your Score: {}
        To play again press Enter!
    """.format(score)
    win.addstr(0, 0, game_over_message)
    win.refresh()

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

def game_loop():
    # Game logic
    ESC = 27
    game_over = False

    while not game_over:
        # Snake and food
        snake = [(4, 4), (4, 3), (4, 2)]
        food = (6, 6)

        win.addch(food[0], food[1], '@', curses.color_pair(2))  # Draw food in red color

        score = 0
        key = curses.KEY_RIGHT
        paused = False

        # Main game loop
        while not game_over:
            win.addstr(0, 2, 'Score ' + str(score) + ' ')
            curses.halfdelay(3) #Snake speed 
            event = win.getch()
            
            if event == ESC:  # Check if Escape key is pressed
                return False
            
            if not game_over:  
                if event == ord(' '):  # Pause 
                    paused = not paused  # Toggle pause state
                    continue  

                if paused:
                    continue  # Skip game if paused

                # Game bug error fixed when two buttons pressed caused instant game over
                if (event == curses.KEY_LEFT and key == curses.KEY_RIGHT) or \
                   (event == curses.KEY_RIGHT and key == curses.KEY_LEFT) or \
                   (event == curses.KEY_UP and key == curses.KEY_DOWN) or \
                   (event == curses.KEY_DOWN and key == curses.KEY_UP):
                    continue

                key = event if event != -1 else key

                # Calculate next coordinates
                y = snake[0][0]
                x = snake[0][1]
                if key == curses.KEY_DOWN:
                    y += 1
                elif key == curses.KEY_UP:
                    y -= 1
                elif key == curses.KEY_LEFT:
                    x -= 1
                elif key == curses.KEY_RIGHT:
                    x += 1

                snake.insert(0, (y, x))
                # Check if snake hits the border
                if y == 0 or y == WINDOW_HEIGHT or x == 0 or x == WINDOW_WIDTH:
                    # Flash snake and food
                    flash_object(snake)
                    flash_object([food])

                    game_over = True
                    draw_game_over(score)  # Display game over message
                    time.sleep(4)  # Wait for 4 seconds
                    break


                # Check if snake runs over itself
                if snake[0] in snake[1:]:
                    # Flash snake and food
                    flash_object(snake)
                    flash_object([food])                  
                    game_over = True
                    draw_game_over(score)  # Display game over message
                    time.sleep(4)  # Wait for 4 seconds
                    break                   

                if snake[0] == food:
                    # Eat the food
                    score += 1
                    food = ()
                    while food == ():
                        food = (randint(1, WINDOW_HEIGHT-1), randint(1, WINDOW_WIDTH-1))
                        if food in snake:
                            food = ()
                    win.addch(food[0], food[1], '@', curses.color_pair(2))  # Draw new food in red color
                else:
                    # Move snake
                    last = snake.pop()
                    win.addch(last[0], last[1], ' ')

                # Clear the screen
                win.clear()

                # Redraw borders
                draw_borders()

                # Draw food
                win.addch(food[0], food[1], '@', curses.color_pair(2))  # Draw food in red color

                # Draw snake head with green color
                win.addstr(snake[0][0], snake[0][1], 'O', snake_color_pair)

                # Draw snake body with green color
                for segment in snake[1:]:
                    win.addstr(segment[0], segment[1], 'o', snake_color_pair)

                win.refresh()

    return True

def flash_object(obj):
    for _ in range(4):
        for segment in obj:
            win.addstr(segment[0], segment[1], 'X')
        win.refresh()
        time.sleep(0.1)
        for segment in obj:
            if segment == obj[0]:
                win.addstr(segment[0], segment[1], 'O', snake_color_pair)
            else:
                win.addch(segment[0], segment[1], '@', curses.color_pair(2))
        win.refresh()
        time.sleep(0.1)    

while True:
    draw_intro()
    key = win.getch()
    if key == 10:
        clear_intro()
        draw_borders()
        if not game_loop():
            break
    elif key == 27:  # Esc key during intro screen
        break

# End game
curses.endwin()
