from turtle import *
 

#I want to pait a house

#step 1:draw a square
speed(5)
width(6)
color("purple")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#step 2:draw a door
forward(70)
color("red")
begin_fill()
left(90)
forward(100)    #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200,200)
pendown()


#step 3:draw a roof
color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#step 4:draw a window
penup()
goto(170,170)
pendown()


color("blue")
begin_fill()
left(30)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

color("purple")
forward(30)
left(90)   
forward(30)
left(30)
color("black")
forward(200)
left(120)
forward(200)
color("purple")
left(30)
forward(30)
left(90)
forward(30)
color("blue")
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()
penup()
goto(0,0)
pendown
right(90)

exitonclick()