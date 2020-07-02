''' Antonio Pelayo July 1, 2020
Problem: 441. Arranging Coins
Difficulty: Easy

You have a total of n coins that you want to form in a staircase shape, where 
every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤
Because the 3rd row is incomplete, we return 2.

Example 2:
n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
Because the 4th row is incomplete, we return 3.
'''

def arrangeCoins(n: int) -> int:
    full_rows = 0
    row_len = 1
        
    while n >= row_len:
        n -= row_len
        row_len += 1
            
        if n >= 0:
            full_rows += 1
        
    return full_rows
            

a = 5
b = 8

print(arrangeCoins(a))
print(arrangeCoins(b))