import pygame
import random
import itertools
import alienLevels as ALL
import scoreController as SC
from playerControler import Player as PC
import shieldController as SHC

# Pygame initialisation
pygame.init()
font = pygame.font.SysFont('Arial', 24)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Level initialisation
level = ALL.level()
currentAlienSpeed = int(1 / level.difficulty * 500)

# List of all bullets present on the screen
bullets = []

# Events initialisation

# Alien shooting event
ALIEN_SHOOT_EVENT = pygame.USEREVENT + 1
alienShootCooldown = random.randint(3000, 4000)
pygame.time.set_timer(ALIEN_SHOOT_EVENT, alienShootCooldown)

# Alien movement event
ALIEN_MOVE_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(ALIEN_MOVE_EVENT, currentAlienSpeed)
currentMovement = "right"

# Alien animation event
ALIEN_ANIMATION_EVENT = pygame.USEREVENT + 3
pygame.time.set_timer(ALIEN_ANIMATION_EVENT, 600)
animation_iter = 0

# Player initialisation
player = PC(screen)
playerScore = 0
playerName = "Joe"

# Sprites initialisation

# Alien sprites initialisation
alien_1_sprites = [
    pygame.image.load("./Sprites/Aliens/alien_1_sprite_1.png"),
    pygame.image.load("./Sprites/Aliens/alien_1_sprite_2.png")
]

alien_2_sprites = [
    pygame.image.load("./Sprites/Aliens/alien_2_sprite_1.png"),
    pygame.image.load("./Sprites/Aliens/alien_2_sprite_2.png")
]

alien_3_sprites = [
    pygame.image.load("./Sprites/Aliens/alien_3_sprite_1.png"),
    pygame.image.load("./Sprites/Aliens/alien_3_sprite_2.png")
]

# Player sprites initialisation
player_sprite = pygame.image.load("./Sprites/player_sprite.png")
player_sprite = pygame.transform.scale(player_sprite, (70,40))

# Menu scene initialisation
current_stage = "menu"
menu_game_logo = pygame.image.load("./Sprites/Space_Invaders_Logo.jpg")
menu_game_logo = pygame.transform.scale(menu_game_logo, (500, 500))

# Buttons initialisation
start_button = pygame.Rect(screen.get_width() * 0.25 - 50, screen.get_height() * 0.75, 100, 50)
quit_button = pygame.Rect(screen.get_width() * 0.75 - 50, screen.get_height() * 0.75, 100, 50)
score_button = pygame.Rect(screen.get_width() * 0.50 - 50, screen.get_height() * 0.75, 100, 50)

def game_lost():
    global playerScore, playerName, current_stage, level, bullets, currentMovement, currentAlienSpeed
    # Score upload to JSON file
    score = SC.Score(playerName, playerScore)
    score.pushScoreData()

    # Reset score for the next game
    playerScore = 0

    # Player reinitialisation
    player.lives = 4

    # Game reset
    current_stage = "menu"
    level = ALL.level()
    bullets = []
    level.difficulty = 1
    currentAlienSpeed = int(1 / level.difficulty * 500)
    pygame.time.set_timer(ALIEN_MOVE_EVENT, currentAlienSpeed)

    currentMovement = "right"

def initshields():
    global shields
    shields = []
    for i in range(4):
        shields.append(SHC.Base(screen, [500, (i+1)*256]))

