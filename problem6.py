

#Problem Nr.6
#http://www.practicepython.org

print("Problem 6")
s = input("Type in a single word..")
s = s.casefold()
revs = reversed(s)
if list(s) == list(revs):
        print("This is a palindrom..")
else:
        print("This is not a palindrom..")
