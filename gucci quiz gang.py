import sys
y = 0
x = 3
while y < 1:
        question1 = input("What is the fastest land animal?")
        if question1  == 'cheetah':
            y =+1
            print("correct")

        elif x  == 0:
            sys.exit("bye")

        else:
            print("Wrong answer")
            print("You have", x, "lives left")
            x-=1
            
while y<2:
        question2 = input("type 'nihao'")
        if question2 == 'nihao':
            print("nicely done, you now have 2 iq, just 198 more questions")
            y=+1
            break
        elif x  == 0:
            sys.exit("bye")
        else:
            print("Wrong answer")
            print("You have", x, "lives left")
            x-=1

while y<3:
    question3 = input("This is a hard question")
    if question3 == 'yes' or 'no':
            print("nicely done, you now have 3 iq, just 197 more questions")
            y=+1
            break
    elif x  == 0:
            sys.exit("bye")
    else:
        print("Wrong answer")
        print("You have", x, "lives left")
        x-=1

while y<4:
    question4 = input("What is always answered but never asked. Hint:a doorbell")
    if question4 == 'a doorbell':
            print("nicely done, you now have 200 iq, just 1 more question")
            y=+1
            break
    elif x  == 0:
            sys.exit("bye")
    else:
        print("Wrong answer")
        print("You have", x, "lives left")
        x-=1

while y<5:
    question5 = input("What goes after gucci")
    if question5 == 'gang':
            print("nicely done, you now have -200 iq")
            for i in range(200000):
                print ("gucci")
                print ("gang")
