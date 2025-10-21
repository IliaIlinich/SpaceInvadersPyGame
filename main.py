import pygame
import random
import alienController as ALC
import alienLevels as ALL

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Player setup
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.5)

# level setup
level1 = ALL.level(screen)

level_flag = 0

# Aliens & Bullets
bullets = []
ALIEN_SHOOT_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ALIEN_SHOOT_EVENT, 4000)


# Main loop
if __name__ == "__main__":
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check for quitting the game
                running = False
            elif event.type == ALIEN_SHOOT_EVENT: # Event for bullets update
                for row in level1.alien_list:
                    for alien in row:
                        flag = random.randint(0, 1000)
                        if flag > 800:
                            alien.shoot(screen, bullets)
        
        # per-frame update & render (outside the event loop)
        screen.fill("black")

        # Draw player
        pygame.draw.circle(screen, "green", (int(player_pos.x), int(player_pos.y)), 40)

        # Continuous player movement (checks keys every frame)
        keys = pygame.key.get_pressed()
        speed = 5
        if keys[pygame.K_LEFT]:
            player_pos.x -= speed
        if keys[pygame.K_RIGHT]:
            player_pos.x += speed
        if keys[pygame.K_UP]:
            player_pos.y -= speed
        if keys[pygame.K_DOWN]:
            player_pos.y += speed

        # Draw level
        level1.draw_level(screen)

        # Bullets
        for bullet in bullets:
            bullet.move()
            pygame.draw.circle(screen, "white", bullet.position, 10)

        # Update the display
        pygame.display.flip()

        # cap fps
        clock.tick(60)

# Quit Pygame
pygame.quit()
