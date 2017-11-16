def turn_clockwise(n):
    if n == "n":
        print("East")
    elif n == "e":
        print("South")
    elif n == "s":
        print("West")
    elif n =="e":
        print("North")
    else:
        print("wrong")

turn_clockwise("n")

def second_inhours(f):
    too = f*3600
    print(too)

second_inhours(9)