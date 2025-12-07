import json
import os

class Score:
    def __init__(self, score):
        self.score = score
    
    def pushScoreData(self):
        new_entry = {"score": self.score}
        size = os.path.getsize("highestScores.json")
        if size > 0:
            with open("highestScores.json", "r") as f:
                data = json.load(f)
        else:
            data = []
        
        data.append(new_entry)
        data.sort(key=lambda x: x["score"], reverse=True)
        data = data[:10]

        with open("highestScores.json", "w") as f:
            json.dump(data, f)

# ADD POP DATA FUNCTION LATER

def pullScoreData():
    if os.path.getsize("highestScores.json") == 0:
        return []
    with open("highestScores.json", "r") as f:
        return json.load(f)

# Function to render score scene
def render_scores(scores, font, screen):
    startX = screen.get_width() / 2 - 100
    startY = 50
    lineHeight = 40
    if len(scores) > 10:
        scores = scores.sort()
        scores.pop
    for i, entry in enumerate(scores):
        text = f"{i+1}. {entry['score']}"
        img = font.render(text, True, (255, 255, 255))
        screen.blit(img, (startX, startY))
        startY += lineHeight
    