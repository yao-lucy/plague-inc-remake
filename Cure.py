class Cure(object):
    def __init__(self):
        self.requirement = 100
        self.efforts = 1.01
        self.completion =  0
        self.completionPercentage = 0
        
    def __repr__(self):
        return "I am a cure!"
    
    def updateStats(self):
        # if self.completion != 0:
        #     self.completion += self.efforts
        if self.completionPercentage < 0.33:
            self.completion *= self.efforts
            self.completionPercentage = self.completion/self.requirement
        elif self.completionPercentage < 0.67:
            self.completion += self.efforts / 5
            self.completionPercentage = self.completion/self.requirement
        else:
            self.completion += self.efforts / 8
            self.completionPercentage = self.completion/self.requirement