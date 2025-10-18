 Libraries Used:- pygame: Used for graphics, game loop, input handling, and screen updates.- sys: Used for exiting the program.- random: Used to place the food randomly.
 Key Functions and Their Purpose:
 1. pygame.init() - Initializes the game engine.
 2. pygame.display.set_mode() - Sets the game window size.
 3. pygame.display.set_caption() - Sets the title of the game window.
 4. pygame.draw.rect() - Draws snake and food blocks.
 5. pygame.event.get() - Captures events (like key presses or mouse clicks).
 6. pygame.KEYDOWN - Detects when a key is pressed.
 7. pygame.quit(), sys.exit() - Cleanly exit the game.
 Game Functions:
 1. game_intro(): Displays the start menu with Start/Quit buttons.
 2. game_loop(): Main gameplay - moves snake, checks collisions, handles scoring.
 3. game_over_screen(): Shows Game Over screen with Play Again/Quit buttons.
 4. draw_snake(): Renders the snake based on coordinates.
 5. show_score(): Displays the current score.
 6. button(): Draws interactive buttons on the screen.
Notes:- The game uses arrow keys to move the snake.- Snake grows when it eats food.- Game ends if the snake hits a wall or itself.
