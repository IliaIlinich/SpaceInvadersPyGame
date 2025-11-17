import pygame
import random
import itertools
import alienLevels as ALL
from playerControler import Player as PC

# Initialize Pygame
pygame.init()
font = pygame.font.SysFont('Arial', 24)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Player setup
player = PC(screen)

# Level setup
level1 = ALL.level(screen, 0)

# Aliens & Bullets
bullets = []
ALIEN_SHOOT_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ALIEN_SHOOT_EVENT, random.randint(3000, 4000))

# Alien movement event
ALIEN_MOVE_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(ALIEN_MOVE_EVENT, 600)

current_movement = "right"

alien_sprites = [
    pygame.image.load("./Sprites/Aliens/alien_1_sprite_1.png"),
    pygame.image.load("./Sprites/Aliens/alien_1_sprite_2.png")
]
alien_sprites[0] = pygame.transform.scale(alien_sprites[0], (70, 70))
alien_sprites[1] = pygame.transform.scale(alien_sprites[1], (70, 70))

animation_iter = 0
ALIEN_ANIMATION_EVENT = pygame.USEREVENT + 3
pygame.time.set_timer(ALIEN_ANIMATION_EVENT, 600)

current_stage = "menu"
menu_game_logo = pygame.image.load("./Sprites/Space_Invaders_Logo.jpg")
menu_game_logo = pygame.transform.scale(menu_game_logo, (500, 500))

start_button = pygame.Rect(screen.get_width() * 0.33 - 50, screen.get_height() * 0.75, 100, 50)
quit_button = pygame.Rect(screen.get_width() * 0.66 - 50, screen.get_height() * 0.75, 100, 50)

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_stage = "menu"
        if current_stage == "menu" and event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                current_stage = "game"
            if quit_button.collidepoint(event.pos):
                running = False
        if current_stage == "game":
            if event.type == ALIEN_ANIMATION_EVENT:
                animation_iter += 1
                if animation_iter >= len(alien_sprites):
                    animation_iter = 0
            elif event.type == ALIEN_SHOOT_EVENT:
                pygame.time.set_timer(ALIEN_SHOOT_EVENT, random.randint(3000, 4000))
                for _ in range(random.randint(1, 3)):
                    all_aliens = list(itertools.chain.from_iterable(level1.alien_list))
                    if all_aliens:
                        alien = random.choice(all_aliens)
                        alien.shoot(screen, bullets, random.choice(['s', 'w', 't']))
            elif event.type == ALIEN_MOVE_EVENT:
                if current_movement == "right":
                    edge_reached = any(
                        alien.get_position().x >= screen.get_width() - 60
                        for row in level1.alien_list for alien in row
                    )
                    if edge_reached:
                        current_movement = "down"
                    else:
                        for row in level1.alien_list:
                            for alien in row:
                                alien.move_right()
                elif current_movement == "left":
                    edge_reached = any(
                        alien.get_position().x <= 60
                        for row in level1.alien_list for alien in row
                    )
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
                    all_aliens = list(itertools.chain.from_iterable(level1.alien_list))
                    if all_aliens:
                        rightmost_x = max(alien.get_position().x for alien in all_aliens)
                        if rightmost_x >= screen.get_width() - 60:
                            current_movement = "left"
                        else:
                            current_movement = "right"

    screen.fill("black")

    mouse_pos = pygame.mouse.get_pos()

    if current_stage == "menu":
        # Menu rendering
        screen.blit(menu_game_logo, (screen.get_width() / 2 - 250, 50))

        # Start button
        start_color = (0, 255, 0) if start_button.collidepoint(mouse_pos) else (255, 255, 255)
        pygame.draw.rect(screen, start_color, start_button, width=3)
        text_start = font.render('START', True, start_color)
        screen.blit(text_start, text_start.get_rect(center=start_button.center))

        # Quit button
        quit_color = (255, 0, 0) if quit_button.collidepoint(mouse_pos) else (255, 255, 255)
        pygame.draw.rect(screen, quit_color, quit_button, width=3)
        text_quit = font.render('QUIT', True, quit_color)
        screen.blit(text_quit, text_quit.get_rect(center=quit_button.center))

    elif current_stage == "game":
        pygame.draw.circle(screen, "green", (int(player.player_pos.x), int(player.player_pos.y)), 40)
        PC.input(player)

        # Draw aliens
        level1.draw_level(screen, alien_sprites, animation_iter)

        # Move and draw bullets
        for bullet in bullets[:]:
            bullet.move(screen, bullets)

    # Screen update and fps lock
    pygame.display.flip()
    clock.tick(60)

pygame.quit()