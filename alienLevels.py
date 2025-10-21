import pygame
import alienController as ALC

class level:
    def __init__(self, screen):
        self.alien_list = [[]]
        for i in range(5):
            alien_line = []
            for j in range(11):
                alien = ALC.Alien(60 + j * (screen.get_width() / 11), 40 + i * 70)
                alien_line.append(alien)
            self.alien_list.append(alien_line)
    
    def draw_level(self, screen):
        for i in range(len(self.alien_list)):
            for j in range(len(self.alien_list[i])):
                self.alien_list[i][j].draw(screen)