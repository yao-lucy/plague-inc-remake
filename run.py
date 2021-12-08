from tkinter import *
from World import *
from Plague import *
from Player import *
from draw import *
from Cure import *

# https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part2.html
# run function code from time-based animation lecture

##

def init(data):
    data.mode = "start" # start, choose, play, buy(3), end, graphs
    
    data.world = None
    data.plague = None
    data.player = None
    data.cure = Cure()
    data.timeCount = 0  
    data.inGameDay = 4 # 2 seconds
    data.mapImage = PhotoImage(file="world.png")
    data.worldInfected = PhotoImage(file="world.png")
    data.faded = PhotoImage(file="faded.png")
    data.start = PhotoImage(file="start.png")
    data.startButtonsH = 50
    data.startButtonsW = 200
    data.countryClicked = None
    data.won = None
    data.countryImages = {
        "North America": PhotoImage(file="NA.png"),
        "South America": PhotoImage(file="SA.png"),
        "Europe": PhotoImage(file="Europe.png"),
        "Africa": PhotoImage(file="Africa.png"),
        "Asia": PhotoImage(file="Asia.png"),
        "Australia": PhotoImage(file="Aus.png")
        }
    data.font = "Calibri 16"
    data.lightColor = "SkyBlue3" # "IndianRed1"
    data.midColor = "gray50" # "IndianRed2"
    data.darkColor = "gray30" # "IndianRed3"
    
    data.updateRadius = 25
    data.tabHeight = 25
    data.tabWidth = data.width//4
    data.tabY0 = 15
    data.tabY1 = data.tabY0 + data.tabHeight
    data.dashboardHeight = data.height//6
    data.dashboardY0 = data.height-data.dashboardHeight
    data.bubbles = []

def startGame(data):
    data.world = World()
    data.plague = Plague()
    data.player = Player()
    data.mode = "play"

def mpStart(event, data):
    if clickPlay(event, data):
        startGame(data)
    elif clickInstr(event, data):
        data.mode = "instructions"

def mpEnd(event, data):
    if clickPlay(event, data): # shady code would not recommend
        init(data)
    elif clickInstr(event, data):
        data.mode = "graph"

def mousePressed(event, data):
    if data.mode == "start": mpStart(event, data)
    elif data.mode == "upgrade": data.plague.mpUpgrade(event, data)
    elif data.mode == "play": data.world.mpPlay(event, data)
    elif data.mode == "country": data.countryClicked.mpCountry(event, data)
    elif data.mode == "graph": data.world.mpEndGraph(event, data)
    elif data.mode == "transmission" or data.mode == "symptom" or data.mode == "ability":
        data.plague.mpUpgrades(event, data)
    elif data.mode == "instructions": mpInstr(event, data)
    elif data.mode == "end": mpEnd(event, data)

def keyPressed(event, data):
    pass # never used

def timerFired(data):
    if data.mode == "play": data.world.tfPlay(data) #  or data.mode == "country"

def redrawAll(canvas, data):
    if data.mode == "start": drawStart(canvas, data)
    elif data.mode == "play": data.world.drawPlay(canvas, data)
    elif data.mode == "instructions": drawInstr(canvas, data)
    elif data.mode == "end": drawEnd(canvas, data)
    elif data.mode == "country": data.countryClicked.drawCountry(canvas, data)
    elif data.mode == "upgrade": data.plague.drawUpgrade(canvas, data)
    elif data.mode == "transmission" or data.mode == "symptom" or data.mode == "ability":
        data.plague.drawUpgrades(canvas, data)
    elif data.mode == "graph": data.world.drawEndGraph(canvas, data)

##

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()
        
    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(900, 600)