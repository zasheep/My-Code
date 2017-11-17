import time

boys = []
girls = []
boyover = 0
boynormal = 0
boyunder = 0
girlover = 0
girlnormal = 0
girlunder = 0
averageboy = 0
averagegirl = 0
loop = "y"

while loop == "y":
    gender = str(input("Is it a b or a g?(b for boy, g for girl and s FOR A SUMMARY OF YOUR ENTRIES)"))
    if gender == ("b"):
        weight1 = float(input("How much does the newborn baby weight?"))
        if weight1 < 2.5:
            boys.append(weight1)
            boyunder = boyunder + 1
        elif weight1 > 4.5:
            boys.append(weight1)
            boyover = boyover + 1
        else:
            boys.append(weight1)
            boynormal = boynormal + 1


    elif gender == ("g"):
        weight1 = float(input("How much does the newborn baby weight?"))
        if weight1 < 2.5:
            girls.append(weight1)
            girlunder = girlunder + 1
        elif weight1 > 4.5:
            girls.append(weight1)
            girlover = girlover + 1
        else:
            girls.append(weight1)
            girlnormal = girlnormal + 1


    elif gender == ("s"):
        averageboy = sum(boys)/len(boys)
        averagegirl = sum(girls)/len(girls)
        print("The average weight of a baby boy is ", (averageboy), "kg")
        print("The average weight of a baby girl is ", (averagegirl), "kg")
        print("Number of baby boys overweight:", (boyover))
        print("Number of baby boys underweight:", (boyunder))
        print("Number of baby boys normal weight:", (boynormal))
        print("Number of baby boys overweight:", (girlover))
        print("Number of baby boys underweight:", (girlunder))
        print("Number of baby boys normal weight:", (girlnormal))
        time.sleep(30)
        break
