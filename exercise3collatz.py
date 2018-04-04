# Martyna Miskiewicz
# The Collatz Cojencture:https://en.wikipedia.org/wiki/Collatz_conjecture

n = 125
print(n)
while n != 1:  #if number is odd 
  if n % 2 == 1:
    n = n * 3 + 1 
    print(n)
  elif n % 2 == 0:  #if number is even
    n = n // 2
    print(n) 
