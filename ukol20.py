import random

cislo = random.randrange(99)

def sude():
    if cislo%2 == 0:
        print("cislo je sude")
    else:
        print ("cislo je liche")

print (cislo)
sude()

# jak to udelat, aby program nacetl jakekoliv cislo bez omezeni nejake maximalni vyse cisla?
