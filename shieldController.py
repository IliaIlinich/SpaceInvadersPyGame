import pygame 

#load shield sprites
shield_sprites =[["lt",[pygame.image.load("./Sprites/base/top_left/top_left1.png"),pygame.image.load("./Sprites/base/top_left/top_left2.png"),pygame.image.load("./Sprites/base/top_left/top_left3.png"),pygame.image.load("./Sprites/base/top_left/top_left4.png")]],
                 ["lb",[pygame.image.load("./Sprites/base/bottom_left/bottom_left1.png"),pygame.image.load("./Sprites/base/bottom_left/bottom_left2.png"),pygame.image.load("./Sprites/base/bottom_left/bottom_left3.png"),pygame.image.load("./Sprites/base/bottom_left/bottom_left4.png")]],
                 ["rt",[pygame.image.load("./Sprites/base/top_right/top_right1.png"),pygame.image.load("./Sprites/base/top_right/top_right2.png"),pygame.image.load("./Sprites/base/top_right/top_right3.png"),pygame.image.load("./Sprites/base/top_right/top_right4.png")]],
                 ["rb",[pygame.image.load("./Sprites/base/bottom_right/bottom_right1.png"),pygame.image.load("./Sprites/base/bottom_right/bottom_right2.png"),pygame.image.load("./Sprites/base/bottom_right/bottom_right3.png"),pygame.image.load("./Sprites/base/bottom_right/bottom_right4.png")]],
                 ["nm",[pygame.image.load("./Sprites/base/normal/normal1.png"),pygame.image.load("./Sprites/base/normal/normal2.png"),pygame.image.load("./Sprites/base/normal/normal3.png"),pygame.image.load("./Sprites/base/normal/normal4.png")]]]

class Base:
    def __init__(self, shield_sprites):
        self.shield = [[["lt",4],["1",4],["2",4],["rt",4]],
                       [["3",4],["lb",4],["rb",4],["4",4]]
                       [["5",4],["6",0],["7",0],["8",0]]]
        self.damaged_tile = ""
        self.numbers = ["1","2","3","4","5","6","7","8"]
        self.current_space = ""
        self.shield_sprites = shield_sprites
    
    #update the damage on the shield segments
    def update_damage(self):
        for row in range(0,3):
            for column in range(0,4):
                if self.damaged_tile == self.shield[row][column][0]:
                    self.shield[row][column][1] -= 1

    def update_sprite(self):
        if self.damaged_tile == "":
            looping = True
            while looping:
                for row in range(0,3):
                    for column in range(0,4):
                        self.current_space = self.shield[row][column][0]
                        self.new_sprite = self.load_sprite()
                running = False
        else:
            self.current_space = self.damaged_tile
            self.new_sprite = self.load_sprite()


    def preload_sprites(self):
        for i in range(0,5):
            for j in range(0,4):
                self.shield_sprites[i][1][j] = pygame.transform.scale(self.shield_sprites[i][1][j], (70,70))    

    def load_sprite(self):
        self.new_sprite = ""
        for i in range(0,5):
            for j in range(0,4):
                if self.current_space == self.shield_sprites[i][0]:
                    self.new_sprite = self.shield_sprites[i][1][j]
        return self.new_sprite





    
                    


        
        
        

    

