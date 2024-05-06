a = 'all '
b =  'work '
c = 'and '
d = 'no '
e = 'play '
f = 'makes '
g= 'Jack '
h = 'a '
i = 'dull '
j = 'boy.'
bruce = 6
r = 1.08
n = 12
p = 10000

print(a +b +c +d +e +f +g +h +i + j)
print (6*(1-2))

print (bruce+4)

t = int(input("How many years do you want to leave $10000 in the bank?"))

total = n*t
x = (((r/n)+1)**total)
y = x*p
print(y)

print(5%2)
print(9%5)
print(15%12)
print(12%15)
print(6%6)
print(0%7)
print(7%1)


currenttime = int(input("What time is it?(0-24)"))
if currenttime > 24:
    print("that's not allowed")
    exit()
waiting = int(input("How many hours do you want to wait?"))
while waiting >= 24:
    waiting = (waiting-24)
    currenttime = (currenttime + waiting)

print ("the time is", currenttime)



