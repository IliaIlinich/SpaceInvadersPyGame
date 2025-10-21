import pygame

class Bullet():
    def __init__(self, pos_x, pos_y):
        self.active = False
        self.direction = [0, 1]
        self.position = pygame.Vector2(pos_x, pos_y)

    def move(self):
        self.position.x += self.direction[0]
        self.position.y += self.direction[1]
