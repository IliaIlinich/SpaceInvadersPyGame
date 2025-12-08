import pygame

class Bullet():
    def __init__(self, pos_x, pos_y, type):
        self.active = False
        self.position = pygame.Vector2(pos_x, pos_y)
        self.type = type # s, w, t, p - square bullet, wave bullet, triangle bullet, player bullet. Each with different speed.
        if self.type == 's':
            self.direction = [0, 7]
        elif self.type == 'w':
            self.direction = [0, 5]
        elif self.type == 't':
            self.direction = [0, 3]
        elif self.type == "p":
            self.direction = [0,-5]

    def draw(self, screen, arr_bullets_in):
        if self.type == 's':
            pygame.draw.rect(screen, "white", (self.position.x, self.position.y, 5, 10))
        elif self.type == 'w':
            pygame.draw.circle(screen, "yellow", (self.position.x, self.position.y), 5)
        elif self.type == 't':
            pygame.draw.polygon(screen, "red", [(self.position.x, self.position.y), (self.position.x + 5, self.position.y - 10), (self.position.x - 5, self.position.y - 10)])
        elif self.type == 'p':
            pygame.draw.rect(screen, "white", (self.position.x, self.position.y, 5, 10))
        else:
            print("Unknown bullet type")
        arr_bullets_in.append(self)

    def move(self, screen, bullets):
        self.position.x += self.direction[0]
        self.position.y += self.direction[1]
        if self.type == 's':
            pygame.draw.rect(screen, "white", (self.position.x, self.position.y, 5, 10))
        elif self.type == 'w':
            pygame.draw.circle(screen, "yellow", (self.position.x, self.position.y), 5)
        elif self.type == 't':
            pygame.draw.polygon(screen, "red", [(self.position.x, self.position.y), (self.position.x + 5, self.position.y - 10), (self.position.x - 5, self.position.y - 10)])
        elif self.type == 'p':
            pygame.draw.rect(screen, "white", (self.position.x, self.position.y, 5, 10))
        else:
            print("Unknown bullet type")
        if self.position.y > screen.get_height() or self.position.y < 0:
            bullets.remove(self)