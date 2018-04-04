# Martyna Miskiewicz
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Miskiewicz"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# My surname is Miskiewicz The first letter M is number 77 and the last letter z is number 122. 
# Then Fibonacci number 199 is 173402521172797813159685037284371942044301

# From what I understand, ord() converts a letter/character (M) (one string character) to a number/value (77). 
# This can be taken from a table called ASCII, which contains a list of characters that represent its values and vice versa chr().
