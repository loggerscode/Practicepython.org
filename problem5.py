

#Problem Nr.5
#http://www.practicepython.org

print ("Problem 5")

a = [1, 1, 2, 3, 5, 8, 13 ,21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = a+b
c.sort()
d = set(c)

print(a)
print(b)
print("Now without duplicates: ", d)
