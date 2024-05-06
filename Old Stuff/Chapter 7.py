myList = [2,2,2,2]
for y in range(1,15):

    number = int(input("put a number"))
    myList.append(number)
    print(myList)

x = 0
y = 0
for n in myList:
    if n % 2 == 1:
        x+=1
    else:
        y +=1

print("odd numbers =",x)
print("even numbers =", y)
