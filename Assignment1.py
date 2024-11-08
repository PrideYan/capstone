from turtle import *

def draw_Duo_La_A_Meng():
    # print head
    penup()
    goto(0, -100)
    pendown()
    begin_fill()
    color("blue")
    circle(150)
    end_fill()

    # print eyes
    penup()
    goto(-40, 40)
    pendown()
    begin_fill()
    color("white")
    circle(30)
    end_fill()

    penup()
    goto(-40, 40)
    pendown()
    begin_fill()
    color("black")
    circle(15)
    end_fill()

    penup()
    goto(40, 40)
    pendown()
    begin_fill()
    color("white")
    circle(30)
    end_fill()

    penup()
    goto(40, 40)
    pendown()
    begin_fill()
    color("black")
    circle(15)
    end_fill()

    # print nose
    penup()
    goto(0, 0)
    pendown()
    begin_fill()
    color("red")
    circle(20)
    end_fill()

    # print mouth
    pensize(5)
    penup()
    goto(-60, -20)
    pendown()
    seth(20)
    fd(80)

    penup()
    goto(-60, -30)
    pendown()
    seth(-20)
    fd(80)

    penup()
    goto(60, -20)
    pendown()
    seth(160)
    fd(80)

    penup()
    goto(60, -30)
    pendown()
    seth(200)
    fd(80)

    # print body
    penup()
    goto(-100, -250)
    pendown()
    begin_fill()
    color("blue")
    seth(0)
    fd(200)
    circle(80, 180)
    fd(200)
    circle(80, 180)
    end_fill()

    # print pocket
    penup()
    goto(-40, -230)
    pendown()
    begin_fill()
    color("white")
    seth(0)
    fd(80)
    circle(40, 180)
    fd(80)
    circle(40, 180)
    end_fill()
    
    # print hand
    penup()
    goto(-160, -140)
    pendown()
    begin_fill()
    color("blue")
    seth(0)
    circle(40)
    end_fill()

    penup()
    goto(160, -140)
    pendown()
    begin_fill()
    color("blue")
    seth(0)
    circle(40)
    end_fill()

    # print foot
    penup()
    goto(-80, -320)
    pendown()
    begin_fill()
    color("blue")
    seth(0)
    circle(40)
    end_fill()

    penup()
    goto(80, -320)
    pendown()
    begin_fill()
    color("blue")
    seth(0)
    circle(40)
    end_fill()
    
    exitonclick()  # EXIST

print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for Duo_La_A_Meng)\n"
              "Your selection is: ")
    try:
        a = eval(a)
        if a == 1:
            draw_Duo_La_A_Meng()
        else:
            print("Please input the value in [1]")
    except:
        print("Please input the value in [1]")
