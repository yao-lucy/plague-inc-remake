from Upgrades import *
from draw import *
from Cure import *

def getBounds(cx, cy, r):
    return cx-r, cy-r, cx+r, cy+r

class Plague(object):
    def __init__(self, name = "The Plague"):
        self.name = name        
        self.severity = 0
        self.lethality = 0
        self.daysUntilDeath = None
        
        self.transmissions = initTransmissions()
        self.symptoms = initSymptoms()
        self.abilities = initAbilities()
        
        self.upgradeTypes = {
            "transmission": self.transmissions,
            "symptom": self.symptoms,
            "ability": self.abilities
            }
        
        # self.infectivity = 1.5 # will remove later
        self.infectivityBasePoints = 3
        self.regionInfectivity = {
            "urban": 0,
            "rural": 0,
            "wealthy": 0,
            "poor": 0,
            "hot": 0,
            "cold": 0,
            "arid": 0,
            "humid": 0,
            }
        self.spreadInfectivity = {
            "land": 0,
            "water": 0,
            "air": 0
            }
        self.spreadBasePoints = {
            "land": 25,
            "water": 10,
            "air": 10
            }
        # len(self.transmissions)+len(self.abilities
        # self.maxPossibleInfectivityPoints = 0 # ~
        # self.maxInfectivityFactor = 10
        # each country has unique infectivityFactor
    
    def __repr__(self):
        return self.name

    ##
    
    def clickedTabs(self, event, data):
        x0 = 0
        y0 = data.tabY0
        x1 = data.width
        y1 = y0 + data.tabHeight
        return x0 < event.x < x1 and y0 < event.y < y1
    
    def findTabClicked(self, event, data):
        options = ["upgrade", "transmission", "symptom", "ability"]
        a = event.x//data.tabWidth
        return options[a]
    
    def clickedBackButton(self, event, data):
        cellW = data.width//3
        cellH = data.height//6
        x = 0
        y = data.height-cellH
        return x < event.x < x + cellW and y < event.y < y + cellH
    
    def mpUpgrade(self, event, data):
        if self.clickedBackButton(event, data):
            data.mode = "play"
        elif self.clickedTabs(event, data):
            upgradeType = self.findTabClicked(event, data)
            data.mode = upgradeType
    
    def drawTabsOverlay(self, canvas, data):
        options = [data.plague.name, "Transmission", "Symptom", "Ability"]
        # canvas.create_rectangle(0, 0, data.width, data.height, width=0, fill=data.darkColor)
        canvas.create_image(data.width//2, data.height//2, image=data.faded)
        cellW = data.width / 4
        cellH = data.tabHeight
        hW = cellW // 2
        hH = cellH // 2
        for i in range(4):
            canvas.create_rectangle(i*cellW, data.tabY0, (i+1)*cellW, cellH+data.tabY0, fill="gray30", outline = "white")
            canvas.create_text(i*cellW+hW, data.tabY0 + hH, text=options[i], font = data.font, fill = "white")
    
    def drawBack(self, canvas, data):
        cellW = data.width//3
        cellH = data.height//6
        x = 0
        y = data.height-cellH
        pointsText = "Points:", data.player.numDNAPoints
        canvas.create_rectangle(x, y, x+cellW, y+cellW, fill = "gray30", outline = "white")
        canvas.create_text(x+cellW//2, y+cellH*(1/3), text=pointsText, fill="white", font = data.font)
        upgradeText = "Click to go back to map."
        canvas.create_text(x+cellW//2, y+cellH*(2/3), text=upgradeText, fill="white", font = data.font)
    
    def drawCountryStats(self, canvas, data):
        characteristicNames = ["Infected", "Dead", "State", "Population", "Density", "Development", "Temperature", "Weather"]
        characteristics = [self.numInfected, self.numDead, self.state, self.population, self.populationDensity, self.development, self.temperature, self.weather]
        
        textColor = "white"
        margin = 50
        boxWidth = 250
        x1 = data.width-margin
        y1 = data.height-margin
        x0 = x1-boxWidth
        y0 = margin
        cx = (x0+x1)//2
        statAmt = len(characteristics)
        cellH = (y1-y0) // statAmt

        for i in range(statAmt):
            canvas.create_rectangle(x0, y0+i*cellH, x1, y0+(i+1)*cellH, fill = "gray30", outline = "white")
            canvas.create_text(x0+10, y0+(i+0.5)*cellH, text = characteristicNames[i], fill = "white", anchor = "w", font = data.font)
            canvas.create_text(cx, y0+(i+0.5)*cellH, text = characteristics[i], fill = "white", anchor = "w", font = data.font)
    
    def drawStats(self, canvas, data):
        characteristicNames = ["Base Infectivity", "Severity", "Lethality"]
        characteristics = [self.infectivityBasePoints, self.severity, self.lethality]
        
        textColor = "white"
        margin = 50
        boxWidth = 250
        x1 = data.width-margin
        y1 = data.height-margin
        x0 = data.width//2 + margin
        y0 = data.tabY1 + margin
        cx = (x0+x1)//2
        statAmt = len(characteristics)
        cellH = (y1-y0) // statAmt

        for i in range(statAmt):
            canvas.create_rectangle(x0, y0+i*cellH, x1, y0+(i+1)*cellH, fill = "gray30", outline = "white")
            canvas.create_text(x0+10, y0+(i+0.5)*cellH, text = characteristicNames[i], fill = "white", anchor = "w", font = data.font)
            canvas.create_text(cx, y0+(i+0.5)*cellH, text = characteristics[i], fill = "white", anchor = "w", font = data.font)
    
    def drawUpgrade(self, canvas, data):
        self.drawTabsOverlay(canvas, data)
        self.drawBack(canvas, data)
        self.drawStats(canvas, data)
    
    ##
    
    def havePrerequisites(self, upgrade, data):
        upgradeType = data.mode
        upgradeList = self.upgradeTypes[upgradeType]
        if upgradeType == "symptom":
            if len(upgrade.prerequisites)==0:
                return True
            for prereqName in upgrade.prerequisites:
                for prereq in upgradeList: # shady code
                    if prereqName == prereq.name:
                        if prereq.inEffect:
                            return True
            return False
        else:
            for prereqName in upgrade.prerequisites:
                for prereq in upgradeList: # shady code
                    if prereqName == prereq.name:
                        if not prereq.inEffect:
                            return False
            return True
        
    def haveDNAPoints(self, upgrade, player):
        return player.numDNAPoints >= upgrade.baseCost
    
    def canUpgrade(self, upgrade, data):
        if upgrade.inEffect:
            return False
        elif not self.havePrerequisites(upgrade, data):
            # print("You have not achieved the prerequisites for %s." % (str(upgrade)))
            return False
        elif not self.haveDNAPoints(upgrade, data.player):
            # print("You need more points to buy %s. Keep collecting!" % (str(upgrade)))
            return False
        return True
    
    def addUpgrade(self, upgrade, data):
        upgrade.inEffect = True
        data.player.numDNAPoints -= upgrade.baseCost
        for type, trait, value in upgrade.effects:
            if type == "infectivity" and trait != None:
                self.regionInfectivity[trait] += value
            elif type == "infectivity" and trait == None:
                self.infectivityBasePoints += value
            elif type == "spread" and trait != None:
                self.spreadInfectivity[trait] += value
            elif type == "severity":
                self.severity += value
                data.cure.requirement += value
            elif type == "lethality":
                if self.lethality == 0 and value != 0:
                    # print(self.name + " is now lethal.")
                    self.lethality += value
                    data.cure.efforts += value / 1000
                    self.daysUntilDeath = 100
                elif value != 0:
                    self.lethality += value
                    data.cure.efforts += value / 50
                    self.daysUntilDeath -= value
    
    ##

    def drawList(self, canvas, data):
        upgradeType = data.mode
        upgradeList = self.upgradeTypes[upgradeType]
        upgradeAmt = len(upgradeList)
        for up in upgradeList:
            color = ""
            if up.inEffect: color = "IndianRed1"
            elif self.canUpgrade(up, data): color = "IndianRed3"
            else: color = "gray70"
            up.draw(canvas, data, color)

    def drawUpgrades(self, canvas, data):
        self.drawTabsOverlay(canvas, data)
        self.drawBack(canvas, data)
        self.drawList(canvas, data)

    def clickedUpgrade(self, event, data):
        upgradeType = data.mode
        upgradeList = self.upgradeTypes[upgradeType]
        flag = False
        for up in upgradeList:
            cx, cy, r = up.getUpdateCoords(data)
            x0, y0, x1, y1 = getBounds(cx, cy, r)
            if x0 < event.x < x1 and y0 < event.y < y1:
                flag = True
        return flag
        
    def getClickedUpgrade(self, event, data):
        upgradeType = data.mode
        upgradeList = self.upgradeTypes[upgradeType]
        for up in upgradeList:
            cx, cy, r = up.getUpdateCoords(data)
            x0, y0, x1, y1 = getBounds(cx, cy, r)
            if x0 < event.x < x1 and y0 < event.y < y1:
                return up

    def mpUpgrades(self, event, data):
        if self.clickedBackButton(event, data):
            data.mode = "play"
        elif self.clickedTabs(event, data):
            upgradeType = self.findTabClicked(event, data)
            if data.mode != upgradeType:
                data.mode = upgradeType
        elif self.clickedUpgrade(event, data):
            upgradeClicked = self.getClickedUpgrade(event, data)
            if self.canUpgrade(upgradeClicked, data):
                self.addUpgrade(upgradeClicked, data)
        if self.severity >= 20 and data.cure.completion == 0:
            data.cure.completion = 1
            print("Research for the cure for %s has begun." % (data.plague.name))
        if self.severity < 20: data.player.bubblePoints = 7
        elif self.severity < 50: data.player.bubblePoints = 12
        else: data.player.bubblePoints = 10