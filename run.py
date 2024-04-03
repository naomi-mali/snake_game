import curses
from random import randint
import time

import sys


def hide_cursor():
    """ Hide the cursor in the terminal """
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()


# Call hide_cursor function to hide the cursor
hide_cursor()


WINDOW_WIDTH = 80
WINDOW_HEIGHT = 22

# Intro
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
   ~~~~~~~~~~~~~| Eat @ to level up |~~~~~~~~~~~~~~
   ~~~~| Avoid X obstacles and borders to win|~~~~~
   -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


def draw_intro():
    """ Draw the introduction message on the screen """
    win.clear()
    # Calculate position to center the intro message
    y_center = (WINDOW_HEIGHT + 2 - intro.count('\n')) // 2
    x_center = (WINDOW_WIDTH + 2 - max(len(line) for line in intro.split('\n'))) // 2
    for i, line in enumerate(intro.split('\n')):
        win.addstr(y_center + i, x_center, line)
    win.refresh()


def clear_intro():
    """ Clear the introduction message from the screen """
    win.clear()
    win.refresh()


def draw_borders(score):
    """ 
    Draw borders around the game window and display the current score.
    Parameters: score (int): The current score to be displayed. 
    """
    win.clear()
    # Draw top border with score
    win.addstr(0, 0, "+" + "-" * (WINDOW_WIDTH - 2) + "+")
    win.addstr(0, 1, f"Score: {score}", curses.A_BOLD)
    # Draw bottom border
    win.addstr(WINDOW_HEIGHT + 1, 0, "+" + "-" * (WINDOW_WIDTH - 2) + "+")
    # Draw side borders
    for i in range(1, WINDOW_HEIGHT + 1):
        win.addstr(i, 0, "|")
        win.addstr(i, WINDOW_WIDTH - 1, "|")
    win.refresh()


def draw_game_over(score):
    """
    Display the game over message with the final score.
    Parameters: score (int): The final score of the player.
    """
    win.clear()
    game_over_message = """

  _____          __  __ ______    ______      ________ _____  
 / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
| |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
| | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
| |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
 \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ 
    
        Your Total Score: {}
        To play again press Enter!
    """.format(score)

    # Calculate the center position for the message
    y_center = (WINDOW_HEIGHT + 2) // 2 - len(game_over_message.split('\n')) // 2
    x_center = (WINDOW_WIDTH + 2 - max(len(line) for line in game_over_message.split('\n'))) // 2

    # Print the game over message at the center of the screen
    for i, line in enumerate(game_over_message.split('\n')):
        win.addstr(y_center + i, x_center, line, curses.A_BOLD)
    win.refresh()


# Function to display score
def display_score(score):
    """
    Display the current score on the game window.
    Parameters: score (int): The current score to be displayed.
    """
    score_str = f"Score: {score}"
    # Display score in the top-right corner
    win.addstr(0, WINDOW_WIDTH - len(score_str) - 2, score_str, curses.A_BOLD)
    win.refresh()


# Setup window
curses.initscr()
win = curses.newwin(WINDOW_HEIGHT + 2, WINDOW_WIDTH + 2, 0, 0)
win.keypad(1)
curses.noecho()

# Initialize colors
curses.start_color()
# Define snake color as green on black background
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
# Define food color as red on black background
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
# Define obstacle color as yellow on black background
curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
# Define black color on black background)
curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLACK)
snake_color_pair = curses.color_pair(1)
obstacle_color_pair = curses.color_pair(3)
background_color_pair = curses.color_pair(4)

# Define levels with their respective parameters
LEVELS = [
    {"speed": 3, "obstacles": 5, "point_threshold": 5},  # Level 1
    {"speed": 5, "obstacles": 7, "point_threshold": 10},  # Level 2
    {"speed": 7, "obstacles": 10, "point_threshold": 15},  # Level 3
    {"speed": 9, "obstacles": 13, "point_threshold": 20},  # Level 4
    {"speed": 11, "obstacles": 15, "point_threshold": 25},  # Level 5
    {"speed": 13, "obstacles": 18, "point_threshold": 30},  # Level 6
    {"speed": 15, "obstacles": 20, "point_threshold": 35},  # Level 7
    {"speed": 17, "obstacles": 22, "point_threshold": 40},  # Level 8
    {"speed": 19, "obstacles": 25, "point_threshold": 45},  # Level 9
    {"speed": 21, "obstacles": 27, "point_threshold": 50},  # Level 10
]


