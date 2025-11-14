# Example file showing a basic pygame "game loop"
from bullet import Bullet
from persone import Persone
import pygame
import os

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

bullet =  Bullet(pos_x = 100, pos_y = 100)
persone = Persone(x = screen.get_width() / 2, y = screen.get_height() / 2)

dt = 0


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    
    # RENDER YOUR GAME HERE
    
    # квадрат
    # rect1 = pygame.Rect((player_pos.x, player_pos.y, 40, 40))
    # pygame.draw.rect(screen, "red", rect1)

    # круг, Михаил
    # pygame.draw.circle(screen, "red", player_pos, 40)

    screen.blit(persone.player_img, persone.player_pos)
    pygame.draw.circle(screen, "red", (bullet.x, bullet.y), bullet.size )
    keys = pygame.key.get_pressed()
    persone.handle_frame(keys, dt, bullet)
    bullet.handle_frame(dt)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
