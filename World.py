import random
from countrydata import *
from draw import *
from Transport import *

def getBounds(cx, cy, r):
    return cx-r, cy-r, cx+r, cy+r

def distance(x0, y0, x1, y1):
    return ((x0-x1)**2+(y0-y1)**2)**(1/2)

def getCountries():
    result = []
    for countryName in countryNames:
        result.append(Country(countryName, population[countryName], populationDensity[countryName], development[countryName], temperature[countryName], weather[countryName], airOut[countryName], waterOut[countryName], neighbors[countryName], coords[countryName]))
    return result
    
def getStats(countries):
    population = 0
    numInfected = 0
    numDead = 0
    for country in countries:
        population += country.population
        numInfected += country.numInfected
        numDead += country.numDead
    return population, numInfected, numDead

class World(object):    
    def __init__(self):
        self.countries = getCountries()
        self.numDays = 0
        self.news = []
        self.infectCountryZero()
        self.population, self.numInfected, self.numDead = getStats(self.countries)
        self.stillHope = True
        self.graphStats = {0: (1, 0)}
        self.dailyTransports = []
    
    def __repr__(self):
        result = ""
        for country in self.countries:
            result += str(country) + ", "
        result = result[:-2] # getting rid of last ", "
        return result
    
    def infectCountryZero(self):
        countryZero = random.choice(self.countries)
        countryZero.infectZero(self.numDays)
        self.news.append("%s is the first continent infected with the plague." % (str(countryZero)))
    
    ##
    
    def clickedUpgradeButton(self, event, data):
        cellW = data.width//3
        cellH = data.height//6
        x = 0
        y = data.height-cellH
        return x < event.x < x + cellW and y < event.y < y + cellH
    
    def checkClickedCountry(self, event, data):
        data.countryClicked = None
        for country in self.countries:
            if country.cx-country.baseR <= event.x <= country.cx+country.baseR and country.cy-country.baseR <= event.y <= country.cy+country.baseR:
                data.countryClicked = country
                data.mode = "country"
    
    def checkClickedBubble(self, event, data):
        for country in self.countries:
            if country.hasBubble and country.clickedBubble(event, data):
                countryClicked = country
                country.hasBubble = False
                data.player.givePoints()
                break
    
    def mpPlay(self, event, data):
        self.checkClickedCountry(event, data)
        self.checkClickedBubble(event, data)
        if self.clickedUpgradeButton(event, data):
            data.mode = "upgrade"
    
    ##
    
    def addDay(self):
        self.numDays += 1
    
    def spreadPlagueByAir(self, plague, data):
        for country in self.countries:
            spreadProbability = country.getSpreadProbability(plague, "air")
            potentialVictims = []
            for neighborName in country.neighbors:
                for country2 in self.countries:
                    if neighborName == str(country2):
                        if not country2.inQuarantine and country2.state == "healthy":
                            potentialVictims.append(country2)
            for potentialVictim in potentialVictims:
                q = random.random()
                if q <= spreadProbability:
                    potentialVictim.infect(self.numDays, data)
                    print("The plague has spread by air from %s to %s." % (country.name, potentialVictim.name))
    
    def spreadPlagueByWater(self, plague, data):
        for country in self.countries:
            spreadProbability = country.getSpreadProbability(plague, "water")
            potentialVictims = []
            for neighborName in country.neighbors:
                for country2 in self.countries:
                    if neighborName == str(country2):
                        if not country2.inQuarantine and country2.state == "healthy":
                            potentialVictims.append(country2)
            for potentialVictim in potentialVictims:
                q = random.random()
                if q <= spreadProbability:
                    potentialVictim.infect(self.numDays, data)
                    print("The plague has spread by water from %s to %s." % (country.name, potentialVictim.name))

    def spreadPlagueByLand(self, plague, data):
        for country in self.countries:
            spreadProbability = country.getSpreadProbability(plague, "land")
            potentialVictims = []
            for neighborName in country.neighbors:
                for country2 in self.countries:
                    if neighborName == str(country2):
                        if not country2.inQuarantine and country2.state == "healthy":
                            potentialVictims.append(country2)
            for potentialVictim in potentialVictims:
                q = random.random()
                if q <= spreadProbability:
                    potentialVictim.infect(self.numDays, data)
                    print("The plague has spread by land from %s to %s." % (country.name, potentialVictim.name))
                    
    # def getDailyTransport(self):
    #     transportTodayProb = 0.25
    #     res = []
    #     for country in self.countries:
    #         if random.random() <= transportTodayProb:
    #             potentialDestinations = {"water": country.waterOut, "air": country.airOut, "land": country.neighbors}
    #             typeToday = random.choice(list(potentialDestinations.keys()))
    #             # print(typeToday)
    #             if len(list(potentialDestinations[typeToday]))==0: continue
    #             destinationToday = random.choice(list(potentialDestinations[typeToday]))
    #             for country2 in self.countries:
    #                 if destinationToday == str(country2):
    #                     fr = country
    #                     to = country2
    #                     if typeToday == "water":
    #                         res.append(Boat(fr, to))
    #                     elif typeToday == "air":
    #                         res.append(Plane(fr, to))
    #                     else: res.append(Bird(fr, to))
    #     # print(res)
    #     return res
    
    def getDailyTransport(self, data):
        transportTodayProb = 0.25
        res = []
        for country in self.countries:
            if random.random() <= transportTodayProb:
                potentialDestinations = {"water": country.waterOut, "air": country.airOut, "land": country.neighbors}
                typeToday = random.choice(list(potentialDestinations.keys()))
                spreadProbability = country.getSpreadProbability(data.plague, typeToday)
                transportType = {"water": "boat", "air": "airplane", "land": "bird"}
                if len(list(potentialDestinations[typeToday]))==0: continue
                destinationToday = random.choice(list(potentialDestinations[typeToday]))
                for country2 in self.countries:
                    if destinationToday == str(country2):
                        transportState = "healthy"
                        fr = country
                        to = country2
                        if fr.state == "infected" and to.state == "healthy":
                            if random.random() <= spreadProbability:
                                to.infect(self.numDays, data)
                                transportState = "infected"
                                self.news.append("An infected %s is going from %s to %s." % (transportType[typeToday], str(fr), str(to)))
                                self.news.append("First occurence of the plague found in %s." % (str(self)))
                        elif fr.state == "infected" and to.state == "infected":
                            transportState = "infected"
                        if typeToday == "water":
                            res.append(Boat(fr, to, transportState))
                        elif typeToday == "air":
                            res.append(Plane(fr, to, transportState))
                        else: res.append(Bird(fr, to, transportState))
        return res
                
    def spreadPlagueOutCountry(self, plague, data):
        self.spreadPlagueByAir(plague, data)
        self.spreadPlagueByWater(plague, data)
        self.spreadPlagueByLand(plague, data)
    
    def spreadPlague(self, plague, data):
        for country in self.countries:
            if country.state == "infected":
                country.spreadPlagueInCountry(plague, self.numDays)
        self.dailyTransports = self.getDailyTransport(data)
        # self.spreadPlagueOutCountry(plague, data)
    
    def killInfected(self, plague):
        for country in self.countries:
            for day in country.dailyInfected:
                daysSinceInfected = self.numDays-day
                if plague.daysUntilDeath != None and daysSinceInfected >= plague.daysUntilDeath:
                    country.numInfected -= country.dailyInfected[day]
                    country.numDead += country.dailyInfected[day]
                    country.dailyInfected[day] = 0
    
    def updateStats(self):
        self.population, self.numInfected, self.numDead = getStats(self.countries)
        for country in self.countries:
            if country.numDead == country.population:
                if country.state != "destroyed":
                    print("%s is destroyed. RIP." % (str(country)))
                country.state = "destroyed"
            country.r = (country.numInfected/country.population) * country.maxRadius
        if self.numInfected + self.numDead == self.population:
            if self.stillHope == True:
                print("There are no more healthy people left in the world.")
                self.stillHope = False
    
    def collectGraphStats(self):
        self.graphStats[self.numDays] = (self.numInfected, self.numDead)
    
    def isWin(self):
        for country in self.countries:
            if not country.state == "destroyed":
                return False
        return True
    
    def isLose(self, data):
        if data.cure == None:
            return False
        else: return data.cure.completionPercentage >= 1 or self.numDays >= 1000
    
    def getInfectedCountries(self):
        res = []
        for country in self.countries:
            if country.state == "infected":
                res.append(country)
        return res
    
    def updateBubbles(self, data):
        if data.timeCount % (data.inGameDay*5) == 0:
            for country in self.countries:
                if country.hasBubble:
                    country.hasBubble = False
            infectedCountries = self.getInfectedCountries()
            countryWithBubble = random.choice(infectedCountries)
            countryWithBubble.hasBubble = True
    
    def updateDailyTransports(self):
        for tr in self.dailyTransports:
            tr.move()
    
    def tfPlay(self, data):
        #print(data.timeCount)
        data.timeCount += 1
        self.updateDailyTransports()
        if data.timeCount % data.inGameDay == 0:
            self.addDay()
            self.spreadPlague(data.plague, data)
            self.killInfected(data.plague)
            self.updateStats()
            data.cure.updateStats()
            self.collectGraphStats()
            self.updateBubbles(data)
            self.news = []
            if self.isWin():
                data.won = True
                data.mode = "end"
            elif self.isLose(data):
                data.won = False
                data.mode = "end"
    
    def drawMap(self, canvas, data):
        canvas.create_rectangle(0, 0, data.width, data.height, fill = "Maroon", width = 0)
        canvas.create_image(data.width//2, data.height//2, image=data.mapImage)
    
    def drawMapOverlay(self, canvas, data):
        canvas.create_text(data.width//2, data.dashboardY0-15, text = "Click on the gray dots to examine each country.", fill = "white", font = "Calibri 12")
        for country in self.countries:
            country.drawCircle(canvas, data)
            if country.hasBubble:
                country.drawBubble(canvas, data)

    def drawPoints(self, canvas, data):
        cellW = data.width//3
        cellH = data.height//6
        x = 0
        y = data.height-cellH
        pointsText = "Points: %d" % (data.player.numDNAPoints)
        canvas.create_rectangle(x, y, x+cellW, y+cellW, fill = data.lightColor, outline="white")
        canvas.create_text(x+cellW//2, y+cellH*(1/3), text=pointsText, fill="white", font = data.font)
        upgradeText = "Click to upgrade %s" % (str(data.plague))
        canvas.create_text(x+cellW//2, y+cellH*(2/3), text=upgradeText, fill="white", font = data.font)
        
    def drawStats(self, canvas, data):
        cellW = data.width//3
        cellH = data.height//6
        x = cellW
        y = data.height-cellH
        infectedText = "Infected:", int(self.numInfected)
        deadText = "Dead:", self.numDead
        canvas.create_rectangle(x, y, x+cellW, y+cellW, fill = data.lightColor, outline="white")
        canvas.create_text(x+cellW//2, y+cellH*(1/4), text=infectedText, fill="red", font = data.font)
        canvas.create_text(x+cellW//2, y+cellH*(2/4), text=deadText, fill="gray30", font = data.font)
        
        barLength = cellW*(4/5)
        barWidth = 5
        barY = y+cellH*(3/4)
        percentDead = self.numDead / self.population
        percentInfected = self.numInfected / self.population
        deadLength = percentDead * barLength
        infectedLength = percentInfected * barLength
        startX = x+cellW//2 - barLength//2
        canvas.create_line(startX, barY, startX + barLength, barY, fill = "blue", width = barWidth)
        canvas.create_line(startX, barY, startX + infectedLength, barY, fill = "red", width = barWidth)
        canvas.create_line(startX+infectedLength, barY, startX+infectedLength+deadLength, barY, fill = "gray30", width = barWidth)
    
    def drawDay(self, canvas, data):
        cellW = data.width//3
        cellH = data.height//6
        x = cellW*2
        y = data.height-cellH
        daysText = "Days since: " + str(self.numDays)
        canvas.create_rectangle(x, y, x+cellW, y+cellW, fill = data.lightColor, outline="white")
        canvas.create_text(x+cellW//2, y+cellH*(1/3), text=daysText, fill="white", font = data.font)
        cureText = ""
        if data.cure.completion == 0:
            cureText = "Cure progress: -"
        else: cureText = "Cure progress: %.2f%%" % (data.cure.completionPercentage*100)
        canvas.create_text(x+cellW//2, y+cellH*(2/3), text=cureText, fill="white", font = data.font)
        
    def drawDailyTransports(self, canvas, data):
        # print(self.dailyTransports)
        for tr in self.dailyTransports:
            tr.draw(canvas, data)
        
    def drawInterface(self, canvas, data):
        self.drawDay(canvas, data)
        self.drawPoints(canvas, data)
        # if data.countryClicked != None:
        #     data.countryClicked.drawStats(canvas, data)
        # else:
        self.drawStats(canvas, data)
    
    def getNewsText(self):
        res = ""
        for n in self.news:
            res += n+", "
        return res[:-2]
    
    def drawNews(self, canvas, data):
        newsW = 200
        newsH = 50
        newsText = "NEWS: " + self.getNewsText()
        if len(self.getNewsText())==0: newsText = "NEWS: Vaccinate your children."
        canvas.create_rectangle(0, 0, data.width, newsH, fill = data.lightColor, outline = "white")
        canvas.create_text(25, newsH//2, text = newsText, anchor = "w", fill = "white", font = data.font)
    
    def drawPlay(self, canvas, data):
        self.drawMap(canvas, data)
        self.drawMapOverlay(canvas, data)
        self.drawInterface(canvas, data)
        self.drawDailyTransports(canvas, data)
        self.drawNews(canvas, data)
    
    def getGraphValues(self, type):
        result = []
        if type == "numInfected":
            for i in range(self.numDays+1):
                result.append(self.graphStats[i][0])
        elif type == "numDead":
            for i in range(self.numDays+1):
                result.append(self.graphStats[i][1])
        return result
    
    def drawBackToEnd(self, canvas, data):
        cellW = data.width//3
        cellH = data.height//6
        x = 0
        y = data.height-cellH
        canvas.create_rectangle(x, y, x+cellW, y+cellW, fill = "gray30", outline = "white")
        upgradeText = "Click to go back to end screen."
        canvas.create_text(x+cellW//2, y+cellH//2, text=upgradeText, fill="white", font = data.font)
    
    def drawGraphStats(self, canvas, data):
        margin = 50
        boxWidth = 500
        x1 = data.width-margin
        y1 = data.height-margin
        x0 = x1-boxWidth
        y0 = margin
        boxHeight = y1-y0
        
        xIncr = boxWidth / self.numDays
        
        infectedGraphValues = self.getGraphValues("numInfected")
        deadGraphValues = self.getGraphValues("numDead")
        infectedMax = max(infectedGraphValues)
        deadMax = max(deadGraphValues)
        
        # print(infectedGraphValues, deadGraphValues)
        
        infectedPoints = [x0, y1]
        deadPoints = [x0, y1]
        for i in range(self.numDays+1):
            infectedPoints.append(x0+xIncr*(i))
            infectedPoints.append(y0+(boxHeight-(infectedGraphValues[i] / infectedMax) * boxHeight))
            deadPoints.append(x0+xIncr*(i))
            if deadMax != 0:
                deadPoints.append(y0+(boxHeight-(deadGraphValues[i] / infectedMax) * boxHeight))
        
        colorKeyCX = x0-2*margin
        colorKeyCY1 = y0+margin
        colorKeyCY2 = y0+(1.5)*margin
        keyRadius = 5
        
        infectedPoints += [x1, y1]
        deadPoints += [x1, y1]
            
        canvas.create_image(data.width//2, data.height//2, image=data.faded)
        canvas.create_rectangle(x0, y0, x1, y1, fill = "gray70", outline = "white")
        # print(infectedPoints)
        canvas.create_polygon(infectedPoints, fill = "red", width=0)
        canvas.create_polygon(deadPoints, fill = "gray30", width=0)
        canvas.create_rectangle(getBounds(colorKeyCX, colorKeyCY1, keyRadius), fill = "red", width=0)
        canvas.create_text(colorKeyCX+2*keyRadius, colorKeyCY1, text = "Infected", anchor = "w", font = data.font, fill = "white")
        canvas.create_rectangle(getBounds(colorKeyCX, colorKeyCY2, keyRadius), fill = "gray30", width=0)
        canvas.create_text(colorKeyCX+2*keyRadius, colorKeyCY2, text = "Dead", anchor = "w", font = data.font, fill = "white")
        
    def drawEndGraph(self, canvas, data):
        self.drawGraphStats(canvas, data)
        self.drawBackToEnd(canvas, data)
    
    def mpEndGraph(self, event, data):
        if data.plague.clickedBackButton(event, data):
            data.mode="end"

class Country(World):
    def __init__(self, name, population, populationDensity, development, temperature, weather, airOut, waterOut, neighbors, coords):
        self.name = name
        self.population = population
        self.populationDensity = populationDensity
        self.development = development # 1, 2, 3
        self.temperature = temperature # "hot", "mild", "cold"
        self.weather = weather # "dry", "normal", "humid"

        self.airOut = airOut
        self.waterOut = waterOut
        self.neighbors = neighbors

        self.numInfected = 0
        self.dailyInfected = {}
        self.numDead = 0
        self.state = "healthy" # "healthy", "infected", "dead"
        self.inQuarantine = False
        
        self.baseR = 10
        self.r = 0
        self.maxRadius = 75
        self.cx, self.cy = coords
        
        self.hasBubble = False
        self.bubbleCX = self.cx - 35
        self.bubbleCY = self.cy
        self.bubbleR = 6
    
    def __repr__(self):
        return self.name
        
    def infectZero(self, numDay):
        self.numInfected = 1
        self.dailyInfected[numDay] = 1
        # print("First occurence of the plague found in %s." % (str(self)))
        self.state = "infected"
        self.hasBubble = True
        
    def infect(self, numDay, data):
        self.numInfected = 1
        self.dailyInfected[numDay] = 1
        self.state = "infected"
        data.player.givePoints()
        self.hasBubble = True
    
    def spreadPlagueInCountry(self, plague, numDay): # other is type Plague
        infectivityFactor = self.getInfectivityFactor(plague)
        # print(infectivityFactor)
        infectedToday = int(self.numInfected*infectivityFactor)+1
        if infectedToday < self.population - self.numDead:
            self.dailyInfected[numDay] = infectedToday - self.numInfected # aka infectedToday - infectedYesterday
            self.numInfected = infectedToday
        else:
            self.dailyInfected[numDay] = (self.population-self.numDead) - self.numInfected
            self.numInfected = self.population - self.numDead
        # print(self.dailyInfected)
    
    def getInfectivityFactor(self, plague):
        self.infectivityPoints = plague.infectivityBasePoints
        for trait in plague.regionInfectivity:
            if trait == self.populationDensity or trait == self.development or trait == self.temperature or trait == self.weather:
                self.infectivityPoints += plague.regionInfectivity[trait]
                # print(plague.regionInfectivity)
        infectivityFactor = 1 + self.infectivityPoints / 100
        # print("infectivityFactor:", infectivityFactor)
        return infectivityFactor
        # return self.infectivityPoints # prob need more math later
    
    def getSpreadProbability(self, plague, transportType):
        spreadPoints = plague.spreadBasePoints[transportType]
        for type in plague.spreadInfectivity:
            if type == transportType:
                spreadPoints += plague.spreadInfectivity[type]
        spreadProbability = spreadPoints / 100
        # print(spreadProbability)
        # print(transportType, spreadProbability)
        return spreadProbability # def need more math later
    
    def drawCircle(self, canvas, data):
        canvas.create_oval(self.cx-self.r, self.cy-self.r, self.cx+self.r, self.cy+self.r, width=3, fill="", outline = "red")
        canvas.create_oval(self.cx-self.baseR, self.cy-self.baseR, self.cx+self.baseR, self.cy+self.baseR, width=0, fill="gray30")
        
    ##
    
    def mpCountry(self, event, data):
        if data.plague.clickedBackButton(event, data):
            data.mode = "play"
        
    def drawCountryImage(self, canvas, data):
        canvas.create_image(data.width//2, data.height//2, image=data.countryImages[data.countryClicked.name])
        
    def drawCountryStats(self, canvas, data):
        characteristicNames = ["Infected", "Dead", "State", "Population", "Density", "Development", "Temperature", "Weather"] # "Flights out", "Boats out", "Land neighbors"
        characteristics = [self.numInfected, self.numDead, self.state, self.population, self.populationDensity, self.development, self.temperature, self.weather] # self.airOut, self.waterOut, self.neighbors
        
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
            canvas.create_rectangle(x0, y0+i*cellH, x1, y0+(i+1)*cellH, fill = data.lightColor, outline = "white")
            canvas.create_text(x0+10, y0+(i+0.5)*cellH, text = characteristicNames[i], fill = "white", anchor = "w", font = data.font)
            canvas.create_text(cx, y0+(i+0.5)*cellH, text = characteristics[i], fill = "white", anchor = "w", font = data.font)
            
    def drawCountry(self, canvas, data):
        canvas.create_image(data.width//2, data.height//2, image=data.faded)
        self.drawCountryImage(canvas, data)
        self.drawCountryStats(canvas, data)
        data.plague.drawBack(canvas, data)
    
    def drawBubble(self, canvas, data):
        canvas.create_oval(getBounds(self.bubbleCX, self.bubbleCY, self.bubbleR), fill = "red", width=0)
        
    def clickedBubble(self, event, data):
        if distance(event.x, event.y, self.bubbleCX, self.bubbleCY) <= self.bubbleR:
            return True