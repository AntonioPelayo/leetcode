''' Antonio Pelayo April 4, 2020
Problem: 1404 Number of Steps to Reduce a Number in Binary Representation to One
Difficulty: Medium

Given a number s in their binary representation. Return the number of steps to 
reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.
If the current number is odd, you have to add 1 to it.
It's guaranteed that you can always reach to one for all testcases.

Example 1:
Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  

Example 2:
Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  

Example 3:
Input: s = "1"
Output: 0

Constraints:
1 <= s.length <= 500
s consists of characters '0' or '1'
s[0] == '1'
'''

def numSteps(s):
    s = list(int(d) for d in s)[::-1]
    steps = 0
    num = 0

    # Convert from binary to decimal
    for power in range(len(s)):
        if s[power] == 0:
            num += 0
        else:
            num += pow(2, power)

    while num != 1:
        if num % 2 == 0:
            # Even
            num = num // 2
        else:
            # Odd
            num += 1
        steps += 1

    return steps

# Examples
a = '1101'
b = '10'
c = '1'

# Failed cases
d = "1111011110000011100000110001011011110010111001010111110001"

print(numSteps(a))
print(numSteps(b))
print(numSteps(c))
print(numSteps(d))