def validateplatenum():
    x = 0
    while x == 0:
        platenum = input("Enter a valid plate number")
        dnum = 0
        upnum = 0

        if platenum == "back":
            menu()
        for char in platenum:
            if char.isupper():
                upnum += 1
            else:
                upnum = upnum

        for char in platenum:
            if char.isdigit():
                dnum += 1
            else:
                dnum = dnum

        if upnum == 1 and dnum == 4:
            print("This is a validated plate number")
            x = + 1

        else:
            x = 0

    day = input("Date of the month?")
    month = input("Month?")
    year = input("Year?")
    repairnum = input("How many repairs has this car received?")
    myfile = open("CARSALES1.txt", "a")
    myfile.write(platenum + " ||| ")
    myfile.write(day + "/" + month + "/" + year + " ||| ")
    myfile.write(repairnum + "\n")
    myfile.close()
    menu()

def search():
    searchfile = open("CARSALES1.txt", "r")
    b = input("input the car's plate number")
    if b == "back":
        menu()
    for line in searchfile:
        if b in line:
            print(line[0:5] + "\n")
            print(line[10:20] + "\n")
            print(line[25])
            break
    else:
        print("REGISTRATION NOT FOUND")
    searchfile.close()
    menu()

def searchrepair():
    d = input("input the number of repair")
    searchrepairfile = open("CARSALES1.txt", "r")
    if d == 'back':
        menu()
    for line in searchrepairfile:
        if line[25] >= d:
            print(line)
            maxrepairvisits = line[25]
            if line[25] > maxrepairvisits:
                maxrepairvisits = maxrepairvisits

            elif line[25] < maxrepairvisits:
                maxrepairvisits = line[25]

    if d > maxrepairvisits:
        print("NO CARS FOUND")
    searchrepairfile.close()
    menu()

def are_you_sure():
    sure = input("Are you sure?(y/n)")
    if sure == "y":
        print("")
    elif sure == "n":
        menu()
    else:
        menu()

def menu():
    print("Type 1 to input data")
    print("Type 2 to search data")
    print("Type 3 to search data by repairs")
    print("Type 4 to input new data of new car sale(basically 1)")
    print("Type 5 to exit")


    number = input("Which number do you want?")


    if number == "1":
        are_you_sure()
        y = 0
        validateplatenum()


    elif number == "2":
        are_you_sure()
        search()

    maxrepairvisits = "0"
    if number == "3":
        are_you_sure()
        searchrepair()

    elif number =="4":
        are_you_sure()
        validateplatenum()
    elif number == "5":
        are_you_sure()
        print("Cy@ u flamingo ripperino")
        exit()
    elif number > "5":
        print("u kappacino i told you a number from 1-4 and get out of here before i report and afk xd, rito banned me after this one")

menu()

