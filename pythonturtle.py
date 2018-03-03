# try this either as a .py file or in the python shell
import turtle

# turtle.home()
# turtle.begin_poly()
# turtle.fd(100)
# turtle.left(20)
# turtle.fd(30)
# turtle.left(60)
# turtle.fd(50)
# turtle.end_poly()
# p = turtle.get_poly()
# register_shape("myFavouriteShape", p)

turtle.color("blue", "red")
turtle.begin_fill()
turtle.circle(120)
turtle.end_fill()

# turtle.reset()
# turtle.shape("circle")
# turtle.shapesize(5,2)
# turtle.tilt(45)
# turtle.tiltangle()


turtle.shape("turtle")
# the distance we want the pointer to travel each time
DIST = 100
for x in range(0,6):
    print "x", x
    for y in range(1,5):
        print "y", y
        # turn the pointer 90 degrees to the right
        turtle.right(90)
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
    DIST += 20

turtle.exitonclick()

