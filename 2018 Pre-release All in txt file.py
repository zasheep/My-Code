maths = []
physics = []
biology = []
economics = []
chemistry = []
def name():
    x = 0
    y =0
    datenum = 0
    monthnum = 0
    yearnum = 0

    while x == 0:
        digitcount1 = 0

        studentname1 = input("Enter your first name")
        for char in studentname1:
            if char.isdigit():
                digitcount1 += 1
            else:
                digitcount1 = digitcount1
        if digitcount1 > 0:
            print("wrong")
            x = 0
        else:
            x += 1

    while y == 0:
        digitcount2 = 0
        studentname2 = input("Enter your last name")
        for char in studentname2:
            if char.isdigit():
                digitcount2 += 1
            else:
                digitcount2 = digitcount2
        if digitcount2 > 0:
            print("wrong")
            y = 0
        else:
            y+=1

    while datenum == 0:
        date = input("Enter which day date number you were born in")
        datenum2 = date
        if datenum2>"31":
            print("A number from 1 to 31 please")
            datenum = 0
        else:
            datenum += 1

    while monthnum == 0:
        month = input("Enter which month number you were born in")
        monthnum2 = month
        if monthnum2>"12":
            print("A number from 1 to 12 please")
            monthnum = 0
        else:
            monthnum += 1

    while yearnum == 0:
        year = input("Enter which year you were born in")
        yearnum2= year
        if yearnum2>"2018":
            print("An actual exisiting year please")
            yearnum = 0
        else:
            yearnum += 1

    myfile = open("AllinTXTFile.txt","a")
    myfile.write(studentname1+" ||| "+studentname2+" ||| "+datenum2+"/"+monthnum2+"/"+yearnum2+" ||| ")
    myfile.close()

    loop = 0
    while loop == 0:
        print("The subjects available in this School are maths, physics, biology, chemistry, economics")
        notdone = input("Do you take any of these subjects?(Don't put in the same subject twice!)(y/n)")
        if notdone =="y":
            classes = input("What subjects do you take?(One at a time)")
            if classes == "maths":
                maths.append(studentname1)
                print(maths)
                myfile = open("AllinTXTFile.txt", "a")
                myfile.write(classes+" ||| ")
                myfile.close()
                loop = 0
            elif classes == "physics":
                physics.append(studentname1)
                print(physics)
                myfile = open("AllinTXTFile.txt", "a")
                myfile.write(classes + " ||| ")
                myfile.close()
                loop = 0
            elif classes == "biology":
                biology.append(studentname1)
                print(biology)
                myfile = open("AllinTXTFile.txt", "a")
                myfile.write(classes + " ||| ")
                myfile.close()
                loop = 0
            elif classes == "chemistry":
                chemistry.append(studentname1)
                print(chemistry)
                myfile = open("AllinTXTFile.txt", "a")
                myfile.write(classes + " ||| ")
                myfile.close()
                loop = 0
            elif classes == "economics":
                economics.append(studentname1)
                print(economics)
                myfile = open("AllinTXTFile.txt", "a")
                myfile.write(classes + " ||| ")
                myfile.close()
                loop = 0


        elif notdone =="n":
            myfile = open("AllinTXTFile.txt", "a")
            myfile.write("\n")
            myfile.close()
            loop += 1

    print("Maths Class:", maths)
    print("Physics Class: ", physics)
    print("Biology Class: ", biology)
    print("Chemistry Class: ", chemistry)
    print("Economics Class: ", economics)

dataloop= 0
while dataloop ==0:
    z2 = input("Input Data? y/n")
    if z2 == "y":
        name()

        dataloop =0

    elif z2 == "n":
        dataloop =+ 1

def search():
    search = input("type this persons name to search what class he/she takes")
    if search in maths:
        print(search, "takes maths")
    if search in physics:
        print(search, "takes physics")
    if search in biology:
        print(search, "takes biology")
    if search in chemistry:
        print(search, "takes chemistry")
    if search in economics:
        print(search, "takes economics")
searchloop = 0
while searchloop==0:
    z3 = input("Search what a student takes? y/n")
    if z3 == "y":
        search()
        searchloop = 0

    elif z3 == "n":
        searchloop= + 1

def number():
    number = input("What subject do you want to search for?(maths, physics, economics, biology, chemistry)")
    physicsnum = 0
    mathsnum = 0
    biologynum = 0
    economicsnum = 0
    chemistrynum = 0
    if number == "maths":
        for x in  maths:
            mathsnum += 1
        print("There are",mathsnum, "people taking maths")
    elif number == "physics":
        for x in physics:
            physicsnum += 1
        print("There are",physicsnum, "people taking physics")
    elif number == "chemistry":
        for x in chemistry:
            chemistrynum += 1
        print("There are",chemistrynum, "people taking chemistry")
    elif number == "biology":
        for x in biology:
            biologynum += 1
        print("There are",biologynum, "people taking biology")
    elif number == "economics":
        for x in economics:
            economicsnum += 1
        print("There are",economicsnum, "people taking economics")
numberloop = 0
while numberloop == 0:
    z4 = input("Search how students are take 'x' subject?(y/n)")
    if z4 == "y":
        number()
        numberloop = 0

    elif z4 =="n":
        numberloop += 1

def date():
    date = input("Which year do you want to search for?")
    searchtxtfile = open("AllinTXTFile.txt", "r")
    for line in searchtxtfile:
        if date in line:
            print(line)
        elif date not in line:
            continue
dateloop = 0
while dateloop ==0:
    z5 = input("Search which students are born in a specific year?(y/n)")
    if z5 == "y":
        date()
        dateloop = 0

    elif z5 == "n":
        dateloop += 1