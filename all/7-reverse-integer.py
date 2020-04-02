''' Antonio Pelayo March 8, 2020
Problem 7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this 
problem, assume that your function returns 0 when the reversed integer overflows.
'''

def reverse(x):
  result = ''
  sign = 1    # -1 if negative

  # Check if negative 
  if x < 0:   
    sign = -1
    result = str(x)[1:]    # String of x without negative sign
  else:
    result = str(x)
  
  result = sign * int(result[::-1])    # Reverse and turn to int

  # Handle overflow case
  if result > (2 ** 31) or result < -(2 ** 31):
    return 0

  return result

a = 123
b = -123
c = 120

print(reverse(a))
print(reverse(b))
print(reverse(c))
print(reverse(1534236469))