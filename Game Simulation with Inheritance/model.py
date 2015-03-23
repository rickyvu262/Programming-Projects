#Submitter: thanhhv (Thanh, Vu)
# I certify that I wrote all the code in this programming assignment
# by myself

import controller, sys
#import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Ice_Freezer
from test.test_class import AllTests


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0;
all_objects = set();
type_select =''


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, all_objects 
    running = False
    cycle_count = 0
    all_objects = set()


#start running the simulation
def start ():
    global running
    running = True
    

#stop running the simulation (freezing it)
def stop ():
    global running
    running = False
    
    


#tep just one update in the simulation
def step ():
    # stop after every cycle, 
    #if running , stop after one cycle
    #if stop, starts for one cycle and stop
    global running, cycle_count, all_objects
    if running:
        stop()
    else:
        cycle_count += 1
        for each_ball in all_objects:
            each_ball.update()
        stop()
        
    


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global type_select
    type_select = kind  
    return type_select

#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global type_select,all_objects
    
    if type_select == 'Ball':
        all_objects.add(eval(type_select)(x,y))
    
    elif type_select =='Floater':
        all_objects.add(eval(type_select)(x,y))

    elif type_select =='Black_Hole':
        all_objects.add(eval(type_select)(x,y))
        
    elif type_select =='Pulsator':
        all_objects.add(eval(type_select)(x,y))
        
    elif type_select =='Hunter':
        all_objects.add(eval(type_select)(x,y))
        
    elif type_select =='Special':
        all_objects.add(Ice_Freezer(x,y))
    
    elif type_select =='Remove':
        for i in find(lambda object_sel: object_sel.contains((x,y))): #inherit from the simulton.contains(xy) to check whether a click on an simulton. 
            remove(i) # remove simulton from the set of that object
            
                           
            
#add simulton s to the simulation
def add(s):
    return all_objects.add(s) # add item to a set
    

# remove simulton s from the simulation    
def remove(s):
    return all_objects.remove(s) # remove item from a set
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global all_objects
    
    return {each for each in all_objects if p(each) }


#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for each_object in set(all_objects):
            each_object.update() 


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for each in controller.the_canvas.find_all():
        controller.the_canvas.delete(each)
        
    for each_object in all_objects:
        each_object.display(controller.the_canvas)
        
    controller.the_progress.config(text=str(len(all_objects))+" balls/"+str(cycle_count)+" cycles")