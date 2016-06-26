from swampy.TurtleWorld import *

world = TurtleWorld()
t = Turtle()
sides = int(raw_input('Enter the number of sides for the polygon:'))
length = int(raw_input('Enter the side length for the polygon:'))
degrees = 360 / sides

def polygon(t):
    print t
    for i in range(sides):
        fd(t,length)
        lt(t, degrees)

polygon(t)

wait_for_user()
