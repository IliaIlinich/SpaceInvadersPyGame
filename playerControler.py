import pygame
import bulletController

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.1)
        self.player_rect = ""
        self.shoot_cooldown = 0
        self.lives = 4


    def input(self, bullets):
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
                self.shoot(bullets)
    
    def shoot(self, bullets):
        new_bullet = bulletController.Bullet(self.player_pos.x, self.player_pos.y, "p")
        new_bullet.draw(self.screen, bullets)