y = 0

def validateuserid():
    x = 0
    f =0

    while x == 0:
        userid = input("Enter a valid userID")
        dloop = 0
        gloop = 0
        floop = 0

        for char in userid:
            if char.isupper():
                dloop += 1
            else:
                dloop = dloop

        for char in userid:
            if char.islower():
                gloop += 1
            else:
                gloop = gloop

        for char in userid:
            if char.isdigit():
                floop += 1
            else:
                floop = floop

        if dloop==1 and gloop==2 and floop==3:
            print("User ID is valid")
            x =+ 1
        else:
            print("unacceptable")
            x = 0

    name = input("what is your name")
    while f == 0:
        phoneloop = 0
        phonenumber = input("What is your phone number")
        for char in phonenumber:
            if char.isdigit():
                phoneloop = phoneloop +1

            else:
                phoneloop = 0
        if phoneloop == 10:
            print("Phone number acceptable")
            f =+1
        else:
            print("https://youtu.be/A1dAs0aWas8?t=1m12s, copy paste this and write in a real number.")

            f = 0
    datejoined = input("Date joined?(dd/mm/yyyy)")
    myfile = open("test.txt", "a")
    myfile.write(userid + "\t")
    myfile.write(name+ "\t")
    myfile.write(phonenumber + "\t")
    myfile.write(datejoined + "\n")
    myfile.close()

while y ==0:
    z = input("Input Data? y/n")
    if z == "y":
        validateuserid()
        y =0
    elif z == "n":
        y =+ 1

printfile = open("test.txt", "r")
for line in printfile:
    print (line)
printfile.close()

t = input("Do you want to search for anyone's information?(y/n)")

if t == "y":
    searchfile = open("test.txt", "r")
    b = input("input user id or name")
    for line in searchfile:
        if b in line: print (line)
    searchfile.close()

elif t =="n":
    print("cy@")

