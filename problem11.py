

#Problem Nr. 11
#http://www.practicepython.org

input_number = int(input("Type in a number.. "))

if input_number > 1:
    for i in range(2,input_number):
        if input_number%i == 0:
            print(input_number, "is not a prime number..")
            break
    else:
        print(input_number, "is a prime number..")
else:
    print(input_number, "is not a prime number..")
