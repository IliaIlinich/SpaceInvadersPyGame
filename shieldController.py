import pygame 

shield_sprites =[["lt",[1,2,3,4]],
                 ["lb",[1,2,3,4]],
                 ["rt",[1,2,3,4]],
                 ["rb",[1,2,3,4]],
                 ["nm",[1,2,3,4]]]

class Base:
    def __init__(self):
        self.shield = [[["lt",4],["1",4],["2",4],["rt",4]],
                       [["3",4],["lb",4],["rb",4],["4",4]]
                       [["5",4],["6",0],["7",0],["8",0]]]
        self.damaged_tile = ""
        self.numbers = ["1","2","3","4","5","6","7","8"]
        self.current_space = ""
    
    def update_damage(self):
        for i in range(0,3):
            for j in range(0,4):
                if self.damaged_tile == self.shield[i][j][0]:
                    self.shield[i][j][1] -= 1

    def update_sprite(self, shield_sprites):
        if self.damaged_tile == "":
            looping = True
            while looping:
                for i in range(0,3):
                    for j in range(0,4):
                        self.current_space = self.shield[i][j][0]
                        




    
                    


        
        
        

    

