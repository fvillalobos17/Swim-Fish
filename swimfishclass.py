#Felicia Villalobos 
#Homework 9
#This code creates and moves an inputed number of fish with classes 
from graphics import *
from random import randint

class Fish:
    ' this is the class that creates the fish, its speed, orients it based on swim direction '
    def __init__(self, win, nfish):
        self.color = color_rgb(randint(0,250),randint(0,250),randint(0,250))
        self.centerp = Point(randint(-100,100), randint(-100,100))
        self.x,self.y = self.centerp.getX(), self.centerp.getY()
        self.P1 = Point(self.x-10, self.y-5)
        self.P2 = Point(self.x+10, self.y+5)
        self.body = Oval(self.P1,self.P2)
        self.centb = self.body.getCenter()
        self.centbX = self.centb.getX()
        self.centbY = self.centb.getY()

        #speed 
        r = 0
        while r == 0:
            r = randint(-1,1)
        #return r -->jk don't do this 
        self.speed = r

        if self.speed < 0: 
            self.tail = Polygon(Point(self.x,self.y),Point(self.x+15,self.y+7), Point(self.x+15,self.y-7))
            self.eye = Circle(Point(self.x-4,self.y+1),1)

        elif self.speed > 0:
            self.tail = Polygon(Point(self.x,self.y),Point(self.x-15,self.y+7),Point(self.x-15,self.y-7))
            self.eye = Circle(Point(self.x+4,self.y+1),1)
            

    def drawfish(self,win):
        self.tail.setFill(self.color)
        self.tail.draw(win)
        self.body.setFill(self.color)
        self.body.draw(win)
        self.eye.setFill('white')
        self.eye.draw(win)
       

    def swim(self):
        self.body.move(self.speed, 0)
        self.tail.move(self.speed, 0)
        self.eye.move(self.speed, 0)


    def wrap(self,win):
        cent = self.body.getCenter()
        self.cx,self.cy = cent.getX(), cent.getY()
        if self.cx > 105:
            self.body.move(-2*103, 0)
            self.tail.move(-2*103, 0)
            self.eye.move(-2*103, 0)

        elif self.cx < -105:
            self.body.move(2*103, 0)
            self.tail.move(2*103, 0)
            self.eye.move(2*103, 0)

class Bubble:
    'this class controls the bubbles, which are supposed to be fish food'
    def __init__(self,win, nbubble):
        self.center = Point(randint(-100,100), randint(-100,100))
        self.x,self.y = self.center.getX(), self.center.getY()
        self.bubble = Circle(Point(self.x, self.y),2)

        r = 0
        while r == 0:
            r = randint(-1,1)
        self.speed = r

    def drawbubble(self,win):
        self.bubble.setFill('orange')
        self.bubble.draw(win)

    def move(self,win):
        self.bubble.move(self.speed, 0)

    def wrap(self,win):
        cent = self.bubble.getCenter()
        self.cx,self.cy = cent.getX(), cent.getY()
        
        if self.cx > 100:
            self.bubble.move(-2*103, 0)
    
        elif self.cx < -100:
            self.bubble.move(2*103, 0)
                   
        
def main():
    'main function that contains the animation loop and objects fish and bubbles'

    win = GraphWin('homework 9', 500,500, autoflush = False)
    win.setBackground('cornflower blue')
    w = 100
    win.setCoords(-w,-w,w,w)

    nfish = eval(input('How many fish?')) 
    print('#fish=', nfish)
    print('click mouse to start...')
    print('Click mouse to quit...')

    nbubble = 10
    Lbubble = []

    for i in range(nbubble):
        onebubble = Bubble(win,nbubble)
        onebubble.drawbubble(win)
        Lbubble.append(onebubble)

##    win.getMouse()
##    while True:
##        p = win.checkMouse()
##        if p != None:
##            break
##        else:
##             for i in range(nbubble):
##                circle = Lbubble[i]
##                circle.move(w)
##                circle.wrap(w)
##                

    Lfish = []

    for i in range(nfish):
        onefish = Fish(win,nfish)
        onefish.drawfish(win)
        Lfish.append(onefish)

    win.getMouse()

    while True:
        p = win.checkMouse()
        if p != None:
            break
        else:
            for i in range(nfish):
                oval = Lfish[i]
                oval.swim()
                oval.wrap(w)
            for i in range(nbubble):
                circle = Lbubble[i]
                circle.move(w)
                circle.wrap(w)
                
                

        update(30)

    win.close()

main()
                
        
        

    
    
    
        
