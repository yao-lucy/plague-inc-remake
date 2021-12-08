class Player(object):
    def __init__(self, name = "Player"):
        self.name = name
        self.numDNAPoints = 1000
        self.bubblePoints = 5
    
    def __repr__(self):
        return self.name
    
    def givePoints(self):
        self.numDNAPoints += self.bubblePoints