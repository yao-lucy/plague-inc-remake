from transmissiondata import *
from symptomdata import *
from abilitydata import *

class PlagueUpgrade(object):
    def __init__(self, name, baseCost, effects, prerequisites, gridCoords=(0, 0)):
        self.name = name
        self.baseCost = baseCost
        self.effects = effects
        self.prerequisites = prerequisites
        self.inEffect = False
        
        self.col, self.row = gridCoords
        self.cx, self.cy, self.r = None, None, None
    
    def __repr__(self):
        result = ""
        if " " in self.name:
            a = self.name.split()
            for b in a:
                result += b+"\n"
            result = result[:-1]
        else: result = self.name
        return result
        # return self.name
    
    def getUpdateCoords(self, data):
        yMargin = 15
        ySpace = data.dashboardY0-data.tabY1 - yMargin*2
        upgradeDiameter = ySpace // 6
        upgradeRadius = upgradeDiameter//2
        xSpace = upgradeDiameter*9
        xMargin = (data.width-xSpace) // 2
        
        x0 = xMargin
        y0 = data.tabY1+yMargin
        x1 = data.width-xMargin
        y1 = data.height-data.dashboardY0
    
        upgradeCX = self.col*upgradeDiameter+x0+upgradeRadius
        if self.col % 2 == 0:
            upgradeCY = self.row*upgradeDiameter+y0+upgradeRadius
        else:
            upgradeCY = (self.row+0.5)*upgradeDiameter+y0+upgradeRadius
        self.cx, self.cy, self.r = upgradeCX, upgradeCY, upgradeRadius
        return upgradeCX, upgradeCY, upgradeRadius
        
    def draw(self, canvas, data, color):
        cx, cy, r = self.getUpdateCoords(data)
        canvas.create_rectangle(cx-r, cy-r, cx+r, cy+r, fill = color, outline = "white")
        canvas.create_text(cx, cy, text = str(self), fill = "white", justify="center")

class Transmission(PlagueUpgrade): # can increase infectivity only
    pass

class Symptom(PlagueUpgrade): # can increase infectivity, severity, and lethality
    pass

class Ability(PlagueUpgrade): # can increase severity, and therefore lethality
    pass
    
def initTransmissions():
    result = []
    for transmissionName in transmissionNames:
        result.append(Transmission(transmissionName, transmissionBaseCosts[transmissionName], transmissionEffects[transmissionName], transmissionPrerequisites[transmissionName], transmissionGridCoords[transmissionName]))
    return result

def initSymptoms():
    result = []
    for symptomName in symptomNames:
        result.append(Symptom(symptomName, symptomBaseCosts[symptomName], symptomEffects[symptomName], symptomPrerequisites[symptomName], symptomGridCoords[symptomName]))
    return result

def initAbilities():
    result = []
    for abilityName in abilityNames:
        result.append(Ability(abilityName, abilityBaseCosts[abilityName], abilityEffects[abilityName], abilityPrerequisites[abilityName], abilityGridCoords[abilityName]))
    return result