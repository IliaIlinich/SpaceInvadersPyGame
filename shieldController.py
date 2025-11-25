import pygame 


class Base:
    def __init__(self):
        self.shield = [[["lt",4],["1",4],["2",4],["rt",4]],
                       [["3",4],["lb",4],["rb",4],["4",4]]
                       [["5",4],["6",0],["7",0],["8",0]]]
        self.damaged_tile = ""
    
    def update_damage(self):
        for i in range(0,3):
            for j in range(0,4):
                if self.damaged_tile == self.shield[i][j][0]:
                    self.shield[i][j][1] -= 1

    
                    


        
        
        

    

