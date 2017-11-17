senior = 0
carer = 2
total = 0
meal = 0
ticket = 0
coach = 0
cost = 0
loop == "y"

while loop == "y":
    senior = int(input("how many senior members?"))
    if senior < 10:
        print("Error, too little senior members to have an outing")
    elif senior >36:
        print("Error, too many senior members.")
    elif senior >24:
        carer = carer + 1
        total = carer + senior
        if total > 25:
            coach = 190
            meal = 13.5
            ticket = 20
            cost = coach + (meal*total)+(ticket*total)
            loop == "x"
            print (coach)
        elif total > 27:
            coach = 225
            meal = 13
            ticket = 19
            cost = coach + (meal*total)+(ticket*total)
            loop == "x"
            print (coach)
            
