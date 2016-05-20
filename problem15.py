

#Problem Nr. 15
#http://www.practicepython.org

word = input("Type in a sentence.. ")

def reverse_word(word):
  y = word.split()
  return " ".join(reversed(y))

print (reverse_word(word))
