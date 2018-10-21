for cislo in range (1, 101):
    if cislo%3 == 0 and cislo%5 == 0:
        cislo = str(cislo)
        print (cislo.replace(cislo, "bum-bac"))
    elif cislo%3 == 0:
        cislo = str(cislo)
        print (cislo.replace(cislo,"bum"))
    elif cislo%5 == 0:
        cislo = str(cislo)
        print (cislo.replace(cislo,"bac"))
    else:
        print (cislo)
