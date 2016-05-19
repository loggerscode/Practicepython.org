

#Problem Nr.3
#http://www.practicepython.org

print("Problem 3")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

print(a)
number = int(input("Type in a number..\nthe program will display you all numbers that are less than\nyour typed-in number in the list "))
print(a)
for i in a:
    if i < number:
        b.append(i)
print(b)
