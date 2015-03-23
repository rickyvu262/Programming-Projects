#Submitter: thanhhv (Thanh, Vu)
# I certify that I wrote all the code in this programming assignment
# by myself

# A Hunter is both Mobile_Simulton and Pulsator; it updates
#   like a Pulsator, but also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2
import model


class Hunter(Pulsator,Mobile_Simulton):
    distance_constant = 200
    def __init__(self,x,y):
        Pulsator.__init__(self, x, y)
        self.randomize_angle() # move random angle
        self._speed = 5 # speed of 5 pix/second
        self.radius = 10
        self.color = 'brown'
        
    def update(self):
        Pulsator.update(self)    #calling update on Pulsator class in order to decrease or increase the size of hunter every 30 seconds
        self.wall_bounce()
        all_Prey_obj = [x for x in model.find(lambda x: isinstance(x, Prey))]
        #if any of these objects is within 200 (distance_constant)
#         for each_object in all_Prey_obj:
#             if self.within_target(each_object) == True:
                
        # if there are prey objects left, compute the closest prey and angle 
        if len(all_Prey_obj) > 0:   
            target_prey = self.closet_prey(all_Prey_obj)
            self._angle = atan2(target_prey._y - self._y, target_prey._x - self._x)   
             
        # tell Hunter to chase that closest Prey
        self.move()
        
        # remove that Prey from simulation after being eaten
        self.delete_eaten() 
        
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius,self._y-self.radius,self._x+self.radius,self._y+self.radius,fill=self.color)
        
    
    
    def within_target(self,object_each): # not needed to check whether if object within 200 since ultimate goal is to find the closest prey
        self.distance_between = self.distance((object_each._x,object_each._y)) 
        return self.distance_between < self.distance_constant   # return True if in target, False outside target
        
    def closet_prey(self,objects_target): # find the closest prey from all prey objects and return that prey
        closest_distance = 200
        closet_prey = objects_target[0]
        for each in objects_target:
            if self.distance((each._x,each._y)) < closest_distance:
                closest_distance = self.distance((each._x,each._y))
                closet_prey = each
        return closet_prey
                
    def delete_eaten(self):
        for i in model.find(lambda x: isinstance(x, Prey)):
            if self.contains(i):
                model.remove(i)
        
            
            
