# EECS 12 Fall 2012
# Homework #6
# Golf
# Author: Thanh Vu



from graphics import *
from time import sleep
from random import random
import math 

# draws a red arrow and return it
def setNewDirection(bc, pm, win):
    
    a = Line(pm, bc)
    a.setOutline("Red")
    a.setArrow("last")
    a.setWidth(2)
    a.draw(win)
    return a

# checks if the rectangle has been hit, returns
# 0,1,2, or 3 depending on whether it has been
# hit, and if so, what side it has been hit from

# pb: a circle (the ball)
# rec: a rectangle (obstacle)
# dx: displacement of the ball in the x direction
# dy: displacement of the ball in the y direction

def checkRecHit(pb, rec, dx, dy):
    #x,y coordinates of golfball's current center position
    x_cur= Point.getX(pb.getCenter())
    y_cur= Point.getY(pb.getCenter())
    # radidus of the golfball
    rad= pb.getRadius()
    
    x_left= Point.getX(rec.getP1()) #rectangle's left x 
    x_right= Point.getX(rec.getP2())#rectangle's right x
    y_up= Point.getY(rec.getP2())# rectangle's top y

    #check with side of rectangle has been hit

    d_top=dy+ y_cur-rad- y_up
    d_left= dx+ x_cur + rad - x_left
    d_right= dx+ x_cur - rad- x_right

    
    if d_top < 0 and d_right < 0 and d_left > 0 :
        #ball hit objects
        if y_cur >= y_up and (x_left <= x_cur <= x_right or -d_top <= min(d_left,-d_right)): # hit top
            return 1
        elif x_cur <= x_left: # hit left
            return 2
        else:
            return 3# hit right
    else:
        return 0 # ball hit nothing and continue to travel
        

