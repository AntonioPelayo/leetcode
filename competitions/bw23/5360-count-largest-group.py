''' Antonio Pelayo April 4, 2020
Problem: 5360. Count Largest Group 
Difficulty: Easy

Given an integer n. Each number from 1 to n is grouped according to the sum of 
its digits. 

Return how many groups have the largest size.

Example 1:
Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.

Example 2:
Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.

Example 3:
Input: n = 15
Output: 6

Example 4:
Input: n = 24
Output: 5

Constraints:
1 <= n <= 10^4
'''

def countLargestGroup(n):
    group_sizes = {}
 
    for i in range(1, n+1):
        # Compute the sum of i's digits
        digits = list(str(i))
        group = sum(int(d) for d in digits)   
            
        if group in group_sizes:
            group_sizes[group] += 1
        else:
            group_sizes[group] = 1
       
    largest_group_size = max(group_sizes.values())
    num_groups = 0

    for group in group_sizes:
        if group_sizes[group] == largest_group_size:
            num_groups += 1
            
    return num_groups

a = 13
b = 2
c = 15
d = 5
print(countLargestGroup(a))
print(countLargestGroup(b))
print(countLargestGroup(c))
print(countLargestGroup(d))