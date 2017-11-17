import random
name = []
place = []
loop = 0
print ("Hello, It's me your friendly neighbourhood spoderman")
print ("I was flying across NYC when I stumbled a small spoder that was abandoned by his parents just like me :(")
print ("So I decided that I will adopt him but I can't think of a name for it")
print ("So I'm giving you the ability to name my pet spoder, You will give me 5 names and I will choose it by random")
while loop <= 4 :
    spoder = input("What will you name me spoder?")
    name.append(spoder)
    loop = loop + 1
if loop >= 4:
        print("Spoderman's pet spoder will be called", random.choice(name))

while loop > 4:
    c = input("Where do you want to place spoder in?")
    place.append(c)
    loop = loop + 1
    if loop >= 8:
        print("Spoderman's pet spoder will live in ", random.choice(place))
        break
        

          