def main():
    
    win = GraphWin("Golf", 1000, 700)
    win.setCoords(0, 0, 100, 70)
    win.configure(background="light blue")
    
    # draw the background
    gameWindow = Image(Point(50, 35), "golf_course.gif")
    gameWindow.draw(win)

    # draw the text message at the top
    msg1 = Text(Point(50, 65.5), "")
    msg1.setTextColor("DarkBlue")
    msg1.setStyle("bold")
    msg1.setSize(18)
    msg1.draw(win)

    # draw the text message for the shots
    shotsTxt = Text(Point(15, 4.5), "Shots:")
    shotsTxt.setTextColor("Purple")
    shotsTxt.setStyle("bold")
    shotsTxt.setSize(20)
    shotsTxt.draw(win)

    #draw the sun
    sun=Circle( Point(55,50), 4)
    sun.setOutline("orange")
    sun.setFill("yellow")
    sun.draw(win)
    
    # draw the balls for the number of shots left
    shots = 3
    shots_img = []
    for i in range(shots):
        gb_img = Image(Point(23 + 5*i, 4.5), "golf_ball.gif")
        gb_img.draw(win)
        shots_img.append(gb_img)

    # draw the Hit button
    button = Rectangle(Point(46, 2), Point(54, 7))
    button.setFill("Pink")
    button.draw(win)
    buttonTxt = Text(Point(50, 4.5), "Hit")
    buttonTxt.setStyle("bold")
    buttonTxt.setSize(20)
    buttonTxt.draw(win)

    # draw the text message for the wind
    windTxt = Text(Point(82.5, 58), "Wind")
    windTxt.setFill("Black")
    windTxt.setStyle("bold")
    windTxt.setSize(20)
    windTxt.draw(win)

    # draw the text message in the center
    msg2 = Text(Point(50, 50), "")
    msg2.setTextColor("Red")
    msg2.setStyle("bold")
    msg2.setSize(36)
    msg2.draw(win)

    # draw the rectangles at the bottom (the ground)
    rec_num=10
    P1=[Point(9.9,8.35),Point(15,8.35),Point(23,8.35),Point(24.5,8.35),Point(35,8.35),Point(40,8.35),Point(50,8.35),Point(60,8.35),Point(63,8.35),Point(70,8.35)]
    P2=[Point(15,12.5),Point(23,13.75),Point(24.5,12.25),Point(35,13.75),Point(40,15),Point(50,16.5),Point(60,18.5),Point(63,16.5),Point(70,14),Point(89.9,12.5)]
    # draw the rectangles using the list P1, P2 and append them to the list called "boxlist"
    boxlist=[]
    for i in range(len(P1)):
        objects= Rectangle(P1[i], P2[i])
        objects.setOutline("Brown")
        objects.setFill("Brown")
        objects.draw(win)
        boxlist.append(objects)
   

    # draw the tee
    tee = Rectangle(Point(82.4,12.5),Point(82.6,13))
    tee.setFill("White")
    tee.draw(win)

    # draw the hole
    hole = Rectangle(Point(23,12.25),Point(24.5,13.75))
    hole.setFill("Black")
    hole.draw(win)

    bc = Point(82.5, 13.4) # ball's initial center point
    rad = 0.4 # ball's radius
    delay = 0.02 # pause in seconds between each update of the ball's motion
    ratio1 = 5 # ratio used for the initial velocity set by the user
    ratio2 = 0.04 # ratio used for the velocity change due to the wind
    ratio3 = 0.1 # ratio used for the velocity change due to gravity

    # check if there are any shots left (initially, shots = 3)
    while shots > 0:
        msg1.setText("Click anywhere below the ball to set\nthe direction and the initial velocity.")

        # undraw the ball and the wind if it is not the first shot
        if shots < 3:
            golfball.undraw()
            wind.undraw()

        # draw the ball
        golfball = Circle(bc, rad)
        golfball.setFill("Red")
        golfball.setOutline("yellow")
        golfball.draw(win)
        gbdrawn = True # flag to check if the golf ball has been drawn

        # randomly set the wind strength and direction and display it
        wind_force = 15*(random()-0.5)
        wind = Line(Point(bc.x-(wind_force/2),55), Point(bc.x+(wind_force/2),55))
        wind.setOutline("Black")
        wind.setArrow("last")
        wind.setWidth(20)
        wind.draw(win)

        #strength of wind shown
        wind_strength= int(-(wind_force))
        wind_num= Text(Point(82.5,52), wind_strength )
        wind_num.setSize(14)
        wind_num.setTextColor("Red")
        wind_num.setStyle("bold")
        wind_num.draw(win)

        wind_unit= Text(Point(86,52),"m/s")
        wind_unit.setSize(14)
        wind_unit.setTextColor("Red")
        wind_unit.setStyle("bold")
        wind_unit.draw(win)
        

        m1=Point(0,14) # initialization of m1 for the while loop
        # check if the click is below the ball
        while m1.y > 13.5:
            m1 = win.getMouse() # click to set the direction
          
        d = setNewDirection(bc, m1, win) # draw the arrow
        
        msg1.setText("Click on the Hit button to play or click anywhere below\nthe ball to change the direction and the initial velocity.")
        m2 = win.getMouse() # click to redraw the arrow for the direction or click on the Hit button
        # check if the click is outside the Hit button
        while not (46 < m2.x < 54 and 2 < m2.y < 7):
            # check if the click is below the ball
            if m2.y <= 13.5:
                # redraw the arrow for the direction
                d.undraw()
                d = setNewDirection(bc, m2, win)
                m1=m2.clone()
                vx = ratio1 * (bc.x - m1.x)
                vy = ratio1 * (bc.y - m1.y)
            # calculate the velocity of the swing
            velocity_num= int(math.sqrt((vx*vx)+(vy*vy)))
            velocity_text= Text(Point (83.5, 15), (str(velocity_num) + ' ' + 'm/s'))
            velocity_text.setTextColor("red")
            velocity_text.setSize(14)
            velocity_text.draw(win)
            m2 = win.getMouse() # click to redraw the arrow for the direction or click on the Hit button
            velocity_text.undraw()
        d.undraw()
        msg1.setText("Nice Shot! Waiting for the ball to come to a stop...")
        
        # compute the initial velocities
        vx = ratio1 * (bc.x - m1.x)
        vy = ratio1 * (bc.y - m1.y)

        # compute the initial displacements
        dx = delay * vx
        dy = delay * vy

        # set the current position to the initial position of the ball
        x_cur = bc.x
        y_cur = bc.y

        # loop to update the ball's position
        for t in range(1000):
            if x_cur + rad + dx > 90: # hits the right side of the frame
                if gbdrawn:
                    golfball.undraw()
                    gbdrawn = False
            elif x_cur - rad + dx < 10: # hits the left side of the frame
                if gbdrawn:
                    golfball.undraw()
                    gbdrawn = False
            elif y_cur + rad + dy > 61.65: # hits the top of the frame
                if gbdrawn:
                    golfball.undraw()
                    gbdrawn = False
            else: # is in the frame
                if not gbdrawn:
                    golfball.draw(win)
                    gbdrawn = True

            # Check if the ball has come to a stop:
            if abs(vx) < 0.001 and abs(vy) < 0.001:
                if 23<x_cur<24.5 and 12.25<y_cur<13.75:
                    msg1.setText("Click anywhere to quit")
                    msg2.setText("CONGRATULATIONS!\n YOU WIN! YAY")
                    shots=0
                break
            
            
            hit=0
            for i in range(len(boxlist)):
                rec=boxlist[i]
                hit= checkRecHit(golfball,rec, dx, dy)
                if hit != 0:
                    
                    break
            
            # Check if any of the rectangles at the bottom have been hit and assign 0,1,2, or 3 to "hit" depending on which side of one of those rectangles has been hit:
            # Check the value of "hit" and update the values of "vx" and "vy" (velocities in the x and y direction) accordingly:
            if hit == 1 or (y_cur - rad) < 12.5:
                vx= vx*0.4
                vy= abs(vy*0.4)
            elif hit==2:
                vx= - abs((vx)* 0.4)
                vy= 0.4* vy
            elif hit==3:
                vx= abs(vx*0.4)
                vy= vy*0.4
            elif hit==0:
                vx= vx+ wind_force * ratio2
                vy= vy-(9.8)*ratio3

            dx = delay * vx # compute the displacement in the x direction
            dy = delay * vy # compute the displacement in the y direction

            x_cur = x_cur + dx # update the current x position
            y_cur = y_cur + dy # update the current y position

            golfball.move(dx, dy) # move the ball

            sleep(delay) # add some delay

       #Check if the user has won the game update the messages, decrement "shots", and undraw a ball from "shots_img":
            
        if shots!=0:
            shots=shots-1
            shots_img[shots].undraw()
            if shots >1:
                if x_cur>24.5 and shots>0:
                    msg2.setText(" OH! So CLOSE! more luck with a \n stronger swing next time.")
                elif x_cur<23:
                    msg2.setText(" OH! Swing it too hard maybe ! ")
                msg1.setText("You have"+ ' '+ str(shots)+' '+ "more shots left ... CLick anywhere to conitinue.")
                wind.undraw()
                wind_num.undraw()
                wind_unit.undraw()
                
            elif shots == 1:
                msg1.setText("You have 1 more shot left...Click anywhere to continue.")
                wind.undraw()
                wind_num.undraw()
                wind_unit.undraw()
            else:
                msg1.setText("Click anywhere to quit")
                msg2.setText("GAME OVER")
                
        

        win.getMouse()
        msg2.setText(" ")
    win.close()

main()
