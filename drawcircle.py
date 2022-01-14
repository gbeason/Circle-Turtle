import sys
import math
import turtle
import getopt

#draw circle using turtle
def drawCircle(x,y,r):
    #move to the start of the circle
    turtle.up() #cease drawing
    turtle.setpos(x + r, y)
    turtle.down() #resume drawing

    #begin drawing the circle
    for i in range(0, 365, 5):
        a = math.radians(i) #convert from degrees to radians
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))

#define parameters for the circle
def getArgs():
    defaultArguments = [100, 100, 50] #default parameters
    cmdlineArguments = getopt.getopt(sys.argv[1:], "svo)")[1] #retrieve command line arguments
    #replace default parameters with those added via command line
    for i in range(len(defaultArguments)):
        if i > (len(cmdlineArguments) - 1):
            break
        defaultArguments[i] = int(cmdlineArguments[i])
    
    return defaultArguments

def __main__():
    xyr = getArgs()
    drawCircle(xyr[0], xyr[1], xyr[2])
    turtle.mainloop()

__main__()