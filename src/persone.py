import os
import pygame

FLOOR_Y = 300


class Persone:

    def __init__(self, player_img = 'src/soldier.png', x = 0, y = 0 ):

        self.player_img = pygame.image.load(os.path.join('', player_img ))
        self.player_pos = pygame.Vector2(x, y)
        self.speed_y = 0
    
    def handle_frame(self, keys, dt):
        
        if keys[pygame.K_w]:
            if self.player_pos.y == FLOOR_Y:
                self.speed_y -= 2600
            # self.player_pos.y -= 1000 * dt
        # if keys[pygame.K_s]:
        #     self.player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            self.player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            self.player_pos.x += 300 * dt

        # обновляем положение по y
        self.player_pos.y += self.speed_y * dt

        # ограничени, чтобы не падал
        if self.player_pos.y > FLOOR_Y:
            self.player_pos.y = FLOOR_Y
        
        # обновляем скорость с учетом гравитации (ускорение вниз)
        if self.player_pos.y < FLOOR_Y:
            self.speed_y += 200
