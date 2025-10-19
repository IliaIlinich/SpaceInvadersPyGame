import pygame
import alienController as ALC

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Player setup
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Alien setup
alien1 = ALC.Alien(screen.get_width() / 3, screen.get_height() / 3)
pygame.time.set_timer(alien1.timer_move, 1000)  # Alien movement timer

# Main loop
if __name__ == "__main__":
    while running:
        # Check if the game was closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                # Background setup
                screen.fill("black")

                # Draw player
                pygame.draw.circle(screen, "green", player_pos, 40)

                # (Temporary) Basic player movement
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    player_pos.x -= 10
                if keys[pygame.K_RIGHT]:
                    player_pos.x += 10
                if keys[pygame.K_UP]:
                    player_pos.y -= 10
                if keys[pygame.K_DOWN]:
                    player_pos.y += 10

                # Movement test
                if event.type == alien1.timer_move:
                    if alien1.stage == 0:
                        alien1.move_right()
                        alien1.stage += 1
                    elif alien1.stage == 1:
                        alien1.move_down()
                        alien1.stage += 1
                    elif alien1.stage == 2:
                        alien1.move_left()
                        alien1.stage += 1
                    elif alien1.stage == 3:
                        alien1.move_up()
                        alien1.stage = 0

                # Draw alien
                alien1.draw(screen)

                # Update the display
                pygame.display.flip()

                # The game is fixed to 60 fps
                clock.tick(60)

# Quit Pygame
pygame.quit()
