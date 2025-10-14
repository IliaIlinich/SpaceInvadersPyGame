import pygame

# General alien class
class Alien:
    def __init__(self, pos_x, pos_y):
        self.position = pygame.Vector2(pos_x, pos_y)

    def draw(self, surface):
        pygame.draw.circle(surface, "red", self.position, 30)
