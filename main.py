import pygame
import random
import alienController as ALC
import alienLevels as ALL
from playerControler import Player as PC


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Player setup
player = PC(screen)

# level setup
level1 = ALL.level(screen, 0)

# Aliens & Bullets
bullets = []
ALIEN_SHOOT_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ALIEN_SHOOT_EVENT, 3000 - level1.difficulty * 100)  # Adjust shooting frequency based on difficulty
# FIX LATER, so at some point the timer is not less than 0!!!!!!!!

# Alien movement event
ALIEN_MOVE_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(ALIEN_MOVE_EVENT, 600)
current_movement = "right"

# Fix later
alien_sprites = [pygame.image.load("./Sprites/Aliens/alien_1_sprite_1.png"),
                pygame.image.load("./Sprites/Aliens/alien_1_sprite_2.png")]
alien_sprites[0] = pygame.transform.scale(alien_sprites[0], (70, 70))
alien_sprites[1] = pygame.transform.scale(alien_sprites[1], (70, 70))

animation_iter = 0
ALIEN_ANIMATION_EVENT = pygame.USEREVENT + 3
pygame.time.set_timer(ALIEN_ANIMATION_EVENT, 600)


# Main loop
if __name__ == "__main__":
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check for quitting the game
                running = False
            elif event.type == ALIEN_ANIMATION_EVENT: # Event for alien animation
                animation_iter += 1
                if animation_iter >= len(alien_sprites):
                    animation_iter = 0
            elif event.type == ALIEN_SHOOT_EVENT: # Event for bullets update
                for i in range(random.randint(1, 3)):
                    cnt = 0 # Counter to find the correct alien to shoot
                    alien_index = random.randint(0, 54)
                    alien_found = False
                    for row in level1.alien_list:
                        if alien_found:
                            break
                        for alien in row:
                            if cnt == alien_index:
                                alien.shoot(screen, bullets)
                                alien_found = True
                                break
                            else:
                                cnt += 1
                    for bullet in bullets:
                        if bullet.position.y > 720:
                            bullets.remove(bullet)
            elif event.type == ALIEN_MOVE_EVENT: # Event for alien movement
                if current_movement == "right":
                    edge_reached = False
                    for row in level1.alien_list:
                        for alien in row:
                            if alien.get_position().x >= screen.get_width() - 60:
                                edge_reached = True
                                break
                    if edge_reached:
                        current_movement = "down"
                    else:
                        for row in level1.alien_list:
                            for alien in row:
                                alien.move_right()
                elif current_movement == "left":
                    edge_reached = False
                    for row in level1.alien_list:
                        for alien in row:
                            if alien.get_position().x <= 60:
                                edge_reached = True
                                break
                    if edge_reached:
                        current_movement = "down"
                    else:
                        for row in level1.alien_list:
                            for alien in row:
                                alien.move_left()
                elif current_movement == "down":
                    for row in level1.alien_list:
                        for alien in row:
                            alien.move_down()
                    # After moving down, decide next horizontal direction
                    rightmost_x = max(alien.get_position().x for row in level1.alien_list for alien in row)
                    leftmost_x = min(alien.get_position().x for row in level1.alien_list for alien in row)
                    if rightmost_x >= screen.get_width() - 60:
                        current_movement = "left"
                    else:
                        current_movement = "right"
        
        # per-frame update & render (outside the event loop)
        screen.fill("black")

        # Draw player
        pygame.draw.circle(screen, "green", (int(player.player_pos.x), int(player.player_pos.y)), 40)

        # Continuous player movement (checks keys every frame)
        PC.input(player)

        # Draw level
        level1.draw_level(screen)

        # Draw Aliens
        for row in level1.alien_list:
            for alien in row:
                screen.blit(alien_sprites[animation_iter], (alien.get_position().x, alien.get_position().y))

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
