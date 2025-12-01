import pygame
import alienController as ALC

class level:
    def __init__(self):
        self.alien_list = [[]]
        self.difficulty = 1
        for i in range(5):
            alien_line = []
            for j in range(11):
                alien = ALC.Alien(60 + j * 70, 40 + i * 70)
                alien_line.append(alien)
            self.alien_list.append(alien_line)
    
    def draw_level(self, screen, alien_sprites, animation_iter):
        for row in self.alien_list:
            for alien in row:
                screen.blit(alien_sprites[animation_iter], (alien.get_position().x - 35, alien.get_position().y - 30))