import sysconfig
import pygame
import math

# Initialize Pygame
pygame.init() 

# Set the width and height of the screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption('Bouncing Ball Animation')

# Set the ball's starting position and size
ball_x = screen_width/2
ball_y = screen_height/2
ball_size = 20

# Set the ball's starting velocity
velocity_x = 2
velocity_y = 2

# Set the ball's acceleration due to gravity
gravity = 0.1

# Set the ball's rotation
rotation = 0

# Set the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sysconfig.exit()

    # Update the ball's position
    ball_x += velocity_x
    ball_y += velocity_y

    # Check if the ball has hit a wall
    if ball_x > screen_width - ball_size or ball_x < 0:
        velocity_x = -velocity_x
    if ball_y > screen_height - ball_size or ball_y < 0:
        velocity_y = -velocity_y

    # Update the ball's velocity due to gravity
    velocity_y += gravity

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ball
    pygame.draw.circle(screen, (255, 255, 255), (int(ball_x), int(ball_y)), ball_size)

    # Rotate the ball
    rotated_image = pygame.transform.rotate(screen, rotation)
    rotation += 10
    if rotation > 360:
        rotation = 0

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)
