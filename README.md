 # Snake Game

![Am I Responsive_ (1)](https://github.com/naomi-mali/test/assets/148251951/0d24799d-ea8a-4e19-977f-d1dc6512df6b)


## Project Overview
As a classic snake game, this implementation pays homage to the timeless appeal of retro arcade games, evoking feelings of nostalgia among players who grew up with similar titles. While appealing to players familiar with classic snake games, this version also introduces the genre to new generations of players, ensuring its enduring popularity and relevance.
Overall, this classic snake game offers a blend of simplicity, challenge, and nostalgia, making it a timeless favorite among gamers of all ages.

[Play the game here!](https://snakegame-c0f28d0c7871.herokuapp.com/)

## Table of Contents
1. [Project Ovewrview](#project-overview)
2. [Objective](#objective)
3. [Gameplay ](#gameplay)
4. [Features](#features)
5. [Controls](#controls)
6. [Visuals](#visuals)
7. [Gameplay Mechanics](#gameplay-mechanics)
8. [User Experience](#user-experience)
9. [Replayability](#replayability)
10. [Flow Chart](#flow-chart)
11. [Languages used](#languages-used)
12. [Software used](#software-used)
13. [Testing and known issues](#testing-and-known-issues)
14. [Testing](#testing)
15. [Manual testing](#manual-testing)
16. [Solved bugs](#solved-bugs)
17. [Terminal Screen Flickering](#terminal-screen-flickering)
18. [Deployment](#deployment )
19. [Future Development Opportunities](#future-development-opportunities)
20. [Credit](#credits)
21. [Learning materials and Code](#learning-materials-and-code)
22. [Acknowledgments](#acknowledgments)


This game is a classic snake game implemented using the curses library in Python. Here's a description of the game:

### Objective:
The objective of the game is to control a snake, represented by the character 'O', and guide it to eat food items represented by '@'. As the snake eats food, it grows longer. The player's goal is to accumulate as many points as possible without crashing the snake into the borders of the game window, obstacles, or itself.

### Gameplay:
The snake moves continuously in the direction it's facing (up, down, left, or right).
The player can control the direction of the snake using arrow keys (up, down, left, right).
The game features different levels, each with its own speed of snake movement and number of obstacles.
The snake's speed increases with each level, making it more challenging to control.
The player progresses to the next level by accumulating a certain number of points (specified as the "point_threshold" in the LEVELS dictionary).
Obstacles ('X') are placed randomly on the game board and must be avoided by the snake. Colliding with an obstacle results in game over.
Eating food increases the player's score. The snake's length increases by one segment each time it consumes food.
The game ends if the snake collides with the borders of the game window, obstacles, or itself.
After game over, the player can choose to play again or exit the game.

### Features:
Level System: The game features multiple levels, each with its own set of parameters such as speed, number of obstacles, and point threshold to level up.
Pause Functionality: The player can pause the game by pressing the spacebar.
Score Tracking: The player's score is displayed at the top of the game window, showing the total score accumulated across multiple playthroughs.
Level Up Message: When the player reaches the point threshold for a level, a level up message is displayed briefly before progressing to the next level.
Game Over Message: When the game ends, a game over message is displayed, showing the total score achieved in that playthrough.

### Controls:
Arrow Keys: Control the direction of the snake (up, down, left, right).
Spacebar: Pause/unpause the game.
Enter: Start a new game or confirm selection in the intro screen.
Esc: Exit the game.

### Visuals:
The ASCII art used for the snake, food, obstacles, and borders adds a retro charm to the game, reminiscent of classic terminal-based games.
The game features colorful ASCII art, including a snake represented by 'O', food represented by '@', and obstacles represented by 'X'.
Borders and UI elements are drawn using ASCII characters to create a visually appealing interface.
Text-based messages are displayed for intro, level up, and game over screens.
Colors are used to distinguish different elements on the game board, such as the green color for the snake, red color for food, and yellow color for obstacles, making it visually appealing and easy to identify each component.

![README md - snake_game - Gitpod Code](https://github.com/naomi-mali/test/assets/148251951/905f4783-582b-402b-ae14-2a4abbc73d40)

![run py - snake_game - Gitpod Code (2)](https://github.com/naomi-mali/test/assets/148251951/bf63bd98-72da-4249-9c9b-8c68f854f12c)


### Gameplay Mechanics:
Snake Movement: The snake moves continuously in the direction specified by the player, and its length increases each time it consumes food.
Collision Detection: The game engine checks for collisions between the snake and various elements, including borders, obstacles, and itself, to determine if the game should continue or end.
Difficulty Progression: As the player advances through levels, the game becomes progressively more challenging with faster snake movement speeds and an increased number of obstacles, requiring quicker reflexes and strategic maneuvering.
Randomization: Food and obstacles are randomly positioned on the game board at the start of each level, ensuring a different gameplay experience each time.

![run py - snake_game - Gitpod Code (1)](https://github.com/naomi-mali/test/assets/148251951/d9762c1d-a0e1-4e5e-9a7f-b76216265b2b)

![run py - snake_game - Gitpod Code](https://github.com/naomi-mali/test/assets/148251951/0b5b72e8-beba-487a-a276-1a566c0b32ee)


### User Experience:
Intuitive Controls: The controls for directing the snake are simple and intuitive, making it easy for players of all skill levels to pick up and play.
Clear Feedback: Visual feedback is provided to the player through changes in the game board, such as the snake's movement, score updates, and the appearance of level up and game over messages, ensuring a clear understanding of the game state.
Engaging Audiovisuals: While the game is text-based, the combination of ASCII art, colors, and animations creates an immersive experience for the player, enhancing their engagement and enjoyment.

![Python Terminal by Code Institute (1)](https://github.com/naomi-mali/test/assets/148251951/26c2e092-d703-4f1a-8a63-079c1159a26e)

The intro page of the Snake game presents players with a visually engaging screen that not only sets the tone for the game but also provides essential instructions on how to play. Here's a description of what the intro page contains:

Title and ASCII Art: At the top of the intro page, there's a prominent title rendered in ASCII art. The title is stylized to grab the player's attention and convey the theme of the game.

Snake and Food ASCII Art: Alongside the title, there are ASCII art representations of a snake and food item. These visual elements give players a glimpse of what to expect in the game and reinforce the theme of controlling a snake to eat food.

Control Instructions: Below the ASCII art, there's a section dedicated to control instructions. It informs players about the keys they need to use to interact with the game. For example:

"Press Enter to Play": Instructs players to press the Enter key to start playing the game.
"Press Space to Pause": Indicates that the Space key can be used to pause or resume the game.
"Press Esc to Exit": Notifies players that they can press the Esc key to exit the game.
"Eat @ to level up": Provides a specific gameplay instruction, indicating that eating '@' symbols allows players to level up in the game.
"Avoid X obstacles and borders to win": Advises players to avoid collision with 'X' symbols representing obstacles and the game borders to succeed in the game.
Level and Objective Description: Optionally, the intro page may include a brief description of the game's objective and how players progress through levels. This description helps set player expectations and provides context for the gameplay.

Overall, the intro page serves as an effective starting point for players, offering both visual appeal 

### Replayability:
High Replay Value: The addictive nature of the gameplay, coupled with the desire to achieve higher scores and reach new levels, encourages players to replay the game multiple times.
Endless Mode: While the game features predefined levels, players can continue playing indefinitely by starting new games after reaching the highest level, providing endless entertainment and challenge.

### Flow Chart
![Untitled Diagram drawio](https://github.com/naomi-mali/test/assets/148251951/83974358-20a4-4da4-a76a-6849c4afca2e)

### Languages used
Python is used for the project.


## Software used
Draw.io - To create a Flow Chart. 
Gitpod - To code the project. 
Git - For version control. 
Github - To store to project. 
Heroku – To deploy the project. 
Ci Python Linter – To validate the python code. 

## Testing and known issues
### Testing

The code has been submitted to the Code Institute PEP8 lint and all major issues were fixed. The ones that remain are due to strings being too long, or a character in a docstring that the lint recognizes erroneously as an escape character. With regard to the strings length, it has been decided that they are to remain as is for design purposes.

### Manual testing
I have tested all input options, valid input and non-valid input by the user. These tests were carried out throughout the entire project process. Finally, no more errors occurred. The detailed error messages to the user are also explained in the features section. A description of the bugs can be found in solved and unsolved bugs.

![CI Python Linter (6)](https://github.com/naomi-mali/test/assets/148251951/4894b126-2e77-4623-98c2-80969fef4c04)
![CI Python Linter (5)](https://github.com/naomi-mali/test/assets/148251951/11f3340b-acb3-4785-ba2c-6d5c841ad7db)
![CI Python Linter (4)](https://github.com/naomi-mali/test/assets/148251951/81d17dad-0d85-4aba-8363-67a0a5527151)
![CI Python Linter (3)](https://github.com/naomi-mali/test/assets/148251951/1646912a-84ed-4008-8208-7cf8488e4ec0)

### Solved bugs

![Python Terminal by Code Institute](https://github.com/naomi-mali/test/assets/148251951/c0afe988-2a34-4865-8287-9677b5c26b3d)

The issue with the curses.curs_set(0) function call occurred due to various reasons, such as compatibility issues or lack of support in certain environments. By replacing it with the code using ANSI escape codes,I am providing a more portable and reliable solution for hiding the cursor in the terminal.

![run py - snake_game - Gitpod Code (6)](https://github.com/naomi-mali/test/assets/148251951/4cc048c7-0a5f-43e6-9e59-8c7104258109)

### Terminal Screen Flickering
When testing I saw that there was a "strobing" effect, I put this down to running it in a console environment like Heroku's online terminal. I think it is due to the game's design to clear and redraw the entire screen every game tick. I found out from my mentor that this approach, while straight forward for ensuring that the game state is accurately represented at all times, can lead to noticeable flickering or "strobing" because of the rapid clearing and redrawing of the screen content. My  mentor said that this effect would be more pronounced in environments with slower refresh rates or where there's a significant delay between sending output and it being displayed, such as in remote terminal sessions in Heroku. He said there were ways in which to make it better but for purposes of this project that would be more advanced coding, maybe something to learn later after the course.

## Deployment 
The project was coded with gitpod, stored on github and then deployed on Heroku. That is how the deployment was done:

Create a requirements.txt with the terminal comand: pip3 freeze > requirements.txt
Pushed the latested code and requirements.txt on to Github.
Log in to Heroku or create an account first.
Click on the New Button on the dashboard in the top right corner.
Click on "Create new app".
Select the relevant region. In my case, I chose Europe.
Select an app name that does not yet exist on heroku.
Click on the "Create app" button.
Click on the settings tab.
Scroll to the buildpacks and click on "add buildpack," select "Python," and click "Add Buildpack".
Repeat last step and add "node.js" buildpack.
IMPORTANT: First the python buildpack must be displayed, then the pack from node.js. It can be moved via drag and drop.
Click on the deploy tab.
Click on Github as the deployment method.
Search for the repository name and click on conncet.
Select Enable Automatic Deploys"
Click on "Deploy Branch"
Click on the "View" button which leads to the deployed app

![Python Terminal by Code Institute (2)](https://github.com/naomi-mali/test/assets/148251951/f58deda2-0140-47ed-8761-245007af5f2d)


## Future Development Opportunities 

 The Snake Game is a simple terminal-based game, implemented using the curses module in Python. Here are some potential future developments for enhancing the game:

Levels with Increasing Difficulty: Currently, the game has predefined levels with fixed parameters such as snake speed, number of obstacles, and point thresholds. You could introduce a more dynamic difficulty curve, where each level gradually increases in difficulty, making the game more challenging as the player progresses.

Customizable Settings: Allow players to customize game settings such as snake speed, number of obstacles, and point thresholds. This adds flexibility and allows players to tailor the game to their preferences or skill level.

Power-Ups and Special Abilities: Introduce power-ups or special abilities that the snake can collect during gameplay. For example, a power-up that increases the snake's speed temporarily or one that makes the snake temporarily invincible to obstacles.

Different Game Modes: Implement different game modes to provide variety and replay value. For example, a timed mode where the player must achieve a high score within a limited time or a survival mode where the goal is to survive as long as possible against increasing difficulty.

Sound Effects and Music: Add sound effects for actions such as eating food, colliding with obstacles, or leveling up. You could also include background music to enhance the gaming experience.

Graphics and Animation: While curses provides basic terminal-based graphics, you could explore more advanced graphics libraries like Pygame or Kivy to create more visually appealing graphics and animations for the game.

Multiplayer Support: Implement multiplayer support, allowing multiple players to compete against each other either locally or over a network.

High Score Tracking: Implement a high score system to keep track of the highest scores achieved by players. This adds competitiveness and motivation for players to strive for higher scores.

Tutorial or Help Section: Include a tutorial or help section within the game to guide new players on how to play and understand game mechanics.

Bug Fixes and Performance Optimization: Continuously test and debug the game to fix any issues or bugs. Additionally, optimize the code for better performance, especially for larger game states or when running on lower-end systems.

Implementing some or all of these features can greatly enhance the gameplay experience and make the Snake game more engaging and enjoyable for players.

## Credits

### Learning materials and Code
 All content from Online Course in Full Stack Software Development especially videos about Portfolio Project 3 and ReadME from Code Instituet.

[codereview](https://codereview.stackexchange.com/questions/104524/simple-console-snake-game-in-python) For Snake Game functional in a console

[youtube](https://www.youtube.com/watch?v=XKHEtdqhLK8&t=41185s) To build functions in the game according a Snake Game

[geeksforgeeks](https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/) For building step by step a Snake Game 

[geeksforgeeks](https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/) For building step by step a Snake Game 

[geeksforgeeks](https://www.geeksforgeeks.org/snake-game-using-tkinter-python/) For building step by step a Snake Game 

[geeksforgeeks](https://www.geeksforgeeks.org/create-a-snake-game-using-turtle-in-python/) For building step by step a Snake Game  

## Acknowledgments

My Code Institute mentor Spencer Barriball.
The Tutor Support team at Code Institute.
To all people who make their knowledge available for free in the internet, especially on youtube.
