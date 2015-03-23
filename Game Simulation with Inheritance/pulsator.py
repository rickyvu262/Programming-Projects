#Submitter: thanhhv (Thanh, Vu)
# I certify that I wrote all the code in this programming assignment
# by myself

# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
import model

class Pulsator(Black_Hole):
    counter_constant = 30
    
    def __init__(self,x,y):
        Black_Hole.__init__(self, x, y)
        self.pul_counter = 0 
        
        
    def update(self):
        self.pul_counter += 1
        if self.radius < 0: # can't shrink anymore, remove pulsator
            model.remove(self)
        elif self.pul_counter == 30: # every 30 seconds, shrink if not eat
            self.radius -= 1 
            self.pul_counter = 0  
            
        elif self.pul_counter < 30: # during 30 seconds, if find Prey object (balls, floaters), remove that objects and increase the radius of pulsator object.
            objects_eaten = model.find(lambda x: self.contains(x))
            for each_object in objects_eaten:
                if each_object in model.all_objects:
                    model.remove(each_object)
                    self.radius += 1
                    
                 
            