pocet_radku = int (input ("Zadej pocet radku \n"))

print ("\nukol05: \n")
for pocet_radku in range (4):
  print ("a")

print ("\nukol06: \n")
for pocet_radku in range (4):
    print ("radek", pocet_radku)

print ("\nukol08: \n")
cislo = int (input ("Zadej cislo, ktere se bude mocnit na druhou \n"))
for cislo in range(4):
    print ("{} na druhou je {}". format(cislo, cislo**2))

print ("\nukol09: \n")
for new_lines in range(pocet_radku):
    print ("\n".strip())
    for x in range (pocet_radku):
        print ("x", end="")

print ("\nukol10: \n")
for cislo in range(pocet_radku):
    print ("\n".strip())
    for nasobek in range (pocet_radku):
        print (cislo*nasobek, end="")

print ("\nukol11: \n")
for nasobek_x in range (pocet_radku):
    print ("x"*nasobek_x)

print ("\nukol12: \n")
for radek in range (1,pocet_radku):
    if radek == 1:
        print ("prvni radek")
    else:
        print ("neni prvni")

print ("\nukol13: \n")
for new_lines in range(pocet_radku):
    print ("\n".strip())
    for x in range (pocet_radku):
        if new_lines == 0 or new_lines == pocet_radku - 1:
            print ("x", end="")
        elif x in range (1, pocet_radku -1):
            print (" ", end="")
        else:
            print ("x", end="")
