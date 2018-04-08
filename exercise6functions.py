# Martyna Miskiewicz
# Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial.
# Testin the factiorial numbers of 5, 7 and 10.

def sumall(until):   # defining the function
  sumuntil = 1       # sum of all the values - until 1
  for i in range(1, until + 1):  # range function 
      sumuntil = sumuntil * i
  return sumuntil # output of the function

print("The factorial of 5 equals: ", sumall(5))
print("The factorial of 7 equals: ", sumall(7))
print("The factorial of 10 equals: ", sumall(10))
