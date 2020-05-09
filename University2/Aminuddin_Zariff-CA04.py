#201458599, Aminuddin_Zariff-CA04.py
#November, 2019
#Creating and calling functions to calculate, input and output student mark's and late penalties

def main():
    option = ""
    while option not in ("C", "X"):  #This while loop is used to repeatedly printing our menu until exiting.
        print("\n-------Main Menu-------")
        print("Option A: Select A to enter in your mark")
        print("Option B: Select B if you were a late submission")
        print("Option C: Select C or X to exit")
        print("-------Main Menu-------\n")
        option = input("Enter your option:")
        option = option.upper()

        while option not in ("A", "B", "C", "X"):      #This while loop is used to valid our inputs
            print("Invalid input, try again")
            option = input("Enter your option:")
            option = option.upper()

        if option == "A":
            student_Mark()      #Selecting A and B will call our functions
        elif option == "B":
            late_Submission()
        else:
            exit()

def student_Mark():
    mark = int(input("Enter your achieved raw mark:"))
    while mark not in range(0, 101): #This while loop uses not in range() because inputting 100 numbers in out tuple would be too long
        print("Invalid input, try again")   #The while loop is our valid input check
        mark = int(input("Enter your achieved raw mark:"))
    print("Final mark:", mark)
    return

def late_Submission():
    late = int(input("How many days late is this submission?"))
    while late < 0:                 #While loop is used to check for valid inputs
        print("Invalid input, try again")
        late = int(input("How many days late is this submission?"))

    mark = int(input("Enter your achieved raw mark:")) #As you might notice, line 42-45 is almost an exact replica of my student_Mark() function
    while mark not in range(0, 101): #Initially I tried to call the function from here but noticed that the variable is local and didnt work with this function
        print("Invalid input, try again") #So I ended up having to repeat the same lines of code for inputting marks.
        mark = int(input("Enter your achieved raw mark:"))

    if late > 7:
        mark = 0
        print("Due to your lateness, your mark has been dropped to a 0")
        print("Final mark:", mark)
        return

    elif late in (1, 2, 3, 4, 5, 6, 7):
        if mark < 40:  #This is to make sure a student does not gain marks because they are late and receive the 40 mark cap
            print("Mark is too low to receive any penalties")
            print("Final mark:", mark)
            return
        else:
            days = 0
            print("\nRaw Grade:", mark)
            print("Numbers of days late:", late)
            print("\nDays late\tMark to Award")
            for i in range(late + 1): #the range is (late + 1) because it counts from 0 and stops 1 less, so I added 1 so calculations occur correct amount of times
                print(days, "\t\t   ", mark)
                mark = mark - 5
                if days == late: #The variable days is used as a counter because we added 1 earlier to our loops, the calculation will be off by 1 loop
                    mark = mark + 5 #Thus comes the condition to reverse the calculation once and have a correct output
                else:
                    days = days + 1
            if mark < 40:
                mark = 40
                print("\nThis mark will be capped at 40")
                print("Final mark:", mark)
                return
            else:
                print("Final mark:", mark)
                return
    else: #This is selected in the case that late = 0, the student isn't late in this case.
        print("You will not receive any late penalties")
        print("Final mark:", mark)
        return

main()