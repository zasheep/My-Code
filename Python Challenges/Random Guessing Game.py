import random
print("Welcome to my guessing game")
print("My number is a random number between 1-100")
print("You have 10 tries until game over. Goodluck")
Number = random.randint(1,100)

t=0
while t<10:
    guess = int(input("Take a guess. "))
    if guess > Number:
        print ("Too high")
    elif guess < Number:
        print ("Too low")
    elif guess == Number:
        print ("Hooray you guessed it, Thank you for playing my game.")
        break

t=t+1

