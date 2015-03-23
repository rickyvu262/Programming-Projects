#Submitter: thanhhv (Thanh, Vu)
# I certify that I wrote all the code in this programming assignment
# by myself

'''
Created on Dec 13, 2014

@author: Thanh
'''
 # Special class is called Ice_Killer. They shot ball every 80 cycles towards Prey objects and kill them (using Hunter as ice_bullets) plus his speed increases after 30 cycles
from prey import Prey
import model
from hunter import Hunter
from ball import Ball
class Ice_Freezer(Hunter):
  
    def __init__(self,x,y):
        Hunter.__init__(self, x, y)
        self.width = 8
        self.length = 10
        self._speed = 1
        self._counter = 0
        
    def display(self,canvas):
        canvas.create_rectangle(self._x-self.length,self._y-self.width,self._x+self.length,self._y+self.width,fill='light blue')
        
    def update(self):
        
        Hunter.update(self)
        self.speed_gain()
        self.bullet()
        self.move()
        
        
    def speed_gain(self):
        self._counter += 1
        if self._counter == 30:
            self._speed += 2
            self._counter = 0
    
    def bullet(self):
        self._counter += 1
        if self._counter == 80:
            x = Hunter(self._x,self._y)
            x.radius = 3
            x.color = 'white'
            model.add(x)
            self._counter = 0
        