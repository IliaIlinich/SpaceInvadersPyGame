import pygame
import bulletController

# General alien class
class Alien:
    def __init__(self, pos_x, pos_y):
        self.position = pygame.Vector2(pos_x, pos_y)

    def get_position(self):
        return self.position

    # Movement
    def move_right(self):
        self.position.x += 10
    
    def move_left(self):
        self.position.x -= 10

    def move_down(self):
        self.position.y += 60

    def shoot(self, screen, arr_bullets_in, bullet_type, difficulty):
        new_bullet = bulletController.Bullet(self.position.x, self.position.y, bullet_type, difficulty)
        new_bullet.draw(screen, arr_bullets_in)
