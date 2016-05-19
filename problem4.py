

#Problem Nr.4
#http://www.practicepython.org

print ("Problem 4")

x = 0
e = []
nummer = int(input("Type in a number.."))
l = range(1,nummer-1)
for i in l:
	if nummer%i == 0:
		e.append(i)
print ("The divisors of this number are",e)
