from tkinter import *

class Transport(object):
    def __init__(self, fr, to, transportState):
        self.fr = fr
        self.to = to
        self.fromX = fr.cx
        self.fromY = fr.cy
        self.toX = to.cx
        self.toY = to.cy
        self.travellingX = self.fromX
        self.travellingY = self.fromY
        self.dy = (self.toY-self.fromY)/20
        self.dx = (self.toX-self.fromX)/20
        self.transportState = transportState
    
    def draw(self, canvas, data):
        if self.transportState == "infected": clr = "red"
        else: clr = "gray20"
        canvas.create_line(self.fromX, self.fromY, self.travellingX, self.travellingY, width = 2, fill = clr)
        canvas.create_image(self.travellingX, self.travellingY, image=self.trImage)
    
    def __repr__(self):
        s = "A(n) %s %s is going from %s to %s." % (self.transportState, type(self).__name__, str(self.fr), str(self.to))
        return s
    
    def move(self):
        self.travellingX += self.dx
        self.travellingY += self.dy
        
class Plane(Transport):
    def __init__(self, fr, to, transportState):
        super().__init__(fr, to, transportState)
        self.trImage = PhotoImage(file="plane.png")

class Boat(Transport):
    def __init__(self, fr, to, transportState):
        super().__init__(fr, to, transportState)
        self.trImage = PhotoImage(file="boat.png")
        
class Bird(Transport):
    def __init__(self, fr, to, transportState):
        super().__init__(fr, to, transportState)
        self.trImage = PhotoImage(file="bird.png")