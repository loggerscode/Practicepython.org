

#Problem Nr. 7
#http://www.practicepython.org

a = [1,4,9,16,25,36,49,64,81,100]
e = []

new_list = [i for i in a if i%2 == 0]        #short version with a
print (new_list)                             #list comprehension

# for i in a:
#     if i%2 == 0:
#         e.append(i)                   long version
# print (e)
