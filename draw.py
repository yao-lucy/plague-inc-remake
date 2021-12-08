from tkinter import *
from World import *
from Plague import *
from Player import *

def getBounds(cx, cy, r):
    return cx-r, cy-r, cx+r, cy+r

def getPlayBounds(data):
    margin = 5
    return data.width//2 - data.startButtonsW, data.height//2 - data.startButtonsH*2-margin, data.width//2 + data.startButtonsW, data.height//2 -margin

def getInstrBounds(data):
    margin = 5
    return data.width//2 - data.startButtonsW//2, data.height//2 +margin, data.width//2 + data.startButtonsW//2, data.height//2 + data.startButtonsH + margin

def drawStart(canvas, data):
    canvas.create_image(data.width//2, data.height//2, image=data.start)
    a0, b0, a1, b1 = getPlayBounds(data)
    canvas.create_rectangle(getPlayBounds(data), fill = "IndianRed4",outline = "white")
    canvas.create_text((a0+a1)//2, (b0+b1)//2, fill = "white", text = "Play", font = "Calibri 30")
    c0, d0, c1, d1 = getInstrBounds(data)
    canvas.create_rectangle(getInstrBounds(data), fill = "IndianRed4", outline = "white")
    canvas.create_text((c0+c1)//2, (d0+d1)//2, fill = "white", text = "Instructions")

def clickPlay(event, data):
    a0, b0, a1, b1 = getPlayBounds(data)
    return a0 < event.x < a1 and b0 < event.y < b1

def clickInstr(event, data):
    a0, b0, a1, b1 = getInstrBounds(data)
    return a0 < event.x < a1 and b0 < event.y < b1

def drawEnd(canvas, data):
    canvas.create_image(data.width//2, data.height//2, image=data.faded)
    if data.won:
        message = "Congrats! Your plague destroyed the whole world."
    else: message = "You lose! Your plague was bad."
    a0, b0, a1, b1 = getPlayBounds(data)
    canvas.create_text(data.width//2, b0-20, text=message, fill = "white", font = "Calibri 12")
    canvas.create_rectangle(getPlayBounds(data), fill = data.lightColor, outline = "white")
    canvas.create_text((a0+a1)//2, (b0+b1)//2, fill = "white", text = "Play again", font = "Calibri 20")
    c0, d0, c1, d1 = getInstrBounds(data)
    canvas.create_rectangle(getInstrBounds(data), fill = data.lightColor, outline = "white")
    canvas.create_text((c0+c1)//2, (d0+d1)//2, fill = "white", text = "See game statistics", font = data.font)

# def drawWin(canvas, data):
#     data.world.drawGraphStats(canvas, data)
#     message = "Congrats! You have destroyed the whole world.\nClick anywhere to play again."
#     canvas.create_text(data.width//2, data.height//2, text=message)
# 
# def drawLose(canvas, data):
#     data.world.drawGraphStats(canvas, data)
#     message = "You lose! A cure was found; humanity is just too good.\nClick anywhere to play again."
#     canvas.create_text(data.width//2, data.height//2, text=message)

def drawBackToStart(canvas, data):
    cellW = data.width//3
    cellH = data.height//6
    x = 0
    y = data.height-cellH
    canvas.create_rectangle(x, y, x+cellW, y+cellW, fill = "gray30", outline = "white")
    instrText = "Click to go back to start."
    canvas.create_text(x+cellW//2, y+cellH//2, text=instrText, fill="white", font = data.font)

def drawInstr(canvas, data):
    canvas.create_image(data.width//2, data.height//2, image=data.start)
    drawBackToStart(canvas, data)
    instructions = '''Welcome to Plague!
    
        The goal of the game is to destroy
        the world with a plague that you develop!
        The game uses an epidemic model with a
        complex and realistic set of variables to
        simulate the spread and severity of the
        plague including weather and transportation
        between countries.
        
        Click on countries to
        explore their statistics. Upgrade your plague
        with transmissions, symptoms, and abilities
        to increase your plague's infectivity,
        severity, and lethality. Beware of the evil
        cure company who will try and stop your
        plague.
        
        Happy playing!'''
    canvas.create_text(data.width//2, data.height//2, text=instructions, fill = "white", justify = "center", font = "Calibri 14")

def clickedBackToStartButton(event, data):
    cellW = data.width//3
    cellH = data.height//6
    x = 0
    y = data.height-cellH
    return x < event.x < x + cellW and y < event.y < y + cellH

def mpInstr(event, data):
    if clickedBackToStartButton(event, data):
        data.mode = "start"