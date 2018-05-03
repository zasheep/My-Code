studentC = 30
coach = 550
x = 0
freeticket=0
paidlist = []
notpaidlist = []
while x<1:
    nostudent = int(input("How many students will attend?"))
    if nostudent <= 0:
        print("Enter a valid number")
        x = 0
    if nostudent >45:
        print("Enter a valid number")
        x = 0
    elif nostudent>0:
        if nostudent<11:
            freeticket =0
            x =+1
        elif nostudent<22:
            freeticket =+1
            x =+1
        elif nostudent< 33:
            freeticket =+2
            x +=1
        elif nostudent<44:
            freeticket =+3
            x +=1
        elif nostudent<45:
            freeticket =+4
            x += 1

print("you get", freeticket, "free ticket")
studentcost = coach + ((studentC*nostudent) - (freeticket*studentC))
print("total student cost is", studentcost)

#end of task 1
paidstudents = 0
notpaidstudents = 0
for i in range(nostudent):
    paid = input("Did this student pay?(y/n)")
    if paid == "y":
        paidstudents =+1
    elif paid == "n":
        notpaidstudents =+1

for i in range(paidstudents):
    name = input("(for paid)What is the students name?")
    paidlist.append(name)
for i in range(notpaidstudents):
    name2 = input("(for notpaid)What is the students name?")
    notpaidlist.append(name2)

print(paidlist)
print(notpaidlist)

    
