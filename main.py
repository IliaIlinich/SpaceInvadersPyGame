import pygame
import random
import itertools
import alienLevels as ALL
import scoreController as SC
from playerControler import Player as PC
import shieldController as SHC

# Initialize Pygame
pygame.init()
font = pygame.font.SysFont('Arial', 24)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Level setup
level = ALL.level()

# Aliens & Bullets
bullets = []
ALIEN_SHOOT_EVENT = pygame.USEREVENT + 1
alienShootCooldown = random.randint(3000, 4000)
if alienShootCooldown - level.difficulty * 1000 >= 1:
    alienShootCooldown -= level.difficulty * 1000
else:
  alienShootCooldown = 1
pygame.time.set_timer(ALIEN_SHOOT_EVENT, alienShootCooldown)

# Player setup
player = PC(screen)
playerScore = 0
playerName = "Joe"

# Alien movement event
ALIEN_MOVE_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(ALIEN_MOVE_EVENT, 600)

current_movement = "right"

# Sprites initialisation
alien_sprites = [
    pygame.image.load("./Sprites/Aliens/alien_1_sprite_1.png"),
    pygame.image.load("./Sprites/Aliens/alien_1_sprite_2.png")
]
alien_sprites[0] = pygame.transform.scale(alien_sprites[0], (70, 70))
alien_sprites[1] = pygame.transform.scale(alien_sprites[1], (70, 70))

player_sprite = pygame.image.load("./Sprites/player_sprite.png")
player_sprite = pygame.transform.scale(player_sprite, (70,40))

animation_iter = 0
ALIEN_ANIMATION_EVENT = pygame.USEREVENT + 3
pygame.time.set_timer(ALIEN_ANIMATION_EVENT, 600)

current_stage = "menu"
menu_game_logo = pygame.image.load("./Sprites/Space_Invaders_Logo.jpg")
menu_game_logo = pygame.transform.scale(menu_game_logo, (500, 500))

start_button = pygame.Rect(screen.get_width() * 0.25 - 50, screen.get_height() * 0.75, 100, 50)
quit_button = pygame.Rect(screen.get_width() * 0.75 - 50, screen.get_height() * 0.75, 100, 50)
score_button = pygame.Rect(screen.get_width() * 0.50 - 50, screen.get_height() * 0.75, 100, 50)

def draw_scores(scores, font):
    startX = screen.get_width() / 2 - 100
    startY = 50
    lineHeight=40
    for i, entry in enumerate(scores):
        text = f"{i+1}. {entry['name']} - {entry['score']}"
        img = font.render(text, True, (255, 255, 255))
        screen.blit(img, (startX, startY))
        startY += lineHeight

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
            if score_button.collidepoint(event.pos):
                current_stage = "score"
        if current_stage == "game":
            if event.type == ALIEN_ANIMATION_EVENT:
                animation_iter += 1
                if animation_iter >= len(alien_sprites):
                    animation_iter = 0
            elif event.type == ALIEN_SHOOT_EVENT:
                alienShootCooldown = random.randint(3000, 4000)
                if alienShootCooldown - level.difficulty * 1000 >= 1:
                    alienShootCooldown -= level.difficulty * 1000
                else:
                  alienShootCooldown = 1
                pygame.time.set_timer(ALIEN_SHOOT_EVENT, alienShootCooldown)
                for _ in range(random.randint(1, 3)):
                    all_aliens = list(itertools.chain.from_iterable(level.alien_list))
                    if all_aliens:
                        alien = random.choice(all_aliens)
                        alien.shoot(screen, bullets, random.choice(['s', 'w', 't']), level.difficulty)
            elif event.type == ALIEN_MOVE_EVENT:
                if current_movement == "right":
                    edge_reached = any(
                        alien.get_position().x >= screen.get_width() - 60
                        for row in level.alien_list for alien in row
                    )
                    if edge_reached:
                        current_movement = "down"
                    else:
                        for row in level.alien_list:
                            for alien in row:
                                alien.move_right()
                elif current_movement == "left":
                    edge_reached = any(
                        alien.get_position().x <= 60
                        for row in level.alien_list for alien in row
                    )
                    if edge_reached:
                        current_movement = "down"
                    else:
                        for row in level.alien_list:
                            for alien in row:
                                alien.move_left()
                elif current_movement == "down":
                    for row in level.alien_list:
                        for alien in row:
                            alien.move_down()
                    all_aliens = list(itertools.chain.from_iterable(level.alien_list))
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

        # Scoreboard button
        score_color = (0, 0, 255) if score_button.collidepoint(mouse_pos) else (255, 255, 255)
        pygame.draw.rect(screen, score_color, score_button, width=3)
        text_score = font.render('SCORE', True, score_color)
        screen.blit(text_score, text_score.get_rect(center=score_button.center))

        # Quit button
        quit_color = (255, 0, 0) if quit_button.collidepoint(mouse_pos) else (255, 255, 255)
        pygame.draw.rect(screen, quit_color, quit_button, width=3)
        text_quit = font.render('QUIT', True, quit_color)
        screen.blit(text_quit, text_quit.get_rect(center=quit_button.center))

    elif current_stage == "game":
        screen.blit(player_sprite, (int(player.player_pos.x)-35, int(player.player_pos.y)))
        player_rect = pygame.Rect((int(player.player_pos.x)-35, int(player.player_pos.y)+10), (70,40))
        PC.input(player, bullets, level.difficulty)

        # Draw aliens
        level.draw_level(screen, alien_sprites, animation_iter)

        # Move and draw bullets
        for bullet in bullets[:]:
            bullet.move(screen, bullets)

        for bullet in bullets[:]:
            bullet_rect = pygame.Rect(bullet.position, (5,10))
            if player_rect.colliderect(bullet_rect):
                try:
                    bullets.remove(bullet)
                except ValueError:
                    continue
                player.lives-=1
                player.player_pos.x = screen.get_width()/2
                if player.lives <= 0:
                    
                    score = SC.Score(playerName, playerScore)
                    score.pushScoreData()
                    playerScore = 0

                    player.lives = 4
                    current_stage = "menu"
                    level = ALL.level()

                    # Aliens & Bullets
                    bullets = []
                    ALIEN_SHOOT_EVENT = pygame.USEREVENT + 1
                    pygame.time.set_timer(ALIEN_SHOOT_EVENT, random.randint(3000, 4000))

                    # Player setup
                    player = PC(screen)

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

                    player_sprite = pygame.image.load("./Sprites/player_sprite.png")
                    player_sprite = pygame.transform.scale(player_sprite, (70,40))

                    animation_iter = 0
                    ALIEN_ANIMATION_EVENT = pygame.USEREVENT + 3
                    pygame.time.set_timer(ALIEN_ANIMATION_EVENT, 600)
            for alien_row in level.alien_list:
                for alien in alien_row:
                    alien_rect = pygame.Rect((alien.position.x - 35, alien.position.y - 35), (70, 70))
                    if alien_rect.colliderect(bullet_rect) and bullet.type == 'p':
                        try:
                            bullets.remove(bullet)
                        except ValueError:
                            continue
                        alien_row.remove(alien)
                        player.kill_counter += 1
                        playerScore += 100
                        if player.kill_counter % 55 == 0:
                            currentDifficulty = level.difficulty
                            level.__init__()
                            level.difficulty = currentDifficulty + 1
    elif current_stage == "score":
      data = SC.pullScoreData()
      top10 = sorted(data, key=lambda x: x["score"], reverse=True)[:10]
      draw_scores(top10, font)

    # Screen update and fps lock
    pygame.display.flip()
    clock.tick(60)

pygame.quit()