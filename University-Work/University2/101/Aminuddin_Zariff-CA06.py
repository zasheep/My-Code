#201458599, Aminuddin_Zariff-CA06.py
#November, 2019
#Calculating the total cost of 5 flights, revenue and profit with varying cases
import random
FlightCost = 5000
def CreateMatrix(num):  #This function randomly generates a flight plan of 15 passengers or a full flight.
    if num == 1:        #It knows how to choose by random boolen selection of either 1 or 'Else:' a 0.
        flight_Matrix = [[num for row in range(5)] for col in range(5)]
        return flight_Matrix
    else:
        Counter = 0
        while Counter != 15:  #This while loop is used to count and make sure the random generated flight has 15 passengers
            Counter = 0  #This variable had to be repeated twice to reset if we didn't get the correct array we wanted
            row = 5
            col = 5
            list_5x5 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
            for r in range(row):
                for c in range(col):
                    list_5x5[r][c] = random.randint(0,1)   #This chooses for either 1 or 0 to be appended into the array
                    SeatInOrNot = list_5x5[r][c]
                    if SeatInOrNot == 1:
                        Counter = Counter + 1
                    else:
                        Counter = Counter
        return list_5x5
def CreateDrinkPrice():  #This function asks and passes the cost of the drink around
    DrinkPrice = int(input("Whats the wholesale cost of one drink?"))
    return DrinkPrice
def CalSeatPrice():     #This function asks and passes the user's seat pricing of what the user wants
    cost = int(input("Enter the Cost of a Band-B Seat:"))
    return cost
def SeatCount(list, SeatClass): #This function is used to calculate the number of seats in Band-A or Band-B when selected
    SeatsInA = 0
    SeatsInB = 0
    SumFlightPlan = [sum(i) for i in list]
    if SeatClass == 'A':
        for i in SumFlightPlan[0:2]:
            SeatsInA = SeatsInA + i
        return SeatsInA
    else:
        for i in SumFlightPlan[2:5]:
            SeatsInB = SeatsInB + i
        return SeatsInB
def CalcProfitMargins(flightplan, drinkcost, percent): #This function outputs what the operator wants to know for min&max profit
    global FlightCost
    SeatsInA = SeatCount(flightplan,'A') #Calculates number of seats in A
    SeatsInB = SeatCount(flightplan,'B') #Calculates number of seats in B
    TotalSeats = SeatsInA+SeatsInB
    Revenue = (FlightCost * (1+percent/100)) #Calculates the revenue for the desired min/max profit
    BandB = Revenue/(2*SeatsInA+SeatsInB) #This is algebracally calculated, eg.5000 = BandA(x) + BandB(y)
    BandA = BandB*2                       #Where x = 2y, 5000 = 10(2y) + 15(y)...5000 = y(20+15)...5000/(20+15) = y
    print("To achieve a profit at",percent,"%:")
    print("1.Seat Only")
    print(f"Band-A seat price = {BandA:.2f}")
    print(f"Band-B seat price = {BandB:.2f}")
    print("Revenue = ",Revenue)
    BandB = (Revenue - (TotalSeats*drinkcost))/(2*SeatsInA+SeatsInB)
    BandA = BandB*2
    print("\n2. Seat + Consumables")
    print(f"Band-A seat price = {BandA:.2f}")
    print(f"Band-B seat price = {BandB:.2f}")
    print("Consumable Price =", drinkcost)
    return(Revenue)
def PrintLayout(flightplan): #This function prints out our flight plan without "[]" and
    for row in flightplan:
        for column in row:
            print(column, end=" ")
        print()
def CalcRevenue(flightplan, drinkrevenue, percent): #This function calls and simplifies for each flight cost and revenue
    TotalRevenue = CalcProfitMargins(flightplan, drinkrevenue, percent)
    print("Cost:", FlightCost)
    print("Revenue:",TotalRevenue)
    print("")
    return TotalRevenue
def CalcFlight(DrinkRevenue, SeatPrice, FullOrHalfFull): #This function intialises and calls for a random flight to be generated
    FlightPlan = CreateMatrix(FullOrHalfFull)
    print("Flight Plan for the flight:")
    PrintLayout(FlightPlan)
    Revenue = (SeatPrice * SeatCount(FlightPlan,'A')*2) + (SeatPrice * SeatCount(FlightPlan,'B'))
    print("")
    print("This is the revenue and cost for your selected seat pricing:")
    print("Band-A seat price = ", SeatPrice*2)
    print("Band-B seat price = ", SeatPrice*1)
    print("Revenue = ", Revenue)
    print("")
    CalcRevenue(FlightPlan, DrinkRevenue, 0) #These 3 lines and under generates the output for breakeven, 2% & 10% profits
    CalcRevenue(FlightPlan, DrinkRevenue, 2)
    CalcRevenue(FlightPlan, DrinkRevenue, 10)
    return Revenue
def main():
    DrinkRevenue = CreateDrinkPrice()
    SeatPrice = CalSeatPrice()
    Total = 0
    for i in range(5): #5 flights are generated
        FullOrHalfFull = random.randint(0,1)
        Sum = CalcFlight(DrinkRevenue, SeatPrice, FullOrHalfFull)
        Total = Total + Sum
    print("Total Cost:", FlightCost*5)
    print("Total Revenue for your selected seat price and 5 flights:", Total)
main()



