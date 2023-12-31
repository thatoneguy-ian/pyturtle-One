# Import turtle, Set Screen Size and Speed
from turtle import *
Screen().setup(1290, 565)
speed(10)

# Set Background Color
bgcolor("black")

# create the orange planet
color("orange")
begin_fill()
circle(60)
end_fill()

#move forward
penup()
forward(100)
pendown()

# create grey planet
color("grey")
begin_fill()
circle(20)
end_fill()

# move forward 
penup()
forward(80)
pendown()

# create red planet
color("red")
begin_fill()
circle(40)
end_fill()

# Move forward 
penup()
forward(90)
pendown()

# Create Green Planet 
color("green")
begin_fill()
circle(20)
end_fill()

done()