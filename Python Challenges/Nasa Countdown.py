import time
C = int(input("How long do you want your countdown to be?"))
while C >= 1:
    print (C - 1)
    C -= 1
    time.sleep(1)
