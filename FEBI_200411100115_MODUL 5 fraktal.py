# 200411100115 FEBI FADLILAH NUR AMINAH

import turtle
my_pen = turtle.Turtle()
my_screen = turtle.Screen()
my_pen.hideturtle()
my_pen.penup()
my_pen.setposition(-200,200)
my_pen.pendown()
my_pen.showturtle()
# Fungsi Pembuatan Fractal
def fractal(my_pen,line,start,lvl):
    if lvl > 0 :
        if start < 4:
            my_pen.forward(line/2)
            my_pen.right(90)
            my_pen.forward(line)
            my_pen.right(90)
            my_pen.forward(line/2)
            my_pen.right(90)
            fractal(my_pen,line,start+1,lvl)
        else:
            fractal(my_pen,line/2,0,lvl-1)
# main 
fractal(my_pen,400,0,6)
my_screen.exitonclick()
