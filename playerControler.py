import pygame

class Player:
    def __init__(self, screen):
        self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.1)
        self.shoot_cooldown = 0
        

    def input(self):
        self.shoot_cooldown -= 1
        keys = pygame.key.get_pressed()
        speed = 5
        if keys[pygame.K_LEFT]:
            self.player_pos.x -= speed
        if keys[pygame.K_RIGHT]:
            self.player_pos.x += speed
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0:
                self.shoot_cooldown = 60
                self.shoot()
    
    def shoot(self):
        print("shoot")