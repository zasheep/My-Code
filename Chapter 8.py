import string
prefixes = "JKLMNOPQ"
suffix = "uack"

for letter in prefixes:
    print(letter + suffix)

b = 0
def count_letters(f):
    b = len(f)
    return b

lenn = count_letters("boo")
print(lenn)

def reverse(p):
    reversedstring = ((p)[::-1])
    return reversedstring

p = input("reverse your sentence")
print (reverse(p))

def mirror (q):
    mirrored = (q)+((q)[::-1])
    return mirrored

q = input("mirror your sentence")
print (mirror(q))



