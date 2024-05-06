import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")
alex.shape("turtle")
total = 0
total2 = 0
for i in range(1000):
    print("We like Python's turtles!")

for x in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    b = "One of the months of the year is " + x
    print(b)

alex.left(3645)
alex.right(45)
for xs in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    print(xs)
    total = total + xs

print(total)

for c in range(4):
    alex.forward(50)
    alex.right(90)

for d in range(3):
    alex.forward(50)
    alex.right(120)

for e in range(6):
    alex.forward(50)
    alex.right(60)

for f in range(8):
    alex.forward(50)
    alex.right(45)

for g in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    alex.forward(100)
    alex.right(g)
    total2 = total2 + g

print ("the pirate is heading in the direction of angle", total2)

for h in range(18):
    alex.forward(50)
    alex.right(20)

for j in range(5):
    alex.forward(100)
    alex.right(144)

for k in range(12):
    alex.penup()
    alex.forward(100)
    alex.pendown()
    alex.forward(10)
    alex.penup()
    alex.forward(10)
    alex.pendown()
    alex.stamp()
    alex.penup()
    alex.back(120)
    alex.right(30)

wn.mainloop()