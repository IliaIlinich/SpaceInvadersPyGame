import pygame
import alienController as ALC

screen = pygame.display.set_mode((1280, 720))

def level1():
    alien_list = [[]]
    for i in range(5):
        alien_line = []
        for j in range(11):
            alien = ALC.Alien(60 + j * (screen.get_width() / 11), 40 + i * 70)
            alien_line.append(alien)
        alien_list.append(alien_line)
    
    for i in range(len(alien_list)):
        for j in range(len(alien_list[i])):
            alien_list[i][j].draw(screen)
