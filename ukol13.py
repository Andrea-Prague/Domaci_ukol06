for new_lines in range(6):
    print ("\n".strip())
    for x in range (6):
        if new_lines == 0 or new_lines == 5:
            print ("x", end="")
        elif x == 1 or x == 2 or x == 3 or x == 4:
            print (" ", end="")
        else:
            print ("x", end="")
