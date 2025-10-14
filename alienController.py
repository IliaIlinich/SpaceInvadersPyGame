import pygame
import main

# Get screen data from the main module
screen = main.screen

# General alien class
class Alien:
    def __init__(self, pos_x, pos_y):
        self.position = pygame.Vector2(pos_x, pos_y)
    
    def draw(self):
        pygame.draw.circle(screen, "red", self.position, 30)
