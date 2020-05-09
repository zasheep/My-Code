#201458599, Aminuddin_Zariff-CA01.py
#October, 2019
#Sequencing and I/O control of strings and numbers to calculate and output the draft of a barge

length = float(input("Enter the length of the Barge:")) #Following the house style, Firstly we get inputs in
breadth = float(input("Enter the breadth of the Barge:"))
height = float(input("Enter the height of the Barge:"))

weight_Iron = 1.06  #Calculations are then done
surface_Area = (2*breadth*height) + (2*length*height) + (breadth*length)
mass = weight_Iron*surface_Area
draft = mass/(length*breadth)
height_WaterLine = height-draft

print("")  #Output, Line 15 is an empty line to prevent the user visually seeing a wall of text
print("Length of Barge:",length)
print("Breadth of Barge:",breadth)
print("Height of Barge:",height)
print("Surface Area:",surface_Area)
print("Mass:",(mass),"Kg")
print(f"Draft:{draft:.2f}")  #I formatted my float to a string for line 21 & 22 to 2 d.p so it doesn't go on forever
print(f"Height of Barge that is above the water line:{height_WaterLine:.2f}")

