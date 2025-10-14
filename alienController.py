import pygame

# General alien class
class Alien:
    def __init__(self, pos_x, pos_y):
        self.position = pygame.Vector2(pos_x, pos_y)

screen = pygame.display.set_mode((1280, 720))

# (Temporary) function to draw an alien
def draw_alien(alien_in):
    pygame.draw.circle(screen, "red", alien_in.position, 30)