# Main loop
while running:
    # Event handling
    for event in pygame.event.get():

        # If the player quits the game
        if event.type == pygame.QUIT:
            running = False

        # If the player presses escape to enter menu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_stage = "menu"

        # Mouse hover over buttons effects in the menu
        if current_stage == "menu" and event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                current_stage = "game"
                initshields()
            if quit_button.collidepoint(event.pos):
                running = False
            if score_button.collidepoint(event.pos):
                current_stage = "score"

        # In game events
        if current_stage == "game":

            # Alien animation event
            if event.type == ALIEN_ANIMATION_EVENT:
                animation_iter += 1
                if animation_iter >= 2:
                    animation_iter = 0

            # Alien shooting event
            elif event.type == ALIEN_SHOOT_EVENT:
                pygame.time.set_timer(ALIEN_SHOOT_EVENT, random.randint(3000, 4000))

                # Choosing random 1 to 3 aliens to shoot
                for _ in range(random.randint(1, 3)):
                    all_aliens = list(itertools.chain.from_iterable(level.alien_list))
                    alien = random.choice(all_aliens)
                    if alien.alienType == 1:
                        alien.shoot(screen, bullets, 's')
                    elif alien.alienType == 2:
                        alien.shoot(screen, bullets, 'w')
                    else:
                        alien.shoot(screen, bullets, 't')

            # Aliens movement event
            elif event.type == ALIEN_MOVE_EVENT:
                # If current movement is to the right
                if currentMovement == "right":
                    for row in level.alien_list:
                        for alien in row:
                            alien.move_right()
                    if ALL.edgeReachedRight(screen, level):
                        currentMovement = "down"

                # If current movement is to the left
                elif currentMovement == "left":
                    for row in level.alien_list:
                        for alien in row:
                            alien.move_left()
                    if ALL.edgeReachedLeft(level):
                        currentMovement = "down"

                # If currect movement is downwards
                elif currentMovement == "down":
                    for row in level.alien_list:
                        for alien in row:
                            alien.move_down()

                    # Checking wether next movement should be to the right or to the left
                    all_aliens = list(itertools.chain.from_iterable(level.alien_list))
                    rightmost_x = max(alien.get_position().x for alien in all_aliens)
                    if rightmost_x >= screen.get_width() - 60:
                        currentMovement = "left"
                    else:
                        currentMovement = "right"

    # Scene render
    screen.fill("black")

    # Getting mouse position every frame
    mouse_pos = pygame.mouse.get_pos()

    # Menu scene rendering
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

    # Game scene rendering
    elif current_stage == "game":

        # Player rendering
        screen.blit(player_sprite, (int(player.player_pos.x)-35, int(player.player_pos.y)))
        player_rect = pygame.Rect((int(player.player_pos.x)-35, int(player.player_pos.y)+10), (70,40))
        PC.input(player, bullets)

        # Aliens rendering
        level.draw_level(screen, alien_1_sprites, alien_2_sprites, alien_3_sprites, animation_iter)

        # Render shields
        for shield in shields:
            shield.preload_sprites()
            shield.update_sprite()

        # Move bullets
        for bullet in bullets:
            bullet.move(screen, bullets)

        # Bullets collisions handling
        for bullet in bullets:
            bullet_rect = pygame.Rect(bullet.position, (5,10))

            # Player collisions handling
            if player_rect.colliderect(bullet_rect):

                # Temporary fix of a trying to delete not present bullet error
                try:
                    bullets.remove(bullet)
                except ValueError:
                    continue
                player.lives -= 1
                player.player_pos.x = screen.get_width() / 2

                # If the player is dead
                if player.lives <= 0:
                    game_lost()

            # Shields collision handling
            for shield in shields:
                rects = shield.get_rect()
                for y in range(len(rects)):
                    for x in range(len(rects[y])):       
                        if rects[y][x].colliderect(bullet_rect):
                            # Temporary fix of a trying to delete not present bullet error
                            try:
                                bullets.remove(bullet)
                            except ValueError:
                                continue
                            shield.damage_tile([y,x])

            # Aliens collision handling
            row_cnt = -1
            for alien_row in level.alien_list:
                row_cnt += 1
                for alien in alien_row:
                    alien_rect = pygame.Rect((alien.position.x - 35, alien.position.y - 35), (70, 70))

                    # If an alien collides with player's bullet
                    if alien_rect.colliderect(bullet_rect) and bullet.type == 'p':
                        # Changing the speed of alinens, so the smaller is their amount on the screen, the faster they move
                        currentAlienSpeed -= 5
                        if currentAlienSpeed <= 100:
                            currentAlienSpeed = 100
                        pygame.time.set_timer(ALIEN_MOVE_EVENT, currentAlienSpeed)
                        # Temporary fix of a trying to delete not present bullet error
                        try:
                            bullets.remove(bullet)
                        except ValueError:
                            continue
                        alien_row.remove(alien)

                        # Incrementing player score by dedicated number for killing corresponding alien type
                        if alien.alienType == 1:
                            playerScore += 300
                        elif alien.alienType == 2:
                            playerScore += 200
                        else:
                            playerScore += 100

                        # If all aliens were destroyed
                        if len(list(itertools.chain.from_iterable(level.alien_list))) == 0:
                            currentDifficulty = level.difficulty
                            level = ALL.level()
                            level.difficulty = currentDifficulty + 1
                            currentAlienSpeed = int(1 / level.difficulty * 500)

        # Checking if aliens have reached the bottom
        all_aliens = list(itertools.chain.from_iterable(level.alien_list))
        bottomMostY = max(alien.get_position().y for alien in all_aliens)
        if bottomMostY >= screen.get_height() - 100:
            game_lost()
        
    # Score scene rendering
    elif current_stage == "score":
        data = SC.pullScoreData()
        scores = sorted(data, key=lambda x: x["score"], reverse=True)[:10]
        SC.render_scores(scores, font, screen)

    # Screen update and fps lock
    pygame.display.flip()
    clock.tick(60)

pygame.quit()