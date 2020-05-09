#201458599, Aminuddin_Zariff-CA03.py
#October, 2019
#Using sequence, selection and iteration constructs to calculate and output the age of a cat in human years
cat_LifeStages = ''   #Inserting Variables
loop_Condition = ''
human_AgeEquivalent = 0
while loop_Condition != 'X':   #Uses a While loop to repeatedly print our menu and input
    print("\n---------Menu----------")
    print("A: Enter 'A' if your cat is still a Kitten or Junior")
    print("B: Enter 'B' if your cat is Prime, Mature, Senior, Geriatric Life stages")
    print("C: Enter 'X' to quit")
    print("---------Menu----------\n")
    option = input("Enter an option or press X to quit:")
    option = option.upper()
    #Input starts at line 13, line 14 is used to make the input all caps to reduce inserting eg. or option == "a" in line 16, 34, 51
    if option == "A":
        kitten_Age = int(input("How many months old is your Cat?"))
        if kitten_Age in(1,2,3,4,5,6,7): #This checks for our input to be correct to our given equivalence table especially in line 26
            cat_LifeStages = "Kitten"
            if kitten_Age < 4:
                human_AgeEquivalent = kitten_Age #Calculations occur after inputs under each if statements
            elif kitten_Age >= 4:
                human_AgeEquivalent = kitten_Age + 4
            print("The cat is", human_AgeEquivalent, "in human years") #Output are then printed out under each if statements
            print("The cat is a",cat_LifeStages)
        elif kitten_Age in(8,12,18,24):
            cat_LifeStages = "Junior"
            human_AgeEquivalent = kitten_Age + 3
            print("The cat is", human_AgeEquivalent, "in human years")
            print("The cat is a", cat_LifeStages)
        else:
            print("Enter a valid number, Try again")

    elif option == "B":
        kitten_Age = int(input("How many years old is your Cat?"))
        human_AgeEquivalent = (kitten_Age - 3) * 4 + 28
        if kitten_Age > 2 and kitten_Age < 19:
            if kitten_Age < 7:
                cat_LifeStages = "Prime"
            elif kitten_Age < 11:
                cat_LifeStages = "Mature"
            elif kitten_Age < 15:
                cat_LifeStages = "Senior"
            elif kitten_Age < 19:
                cat_LifeStages = "Geriatric"
            print("The cat is", human_AgeEquivalent, "in human years")
            print("The cat is a", cat_LifeStages, "cat")
        else:
            print("Enter a valid number, Try again")

    elif option == "X":   #this offsets my while loop, breaking it
        loop_Condition = "X"
        print("Exiting")
    else:
        print("Enter a valid option, try again")