import pygame 

#load shield sprites
shield_sprites =[["lt",[pygame.image.load("./Sprites/base/top_left/top_left1.png"),pygame.image.load("./Sprites/base/top_left/top_left2.png"),pygame.image.load("./Sprites/base/top_left/top_left3.png"),pygame.image.load("./Sprites/base/top_left/top_left4.png")]],
                 ["lb",[pygame.image.load("./Sprites/base/bottom_left/bottom_left1.png"),pygame.image.load("./Sprites/base/bottom_left/bottom_left2.png"),pygame.image.load("./Sprites/base/bottom_left/bottom_left3.png"),pygame.image.load("./Sprites/base/bottom_left/bottom_left4.png")]],
                 ["rt",[pygame.image.load("./Sprites/base/top_right/top_right1.png"),pygame.image.load("./Sprites/base/top_right/top_right2.png"),pygame.image.load("./Sprites/base/top_right/top_right3.png"),pygame.image.load("./Sprites/base/top_right/top_right4.png")]],
                 ["rb",[pygame.image.load("./Sprites/base/bottom_right/bottom_right1.png"),pygame.image.load("./Sprites/base/bottom_right/bottom_right2.png"),pygame.image.load("./Sprites/base/bottom_right/bottom_right3.png"),pygame.image.load("./Sprites/base/bottom_right/bottom_right4.png")]],
                 ["nm",[pygame.image.load("./Sprites/base/normal/normal1.png"),pygame.image.load("./Sprites/base/normal/normal2.png"),pygame.image.load("./Sprites/base/normal/normal3.png"),pygame.image.load("./Sprites/base/normal/normal4.png")]]]

class Base:
    def __init__(self, screen, location):
        self.shield = [[["lt",4],["1",4],["2",4],["rt",4]],
                       [["3",4],["lb",4],["rb",4],["4",4]],
                       [["5",4],["0",0],["0",0],["8",4]]]
        self.damaged_tile = ""
        self.numbers = ["1","2","3","4","5","6","7","8"]
        self.current_space = ""
        self.shield_sprites = shield_sprites
        self.screen = screen
        self.location = location
    
    #update the damage on the shield segments
    def update_damage(self):
        for row in range(0,3):
            for column in range(0,4):
                if self.damaged_tile == self.shield[row][column][0]:
                    self.shield[row][column][1] -= 1
        self.check_health()

    def update_sprite(self):
        for row in range(0,3):
            for column in range(0,4):
                if self.shield[row][column][0] == "0":
                    continue
                self.current_space = self.shield[row][column][0]
                self.new_sprite = self.load_sprite(self.shield[row][column][1]-1)
                self.screen.blit(self.new_sprite, (self.location[1]+column*25, self.location[0]+row*25))

    def preload_sprites(self):
        for i in range(0,5):
            for j in range(0,4):
                #print(self.shield_sprites[i][1][j])
                self.shield_sprites[i][1][j] = pygame.transform.scale(self.shield_sprites[i][1][j], (25,25))   

    def load_sprite(self, health):
        #print(health)
        self.new_sprite = ""
        if self.current_space in self.numbers:
            self.current_space = "nm"
        for i in range(0,5):
            if self.current_space == self.shield_sprites[i][0]:
                self.new_sprite = self.shield_sprites[i][1][health]
        return self.new_sprite
    
    def check_health(self):
        for row in range(0,3):
            for column in range(0,4):
                if self.shield[row][column][0] == "0":
                    continue
                if self.shield[row][column][1] <= 0:
                    self.shield[row][column][0] = "0"
                else:
                    self.update_sprite()
                    
    def get_rect(self):
        rects = []
        for y in range(3):
            rects.append([])
            for x in range(4):
                if self.shield[y][x][0] == "0":
                    continue
                rects[y].append(pygame.Rect((self.location[1]+x*25, self.location[0]+y*25), (25,25)))
        return rects

    def damage_tile(self, tile):
        self.shield[tile[0]][tile[1]][1] -= 1
        self.check_health()
                