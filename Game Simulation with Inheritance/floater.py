#Submitter: thanhhv (Thanh, Vu)
# I certify that I wrote all the code in this programming assignment
# by myself

# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random


class Floater(Prey):
    radius = 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,0,5)
        self.randomize_angle()
        self._color ='red'
        
    def update(self):
        #define random_val between 1 to 100 to represent percentage (1% to 100%)
        random_value = random.randint(1,100)
        if random_value < 30: # speed and angle change apply
            self._angle += random.uniform (-0.5,0.5)
            if 3 <= self._speed <= 7: # speed only varies between 3 to 7 
                self._speed += random.uniform(-0.5,0.5)
        self.move()     
        self.wall_bounce()
        
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill=self._color)
        
    