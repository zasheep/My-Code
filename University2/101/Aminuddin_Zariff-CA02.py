#201458599, Aminuddin_Zariff-CA02.py
#October, 2019
#Sequencing and I/O control of strings and numbers to calculate and output the battery and distance travelled by the robot

import math   #We begin by importing math (this is for cosine, sine and pi) and stating our constants
speed = 1.5
battery_Usage_perSecond = 2.7

angle = float(input("Enter an angle between 0-90 degrees"))
if angle > 90 or angle < 0:     #these if statements in line 10 & 16 are for validation for correct inputs
    print("Error, enter an number between 0-90") #For efficiency, I used "or" instead of an Else statement
    print("Terminating")
    quit()

time_Travelled = float(input("How many seconds does the robot take to travel?"))
if time_Travelled < 0:
    print("Error, robot cannot travel below 0 seconds")
    print("Enter a number above 0")
    print("Terminating")
    quit()

radians = (angle/360)*2*math.pi     #Calculations are done
distance = speed * time_Travelled
horizontal_Distance = distance * math.cos(radians)
vertical_Distance = distance * math.sin(radians)
battery_Used = battery_Usage_perSecond * time_Travelled
battery_Left = 100 - battery_Used

print("--------------------------------------")  #Lastly, program outputs to 2 d.p so the calculated number looks clear
print(f"Distance Travelled: {distance:.2f}",)
print(f"Distance Travelled Horizontally: {horizontal_Distance:.2f}")
print(f"Distance Travelled Vertically: {vertical_Distance:.2f}")
print(f"Battery Usage: {battery_Used:.2f}%")

if battery_Used > 100:
    print("The battery will run out before reaching it's finally position!")
    quit()
elif battery_Used > 50:
    print("The battery usage is over 50% and cannot make a return trip immediately")
    print(f"Battery left:{battery_Left:.2f}")
else:
    print(f"Performing this trip will leave the robot at{battery_Left:.2f}%")
