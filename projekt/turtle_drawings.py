# Funkce pro kreslení sluníčka a sněhuláka (pomocí turtle)

import turtle
import threading

def wait_for_ok():
    screen = turtle.Screen()
    screen.title("Klikni Enter nebo zavři okno")
    screen.onkey(screen.bye, "Return")
    screen.listen()

    try:
        screen.mainloop()
    except turtle.Terminator:
        pass  # bezpečně ukončeno



def draw_snowman():
    def run():
        turtle.clearscreen()
        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(0, -100)
        t.pendown()
        t.circle(50)
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.circle(35)
        t.penup()
        t.goto(0, 60)
        t.pendown()
        t.circle(20)
        wait_for_ok()

    threading.Thread(target=run).start()


def draw_sun_1():
    def run():
        turtle.clearscreen()
        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        t.color("gold")

        t.penup()
        t.goto(0, -100)
        t.begin_fill()
        t.circle(100)
        t.end_fill()

        t.penup()
        t.goto(0, 0)
        t.pensize(3)
        for _ in range(18):
            t.forward(140)
            t.pendown()
            t.forward(20)
            t.penup()
            t.backward(160)
            t.right(20)

        wait_for_ok()

    threading.Thread(target=run).start()



def draw_sun_2():
    def run():
        turtle.clearscreen()
        t = turtle.Turtle()
        t.color("orange")
        t.penup()
        t.goto(0, -60)
        t.begin_fill()
        t.circle(60)
        t.end_fill()
        t.goto(0, 0)
        t.color("darkorange")
        for _ in range(36):
            t.forward(80)
            t.backward(80)
            t.right(10)
        wait_for_ok()
    threading.Thread(target=run).start()


def draw_sun_3():
    def run():
        draw_sun_1()  # nakreslí základ
        t = turtle.Turtle()
        t.color("red")
        for i in range(12):
            t.penup()
            t.goto(0, 0)
            t.setheading(i * 30)
            t.forward(100)
            t.pendown()
            t.circle(10)
        wait_for_ok()
    threading.Thread(target=run).start()