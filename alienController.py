import pygame

# General alien class
class Alien:
    def __init__(self, pos_x, pos_y):
        self.position = pygame.Vector2(pos_x, pos_y)
        self.stage = 0 # Terminal variable for movement testing
        self.timer_move = pygame.USEREVENT + 1

    def draw(self, surface):
        pygame.draw.circle(surface, "red", self.position, 30)

    # Movement
    def move_right(self):
        self.position.x += 60
    
    def move_left(self):
        self.position.x -= 60
    
    def move_up(self):
        self.position.y -= 60

    def move_down(self):
        self.position.y += 60
