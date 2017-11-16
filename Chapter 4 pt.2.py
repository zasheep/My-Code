import turtle
x=0
total = 0
def draw_equitriangle(t,sz):
    for c in range(3):
        t.forward(sz)
        t.right(120)


def sum_to(n):
    if n<x:
        x = x +1
        total = x + x
    print(total)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()


draw_equitriangle(alex, 50)

sum_to(10)
wn.mainloop()
