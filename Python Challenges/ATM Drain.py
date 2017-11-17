import time
print ("Your bank account has $5000 Dollars, How much would you like to Withdraw?")
print ("We will only accept a transaction if the amount of money you would like to withdraw is a multiple of 5")
print ("We will also charge you $0.5 for each successful transaction")

amount = int(input("How much would you like you to withdraw?"))

if amount % 5 == 0:
    time.sleep(1)
    print("Please wait")
    time.sleep(1)
    print("Money printing")
    time.sleep(1)
    print("Done, please collect the money")
    print(5000 - amount, "is left in your bank account.")
    amount = 5000 - amount
    print("Subtracting an extra $0.5 for a successful transaction")
    time.sleep(1)
    print (amount - 0.5, "is left in your bank account")

elif amount > 5000:
    print("You don't have that amount of money")
    time.sleep(1)
    print("Removing Card, transaction cancelled.")
    exit


else:
    print("Next time enter a number that is a multiply of 5")
    time.sleep(1)
    print("Removing Card, transaction cancelled.")
    exit

