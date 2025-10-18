import pygame
import time
import random

# Initialize
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 255, 0)
blue = (0, 100, 255)

# Display
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game by Harshad")

block = 10
speed = 15

clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 30)
score_font = pygame.font.SysFont("bahnschrift", 25)

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], block, block])

def draw_score(score):
    value = score_font.render(f"Score: {score}", True, black)
    screen.blit(value, [10, 10])

def game_over_screen(score):
    screen.fill(white)
    msg = font.render("Game Over", True, red)
    screen.blit(msg, [width // 3, height // 3])
    draw_score(score)
    pygame.display.update()
    time.sleep(2)

def game_loop():
    x = width / 2
    y = height / 2
    dx = dy = 0

    snake = []
    length = 1

    foodx = round(random.randrange(0, width - block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block) / 10.0) * 10.0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = block
                    dx = 0

        x += dx
        y += dy

        # Collision with wall
        if x < 0 or x >= width or y < 0 or y >= height:
            game_over_screen(length - 1)
            break

        screen.fill(blue)
        pygame.draw.rect(screen, green, [foodx, foody, block, block])

        head = [x, y]
        snake.append(head)
        if len(snake) > length:
            del snake[0]

        # Collision with self
        if head in snake[:-1]:
            game_over_screen(length - 1)
            break

        draw_snake(snake)
        draw_score(length - 1)
        pygame.display.update()

        # Eating food
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block) / 10.0) * 10.0
            length += 1

        clock.tick(speed)

    pygame.quit()

game_loop()
