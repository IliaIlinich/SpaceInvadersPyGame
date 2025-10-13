import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #background
    screen.fill("black")

    #player
    pygame.draw.circle(screen, "green", player_pos, 40)

    # basic movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos.x -= 10
    if keys[pygame.K_RIGHT]:
        player_pos.x += 10
    if keys[pygame.K_UP]:
        player_pos.y -= 10
    if keys[pygame.K_DOWN]:
        player_pos.y += 10

    pygame.display.flip()

    # 60 fps
    clock.tick(60)

pygame.quit()
