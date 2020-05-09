# 201458599, Aminuddin_Zariff-CA07.py
# December, 2019
# To play a board game against a computerised player 2 where a square of tokens is the winning goal
import random

def MatrixCreate(x,y):
    Matrix = [[0 for col in range(y)] for row in range(x)] #Creates a Matrix based on length of x and y. x & y = 5
    return Matrix

def PrintLayout(Matrix): #This prints out the matrix in a format suitable for the users eyes
    for row in Matrix:
        for column in row:
            print(column, end=" ")
        print()

def PlayerMove(XorY): #This promts the user to enter in their desired x and y position in the matrix
    if XorY == 'X':
        Move = int(input("Select your X Co-ordinate:"))
        return Move
    else:
        Move = int(input("Select your Y Co-ordinate:"))
        return Move

def ComputerMove(XorY,x,y): #Computer randomly generates an x and y postion for matrix
    if XorY == "X":
        Move = random.randint(1,x)
        return Move
    elif XorY == "Y":
        Move = random.randint(1,y)
        return Move

def Turn(Field,x,y,player):
    if player == 1:
        xPlayer = PlayerMove("X") #Player is promted to input their x Co-ordinate
        yPlayer = PlayerMove("Y") #Player is promted to input their y Co-ordinate
        FieldUpdate(xPlayer,yPlayer,1,Field) #This changes the matrix with their chosen x and y
        print("\nPlayer Moves:")
        PrintLayout(Field)
        WinCondition = CheckWin(Field,xPlayer,yPlayer,1) #Checks if the player has achieved the goal state
        print("")
        return WinCondition
    else:
        print("Computer Moves:")
        xComputer = ComputerMove("X",x,y) #Computer chooses their x Co-ordinate
        yComputer = ComputerMove("Y",x,y) #Computer chooses their y Co-ordinate
        FieldUpdate(xComputer,yComputer,2,Field) #This changes the matrix with their chosen x and y
        PrintLayout(Field)
        print("")
        return

def FieldUpdate(x,y,Player,Field): #This def updates the board/matrix of the game
    if Field[y - 1][x - 1] == 1:
        if Player == 1:
            if Field[y - 1][x - 1] == 1 or Field[y - 1][x - 1] == 2: #If the player selects a player owned space, they are promted to select a new space
                print("This space is occupied, select new co-ordinates")
                xPlayer = PlayerMove("X")
                yPlayer = PlayerMove("Y")
                FieldUpdate(xPlayer, yPlayer, 1, Field) #recursion is used to update their newly selected Co-ordinates
                return
        elif Player == 2: #On a player owned space, Computer takes over it
            if Field[y - 1][x - 1] == 2: #However if the computer selects its own, it will select a new one
                xComputer2 = ComputerMove("X", x, y)
                yComputer2 = ComputerMove("Y", x, y)
                FieldUpdate(xComputer2, yComputer2, 2, Field)
                return
            elif Field[y - 1][x - 1] == 1: #Computer takes over a player owned space
                Field[y - 1][x - 1] = 2
                return
            else:
                return

    elif Field[y - 1][x - 1] == 2: #This line is to be careful of recursion, player should not be able to take over a Computer owned space
        if Player == 1: #thus the player is promted to choose new Co-ordinates
            print("This space is occupied, select new co-ordinates")
        xPlayer = PlayerMove("X")
        yPlayer = PlayerMove("Y")
        FieldUpdate(xPlayer, yPlayer, 1, Field)
        return
    else: #If the space is empty, this is selected and the space is updated accordingly to who's move it is
        if Player == 1:
            Field[y - 1][x - 1] = 1
            return
        else:
            Field[y - 1][x - 1] = 2
            return

def CheckWin(Field,x,y,player): #Checks if the player achieved it's Win Condition
    for i in Field:
        for z in i:
            if x == 5 or y == 5: #WinCheck should not work on the edges of the since it will select a non existing...
                WinCondition = 0 #element such as x Co-ordinate of 6 (Our matrix only goes from 1-5 or 0-4(python))
                return WinCondition #Thus is returned since Win Condition cannot be checked
            else:
                if Field[y][x] == player and Field[y-1][x-1] == player and Field[y][x - 1] == player and Field[y - 1][x] == player:
                    WinCondition = 1
                    return WinCondition
                else:
                    WinCondition = 0
                    return WinCondition

def Empty(Field): #This checks if the matrix is completely filled
    list = []
    for i in Field:
        for x in i:
            list.append(x)
            if x == 0: #If the matrix is still empty, the game still goes on
                WinCondition = 0
                return WinCondition #WinCondition is passed here due to our while loop usage at line 124
            else:
                z = 1 #does nothing, so our for loop can pass through(line 103)
    x = 0
    if x not in list: #If the matrix is full, WinCondition of 2 is passed and Computer Wins.
        WinCondition = 2
        return WinCondition

def main():
    x= 5
    y= 5
    Count = 1
    WinCondition = 0
    Field = MatrixCreate(x,y)
    PrintLayout(Field)
    while Count != 0:
        while WinCondition != 1:
            WinCondition = Turn(Field,x,y,1) #Player always moves first
            if WinCondition == 0:
                Turn(Field,x,y,2) #If the game hasn't ended, Computer then moves
                #Turn(Field,x,y,2) #FOR TESTING PURPOSES, this line allows for the computer to move twice or thrice
                #Turn(Field,x,y,2) #Remove the '#' for twice or thrice, etc
                #Turn(Field,x,y,2)
                WinCondition = Empty(Field) #Checks if the matrix is empty
                if WinCondition == 2:
                    print("You lost. Computer Wins")
                    exit()
        Count = 0 #If the Win Condition is met, the while loop to keep the game going is broken and the player is promted a victory
    print("You've won. Congratulations")
    exit()

main()