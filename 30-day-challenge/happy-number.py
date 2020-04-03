''' Antonio Pelayo April 2, 2020
Problem: 202 Happy Number
Difficulty: Easy

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any 
positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), or it 
loops endlessly in a cycle which does not include 1. Those numbers for which 
this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true

Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

def isHappy(n):
    nums_seen = []

    while n not in nums_seen:
        if n == 1:
            return True      # Number is happy
        nums_seen.append(n)  # Add to seen list

        # Get next sum of square digits
        digits = list(str(n))
        n = 0
        n = sum(int(d) ** 2 for d in digits)  # Next number in series

    # Broke out of loop, seen n before, infinite loop
    return False

a = 19
print(isHappy(a))
