import itertools
import alienController as ALC

class level:
    def __init__(self):
        self.alien_list = [[]]
        self.difficulty = 1
        alienType = -1
        for i in range(5):
            if i == 0:
                alienType = 1
            elif 1 <= i <= 2:
                alienType = 2
            else:
                alienType = 3
            alien_line = []
            for j in range(11):
                alien = ALC.Alien(100 + j * 70, 100 + i * 70, alienType)
                alien_line.append(alien)
            self.alien_list.append(alien_line)
    
    def draw_level(self, screen, alien_1_sprites, alien_2_sprites, alien_3_sprites, animation_iter):
        for row in self.alien_list:
            for alien in row:
                if alien.alienType == 1:
                    screen.blit(alien_3_sprites[animation_iter], (alien.get_position().x - 35, alien.get_position().y - 30))
                elif alien.alienType == 2:
                    screen.blit(alien_2_sprites[animation_iter], (alien.get_position().x - 35, alien.get_position().y - 30))
                else:
                    screen.blit(alien_1_sprites[animation_iter], (alien.get_position().x - 35, alien.get_position().y - 30))

# Function to check if aliens have reached the end of the screen
def edgeReachedRight(screen, level):
    edgeReached = False
    all_aliens = list(itertools.chain.from_iterable(level.alien_list))
    for alien in all_aliens:
        if alien.get_position().x >= screen.get_width() - 60:
            edgeReached = True
    return edgeReached

def edgeReachedLeft(level):
    edgeReached = False
    all_aliens = list(itertools.chain.from_iterable(level.alien_list))
    for alien in all_aliens:
        if alien.get_position().x <= 60:
            edgeReached = True
    return edgeReached