cislo_1 = int(input ("Zadej prvni cislo"))
cislo_2 = int(input ("Zadej druhe cislo"))
cislo_3 = int(input ("Zadej treti cislo"))

def soucet ():
    if cislo_1 + cislo_2 + cislo_3 > 10:
        print ("Soucet je vetsi, nez 10")
    else:
        print ("Soucet neni vetsi, nez 10")
soucet()
