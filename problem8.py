

#Problem Nr. 8
##http://www.practicepython.org

print("Problem 8")

neuespiel = True

while neuespiel:
    zuga = input("Player A's turn.. ").casefold()
    zugb = input("Player B's turn.. ").casefold()                                      #lange Version
    if zuga == zugb:
            print("draw")
    if (zuga == "stone" and zugb == "scissors") or (zuga == "scissors" and zugb == "paper") or (zuga == "paper" and zugb == "stone"):
            print ("Player A has won!")
    else:
            print ("Player B has won!")

    eingabe = input("Begin a new game? Y/N ")
    neuespiel = eingabe.casefold() == "y"
