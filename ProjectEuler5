# Martyna Miskiewicz
# Problem 5 from Project Euler: https://projecteuler.net/problem=5 
# answer is 232792560

divisible = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
counter = 20

for number in range(counter, 999999999, counter): # for loop starts at 20 ends at 999999999 and it also increments by 20
    if all(number % n == 0 for n in divisible): # this condition checks if the number is divided by an element from the divisible list with no remainder
        print('solution equals to', number)
        break
