# Snake Game

## Project Overview
As a classic snake game, this implementation pays homage to the timeless appeal of retro arcade games, evoking feelings of nostalgia among players who grew up with similar titles. While appealing to players familiar with classic snake games, this version also introduces the genre to new generations of players, ensuring its enduring popularity and relevance.
Overall, this classic snake game offers a blend of simplicity, challenge, and nostalgia, making it a timeless favorite among gamers of all ages.

[Play the game here!](https://snakegame-c0f28d0c7871.herokuapp.com/)

## Table of Contents
1. [Project-Ovewrview] (#project-overview)
2. [Objective] (#objective)
3. [Gameplay] (#gameplay)
4. [Features] (#features)
5. [Controls] (#controls)
6. [Visuals] (#visuals)
7. [Gameplay-Mechanics] (#gameplay-mechanics)
8. [User-Experience] (#user-experience)
9. [Replayability] (#replayability)
10. [] (#)
11. [] (#)
12. [] (#)
13. [] (#)
14. [] (#)



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

### Gameplay Mechanics:
Snake Movement: The snake moves continuously in the direction specified by the player, and its length increases each time it consumes food.
Collision Detection: The game engine checks for collisions between the snake and various elements, including borders, obstacles, and itself, to determine if the game should continue or end.
Difficulty Progression: As the player advances through levels, the game becomes progressively more challenging with faster snake movement speeds and an increased number of obstacles, requiring quicker reflexes and strategic maneuvering.
Randomization: Food and obstacles are randomly positioned on the game board at the start of each level, ensuring a different gameplay experience each time.

### User Experience:
Intuitive Controls: The controls for directing the snake are simple and intuitive, making it easy for players of all skill levels to pick up and play.
Clear Feedback: Visual feedback is provided to the player through changes in the game board, such as the snake's movement, score updates, and the appearance of level up and game over messages, ensuring a clear understanding of the game state.
Engaging Audiovisuals: While the game is text-based, the combination of ASCII art, colors, and animations creates an immersive experience for the player, enhancing their engagement and enjoyment.

### Replayability:
High Replay Value: The addictive nature of the gameplay, coupled with the desire to achieve higher scores and reach new levels, encourages players to replay the game multiple times.
Endless Mode: While the game features predefined levels, players can continue playing indefinitely by starting new games after reaching the highest level, providing endless entertainment and challenge.

