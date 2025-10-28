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
level1 = ALL.level(screen, 0)

# Aliens & Bullets
bullets = []
ALIEN_SHOOT_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ALIEN_SHOOT_EVENT, 1000 - level1.difficulty * 100)  # Adjust shooting frequency based on difficulty
# FIX LATER, so at some point the timer is not less than 0!!!!!!!!

# Alien movement event
ALIEN_MOVE_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(ALIEN_MOVE_EVENT, 1000)
current_movement = "right"

# Main loop
if __name__ == "__main__":
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check for quitting the game
                running = False
            elif event.type == ALIEN_SHOOT_EVENT: # Event for bullets update
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
