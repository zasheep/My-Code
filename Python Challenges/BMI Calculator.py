print("Welcome to the BMI Calculator")
print("Lets see if your are underweight, normal or overweight")

weight = float(input("How much do you weight?(KG only)"))
height = float(input("How tall are you?(Meters only"))
BMI = (weight/height**2)

print ("Your BMI is" , BMI)

print ("If your BMI is less than 18, you are underweight")
print ("If your BMI is higher than 18.5 but less than 25, you are normal")
print ("If your BMI is higher than 25 but less than 30, you are overweight!")
print ("If your BMI is higher than 30, you should go to the doctor...you are obese")

