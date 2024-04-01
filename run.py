import curses
from random import randint
import time

WINDOW_WIDTH = 85
WINDOW_HEIGHT = 30

#Intro
intro = """
 ____              _           ____                       
/ ___| _ __   __ _| | _____   / ___| __ _ _ __ ___   ___  
\___ \| '_ \ / _` | |/ / _ \ | |  _ / _` | '_ ` _ \ / _ \ 
 ___) | | | | (_| |   <  __/ | |_| | (_| | | | | | |  __/ 
|____/|_| |_|\__,_|_|\_\___|  \____|\__,_|_| |_| |_|\___| 
 
                          ___   
                         / o o\ 
         *               \   ---<     @
          \\              \  /
           \ \ ___________/ /
            \  ___________ /

   *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
   ~~~~~~~~~~~~~| Press Enter to Play |~~~~~~~~~~~~
   ~~~~~~~~~~~~~| Press Space to Pause |~~~~~~~~~~~
   ~~~~~~~~~~~~~| Press Esc to Exit |~~~~~~~~~~~~~~
   -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def draw_intro():
    win.clear()
    # Calculate position to center the intro message

    y_center = (WINDOW_HEIGHT + 2 - intro.count('\n')) // 2

    x_center = (WINDOW_WIDTH + 2 - max(len(line) for line in intro.split('\n'))) // 2

    for i, line in enumerate(intro.split('\n')):

        win.addstr(y_center + i, x_center, line)    
    win.refresh()

def clear_intro():
    win.clear()
    win.refresh()

def draw_borders():
    win.border('|', '|', '-', '-', '+', '+', '+', '+')

def draw_game_over(score):
    win.clear()
    game_over_message = """

  _____          __  __ ______    ______      ________ _____  
 / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
| |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
| | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
| |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
 \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ 
    
        Your Score: {}
        To play again press Enter!
    """.format(score)
    

    # Calculate the center position for the message

    y_center = (WINDOW_HEIGHT + 2) // 2 - len(game_over_message.split('\n')) // 2

    x_center = (WINDOW_WIDTH + 2 - max(len(line) for line in game_over_message.split('\n'))) // 2

    # Print the game over message at the center of the screen

    for i, line in enumerate(game_over_message.split('\n')):

        win.addstr(y_center + i, x_center, line, curses.A_BOLD)



 
    win.refresh()

# Setup window
curses.initscr()
win = curses.newwin(WINDOW_HEIGHT + 2, WINDOW_WIDTH + 2, 0, 0)  
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
                    time.sleep(1.8)  # Wait for 1.8 seconds
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
