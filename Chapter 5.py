
number = int(input("input a number from 0-6"))
if number == 0:
    number = "Sunday"

elif number == 1:
    number = "Monday"

elif number == 2:
    number = "Tuesday"

elif number == 3:
    number = "Wednesday"

elif number == 4:
    number = "Thursday"

elif number == 5:
    number = "Friday"

elif number == 6:
    number = "Saturday"
else:
    print("thats not an acceptable number")
    exit()


number = int(input("Whats the day today? 1 for monday, 2 for tuesday, etc."))
number = number + 137
while number > 7:

    number = number - 7

print (number, "Is the day u return at")

mark = float(input("whats your marks"))
if mark >74:
    print ("first")

elif mark > 69:
    print ("upper")

elif mark > 59:
    print("second")

elif mark > 49:
    print("third")
elif mark >44:
    print(" F1 Supp")
elif mark > 39:
    print("F2")
else :
    print("u're really bad at test, git gud, F3. failfailfail")




