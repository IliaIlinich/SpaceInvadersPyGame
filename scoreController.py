import json
import os

class Score:
    def __init__(self, name, score):
        self.score = score
        self.name = name
    
    def pushScoreData(self):
        new_entry = {"name": self.name, "score": self.score}

        if os.path.getsize("highestScores.json") > 0:
            with open("highestScores.json", "r") as f:
                data = json.load(f)
        else:
            data = []

        data.append(new_entry)

        with open("highestScores.json", "w") as f:
            json.dump(data, f)

# ADD POP DATA FUNCTION LATER

def pullScoreData():
    if os.path.getsize("highestScores.json") == 0:
        return []
    with open("highestScores.json", "r") as f:
        return json.load(f)

'''
scoreTest1 = Score("john", 300)
scoreTest1.pushScoreData()

scoreTest2 = Score("anna", 500)
scoreTest2.pushScoreData()

pulledData = pullScoreData()
for name in pulledData:
    print(name["name"])
'''