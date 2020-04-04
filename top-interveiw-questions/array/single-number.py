''' Antonio Pelayo April 1, 2020
Problem: 136. Single Number
Difficulty: Easy

Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it 
without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
'''

def singeNumber(nums):
    # Twice the sum of the set minus the sum of nums will result in the non
    # duplicate number
    nums_set = set(nums)

    single_num = (sum(nums_set) * 2) - sum(nums)

    return single_num


a = [2, 2, 1]
b = [4, 1, 2, 1, 2]

print(singeNumber(a))
print(singeNumber(b))