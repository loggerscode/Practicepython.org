

#Problem Nr. 9
#http://www.practicepython.org

import random

x =(random.randint(1,9))

eingabe = int(input("Guess the number (1-9).. "))
if eingabe < x:
    print ("underrated..")
if eingabe > x:
    print ("overrated..")
if eingabe == x:
    print ("right guessed..")
print ("The number was:" , x)
