from swampy.TurtleWorld import *

world = TurtleWorld()
t = Turtle()
length = int(raw_input('Enter the side length for the square:'))

def square(t):
    print t
    for i in range(4):
        fd(t,length)
        lt(t)

square(t)

wait_for_user()
