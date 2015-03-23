#Submitter: thanhhv (Thanh, Vu)
# I certify that I wrote all the code in this programming assignment
# by myself

# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey
 # Ball is the subclass from Prey (should inherit certain method from Prey)

class Ball(Prey):
    
    radius = 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x, y,10,1,0,5)
        self.randomize_angle()
        self._color ='blue'
        
    def update(self):
        self.move()
        self.wall_bounce()
        
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.radius      , self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill=self._color)