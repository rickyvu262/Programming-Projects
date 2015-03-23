#Submitter: thanhhv (Thanh, Vu)
# I certify that I wrote all the code in this programming assignment
# by myself

# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model

class Black_Hole(Simulton):
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,1)
        self.color = 'black'
    def update(self):
        objects_eaten = model.find(lambda x: self.contains(x)) # find(p) where p is predicate 
        for each_object in objects_eaten:
            if each_object in model.all_objects:
                model.remove(each_object)
    
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius,self._y-self.radius,self._x+self.radius,self._y+self.radius,fill= self.color)
    
    def contains(self,object_):
        distance_val = self.distance((object_._x, object_._y))
        if distance_val < self.radius and isinstance(object_,Prey): #return true if object(floater or balls) is an instance of Prey
            return True
        
        
        