def game_loop():
    """
    The main game loop controlling the gameplay.
    Returns: True if the player decides to play again, False otherwise.
    """
    global current_level, current_score, total_score
    # Game logic
    ESC = 27
    game_over = False

    while not game_over:
        # Reset score at the beginning of each level
        current_score = 0

        # Snake and food
        snake = [(4, 4), (4, 3), (4, 2)]
        food = ()
        while food == () or food in snake or food[0] <= 1 or food[1] <= 1 or food[0] >= WINDOW_HEIGHT - 2 or food[1] >= WINDOW_WIDTH - 2:
            food = (randint(2, WINDOW_HEIGHT - 3), randint(2, WINDOW_WIDTH - 3))
        # Use parameters from the current level
        level_params = LEVELS[current_level]
        snake_speed = level_params["speed"]
        num_obstacles = level_params["obstacles"]
        point_threshold = level_params["point_threshold"]

        # Add obstacles based on current level
        obstacles = []
        for _ in range(num_obstacles):
            obstacle = ()
            while obstacle == () or obstacle in obstacles or obstacle in snake:
                obstacle = (randint(1, WINDOW_HEIGHT-1), randint(1, WINDOW_WIDTH-1))
            obstacles.append(obstacle)

        score = 0
        key = curses.KEY_RIGHT
        paused = False

        # Main game loop
        while not game_over:
            # Snake speed based on current level
            curses.halfdelay(snake_speed)
            event = win.getch()

            if event == ESC:  # Check if Escape key is pressed
                return False

            if not game_over:
                if event == ord(' '):  # Pause
                    paused = not paused  # Toggle pause state
                    continue

                if paused:
                    continue  # Skip game if paused

                # Prevents crash on simultaneous button press
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
                    total_score += score
                    draw_game_over(total_score)  # Display game over message
                    time.sleep(1.8)  # Wait for 1.8 seconds
                    break

                # Check if snake runs over itself
                if snake[0] in snake[1:]:
                    # Flash snake and food
                    flash_object(snake)
                    flash_object([food])
                    game_over = True
                    total_score += score
                    draw_game_over(total_score)  # Display game over message
                    time.sleep(4)  # Wait for 4 seconds
                    break

                # Check if snake collides with any obstacle
                if snake[0] in obstacles:
                    # Flash snake and obstacle
                    flash_object(snake)
                    flash_object([snake[0]])
                    flash_object([obstacle])
                    game_over = True
                    total_score += score
                    draw_game_over(total_score)  # Display game over message
                    time.sleep(1.8)  # Wait for 1.8 seconds
                    break
                if snake[0] == food:
                    # Eat the food
                    score += 1
                    current_score += 1  # Increment current score
                    total_score += 1
                    food = ()
                    while food == () or food in snake or food in obstacles or food[0] <= 1 or food[1] <= 1 or food[0] >= WINDOW_HEIGHT - 2 or food[1] >= WINDOW_WIDTH - 2:
                        food = (randint(2, WINDOW_HEIGHT - 3), randint(2, WINDOW_WIDTH - 3))
                        # Draw new food in red color
                    win.addch(food[0], food[1], '@', curses.color_pair(2))
                else:
                    # Move snake
                    last = snake.pop()
                    win.addch(last[0], last[1], ' ')

                # Clear the screen
                win.clear()

                # Redraw borders
                draw_borders(total_score)

                # Draw food in red color
                win.addch(food[0], food[1], '@', curses.color_pair(2))

                # Draw obstacles in yellow color
                for obstacle in obstacles:
                    win.addstr(obstacle[0], obstacle[1], 'X', obstacle_color_pair)

                # Draw snake head with green color
                win.addstr(snake[0][0], snake[0][1], 'O', snake_color_pair)

                # Draw snake body with green color
                for segment in snake[1:]:
                    win.addstr(segment[0], segment[1], 'o', snake_color_pair)

                win.refresh()

                # Check if player reaches the point threshold to level up
                if current_score >= point_threshold:
                    current_level += 1  # Move to the next level

                    # Display level up message
                    if current_level <= 10:
                        level_up_message = f"You have reached Level {current_level}!"
                    else:
                        level_up_message = "You have reached the maximum level!"
                    draw_level_message(level_up_message)

                    return True

    return False  # Game over, return to intro


def draw_level_message(message):
    """ Display a message indicating the player has leveled up.
        Parameters: message (str): The message to be displayed.
    """    
# Clear the screen
    win.clear()

    # Calculate position to center the message
    y_center = (WINDOW_HEIGHT + 2) // 2
    x_center = (WINDOW_WIDTH + 2 - len(message)) // 2

    # Print the level up message at the center of the screen
    win.addstr(y_center, x_center, message, curses.A_BOLD)
    win.refresh()
    time.sleep(2)  # Wait for 2 seconds


def flash_object(obj):
    """
    Flash an object on the screen for visual effect.
    Parameters: obj (list of tuples): The object to be flashed on the screen,
    represented by a list of coordinate tuples.
    """
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


def gameloop():
    """The main game loop controlling the flow of the game """


while True:
    draw_intro()
    key = win.getch()
    if key == 10:
        clear_intro()
        draw_borders(0)  # Initialize score to 0
        current_level = 0  # Reset the level
        current_score = 0  # Reset the score
        total_score = 0    # Initialize total score
        # Keep starting new games until the player decides to exit
        while game_loop():
            pass
    elif key == 27:  # Esc key during intro screen
        break

# End game
curses.endwin()

if __name__ == '__main__':
    gameloop()
